<template>
	<input
		class="input"
		:type="type"
		:placeholder="placeholder"
		:name="name"
		:value="valueView"
		v-maska="maskConvert"
		@input="onInput"
	/>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';
import type { ComputedRef } from 'vue';
import { maska } from 'maska';

interface modelValueEmit {
	value: string;
	rawValue: string;
}

export default defineComponent({
	name: 'AppInput',
	emits: ['update:modelValue'],
	props: {
		type: {
			type: String,
			default: 'text',
		},
		placeholder: {
			type: String,
			default: '',
		},
		name: {
			type: String,
			default: '',
		},
		modelValue: {
			type: [Object as () => modelValueEmit, String],
			default: '',
		},
		mask: {
			type: String,
			default: '',
		},
	},
	setup(props, { emit }) {
		function onInput(event: Event) {
			const target: HTMLInputElement = event.target as HTMLInputElement;

			if (props.mask) {
				const modelValue: modelValueEmit = {
					value: target.value,
					rawValue: `${target.dataset.maskRawValue}`,
				};

				emit('update:modelValue', modelValue);
			} else {
				emit('update:modelValue', target.value);
			}
		}

		const maskConvert: ComputedRef<string> = computed(() => props.mask ? props.mask : '');
		const valueView: ComputedRef<string | modelValueEmit> = computed(() => {
			if (props.mask) {
				const modelValue: modelValueEmit = props.modelValue as modelValueEmit;

				return modelValue.value;
			}

			return props.modelValue;
		});

		return {
			onInput,
			maskConvert,
			valueView,
		};
	},
	directives: {
		maska,
	},
});
</script>

<style lang="scss" scoped>
	@import "@/assets/css/modules/var";

	.input {
		display: inline-block;
		width: 100%;
		padding: 15px 25px;
		border: 1px solid $border;
		border-radius: 5px;
		color: $black;
		letter-spacing: .1em;
		transition: border-color .2s ease, color .2s ease;
		outline: none;

		&::placeholder {
			color: $surface;
		}

		&:focus {
			border-color: $primary;
			color: $black;
		}
	}
</style>
