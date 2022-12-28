<template>
	<div class="productCard">
		<div class="productCard__top">
			<div v-if="status" class="productCard__status badge" :class="statusCssMap">{{ status.text }}</div>
			<AppChip
				class="productCard__compare"
				:class="isInCompare ? 'active' : ''"
				tag="button"
				color="white"
				circle="medium"
				aria-label="Добавить в сравнение"
				type="button"
			>
				<CompareIcon />
			</AppChip>
			<Swiper class="productCard__slider">
				<SwiperSlide v-for="image in images" :key="image.images" class="productCard__slide">
					<img class="productCard__img" :src="image.images" alt="" @error="changeImageOnError">
				</SwiperSlide>
				<SwiperSlide v-if="!images || !images.length">
					<img class="productCard__img" :src="require('@/assets/img/misc/product.png')" alt="">
				</SwiperSlide>
				<SwiperArrow class="productCard__arrow productCard__arrow_prev" type="prev" />
				<SwiperArrow class="productCard__arrow productCard__arrow_next" type="next" />
			</Swiper>
		</div>
		<div class="productCard__info">
			<h3 class="productCard__title">{{ name }}</h3>
			<div v-if="features && features.length" class="productCard__features features">
				<AppFeature
					v-for="feature in features"
					:key="feature.text"
					class="features__item"
					:text="feature.text"
					:icon="feature.icon" />
			</div>
			<div class="productCard__row">
				<div class="productCard__prices">
					<div class="productCard__common">{{ sales_price }}</div>
					<div class="productCard__price">{{ price }}</div>
				</div>
				<div class="productCard__row">
					<AppChip
						class="productCard__chip"
						:class="isInCart ? 'active' : ''"
						tag="button"
						color="white"
						mod="stroke"
						circle="medium"
						type="button"
						aria-label="Добавить в корзину"
					>
						<CartIcon />
					</AppChip>
					<AppChip
						class="productCard__chip"
						:class="isInFavorites ? 'active' : ''"
						tag="button"
						color="white"
						mod="stroke"
						circle="medium"
						type="button"
						aria-label="Добавить в избранное"
					>
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
		images: {
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
			type: Object as () => { icon: string; text: string }[] | null,
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
		console.log(props.images);

		const statusCssMap = computed(() => ({
			success: props.status?.badge === 'latest',
			danger: props.status?.badge === 'hit',
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
		height: 230px;
		border-radius: 10px 10px 0 0;
		border-bottom: 1px solid $border;

		.swiper {
			height: 100%;
		}
	}

	&__slide {
		border-radius: 10px 10px 0 0;
		text-align: center;
		overflow: hidden;
	}

	&__img {
		width: 100%;
		height: 100%;
		object-fit: cover;
		object-position: center;
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
