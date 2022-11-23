<template>
	<svg :width="width" :height="height" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path d="M5.03 1.6h-.16c.1 0 .16-.08.16-.16v.15h5.94v-.15c0 .08.07.15.15.15h-.15V3h1.4V1.44c0-.7-.56-1.25-1.24-1.25H4.87c-.68 0-1.25.56-1.25 1.25V3h1.41V1.6ZM14.87 3H1.13a.62.62 0 0 0-.63.63v.62c0 .09.07.16.16.16h1.18l.48 10.21c.03.67.58 1.2 1.25 1.2h8.86c.67 0 1.22-.53 1.25-1.2l.48-10.21h1.18c.09 0 .16-.07.16-.16v-.63a.62.62 0 0 0-.63-.62Zm-2.59 11.4H3.72l-.48-10h9.52l-.48 10Z" fill="#5D6C7B"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'RemoveIcon',
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
