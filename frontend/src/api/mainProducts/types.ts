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
	images: string[] | null,
	features?: featureI[] | null;
	description: string;
	sales_price: number | null,
	sold_time: number | null,
	is_in_cart?: boolean;
	is_in_favorites?: boolean;
	is_in_compare?: boolean;
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
