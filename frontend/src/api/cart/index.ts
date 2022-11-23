import { api } from '@/api';
import { AxiosResponse, AxiosInstance } from 'axios';

// Cart

class Cart {
	private api: AxiosInstance;

	constructor() {
		this.api = api;
	}

	public get(): Promise<AxiosResponse> {
		return this.api.get('cart');
	}

	public add(id: string, cnt: number): Promise<AxiosResponse> {
		return this.api.post('cart', { id, cnt });
	}

	public remove(id: string): Promise<AxiosResponse> {
		return this.api.delete(`cart/${id}`);
	}
}

export default Cart;
