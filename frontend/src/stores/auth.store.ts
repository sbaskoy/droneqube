import { AuthUser } from "@/models/auth_user.model";
import { defineStore } from "pinia";

type AuthStore = {
    user: AuthUser | null,
    password: string,
    username: string,
}

export const useAuthStore = defineStore("auth", {
    state: (): AuthStore => {
        return {
            user: null,
            password: "",
            username: "",
        }
    },
    getters: {
        userId(state) {
            return state.user?.user.id;
        }
    },
    actions: {
        setUser(user: AuthUser) {
            this.user = user;
        },
        setTokens(access_token: string, refresh_token: string) {
            if (this.user) {
                this.user.access_token = access_token;
                this.user.refresh_token = refresh_token;
            }
        }
    },
    persist: true,
})