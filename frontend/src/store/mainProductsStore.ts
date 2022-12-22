import { defineStore } from 'pinia';
import MainProducts from '@/api/mainProducts';
import { ProductI } from '@/api/mainProducts/types';

const mainProducts = new MainProducts();

export const useMainProductsStore = defineStore('mainProductsStore', {
	state: () => ({
		products: [] as ProductI[],
	}),
	actions: {
		async get(): Promise<void> {
			try {
				const response = await mainProducts.get();

				if (response.status === 200) {
					this.products = response.data.results;
				}
			} catch (e) {
				console.warn(e);
			}
		},
	},
});
