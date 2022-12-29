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
					for (let i = 0; i < response.data.results.length; i++) {
						const item = response.data.results[i];

						item.priceFormat = new Intl.NumberFormat('ru', { style: 'currency', currency: 'RUB', maximumFractionDigits: 2 }).format(item.price);

						if (item?.sales_price) {
							item.salesPriceFormat = new Intl.NumberFormat('ru', { style: 'currency', currency: 'RUB' }).format(item?.sales_price);
						}

						item.salesPriceFormat = null;
					}

					this.products = response.data.results;
				}
			} catch (e) {
				console.warn(e);
			}
		},
	},
});
