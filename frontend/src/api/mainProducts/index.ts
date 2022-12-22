import { api } from '@/api';
import { AxiosResponse, AxiosInstance } from 'axios';
import { ProductsResponseHeadI } from '@/api/mainProducts/types';

class mainProducts {
	private api: AxiosInstance;

	constructor() {
		this.api = api;
	}

	public get(): Promise<AxiosResponse<ProductsResponseHeadI>> {
		return this.api.get('products/');
	}
}

export default mainProducts;
