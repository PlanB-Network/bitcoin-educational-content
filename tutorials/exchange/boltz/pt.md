---
name: Boltz
description: Alterne entre diferentes camadas de Bitcoin mantendo o controlo.
---


![cover](assets/cover.webp)



Desde a sua implantação em 2009, o sistema de dinheiro eletrónico peer-to-peer do Bitcoin cresceu exponencialmente, dando vida a soluções que lhe permitem hoje ser um sistema que podemos utilizar instantaneamente nas nossas acções quotidianas, nomeadamente através do Lightning Network.



No entanto, subsistia um problema importante entre as camadas do protocolo Bitcoin: a interoperabilidade dos fluidos. Para explorar todo o potencial do Bitcoin, era imperativo encontrar uma solução que permitisse transacções entre as diferentes camadas do protocolo. Esta necessidade deu origem, em 2019, ao Boltz, uma ponte que liga vários níveis do Bitcoin.



## O que é Boltz?



[Boltz](https://boltz.Exchange) é uma plataforma sem custódia ideal para quem deseja efetuar transacções entre as diferentes camadas do protocolo Bitcoin:




- on chain**: A principal cadeia do Bitcoin, onde as transacções são confirmadas a cada 10 minutos em média, as taxas de transação são frequentemente elevadas, o que não satisfaz necessariamente as necessidades dos utilizadores;
- Lightning Network**: A sobreposição do Bitcoin para pagamentos instantâneos com taxas baixas, permitindo que o Bitcoin seja utilizado para pagamentos diários;
- Liquid Network**: uma sobreposição para o Bitcoin criada pela Blockstream, que permite a utilização rápida do Confidential Transactions e de outros instrumentos financeiros baseados no Bitcoin;
- RootStock**: Uma solução para o desenvolvimento de contratos inteligentes baseados no protocolo Bitcoin.



![layers](assets/fr/01.webp)



A interoperabilidade entre estes diferentes níveis é da maior importância, uma vez que dá aos utilizadores a flexibilidade de que necessitam para tirar o máximo partido de tudo o que o ecossistema Bitcoin tem para oferecer.



A Boltz utiliza swaps atómicos. Esta tecnologia permite trocar bitcoins entre 2 camadas (por exemplo, BTC onchain em Exchange por BTC em Lightning) diretamente entre duas partes, sem necessidade de confiança e sem necessidade de um intermediário. Estas trocas são designadas "atómicas" porque só podem produzir dois resultados:




- Ou o Exchange é bem sucedido e os dois participantes trocaram efetivamente as suas BTC ;
- Ou o Exchange falha, e ambos os participantes saem com as suas BTC originais.



Desta forma, o utilizador mantém a auto-custódia permanente das suas bitcoins e o Exchange não se baseia em qualquer confiança na contraparte: ou o Exchange tem êxito ou falha, mas nenhuma das partes pode roubar os fundos da outra.



Um Exchange atómico funciona com contratos inteligentes [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). Neste tipo de Contract, o montante é "bloqueado" num canal bidirecional e é introduzida uma restrição temporal, pelo que, se a transação não for concluída dentro de um determinado prazo, o saldo reverte para o depositante. Este é o mecanismo utilizado pela plataforma Boltz.



## As tuas primeiras trocas com Boltz



A Boltz é uma plataforma web não depositária que não requer qualquer informação pessoal do utilizador. A Boltz tem um Interface minimalista e fluido que lhe permite começar a negociar em menos de um minuto.



![boltz](assets/fr/02.webp)



Uma vez na plataforma, é possível criar trocas atómicas entre os diferentes níveis do ecossistema Bitcoin.



![home](assets/fr/03.webp)



Verás o número mínimo e máximo de satoshis (a unidade mais pequena de Bitcoin) que podes transacionar através do Boltz, incluindo taxas de rede e uma percentagem cobrada pelo Boltz entre 0,1% e 0,5%.



![fees](assets/fr/04.webp)



Em seguida, selecione o Layer a partir do qual pretende criar um Exchange atómico e selecione o Layer no qual pretende receber os bitcoins.



![couches](assets/fr/05.webp)



Neste tutorial, vamos concentrar-nos no Exchange atómico do Layer principal para o Lightning Network.



Pode configurar a unidade mestra para as suas trocas, escolhendo entre as opções :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Quando tiver concluído as suas configurações básicas, insira o montante do seu Exchange atómico e, em seguida, crie um Invoice relâmpago para o montante equivalente ou insira simplesmente o seu LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Por razões de segurança, verifique os parâmetros do seu Exchange atómico para exportar as chaves de segurança ligadas ao seu Exchange.



No ícone **Configurações**, descarregue a chave de cópia de segurança e guarde o ficheiro de forma adequada.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Este ficheiro contém as 12 palavras-chave da carteira associadas às suas trocas atómicas.



Em seguida, clique no botão **Criar Exchange atómico** e proceda ao pagamento do montante indicado.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Assim que o seu pagamento for efectuado e confirmado, receberá automaticamente o montante equivalente no seu Lightning Wallet.



No menu **Reembolsar**, procure o seu histórico atómico do Exchange para identificar o Exchange em que deseja ser reembolsado. Também pode importar um histórico de trocas efectuadas noutro aparelho, por exemplo, utilizando o ficheiro de chaves de segurança associado a essas trocas.



![refund](assets/fr/11.webp)



No menu **Histórico**, pode descarregar um histórico mais detalhado das trocas associadas à sua chave de recuperação clicando no botão **Cópia de segurança**.



![backup](assets/fr/12.webp)



⚠️ Também não divulgue este ficheiro, pois contém todas as informações associadas às suas transacções e a chave de segurança associada a essas transacções.



O Boltz oferece-lhe um elevado nível de confidencialidade graças ao seu acesso através de uma ligação `.onion' na rede Tor. Torne as trocas atómicas totalmente anónimas selecionando o menu **Onion**, depois de ativar a navegação Tor no seu navegador.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Neste momento, já conhece o Boltz, uma plataforma Exchange única que permite a interoperabilidade entre os diferentes níveis do ecossistema Bitcoin.