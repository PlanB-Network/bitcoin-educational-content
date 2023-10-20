---
name: Watch Tower
description: Compreendendo e usando uma torre de observação
---

> Crédito para: https://blog.summerofbitcoin.org/bitcoin-lightning-and-the-eye-of-satoshi-watchtower-revolutionizing-transactions-and-security//

## Como as torres de observação funcionam?

Parte essencial do ecossistema da Lightning Network, as torres de observação fornecem um grau extra de proteção aos canais de raio dos usuários. Sua principal responsabilidade é monitorar a saúde dos canais e intervir se uma das partes do canal tentar fraudar a outra.

Então, como uma torre de observação pode determinar se um canal foi comprometido? A torre de observação recebe as informações necessárias do cliente, uma das partes do canal, para identificar e responder adequadamente a qualquer violação. Os detalhes da transação mais recente, a condição atual do canal e as informações necessárias para criar transações de penalidade são frequentemente incluídos nessas informações. Antes de transmitir os dados para a torre de observação, o cliente pode criptografá-los para proteger a privacidade e o sigilo. Isso impede que a torre de observação descriptografe os dados criptografados, a menos que ocorra uma violação, mesmo que ela obtenha os dados. A privacidade do cliente é protegida por esse sistema de criptografia, que também impede que a torre de observação acesse dados privados sem autorização.

## Como configurar seu próprio Eye of Satoshi e começar a contribuir

O Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) é uma torre de observação Lightning não custodial compatível com [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Ele possui dois componentes principais:

1. teos: incluindo uma CLI e a funcionalidade principal do lado do servidor da torre. Dois binários - teosd e teos-cli - serão produzidos quando esta caixa for construída.

2. teos-common: incluindo funcionalidade compartilhada do lado do servidor e do lado do cliente (útil para criar um cliente).

Para executar a torre com sucesso, você precisará ter o bitcoind em execução antes de executar a torre com o comando teosd. Antes de executar esses comandos, você precisa configurar seu arquivo bitcoin.conf. Aqui estão as etapas de como fazer isso:-

1. Instale o bitcoin core a partir da fonte ou faça o download. Após o download, coloque o arquivo bitcoin.conf no diretório do usuário do Bitcoin core. Verifique este link para obter mais informações sobre onde colocar o arquivo, pois isso depende do sistema operacional que você está usando.

2. Após identificar o local onde o arquivo precisa ser criado, adicione estas opções:-

```
#RPC
server=1
rpcuser=<seu-usuário>
rpcpassword=<sua-senha>

#chain
regtest=1
```

- server: Para solicitações RPC
- rpcuser e rpcpassword: Os clientes RPC podem autenticar-se com o servidor
- regtest: Não é necessário, mas útil se você estiver planejando para desenvolvimento.

rpcuser e rpcpassword precisam ser escolhidos por você. Eles devem ser escritos sem aspas. Por exemplo:-

```
rpcuser=aniketh
rpcpassword=senhaforte
```

Agora, se você executar o bitcoind, ele deve iniciar a execução do nó.

1. Para a parte da torre, primeiro, você precisa instalar o teos a partir da fonte. Siga as instruções fornecidas neste link.
2. Após instalar com sucesso o teos em seu sistema e executar os testes, você pode prosseguir com o último passo, que é configurar o arquivo teos.toml no diretório do usuário teos. O arquivo precisa ser colocado em uma pasta chamada .teos (observe o ponto) dentro da sua pasta pessoal. Ou seja, por exemplo, /home/<seu-nome-de-usuário>/.teos para Linux. Assim que encontrar o local, crie um arquivo teos.toml e defina essas opções correspondentes às coisas que alteramos no bitcoind.

```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <seu-usuário>
btc_rpc_password = <sua-senha>
```

Observe que aqui o nome de usuário e a senha precisam ser escritos entre aspas, ou seja, para o mesmo exemplo anterior:

```
btc_rpc_user = "aniketh"
btc_rpc_password = "senhaforte"
```

Depois de fazer isso, você estará pronto para executar a torre. Como estamos executando no regtest, é provável que não haja blocos minerados em nossa rede de teste do bitcoin na primeira vez em que a torre se conectar a ela (se houver, algo está definitivamente errado). A torre cria um cache interno dos últimos 100 blocos do bitcoind, então, ao executar pela primeira vez, podemos receber o seguinte erro:

> ERRO [teosd] Não há blocos suficientes para iniciar a torre (necessários: 100). Minerar pelo menos mais 100

Como estamos executando no regtest, podemos minerar um bloco emitindo um comando RPC, sem precisar esperar pelo tempo médio de 10 minutos que normalmente vemos em outras redes (como mainnet ou testnet). Verifique a ajuda do bitcoin-cli e procure como minerar blocos. Se precisar de ajuda, você pode ler este artigo.

![image](assets\2.jpeg)

É isso, você executou a torre com sucesso. Parabéns. 🎉
