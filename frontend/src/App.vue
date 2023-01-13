<template>
	<div class="wrapper">
		<AppHeader />
		<main class="content">
			<RouterView />
		</main>
		<AppFooter />
		<ErrorAlert />
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AppHeader from '@/components/header.vue';
import AppFooter from '@/components/footer.vue';
import ErrorAlert from '@/components/errorAlert.vue';
import { addResponseHandler, errorConfigI } from '@/api';
import { useErrorStore } from '@/store/errorStore';

addResponseHandler(response => response, error => {
	const errorStore = useErrorStore();

	if (error.config.params?.errorConfig) {
		const errorConfig: errorConfigI = error.config.params.errorConfig;

		errorStore.appendError(errorConfig.title, errorConfig.text, errorConfig.critical);
	}

	return Promise.reject(error);
});

export default defineComponent({
	name: 'AppMain',
	components: {
		AppHeader,
		AppFooter,
		ErrorAlert,
	},
});
</script>

<style lang="scss">
	@import './assets/css/modules/normalize';
	@import './assets/css/modules/fonts';
	@import './assets/css/modules/var';
	@import './assets/css/modules/config';
	@import './assets/css/modules/colors';
	@import './assets/css/modules/transitions';
	@import './assets/css/components/icon';
</style>
