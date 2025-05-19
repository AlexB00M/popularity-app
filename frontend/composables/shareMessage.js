const token = '7975261246:AAGrpUP8U_pmw-TTv-mEDjZ5TB1pTdwSPFc';

const data = {
user_id: 780952786,
result: JSON.stringify({
    type: "article",
    id: userStore.dataUnsafe.user.id,
    title: "Заголовок статьи",
    input_message_content: {
    message_text: "Это сообщение будет отправлено."
    }
}),
allow_user_chats: true,
};

await fetch(`https://api.telegram.org/bot${token}/savePreparedInlineMessage`, {
method: 'POST',
headers: {
    'Content-Type': 'application/json'
},
body: JSON.stringify(data)
})
.then(response => response.json())
.then(async (preparedMessage) =>  {
    console.log(preparedMessage)
    miniApp.shareMessage(preparedMessage.result.id, (status) => {
    console.log('status -', status)
    })
})
.catch(error => {
    console.error('Error:', error);
});