import { MaybeRef, computed, ref, unref } from "vue"

type FilterOptions<T> = {
    arr: MaybeRef<T[] | undefined | null>,
    fn: (item: T, searchTerm: string) => boolean
}

export const useFilter = <T>(options: FilterOptions<T>) => {
    const filterText = ref("")
    const filteredItems = computed(() => {
        const { arr, fn } = options;
        const searchTerm = filterText.value.toLowerCase();
        const data = unref(arr);
        if (searchTerm) {
            return data?.filter((item) => fn(item, searchTerm))
        }
        return data;
    });
    return { filterText, filteredItems }
}