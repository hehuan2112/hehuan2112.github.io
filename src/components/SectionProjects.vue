<script setup>
import { md } from '../utils/markdown.js'

defineProps({
  projects: { type: Array, required: true },
})
</script>

<template>
  <h2 class="section-header" id="projects">
    <i class="bi bi-journal-code"></i> Projects
  </h2>

  <div
    v-for="(proj, i) in projects"
    :key="i"
    class="project"
  >
    <div class="project-image">
      <span class="project-date">{{ proj.date }}</span>
      <img
        v-if="proj.thumb"
        :src="`/file/${proj.thumb}`"
        :alt="proj.title"
        loading="lazy"
        @error="e => e.target.style.display='none'"
      >
    </div>

    <div class="project-content">
      <b>{{ proj.title }}</b><br>
      <i>{{ proj.organization }}, {{ proj.location }}</i><br>
      <div v-html="md(proj.description)"></div>
      <template v-if="proj.links && proj.links.length">
        Links:
        <a
          v-for="(link, li) in proj.links"
          :key="li"
          :href="link[1]"
          :class="`tag-link tag-link-${link[2]}`"
          target="_blank"
          rel="noopener"
        >{{ link[0] }}</a>
      </template>
    </div>
  </div>
</template>
