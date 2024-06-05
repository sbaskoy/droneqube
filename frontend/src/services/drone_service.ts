

import { Drone } from "@/models/drone.model";
import { Image } from "@/models/image.model";

import service from "@/services/droneqube_service";

type DroneCreateData = {
    name: string,
    serial_number?: string,
}


class DroneService {
    static async getDrones(page: number = 1) {
        const response = await service.get("/drones", { params: { page } });
        if (response.data) {
            return response.data as Drone[];
        }
    }
    static async createDrone(_data: DroneCreateData) {
        const response = await service.post("/drones", { ..._data });
        if (response.data) {
            return response.data as Drone;
        }
    }

    static async listImages(droneId: number) {
        const response = await service.get(`/drones/${droneId}/images`);
        if (response.data) {
            return response.data as Image[]
        }
    }

}
export default DroneService;