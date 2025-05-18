export default defineNuxtPlugin(() => {
    const tg =  window.Telegram?.WebApp;
  
    const getTelegram = () => tg;
    const getUser = () => tg?.initDataUnsafe?.user;
  
    return {
      provide: {
        telegram: {
          getTelegram,
          getUser,
        },
      },
    };
  });
  