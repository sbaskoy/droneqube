import { App } from "vue"
import { plugin as VueTippy } from 'vue-tippy'
import 'tippy.js/dist/tippy.css'


const tippyOptions = {
    directive: 'tippy', // => v-tippy
    component: 'tippy', // => <tippy/>
    componentSingleton: 'tippy-singleton', // => <tippy-singleton/>,
    defaultProps: {
        placement: 'top',
        allowHTML: true,
    }, 
};

export const tippyBuilder = (app: App<Element>) => {
    app.use(VueTippy, tippyOptions)
}