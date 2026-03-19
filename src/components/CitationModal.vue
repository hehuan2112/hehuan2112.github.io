<script setup>
import { ref, computed } from 'vue'
import { formatCitation } from '../utils/markdown.js'

const props = defineProps({
  pub: { type: Object, required: true },
})

const emit = defineEmits(['close'])

const copied = ref(false)

const citationHtml = computed(() => {
  const { title, source, date, place, type } = props.pub
  let base = formatCitation(props.pub)
  // For conference pubs, insert place before date
  if (type === 'conference' && place) {
    base = base.replace(`. ${date}.`, `, ${place}. ${date}.`)
  }
  return base
})

const citationText = computed(() => {
  return citationHtml.value.replace(/<em>(.*?)<\/em>/g, '$1').replace(/<[^>]+>/g, '')
})

function copyToClipboard() {
  navigator.clipboard.writeText(citationText.value).then(() => {
    copied.value = true
    setTimeout(() => { copied.value = false }, 2000)
  })
}

function onOverlayClick(e) {
  if (e.target === e.currentTarget) emit('close')
}
</script>

<template>
  <div class="modal-overlay" @click="onOverlayClick">
    <div class="modal-container" role="dialog" aria-modal="true">
      <div class="modal-header">
        <h3>Citation</h3>
        <button class="modal-close" @click="emit('close')" aria-label="Close">&#x2715;</button>
      </div>
      <div class="citation-text" v-html="citationHtml"></div>
      <div class="modal-actions">
        <button class="btn" @click="emit('close')">Close</button>
        <button class="btn btn-primary" @click="copyToClipboard">
          {{ copied ? 'Copied!' : 'Copy to Clipboard' }}
        </button>
      </div>
    </div>
  </div>
</template>
