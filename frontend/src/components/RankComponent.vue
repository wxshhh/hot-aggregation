<template>
    <div v-if="rank==1" style="display: flex; justify-content: center;align-items:center" >
        <img src="https://www.suredian.com/static/images/index/top1.svg" width="50" alt="">
    </div>
    <div v-else-if="rank==2" style="display: flex; justify-content: center;align-items:center">
        <img src="https://www.suredian.com/static/images/index/top2.svg" width="50" alt="">
    </div>
    <div v-else-if="rank==3" style="display: flex; justify-content: center;align-items:center">
        <img src="https://www.suredian.com/static/images/index/top3.svg" width="50" alt="">
    </div>
    <div v-else style="display: flex; justify-content: center;align-items:center">
        <h1>
            <i style="font-size: 20px;">NO.</i>{{rank}}
        </h1>
    </div>
</template>

<script>
    export default {
    props: ['rank'],
    setup() {

    }
}
</script>