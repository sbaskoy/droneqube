
export const findElementPositionByTarget = (target: HTMLElement, popup: HTMLElement, parent: HTMLElement, position: "top" | "bottom", margin: number = 0,setWFull:boolean=false) => {
    const targetRect = target.getBoundingClientRect();

    const parentRect = parent.getBoundingClientRect();

    const popupWidth = setWFull ? target.offsetWidth  : popup.offsetWidth

    let top = position === 'bottom'
        ? targetRect.bottom + window.scrollY + margin
        : targetRect.top - popup.offsetHeight + window.scrollY - margin;

    let left = targetRect.left + window.scrollX;

    const parentBottom = parentRect.bottom + window.scrollY;
    const parentTop = parentRect.top + window.scrollY;
    const parentRight = parentRect.right + window.scrollX;

    if (position === 'bottom' && top + popup.offsetHeight > parentBottom) {
        top = targetRect.top - popup.offsetHeight + window.scrollY - margin;
    }
    if (position === 'top' && top < parentTop) {
        top = targetRect.bottom + window.scrollY + margin;
    }
    if (left + popupWidth > parentRight) {
        left = targetRect.right - popupWidth;
    }

    return { top, left, popup, width: popupWidth }

}