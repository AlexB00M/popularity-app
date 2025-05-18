export default defineNuxtPlugin(async (nuxtApp) => {
    const userStroe = useUserStore()
    if (userStroe.webAppData.initData !== 'user') {
        console.log(userStroe.webAppData.initData)
        fetch('http://127.0.0.1:8000/api/auth/telegram/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ initData: userStroe.webAppData.initData }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Токены:', data);
            localStorage.setItem('accessToken', data.tokens.access)
            localStorage.setItem('refreshToken', data.tokens.refresh)
        })
        .catch(error => {
            console.error('Ошибка при получении токенов:', error)
        });
    }
})