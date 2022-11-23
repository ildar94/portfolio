<template>
	<svg class="icon icon_whatsApp" :class="colorClass" :width="width" :height="height" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg">
		<g clip-path="url(#a)">
			<path class="icon__path" d="M9.5.5a9 9 0 0 0-7.58 13.85L.52 18a.37.37 0 0 0 .48.48l3.75-1.33A9 9 0 1 0 9.5.5Z" />
			<path fill="#fff" d="m13.78 11.04-1.5-.75c-.64-.34-1.4.29-1.77.65a4.51 4.51 0 0 1-1.5-.96 4.5 4.5 0 0 1-.96-1.5c.36-.36.99-1.13.65-1.78-.3-.57-.75-1.5-.75-1.5a.37.37 0 0 0-.33-.2h-.75A2.26 2.26 0 0 0 5 7.25c0 1.18 1.4 3.44 2.35 4.39.95.95 3.21 2.36 4.4 2.36 1.1 0 2.05-.79 2.24-1.88v-.75a.37.37 0 0 0-.2-.33Z" />
		</g>
		<defs>
			<clipPath id="a">
				<path fill="#fff" transform="translate(.5 .5)" d="M0 0h18v18H0z"/>
			</clipPath>
		</defs>
	</svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useIconColor } from '@/composables/iconColor';

export default defineComponent({
	name: 'WhatsAppIcon',
	props: {
		color: {
			type: String,
			default: 'gray',
		},
		width: {
			type: String,
			default: '19',
		},
		height: {
			type: String,
			default: '19',
		},
	},
	setup(props) {
		const colorClass = useIconColor(props.color);

		return {
			colorClass,
		};
	},
});
</script>
