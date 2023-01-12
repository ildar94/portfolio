interface attrI {
	['key']: string
}

interface featureI {
	text: string;
	icon: string;
}

interface ProductI {
	id: number,
	category_id: string,
	name: string,
	slug: string
	article: number,
	price: number,
	priceFormat: string;
	sales_price: number | null,
	salesPriceFormat: string | null;
	images: string[] | null,
	features?: featureI[] | null;
	description: string;
	sold_time: number | null,
	attr: attrI,
}

interface ProductsResponseHeadI {
	links: {
		next: string;
		previous: string;
	};
	total_count: number;
	page_size: number;
	total_pages: number;
	current_page_number: number;
	next: string | null;
	previous: string | null;
	results: ProductI[];
}

export { attrI, ProductI, ProductsResponseHeadI };
