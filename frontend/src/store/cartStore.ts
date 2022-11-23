import { defineStore } from 'pinia';
import Cart from '@/api/cart';
import { AxiosResponse } from 'axios';

const cartApi: Cart = new Cart();

interface cartProductsInterface {
	id: string;
	cnt: number;
}

export const useCartStore = defineStore('cartStore', {
	state: () => ({
		products: [] as cartProductsInterface[],
		cnt: 0,
		modalOpen: false,
	}),
	actions: {
		async getProducts(): Promise<void> {
			const response: AxiosResponse = await cartApi.get();

			if (response.status === 200) {
				this.products = response.data;
				this.cnt = response.data.length;
			}
		},
		async addToCart(id: string): Promise<void> {
			const response: AxiosResponse = await cartApi.add(id, 1);

			if (response.status >= 200 && response.status <= 299) {
				this.products.push({ id, cnt: 1 });
				this.cnt += 1;
				this.modalOpen = true;
			}
		},
		async removeFromCart(id: string): Promise<void> {
			const response: AxiosResponse = await cartApi.remove(id);

			if (response.status === 200) {
				const index = this.products.findIndex(item => item.id === id);

				if (index >= 0) {
					this.products.splice(index, 1);
				}

				this.cnt -= 1;
			}
		},
	},
});
