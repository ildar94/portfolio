<template>
	<AppChip
		class="swiperArrow"
		color="whiteDeep"
		circle="medium"
		tag="button"
		type="button"
		:aria-label="type === 'next' ? 'Следующая картинка' : 'Предыдущая картинка'"
		@click="changeSlide">
		<ArrowLeftIcon v-if="type === 'prev'" :fill="null" />
		<ArrowRightIcon v-else-if="type === 'next'" :fill="null" />
	</AppChip>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useSwiper } from 'swiper/vue';
import AppChip from '@/components/chip/index.vue';
import ArrowLeftIcon from '@/components/icons/arrowLeftIcon.vue';
import ArrowRightIcon from '@/components/icons/arrowRightIcon.vue';

export default defineComponent({
	name: 'swiperArrow',
	props: {
		type: {
			type: String,
			required: true,
			validator: (value: string) => ['prev', 'next'].includes(value),
		},
	},
	setup(props) {
		const swiper = useSwiper();

		function changeSlide() {
			if (props.type === 'next') {
				swiper.value.slideNext();
			}

			if (props.type === 'prev') {
				swiper.value.slidePrev();
			}
		}

		return { changeSlide };
	},
	components: {
		AppChip,
		ArrowLeftIcon,
		ArrowRightIcon,
	},
});
</script>

<style lang="scss" scoped>
@import '@/assets/css/modules/var';

.swiperArrow svg {
	fill: $primary;
}
</style>
