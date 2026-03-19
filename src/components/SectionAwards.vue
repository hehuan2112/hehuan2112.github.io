<script setup>
defineProps({
  awards: { type: Array, required: true },
})
</script>

<template>
  <h2 class="section-header" id="awards">
    <i class="bi bi-award"></i> Awards
  </h2>

  <div
    v-for="(award, i) in awards"
    :key="i"
    class="award-item"
  >
    <div class="award-date">{{ award.date }}</div>
    <div class="award-content">
      <b>{{ award.title }}</b><br>
      <span style="color:#555; font-size:0.92em;">{{ award.organization }}</span>
      <template v-if="award.location">
        <span style="color:#888; font-size:0.88em;"> · {{ award.location }}</span>
      </template>
    </div>
  </div>
</template>
