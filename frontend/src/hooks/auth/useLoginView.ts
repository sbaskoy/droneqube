

import AuthService from "@/services/auth_service";
import { useAuthStore } from "@/stores/auth.store";
import { useLoadingStore } from "@/stores/loading.store";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

export const useLoginView = () => {
    const authStore = useAuthStore();
    const loadingStore = useLoadingStore();
    const { username, password } = storeToRefs(authStore);
    const router = useRouter();

    const handleLoginButton = async () => {
        loadingStore.show();
        var res = await AuthService.login(username.value, password.value);
        if (res) {
            authStore.setUser(res);
            router.push({ name: "Home" })
        }
        loadingStore.hide();
    }
    return { username, password, handleLoginButton }
}