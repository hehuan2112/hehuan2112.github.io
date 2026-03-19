<script setup>
const props = defineProps({
  isMobile: { type: Boolean, default: false },
})

const emit = defineEmits(['navigate'])

const navItems = [
  { href: '#news', icon: 'bi-newspaper', label: 'News' },
  { href: '#publications', icon: 'bi-journal-richtext', label: 'Publications' },
  { href: '#projects', icon: 'bi-journal-code', label: 'Projects' },
  { href: '#tools', icon: 'bi-tools', label: 'Tools' },
  { href: '#patents', icon: 'bi-file-lock', label: 'Patents' },
  { href: '#work_exp', icon: 'bi-buildings', label: 'Work Exp.' },
  { href: '#community_services', icon: 'bi-people', label: 'Services' },
  { href: '#awards', icon: 'bi-award', label: 'Awards' },
]

function onNavClick() {
  emit('navigate')
}
</script>

<template>
  <!-- Desktop nav (rendered in right column, sticky) -->
  <nav v-if="!isMobile" class="navigation">
    <ul class="nav-list">
      <li v-for="item in navItems" :key="item.href">
        <a :href="item.href" target="_self">
          <i :class="['bi', item.icon]"></i>
          {{ item.label }}
        </a>
      </li>
    </ul>
  </nav>

  <!-- Mobile nav (dropdown, shown when toggler clicked) -->
  <ul v-else class="nav-list">
    <li v-for="item in navItems" :key="item.href">
      <a :href="item.href" target="_self" @click="onNavClick">
        <i :class="['bi', item.icon]"></i>
        {{ item.label }}
      </a>
    </li>
  </ul>
</template>
