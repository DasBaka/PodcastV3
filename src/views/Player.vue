<template>
<div class="text-h6 mb-n1 text-center pt-2">Epsode titel</div>
<v-container class="fill-height px-0 pt-0">

    <v-responsive class="align-center text-center fill-height">
        <div class:="d-flex w-100 pa-6">
        <v-img src="@/assets/daily.jpg"/>
        </div>

        <div class="text-body-2 font-weight-light mb-n1 py-2">Podcast titel</div>

        <v-row class="d-flex align-center justify-center">
            <v-btn value="prevChapter" variant="plain">
                <v-icon>mdi-skip-previous</v-icon>

            </v-btn>
            <div class="text-caption">Chapter titel</div>
            <v-btn value="nextChapter" variant="plain">
                <v-icon>mdi-skip-next</v-icon>
            </v-btn>
        </v-row>
        <div class="d-flex w-100 px-3">
            <v-slider />
        </div>
        <div class="d-flex w-100 justify-space-between px-1">
            <div>00:00:00</div>

            <div>00:00:00</div>

        </div>
        <div class="py-2" />
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
        <div class="py-2" />
        <div class="d-flex w-100 px-1">
            <v-sheet>
                Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

                Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet,
            </v-sheet>
        </div>
    </v-responsive>

</v-container>
</template>

<script lang="ts" setup>

  </script>
