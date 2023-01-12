import { defineStore } from 'pinia';
import Menu from '@/api/menu';
import { AxiosResponse } from 'axios';

const menuApi: Menu = new Menu();

interface subMenuItemInterface {
	type: string;
	item: { item: string; }[];
}

interface menuItemInterface {
	id: string;
	icon: string;
	name: string;
	slug: string;
	submenu: subMenuItemInterface[];
}

export const useMenuStore = defineStore('menuStore', {
	state: () => ({
		cat: [] as menuItemInterface[],
	}),
	actions: {
		async getMenu(): Promise<void> {
			const response: AxiosResponse = await menuApi.get();

			if (response.status === 200) {
				this.cat = response.data;
			}
		},
	},
});
