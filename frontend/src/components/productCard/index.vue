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
				<SwiperArrow class="productCard__arrow productCard__arrow_prev" type="prev" />
				<SwiperArrow class="productCard__arrow productCard__arrow_next" type="next" />
			</Swiper>
		</div>
		<div class="productCard__info">
			<h3 class="productCard__title">Kugoo Kirin M4</h3>
			<div class="productCard__features features">
				<AppFeature class="features__item" text="2000 mAh" icon="accumulator"></AppFeature>
				<AppFeature class="features__item" text="1,2 л.с." icon="power"></AppFeature>
				<AppFeature class="features__item" text="60 км/ч" icon="speedometer"></AppFeature>
				<AppFeature class="features__item" text="5 часов" icon="timer"></AppFeature>
			</div>
			<div class="productCard__row">
				<div class="productCard__prices">
					<div class="productCard__common">39 900 ₽</div>
					<div class="productCard__price">39 900 ₽</div>
				</div>
				<div class="productCard__row">
					<AppChip class="productCard__chip " tag="button" color="white" mod="stroke" circle="medium" type="button" aria-label="Добавить в корзину">
						<CartIcon />
					</AppChip>
					<AppChip class="productCard__chip" tag="button" color="white" mod="stroke" circle="medium" type="button" aria-label="Добавить в избранное">
						<FavoritesIcon />
					</AppChip>
				</div>
			</div>
			<AppButton class="productCard__button">Купить в 1 клик</AppButton>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import SwiperArrow from '@/components/swiperArrow.vue';
import AppChip from '@/components/chip/index.vue';
import AppButton from '@/components/button/index.vue';
import AppFeature from '@/components/feature.vue';
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
		SwiperArrow,
		AppChip,
		AppButton,
		AppFeature,
		CompareIcon,
		CartIcon,
		FavoritesIcon,
	},
});
</script>

<style lang="scss" scoped>
@import '@/assets/css/modules/var';
@import '@/assets/css/components/badge';
@import '@/assets/css/components/features';

.productCard {
	display: flex;
	flex-direction: column;
	border-radius: 10px;
	outline: 1px solid $border;

	&__top {
		position: relative;
		display: flex;
		justify-content: center;
		align-items: center;
		min-height: 230px;
		border-radius: 10px 10px 0 0;
		background-color: $backgroundCard;
	}

	&__slide {
		text-align: center;
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

	&__info {
		padding: 20px 25px;
	}

	&__title {
		margin: 0;
		font-size: 18px;
		font-weight: 600;
	}

	&__list {
		margin: 0;
		padding: 0;
		list-style-type: none;
	}

	&__features {
		margin-top: 20px;
		margin-bottom: 25px;
	}

	&__row {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	&__common {
		font-size: 12px;
		font-weight: 500;
		text-decoration-line: line-through;
		color: $surface;
	}

	&__price {
		font-size: 20px;
		font-weight: 600;
	}

	&__chip + &__chip {
		margin-left: 10px;
	}

	&__button {
		margin-top: 15px;
		width: 100%;
	}

	&__arrow {
		position: absolute;
		top: 50%;
		transform: translateY(-50%);
		z-index: 1;

		&_prev {
			left: 10px;
		}

		&_next {
			right: 10px;
		}
	}
}
</style>
