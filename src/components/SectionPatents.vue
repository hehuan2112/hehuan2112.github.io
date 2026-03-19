<script setup>
defineProps({
  patents: { type: Array, required: true },
})
</script>

<template>
  <h2 class="section-header" id="patents">
    <i class="bi bi-file-lock"></i> Patents
  </h2>

  <div
    v-for="(pat, i) in patents"
    :key="i"
    class="patent"
  >
    <div class="patent-id">
      <span>{{ pat.pid }}</span><br>
      <span style="font-size:0.85em; color:#999;">{{ pat.pid2 }}</span>
    </div>
    <div class="patent-content">
      <b>{{ pat.title }}</b><br>
      <i style="font-size:0.9em; color:#555;">{{ pat.subtitle }}</i><br>
      <span style="color:#666;">{{ pat.authors }}</span>
    </div>
  </div>
</template>
