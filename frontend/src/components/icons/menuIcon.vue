<template>
	<svg :width="width" :height="height" viewBox="0 0 13 12" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path stroke="#fff" stroke-width="1.3" stroke-linecap="round" d="M.65 1.35h11.7M.65 6.35h11.7M6.65 11.35h5.7"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'MenuIcon',
	props: {
		width: {
			type: String,
			default: '13',
		},
		height: {
			type: String,
			default: '12',
		},
	},
});
</script>
