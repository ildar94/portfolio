interface attrI {
	['key']: string
}

interface ProductI {
	id: number,
	category_id: string,
	name: string,
	slug: string
	article: number,
	price: number,
	product_image: string[] | null,
	description: string;
	sales_price: number | null,
	sold_time: number | null,
	attr: attrI,
}

interface ProductsResponseHeadI {
	count: number;
	next: string | null;
	previous: string | null;
	results: ProductI[];
}

export { attrI, ProductI, ProductsResponseHeadI };
