import { api, apiWithToken } from '@/api';
import { AxiosResponse, AxiosInstance } from 'axios';
import { UserAuthI } from '@/api/user/types';

class Auth {
	private api: AxiosInstance;
	private authApi: AxiosInstance;

	constructor() {
		this.api = api;
		this.authApi = apiWithToken;
	}
}
