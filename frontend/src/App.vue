<template>
	<div class="wrapper">
		<AppHeader />
		<main class="content">
			<RouterView />
		</main>
		<AppFooter />
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AppHeader from '@/components/header.vue';
import AppFooter from '@/components/footer.vue';

export default defineComponent({
	name: 'AppMain',
	components: {
		AppHeader,
		AppFooter,
	},
});
</script>

<style lang="scss">
	@import './assets/css/modules/normalize';
	@import './assets/css/modules/fonts';
	@import './assets/css/modules/var';
	@import './assets/css/modules/config';
	@import './assets/css/modules/colors';
	@import './assets/css/components/icon';
</style>
