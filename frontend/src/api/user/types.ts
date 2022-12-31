interface UserI {
	name: string;
	surname: string;
	email: string;
	phone: string;
	city: string;
	street: string;
	house: string;
	apartment: string;
}

interface UserAuthI extends UserI {
	password: string;
	passwordRetry: string;
}

export { UserI, UserAuthI };
