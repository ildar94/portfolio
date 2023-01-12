import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import index from '@/pages/index/index.vue';
import service from '@/pages/service.vue';
import catalog from '@/pages/catalog/index.vue';
import subCatalog from '@/pages/catalog/catalog.vue';
import about from '@/pages/about.vue';
import news from '@/pages/news.vue';
import specials from '@/pages/specials.vue';
import contacts from '@/pages/contacts.vue';
import favorites from '@/pages/favorites.vue';
import compare from '@/pages/compare.vue';
import cart from '@/pages/cart.vue';

const routes: Array<RouteRecordRaw> = [
	{
		path: '/',
		name: 'index',
		component: index,
		meta: {
			name: 'Главная',
		},
	},
	{
		path: '/',
		name: 'service',
		component: service,
		meta: {
			name: 'Сервис',
		},
	},
	{
		path: '/catalog/',
		name: 'catalog',
		component: catalog,
		meta: {
			name: 'Каталог',
		},
	},
	{
		path: '/catalog/:slug',
		name: 'subCatalog',
		component: subCatalog,
	},
	{
		path: '/about',
		name: 'about',
		component: about,
		meta: {
			name: 'О нас',
		},
	},
	{
		path: '/news',
		name: 'news',
		component: news,
		meta: {
			name: 'Новости',
		},
	},
	{
		path: '/contacts',
		name: 'contacts',
		component: contacts,
		meta: {
			name: 'Контакты',
		},
	},
	{
		path: '/specials',
		name: 'specials',
		component: specials,
		meta: {
			name: 'Акции',
		},
	},
	{
		path: '/favorites',
		name: 'favorites',
		component: favorites,
		meta: {
			name: 'Избранное',
		},
	},
	{
		path: '/compare',
		name: 'compare',
		component: compare,
		meta: {
			name: 'Сравнения',
		},
	},
	{
		path: '/cart',
		name: 'cart',
		component: cart,
		meta: {
			name: 'Корзина',
		},
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
