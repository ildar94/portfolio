import { defineStore } from 'pinia';
import { ProductCardProps } from '@/components/productCard/types';
import MainProducts from '@/api/mainProducts';
import { AxiosResponse } from 'axios';

const mainProducts = new MainProducts();

export const useMainProductsStore = defineStore('mainProductsStore', {
	state: () => ({
		products: [] as ProductCardProps[],
	}),
	actions: {
		async get(): Promise<void> {
			const response: AxiosResponse = await mainProducts.get();

			if (response.status === 200) {
				this.products = response.data;
			}
		},
	},
});
