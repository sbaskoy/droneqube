import { Assignment } from "./assignment.model"

export enum DroneStatus {
    Available = "Available",
    InActive = "InActive",
}

export type Drone = {
    id: string,
    name: string,
    serial_number: string,
    status: DroneStatus,
    task_assignments?: Assignment[]

}