<template>
    <el-row style="margin:auto">
        <img src="https://www.suredian.com/static/images/res/baidu.svg" alt="" width="50">
        <span style="font-size:40px;padding: 10px;">百度贴吧</span>
    </el-row>
    <el-row v-for="item in data" :key="item.id" :gutter="0"
        style="padding: 14px; margin:5px; background-color: white;border-radius: 8px">
        <el-col :span="6">
            <img :src=item.image_url class="image" width="250" height="156" />
        </el-col>
        <el-col :span="18">
            <el-row>
                <el-col :span="2">
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
                <div>
                    简介：{{item.describe}}
                </div>
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
    props: ['date'],
    components: {
        RankComponent
    },
    setup(props) {
        let data = ref(null);
        const getData = async function (date) {
            let day = date.getDate()
            let month = date.getMonth() + 1
            let year = date.getFullYear() % 100;
            try {
                const response = await http.get('tieba?date=' + year + month + day);
                data.value = response.data;
            } catch (error) {
                console.error(error);
            }
        }
        getData(props.date)
        return {
            data,
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
</style>
