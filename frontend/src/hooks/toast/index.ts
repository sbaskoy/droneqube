
import { toast, ToastOptions } from 'vue3-toastify';

const toastSettings = <ToastOptions>{
    autoClose: 1000,
    position: "top-center",
    
}

export const useErrorToast = (message: string) => {
    return toast(message, { ...toastSettings, type: 'error', });
}
export const useInfoToast = (message: string) => {
    return toast(message, { ...toastSettings, type: "info" });
}
export const useSuccessToast = (message: string) => {
    return toast(message, { ...toastSettings, type: "success" });
}