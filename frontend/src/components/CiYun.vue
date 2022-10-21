<template>
    <el-row style="display:flex; justify-content: flex-start;align-items: center; width: 1100px; margin:5px;">
        <img src="../assets/ciyun.png" alt="" width="50" height="50">
        <span style="font-size:40px;padding: 10px;">词云</span>
    </el-row>
    <el-row style="display:flex; justify-content: center;align-items: center; width: 1100px; margin:5px;">
        <img src="../assets/ciyun.png" alt="" width="500" height="500" style="border-radius: 10px;">
    </el-row>
</template>

<script>
// import { ref } from 'vue'
// import { http } from '../untils/request.js'
// export default {
//     props: ['date', 'data'],
//     emits: ['submit'],
//     components: {

//     },
//     setup(props, { emit }) {
//         const ciyun = ref(props.data.ciyun);
//         const getData = async function (date) {
//             let day = date.getDate()
//             let month = date.getMonth() + 1
//             let year = date.getFullYear() % 100;
//             try {
//                 const response = await http.get('ciyun?date=' + year + month + day);
//                 emit('submit', 'ciyun', response.data);
//                 ciyun.value = response.data;
//             } catch (error) {
//                 console.error(error);
//             }
//         }
//         if (ciyun.value == null) {
//             getData(props.date)
//         }
//         return {
//             ciyun,
//             getData
//         }
//     }
// }
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
