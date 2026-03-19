<script setup>
defineProps({
  academicExp: { type: Array, required: true },
})
</script>

<template>
  <h2 class="section-header" id="community_services">
    <i class="bi bi-people"></i> Community Services
  </h2>

  <div
    v-for="(cat, i) in academicExp"
    :key="i"
    class="service-category"
  >
    <h4>{{ cat.category }}</h4>
    <ul>
      <li v-for="(item, j) in cat.items" :key="j">{{ item }}</li>
    </ul>
  </div>
</template>
