


import { Image } from "@/models/image.model";
import { defineStore } from "pinia";

type ImageDialogStore = {
    images: Image[],
    selectedIndex: number,
    show: boolean,
    title: string

}

export const useShowImageDialog = defineStore("show_images_dialog", {
    state: (): ImageDialogStore => {
        return {
            images: [],
            selectedIndex: 0,
            show: false,
            title: "",
        }
    },
    actions: {
        showImagesDialog(_images: Image[], _title: string = "", startIndex: number = 0,) {
            this.images = _images;
            this.selectedIndex = startIndex;
            this.title = _title;
            this.show = true;
        },
        hideDialog() {
            this.show = false;
        },
        next() {
            if (this.selectedIndex + 1 < this.images.length) {
                this.selectedIndex++;
            }
        },
        previous() {
            if (this.selectedIndex - 1 >= 0) {
                this.selectedIndex--;
            }
        },
        setIndex(index: number) {
            this.selectedIndex = index;
        }
    }
})