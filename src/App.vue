<script setup>
import { ref } from 'vue'
import data from './data/index.js'
import { md } from './utils/markdown.js'

import ProfileSidebar from './components/ProfileSidebar.vue'
import MainNav from './components/MainNav.vue'
import SectionPublications from './components/SectionPublications.vue'
import SectionProjects from './components/SectionProjects.vue'
import SectionTools from './components/SectionTools.vue'
import SectionPatents from './components/SectionPatents.vue'
import SectionWorkExp from './components/SectionWorkExp.vue'
import SectionServices from './components/SectionServices.vue'
import SectionAwards from './components/SectionAwards.vue'
import CitationModal from './components/CitationModal.vue'

const navbarOpen = ref(false)
const citationPub = ref(null)

function toggleNavbar() {
  navbarOpen.value = !navbarOpen.value
}

function closeNavbar() {
  navbarOpen.value = false
}

function backToTop() {
  const wrapper = document.querySelector('.wrapper')
  if (wrapper) wrapper.scrollTo({ top: 0, behavior: 'smooth' })
}

function onCite(pub) {
  citationPub.value = pub
}

function closeCitation() {
  citationPub.value = null
}
</script>

<template>
  <!-- Mobile hamburger button -->
  <button class="navbar-toggler" @click="toggleNavbar" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <!-- Mobile nav dropdown -->
  <div v-if="navbarOpen" class="mobile-nav-dropdown">
    <MainNav :is-mobile="true" @navigate="closeNavbar" />
  </div>

  <!-- Back-to-top button -->
  <button class="back-to-top" @click="backToTop" title="Back to Page Top">
    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
      <polygon points="16,14 6,24 7.4,25.4 16,16.8 24.6,25.4 26,24" fill="currentColor"/>
      <rect x="4" y="8" width="24" height="2" fill="currentColor"/>
    </svg>
  </button>

  <!-- Main scrollable wrapper -->
  <div class="wrapper">
    <div class="container">
      <div class="layout-row">
        <!-- Left sidebar: profile + news -->
        <div id="left" class="column-left">
          <ProfileSidebar :me="data.me" :news="data.news" />
        </div>

        <!-- Right content -->
        <div id="right" class="column-right">
          <!-- About text -->
          <div id="about" class="about-section" v-html="md(data.me.about)"></div>

          <!-- Anchor for publications (nav lands here) -->
          <span id="publications" class="section-anchor"></span>

          <!-- Sticky navigation bar (desktop) -->
          <MainNav />

          <!-- Content sections -->
          <SectionPublications :publications="data.publications" @cite="onCite" />
          <SectionProjects :projects="data.projects" />
          <SectionTools :tools="data.tools" />
          <SectionPatents :patents="data.patents" />
          <SectionWorkExp :work-exp="data.workExp" />
          <SectionServices :academic-exp="data.academicExp" />
          <SectionAwards :awards="data.awards" />

          <p style="margin-bottom: 3em;">&nbsp;</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Citation modal (teleported to body) -->
  <Teleport to="body">
    <CitationModal v-if="citationPub" :pub="citationPub" @close="closeCitation" />
  </Teleport>
</template>
