import { Drone } from "./drone.model"
import { Task } from "./task.model"

export type Assignment = {
    id: string,
    completed: boolean,
    drone?: Drone,
    task?: Task
}