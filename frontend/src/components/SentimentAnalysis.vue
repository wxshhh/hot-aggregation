<template>
        <el-row style="margin:auto;width: 1100px; margin:5px;">
            <img src="data:image/jpeg;base64,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" alt="" width="50">
            <span style="font-size:40px;padding: 10px;">今日情绪分析</span>
        </el-row>
        <div class="echarts-box" style="display:flex; justify-content: center; flex-wrap: wrap;width: 1100px; margin:5px;">
            <div id="pieEcharts" :style="{ width: '900px', height: '300px' }"></div>
            <div id="barEcharts" :style="{ width: '900px', height: '300px' }"></div>
        </div>
</template>

<script>
import * as echarts from "echarts";
import { ref, onMounted, onUnmounted } from "vue";
import { http } from '../untils/request.js'
export default {
    props: ['data',],
    emits: ['submit'],
    setup(props, { emit }) {
        const sentiment = ref(props.data.sentiment);
        let value = {
            postive: 0,
            nagetive: 0
        };
        let data = {
            index: [],
            val: []
        };

        const getData = async function () {
            try {
                const response = await http.get('sentiments');
                emit('submit', 'sentiment', response.data);
                sentiment.value = response.data;
                value = count(sentiment.value);
                data = {
                    index: range(1, sentiment.value.length + 1),
                    val: sentiment.value
                }
                console.log(value)
                console.log(data)
            } catch (error) {
                console.error(error);
            }
        }
        let echart = echarts;
        onMounted(async () => {
            if (sentiment.value == null) {
                await getData();
            }
            else {
                value = count(sentiment.value);
                data = {
                    index: range(1, sentiment.value.length + 1),
                    val: sentiment.value
                }
            }
            initChart(value, data);
        });

        onUnmounted(() => {
            echart.dispose;
        });

        function count(data) {
            if (data == null) {
                return;
            }
            let count = 0;
            for (let i of data) {
                count += i < 0.4 ? 0 : 1
            }
            return {
                postive: count,
                nagetive: data.length - count
            }
        }
        
        function range(start, end) {
            return [...Array(end - start).keys()].map(item => start + item);
        }

      function ave(arr) {
        let sum = 0;
        for (let i of arr) {
          sum += i;
        }
        return sum / arr.length
      }

        function initChart(value, data) {
            let pieChart = echart.init(document.getElementById("pieEcharts"), "white");
            let barChart = echart.init(document.getElementById("barEcharts"), "white");
            pieChart.setOption({
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                series: [
                    {
                        name: 'Access From',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: '40',
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: [
                            { value: value.postive, name: 'Postive 😊' },
                            { value: value.nagetive, name: 'Negative 😡' },
                        ]
                    }
                ]
            });
            let average = ave(data.val)
            barChart.setOption({
                title: {
                    text: '热搜情绪指数',
                    left: 10
                },
                toolbox: {
                    feature: {
                        dataZoom: {
                            yAxisIndex: false
                        },
                        saveAsImage: {
                            pixelRatio: 2
                        }
                    }
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },
                grid: {
                    bottom: 90
                },
                dataZoom: [
                    {
                        type: 'inside'
                    },
                    {
                        type: 'slider'
                    }
                ],
                xAxis: {
                    show: false,
                    data: data.index,
                    silent: false,
                    splitLine: {
                        show: false
                    },
                    splitArea: {
                        show: false
                    }
                },
                yAxis: {
                    splitArea: {
                        show: false
                    }
                },
                series: [
                    {
                        type: 'bar',
                        data: data.val,
                        large: true
                    },
                  {
                    type: 'line',
                    markLine: {
                      symbol: ['none', 'none'],
                      silent: true,
                      lineStyle: {
                        normal: {
                          color: 'red',
                          width: 2,
                        }
                      },
                      data: [{
                        yAxis: average,
                      }],
                      label: {
                        position: 'top',
                        normal: {
                          formatter: average.toFixed(4)
                        }
                      },
                    },
                  }
                ]
            });
            window.onresize = function () {
                pieChart.resize();
                barChart.resize();
            };
        }
        return { initChart };
    }
};
</script>