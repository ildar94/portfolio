<template>
	<svg :width="width" :height="height" viewBox="0 0 20 18" fill="none" xmlns="http://www.w3.org/2000/svg">
		<path d="M19.152 6.254h-4.149L12.676.924a.586.586 0 1 0-1.074.47l2.122 4.86H6.276l2.122-4.86a.586.586 0 0 0-1.074-.47l-2.327 5.33H.847c-.542 0-.945.492-.826 1.009l2.185 9.517c.087.377.43.646.827.646h13.934c.397 0 .74-.268.827-.646l2.185-9.517c.119-.517-.284-1.009-.827-1.009ZM5.107 8.051a.586.586 0 0 1-.537-.82l.44-1.008h1.28L5.643 7.7a.586.586 0 0 1-.537.351Zm1.963 6.25a.586.586 0 1 1-1.172 0v-4.297a.586.586 0 1 1 1.172 0v4.297Zm3.516 0a.586.586 0 0 1-1.172 0v-4.297a.586.586 0 1 1 1.172 0v4.297Zm3.516 0a.586.586 0 0 1-1.172 0v-4.297a.586.586 0 0 1 1.172 0v4.297Zm1.025-6.299a.583.583 0 0 1-.771-.302l-.645-1.477h1.278l.44 1.008a.586.586 0 0 1-.302.771Z" fill="#6F73EE"/>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'CompareIcon',
	props: {
		width: {
			type: String,
			default: '20',
		},
		height: {
			type: String,
			default: '18',
		},
	},
});
</script>
