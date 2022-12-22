import { defineStore } from 'pinia';
import Promo from '@/api/promo';
import { AxiosResponse } from 'axios';

const promoApi: Promo = new Promo();

interface mainBannerItemInterface {
	id: string;
	title: string;
	description: string;
	image: string;
	category: string;
}

export const usePromoStore = defineStore('promoStore', {
	state: () => ({
		mainBanner: [] as mainBannerItemInterface[],
	}),
	actions: {
		async getMainBanner(): Promise<void> {
			const response: AxiosResponse = await promoApi.getMainBanner();

			if (response.status === 200) {
				this.mainBanner = response.data?.results;
			}
		},
	},
});
