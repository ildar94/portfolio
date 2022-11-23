import { api } from '@/api';
import { AxiosResponse, AxiosInstance } from 'axios';

class mainProducts {
	private api: AxiosInstance;

	constructor() {
		this.api = api;
	}

	public get(): Promise<AxiosResponse> {
		return this.api.get('mainProducts');
	}
}

export default mainProducts;
