<template>
	<component
		:is="tag"
		class="button"
		:class="buttonClasses"
		:type="type"
		@click="$emit('click')"
	>
		<span v-if="icon" class="button__icon" :style="{ 'marginRight': `${iconIndent}px` }">
			<slot name="icon"></slot>
		</span>
		<slot></slot>
	</component>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';
import type { ComputedRef } from 'vue';
import { colorProp, modProp, sizeProp } from '@/components/button/types';

export default defineComponent({
	name: 'AppButton',
	emits: ['click'],
	props: {
		tag: {
			type: String,
			default: 'button',
		},
		type: {
			type: String,
			default: 'button',
			validator: (value: string) => ['button', 'submit', 'reset'].includes(value),
		},
		icon: {
			type: Boolean,
			default: false,
		},
		iconIndent: {
			type: String,
			default: '15',
		},
		color: {
			type: String,
			default: 'primary',
			validator: (value: string) => colorProp.includes(value),
		},
		mod: {
			type: String,
			default: 'fill',
			validator: (value: string) => modProp.includes(value),
		},
		size: {
			type: String,
			default: 'medium',
			validator: (value: string) => sizeProp.includes(value),
		},
	},
	setup(props) {
		const buttonClasses: ComputedRef<object> = computed(() => ({
			button_icon: props.icon,
			[`button_${props.color}_${props.mod}`]: props.color && props.mod,
			[`button_${props.size}`]: props.size,
		}));

		return {
			buttonClasses,
		};
	},
});
</script>

<style lang="scss" scoped>
	@import '@/assets/css/modules/var';

	.button {
		border-width: 1px;
		border-style: solid;
		border-radius: 5px;
		background-color: transparent;
		font-weight: 500;
		transition: background-color .2s ease, color .2s ease;
		outline: none;

		&_icon {
			display: inline-flex;
			justify-content: center;
			align-items: center;
			line-height: 1;
		}

		&_primary_fill {
			background-color: $primary;
			border-color: $primary;
			color: #fff;

			&:hover,
			&:focus-visible {
				background-color: $primary-800;
			}
		}

		&_primary_stroke {
			border-color: $primary;
			color: $primary;

			&:hover,
			&:focus-visible {
				background-color: $primary;
				color: #fff;
			}
		}

		&_secondary_fill {
			background-color: $secondary;
			border-color: $secondary;
			color: #fff;

			&:hover,
			&:focus-visible {
				background-color: $secondary-900;
			}
		}

		&_secondary_stroke {
			border-color: $secondary;
			color: $secondary;

			&:hover,
			&:focus-visible {
				background-color: $secondary;
				color: #fff;
			}
		}

		&_tertiary_fill {
			background-color: $background;
			border-color: $background;
			color: $surface;

			&:hover,
			&:focus-visible {
				background-color: transparent;
				border-color: $primary;
				color: $primary;
			}
		}

		&_tertiary_stroke {
			border-color: $background;
			color: $surface;

			&:hover,
			&:focus-visible {
				background-color: $primary;
				border-color: $primary;
				color: #fff;
			}
		}

		&_success_fill {
			background-color: $success;
			border-color: $success;
			color: #fff;

			&:hover,
			&:focus-visible {
				background-color: $success-800;
				color: #fff;
			}
		}

		&_success_stroke {
			border-color: $success;
			color: $success;

			&:hover,
			&:focus-visible {
				background-color: $success-800;
				color: #fff;
			}
		}

		&_white_fill {
			background-color: #fff;
			border-color: #fff;
			color: $primary;

			&:hover,
			&:focus-visible {
				background-color: $background;
			}
		}

		&_white_stroke {
			border-color: #fff;
			color: #fff;

			&:hover,
			&:focus-visible {
				background-color: #fff;
				color: $primary;
			}
		}

		&_small {
			min-width: 80px;
			min-height: 30px;
			padding: 5px 10px;
		}

		&_medium {
			min-width: 115px;
			min-height: 40px;
			padding: 8px 15px;
		}

		&_large {
			min-width: 140px;
			min-height: 50px;
			padding: 15px 25px;
		}

		&__icon {
			display: flex;
		}
	}
</style>
