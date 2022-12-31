<template>
	<svg :width="width" :height="height" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
		<path clip-rule="evenodd" d="M12 3.75a3.26 3.26 0 0 0-3.33 3.19A3.26 3.26 0 0 0 12 10.12a3.26 3.26 0 0 0 3.33-3.18A3.26 3.26 0 0 0 12 3.75ZM7.17 6.94A4.76 4.76 0 0 1 12 2.25a4.76 4.76 0 0 1 4.83 4.69A4.76 4.76 0 0 1 12 11.62a4.76 4.76 0 0 1-4.83-4.68Zm7.5 8.03c-1.77-.3-3.57-.3-5.34 0l-.2.03-.13-.74.13.74a4.12 4.12 0 0 0-3.38 4.11c0 .65.5 1.14 1.08 1.14h10.34c.57 0 1.08-.49 1.08-1.14 0-2.06-1.45-3.79-3.38-4.1l.13-.75-.13.74-.2-.03Zm.24-1.48-.12.74.12-.74.2.03a5.61 5.61 0 0 1 4.64 5.6 2.6 2.6 0 0 1-2.58 2.63H6.83a2.6 2.6 0 0 1-2.58-2.64 5.61 5.61 0 0 1 4.63-5.59l.21-.03.12.74-.12-.74c1.93-.32 3.9-.32 5.82 0Z" :fill="fill" fill-rule="evenodd"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'userIcon',
	props: {
		width: {
			type: String,
			default: '20',
		},
		height: {
			type: String,
			default: '20',
		},
		fill: {
			type: String,
			default: '#282739',
		},
	},
});
</script>

<style scoped>

</style>
