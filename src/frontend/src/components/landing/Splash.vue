<template>

    <b-carousel id="inSlider"
                style="text-shadow: 1px 1px 2px #333;"
                controls
                indicators
                background="#ababab"
                :interval="4000"
                img-width="1900"
                img-height="500"
    >

      <!-- Text slides with image -->
      <b-carousel-slide caption="This is the title"
                        caption-tag="h1"
                        text="Nulla vitae elit libero, a pharetra augue mollis interdum."
                        img-src="static/img/landing/runner.jpg">
                          
                        </b-carousel-slide>
      <b-carousel-slide caption=""
                        text="Nulla vitae elit libero, a pharetra augue mollis interdum."
                        img-src="static/img/landing/plank2.jpg">
                      </b-carousel-slide>
     
    </b-carousel>

</template>
  

<script>
  
</script>

<style>
  

</style>