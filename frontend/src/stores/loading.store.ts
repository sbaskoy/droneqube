import { defineStore } from "pinia";

type LoadingStore = {
    loading: boolean
}

export const useLoadingStore = defineStore("loading_store", {
    state: () => (<LoadingStore>{ loading: false }),
    actions: {
        setLoading(val: boolean) {
            this.loading = val;
        },
        show() {
            this.loading = true;
        },
        hide() {
            this.loading = false;
        },
    },
})