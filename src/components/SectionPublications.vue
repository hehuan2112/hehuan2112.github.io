<script setup>
import { computed, onBeforeUnmount, ref } from 'vue'
import { getYear, highlightMe } from '../utils/markdown.js'

const props = defineProps({
  publications: { type: Array, required: true },
})

const emit = defineEmits(['cite'])
const identifierTypes = new Set(['pmid', 'pmcid', 'doi'])
const copiedLink = ref(null)
let copyResetTimer

// Build sorted year list: newest first, then "Before 2018"
const years = computed(() => {
  const yearSet = new Set()
  for (const p of props.publications) {
    const y = getYear(p.date)
    if (y && y >= 2018) yearSet.add(y)
  }
  const sorted = Array.from(yearSet).sort((a, b) => b - a)
  sorted.push('Before 2018')
  return sorted
})

function pubsForYear(year) {
  if (year === 'Before 2018') {
    return props.publications.filter(p => {
      const y = getYear(p.date)
      return !y || y < 2018
    })
  }
  return props.publications.filter(p => getYear(p.date) === year)
}

function imgSrc(thumb) {
  return thumb ? `/file/${thumb}` : null
}

function linkClass(type) {
  return `tag-link tag-link-${type}`
}

function isIdentifier(type) {
  return identifierTypes.has(type?.toLowerCase())
}

async function copyIdentifier(link) {
  const identifier = link[0]

  try {
    await navigator.clipboard.writeText(identifier)
  } catch {
    const textarea = document.createElement('textarea')
    textarea.value = identifier
    textarea.style.position = 'fixed'
    textarea.style.opacity = '0'
    document.body.appendChild(textarea)
    textarea.select()
    document.execCommand('copy')
    textarea.remove()
  }

  copiedLink.value = link
  clearTimeout(copyResetTimer)
  copyResetTimer = setTimeout(() => {
    copiedLink.value = null
  }, 1500)
}

onBeforeUnmount(() => clearTimeout(copyResetTimer))
</script>

<template>
  <div>
    <div v-for="year in years" :key="year">
      <template v-if="pubsForYear(year).length > 0">
        <h3 class="pub-year">{{ year }}</h3>
        <div
          v-for="(pub, idx) in pubsForYear(year)"
          :key="idx"
          class="publication"
        >
          <!-- Thumbnail -->
          <div class="pub-image">
            <img
              v-if="pub.thumb"
              :src="imgSrc(pub.thumb)"
              :alt="pub.title"
              loading="lazy"
              @error="e => e.target.style.display='none'"
            >
          </div>

          <!-- Content -->
          <div class="pub-content">
            <b class="pub-title">{{ pub.title }}</b>
            <br>
            <span
              class="pub-authors"
              v-html="highlightMe(pub.authors)"
            ></span>
            <br>
            <i>
              <span class="pub-source">{{ pub.source }}</span>
              <template v-if="pub.place">, <span class="pub-place">{{ pub.place }}</span></template>,
              <span class="pub-date">{{ pub.date }}</span>
            </i>
            <br>
            <span class="pub-links">
              <span
                v-for="(link, li) in pub.links"
                :key="li"
                :class="{ 'identifier-link': isIdentifier(link[2]) }"
              >
                <a
                  :href="link[1]"
                  :class="linkClass(link[2])"
                  target="_blank"
                  rel="noopener"
                >{{ link[0] }}</a>
                <button
                  v-if="isIdentifier(link[2])"
                  class="tag-link identifier-copy"
                  type="button"
                  :title="`Copy ${link[2].toUpperCase()}`"
                  :aria-label="`Copy ${link[2].toUpperCase()} ${link[0]}`"
                  @click="copyIdentifier(link)"
                >
                  <i
                    class="bi"
                    :class="copiedLink === link ? 'bi-check2' : 'bi-copy'"
                    aria-hidden="true"
                  ></i>
                  {{ copiedLink === link ? 'Copied' : 'Copy' }}
                </button>
              </span>
            </span>
            <a
              class="tag-link tag-link-cite"
              href="javascript:void(0)"
              title="Cite this work"
              @click.prevent="emit('cite', pub)"
            >
              <i class="bi bi-quote"></i> Cite
            </a>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>
