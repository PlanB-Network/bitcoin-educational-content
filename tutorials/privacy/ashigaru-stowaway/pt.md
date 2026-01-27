---
name: Ashigaru - Stowaway
description: Como posso efetuar uma transação Payjoin em Ashigaru?
---
![cover](assets/cover.webp)



> *Forçar os espiões da cadeia de blocos a repensar tudo o que pensam que sabem

O Payjoin é uma estrutura de transação Bitcoin concebida para aumentar a confidencialidade do utilizador ao envolver a colaboração direta com o destinatário do pagamento. Existem várias implementações para facilitar a sua aplicação e automatizar o processo. A mais conhecida é, sem dúvida, o Stowaway, inicialmente desenvolvido pela equipa do Samurai Wallet e agora integrado no seu Ashigaru fork.



## Como é que o Stowaway funciona?



Como mencionado anteriormente, o Ashigaru integra uma ferramenta PayJoin chamada `Stowaway`. Esta está disponível na aplicação Ashigaru para Android. Para que um Payjoin seja realizado, o destinatário (que também assume o papel de colaborador) deve estar a utilizar um software compatível com o Stowaway, ou seja, apenas Ashigaru de momento.



O Stowaway baseia-se numa categoria de transacções que Samurai designou por "Cahoots". Um Cahoot é uma transação colaborativa entre vários utilizadores, envolvendo uma troca de informações fora da blockchain Bitcoin. A Ashigaru oferece atualmente duas ferramentas Cahoots: Stowaway (Payjoins) e StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

As transacções Cahoots requerem a troca de transacções parcialmente assinadas entre utilizadores. Este processo pode ser longo e tedioso, especialmente quando efectuado remotamente. No entanto, ainda é possível fazê-lo manualmente, se os colaboradores estiverem no mesmo local. Em termos concretos, trata-se de digitalizar cinco códigos QR sucessivamente, trocados entre os dois participantes.



À distância, este método torna-se demasiado complexo. Para remediar esta situação, Samourai desenvolveu um protocolo de comunicação encriptado baseado no Tor, denominado "*Soroban*". Graças ao Soroban, os intercâmbios necessários para um Payjoin são automatizados e realizam-se em segundo plano.



Estas comunicações encriptadas requerem uma ligação e autenticação entre os participantes do Cahoot. É por isso que o Soroban depende dos Paynyms dos utilizadores. Se você ainda não está familiarizado com o funcionamento do Paynyms, dê uma olhada neste tutorial dedicado para saber mais:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Em poucas palavras, um Paynym é um identificador único associado ao seu wallet, que lhe permite ativar várias funções, incluindo trocas encriptadas. Tem a forma de um identificador acompanhado de uma ilustração. Eis, por exemplo, o que utilizo no Testnet:



![Image](assets/fr/01.webp)



**Resumindo





- payjoin" = Estrutura específica de transação colaborativa;





- `Stowaway` = Implementação do Payjoin disponível em Ashigaru ;





- `Cahoots` = Nome dado pelos Samourai a todos os seus tipos de transacções colaborativas, em particular o Payjoin `Stowaway`, hoje assumido em Ashigaru ;





- soroban = Protocolo de comunicação encriptado estabelecido no Tor que permite a colaboração com outros utilizadores numa transação `Cahoots`;





- paynym" = Identificador único wallet utilizado para estabelecer comunicação com outro utilizador no "Soroban", a fim de efetuar uma transação "Chahoots".



Para uma análise mais aprofundada sobre como funcionam os Payjoins e a sua utilidade na privacidade onchain, recomendo este outro tutorial:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Como é que estabeleço uma ligação entre Paynyms?



Para começar, é claro que você precisa instalar o Ashigaru e criar um arquivo :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Para realizar uma transação Cahoots remota, incluindo um PayJoin (*Stowaway*) via Ashigaru, deve primeiro "seguir" o utilizador com quem deseja colaborar, usando o seu Paynym. No caso de um Stowaway, isto significa seguir a pessoa a quem deseja enviar bitcoins. Se ainda não sabe como seguir outro Paynym, encontrará o procedimento detalhado neste tutorial :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Como é que faço um Payjoin no Ashigaru?



Para efetuar uma transação Stowaway, clique na imagem do seu Paynym no canto superior esquerdo do ecrã e abra o menu "Colaborar". A pessoa que participa na transação consigo deve fazer o mesmo, a não ser que estejam a trocar códigos QR pessoalmente.



![Image](assets/fr/02.webp)



Tem duas opções: selecionar `Iniciar` se for o remetente do pagamento, ou `Participar` se for o beneficiário deste pagamento.



![Image](assets/fr/03.webp)



