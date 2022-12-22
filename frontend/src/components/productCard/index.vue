<template>
	<div class="productCard">
		<div class="productCard__top">
			<div class="productCard__status badge badge_success" :class="statusCssMap">Новинка</div>
			<AppChip class="productCard__compare" tag="button" color="white" circle="medium" aria-label="Добавить в сравнение" type="button">
				<CompareIcon />
			</AppChip>
			<Swiper class="productCard__slider">
				<SwiperSlide class="productCard__slide">
					<img src="" alt="" @error="changeImageOnError">
				</SwiperSlide>
				<SwiperSlide class="productCard__slide">
					<img src="" alt="" @error="changeImageOnError">
				</SwiperSlide>
				<SwiperSlide class="productCard__slide">
					<img src="" alt="" @error="changeImageOnError">
				</SwiperSlide>
			</Swiper>
		</div>
		<div class="productCard__info">
			<h3 class="productCard__title">Тайтал</h3>
			<ul class="productCard__list">
				<li class="productCard__item">
					<div class="productCard__feature">
						<svg class="productCard__icon">
							<use href="#"></use>
						</svg>
						<span class="productCard__text">2000 mAh</span>
					</div>
				</li>
			</ul>
			<div class="productCard__row">
				<div class="productCard__prices">
					<div class="productCard__common">39 900 ₽</div>
					<div class="productCard__price">39 900 ₽</div>
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
import { defineComponent, computed } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import AppChip from '@/components/chip/index.vue';
import AppButton from '@/components/button/index.vue';
import CompareIcon from '@/components/icons/compareIcon.vue';
import CartIcon from '@/components/icons/cartIcon.vue';
import FavoritesIcon from '@/components/icons/favoritesIcon.vue';
import { statusBadge } from '@/components/productCard/types';

export default defineComponent({
	name: 'ProductCard',
	props: {
		name: {
			type: String,
			required: true,
		},
		pictures: {
			type: Array as () => string[],
			default: () => [''],
		},
		status: {
			type: Object as () => { text: string; badge: statusBadge } | null,
			default: null,
		},
		isInCompare: {
			type: Boolean,
			default: false,
		},
		isInCart: {
			type: Boolean,
			default: false,
		},
		isInFavorites: {
			type: Boolean,
			default: false,
		},
		features: {
			type: Object as () => { icon: string; text: string } | null,
			default: null,
		},
		price: {
			type: Number,
			required: true,
		},
		sales_price: {
			type: Number as () => number | null,
			default: null,
		},
	},
	setup(props) {
		const statusCssMap = computed(() => ({
			badge_success: props.status?.badge === 'latest',
			badge_danger: props.status?.badge === 'hit',
		}));

		function changeImageOnError(e: Event) {
			const target: HTMLImageElement = e.target as HTMLImageElement;
			target.src = require('@/assets/img/misc/product_2.png');
		}

		return {
			changeImageOnError,
			statusCssMap,
		};
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

.productCard {
	display: flex;
	flex-direction: column;
	border-radius: 10px;
	outline: 1px solid $border;

	&__top {
		position: relative;
		border-radius: 10px 10px 0 0;
		background-color: $backgroundCard;
	}

	&__status,
	&__compare {
		position: absolute;
		top: 10px;
		z-index: 10;
	}

	&__status {
		left: 10px;
	}

	&__compare {
		right: 10px;
	}
}
</style>
