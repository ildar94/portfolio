import { defineStore } from 'pinia';
import Cart from '@/api/cart';
import { AxiosResponse } from 'axios';
import { CartItemI } from '@/api/cart/types';
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
			return !!state.products.find(item => item.product_id === id);
		},
	},
	actions: {
		async getCartId(): Promise<void> {
			const response = await cartApi.getId();

			if (response.status === 200) {
				this.cartId = response.data[0].id;
			}
		},
		async getProducts(): Promise<void> {
			if (this.cartId === '') {
				await this.getCartId();
			}

			const response = await cartApi.get(this.cartId);

			if (response.status === 200) {
				for (let i = 0; i < response.data.items.length; i++) {
					const item = response.data.items[i];

					if (!item.totalPriceFormat) {
						item.totalPriceFormat = priceFormat(item.total_price);
					}

					if (!item.product.formatPrice) {
						item.product.formatPrice = priceFormat(item.product.price);
					}

					if (!response.data.totalPriceFormat) {
						response.data.totalPriceFormat = priceFormat(response.data.total_price);
					}
				}

				this.products = response.data.items;
				this.cnt = response.data.items.length;
				this.total = response.data.total_price;
				this.totalFormat = response.data.totalPriceFormat;
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
		async editCnt(id: number, cnt: number): Promise<void> {
			const response: AxiosResponse = await cartApi.edit(this.cartId, id, cnt);

			console.log(response);
		},
	},
});
