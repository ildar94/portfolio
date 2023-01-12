<template>
	<svg :width="width" :height="height" viewBox="0 0 29 29" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path :fill="fill" d="M21.59 7.45 7.44 21.59l-.74-.74L20.84 6.7z"/>
		<path :fill="fill" d="M20.5 21.92 6.37 7.78l.71-.71 14.14 14.14z"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'crossIcon',
	props: {
		width: {
			type: String,
			default: '29',
		},
		height: {
			type: String,
			default: '29',
		},
		fill: {
			type: String,
			default: '#5D6C7B',
		},
	},
});
</script>

<style scoped>

</style>
