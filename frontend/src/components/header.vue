<template>
	<header class="header">
		<div class="header__top">
			<div class="container">
				<div class="header__row">
					<RouterLink
						class="header__link"
						:to="{ name: links?.service?.name }"
					>
						{{ links.service?.meta?.name || links?.service?.name }}
					</RouterLink>
					<button class="header__button header__button_modal" type="button">Заказать звонок</button>
					<div class="header__socials">
						<button
							class="header__button header__button_social"
							type="button"
							aria-label="Заказать звонок через whatsApp"
						>
							<WhatsAppIcon/>
						</button>
						<button
							class="header__button header__button_social"
							type="button"
							aria-label="Заказать звонок через telegram"
						>
							<TelegramIcon/>
						</button>
					</div>
				</div>
				<div class="header__contacts">
					<a class="header__phone" href="tel:+79529561997">+7 (952) 956-19-97</a>
					<button
						class="header__contactsTrigger"
						:class="isOpenContacts ? 'active' : ''"
						type="button"
						aria-label="Открыть контакты"
						@click="isOpenContacts = !isOpenContacts"
						ref="outsideContactsButton"
					>
						<CirclePlusIcon />
					</button>
					<transition name="fade">
						<div v-show="isOpenContacts" class="contactsModal" ref="outsideContactsModal">
							<ul class="contactsModal__list">
								<li class="contactsModal__item">
									<div class="contactsModal__name">Сервисный центр</div>
									<a class="contactsModal__link" href="tel:+79529561997">+7 (952) 956-19-97</a>
								</li>
								<li class="contactsModal__item">
									<div class="contactsModal__name">Оптовый отдел</div>
									<a class="contactsModal__link" href="tel:+79529561997">+7 (952) 956-19-97</a>
									<span class="contactsModal__time">пн-сб 10:00 - 19:00</span>
								</li>
								<li class="contactsModal__item">
									<div class="contactsModal__name">Отдел рекламаций и претензий</div>
									<a class="contactsModal__link" href="tel:+79529561997">+7 (952) 956-19-97</a>
									<span class="contactsModal__time">ср-вс с 10:00 до 19:00</span>
								</li>
							</ul>
						</div>
					</transition>
				</div>
			</div>
		</div>
		<div class="header__middle container">
			<h1 class="header__title">
				<RouterLink class="header__logo" to="/">RIG</RouterLink>
			</h1>
			<div class="header__catalog">
				<AppButton ref="outsideButtonMenu" :icon="true" @click="isMenuOpen = !isMenuOpen">
					<template #icon>
						<MenuIcon class="button__icon"/>
					</template>
					Каталог
				</AppButton>
				<AppMenu ref="outsideMenu" :isOpen="isMenuOpen" />
			</div>
			<SearchInput class="header__search" />
			<div class="header__right">
				<RouterLink v-slot="{ href, navigate }" custom :to="{ name: links?.compare.name }">
					<AppChip
						class="header__chip"
						tag="a"
						color="white"
						circle="medium"
						:colorOnHover="true"
						:href="href"
						aria-label="Сравнения"
						@click="navigate"
					>
						<CompareIcon />
					</AppChip>
				</RouterLink>
				<RouterLink v-slot="{ href, navigate }" custom :to="{ name: links?.favorites.name }">
					<AppChip
						class="header__chip"
						tag="a"
						color="white"
						circle="medium"
						:colorOnHover="true"
						:href="href"
						aria-label="Избранное"
						@click="navigate"
					>
						<FavoritesIcon />
					</AppChip>
				</RouterLink>
				<RouterLink v-slot="{ href, navigate }" custom :to="{ name: links?.cart.name }">
					<AppChip
						class="header__chip"
						tag="a"
						color="white"
						:colorOnHover="true"
						:href="href"
						@click="navigate"
					>
						<CartIcon />
						<span class="header__text">{{ links.cart?.meta?.name || links?.cart?.name }}</span>
					</AppChip>
				</RouterLink>
				<CartModal />
			</div>
		</div>
		<div class="header__bottom">
			<nav class="header__nav nav container">
				<router-link class="nav__link" :to="{ name: links?.about.name }">
					{{ links.about?.meta?.name || links?.about?.name }}
				</router-link>
				<router-link class="nav__link" :to="{ name: links?.news.name }">
					{{ links.news?.meta?.name || links?.news?.name }}
				</router-link>
				<router-link class="nav__link" :to="{ name: links?.contacts.name }">
					{{ links.contacts?.meta?.name || links?.contacts?.name }}
				</router-link>
				<router-link class="nav__link" :to="{ name: links?.specials.name }">
					{{ links.specials?.meta?.name || links?.specials?.name }}
					<AppChip class="nav__chip" tag="span" color="primary" circle="small">%</AppChip>
				</router-link>
			</nav>
		</div>
	</header>
</template>

