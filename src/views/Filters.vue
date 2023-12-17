<template>
<div class="filters">
    
    <v-app-bar :elevation="5">
        <v-app-bar-title>filters</v-app-bar-title>
        <template v-slot:append>
            <v-btn icon="mdi-filter-plus"></v-btn>
        </template>
    </v-app-bar>
    <v-list lines="two">
        <v-list-item :title="'t&t'" subtitle="x Episodes">
            <v-divider :thickness="2" class="border-opacity-50">
        </v-divider></v-list-item>
        <v-list-item :title="'tapcaf'" subtitle="x Episodes">
            <v-divider :thickness="2" class="border-opacity-50"></v-divider>
        </v-list-item>
    </v-list>
</div>
</template>

<script lang="ts" setup>

</script>
