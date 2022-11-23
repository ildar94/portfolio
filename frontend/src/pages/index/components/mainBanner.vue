<template>
	<div class="mainBanner">
		<Swiper
			class="mainBanner__swiper"
			:modules="modules"
			:autoplay="{ delay: 1500, disableOnInteraction: false }"
			@progress="onProgress"
		>
			<SwiperSlide
				v-for="slide in promoStore.mainBanner"
				:key="slide.id"
				class="mainBanner__slide"
			>
				<div class="container">
					<div class="mainBanner__info">
						<h2 class="mainBanner__title">{{ slide.title }}</h2>
						<div class="mainBanner__desc">{{ slide.desc }}</div>
						<RouterLink to="/catalog/" v-slot="{ href, navigate }">
							<AppButton class="mainBanner__link" color="white" size="large" tag="a" :href="href" @click="navigate">Перейти в католог</AppButton>
						</RouterLink>
					</div>
				</div>
				<div class="mainBanner__image">
					<img class="mainBanner__img" :src="slide.image" alt="" @error="changeImageOnError">
				</div>
			</SwiperSlide>
			<SwiperControl :progress="progress" class="mainBanner__controls container" />
		</Swiper>
	</div>
</template>

<script lang="ts">
import { defineComponent, ref, Ref } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import type { Swiper as SwiperType } from 'swiper/types';
import { Autoplay } from 'swiper';
import AppButton from '@/components/button/index.vue';
import SwiperControl from '@/components/swiperControl.vue';
import { usePromoStore } from '@/store/promoStore';

import 'swiper/css';
import 'swiper/css/autoplay';

export default defineComponent({
	name: 'MainBanner',
	components: {
		Swiper,
		SwiperSlide,
		AppButton,
		SwiperControl,
	},
	setup() {
		const promoStore = usePromoStore();

		promoStore.getMainBanner();

		function changeImageOnError(e: Event) {
			const target: HTMLImageElement = e.target as HTMLImageElement;

			target.src = require('@/assets/img/misc/slide.png');
		}

		const progress: Ref<number> = ref(0);

		function onProgress(swiper: SwiperType, value: number) {
			progress.value = value;
		}

		return {
			modules: [Autoplay],
			promoStore,
			changeImageOnError,
			progress,
			onProgress,
		};
	},
});
</script>

<style lang="scss" scoped>
	@import "@/assets/css/modules/var";

	.mainBanner {
		max-width: 1380px;
		margin: 0 auto;
		color: #fff;

		.container {
			width: 100%;
		}

		&__swiper,
		&__slide {
			min-height: 405px;
		}

		&__slide {
			position: relative;
			display: flex;
			align-items: center;
			justify-content: space-between;
			background-image: radial-gradient(58.73% 541.94% at 75.14% 62.23%, #A6A9FF 0%, #6F73EE 100%);
		}

		&__info {
			max-width: 615px;
		}

		&__title {
			font-size: 35px;
			font-weight: 600;
			text-transform: uppercase;
		}

		&__desc {
			margin-top: 5px;
			font-size: 20px;
		}

		&__link {
			font-weight: normal;
			margin-top: 25px;
		}

		&__controls {
			bottom: 30px;
			left: 50%;
			transform: translateX(-50%);
		}

		&__image {
			position: absolute;
			right: 0;
			bottom: 0;
			max-width: 540px;
		}
	}
</style>
