<template>
	<div class="feature">
		<FeatureSpriteIcon class="feature__icon" v-if="icon" :name="icon"></FeatureSpriteIcon>
		<span class="feature__text">{{ text }}</span>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FeatureSpriteIcon from '@/components/icons/featureSpriteIcon.vue';

export default defineComponent({
	name: 'appFeature',
	props: {
		icon: {
			type: String,
			default: '',
		},
		text: {
			type: String,
			required: true,
		},
	},
	components: {
		FeatureSpriteIcon,
	},
});
</script>

<style lang="scss" scoped>
@import '@/assets/css/modules/var';

.feature {
	display: inline-flex;
	align-items: center;

	&__icon {
		width: 18px;
		height: 18px;
	}

	&__text {
		margin-left: 10px;
		font-size: 14px;
		color: $surface;
	}
}
</style>
