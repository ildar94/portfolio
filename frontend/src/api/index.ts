import axios, { AxiosInstance } from 'axios';

const api: AxiosInstance = axios.create({
	baseURL: '/api/v1/',
	timeout: 2000,
});

export { api };
