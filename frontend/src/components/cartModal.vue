<template>
	<transition name="fade">
		<div v-show="cart.modalOpen" class="cartModal" ref="outsideCartModal">
			<div class="cartModal__header">
				<h2 class="cartModal__title">В вашей корзине</h2>
				<div class="cartModal__cnt">{{ cart.cnt }} товара</div>
			</div>
			<div class="cartModal__content">
				<ul class="cartModal__list">
					<li
						v-for="product in cart.products"
						:key="product.id"
						class="cartModal__item">
						<div class="cartModal__product">
							<div class="cartModal__image">
								<img class="cartModal__img" src="@/assets/img/misc/product.png" alt="Kugoo Kirin M4">
							</div>
							<div class="cartModal__desc">
								<div class="cartModal__name">Kugoo Kirin M4</div>
								<div class="cartModal__info">
									<span class="cartModal__price">29 900 ₽</span>
									<span class="cartModal__count">{{ product.cnt }} шт.</span>
								</div>
							</div>
						</div>
						<button
							class="cartModal__button"
							type="button"
							aria-label="Удалить"
							@click="cart.removeFromCart(product.id)"
						>
							<RemoveIcon />
						</button>
					</li>
				</ul>
			</div>
			<div class="cartModal__footer">
				<div class="cartModal__total">
					<div class="cartModal__key">Сумма:</div>
					<div class="cartModal__val">59 800 ₽</div>
				</div>
				<AppButton>Оформить заказ</AppButton>
			</div>
		</div>
	</transition>
</template>

<script lang="ts">
import { defineComponent, ref, Ref, onMounted } from 'vue';
import RemoveIcon from '@/components/icons/removeIcon.vue';
import AppButton from '@/components/button/index.vue';
import { useCartStore } from '@/store/cartStore';
import { useClickOutside } from '@/composables/clickOutside';

export default defineComponent({
	name: 'CartModal',
	setup() {
		const cart = useCartStore();

		cart.getProducts();

		const outsideCartModal: Ref<HTMLElement | null> = ref(null);

		onMounted(() => {
			useClickOutside(outsideCartModal?.value, () => {
				cart.modalOpen = false;
			});
		});

		return {
			cart,
			outsideCartModal,
		};
	},
	components: {
		RemoveIcon,
		AppButton,
	},
});
</script>

<style lang="scss" scoped>
	@import '@/assets/css/modules/var';

	.cartModal {
		position: absolute;
		top: 100%;
		right: 0;
		margin-top: 10px;
		min-width: 305px;
		border-radius: 5px;
		background-color: #fff;
		box-shadow: 0 10px 30px rgba(111, 115, 238, .1);

		&__header,
		&__footer,
		&__item {
			padding: 15px 20px;
		}

		&__header,
		&__item,
		&__product,
		&__image,
		&__footer {
			display: flex;
			justify-content: space-between;
			align-items: center;
		}

		&__header {
			border-radius: 5px 5px 0 0;
			background-color: $background;
		}

		&__title {
			margin: 0;
			font-size: 16px;
			font-weight: 500;
		}

		&__cnt {
			font-size: 14px;
			color: $surface;
		}

		&__list {
			margin: 0;
			max-height: 200px;
			padding: 0;
			list-style: none;
			overflow-y: auto;
			overflow-x: hidden;
		}

		&__item {
			border-bottom: 1px solid $border;
		}

		&__image {
			width: 50px;
			height: 50px;
			border-radius: 50%;
			background-color: $productBackground;
			overflow: hidden;
		}

		&__desc {
			margin-left: 15px;
		}

		&__name,
		&__info {
			font-size: 14px;
		}

		&__name {
			font-size: 14px;
			font-weight: 500;
		}

		&__info {
			margin-top: 5px;
		}

		&__count {
			margin-left: 10px;
		}

		&__button {
			display: flex;
			padding: 5px 0;
			border-width: 0;
			background-color: transparent;

			:deep(path) {
				transition: fill .2s ease;
			}

			&:hover {
				:deep(path) {
					fill: $danger;
				}
			}
		}

		&__footer {
			position: sticky;
			left: 0;
			right: 0;
			bottom: 0;
			border-radius: 0 0 5px 5px;
			box-shadow: 0px -4px 50px rgba(0, 0, 0, .1);
		}
	}
</style>
