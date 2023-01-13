import { defineStore } from 'pinia';

export const useCartStore = defineStore('userStore', {
	state: () => ({
		id: null,
	}),
});
