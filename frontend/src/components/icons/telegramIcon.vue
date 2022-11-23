<template>
	<svg class="icon icon_telegram" :class="colorClass" :width="width" :height="height" viewBox="0 0 19 15" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path class="icon__path" d="m7.23 9.89-.3 4.18c.43 0 .61-.18.83-.4l2-1.9 4.14 3.02c.76.43 1.29.2 1.5-.7L18.1 1.37c.24-1.13-.4-1.57-1.14-1.3L1 6.2C-.09 6.62-.07 7.22.81 7.5L4.9 8.78l9.48-5.94c.45-.3.85-.13.52.17L7.23 9.89Z" />
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useIconColor } from '@/composables/iconColor';

export default defineComponent({
	name: 'TelegramAppIcon',
	props: {
		color: {
			type: String,
			default: 'gray',
		},
		width: {
			type: String,
			default: '19',
		},
		height: {
			type: String,
			default: '15',
		},
	},
	setup(props) {
		const colorClass = useIconColor(props.color);

		return {
			colorClass,
		};
	},
});
</script>
