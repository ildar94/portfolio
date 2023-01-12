import { ComputedRef, Ref, watchEffect } from 'vue';

interface schemeItemI {
	fn: (...args: any[]) => boolean;
	errorMessage: string;
	params?: any[];
}

interface schemeI {
	[key: string]: schemeItemI[];
}

interface validResultI {
	isValid: boolean;
	error: string;
}

function useValidation(
	data: { [key: string]: any },
	scheme: ComputedRef<schemeI>,
): { [key: string]: validResultI } {
	const result: { [key: string]: validResultI } = {};

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
			}
		}
	});

	return result;
}

export { useValidation, schemeI, schemeItemI };
