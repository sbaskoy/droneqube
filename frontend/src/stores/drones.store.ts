import { useFilter } from "@/hooks/utils/useFilter";
import { Drone } from "@/models/drone.model";
import DroneService from "@/services/drone_service";
import { defineStore } from "pinia";
import { ref } from 'vue';


export const useDronesStore = defineStore("drones_store", () => {
    const drones = ref<Drone[]>();
    const loading = ref(false)
    const pageIndex = ref(1);
    const { filterText, filteredItems: filteredDrones } = useFilter({
        arr: drones,
        fn: (drone, searchTerm) => drone.name.toLowerCase().includes(searchTerm) || drone.serial_number.toLowerCase().includes(searchTerm)
    })
    const loadDrones = async () => {
        loading.value = true;
        const response = await DroneService.getDrones(pageIndex.value);
        loading.value = false;
        return response;

    }
    const addDrone = (drone: Drone) => {
        if (!drones.value?.some(i => i.id == drone.id)) {
            drones.value?.push(drone);
        }
    }
    const loadMore = async () => {
        if (loading.value) return;
        pageIndex.value = pageIndex.value + 1;
        const res = await loadDrones();
        if (res) {
            drones.value?.push(...res);
        }
    }
    (async () => {
        const res = await loadDrones();
        if (res) {
            drones.value = res;
        }
    })();
    return { loading, filterText, filteredDrones, loadMore, addDrone }
})