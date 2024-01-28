<template>
<div class="podcasts">

    <v-app-bar :elevation="5">
        <v-app-bar-title>podcasts</v-app-bar-title>
        <template v-slot:append>
            <v-btn append-icon="mdi-rss-box" variant="tonal">add</v-btn>
            <v-btn icon="mdi-folder-plus"></v-btn>
        </template>
    </v-app-bar>
    <v-expansion-panels>

        <v-expansion-panel title="🕓" text="">

            <v-expansion-panel-text>
                <div class="d-flex w-100 justify-space-between">
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>

                </div>

            </v-expansion-panel-text>
        </v-expansion-panel>
        <v-expansion-panel title="⚾">
            <v-expansion-panel-text>
                <div class="d-flex justify-space-between">
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>

                </div>
            </v-expansion-panel-text>
        </v-expansion-panel>
        <v-expansion-panel title="😆">
            <v-expansion-panel-text>
                <div class="d-flex w-100 justify-space-between">
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>

                </div>

            </v-expansion-panel-text>
        </v-expansion-panel>

        <v-expansion-panel title="🎵🎬📚">
            <v-expansion-panel-text>
                <div class="d-flex w-100 justify-space-between">
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>

                </div>

            </v-expansion-panel-text>
        </v-expansion-panel>
        <v-expansion-panel title="🎙️">
            <v-expansion-panel-text>
                <div class="d-flex w-100 justify-space-between">
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>

                </div>

            </v-expansion-panel-text>
        </v-expansion-panel>
        <v-expansion-panel title="🎭">

            <v-expansion-panel-text>
                <div class="d-flex w-100 justify-space-between">
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>

                </div>

            </v-expansion-panel-text>
        </v-expansion-panel>
        <v-expansion-panel title="🏁">
            <v-expansion-panel-text>
                <div class="d-flex w-100 justify-space-between">
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>

                </div>

            </v-expansion-panel-text>
        </v-expansion-panel>
        <v-expansion-panel title="ungrouped" text="">

            <v-expansion-panel-text>
                <div class="d-flex w-100 justify-space-between">
                    <v-img :max-width="90" aspect-ratio="1/1" cover src=https://content.production.cdn.art19.com/images/ad/2c/aa/94/ad2caa94-bafc-4230-b3e6-32ef122001d1/ee10aaf8b59ae3c08000cb5a6cd3b3f96c90baac180b9f087ef3bfd67e7a57e9b9fdb2b1e029be5ec7290341c703faa5e6ff8da2d3fa8d434125fc788c09bdee.jpeg></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="https://images.podigee-cdn.net/0x,svW9CHZnAdRS5IFS-tFw06aEv12tD16FK9RTPkzQy6fM=/https://main.podigee-cdn.net/uploads/u33673/12ed70fa-6526-462c-96f4-4e78194863a3.jpeg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>
                    <v-img :max-width="90" aspect-ratio="1/1" cover src="@/assets/daily.jpg"></v-img>

                </div>

            </v-expansion-panel-text>
        </v-expansion-panel>

    </v-expansion-panels>
</div>
</template>

<script lang="ts">
export default {
    data() {
        return {
            podcast1: {
                    title: 'The Sojourn',
                    descprition: ' <p>The Tantalus Cluster is the fragile cradle of humanity.</p><p>“The Sojourn is a melange of rich storytelling, superb sound effects, and well-written characters that sound so real its like youre in the shuttle beside them. Theres a lot to enjoy in this immersive, fun audiodrama."',
                    author: 'Daniel Orrett',
                    imgurl: "https://content.production.cdn.art19.com/images/ad/2c/aa/94/ad2caa94-bafc-4230-b3e6-32ef122001d1/ee10aaf8b59ae3c08000cb5a6cd3b3f96c90baac180b9f087ef3bfd67e7a57e9b9fdb2b1e029be5ec7290341c703faa5e6ff8da2d3fa8d434125fc788c09bdee.jpeg"
                },
            podcast2:    {
                    title: 'Jung &amp; Naiv',
                    descprition: 'Politik für Desinteressierte: Interviews, Talks und Shows. Uns gibt es nur dank eurer finanziellen Unterstützung https://paypal.me/jungnaiv Auf Youtube als Video, hier als Podcast - DE/EN - www.jungundnaiv.de',
                    author: 'Tilo Jung',
                    imgurl: "https://images.podigee-cdn.net/0x,svW9CHZnAdRS5IFS-tFw06aEv12tD16FK9RTPkzQy6fM=/https://main.podigee-cdn.net/uploads/u33673/12ed70fa-6526-462c-96f4-4e78194863a3.jpeg"
                }

            
        }
    }
}
</script>
