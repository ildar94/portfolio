<template>
	<div class="mainProductList">
		<div class="mainProductList__head">
			<h2 class="mainProductList__title title-h2">Электросамокаты</h2>
			<div class="mainProductList__row">
				<AppButton class="mainProductList__button" color="primary" mod="stroke">Хиты продаж</AppButton>
				<AppButton class="mainProductList__button" color="tertiary" mod="fill">Для города</AppButton>
				<AppButton class="mainProductList__button" color="tertiary" mod="fill">Для взрослых</AppButton>
				<AppButton class="mainProductList__button" color="tertiary" mod="fill">Для детей</AppButton>
			</div>
		</div>
		<div class="productList">
			<div class="productList__item" v-for="item in mainProducts.products.slice(0, 8)" :key="item.id">
				<ProductCard
					:id="item.id"
					:name="item.name"
					:price="item.priceFormat"
					:images="item.images"
					:sales_price="item.salesPriceFormat"
					:features="item?.features"
					:is-in-cart="cartStore.isInCart(item.id)"
					:is-in-compare="false"
					:is-in-favorites="false"
				/>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AppButton from '@/components/button/index.vue';
import { useMainProductsStore } from '@/store/mainProductsStore';
import { useCartStore } from '@/store/cartStore';
import ProductCard from '@/components/productCard.vue';

export default defineComponent({
	name: 'MainProductList',
	setup() {
		const mainProducts = useMainProductsStore();

		mainProducts.get();

		const cartStore = useCartStore();

		return {
			mainProducts,
			cartStore,
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

		&__head {
			display: flex;
			justify-content: space-between;
			align-items: center;
			margin-bottom: 35px;
		}

		&__title {
			margin: 0;
			text-transform: uppercase;
		}

		&__row {
			display: flex;
		}

		&__button + &__button {
			margin-left: 10px;
		}
	}
</style>
