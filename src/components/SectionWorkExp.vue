<script setup>
defineProps({
  workExp: { type: Array, required: true },
})
</script>

<template>
  <h2 class="section-header" id="work_exp">
    <i class="bi bi-buildings"></i> Work Experience
  </h2>

  <div
    v-for="(job, i) in workExp"
    :key="i"
    class="work-item"
  >
    <div class="work-date">
      {{ job.date_start }} –<br>{{ job.date_end }}
    </div>
    <div class="work-content">
      <b>{{ job.title }}</b><br>
      <span style="color:#555;">{{ job.organization }}</span>
    </div>
  </div>
</template>
