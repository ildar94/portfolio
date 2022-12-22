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
		<div class="productList">
			<div class="productList__item" v-for="item in mainProducts.products.slice(0, 8)" :key="item.id">
				<ProductCard
					:name="item.name"
					:price="item.price"
					:pictures="item.product_image"
					:sales_price="item.sales_price"
				/>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AppButton from '@/components/button/index.vue';
import { useMainProductsStore } from '@/store/mainProductsStore';
import ProductCard from '@/components/productCard/index.vue';

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
		ProductCard,
	},
});
</script>

<style lang="scss" scoped>
	@import '@/assets/css/modules/var';
	@import '@/assets/css/modules/polygraphy';
	@import '@/assets/css/components/productList';

	.mainProductList {
		margin-top: 75px;

		&__title {
			margin: 0;
			text-transform: uppercase;
		}
	}
</style>
