<template>
	<svg :width="width" :height="height" viewBox="0 0 7 12" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path d="M.47 6.53a.75.75 0 0 1 0-1.06L5.24.7A.75.75 0 1 1 6.3 1.76L2.06 6l4.24 4.24a.75.75 0 0 1-1.06 1.06L.47 6.53ZM2 6.75H1v-1.5h1v1.5Z" :fill="fill"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'ArrowLeftIcon',
	props: {
		width: {
			type: String,
			default: '7',
		},
		height: {
			type: String,
			default: '12',
		},
		fill: {
			type: String,
			default: '#fff',
		},
	},
});
</script>
