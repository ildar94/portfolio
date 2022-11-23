<template>
	<label class="searchInput">
		<AppInput class="searchInput__input" v-model="value" :placeholder="placeholder" />
		<AppButton
			@click="$emit('update:modelValue', value)"
			class="searchInput__button"
			:icon="true"
			icon-indent="0"
		>
			<template #icon>
				<SearchIcon class="searchInput__icon" />
			</template>
		</AppButton>
	</label>
</template>

<script lang="ts">
import { defineComponent, ref, watchEffect } from 'vue';
import type { Ref } from 'vue';
import AppInput from '@/components/form/input.vue';
import AppButton from '@/components/button/index.vue';
import SearchIcon from '@/components/icons/searchIcon.vue';

export default defineComponent({
	name: 'SearchInput',
	emits: ['update:modelValue'],
	props: {
		placeholder: {
			type: String,
			default: 'Поиск',
		},
		modelValue: {
			type: String,
			default: '',
		},
	},
	setup(props, { emit }) {
		const value: Ref<string> = ref(props.modelValue);

		watchEffect(() => {
			emit('update:modelValue', value.value);
		});

		return {
			value,
		};
	},
	components: {
		AppInput,
		AppButton,
		SearchIcon,
	},
});
</script>

<style lang="scss" scoped>
	@import "@/assets/css/modules/var";

	.searchInput {
		display: flex;
		max-width: 650px;
		width: 100%;

		&__input {
			padding: 0 20px;
			border-top-right-radius: 0;
			border-bottom-right-radius: 0;
			border-color: $primary;
			font-size: 14px;
		}

		&__button {
			display: flex;
			justify-content: center;
			align-items: center;
			min-width: 40px;
			height: 40px;
			border-radius: 0 5px 5px 0;
		}
	}
</style>
