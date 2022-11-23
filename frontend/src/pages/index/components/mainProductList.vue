<template>
	<div class="mainProductList">
		<div class="mainProductList__head">
			<h2 class="mainProductList__title title-h2">Электросамокаты</h2>
			<div class="mainProductList__row">
				<AppButton color="primary" mod="stroke">Хиты продаж</AppButton>
				<AppButton color="tertiary" mod="fill">Для города</AppButton>
				<AppButton color="tertiary" mod="fill">Для взрослых</AppButton>
				<AppButton color="tertiary" mod="fill">Для детей</AppButton>
			</div>
		</div>
		<ProductList :products="mainProducts.products" />
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AppButton from '@/components/button/index.vue';
import ProductList from '@/components/productList.vue';
import { useMainProductsStore } from '@/store/mainProductsStore';

export default defineComponent({
	name: 'MainProductList',
	setup() {
		const mainProducts = useMainProductsStore();

		mainProducts.get();

		return {
			mainProducts,
		};
	},
	components: {
		AppButton,
		ProductList,
	},
});
</script>

<style lang="scss" scoped>
	@import '@/assets/css/modules/var';
	@import '@/assets/css/modules/polygraphy';

	.mainProductList {
		margin-top: 75px;

		&__title {
			margin: 0;
			text-transform: uppercase;
		}
	}
</style>
