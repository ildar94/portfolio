<template>
	<h2>Catalog {{ slug }}</h2>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';
import { useRoute } from 'vue-router';

export default defineComponent({
	name: 'subCatalog',
	setup() {
		const route = useRoute();
		const slug = computed(() => route.params?.slug);

		return {
			slug,
		};
	},
});
</script>

<style lang="scss" scoped>

</style>
