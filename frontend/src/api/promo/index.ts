import { api } from '@/api';
import { AxiosInstance, AxiosResponse } from 'axios';

class Promo {
	private api: AxiosInstance;

	constructor() {
		this.api = api;
	}

	// todo В дальнейшем нужно сделать get под каждую сущность внутри промо, чтобы не тянуть все сразу
	public get(): Promise<AxiosResponse> {
		return this.api.get('promo');
	}
}

export default Promo;
