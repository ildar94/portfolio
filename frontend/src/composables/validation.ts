import { ComputedRef, Ref, watchEffect } from 'vue';

interface schemeItemI {
	fn: (...args: any[]) => boolean;
	errorMessage: string;
	params?: any[];
}

type schemeI<T> = {
	[K in keyof T]: schemeItemI[];
}

interface validResultI {
	isValid: boolean;
	error: string;
}

function useValidation<T>(
	data: { [key: string]: any },
	scheme: ComputedRef<schemeI<T>>,
): { [K in keyof T]: validResultI } {
	const result: { [K in keyof T]: validResultI } = {} as { [K in keyof T]: validResultI };

	watchEffect(() => {
		const fields = { ...data };

		for (const key in scheme.value) {
			if (key in fields) {
				const valid: validResultI = {
					isValid: true,
					error: '',
				};

				for (let i = 0; i < scheme.value[key].length; i++) {
					const rules = scheme.value[key][i];
					let isValid;

					if (rules?.params) {
						isValid = rules.fn.apply(null, rules.params);
					} else {
						isValid = rules.fn(fields[key]);
					}

					if (!isValid) {
						valid.isValid = false;
						valid.error = rules.errorMessage;

						break;
					}
				}

				result[key] = valid;
			} else {
				result[key] = { isValid: true, error: '' };
			}
		}
	});

	return result;
}

export { useValidation, schemeI, schemeItemI };