<script lang="ts">
import { defineComponent, ref, ComponentPublicInstance, onMounted } from 'vue';
import type { Ref } from 'vue';
import { RouteRecordNormalized, Router, useRouter } from 'vue-router';
import WhatsAppIcon from '@/components/icons/whatsAppIcon.vue';
import TelegramIcon from '@/components/icons/telegramIcon.vue';
import MenuIcon from '@/components/icons/menuIcon.vue';
import CompareIcon from '@/components/icons/compareIcon.vue';
import FavoritesIcon from '@/components/icons/favoritesIcon.vue';
import CartIcon from '@/components/icons/cartIcon.vue';
import CirclePlusIcon from '@/components/icons/circlePlusIcon.vue';
import SearchInput from '@/components/form/searchInput.vue';
import AppButton from '@/components/button/index.vue';
import AppMenu from '@/components/menu.vue';
import AppChip from '@/components/chip/index.vue';
import CartModal from '@/components/cartModal.vue';
import { useClickOutside } from '@/composables/clickOutside';

export default defineComponent({
	name: 'AppHeader',
	setup() {
		const router: Router = useRouter();
		const routes: RouteRecordNormalized[] = router.getRoutes();
		const useRoutes: RouteRecordNormalized[] = routes.filter(route => [
			'service',
			'compare',
			'favorites',
			'cart',
			'about',
			'news',
			'contacts',
			'specials',
		].includes(route.name as string));
		const links: { [key: string]: RouteRecordNormalized } = {};

		for (const route in useRoutes) {
			links[useRoutes[route].name as string] = useRoutes[route];
		}

		const isMenuOpen: Ref<boolean> = ref(false);
		const outsideMenu: Ref<ComponentPublicInstance | null> = ref(null);
		const outsideButtonMenu: Ref<ComponentPublicInstance | null> = ref(null);

		const isOpenContacts: Ref<boolean> = ref(false);
		const outsideContactsButton: Ref<HTMLElement | null> = ref(null);
		const outsideContactsModal: Ref<HTMLElement | null> = ref(null);

		onMounted(() => {
			useClickOutside([outsideMenu?.value?.$el, outsideButtonMenu?.value?.$el], () => {
				isMenuOpen.value = false;
			});

			useClickOutside([outsideContactsButton?.value, outsideContactsModal?.value], () => {
				isOpenContacts.value = false;
			});
		});

		return {
			links,
			isMenuOpen,
			outsideMenu,
			outsideButtonMenu,
			isOpenContacts,
			outsideContactsButton,
			outsideContactsModal,
		};
	},
	components: {
		WhatsAppIcon,
		TelegramIcon,
		MenuIcon,
		CompareIcon,
		FavoritesIcon,
		CartIcon,
		CirclePlusIcon,
		SearchInput,
		AppButton,
		AppMenu,
		AppChip,
		CartModal,
	},
});
</script>

<style lang="scss" scoped>
	@import '@/assets/css/modules/var';
	@import '@/assets/css/components/icon';
	@import '@/assets/css/components/nav';
	@import '@/assets/css/components/contactsModal';

	.header {
		&__top .container,
		&__row,
		&__socials,
		&__right,
		&__contactsTrigger {
			display: flex;
			justify-content: space-between;
			align-items: center;
		}

		&__top {
			padding: 10px 0;
			border-bottom: 1px solid $hr;
		}

		&__title {
			margin: 0;
		}

		&__link,
		&__button_modal,
		&__phone {
			color: $surface;
			transition: color .2s ease;

			&:hover {
				color: $black;
			}
		}

		&__link,
		&__button_modal {
			font-size: 14px;
		}

		&__button_modal,
		&__socials {
			margin-left: 30px;
		}

		&__button,
		&__contactsTrigger {
			padding: 0;
			border-width: 0;
			background-color: transparent;
		}

		&__button {
			&_social {
				display: flex;

				:deep(.icon__path) {
					transition: fill .2s ease;
				}

				&:hover :deep(.icon_whatsApp .icon__path) {
					fill: $success;
				}

				&:hover :deep(.icon_telegram .icon__path) {
					fill: $secondary-900;
				}
			}

			&_social + &_social {
				margin-left: 10px;
			}
		}

		&__contacts,
		&__middle {
			display: flex;
			align-items: center;
		}

		&__contacts,
		&__catalog,
		&__right {
			position: relative;
		}

		&__contactsTrigger {
			margin-left: 10px;

			:deep(circle),
			:deep(path) {
				transition: stroke .2s ease, fill .2s ease;
			}

			&:hover,
			&.active {
				:deep(circle) {
					stroke: transparent;
					fill: $surface;
				}

				:deep(path) {
					fill: #fff;
				}
			}
		}

		&__middle {
			padding-top: 30px;
			padding-bottom: 30px;
		}

		&__logo {
			font-size: 30px;
			font-weight: bold;
			color: $black;
		}

		&__catalog {
			margin-left: 35px;
		}

		&__search {
			margin-left: 20px;
		}

		&__right {
			margin-left: auto;
			align-items: stretch;
		}

		&__chip {
			color: $black;
		}

		&__chip + &__chip {
			margin-left: 5px;
		}

		&__text {
			margin-left: 10px;
		}

		&__bottom {
			padding: 10px 0;
			background-color: $background;
		}
	}
</style>
