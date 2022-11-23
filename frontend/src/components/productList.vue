<template>
	<div class="productList">
		<div v-for="item in products" :key="item" class="productList__item">
			<ProductCard v-bind="item" />
		</div>
	</div>
</template>

<script lang="ts" setup>
import ProductCard from '@/components/productCard/index.vue';
import { ProductCardProps } from '@/components/productCard/types';

defineProps<{ products: ProductCardProps[] }>();

</script>

<style lang="scss" scoped>
	.productList {
		display: flex;
		flex-wrap: wrap;
		margin-left: -15px;
		margin-right: -15px;

		&__item {
			flex-basis: calc(25% - 15px);
			margin: 15px;
		}
	}
</style>
