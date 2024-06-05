



import { Assignment } from "@/models/assignment.model";
import { Image } from "@/models/image.model";
import { Task } from "@/models/task.model";
import service from "@/services/droneqube_service";

type TaskCreateData = {
    name: string,
    description: string,
}

type AssignDroneData = {
    drone_id: number
}
class TaskService {
    static async getTasks(pageIndex:number=1) {
        const response = await service.get("/tasks", { params: { page: pageIndex } });
        if (response.data) {
            return response.data as Task[];
        }
    }
    static async createTask(_data: TaskCreateData) {
        const response = await service.post("/tasks", { ..._data });
        if (response.data) {
            return response.data as Task;
        }
    }
    static async assignDrone(taskId: number, _data: AssignDroneData) {
        const response = await service.post(`/tasks/${taskId}/assign-drone`, { ..._data });
        if (response.data) {
            return response.data as Assignment
        }
    }
    static async listImages(taskId: number) {
        const response = await service.get(`/tasks/${taskId}/images`);
        if (response.data) {
            return response.data as Image[]
        }
    }

}
export default TaskService;