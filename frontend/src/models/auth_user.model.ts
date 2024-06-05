import { Role } from "./role.model"

export type User = {
    id: string,
    name: string,
    last_name: string,
    username: string,
    role: Role,
}
export type AuthUser = {
    access_token: string,
    refresh_token: string,
    user: User
}