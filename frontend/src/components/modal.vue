<template>
	<transition name="fade">
		<div v-if="show" class="modal">
			<div class="modal__inner">
				<Chip
					class="modal__close"
					color="white"
					:color-on-hover="true"
					circle="medium"
					tag="button"
					type="button"
					aria-label="Закрыть"
					@click="$emit('close')"
				>
					<CrossIcon fill="none" />
				</Chip>
				<div class="modal__header">
					<h2 class="modal__title title-h2">{{ title }}</h2>
				</div>
				<div class="modal__content">
					<slot></slot>
					<div v-if="$slots.footer" class="modal__footer">
						<slot name="footer"></slot>
					</div>
				</div>
			</div>
		</div>
	</transition>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Chip from '@/components/chip/index.vue';
import CrossIcon from '@/components/icons/crossIcon.vue';

export default defineComponent({
	name: 'appModal',
	emits: ['close'],
	props: {
		show: {
			type: Boolean,
			default: false,
		},
		title: {
			type: String,
			default: 'Modal header title',
		},
	},
	components: {
		Chip,
		CrossIcon,
	},
});
</script>

<style lang="scss" scoped>
@import '@/assets/css/modules/var';
@import '@/assets/css/modules/polygraphy';

.modal {
	position: fixed;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background-color: rgba($black, .5);
	z-index: 100;

	&__close {
		position: absolute;
		top: 10px;
		right: 10px;
		padding: 0;
		border-width: 0;
		background-color: transparent;

		:deep(path) {
			fill: $surface;
			transition: fill .2s ease;
		}

		&:hover {
			:deep(path) {
				fill: $primary;
			}
		}
	}

	&__inner {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		border-radius: 5px;
		padding-top: 40px;
		padding-bottom: 40px;
		background: #fff;
	}

	&__header,
	&__content {
		padding-left: 40px;
		padding-right: 40px;
	}

	&__header {
		padding-bottom: 15px;
	}

	&__content {
		padding-top: 15px;
		padding-bottom: 15px;
	}

	&__footer {
		padding-top: 15px;
	}

	&__title {
		margin: 0;
		line-height: 1;
	}
}
</style>
