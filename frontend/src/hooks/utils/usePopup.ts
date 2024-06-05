import { findElementPositionByTarget } from '@/helpers/html_helpers';
import { ref, onMounted, onUnmounted } from 'vue';

interface UsePopupOptions {
    position?: 'top' | 'bottom';
    margin?: number,
    isWidthFull?:boolean,
    containerElementSelector?: () => HTMLElement | null
}

export function usePopup(options: UsePopupOptions = { position: 'bottom', margin: 0 }) {
    const { position = 'bottom', margin = 0,isWidthFull } = options;
    const isVisible = ref(false);
    const popupElement = ref<HTMLElement>();
    const targetElement = ref<HTMLElement>();
    const containerElement = ref<HTMLElement>();

    const show = () => {
        if (popupElement.value && targetElement.value) {
            const parent = (containerElement.value ?? options.containerElementSelector?.() ?? document.body);
            const { left, top, popup,width } = findElementPositionByTarget(targetElement.value, popupElement.value, parent, position, margin, isWidthFull);

            popup.style.top = `${top}px`;
            popup.style.left = `${left}px`;
            popup.style.width = `${width}px`;
            
            // popup.style.left = `${targetRect.left + window.scrollX}px`;
            popup.style.position = 'absolute';
            popup.style.visibility = 'visible';
            popup.classList.remove('animate-fadeOut');
            popup.classList.add('animate-fadeIn');
            isVisible.value = true;
        }
    };

    const hide = () => {
        if (popupElement.value) {
            const popup = popupElement.value;
            isVisible.value = false;
            popup.classList.remove('animate-fadeIn');
            popup.classList.add('animate-fadeOut');
            setTimeout(() => {
                popupElement.value!.style.visibility = 'hidden';
                popupElement.value!.style.top = '0px';
                popupElement.value!.style.left = '0px';
            }, 300);
        }
    };

    const toggle = () => {
        if (isVisible.value) {
            hide();
        } else {
            show();
        }
    };

    const handleClickOutside = (event: MouseEvent) => {
        if (popupElement.value && !popupElement.value.contains(event.target as Node) && targetElement.value && !targetElement.value.contains(event.target as Node)) {
            hide();
        }
    };

    onMounted(() => {
        if (popupElement.value) {
            isVisible.value = false;
            popupElement.value.style.visibility = 'hidden';
            popupElement.value.style.top = "0px";
            document.addEventListener('click', handleClickOutside);
        }
    });
    onUnmounted(() => {
        document.removeEventListener('click', handleClickOutside);
    });

    return { isVisible, targetElement, popupElement, containerElement, show, hide, toggle };
}
