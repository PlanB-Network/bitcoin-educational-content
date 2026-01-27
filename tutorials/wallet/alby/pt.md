---
name: Alby

description: Extensão do navegador para Bitcoin e Lightning Network
---

![cover](assets/cover.webp)




Facilitar cada vez mais os pagamentos com bitcoin é o desafio que enfrentam muitas empresas do sector. O Alby destaca-se da multidão com a sua extensão Alby wallet para os navegadores. Esta extensão tem por objetivo criar um quadro fluido que detecta automaticamente os endereços e permite efetuar pagamentos em bitcoin sem fricção. Neste tutorial, descobrimos a extensão Alby e testamos como facilita os pagamentos a partir do navegador.




![video](https://youtu.be/nd5fX2vHuDw)




## Extensão Alby



A extensão Alby é uma ferramenta que permite ao seu navegador Web interagir facilmente e de forma segura com a rede Bitcoin e a sua camada Lightning Network. Caracteriza-se por três aspectos:




- Lightning Network wallet: Ligue o seu nó ou conta Alby para enviar e receber bitcoin de forma rápida e barata através da camada Lightning Network.
- Pagamentos fluidos através da Web: Elimina a necessidade de digitalizar códigos QR ou de alternar entre aplicações para pagamentos em bitcoin em sítios Web que suportam Lightning. Permite transacções fluidas com um único clique, ou sem confirmação se tiver definido um orçamento.
- Um gestor Nostr: A extensão gere as suas chaves Nostr, facilitando a ligação e a interação com as aplicações Nostr, actuando como um signatário seguro sem expor a sua chave privada a todas as plataformas.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Ligar à extensão



Neste tutorial, usaremos a extensão Alby no navegador Firefox em um sistema operacional Ubuntu. No entanto, ela também está disponível no Windows e em navegadores como o Chrome.



Pode adicionar a extensão Alby ao seu browser visitando a loja de extensões [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) ou a loja de extensões [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ É importante verificar se o autor da extensão é de facto a conta oficial do Alby, para evitar qualquer forma de pirataria ou roubo dos seus bitcoins.



Adicione a extensão ao seu browser clicando no botão à direita.


Conceda as permissões necessárias para instalar e utilizar a extensão e, em seguida, fixe a extensão na barra de ferramentas para facilitar a recuperação.



![pin](assets/fr/03.webp)



Você também deve definir um código de desbloqueio (muito importante), que garantirá o acesso seguro ao seu Lightning wallet a partir do seu navegador. Sugerimos que defina uma palavra-passe alfanumérica forte.



ℹ️ Guarde esta palavra-passe num local seguro para poder aceder-lhe em caso de esquecimento, uma vez que pode ser alterada mas não recuperada.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



O Alby demonstra a sua capacidade de adaptação ao oferecer-lhe duas opções:




- Continue com uma conta Alby se quiser desfrutar das aplicações enquanto mantém o controlo dos seus bitcoins.
- Ligue o seu próprio nó wallet ou Lightning se já tiver um suportado pela extensão.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


Neste tutorial, optámos por continuar com a conta Alby para tirar partido das funcionalidades do ecossistema Alby.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Inicie sessão na sua conta Alby ou crie uma se ainda não tiver uma.



![signup](assets/fr/05.webp)



## Efetuar os primeiros pagamentos



Uma vez iniciada a sessão, pode clicar na extensão Alby na barra de ferramentas para aceder à sua carteira.



![buzzin](assets/fr/06.webp)



Depois de criares a tua conta Alby, terás de a ligar a um wallet para poderes gastar satoshis. Para ligar o bitcoin wallet à tua conta Alby, sugerimos que utilizes um nó Alby Hub, que podes configurar no teu computador ou subscrever um plano oferecido pelo Alby.



![hubplan](assets/fr/13.webp)




Neste tutorial, a nossa conta Alby é suportada por uma instalação local na nossa máquina.


Para construir o seu próprio nó Alby, recomendamos o nosso tutorial Alby Hub.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Este nó permite-lhe criar carteiras Lightning auto-custodiais e gerir eficazmente os seus canais Lightning para enviar e receber satoshis.



![channels](assets/fr/14.webp)



Abrir canais de receção que definem o número total de satoshis que pode receber.



![receivechanal](assets/fr/15.webp)



Abra canais de envio bloqueando satoshis num endereço bitcoin onchain. Os satoshis que bloqueou definem o total de satoshis que pode gastar.



![spend](assets/fr/16.webp)



Agora é possível enviar e receber satoshis através da extensão Alby.



![exchange](assets/fr/08.webp)



A partir deste momento, a extensão Alby é capaz de detetar os endereços Lightning e as facturas disponíveis nas páginas Web que visita e sugere-lhe que as pague em bitcoin ou Lightning diretamente a partir da sua extensão.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Proteger as chaves de recuperação com a chave mestra



A chave mestra oferecida pela extensão Alby actua como uma sobreposição protetora que lhe permite comunicar de forma segura com a camada de rede principal do Bitcoin (Onchain), o sistema Nostr e permite-lhe ativar a ligação Lightning com as aplicações Nostr.



![masterKey](assets/fr/11.webp)



Esta chave mestra tem a forma de 12 palavras semelhantes à sua frase de recuperação. Por isso, recomendamos que a guarde utilizando métodos seguros para garantir que pode ser acedida em qualquer altura.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Agora você pode experimentar pagamentos sem atrito de bitcoin e Lightning com a extensão Alby. Se você gostou deste tutorial, recomendamos nosso tutorial Alby Hub para configurar seu próprio nó Alby e controlar todos os aspectos de suas carteiras Alby a partir de uma interface suave e poderosa.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a