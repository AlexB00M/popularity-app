
// сервис подсказок да дата
export const useStoreStore = defineStore('useStoreStore', {
    state: () => ({
        userStarsBalance: null,
        storeBuyCards: {},
        storeBuyTotalCost: 0,
    }),

    actions: {
        init() {
            const appStore = useAppStore()
            const cardsConfig = appStore.cardsConfig
            for (const card in cardsConfig){
                this.storeBuyCards[card] = {
                    'cost': cardsConfig[card].cost,
                    'count': 0
                }
            }
            this.userStarsBalance = 100
        },
        reserAll() {
            for (const card in this.storeBuyCards){
                this.storeBuyCards[card]['count'] = 0
            }
        }
    }
})