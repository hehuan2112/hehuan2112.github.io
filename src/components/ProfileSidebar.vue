<script setup>
import { mdInline } from '../utils/markdown.js'

defineProps({
  me: { type: Object, required: true },
  news: { type: Array, required: true },
})
</script>

<template>
  <div id="info">
    <img src="/img/me3.jpg" alt="Huan He" @error="e => e.target.style.display='none'">
    <p>
      <span class="name">Huan He</span><br>
      <span class="email">{{ me.email }}</span><br>
      <span class="institution">{{ me.institution }}</span>
    </p>
  </div>

  <hr>

  <div class="news-section">
    <h4 id="news">NEWS</h4>
    <div
      v-for="(item, i) in news"
      :key="i"
      class="news-item"
    >
      <span class="news-date">{{ item.date }}: </span><span v-html="mdInline(item.text)"></span>
    </div>
  </div>
</template>
