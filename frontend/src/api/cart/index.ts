import { api } from '@/api';
import { AxiosResponse, AxiosInstance } from 'axios';
import { CartResponseI, CartAddResponseI } from '@/api/cart/types';

class Cart {
	private api: AxiosInstance;

	constructor() {
		this.api = api;
	}

	public getId(): Promise<AxiosResponse<CartResponseI[]>> {
		return this.api.get('cart/carts/');
	}

	public get(id: string): Promise<AxiosResponse<CartResponseI>> {
		return this.api.get(`cart/carts/${id}/`);
	}

	public add(cartId: string, id: number, cnt: number): Promise<AxiosResponse<CartAddResponseI>> {
		return this.api.post(`cart/carts/${cartId}/items/`, { product_id: id, quantity: cnt });
	}

	public remove(cartId: string, id: number): Promise<AxiosResponse> {
		return this.api.delete(`cart/carts/${cartId}/items/${id}/`);
	}

	public edit(cartId: string, id: number, cnt: number): Promise<AxiosResponse> {
		return this.api.patch(`cart/carts/${cartId}/items/${id}/`, { quantity: cnt });
	}
}

export default Cart;
