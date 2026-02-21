const wppconnect = require('@wppconnect-team/wppconnect');
const axios = require('axios');

wppconnect.create().then((client) => start(client));

function start(client) {
  client.onMessage(async (message) => {

    if (message.body && !message.isGroupMsg) {

      try {
        const response = await axios.post('http://localhost:5000/chat', {
          mensagem: message.body
        });

        await client.sendText(message.from, response.data.resposta);

      } catch (error) {
        console.log(error);
        await client.sendText(message.from, "Erro ao falar com a IA 😢");
      }

    }

  });
}