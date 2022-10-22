<template>
    <el-row style="display:flex; justify-content: flex-start;align-items: center; width: 1100px; margin:5px;">
        <img src="../assets/ciyun.png" alt="" width="50" height="50">
        <span style="font-size:40px;padding: 10px;">词云</span>
    </el-row>
    <el-row style="display:flex; justify-content: center;align-items: center; width: 1100px; margin:5px;">
        <img src="../assets/ciyun.png" alt="" height="600" style="border-radius: 10px;">
    </el-row>
</template>

<script>

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
