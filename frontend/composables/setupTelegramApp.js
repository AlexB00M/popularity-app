import { useViewport } from 'vue-tg'
import { useTheme } from 'vue-tg'

export function setupTelegramApp(webAppData){
    const { $telegram } = useNuxtApp()
    const tg = $telegram.getTelegram()
    const theme = useTheme()
    const themeParams = theme.themeParams
    console.log(themeParams)
    // const colorScheme = theme.colorScheme.value

    if (webAppData.platform !== "tdesktop"){
        tg.requestFullscreen()
    } 

    const viewport = useViewport()
    viewport.isVerticalSwipesEnabled.value = false
    
}