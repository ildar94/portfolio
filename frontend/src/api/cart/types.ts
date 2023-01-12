interface CartItemProductI {
	name: string;
	description: string;
	price: number;
	formatPrice: string;
}

interface CartItemI {
	id: number;
	product_id: number;
	product: CartItemProductI;
	quantity: number;
	total_price: number;
	totalPriceFormat: string;
}

interface CartResponseI {
	id: string;
	session: string;
	items: CartItemI[],
	total_price: number;
	totalPriceFormat: string;
}

interface CartAddResponseI {
	id: number;
	product_id: number;
	quantity: number;
}

export { CartResponseI, CartItemI, CartAddResponseI };
