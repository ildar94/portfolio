function isValidEmail(email: string): boolean {
	const regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

	return regex.test(email);
}
function required(text: string): boolean {
	return !!text && !!text.length;
}

function minLength(minLength: number, text: string): boolean {
	return text.length >= minLength;
}

function maxLength(maxLength: number, text: string): boolean {
	return text.length <= maxLength;
}

function isEqual(text: string, equalText: string): boolean {
	return text === equalText;
}

export { isValidEmail, required, minLength, maxLength, isEqual };
