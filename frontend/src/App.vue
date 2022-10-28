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
            <el-menu-item index="1-5" @click="clickWordCloud"><img src="./assets/ciyun.png" alt="" width="30"
                style="margin-right:8px">今日热词
            </el-menu-item>
            <el-menu-item index="1-6" @click="clickSentimentAnlysis"><img src="data:image/jpeg;base64,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" alt="" width="30"
                style="margin-right:8px">今日情绪分析
            </el-menu-item>
          </el-menu>
        </el-affix>
      </el-aside>
      <el-main style="width:80%;">
        <el-col style="width: 1110px;">
          <component :is="currentComponent" :date="date" ref="childrenRef" :data="data" @submit="submit" />
        </el-col>
      </el-main>
    </el-container>
  </div>
</template>


<script>
import BiLiBiLi from './components/BiLiBiLi.vue'
import TieBa from './components/TieBa.vue'
import WeiBo from './components/WeiBo.vue'
import ZhiHu from './components/ZhiHu.vue'
import WordCloud from './components/WordCloud.vue'
import SentimentAnalysis from './components/SentimentAnalysis.vue'
import { ref, watch } from 'vue'

export default {
  name: 'App',
  components: {
    BiLiBiLi,
    TieBa,
    WeiBo,
    ZhiHu,
    WordCloud,
    SentimentAnalysis
  },
  setup() {
    let data = ref({
      bilibili: null,
      tieba: null,
      weibo: null,
      zhihu: null,
      sentiment: null,
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
    const clickWordCloud = () => {
      currentComponent.value = 'WordCloud';
    }
    const clickSentimentAnlysis = () => {
      currentComponent.value = 'SentimentAnalysis';
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
      else if (target == 'zhihu') {
        data.value.zhihu = val;
      }
      else {
        data.value.sentiment = val;
      }
    }
    const disabledDate = (time) => {
      return time.getTime() > Date.now() || time.getTime() < 1666195200000;
    }
    watch(date, (newDate) => {
      data.value = {
        bilibili: null,
        tieba: null,
        weibo: null,
        zhihu: null,
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
      clickWordCloud,
      clickSentimentAnlysis,
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


