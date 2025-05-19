

export default defineNuxtPlugin(async (nuxtApp) => {
    const userStore = useUserStore()
    const appStore = useAppStore()
    const themeStore = useThemeStore()
    const storeStore = useStoreStore()

    themeStore.init()
    appStore.init()
    await userStore.init()
    storeStore.init()

    console.log("Хранилища загружены!", userStore, appStore)
    
})