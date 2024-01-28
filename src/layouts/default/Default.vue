<template>
  <v-app>
    

    <v-main>
      <router-view />
      <v-bottom-navigation class="height: 150px">
        <div class="d-flex w-100  justify-space-evenly">
        <v-btn class="d-flex" value="podcasts"  style="font-size: x-small" :to="{name: 'Podcasts'}">
          <v-icon>mdi-dots-grid</v-icon>
      
          <span></span>
        </v-btn>
      
        <v-btn value="filters" style="font-size: x-small" :to="{name: 'Filters'}">
          <v-icon>mdi-filter-multiple</v-icon>
      
          <span></span>
        </v-btn>
      
        
    
        <v-btn  value="profile"  style="font-size: x-small" :to="{name: 'Profile'}">
          <v-icon>mdi-account</v-icon>
      
          <span></span>
        </v-btn>
    
        <v-btn  value="player" style="font-size: x-small" :to="{name: 'Player'}">
          <v-icon>mdi-play</v-icon>
      
          <span></span>
        </v-btn>
  
        <v-btn  value="queue" style="font-size: xx-small" :to="{name: 'Queue'}">
          <v-icon>mdi-format-list-bulleted-square</v-icon>
      
          <span></span>
        </v-btn>
      </div>
      </v-bottom-navigation>
    </v-main>
  </v-app>
</template>

<script lang="ts" setup>


 
  
</script>
