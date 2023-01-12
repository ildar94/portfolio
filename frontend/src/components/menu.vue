<template>
	<transition name="fade">
		<div v-show="isOpen" class="menu">
			<ul class="menu__list">
				<li
					v-for="(item, index) in menu.cat"
					:key="item.id"
					class="menu__item"
				>
					<router-link :to="`/catalog/${item.slug}`" custom v-slot="{ href, navigate }">
						<a
							class="menu__link"
							:class="index === activeCatIndex ? 'active' : ''"
							:href="href"
							@click.prevent="openCat($event, index, navigate)"
						>
							<svg class="menu__icon">
								<use :xlink:href="`#${item.icon}`"></use>
							</svg>
							<span class="menu__text">{{ item.name }}</span>
						</a>
					</router-link>
				</li>
			</ul>
			<template v-for="(item, index) in menu.cat" :key="item.id">
				<div v-if="index === activeCatIndex" class="menu__box">
					<div
						v-for="subItem in item.submenu"
						:key="subItem.type"
						class="menu__column"
					>
						<h3 class="menu__title">{{ subItem.type }}</h3>
						<div class="menu__links">
							<router-link
								v-for="link in subItem.item"
								:key="link.item"
								:to="`/catalog/${item.slug}/${link.item}`"
								class="menu__link"
							>
								{{ link.item }}
							</router-link>
						</div>
					</div>
				</div>
			</template>
			<MenuSpriteIcon/>
		</div>
	</transition>
</template>

<script lang="ts">
import { defineComponent, ref, Ref } from 'vue';
import MenuSpriteIcon from '@/components/icons/menuSpriteIcon.vue';
import { useMenuStore } from '@/store/menuStore';
import { NavigationFailure } from 'vue-router';

export default defineComponent({
	name: 'AppMenu',
	props: {
		isOpen: {
			type: Boolean,
			default: false,
		},
	},
	setup() {
		const menu = useMenuStore();
		menu.getMenu();

		const activeCatIndex: Ref<number> = ref(0);

		function openCat(
			e: PointerEvent,
			index: number,
			navigate: (e?: (MouseEvent | undefined)) => Promise<void | NavigationFailure>,
		) {
			const target: HTMLElement = e.currentTarget as HTMLElement;

			if (target.classList.contains('active')) {
				navigate();
			}

			activeCatIndex.value = index;
		}

		return {
			menu,
			activeCatIndex,
			openCat,
		};
	},
	components: {
		MenuSpriteIcon,
	},
});
</script>

<style lang="scss" scoped>
	@import '@/assets/css/modules/var';

	.menu {
		position: absolute;
		left: 0;
		top: 100%;
		margin-top: 20px;
		display: flex;
		padding: 10px;
		border-radius: 5px;
		background-color: #fff;
		box-shadow: 0 10px 30px rgba(111, 115, 238, .1);
		z-index: 2;

		&__list {
			margin: 0;
			padding: 13px 25px;
			list-style: none;
			border-radius: 5px;
			background-color: $background;
		}

		&__item {
			.menu__link {
				display: inline-flex;
				align-items: center;
				padding: 7px 0;
				border-bottom: 1px solid transparent;
				font-size: 16px;
				font-weight: 500;
				color: $black;
			}
		}

		&__link {
			display: block;
			padding: 5px 0;
			font-size: 14px;
			color: $surface;

			:deep(svg) {
				fill: $surface;
			}

			&.active,
			&:hover {
				:deep(svg) {
					fill: $primary;
				}

				color: $primary;
			}

			&.active {
				border-bottom-color: $primary;
			}
		}

		&__icon {
			max-width: 16px;
			max-height: 16px;
		}

		&__text {
			margin-left: 10px
		}

		&__box {
			display: flex;
			flex-wrap: wrap;
			max-width: 600px;
			width: 100vw;
		}

		&__column {
			max-width: 170px;
			margin: 20px 30px;
		}

		&__title {
			margin: 0 0 10px;
			font-size: 16px;
			font-weight: 500;
		}
	}
</style>
