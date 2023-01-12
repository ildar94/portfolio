import { defineStore } from 'pinia';
import Cart from '@/api/cart';
import { AxiosResponse } from 'axios';
import { CartItemI, CartResponseI } from '@/api/cart/types';
import { priceFormat } from '@/utils/format';

const cartApi: Cart = new Cart();

export const useCartStore = defineStore('cartStore', {
	state: () => ({
		cartId: '',
		products: [] as CartItemI[],
		cnt: 0,
		total: 0,
		totalFormat: '',
		modalOpen: false,
	}),
	getters: {
		isInCart: (state) => (id: number) => {
			return !!state.products.find(item => item.product.id === id);
		},
	},
	actions: {
		async getCartId(): Promise<CartResponseI | null> {
			const response = await cartApi.getId();

			if (response.status === 200) {
				this.cartId = response.data[0].id;

				return response.data[0];
			}

			return null;
		},
		async getProducts(): Promise<void> {
			let cart: CartResponseI | null = null;

			if (this.cartId === '') {
				cart = await this.getCartId();
			}

			if (cart) {
				let data: CartResponseI;

				if (cart.items.length) {
					data = cart;
				} else {
					const response = await cartApi.get(this.cartId);

					if (response.status === 200) {
						data = response.data;
					}

					throw response.status;
				}

				data.items = data.items.map(item => {
					if (!item.totalPriceFormat) item.totalPriceFormat = priceFormat(item.total_price);
					if (!item.product.formatPrice) item.product.formatPrice = priceFormat(item.product.price);

					return item;
				});

				if (!data.totalPriceFormat) data.totalPriceFormat = priceFormat(data.total_price);

				this.products = data.items;
				this.cnt = data.items.length;
				this.total = data.total_price;
				this.totalFormat = data.totalPriceFormat;
			}
		},
		async addToCart(id: number): Promise<void> {
			const response = await cartApi.add(this.cartId, id, 1);

			if (response.status === 201) {
				await this.getProducts();

				this.modalOpen = true;
			}
		},
		async removeFromCart(id: number): Promise<void> {
			const response: AxiosResponse = await cartApi.remove(this.cartId, id);

			if (response.status === 204) {
				const index = this.products.findIndex(item => item.id === id);

				if (index >= 0) {
					this.products.splice(index, 1);
				}

				this.cnt -= 1;

				if (!this.products.length) {
					this.total = 0;
					this.totalFormat = '';
					this.modalOpen = false;
				}
			}
		},
	},
});
