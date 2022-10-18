<template>
    <el-row style="margin:auto">
      <img src="https://www.suredian.com/static/images/res/weibo.svg" alt="" width="50">
      <span style="font-size:40px;padding: 10px;">微博</span>
    </el-row>
    <el-row v-for="item in data" :key="item.id" :gutter="0" style="padding: 14px; margin:5px; background-color: white;border-radius: 8px">
        <el-link :underline="false" :href=item.link target="_blank">
            <h1>
                {{item.rank}}  {{item.title}}
            </h1>
        </el-link>
    </el-row>
</template>
<script>

export default {
    props: ['data'],
    setup() {

    }
}
</script>
<style>
a {
    text-decoration: none;
}

a:visited {
    text-decoration: none;
}
</style>