Se for o destinatário, o procedimento é muito simples. Para a colaboração à distância através da rede Soroban, clique em `Participar`, escolha a conta que deseja utilizar, depois prima `Esperar PEDIDOS DE CAHOOTS` para aguardar o pedido enviado pelo pagador.



![Image](assets/fr/04.webp)



Por outro lado, para a colaboração presencial através da leitura do código QR, vá à página inicial do seu wallet, prima o ícone do código QR na parte superior do ecrã e, em seguida, leia o código QR fornecido pelo pagador que inicia a transação.



![Image](assets/fr/05.webp)



Se estiver na função de pagador, ou seja, se for o iniciador da transação, vá ao menu `Colaborar` e selecione `Iniciar`.



![Image](assets/fr/06.webp)



Para o tipo de transação, uma vez que pretendemos fazer um Payjoin Stowaway, escolha esta opção.



![Image](assets/fr/07.webp)



Pode então escolher entre a colaboração em linha (*Cahoots* via *Soroban*) ou a colaboração presencial, com troca de códigos QR.



![Image](assets/fr/08.webp)



### Cahoots online



Se escolheu a opção `Online`, selecione o destinatário a partir dos Paynyms que está a seguir.



![Image](assets/fr/09.webp)



Clique em "Configurar transação" e, em seguida, escolha a conta a partir da qual pretende efetuar a despesa.



![Image](assets/fr/10.webp)



Na página seguinte, introduza os dados da transação: o montante a enviar ao destinatário e a taxa de carregamento. Não é necessário introduzir um endereço de receção, uma vez que o destinatário o transmitirá ele próprio durante os intercâmbios PSBT.



Em seguida, clique em "Rever a configuração da transação".



![Image](assets/fr/11.webp)



Verifique cuidadosamente as informações, certifique-se de que o seu colaborador está a ouvir os pedidos *Cahoots*, depois clique no botão verde `BEGIN TRANSACTION` para iniciar a troca de PSBTs via Soroban.



![Image](assets/fr/12.webp)



Aguarde até que ambos os participantes tenham assinado a transação e, em seguida, transmita-a na rede Bitcoin.



![Image](assets/fr/13.webp)



### Discussões presenciais



Se desejar efetuar a troca pessoalmente, selecione o tipo de transação `STONEWALL X2` e, em seguida, escolha a opção `Pessoal / Manual`.



![Image](assets/fr/14.webp)



Clique em "Configurar transação" e, em seguida, escolha a conta a partir da qual pretende efetuar a despesa.



![Image](assets/fr/15.webp)



Na página seguinte, introduza os dados da transação: o montante a enviar ao destinatário e a taxa de carregamento. Não é necessário introduzir um endereço de receção, uma vez que o destinatário o transmitirá ele próprio durante os intercâmbios PSBT.



Em seguida, clique em "Rever a configuração da transação".



![Image](assets/fr/16.webp)



Verifique os dados e, em seguida, prima o botão verde "INICIAR TRANSAÇÃO" para iniciar a troca de PSBT através da leitura do código QR.



![Image](assets/fr/17.webp)



A troca é feita alternando a digitalização com o colaborador: clique em `MOSTRAR CÓDIGO QR` para mostrar o seu código QR ao seu colaborador, que o digitalizará. Este, por sua vez, clica em `MOSTRAR CÓDIGO QR` para mostrar o seu, e o colaborador digitaliza-o com `Lançar scanner QR`. Repita este processo até que as cinco etapas de intercâmbio tenham sido concluídas.



![Image](assets/fr/18.webp)



Quando todas as trocas estiverem concluídas, verifique os detalhes da transação e, em seguida, liberte-a arrastando a seta verde na parte inferior do ecrã.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). A sua estrutura é a seguinte:



![Image](assets/fr/20.webp)



*Crédito: [mempool.space](https://mempool.space/)*



Se analisarmos esta transação, vemos o meu UTXO de `164 211 sats` no lado da entrada, bem como o UTXO de `190 002 sats` pertencente ao beneficiário efetivo do pagamento. Do lado da saída, recebo um UTXO de troca de `63 995 sats`, enquanto o beneficiário recebe um UTXO de `290 002 sats`. Comparando entradas e saídas, podemos ver que o beneficiário ganhou efetivamente 100 000 sats`, o que corresponde ao montante do meu pagamento efetivo, e que eu perdi 100 000 sats`, aos quais acrescentei os custos mining.



Obviamente, posso descrever esta estrutura porque eu próprio construí a transação. Mas para um observador externo, é geralmente impossível determinar que UTXOs pertencem a que participante, quer nas entradas quer nas saídas.



Para aprofundar seu conhecimento sobre o gerenciamento de privacidade onchain no Bitcoin, recomendo que você faça meu treinamento BTC 204 na Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c