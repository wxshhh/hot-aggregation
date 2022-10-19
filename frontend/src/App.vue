<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="20%">
        <el-affix :offset="60">
          <el-row>
            <div style="margin:auto">
              选择日期:
            </div>
            <el-date-picker v-model="date" type="date" placeholder="Pick a date" :disabled-date="disabledDate"
              style="margin:auto" />
          </el-row>
          <el-menu active-text-color="#ffd04b" class="el-menu-demo" default-active="1-1" style="border-radius: 8px;margin-top:10px; ">
            <el-menu-item index="1-1" @click="clickBilibili"><img
                src="https://www.suredian.com/static/images/res/bilibili.svg" alt="" width="30"
                style="margin-right:8px">哔哩哔哩</el-menu-item>
            <el-menu-item index="1-2" @click="clickTieBa"><img
                src="https://www.suredian.com/static/images/res/tieba.svg" alt="" width="30" style="margin-right:8px">贴吧
            </el-menu-item>
            <el-menu-item index="1-3" @click="clickWeiBo"><img
                src="https://www.suredian.com/static/images/res/weibo.svg" alt="" width="30" style="margin-right:8px">微博
            </el-menu-item>
            <el-menu-item index="1-4" @click="clickZhiHu"><img
                src="https://www.suredian.com/static/images/res/zhihu.svg" alt="" width="30" style="margin-right:8px">知乎
            </el-menu-item>
          </el-menu>
        </el-affix>
      </el-aside>
      <el-main>
        <component :is="currentComponent" :date="date" ref="childrenRef" />
      </el-main>
    </el-container>
  </div>
</template>


<script>
import BiLiBiLi from './components/BiLiBiLi.vue'
import TieBa from './components/TieBa.vue'
import WeiBo from './components/WeiBo.vue'
import ZhiHu from './components/ZhiHu.vue'
import { ref, watch } from 'vue'
// import {
//   Document,
//   Location,
//   Setting,
// } from '@element-plus/icons-vue'
import axios from "axios";


const http = axios.create({
  baseURL: '',
  timeout: 1000 * 60 * 2,
  withCredentials: true,
})
http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

export default {
  name: 'App',
  components: {
    BiLiBiLi,
    TieBa,
    WeiBo,
    ZhiHu,
  },
  setup() {
    let date = ref(new Date());
    let currentComponent = ref('BiLiBiLi');
    let childrenRef = ref();
    const clickBilibili = () => {
      currentComponent.value = 'BiLiBiLi';
    }
    const clickTieBa = () => {
      currentComponent.value = 'TieBa';
    }
    const clickWeiBo = () => {
      currentComponent.value = 'WeiBo';
    }
    const clickZhiHu = () => {
      currentComponent.value = 'ZhiHu';
    }
    const disabledDate = (time) => {
      return time.getTime() > Date.now()
    }

    function test() {
      console.log(childrenRef.value);
      childrenRef.value.isChild()
    }
    watch(date, (newDate) => {
      childrenRef.value.getData(newDate);
    })
    return {
      test,
      date,
      currentComponent,
      clickBilibili,
      clickTieBa,
      clickWeiBo,
      clickZhiHu,
      // Document,
      // Location,
      // Setting,
      childrenRef,
      disabledDate
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  /* text-align: center; */
  /* margin-top: 60px; */
}

body {
  background-color: #F5F7FA;
}

.demo-date-picker {
  display: flex;
  width: 100%;
  padding: 0;
  flex-wrap: wrap;
}
.is-active{
  background-color:  #d9ecff;
}
.el-menu-item {
  border-radius: 8px;
}
</style>


