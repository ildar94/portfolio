type statusBadge = 'hit' | 'latest';

interface ProductCardFeatureProp {
	icon?: string;
	text: string;
}

interface ProductCardProps {
	name: string;
	images: string[];
	status?: { text: string; badge: statusBadge };
	isInCompare?: boolean;
	isInCart?: boolean;
	isInFavorites?: boolean;
	features: ProductCardFeatureProp[];
	price: string;
	sales_price?: string;
}

export { ProductCardFeatureProp, ProductCardProps };
