<template>
	<svg :width="width" :height="height" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path d="m15.95 14.85-5.2-5.2A5.96 5.96 0 0 0 6 0 5.96 5.96 0 0 0 .01 6.01a5.96 5.96 0 0 0 6 6c1.34 0 2.61-.44 3.65-1.24l5.2 5.2a.16.16 0 0 0 .18.03l.05-.04.87-.87a.16.16 0 0 0 .04-.18.16.16 0 0 0-.04-.05ZM9.17 9.17a4.46 4.46 0 0 1-6.34 0 4.46 4.46 0 0 1 0-6.34 4.46 4.46 0 0 1 6.34 0 4.46 4.46 0 0 1 0 6.34Z" fill="#fff"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'SearchIcon',
	props: {
		width: {
			type: String,
			default: '16',
		},
		height: {
			type: String,
			default: '16',
		},
	},
});
</script>
