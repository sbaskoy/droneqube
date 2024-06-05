import { useAuthStore } from "@/stores/auth.store";
import axios, { AxiosError, AxiosRequestConfig } from "axios";

import { useErrorToast } from "@/hooks/toast";
import { ApiErrorModel } from "@/models/api_info.model";

const SERVICE_URL = import.meta.env.VITE_API_URL;


const axiosInstance = axios.create({
    baseURL: SERVICE_URL,
})

const errorHandler = async (error: AxiosError) => {

    const originalRequest = error.config as AxiosRequestConfig & { _retry?: boolean };

    if (error.response?.status === 401 && !originalRequest?._retry) {
        originalRequest._retry = true;
        const authStore = useAuthStore();
        const refreshToken = authStore.user?.refresh_token;
        const response = await axios.post(`${SERVICE_URL}/auth/refresh`, {}, {
            headers: { 'Authorization': `Bearer ${refreshToken}` }
        });
        if (response.status === 200) {
            const { access_token, refresh_token } = response.data ?? {};
            if (access_token && refresh_token) {
                authStore.setTokens(access_token, refresh_token);
            }
            axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
            originalRequest!.headers!['Authorization'] = `Bearer ${access_token}`;
            return axiosInstance(originalRequest);
        }
    }


    let errorMessage = "DroneQube service bağlanılamadı.";
    const errorData = error.response?.data as ApiErrorModel | undefined;;
    const message = errorData?.error.message;
    if (typeof message == "string") {
        errorMessage = message;
    } else if (typeof message == "object") {
        errorMessage = Object.entries(message).map(([key, values]) => {
            return `${key}: ${values.map(i => i).join(",")}`
        }).join("\n");
    }
    useErrorToast(errorMessage);
    return { data: null }
}



axiosInstance.interceptors.request.use(
    config => {
        const { user } = useAuthStore();
        if (user?.access_token) {
            config.headers['Authorization'] = `Bearer ${user?.access_token}`;
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

axiosInstance.interceptors.response.use(response => response, errorHandler);
export default axiosInstance;
