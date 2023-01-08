function priceFormat(price: number, fractionDigits = 2): string {
	return new Intl.NumberFormat('ru', { style: 'currency', currency: 'RUB', maximumFractionDigits: fractionDigits }).format(price);
}

export { priceFormat };
