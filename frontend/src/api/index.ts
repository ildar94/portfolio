import axios, { AxiosInstance } from 'axios';

const api: AxiosInstance = axios.create({
	baseURL: 'http://localhost:8000/api/v1/',
	timeout: 2000,
});

export { api };
