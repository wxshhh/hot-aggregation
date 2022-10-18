<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="20%">
        <el-affix :offset="60">
          <el-menu active-text-color="#ffd04b" class="el-menu-demo" default-active="1-1">
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
        <component :is="currentComponent" :data="dataPath" />
      </el-main>
    </el-container>
  </div>
</template>


<script>
import BiLiBiLi from './components/BiLiBiLi.vue'
import TieBa from './components/TieBa.vue'
import WeiBo from './components/WeiBo.vue'
import ZhiHu from './components/ZhiHu.vue'
import { ref, } from 'vue'
import {
  Document,
  Location,
  Setting,
} from '@element-plus/icons-vue'

export default {
  name: 'App',
  components: {
    BiLiBiLi,
    TieBa,
    WeiBo,
    ZhiHu
  },
  setup() {
    let currentComponent = ref('BiLiBiLi');
    const data = ref({
      bilibili: [{
        rank: 1,
        title: "24楼的孩子，你爸妈很伟大。也许我只能沉默，可湿润了眼眶！！！",
        link: "https://b23.tv/BV15B4y1j7ep",
        describe: "-",
        author: "",
        image_url: "http://i0.hdslb.com/bfs/archive/bd8bf8a5cdd96ac58434e0fa8e1f092c902d466d.jpg",
        view: 827640,
        reply: 1573,
        favorite: 7596,
        coin: 98555,
        share: 263
      },
      {
        rank: 2,
        title: "什么叫国产战争片天花板！《特级英雄黄继光》硬核影评",
        link: "https://b23.tv/BV17D4y1C7W5",
        describe: "Staff总策划：花岗岩\n总顾问：星海论坛Suit\n总监制：花家小可爱\n",
        author: "",
        image_url: "http://i1.hdslb.com/bfs/archive/f831d5441d36599aa94dd675023b51bdafe1bf56.jpg",
        view: 1388438,
        reply: 3270,
        favorite: 38721,
        coin: 175836,
        share: 11193
      },
      {
        rank: 3,
        title: "不懂英语如何刺探英国情报？【硬核狠人40】",
        link: "https://b23.tv/BV1R44y1f7Yv",
        describe: "本篇为硬核狠人之艾丽萨.巴兹纳。",
        author: "小约翰可汗",
        image_url: "http://i1.hdslb.com/bfs/archive/d76155b3c9d53787338464aebfd62a469317a3e5.jpg",
        view: 783458,
        reply: 2034,
        favorite: 13891,
        coin: 36159,
        share: 2464
      },
      {
        rank: 4,
        title: "【S12全球总决赛】小组赛 10月14日 EDG vs T1",
        link: "https://b23.tv/BV1Z8411W7aW",
        describe: "【S12全球总决赛】小组赛 10月14日 EDG vs T1",
        author: "哔哩哔哩英雄联盟赛事",
        image_url: "http://i1.hdslb.com/bfs/archive/67b84fc45a6e64f3e68ef125c49fd091f311ae80.jpg",
        view: 1244350,
        reply: 2001,
        favorite: 922,
        coin: 1293,
        share: 790
      },
      ],
      tieba: [{
        rank: 1,
        title: "RNG八人确诊",
        link: "https://tieba.baidu.com/hottopic/browse/hottopic?topic_id=8544731&topic_name=RNG%E5%85%AB%E4%BA%BA%E7%A1%AE%E8%AF%8A",
        image_url: "https://tiebapic.baidu.com/forum/whfpf%3D84%2C88%2C40%3Bq%3D90/sign=644ac472f7b7d0a27b9c57ddadd24e3d/d058ccbf6c81800ad0a621cef43533fa838b47ab.jpg?tbpicau=2022-10-16-05_688f932664c0a2e92684f982bcaff344",
        describe: "RNG选手Breathe（陈晨）、Wei（闫扬威）、小虎（李元浩）、Ming（史森明）选手，教练Tabe（王柏勤）、助理教练Xiaobai（...",
        heat: "186.1W实时讨论"
      }],
      weibo: [{
        rank: 1,
        title: "羊了个羊出逃消防员被迫陪跑追回",
        link: "https://s.weibo.com/weibo?q=%23羊了个羊出逃消防员被迫陪跑追回%23"
      }],
      zhihu: [{
        rank: 1,
        title: "美发布新版国家安全战略，将中国定位为「优先考虑的、唯一的全球竞争对手」，这释放了哪些信号？",
        link: "https://www.zhihu.com/question/559096713",
        image_url: "https://pica.zhimg.com/80/v2-4ae5a82a178071e981e3b65d87fbff09_1440w.png",
        describe: "据路透社、法新社等多家媒体报道，美国白宫当地时间 12 日发布新版国家安全战略，其中果不其然提到中国，声称即使美国要努力约束「危险的俄罗斯」，中国也被定位为其「优先考虑的、唯一的全球竞争对手」。然而对...",
        heat: "848 万热度"
      }]
    })
    let dataPath = ref(data.value.bilibili);
    const clickBilibili = () => {
      currentComponent.value = 'BiLiBiLi';
      dataPath.value = data.value.bilibili;
    }
    const clickTieBa = () => {
      currentComponent.value = 'TieBa';
      dataPath.value = data.value.tieba;
    }
    const clickWeiBo = () => {
      currentComponent.value = 'WeiBo';
      dataPath.value = data.value.weibo;
    }
    const clickZhiHu = () => {
      currentComponent.value = 'ZhiHu';
      dataPath.value = data.value.zhihu;
    }

    return {
      data,
      dataPath,
      currentComponent,
      clickBilibili,
      clickTieBa,
      clickWeiBo,
      clickZhiHu,
      Document,
      Location,
      Setting,
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
}

body {
  background-color: #F5F7FA;
}
</style>


