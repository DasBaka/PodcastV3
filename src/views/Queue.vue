<template>
  <div class="queue">
    <v-app-bar :elevation="5">
      <v-app-bar-title>now playing</v-app-bar-title>
      <template v-slot:append>
        <v-btn icon="mdi-pause"></v-btn>
      </template>
    </v-app-bar>
    <v-list lines="one">
      <v-list-item
        v-for="n in 25"
        :key="n"
        class="px-2">
        <div class="d-flex w-100 justify-space-between pa-2">
          <div class="d-flex ga-2 flex-grow-1">
            <v-img
              :max-width="50"
              aspect-ratio="1/1"
              cover
              src="@/assets/daily.jpg"></v-img>
            <div>
              <p style="font-size: xx-small">nr. & date</p>
              <p style="font-size: small">episode titel kk</p>
              <p style="font-size: xx-small">dlstate&lenghth</p>
            </div>
          </div>

          <v-btn icon="mdi-arrow-expand-down" size="x-small">
            
          </v-btn>
        </div>

        <v-divider
          :thickness="2"
          class="border-opacity-50"></v-divider>
      </v-list-item>
    </v-list>
  </div>
</template>

<script lang="ts" setup></script>
