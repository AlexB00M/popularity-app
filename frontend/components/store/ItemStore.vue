<template>
    <div class="store-card-container" style="width: 100px; flex-shrink: 0;" :style="themeStore.colorTheme === 'dark' ? { backgroundColor: 'var(--tg-theme-secondary-bg-color)' } : {}"> 
        <button class="store-card-data" @click="modalItemCardOpen">
            <div class="store-card-data-params" :style="{ color: appStore.colorTotal }">
                +{{ appStore.cardsConfig[Name].pointsPerOne }}<nuxt-icon name="fire"/>
            </div>
            <DotLottieVue class="store-card-image" autoplay loop :src="appStore.cardsConfig[Name].url"/>
        </button>
        <div class="store-card-buy-button-container">
            <!-- @click="modalBuyCardOpen" -->
            <button v-if="storeStore.storeBuyCards[Name].count == 0 || isSpining" class="store-item-card-buy-button" @click="incriment"> 
                <nuxt-icon class="store-item-card-star-icon" name="telegramStar"/>
                <div class="store-item-card-buy-button-text">
                    {{ appStore.cardsConfig[Name].cost }}
                </div>
            </button>
            <div v-else class="store-card-count-params">
                <div class="store-card-count-params-container">
                    <button class="store-cards-count-params min" @click="storeStore.storeBuyCards[Name].count--">
                        -
                    </button>
                    <div class="store-cards-count-params-count">
                        {{ storeStore.storeBuyCards[Name].count }}
                    </div>
                    <button class="store-cards-count-params plus" @click="storeStore.storeBuyCards[Name].count++">
                        + 
                    </button>
                </div>
            </div>
        </div>
    </div>
    <ModalItemStoreCard :Visible="modalItemCardVisible" :CardName="Name" :CardImageUrl="appStore.cardsConfig[Name].url" @close="modalItemCardClose"/>
    <MainButton v-if="isAnyCard"  :text="`Buy ${totalCost} Stars`" :hasShineEffect="true"/>
    <!-- <ModalBuyCard :Visible="modalBuyCardVisible" :CardName="Name" :CardImageUrl="appStore.cardsConfig[Name].url" @close="modalBuyCardClose"/> -->
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue' 
import { useSecondaryButton, MainButton } from 'vue-tg'

const props = defineProps({
    Name: String,
})
const test = ref('')
const secondaryButton = useSecondaryButton()
secondaryButton.hasShineEffect.value = true

secondaryButton.onClick(() => {
    Object.keys(storeStore.storeBuyCards).forEach((key) => {
        if (storeStore.storeBuyCards[key].hasOwnProperty('count')) {
            storeStore.storeBuyCards[key].count = 0;
        }
    });
})

const storeStore = useStoreStore()
const appStore = useAppStore()
const themeStore = useThemeStore()

const isAnyCard = useState('isAnyCard')
const oneOpened = useState('oneOpened')
const isSpining = useState('isSpining')
const isBuying = useState('isBuying', () => false)
const isBuyingStars = useState('isBuyingStars')

const modalItemCardVisible = ref(false)
const modalBuyCardVisible = ref(false)

oneOpened.value = false

watch(() => storeStore.storeBuyCards[props.Name].count, (newCount) => {
  isBuying.value = newCount !== 0
})

watchEffect(() => {
    if (isAnyCard.value) {
        secondaryButton.show();
    } else {
        secondaryButton.hide();
    }
});

const incriment = () => {
    console.log(localStorage.getItem('accessToken'))
    fetch('http://localhost:8000/api/user/user_rank/', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
            'Content-Type': 'application/json'
        }
        })
        .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
        })
        .then(data => {
        console.log('Профиль пользователя:', data);
        })
        .catch(error => {
        console.error('Ошибка при запросе профиля:', error);
    });
    // console.log(localStorage.getItem('refreshToken'))
    // fetch('http://localhost:8000/api/auth/token/refresh/', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({
    //         "refresh": localStorage.getItem('refreshToken')
    //     })
    //     })
    //     .then(response => {
    //     if (!response.ok) {
    //         throw new Error(`HTTP error! Status: ${response.status}`);
    //     }
    //     return response.json();
    //     })
    //     .then(data => {
    //         console.log('Профиль пользователя:', data);
    //         localStorage.setItem('accessToken', data.access)
    //     })
    //     .catch(error => {
    //         console.error('Ошибка при запросе профиля:', error);
    // });
    if (isBuyingStars.value) return
    if (!isSpining.value){
        storeStore.storeBuyCards[props.Name].count++
    }
}

const totalCost = computed(() => {
    return Object.values(storeStore.storeBuyCards).reduce((sum, card) => {
        return sum + card.count * card.cost
    }, 0)
})

const modalItemCardOpen = () => {
    if (isBuyingStars.value) return
    if (isSpining.value) return
    if (isAnyCard.value) return
    if (oneOpened.value) return

    modalItemCardVisible.value = true
    oneOpened.value = true
}
const modalItemCardClose = () => {
    modalItemCardVisible.value = false
    oneOpened.value = false
} 
const modalBuyCardClose = () => {
    // modalBuyCardVisible.value = false
    // oneOpened.value = false
} 
const modalBuyCardOpen = () => {
    // if (oneOpened.value) return

    // oneOpened.value = true
    // modalBuyCardVisible.value = true
}
</script>

<style>
.store-cards-count-params.min {
    position: absolute;
    top: 0;
    left: 0;
}
.store-cards-count-params.plus {
    position: absolute;
    top: 0;
    right: 0;
}
.store-cards-count-params-count {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 13px;
    font-weight: bold;
    color: #ffc400;
}
.store-cards-count-params {
    background-color: #ad85039f;
    cursor: pointer;
    width: 23px;
    height: 23px;
    border: 5px;
    color: var(--tg-theme-text-color);
    border-radius: 5px;
}
.store-card-count-params-container {
    position: relative;
    width: 90px; 
    height: 23px;
}
.store-card-buy-button-container {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    height: 25px;
}
.store-card-data {
  cursor: pointer;
  border-radius: 10px;
}
.store-card-data-params {
  padding-top: 5px;
  font-size: 13px;
  font-weight: bold;
  text-align: center;
}
.store-card-image {
  height: 100px;
  top: 0;
}
.store-card-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 5px; 
    border-radius: 10px;
    min-height: 153px;
    box-shadow: 0 0px 12px rgba(0, 0, 0, 0.1);
}
.store-item-card-star-icon {
    font-size: 16px;
    color: #ffc400;
}
.store-item-card-buy-button-text {
    font-size: 10px;
    font-weight: bold;
    color: #ad8603;
    display: inline;
}
.store-item-card-buy-button {
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 4px;
    background-color: #f0b40029;
    border-radius: 20px;
    padding: 2px 6px 2px 6px;
}
</style>