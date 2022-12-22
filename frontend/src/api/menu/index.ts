import { api } from '@/api';
import { AxiosResponse, AxiosInstance } from 'axios';

class Menu {
	private api: AxiosInstance;

	constructor() {
		this.api = api;
	}

	public get(): Promise<AxiosResponse> {
		return this.api.get('shop/menu/');
	}
}

export default Menu;
