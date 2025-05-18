import {
    useWebApp,
    useWebAppCloudStorage,
    useWebAppRequests
} from 'vue-tg'
import { defineStore } from 'pinia';
// сервис подсказок да дата
export const useUserStore = defineStore('useUserStore', {
    state: () => ({
        webAppData: null,   
        dataUnsafe: null,
        contactData: null,
        desktop: false
    }),

    actions: {
        init(){
            return new Promise(async (resolve, reject) => {
                this.webAppData = useWebApp()
                if (this.webAppData.version > '6.0'){
                    this.dataUnsafe = await this.initDataUnsafe()
                }
                if (this.webAppData.platform == 'tdesktop'){
                    this.desktop = true
                }
                resolve(true)
            })
        },
        initDataUnsafe(){
            return new Promise(async (resolve, reject) => {
                let dataUnsafe = useWebApp().initDataUnsafe
                useWebAppCloudStorage().getStorageItem('initDataUnsafe').then(async (data) => {
                    if (typeof data === 'string' && data === ''){
                        useWebAppCloudStorage().setStorageItem('initDataUnsafe', JSON.stringify(dataUnsafe))
                        resolve(dataUnsafe)
                    } else {
                        if (dataUnsafe.user !== null){
                            if (dataUnsafe.user.username !== JSON.parse(data).user.username || dataUnsafe.user.photo_url !== JSON.parse(data).user.photo_url){
                                useWebAppCloudStorage().setStorageItem('initDataUnsafe', JSON.stringify(dataUnsafe))
                            }
                        }
                        resolve(JSON.parse(data))
                    }
                }) 
            })
        },
    }
})