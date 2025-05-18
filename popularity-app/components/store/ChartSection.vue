<template>
    <div class="section-container">
        <div class="section-lable" style="margin-bottom: 0;">Chart</div>
        <div class="section-chart-container">
            <div class="lw-chart" ref="chartContainer"></div>
        </div>
        <div class="section-chart-buttons-container">
            <button style="background-color: #3fbe7d;" class="section-chart-button">
            Buy
            </button>
            <button style="background-color: #ef454a;" class="section-chart-button">
            Sell
            </button>
        </div>
    </div>
</template>

<script setup>
import { createChart } from 'lightweight-charts'

const chartContainer = ref(null)
const themeStore = useThemeStore()

onMounted(() => {
    console.log(themeStore.themeParams)
    const chart = createChart(chartContainer.value, {
      layout: {
        background: { color: themeStore.themeParams.section_bg_color },
        textColor: themeStore.themeParams.text_color,
      },
      grid: {
        vertLines: { color: '#1E2F4100' },
        horzLines: { color: '#1E2F4100' },
      },
      leftPriceScale: {
        visible: true,
        borderVisible: false,
      },
      rightPriceScale: {
        visible: false,
      },
    })

    const areaSeries = chart.addAreaSeries({
      priceScaleId: 'left',
    })

    areaSeries.setData([
      { time: '2018-12-22', value: 32.51 },
      { time: '2018-12-23', value: 31.11 },
      { time: '2018-12-24', value: 27.02 },
      { time: '2018-12-25', value: 27.32 },
      { time: '2018-12-26', value: 25.17 },
      { time: '2018-12-27', value: 28.89 },
      { time: '2018-12-28', value: 25.46 },
      { time: '2018-12-29', value: 23.92 },
      { time: '2018-12-30', value: 22.68 },
      { time: '2018-12-31', value: 22.67 },
    ])

    
    chart.timeScale().fitContent()

    setInterval(() => {
        const now = Math.floor(Date.now() / 1000) // Unix timestamp в секундах
        const newPrice = 22 + Math.random() * 3 // Примерное случайное значение

        areaSeries.update({ time: now, value: newPrice })
    }, 300000)
})

</script>

<style>

.lw-chart {
    width: 100%;
    height: 150px;
    background-color: #ffffff00;
    margin-bottom: 5px;
}
.section-chart-buttons-container {
    display: flex;
    justify-content: space-around;
} 
.section-chart-button {
    color: var(--tg-theme-text-color);
    width: 47%;
    border-radius: 5px;
    padding: 10px;
    font-weight: bold;
    font-size: 15px;
}
</style>
