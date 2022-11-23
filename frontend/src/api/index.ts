import axios, { AxiosInstance } from 'axios';

const api: AxiosInstance = axios.create({
	baseURL: 'http://localhost:3000/',
	timeout: 2000,
});

export { api };
