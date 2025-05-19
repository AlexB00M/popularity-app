import { useTheme } from 'vue-tg'

// сервис подсказок да дата
export const useThemeStore = defineStore('useThemeStore', {
    state: () => ({
        themeParams: null,
        colorTheme: null
    }),

    actions: {
        init(){
            const theme = useTheme()
            this.themeParams = theme.themeParams
            this.colorTheme = theme.colorScheme
        },
    }
})