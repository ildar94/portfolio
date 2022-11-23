<template>
	<div class="productCard">
		<div class="productCard__top">
			<div v-if="status" class="productCard__status badge" :class="`badge_${status.badge}`">{{ status.text }}</div>
			<Chip class="productCard__compare" tag="button" color="white" circle="small" aria-label="Добавить в сравнение" type="button">
				<CompareIcon />
			</Chip>
			<Swiper class="productCard__slider">
				<SwiperSlide v-for="image in images" :key="image" class="productCard__slide">
					<img :src="image" alt="" @error="changeImageOnError">
				</SwiperSlide>
			</Swiper>
		</div>
		<div class="productCard__info">
			<h3 class="productCard__title">{{ name }}</h3>
			<ul class="productCard__list">
				<li class="productCard__item" v-for="feature in features" :key="feature.text">
					<div class="productCard__feature">
						<svg v-if="feature.icon" class="productCard__icon">
							<use :href="`#${feature.icon}`"></use>
						</svg>
						<span class="productCard__text">{{ feature.text }}</span>
					</div>
				</li>
			</ul>
			<div class="productCard__row">
				<div class="productCard__prices">
					<div v-if="sales_price" class="productCard__common">{{ sales_price }}</div>
					<div class="productCard__price">{{ price }}</div>
				</div>
				<div class="productCard__row">
					<AppChip tag="button" color="white" mod="stroke" circle="medium" type="button" aria-label="Добавить в корзину">
						<CartIcon />
					</AppChip>
					<AppChip tag="button" color="white" mod="stroke" circle="medium" type="button" aria-label="Добавить в избранное">
						<FavoritesIcon />
					</AppChip>
				</div>
			</div>
			<AppButton>Купить в 1 клик</AppButton>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, defineProps } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import AppChip from '@/components/chip/index.vue';
import AppButton from '@/components/button/index.vue';
import CompareIcon from '@/components/icons/compareIcon.vue';
import CartIcon from '@/components/icons/cartIcon.vue';
import FavoritesIcon from '@/components/icons/favoritesIcon.vue';
import { ProductCardProps } from '@/components/productCard/types';

export default defineComponent({
	name: 'ProductCard',
	setup() {
		const props = defineProps<{ props: ProductCardProps }>();

		function changeImageOnError(e: Event) {
			const target: HTMLImageElement = e.target as HTMLImageElement;
			target.src = require('@/assets/img/misc/product.png');
		}

		return { props, changeImageOnError };
	},
	components: {
		Swiper,
		SwiperSlide,
		AppChip,
		AppButton,
		CompareIcon,
		CartIcon,
		FavoritesIcon,
	},
});
</script>

<style lang="scss" scoped>
@import '@/assets/css/modules/var';
@import '@/assets/css/components/badge';
</style>
