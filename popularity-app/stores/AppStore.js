import { defineStore } from 'pinia';
import cardsConfiguration from '~/assets/dataTest/cardsConfiguration.json'
import userCards from '~/assets/dataTest/userCards.json'
import totalPointsConfig from '~/assets/dataTest/totalPointsConfiguration.json'

// сервис подсказок да дата
export const useAppStore = defineStore('useAppStore', {
    state: () => ({
        cardsConfig: null,
        totalPointsConfig: null,
        totalPoints: null,
        colorTotal: null, 
        userPossition: null,
        userCards: null,
        userRaiting: null,
        userHistory: null,
        userMessages: null,
        
    }),

    actions: {
        init(){
            this.cardsConfig = this.sortConfigDesc(cardsConfiguration)
            this.totalPointsConfig = totalPointsConfig
            this.userCards = userCards
            this.totalPoints = this.calcTotalPoints(this.cardsConfig, this.userCards)
            this.colorTotal = totalPointsConfig[getLevelByTotalPoints(this.totalPoints, this.totalPointsConfig)].color
            this.userPossition = 230
        },
        calcTotalPoints(cardsConfig, userCards){
            let total = 0

            userCards.forEach(card => {
              const name = card.name
              const count = card.count
          
              if (cardsConfig[name] && cardsConfig[name].pointsPerOne) {
                const pointsPerOne = parseInt(cardsConfig[name].pointsPerOne, 10)
                total += count * pointsPerOne
              }
            })
            return total
        }, 
        sortConfigAsc(cardsConfig) {
            const sortedEntries = Object.entries(cardsConfig).sort((a, b) => {
                return Number(a[1].chance) - Number(b[1].chance); 
              });
            
            return Object.fromEntries(sortedEntries);
        },
        sortConfigDesc(cardsConfig) {
            const sortedEntries = Object.entries(cardsConfig).sort((a, b) => {
                return Number(b[1].chance) - Number(a[1].chance); // по убыванию
            });
            
            return Object.fromEntries(sortedEntries);
        }
        
        // getCardsConfig()
        // getUserCards()
        // getUserData() ранг друзья и тд
        // Потом мб еще что-то...
    }
})