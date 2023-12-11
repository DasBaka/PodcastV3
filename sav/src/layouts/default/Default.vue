<template>
  <v-app>
    

    <v-main>
      <router-view />
      <v-bottom-navigation>
        <v-btn value="podcasts" :to="{name: 'Podcasts'}">
          <v-icon>mdi-dots-grid</v-icon>
      
          <span>Podcasts</span>
        </v-btn>
      
        <v-btn value="filters" :to="{name: 'Filters'}">
          <v-icon>mdi-filter-multiple</v-icon>
      
          <span>Filters</span>
        </v-btn>
      
        
    
        <v-btn value="profile" :to="{name: 'Profile'}">
          <v-icon>mdi-account</v-icon>
      
          <span>Profile</span>
        </v-btn>
    
        <v-btn value="player" :to="{name: 'Player'}">
          <v-icon>mdi-play</v-icon>
      
          <span>Player</span>
        </v-btn>
  
        <v-btn value="queue" :to="{name: 'Queue'}">
          <v-icon>mdi-format-list-bulleted-square</v-icon>
      
          <span>Queue</span>
        </v-btn>
    
      </v-bottom-navigation>
    </v-main>
  </v-app>
</template>

<script lang="ts" setup>


 
  
</script>
