<template>
    <el-row style="margin:auto;width: 1100px; margin:5px;">
        <img src="https://www.suredian.com/static/images/res/zhihu.svg" alt="" width="50">
        <span style="font-size:40px;padding: 10px;">知乎</span>
    </el-row>
    <el-row v-for="item in zhihu" :key="item.id" :gutter="0"
        style="padding: 14px; margin:5px; background-color: white;border-radius: 8px;width: 1100px;">
        <el-col :span="6">
            <img :src=item.image_url class="image" width="250" height="156" style="border-radius: 8px" />
        </el-col>
        <el-col :span="18">
            <el-row>
                <el-col :span="2" style="display:flex; align-items:center;">
                    <RankComponent :rank="item.rank"></RankComponent>
                </el-col>
                <el-col :span="22">
                    <el-link :underline="false" :href=item.link target="_blank">
                        <h1>
                            {{item.title}}
                        </h1>
                    </el-link>
                </el-col>
            </el-row>
            <el-row>
                <p class="describe">
                    简介：{{item.describe}}
                </p>
            </el-row>
            <el-row>
                <div class="heatShow">
                    热度：{{item.heat}}
                </div>
            </el-row>
        </el-col>
    </el-row>
</template>
<script>
import RankComponent from './RankComponent.vue'
import { ref } from 'vue'
import { http } from '../untils/request.js'
export default {
    props: ['date', 'data',],
    emits: ['submit'],
    components: {
        RankComponent
    },
    setup(props, { emit }) {
        const zhihu = ref(props.data.zhihu);
        const getData = async function (date) {
            let day = date.getDate()
            let month = date.getMonth() + 1
            let year = date.getFullYear() % 100;
            try {
                const response = await http.get('zhihu?date=' + year + month + day);
                emit('submit', 'zhihu', response.data);
                zhihu.value = response.data;
            } catch (error) {
                console.error(error);
            }
        }
        if (zhihu.value == null) {
            getData(props.date)
        }
        return {
            zhihu,
            getData
        }
    }
}
</script>
<style>
.heatShow {
    font-size: 13px;
    margin-top: 10px;
    color: #8d9298;
}

.describe {
    word-break: break-all;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
}
</style>