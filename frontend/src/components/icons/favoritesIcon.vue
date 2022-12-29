<template>
	<svg :width="width" :height="height" viewBox="0 0 18 16" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path d="M17 3.51A5.11 5.11 0 0 0 12.26.4 5.16 5.16 0 0 0 9 1.56 5.07 5.07 0 0 0 5.74.4 5.12 5.12 0 0 0 .6 5.52c0 .65.13 1.33.4 2.02.22.58.53 1.19.93 1.8.64.95 1.52 1.95 2.6 2.97 1.81 1.68 3.6 2.85 3.68 2.9l.46.3c.2.12.46.12.67 0l.46-.3c.07-.06 1.86-1.22 3.67-2.9a17.18 17.18 0 0 0 2.6-2.98c.4-.6.72-1.2.94-1.79.26-.69.4-1.37.4-2.02 0-.7-.14-1.37-.41-2ZM9 13.95S2.08 9.47 2.08 5.52A3.67 3.67 0 0 1 9 3.87a3.67 3.67 0 0 1 6.93 1.65c0 3.95-6.93 8.43-6.93 8.43Z" :fill="fill"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'CompareIcon',
	props: {
		width: {
			type: String,
			default: '18',
		},
		height: {
			type: String,
			default: '16',
		},
		fill: {
			type: String,
			default: '#282739',
		},
	},
});
</script>
