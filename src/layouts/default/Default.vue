<template>
  <v-app>
    

    <v-main>
      <router-view />
      <v-bottom-navigation class="height: 150px">
        <div class="d-flex w-100  justify-space-evenly">
          
        <v-btn class="d-flex flex-grow-1" value="podcasts"  style="font-size: xx-small; min-width: 0; height: 56px ;" :to="{name: 'Podcasts'}">
          <v-icon>mdi-dots-grid</v-icon>
      
          <span></span>
        </v-btn>
      
        <v-btn  class="d-flex flex-grow-1"  value="filters" style="font-size:xx-small; min-width: 0; height: 56px;width: auto" :to="{name: 'Filters'}">
          <v-icon>mdi-filter-multiple</v-icon>
      
          <span></span>
        </v-btn>
      
        
    
        <v-btn class="d-flex flex-grow-1"   value="profile"  style="font-size:xx-small;min-width: 0 ;height: 56px;width:calc(var(--variable-width) + 20px)" :to="{name: 'Profile'}">
          <v-icon>mdi-account</v-icon>
      
          <span></span>
        </v-btn>
    
        <v-btn class="d-flex flex-grow-1"  value="player" style="font-size:xx-small; min-width: 0; height: 56px;width:calc(var(--variable-width) + 20px)" :to="{name: 'Player'}">
          <v-icon>mdi-play</v-icon>
      
          <span></span>
        </v-btn>
  
        <v-btn  class="d-flex flex-grow-1"  value="queue" style="font-size:xx-small; min-width: 0; height: 56px;" :to="{name: 'Queue'}">
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
