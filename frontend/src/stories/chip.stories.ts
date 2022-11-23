import { Meta, StoryFn } from '@storybook/vue3';
import AppChip from '@/components/chip/index.vue';
import { colorProp, circleProp, modProp } from '@/components/chip/types';

export default {
	title: 'Чип',
	component: AppChip,
	argTypes: {
		tag: {
			table: {
				disable: true,
			},
		},
		color: {
			options: colorProp,
			control: 'select',
		},
		circle: {
			options: circleProp,
			control: 'select',
		},
		mod: {
			options: modProp,
			control: 'select',
		},
		colorOnHover: {
			control: 'boolean',
		},
	},
} as Meta<typeof AppChip>;

const Template: StoryFn<typeof AppChip> = (args) => ({
	components: { AppChip },
	setup() {
		return { args };
	},
	template: `
		<AppChip v-bind="args">{{ args.default }}</AppChip>`,
});

export const Primary = Template.bind({});

Primary.args = {
	color: 'primary',
	default: 'Корзина',
};

export const Circle = Template.bind({});

Circle.args = {
	color: 'secondary',
	circle: 'medium',
	default: '%',
}

export const Hover = Template.bind({});

Hover.args = {
	color: 'white',
	colorOnHover: true,
	default: 'Наведи и я закрашусь',
}
