import { defineStore } from 'pinia';
import MainProducts from '@/api/mainProducts';
import { ProductI } from '@/api/mainProducts/types';
import { priceFormat } from '@/utils/format';

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

						item.priceFormat = priceFormat(item.price);

						if (item?.sales_price) {
							item.salesPriceFormat = priceFormat(item.sales_price);
						} else {
							item.salesPriceFormat = null;
						}
					}

					this.products = response.data.results;
				}
			} catch (e) {
				console.warn(e);
			}
		},
	},
});
