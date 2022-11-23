<template>
	<svg :width="width" :height="height" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
		<circle cx="9" cy="9" r="8.5" stroke="#5D6C7B"/>
		<path d="M5 9.65h8v-1.3H5v1.3ZM8.3 5v8h1.4V5H8.3Z" fill="#5D6C7B"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'CirclePlusIcon',
	props: {
		width: {
			type: String,
			default: '18',
		},
		height: {
			type: String,
			default: '18',
		},
	},
});
</script>
