import { onUnmounted } from 'vue';

type elementType = HTMLElement | null;

export function useClickOutside(element: elementType | elementType[], callback: () => any): void | null {
	if (!element) return null;

	function handler(e: MouseEvent) {
		const target = e.target;

		if (Array.isArray(element) && element.some(isInside)) {
			return;
		}

		if (!Array.isArray(element) && isInside(element as elementType)) {
			return;
		}

		function isInside(elementItem: elementType) {
			return target === elementItem || e.composedPath().includes(elementItem as HTMLElement);
		}

		if (typeof callback === 'function') {
			callback();
		}
	}

	window.addEventListener('click', handler);
	onUnmounted(() => window.removeEventListener('click', handler));
}
