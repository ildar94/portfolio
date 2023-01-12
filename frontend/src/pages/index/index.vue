<template>
	<MainBanner />
	<div class="container">
		<div class="keyVal keyVal_row">
			<div class="keyVal__item">
				<h3 class="keyVal__key">Гарантия 1 год </h3>
				<span class="keyVal__val">на весь ассортимент</span>
			</div>
			<div class="keyVal__item">
				<h3 class="keyVal__key">рассрочка</h3>
				<span class="keyVal__val">от 6 месяцев</span>
			</div>
			<div class="keyVal__item">
				<h3 class="keyVal__key">Подарки</h3>
				<span class="keyVal__val">и бонусам к покупкам</span>
			</div>
		</div>
		<MainProductList />
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MainBanner from '@/pages/index/components/mainBanner.vue';
import MainProductList from '@/pages/index/components/mainProductList.vue';

export default defineComponent({
	name: 'indexPage',
	components: {
		MainBanner,
		MainProductList,
	},
});
</script>

<style lang="scss" scoped>
	@import "@/assets/css/components/keyVal";
</style>
