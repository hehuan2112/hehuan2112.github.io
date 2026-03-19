<script setup>
defineProps({
  tools: { type: Array, required: true },
})
</script>

<template>
  <h2 class="section-header" id="tools">
    <i class="bi bi-tools"></i> Tools
  </h2>

  <div class="tools-grid">
    <div
      v-for="(tool, i) in tools"
      :key="i"
      class="tool-item"
    >
      <div class="tool-image">
        <img
          v-if="tool.thumb"
          :src="`/file/${tool.thumb}`"
          :alt="tool.title"
          loading="lazy"
          @error="e => e.target.style.display='none'"
        >
      </div>
      <b>{{ tool.title }}</b><br>
      {{ tool.description }}<br>
      <template v-if="tool.homepage">
        <a :href="tool.homepage" class="tag-link tag-link-demo" target="_blank" rel="noopener">Homepage</a>
      </template>
      <template v-if="tool.repository">
        | <a :href="tool.repository" class="tag-link tag-link-demo" target="_blank" rel="noopener">Repository</a>
      </template>
    </div>
  </div>
</template>
