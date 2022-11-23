import { Meta, StoryFn } from '@storybook/vue3';
import AppButton from '@/components/button/index.vue';
import { colorProp, modProp, sizeProp } from '@/components/button/types';
import MenuIcon from '@/components/icons/menuIcon.vue';

export default {
	title: 'Кнопки',
	component: AppButton,
	argTypes: {
		tag: {
			table: {
				disable: true,
			},
		},
		iconIndent: {
			control: 'number'
		},
		icon: {
			control: 'boolean',
		},
		mod: {
			options: modProp,
			control: 'select',
		},
		color: {
			options: colorProp,
			control: 'select',
		},
		size: {
			options: sizeProp,
			control: 'select',
		},
	},
} as Meta<typeof AppButton>;

const Template: StoryFn<typeof AppButton> = (args) => ({
	components: { AppButton, MenuIcon },
	setup() {
		return { args };
	},
	template: `
		<AppButton v-bind="args">
			<template #icon v-if="args.icon"><MenuIcon /></template>
			{{ args.default }}
		</AppButton>`,
});

export const Primary = Template.bind({});

Primary.args = {
	mod: 'stroke',
	color: 'primary',
	default: 'Нажать',
};

export const Icon = Template.bind({});

Icon.args = {
	color: 'secondary',
	size: 'small',
	icon: true,
	default: 'Каталог',
}
