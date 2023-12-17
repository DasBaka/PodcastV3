<template>
<div class="text-body-2 font-weight-light mb-n1 text-center">Podcast titel</div>
<v-container class="fill-height">

    <v-responsive class="align-center text-center fill-height">
        <v-img src="@/assets/daily.jpg" />

        <div class="text-body-2 font-weight-light mb-n1">Episode titel</div>

        <v-row class="d-flex align-center justify-center">
            <v-btn value="prevChapter" variant="plain">
                <v-icon>mdi-skip-previous</v-icon>

            </v-btn>
            <div class="text-caption">Chapter titel</div>
            <v-btn value="nextChapter" variant="plain">
                <v-icon>mdi-skip-next</v-icon>
            </v-btn>
        </v-row>

        <v-slider></v-slider>
        <v-row value>

            <v-row justify="space-between">
                <div>00:00:00</div>
                
                <div>00:00:00</div>
            </v-row>
        </v-row>

        <v-row align-content="end" justify="center">
            <v-btn value="back" stacked variant="plain" size="large">
                <v-icon>mdi-arrow-u-left-top</v-icon>
                <span>15s</span>

            </v-btn>

            <v-btn value="play" stacked variant="plain" size="large">
                <v-icon>mdi-play</v-icon>

            </v-btn>

            <v-btn value="forward" stacked variant="plain" size="large">
                <v-icon>mdi-arrow-u-right-top</v-icon>
                <span>15s</span>

            </v-btn>
        </v-row>

        <div class="py-14" />
    </v-responsive>

</v-container>
</template>

<script lang="ts" setup>

  </script>
