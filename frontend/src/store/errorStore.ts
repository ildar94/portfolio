import { defineStore } from 'pinia';

interface errorI {
	id: number;
	title: string;
	text: string;
	critical: boolean;
}

export const useErrorStore = defineStore('errorStore', {
	state: () => ({
		errors: [] as errorI[],
		lastErrorId: 0,
	}),
	getters: {
		errorsCnt: (state) => state.errors.length,
	},
	actions: {
		appendError(title: string, text: string, critical = false) {
			this.errors.push({ id: this.lastErrorId += 1, title, text, critical });

			const lastErrorId = this.lastErrorId;

			if (!critical) {
				setTimeout(this.removeError.bind(this, lastErrorId), 2000);
			}
		},
		removeError(id: number) {
			this.errors = this.errors.filter(item => item.id !== id);
		},
	},
});
