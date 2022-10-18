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
                    <div v-if="item.rank==1" style="padding-top:10px;padding-right:5px;">
                        <img src="https://www.suredian.com/static/images/index/top1.svg" width="50" alt="">
                    </div>
                    <div v-else-if="item.rank==2" style="padding-top:10px;padding-right:5px;">
                        <img src="https://www.suredian.com/static/images/index/top2.svg" width="50" alt="">
                    </div>
                    <div v-else-if="item.rank==3" style="padding-top:10px;padding-right:5px;">
                        <img src="https://www.suredian.com/static/images/index/top3.svg" width="50" alt="">
                    </div>
                    <div v-else>
                        <h1 style="text-align:center;">
                            NO.{{item.rank}}
                        </h1>
                    </div>
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
                热度：{{item.heat}}
            </el-row>
        </el-col>
    </el-row>
</template>
<script>

export default {
    component:{
        
    },
    props: ['data'],
    setup() {

    }
}
</script>