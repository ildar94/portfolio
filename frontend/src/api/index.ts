import axios, { AxiosInstance, AxiosResponse, AxiosError } from 'axios';
import { getToken, setToken } from '@/utils/token';

const api: AxiosInstance = axios.create({
	baseURL: '/api/v1/',
	timeout: 2000,
});

const apiWithToken: AxiosInstance = axios.create({
	baseURL: '/api/v1/',
	timeout: 2000,
});

function addResponseHandler(onSuccess: (response: AxiosResponse) => any, onError: (error: AxiosError) => any) {
	api.interceptors.response.use(onSuccess, onError);
}

interface errorConfigI {
	title: string;
	text: string;
	critical?: boolean;
}

apiWithToken.interceptors.request.use((config) => {
	const at = getToken('at');

	if (!at) {
		throw Object.assign('at is not defined', { code: 403 });
	}

	if (!config.headers) {
		config.headers = {};
	}

	config.headers.Authorization = at;

	return config;
});

apiWithToken.interceptors.response.use(async(config) => {
	return config;
}, async error => {
	if (error.request.status >= 401 && error.request.status <= 403 && !error.config._retry) {
		const rt = getToken('rt');

		try {
			const response = await api.post('token/refresh/', { rt });

			setToken('rt', response.data);

			error.config._retry = true;

			apiWithToken(error.config);
		} catch (error) {
			throw new Error('can`t refresh');
		}
	}

	return error;
});

export { api, apiWithToken, addResponseHandler, errorConfigI };
