<template>
    <div class="category_main">
        <NavigationBar />
        <div class="category_container">
            <div v-for="(icon, index) in icons" :key="index" class="category_icon">
                <img :src="icon.src | imagePath">
                <span>{{icon.text}}</span>
            </div>
        </div>
    </div>
</template>
<script>
import NavigationBar from "./NavigationBar";
export default {
    components: {
    NavigationBar: NavigationBar,
    },
    filters: {
        imagePath(value) {
            return require('@/image/' + value);
        }
    },
    data:()=>({
        icons:[{src:'icons/function/blood.png', text:'혈행개선'},
        {src:'icons/function/calories.png', text:'체지방감소'},
        {src:'icons/function/cell-protect.png', text:'세포보호'},
        {src:'icons/function/afraid.png', text:'긴장완화'},
        {src:'icons/function/dick.png', text:'전립선건강'},
        {src:'icons/function/energy.png', text:'에너지생성'},
        {src:'icons/function/fatigue.png', text:'피로개선'},
        {src:'icons/function/immune.png', text:'면역기능'},
        {src:'icons/function/intestine.png', text:'장건강'},
        {src:'icons/function/liver.png', text:'간건강'},
        {src:'icons/function/memory.png', text:'기억력개선'},
        {src:'icons/function/pregnant.png', text:'엽산대사'},
        {src:'icons/function/run.png', text:'지구력증진'},
        {src:'icons/function/skincare.png', text:'피부건강'},
        {src:'icons/function/visibility.png', text:'눈건강'},
        {src:'icons/function/x-ray.png', text:'뼈형성'}
        ]
    })
}
</script>
<style>
.category_main{
    width: 100%;
}

.category_container{
    margin-top:0.1%;
    padding-top:2%;
    width: 100%;
    height:92.5vh;
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;
    background-color:#fff;
}

.category_icon{
    width: 33%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.category_icon img{
    width: 30%;
}

.category_icon span{
    margin-top:5%;
}
</style>
