import { api } from '@/api';
import { AxiosInstance, AxiosResponse } from 'axios';

class Promo {
	private api: AxiosInstance;

	constructor() {
		this.api = api;
	}

	public getMainBanner(): Promise<AxiosResponse> {
		return this.api.get('promo/mainbanner/');
	}
}

export default Promo;
