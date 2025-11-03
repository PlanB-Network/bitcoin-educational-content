---
name: StashPay
description: O Bitcoin Wallet minimalista para todos
---

![cover](assets/cover.webp)



A experiência do utilizador é um fator-chave na adoção de soluções Bitcoin em todo o mundo. Fornecer uma experiência suave, simples e tecnicamente livre é a prioridade para muitas carteiras e plataformas Exchange. A este respeito, a StashPay destaca-se pela sua abordagem minimalista, ao mesmo tempo que demonstra o poder da Lightning Network.



Neste tutorial, vamos dar uma vista de olhos a este portefólio para descobrir como funciona e como é ideal para pequenas empresas ou empresários em nome individual.



## Começar a utilizar o StashPay



StashPay é um Wallet autocustodial Lightning reconhecido principalmente pela sua experiência de utilizador minimalista e centrada no utilizador.  Com este Wallet, não é necessário qualquer conhecimento técnico para receber e enviar os seus primeiros satoshis.



O StashPay é um projeto open-source desenvolvido em React Native e tem como objetivo resolver o problema das altas taxas de transação mesmo com transações na cadeia principal do protocolo Bitcoin. Está disponível como uma aplicação móvel nas plataformas Android e iOS através de ligações de transferência presentes no [sítio Web](https://stashpay.me/).



![introduce](assets/fr/01.webp)



É importante descarregar a aplicação Android a partir do sítio Web, uma vez que não está disponível na Google Play Store.


Quando a transferência estiver concluída, conceda as permissões necessárias para que possa instalar a aplicação no seu telemóvel Android.



Uma vez instalada a aplicação, o StashPay criará um Bitcoin Wallet inicial para si na primeira vez que a abrir. Antes de qualquer transação, recomendamos que faça uma cópia de segurança deste Wallet. Abaixo, encontrará todas as nossas diretrizes para garantir que as suas frases de recuperação têm uma cópia de segurança adequada.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Aceder às definições do StashPay clicando no ícone "Definições" e, em seguida, na opção **Criar cópia de segurança**. Em seguida, autorizar a visualização das frases de recuperação. Não copie as suas frases de recuperação para a área de transferência do seu telemóvel, pois podem estar acessíveis a outras aplicações fraudulentas instaladas no seu telemóvel.



![backup](assets/fr/02.webp)



Também pode recuperar um Bitcoin Wallet que já esteja a utilizar, clicando na opção **Recuperar Wallet** e inserindo as suas 12 ou 24 palavras de recuperação.



### Receber os seus primeiros satoshis no StashPay



No ecrã inicial, clique no botão **Receber** e defina um montante superior ao montante especificado a vermelho. No nosso caso, não podemos receber menos de 0,11 USD com o StashPay Wallet.



![receive](assets/fr/03.webp)



Depois de ter definido o montante, pode clicar no botão **Criar Invoice** e, em seguida, digitalizar ou copiar o Invoice para o enviar para o seu remetente satoshis.



![receive_sats](assets/fr/04.webp)



Pode ver o seu histórico de transacções clicando no ícone "relógio" na página inicial.



![network_fee](assets/fr/05.webp)



Deves ter reparado que, para receberes satoshis, tens de pagar uma taxa de rede. Estas taxas serão deduzidas dos satoshis que está prestes a receber. Isto deve-se ao facto de o StashPay ser um Wallet baseado no Breez Development Kit. Para receber satoshis com a implementação do Kit sem nós Lightning, a Breez cobrará ao cliente (StashPay no nosso caso) `0,25% + 40 satoshis`. Saiba mais no nosso tutorial Misty Breez.



https://planb.academy/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Enviar bitcoins com o StashPay



O envio de bitcoins com o StashPay é bastante intuitivo graças ao Interface minimalista. No ecrã inicial, clicar no botão **Enviar**. Digitalize o código QR ou cole o Address para o qual deseja enviar satoshis. O StashPay detectará automaticamente a cadeia do protocolo Bitcoin para a qual deseja enviar bitcoins.



![send](assets/fr/06.webp)



Como o StashPay é um Wallet baseado no Kit de Desenvolvimento Breez, beneficia de uma vantagem interessante: enviar bitcoins na cadeia principal a baixo custo. A Breez utiliza o serviço Boltz para realizar transacções entre as diferentes cadeias do protocolo Bitcoin, permitindo aos clientes que implementam o Kit de Desenvolvimento beneficiar deste serviço diretamente na sua aplicação.



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

No entanto, o Breez SDK impõe um montante mínimo a partir do qual é possível enviar bitcoins para um Address na cadeia principal.



![onchain](assets/fr/07.webp)



Também pode enviar bitcoins utilizando o Lightning Address do seu destinatário. Reveja os detalhes da transação e confirme clicando no botão **Enviar**.



![confirm](assets/fr/08.webp)



## Mais configurações



Nas definições do StashPay, pode ajustar as configurações para personalizar a sua utilização do Wallet.



StashPay permite-lhe Exchange satoshis com base na moeda local da sua escolha. Clique na opção **Moedas** e, em seguida, procure a sua moeda na lista de +113 moedas oferecidas pelo StashPay.



![currencies](assets/fr/09.webp)



No menu **Opções de receção**, encontrará todas as definições para receber bitcoins com o StashPay. Por exemplo, ao selecionar **Escolher Lightning ou Onchain**, permite que o teu Wallet receba bitcoins da cadeia principal.



![receive-onchain](assets/fr/10.webp)



A opção **Scan OnChain addresses** permite-lhe atualizar o saldo do seu Wallet verificando todos os UTXOs (bitcoins que ainda não gastou) ligados aos seus vários endereços.



![rescan](assets/fr/11.webp)



O menu **Exportar registo** lista todas as acções da infraestrutura Breez e Boltz relativas às suas transacções e trocas atómicas entre as várias cadeias do protocolo Bitcoin.



![export](assets/fr/12.webp)



Acabou de se familiarizar com o Bitcoin Wallet minimalista da StashPay. Se achou este tutorial útil, recomendamos o nosso tutorial sobre como começar a utilizar o Bitcoin e ganhar os seus primeiros bitcoins.



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f