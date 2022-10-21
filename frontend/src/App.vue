<template>
  <div class="common-layout">
    <el-container>
      <el-aside>
        <el-affix :offset="60">
          <el-row>
            <el-col style="display: flex; justify-content: center;align-items:center">
              选择日期：
              <el-date-picker v-model="date" type="date" placeholder="Pick a date" :disabled-date="disabledDate"
                style="width: 50%;" />
            </el-col>
          </el-row>
          <el-menu active-text-color="#ffd04b" default-active="1-1" style="margin-top:15px;border-radius: 8px;">
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
      <el-main style="width:80%;">
        <component :is="currentComponent" :date="date" ref="childrenRef" :data="data" @submit="submit" />
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

// import axios from "axios";

// const http = axios.create({
//   baseURL: '',
//   timeout: 1000 * 60 * 2,
//   withCredentials: true,
// })
// http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

export default {
  name: 'App',
  components: {
    BiLiBiLi,
    TieBa,
    WeiBo,
    ZhiHu,
  },
  setup() {
    let data = ref({
      bilibili: null,
      tieba: null,
      weibo: null,
      zhihu: null
    });
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
    const submit = (target, val) => {
      if (target == 'bilibili') {
        data.value.bilibili = val;
      }
      else if (target == 'tieba') {
        data.value.tieba = val;
      }
      else if (target == 'weibo') {
        data.value.weibo = val;
      }
      else {
        data.value.zhihu = val;
      }
      // console.log(val);
      // console.log(data.value)
    }
    const disabledDate = (time) => {
      return time.getTime() > Date.now() || time.getTime() < 1666000000000;
    }
    watch(date, (newDate) => {
      data.value = {
        bilibili: null,
        tieba: null,
        weibo: null,
        zhihu: null
      };
      childrenRef.value.getData(newDate);
    })
    return {
      data,
      date,
      currentComponent,
      childrenRef,
      submit,
      clickBilibili,
      clickTieBa,
      clickWeiBo,
      clickZhiHu,
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
  min-height: 100%;
  display: flex;
  flex-direction: column;
}

body {
  background-color: #F5F7FA;
  display: flex;
  justify-content: center;
  margin-left: 20px;
  margin-right: 20px;
}

.demo-date-picker {
  display: flex;
  width: 200px;
  padding: 0;
  flex-wrap: wrap;
}

.el-menu-demo {
  background-color: aqua
}

.is-active {
  background-color: #d9ecff;
}

.el-menu-item {
  border-radius: 8px;
}

.common-layout {
  display: flex;
  justify-content: flex-start;
  max-width: 2540px;
  min-width: 1080px;
}
</style>


