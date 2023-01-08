<template>
	<input
		class="input"
		:type="type"
		:placeholder="placeholder"
		:name="name"
		:value="modelValue"
		@input="$emit('update:modelValue', $event.target.value)"
	>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

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
			type: String,
			default: '',
		},
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
