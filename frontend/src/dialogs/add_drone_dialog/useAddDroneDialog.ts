import { useInfoToast } from "@/hooks/toast";
import DroneService from "@/services/drone_service";

import { useDronesStore } from "@/stores/drones.store";
import { useLoadingStore } from "@/stores/loading.store";

import { defineStore } from "pinia";
import { ref } from "vue";

export const useAddDroneDialog = defineStore("add_drone_dialog", () => {
    const show = ref(false);
    const droneName = ref("");
    const droneSerialNumber = ref("");
    const loadingStore = useLoadingStore();
    const dronesStore = useDronesStore();
    const showAddDroneDialog = () => {
        show.value = true;
    }
    const hideAddDroneDialog = () => {
        show.value = false;
    }
    const addNewDrone = async () => {
        loadingStore.show();
        var res = await DroneService.createDrone({
            name: droneName.value,
            serial_number: droneSerialNumber.value ? droneSerialNumber.value : undefined
        });

        if (res) {
            dronesStore.addDrone(res);
            droneName.value = "";
            droneSerialNumber.value = "";
            useInfoToast("Drone başarıyla eklendi.")
        }
        loadingStore.hide();
    }
    return { show, droneName, droneSerialNumber, showAddDroneDialog, hideAddDroneDialog, addNewDrone }
})