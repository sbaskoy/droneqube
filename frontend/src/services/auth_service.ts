

import { AuthUser } from "@/models/auth_user.model";
import service from "@/services/droneqube_service";

class AuthService {
    static async login(username: string, password: string) {
        const response = await service.post("/auth/login", { username, password })
        if (response.data) {
            return response.data as AuthUser;
        }
    }
    static async refresh() {
        const response = await service.post("/auth/refresh", {})
        if (response.data) {
            return response.data as AuthUser;
        }
    }

}
export default AuthService;