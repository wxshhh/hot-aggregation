<template>
    <div v-if="rank==1" style="padding-top:10px;padding-right:5px;">
        <img src="https://www.suredian.com/static/images/index/top1.svg" width="50" alt="">
    </div>
    <div v-else-if="rank==2" style="padding-top:10px;padding-right:5px;">
        <img src="https://www.suredian.com/static/images/index/top2.svg" width="50" alt="">
    </div>
    <div v-else-if="rank==3" style="padding-top:10px;padding-right:5px;">
        <img src="https://www.suredian.com/static/images/index/top3.svg" width="50" alt="">
    </div>
    <div v-else>
        <h1 style="text-align:center;">
            NO.{{rank}}
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