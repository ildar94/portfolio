<template>
	<teleport to="body">
			<div v-if="errorStore.errorsCnt" class="errorAlert">
				<transition-group name="wow" tag="ul" class="errorAlert__list" appear>
					<li class="errorAlert__item" v-for="error in errorStore.errors" :key="error.id">
						<div class="errorAlert__title">{{ error.title }}</div>
						<div class="errorAlert__text">{{ error.text }}</div>
						<appButton v-if="error.critical" color="success" mod="stroke" size="small" class="errorAlert__button" @click="reload()">Перезагрузить страницу</appButton>
					</li>
				</transition-group>
			</div>
	</teleport>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import appButton from '@/components/button/index.vue';
import { useErrorStore } from '@/store/errorStore';

export default defineComponent({
	name: 'errorAlert',
	setup() {
		const errorStore = useErrorStore();

		function reload() {
			document.location.reload();
		}

		return {
			errorStore,
			reload,
		};
	},
	components: {
		appButton,
	},
});
</script>

<style lang="scss" scoped>
@import '@/assets/css/modules/var';

.errorAlert {
	position: fixed;
	top: 20px;
	right: 20px;
	z-index: 101;

	&__list {
		margin: 0;
		padding: 0;
		list-style: none;
	}

	&__item {
		max-width: 550px;
		padding: 20px;
		border-radius: 15px;
		background-color: dimgrey;
		color: ghostwhite;
	}

	&__item + &__item {
		margin-top: 15px;
	}

	&__title {
		font-size: 18px;
		font-weight: 500;
	}

	&__text {
		margin-top: 5px;
	}

	&__button {
		margin-top: 10px;
	}
}
</style>
