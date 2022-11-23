<template>
	<div class="swiperControl">
		<button
			class="swiperControl__button swiperControl__button_prev"
			type="button"
			aria-label="Пердыдущий слайд"
			:disabled="swiper.isBeginning"
			@click="swiper.slidePrev()"
		>
			<ArrowLeftIcon />
		</button>
		<div class="swiperControl__info">
			<span class="swiperControl__text">{{ swiper.activeIndex + 1 }}</span>
			<span class="swiperControl__progress">
				<span class="swiperControl__progressBar" :style="progressBarWidth"></span>
			</span>
			<span class="swiperControl__text">{{ swiper.slides.length }}</span>
		</div>
		<button
			class="swiperControl__button swiperControl__button_next"
			type="button"
			aria-label="Следующий слайд"
			:disabled="swiper.isEnd"
			@click="swiper.slideNext()"
		>
			<ArrowRightIcon />
		</button>
	</div>
</template>

<script lang="ts">
import { defineComponent, computed, ComputedRef, Ref } from 'vue';
import ArrowLeftIcon from '@/components/icons/arrowLeftIcon.vue';
import ArrowRightIcon from '@/components/icons/arrowRightIcon.vue';
import { useSwiper } from 'swiper/vue';
import { Swiper } from 'swiper/types';

export default defineComponent({
	name: 'SwiperControl',
	props: {
		progress: {
			type: Number,
			required: true,
		},
	},
	setup(props) {
		const swiper: Ref<Swiper> = useSwiper();
		const progressBarWidth: ComputedRef<string> = computed(() => `width: ${props.progress * 100}%`);

		return {
			progressBarWidth,
			swiper,
		};
	},
	components: {
		ArrowLeftIcon,
		ArrowRightIcon,
	},
});
</script>

<style lang="scss" scoped>
	@import "@/assets/css/modules/var";

	.swiperControl {
		position: absolute;
		display: flex;
		align-items: center;
		z-index: 100;

		&__button {
			display: flex;
			justify-content: center;
			align-items: center;
			width: 26px;
			height: 26px;
			border: 1px solid rgba(255, 255, 255, .2);
			border-radius: 50%;
			background-color: transparent;
			transition: background-color .2s ease, border-color .2s ease;

			&:disabled {
				opacity: .5;
				cursor: default;
			}

			&_prev {
				margin-right: 15px;
			}

			&_next {
				margin-left: 15px;
			}

			:deep(path) {
				transition: fill .2s ease;
			}

			&:hover:not(:disabled) {
				background-color: #fff;
				border-color: #fff;

				:deep(path) {
					fill: $primary;
				}
			}
		}

		&__info {
			display: flex;
			align-items: center;
		}

		&__progress,
		&__progressBar {
			border-radius: 10px;
		}

		&__progress {
			position: relative;
			margin: 0 10px;
			width: 35px;
			height: 2px;
			background-color: $primary-200;
		}

		&__progressBar {
			position: absolute;
			top: 0;
			left: 0;
			bottom: 0;
			background-color: #fff;
			transition: width .2s ease;
		}
	}
</style>
