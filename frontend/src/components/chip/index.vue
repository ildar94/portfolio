<template>
	<component :is="tag" class="chip" :class="chipClasses"><slot></slot></component>
</template>

<script lang="ts">
import { defineComponent, computed, ComputedRef } from 'vue';
import { colorProp, circleProp, modProp } from '@/components/chip/types';

export default defineComponent({
	name: 'AppChip',
	props: {
		tag: {
			type: String,
			default: 'div',
		},
		color: {
			type: String,
			required: true,
			validator: (value: string) => colorProp.includes(value),
		},
		mod: {
			type: String,
			default: 'fill',
			validator: (value: string) => modProp.includes(value),
		},
		colorOnHover: {
			type: Boolean,
			default: false,
		},
		circle: {
			type: String,
			default: '',
			validator: (value: string) => circleProp.includes(value),
		},
	},
	setup(props) {
		const chipClasses: ComputedRef<object> = computed(() => ({
			[`chip_${props.color}_${props.mod}`]: props.color && props.mod,
			chip_hover: props.colorOnHover,
			[`chip_circle_${props.circle}`]: !!props.circle,
		}));

		return {
			chipClasses,
		};
	},
});
</script>

<style lang="scss" scoped>
	@import '@/assets/css/modules/var';

	.chip {
		display: inline-flex;
		justify-content: center;
		align-items: center;
		padding: 10px;
		border: 1px solid transparent;
		border-radius: 2em;
		font-size: 14px;
		line-height: 1;
		color: #fff;
		transition: background-color .2s ease;

		&_white_fill,
		&_primary_stroke,
		&_secondary_stroke,
		&_white_stroke {
			color: $black;
		}

		&_primary_fill:not(&_hover),
		&_hover.chip_primary_fill:hover,
		&_hover.chip_primary_stroke:hover, {
			background-color: $primary;
		}

		&_secondary_fill:not(&_hover),
		&_hover.chip_secondary_fill:hover,
		&_hover.chip_secondary_stroke:hover {
			background-color: $secondary;
		}

		&_white_fill:not(&_hover),
		&_hover.chip_white_fill:hover,
		&_hover.chip_white_stroke:hover {
			background-color: $background;
		}

		&_hover.chip_primary_stroke:hover,
		&_hover.chip_secondary_stroke:hover {
			color: #fff;
		}

		&_primary_stroke {
			border-color: $primary;
		}

		&_secondary_stroke {
			border-color: $secondary;
		}

		&_white_stroke {
			border-color: $background;
		}

		&_circle_small {
			width: 30px;
			height: 30px;
			border-radius: 50%;
		}

		&_circle_medium {
			width: 40px;
			height: 40px;
			border-radius: 50%;
		}

		&_circle_large {
			width: 50px;
			height: 50px;
			border-radius: 50%;
		}
	}
</style>
