import { Assignment } from "./assignment.model"


export type Task = {
    id: number,
    name: string,
    description: string,
    drone_assignments?: Assignment[]
}