export type ApiErrorModel = {
    error: {
        message: string | { [key: string]: string[] },
        type: string,
        status_code: number,
    }
}