interface parseJWTI {
	header: object | string;
	payload: object | string;
	sign: string;
}

function getJWTPayload(token: string): object | string {
	return parseJWT(token).payload;
}

function parseJWT(token: string): parseJWTI {
	const parts = token.split('.');

	return {
		header: parsePart(parts[0]),
		payload: parsePart(parts[1]),
		sign: parts[2],
	};
}

function parsePart(str: string): object | string {
	return JSON.parse(atob(str));
}

type TTokenType = 'at' | 'rt';

function setToken(tokenType: TTokenType = 'at', token: string) {
	localStorage.setItem(tokenType, token);
}

function getToken(tokenType: TTokenType) {
	return localStorage.getItem(tokenType);
}

function removeToken(tokenType: TTokenType) {
	localStorage.removeItem(tokenType);
}

export { getJWTPayload, setToken, getToken, removeToken };
