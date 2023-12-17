<template>
<div class="queue">
    <v-app-bar :elevation="5">
        <v-app-bar-title>now playing</v-app-bar-title>
        <template v-slot:append>
            <v-btn icon="mdi-pause"></v-btn>
        </template>
    </v-app-bar>
    <v-list lines="one">
        <v-list-item v-for="n in 25" :key="n">

            <v-row>
                <v-col cols="2">
                    <v-img :max-width="50" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                </v-col>
                <v-col>
                    <div style="font-size:xx-small">nr. & date</div>
                    <div style="font-size:small">episode titel kk</div>
                    <div style="font-size:xx-small">dlstate&lenghth</div>
                </v-col>
                <v-col justify="end">
                    <v-btn icon="mdi-pan-vertical"></v-btn>
                </v-col>
            </v-row>

           

            <v-divider :thickness="2" class="border-opacity-50"></v-divider>
        </v-list-item>
    </v-list>
</div>
</template>

<script lang="ts" setup>

</script>
