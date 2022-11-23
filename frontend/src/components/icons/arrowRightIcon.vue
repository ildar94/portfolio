<template>
	<svg :width="width" :height="height" viewBox="0 0 7 12" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path d="M6.53 6.53c.3-.3.3-.77 0-1.06L1.76.7A.75.75 0 0 0 .7 1.76L4.94 6 .7 10.24a.75.75 0 0 0 1.06 1.06l4.77-4.77ZM5 6.75h1v-1.5H5v1.5Z" fill="#fff"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'ArrowRightIcon',
	props: {
		width: {
			type: String,
			default: '7',
		},
		height: {
			type: String,
			default: '12',
		},
	},
});
</script>
