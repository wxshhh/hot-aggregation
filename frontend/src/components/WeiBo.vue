<template>
    <el-row style="margin:auto;width: 1100px; margin:5px;">
        <img src="https://www.suredian.com/static/images/res/weibo.svg" alt="" width="50">
        <span style="font-size:40px;padding: 10px;">微博</span>
    </el-row>
    <el-row v-for="item in weibo" :key="item.id" :gutter="0"
        style="padding: 14px; margin:5px; background-color: white;border-radius: 8px;width: 1100px;">
        <el-col>
            <el-row :gutter="5">
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
        const weibo = ref(props.data.weibo);
        const getData = async function (date) {
            let day = date.getDate()
            let month = date.getMonth() + 1
            let year = date.getFullYear() % 100;
            try {
                const response = await http.get('weibo?date=' + year + month + day);
                emit('submit', 'weibo', response.data);
                weibo.value = response.data;
            } catch (error) {
                console.error(error);
            }
        }
        if (weibo.value == null) {
            getData(props.date)
        }
        return {
            weibo,
            getData
        }
    }
}
</script>

