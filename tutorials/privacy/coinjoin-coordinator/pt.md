---
name: Coordenador Coinjoin - WabiSabi
description: Como configurar e executar um coordenador de coinjoin seguindo o protocolo WabiSabi (usado no Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Introdução 👋


Neste guia especializado, vamos ajudá-lo a configurar um coordenador coinjoin, essencialmente um servidor que reúne pessoas que querem economizar em taxas de transação ou aumentar a sua privacidade onchain em transações colaborativas. Uma vez que já não existe um coordenador gerido por uma empresa, incluído no Wasabi Wallet, os utilizadores têm de encontrar e selecionar o seu próprio servidor coordenador preferido. Apenas alguns coordenadores apareceram pedindo uma taxa de coordenação de 0%, então os desenvolvedores do Wasabi Wallet têm trabalhado duro para tornar o mais fácil possível começar a executar seu próprio coordenador de comunidade (em hardware tão pequeno quanto um Raspberry Pi5!). Os coordenadores atualmente activos que pedem 0% de taxa de coordenação podem ser encontrados em [LiquiSabi](https://liquisabi.com) e, mais importante, em [nostr](https://github.com/Kukks/WasabiNostr).


## Requisitos 🫴



- VPS (nó hospedado) ou computador/servidor (nó auto-hospedado)
- Nó principal Bitcoin podado/completo (testado com a versão 29.0)


Opcional:


- (sub)Domínio que encaminha o tráfego para o nó (por exemplo, coinjoin.[yourdomain].io)


Recomenda-se que tenha alguma experiência com comandos de linha de comandos e bash, uma vez que nem todos os passos podem ser automatizados.


Em termos de hardware, é aconselhável ter um sistema com:


- 4 núcleos
- 16 GB DE RAM
- sSD de 2 TB ou NVMe (para um nó completo) / SSD de 128 GB (para um nó pruned)


Estes requisitos podem ser fornecidos por um Raspberry Pi 5 por apenas 120 dólares, excluindo o armazenamento que custa cerca de 100 dólares por uma pen de 2TB NVMe.


Os VPS baratos normalmente vêm com apenas 1 núcleo e 4GB de RAM, o que eu descobri ser muito pouco para sincronizar e verificar todo o bitcoin blockchain no blockheight 911817.


Em termos de armazenamento, um nó completo precisará de, no mínimo, 2 TB de armazenamento em disco, de preferência do tipo SSD ou NVMe. Ao podar o blockchain, uma unidade de armazenamento muito menor é aceitável (por exemplo, um SSD de 128 GB).


Se tenciona executar um coordenador para grandes junções de moedas (mais de 300 entradas), é aconselhável escolher um sistema com núcleos mais rápidos/novos com um desempenho superior para todas as verificações de assinaturas.


## Instalação 🛠️


No nó, queremos descarregar e instalar a última versão lançada do Wasabi Wallet, que inclui um backend e um coordenador como executáveis autónomos ao lado do wallet.


Encontrar a última versão: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) e verifique a assinatura PGP da versão com as chaves: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Os detalhes da implantação diferem dependendo do hardware (arquitetura da CPU) e da escolha do sistema operacional. Abaixo, os diferentes detalhes são fornecidos para um Raspberry Pi (ARM-64) com o Debian baseado no RaspiBlitz como ponto de partida. Pule adiante para a implantação do SO Ubuntu (X86-64) usando Nix.


Encontre as instruções de instalação aqui: [Wasabi Docs] (https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Implantação do RaspiBlitz/Debian


Para os nós RaspiBlitz (testados com a v1.11) pode ser utilizada uma implementação script construída a partir do código fonte: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Fácil implementação


Para uma implementação mínima, basta extrair os executáveis para a sua plataforma numa pasta.

Exemplo de códigos de linha de comando para Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


O resultado deve ser a seguinte mensagem de assinatura válida:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


E pode proceder à instalação do pacote descarregado:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Configuração 🧾


Antes de executar o coordenador, é necessário editar o arquivo Config.json com o seu:


- Credenciais Bitcoin RPC
- Parâmetros de ronda preferidos
- Chave pública alargada do coordenador (criar um novo SegWit wallet para receber as poeiras recolhidas)

**Aviso**: Taproot wallet resultará em UTXO não gastáveis! Use um Segwit wallet nativo aqui.


- Tipos de endereços de entrada e saída permitidos
- Configuração do anunciador para publicação através do nostr (nome, descrição, Uri, entradas mínimas, relé do nostr, chave privada do nostr)


Pode executar o coordenador acessível apenas através do endereço .onion, ou utilizar o seu domínio clearnet personalizado.


Localizar ou criar o ficheiro de configuração neste caminho:


`~/.walletwasabi/coordinator/Config.json`


Edite-o com o comando:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Veja este exemplo Config.json:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Configuração do Tor 🧅


Para preencher a sua OnionServicePrivateKey, é provável que tenha de gerar uma primeiro.


O Wasabi Wallet irá gerar uma chave privada para você se você executá-lo pela primeira vez com ```"PublishAsOnionService": true,``` definido no arquivo Config.json.


Executar o coordenador uma vez com o comando:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Para ver o endereço do serviço oculto Onion, verifique os registos do coordenador com:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


e encontrará algo do género:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


O URL longo que termina em .onion é o seu endereço de serviço oculto ou CoordinatorUri.


Ou verifique novamente o ficheiro de configuração do coordenador com:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Que agora deve ser preenchido automaticamente.


## Corrida ⚡


Depois de definidos todos os parâmetros de configuração, pode executar o serviço coordenador e começar a anunciar a sua primeira ronda 🕶️


Basta iniciar o coordenador com o comando:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Pode monitorizar a ronda atual e o número de UTXO's/coins registados verificando (no browser Tor para .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Opcional: depuração do servidor coordenador


Pode monitorizar quaisquer problemas ou erros no ficheiro de registo em ```~/.walletwasabi/backend/Logs.txt``


Problemas típicos incluem problemas de conexão com o RPC, que deve ser ativado em ```~/.bitcoin/bitcoin.conf`` com:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Opcional: Executar o servidor backend


Juntamente com o coordenador, também pode fornecer um servidor de backend para os utilizadores que não têm o seu próprio nó de bitcoin para se ligarem a estimativas de taxas e filtros de blocos.


Iniciar este serviço com o comando:


```
wbackend
```


## Convidar utilizadores do Wasabi para o seu coordenador 🫂


Para que outros utilizadores encontrem o seu serviço, pode contar com o anunciador nostr ou partilhar uma ligação mágica com o seu domínio (clearnet) ou serviço oculto (ligação .onion) e parâmetros redondos como este:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Quando um utilizador copia a ligação mágica e abre o seu Wasabi Wallet, o software mostra automaticamente a caixa de diálogo do coordenador com o seu domínio e parâmetros.


![detected](assets/en/02.webp)


💚🍣 Parabéns pela descentralização da privacidade do bitcoin 🕶️


Lembra-te do teu treino [wasabika] (https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet é apenas para defesa 🛡️