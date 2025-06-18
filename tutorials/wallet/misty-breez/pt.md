---
name: Brisa de Névoa
description: O Lightning Wallet sem arco.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez é um Wallet autónomo Lightning desenvolvido pela Breez com base no seu Kit de Desenvolvimento de Software e na rede **Liquid** desenvolvida pela BlockStream.


Inclui uma abordagem completamente nova ao funcionamento sem um nó Lightning: uma potencial **MUDANÇA DE JOGO** nas transferências inter-redes Bitcoin.


Neste tutorial, descreveremos o funcionamento desta carteira e dar-lhe-emos uma visão geral completa.



## Como é que o Misty Breez funciona?



Misty Breez é uma implementação sem um nó Lightning como backend. Foi desenvolvida com base no Breez SDK e no Liquid.



O Liquid é um Layer paralelo à rede Bitcoin, oferecendo melhorias significativas na velocidade e nos custos de transação. Este Layer permite que Misty Breez dispense um nó Lightning e, em vez disso, use serviços Exchange de terceiros, como **Boltz**, para garantir a interoperabilidade entre o Liquid Network e o Lightning Network. Não se apressem, voltaremos a este assunto.



Para já, vamos começar a nossa aventura com o Misty Breez Wallet.



## Começar a utilizar o Misty Breez



A aplicação móvel Misty Breez está disponível nas plataformas de transferência oficiais, como a Google Play Store (no Android) e a Apple Store (no iOS). Também pode ser redireccionado para a aplicação certa a partir do sítio Web oficial [Misty Breez] (https://breez.technology/misty/).



⚠️ Não confundir o Misty Breez com o Breez Wallet.



⚠️ **IMPORTANTE**: Para a segurança dos seus bitcoins, é essencial descarregar a aplicação a partir de plataformas oficiais para garantir a sua autenticidade.



![download-misty-breez](assets/fr/01.webp)



Neste tutorial, vamos começar a partir de um dispositivo Android. No entanto, cada um dos passos e funcionalidades específicos detalhados nesta secção aplicam-se ao iOS.



Após a instalação, Misty Breez dá-lhe a opção de criar um novo Wallet ou restaurar um antigo Lightning Wallet para o qual tem as palavras de recuperação.


Neste tutorial, optamos por criar um novo portefólio.



o ⚠️Misty Breez está atualmente em fase de desenvolvimento, pelo que aconselhamos a começar com quantidades razoáveis.



![create-wallet](assets/fr/02.webp)


### Guarde as suas palavras de recuperação :


Uma das primeiras coisas que deve fazer ao criar um novo portefólio é fazer uma cópia de segurança das suas 12 palavras de recuperação.


Seguem-se algumas sugestões sobre como fazer uma cópia de segurança da sua frase de segurança.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Para fazer uma cópia de segurança das suas frases, selecione o menu **Preferências > Segurança** e, em seguida, a opção **Verificar a sua frase de cópia de segurança**.



![backup](assets/fr/03.webp)


Para maior segurança, pode também **criar um código PIN** para autenticar o acesso ao seu Wallet.




Encontre a sua moeda local na multiplicidade de moedas aceites pelo Misty Breez. Configure a sua moeda no menu **Preferências > Moedas Fiat**, depois selecione a moeda ou moedas que pretende.



![devises](assets/fr/04.webp)



### Efetuar as primeiras transacções


Se já está familiarizado com o portefólio Breez, não ficará de todo desanimado com o intuitivo Interface do Misty Breez.



No menu **Balance** do Interface, clique na opção **Receive** para criar facturas para receber os seus bitcoins no seu Wallet.



⚠️ Misty Breez pedir-lhe-á que active as notificações da aplicação nas definições do seu telemóvel para lhe dar direito a um Lightning Address.



Com Misty Breez, pode :




- Receber bitcoins no Lightning Network de **100 satoshis** até **25.000.000 satoshis**.
- Receber bitcoins na rede principal Bitcoin a partir de **25.000 satoshis**.



![transactions](assets/fr/05.webp)



É aqui que começa a magia de Misty Breez.


Ao contrário do Breez Wallet, que lhe fornece um nó Lightning e lhe pede para cobrir os custos de abertura e fecho dos canais de pagamento, o Misty Breez não lhe pede para fazer nada. Como mencionado anteriormente, o Misty Breez nem sequer funciona com base num nó Lightning.



Vamos dar uma vista de olhos aos bastidores.



Na realidade, possui uma carteira Liquid que está associada à sua carteira Misty Breez. Logicamente, estará a lidar com L-BTC (Liquid Bitcoin) a taxas fixas associadas a serviços de conversão de satoshis submarinos de terceiros que lhe permitirão interoperar com o Lightning Network.



Quando recebe um pagamento no seu Misty Breez Wallet, o remetente envia-lhe satoshis que passarão por um serviço de conversão como o Boltz (atualmente utilizado pela Misty Breez), para converter os satoshis enviados em L-BTC que serão recebidos no seu Misty Breez Wallet (associado Liquid Wallet).


Eis um diagrama simplificado do processo nos bastidores.



![lnswap-in](assets/fr/06.webp)



Clicar no Interface no menu **Saldo**, clicar na opção **Enviar** para pagar um Invoice relâmpago.


Insira o Lightning Invoice, o Lightning Address do seu destinatário ou simplesmente digitalize o código QR no Invoice para efetuar o seu pagamento.



![send-bitcoins](assets/fr/07.webp)



Nos bastidores, você habilita o Liquid Wallet associado ao seu Misty Breez Wallet para converter o equivalente a L-BTC em satoshis via Boltz, depois transfere esses satoshis para o Lightning Wallet do seu destinatário (presente no Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Esta caraterística da infraestrutura do Misty Breez permite que os utilizadores efectuem transacções mesmo quando o Misty Breez está offline.



Para os mais experientes, existe também um menu **Preferências > Programadores** que lhe dá um pouco mais de pormenor sobre o :




- A versão do Kit de Desenvolvimento de Software Breez.
- A chave pública do seu Misty Breez Wallet.
- O mutuário, o identificador único derivado da chave pública primária.
- O saldo da sua carteira.
- Dica Liquid, para enviar pequenas quantidades de L-BTC.
- A ponta Bitcoin, para enviar pequenas quantidades de Bitcoin.



Também pode executar determinadas acções, como sincronizar com o Liquid Network, fazer cópias de segurança das suas chaves, partilhar o seu registo de actividades e optar por voltar a analisar o Liquid Network.



![dev-mode](assets/fr/09.webp)


Parabéns! Agora você tem uma boa compreensão do portfólio Misty Breez e sua contribuição para as transações inter-redes Bitcoin. Se você achou este tutorial útil, por favor, dê-nos um polegar Green. Teremos todo o gosto em ouvir de si.



Para ir mais longe, recomendo também que descubram o nosso tutorial sobre o Aqua Wallet, que funciona de forma semelhante ao Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125