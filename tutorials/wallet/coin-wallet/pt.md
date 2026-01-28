---
name: Coin Wallet
description: Tutorial sobre Coin Wallet e formas de melhorar a privacidade e a segurança
---

![cover](assets/cover.webp)


Este tutorial aborda o [Coin Wallet](https://coin.space/) - um wallet criptográfico auto-custodial para dispositivos móveis, e como aumentar a segurança e a privacidade ao utilizar aplicações móveis wallet.



## Sobre o Coin Wallet


*o *Coin Wallet** é um wallet de código aberto, autocustodial / não-custodial, criado por uma equipa de entusiastas do Bitcoin em 2015. Começou como uma aplicação Web, seguida da aplicação iOS em 2017 e da aplicação Android em 2020 - disponível no Google Play, Samsung Galaxy Store e Huawei AppGallery.


Principais vantagens:


- Arquitetura sem custódia
- Totalmente [código-fonte aberto](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Design simples e limpo
- Centrado no objetivo principal - armazenar criptomoedas de forma segura, sem funcionalidades desnecessárias
- Suporte multiplataforma: telemóvel (iOS e Android), computador de secretária, Web
- Suporte RBF (Replace-By-Fee) - acelere as transacções bloqueadas em qualquer altura
- Hardware 2FA com [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / chave FIDO2
- Suporte Tor integrado - encaminhe todo o tráfego através da rede Tor para obter o máximo de privacidade



## 1️⃣ Instalação do Coin Wallet

Coin Wallet está disponível em todas as principais plataformas.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Todas as ligações de lançamento](https://github.com/CoinSpace/CoinSpace/releases)


Também disponível para ambiente de trabalho (Windows, Linux, macOS), como uma aplicação Web e através do Tor.


![image](assets/en/01.webp)


## 2️⃣ Criar um Wallet e definir o PIN


Um wallet é criado utilizando um passphrase - uma sequência aleatória de 12 palavras separadas por espaços, gerada a partir de uma [lista de 2048 palavras](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin O Wallet suporta frases-passe de 12, 15, 18, 21 ou 24 palavras importadas de outras carteiras.


O passphrase é a forma legível por humanos da chave mestra privada. Deve ser guardada de forma segura. O passphrase é tudo o que é necessário para aceder ou restaurar o wallet. Se o passphrase for perdido, o wallet e todos os fundos são perdidos permanentemente. O passphrase nunca deve ser partilhado. O Coin Wallet não armazena chaves em nenhum servidor ou base de dados.


**Um passphrase de 12 palavras é seguro?

Com 2048 palavras possíveis por posição, existem 2048¹² ≈ 10³⁹ combinações - fornecendo ~128 bits de segurança, comparáveis às chaves privadas Bitcoin. Este nível é amplamente considerado suficiente.


![image](assets/en/02.webp)


Depois de o passphrase ser escrito e confirmado, a aplicação pede para definir um **PIN de 4 dígitos** para acesso quotidiano. Para maior comodidade, pode ativar a autenticação biométrica (impressão digital ou reconhecimento facial) em vez de utilizar um PIN.


![image](assets/en/03.webp)



Não há conta, recuperação de chaves, reinicialização do passphrase nem reversão de transacções. A segurança é da inteira responsabilidade do utilizador.


Para melhores práticas detalhadas sobre como guardar a frase mnemónica:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Senha + PIN. Quando e como são utilizados


**Quando é que o passphrase é necessário?

Só nestes casos raros:


- Configurar o wallet num novo dispositivo
- Reinstalar a aplicação Coin Wallet
- Limpar os dados da aplicação/navegador (Armazenamento local)
- Remoção de uma chave de hardware da conta
- Introduzir o PIN errado três vezes (a aplicação bloqueia por segurança)


Na utilização quotidiana, o PIN de 4 dígitos é suficiente para desbloquear o wallet.


**Passphrase + PIN: como funciona**

A passphrase é a verdadeira chave mestra privada e funciona em qualquer dispositivo.

Uma vez que digitar 12-24 palavras de cada vez seria inconveniente, o Coin Wallet utiliza um PIN de 4 dígitos para um acesso rápido e quotidiano no dispositivo atual.

Um simples PIN, por si só, não é suficientemente seguro para proteger diretamente a chave mestra, pelo que nunca é utilizado para encriptação. Em vez disso:



- O PIN é enviado para o servidor e trocado por um longo token criptográfico.
- Este token desencripta a chave mestra encriptada armazenada apenas no dispositivo.


Se o PIN for introduzido incorretamente três vezes, o servidor elimina permanentemente o token. A chave armazenada localmente torna-se inutilizável e a única forma de recuperar o wallet é introduzindo o passphrase original.

Esta conceção proporciona comodidade e uma forte proteção de recurso.



## 4️⃣ Receber ₿itcoin - Tipos de Address e privacidade


Coin Wallet suporta os três formatos de endereço Bitcoin:



- SegWit nativo (Bech32)** - começa com **bc1q** - taxas mais baixas, recomendado
- SegWit (P2SH)** aninhado - começa com **3**
- Legado (P2PKH)** - começa com **1**


![image](assets/en/04.webp)


**Porque é que o endereço muda após cada depósito?

Este facto é intencional e protege a privacidade. Sempre que são recebidas moedas, o Coin Wallet gera automaticamente um novo endereço não utilizado. Se o mesmo endereço fosse reutilizado (por exemplo, para o salário mensal), qualquer pessoa poderia facilmente somar todas as transacções recebidas num explorador de cadeias de blocos e saber o rendimento total.


Os endereços antigos permanecem válidos para sempre - pode continuar a receber para eles - mas a utilização de um novo endereço de cada vez é a melhor prática recomendada em termos de privacidade.


**Como receber o Bitcoin:**

1. Abrir a moeda

2. Toque em **Receber**

3. Escolher o tipo de endereço pretendido (de preferência **bc1q** - `Native SegWit`)

4. Mostrar o código QR ou copiar o endereço e enviá-lo ao pagador


**Opcional - Mecto (para pagamentos presenciais):**

No mesmo ecrã Receber, existe um botão `Mecto`.

Quando o liga:


- Ser-lhe-á pedido que introduza um **nickname** (gravatar)
- A sua localização atual + endereço de receção são temporariamente partilhados com outros utilizadores do Coin Wallet que também tenham o Mecto ativado
- Podem descobri-lo num pequeno mapa e enviar moedas sem ter de digitar ou digitalizar


Os dados são visíveis apenas para outros utilizadores do Mecto e são automaticamente eliminados após 1 hora (ou imediatamente quando o desligar).

O Mecto é totalmente opcional - deixe-o desligado se preferir o máximo de privacidade.


![image](assets/en/05.webp)


## 5️⃣ Envio de ₿itcoin


Para enviar o Bitcoin:


1. Abrir a moeda → tocar em **Enviar**

2. Colar o endereço ou ler o código QR

3. Introduzir o montante (ou tocar em **Max**)

4. Escolha a velocidade da transação:



| Velocidade   | Tempo de confirmação aproximado | Nível de taxa     |
|---------|---------------------------|---------------|
| **Lento**    | ~120 minutos              | Mais baixo
| **Padrão** | ~60 minutos               | Médio
| **Rápido**    | ~20 minutos               | Mais alto

5. Confirme com o seu PIN de 4 dígitos → a transação é transmitida


### Como acelerar uma transação pendente de ₿itcoin (RBF)


Se escolher uma taxa lenta e a transação ficar bloqueada:


1. Ir para o separador **Histórico**

2. Toque na transação pendente

3. Torneira **Accelerate** (Substituição mediante taxa)

4. Confirmar → a transação será retransmitida com uma taxa mais elevada


A aceleração RBF é atualmente suportada para:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Mais informações sobre o Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Exportação de chaves privadas


**Quando é que é realmente necessária uma chave privada?

(99 % dos utilizadores nunca o fazem - as 12 palavras passphrase são suficientes)



| Situação                                      | Por que você precisa da chave privada                     |
|------------------------------------------------|--------------------------------------------------|
| Limpeza de uma carteira de papel antiga                   | Para mover fundos para sua carteira atual             |
| Importar para um assinante de hardware (por exemplo, Coldcard) | Para assinatura offline                              |
| Recuperação de emergência (sementes perdidas, mas o aplicativo ainda está aberto) | Para salvar moedas antes do aplicativo desaparecer           |
| Usando ferramentas que não aceitam frases de sementes     | Alguns utilitários apenas de monitoramento ou assinatura             |

### Como exportar chaves privadas no Coin Wallet


1. Aberto **Bitcoin (BTC)**

2. Desloque-se para o fundo da página - toque em **Exportar chaves privadas**

3. A aplicação mostra todos os endereços com saldo + a sua chave privada no formato **WIF** (começa por 5, K ou L) e um código QR.


Só aparecem os endereços não vazios.


**Exemplo de chave WIF

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**O que fazer a seguir (recomendado)**


- Abrir o Electrum, Sparrow, BlueWallet ou qualquer hardware wallet
- Importar/aproveitar chave privada
- Todos os fundos são transferidos instantaneamente para um novo endereço seguro no seu atual seed


Nunca guarde a chave privada digitalmente em texto simples. Depois de varrida, pode ser eliminada em segurança.


Para obter um guia completo sobre chaves privadas e caminhos de derivação: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Detalhes técnicos - BIP39, BIP32 e percursos de derivação


A Coin Wallet segue rigorosamente as normas oficiais da Bitcoin que são utilizadas por quase todas as carteiras sérias.


`BIP39` - como o passphrase se torna a chave mestra privada


- Número de palavras por defeito: 12
- Opcional passphrase/palavra-passe: nenhuma ("")
- Entropia inicial: 128 bits (12 palavras) → 256 bits (24 palavras)
- Implementação de código aberto: https://github.com/paulmillr/scure-bip39
- Lista de palavras: lista de 2048 palavras em inglês padrão
- Suporta a importação de frases de 12, 15, 18, 21 e 24 palavras de qualquer outro BIP39 wallet


`BIP32 + BIP44/BIP49/BIP84` - geração determinística de todos os endereços

A partir de uma chave mestra, o wallet pode generate biliões de endereços numa ordem estritamente definida. É por isso que as mesmas 12 palavras introduzidas no Electrum, Sparrow, Trezor, Ledger, BlueWallet, etc. mostrarão exatamente os mesmos endereços e saldos.





**Caminhos de derivação usados em Coin Wallet para Bitcoin**

| Tipo de endereço              | Padrão | Caminho de derivação       | Começa com | Comentário                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| SegWit Nativo (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Formato moderno, taxas mais baixas           |
| SegWit Aninhado (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Wrapper de compatibilidade para serviços antigos |
| Herdado (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Formato mais antigo, taxas mais altas          |

Dentro de cada caminho:


- `/0` - cadeia externa (endereços que indica para receber pagamentos)
- `/1` - cadeia interna (alterar endereços que o próprio wallet usa)


Uma vez que o Coin Wallet segue estas normas públicas sem quaisquer alterações, os seus fundos continuarão a ser recuperáveis em qualquer outro wallet compatível, mesmo daqui a 10-20-30 anos.


## 8️⃣ Melhorar o anonimato com o Tor


**Porquê usar o Tor em Coin Wallet

O Tor esconde o seu verdadeiro endereço IP dos nós, trocas e observadores do Bitcoin.

Todo o tráfego (saldos, transacções, trocas) passa pela rede Tor - sem ligações diretas, sem fugas de IP.

Isto é implementado diretamente no código fonte da aplicação (ver [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


O Coin Wallet tem um endereço .onion oculto e, desde a v6.6.3 (dezembro de 2024), **suporte Tor integrado diretamente na aplicação móvel**.


### Como ativar o Tor no Android e iOS


1. **Instalar o Orbot** - aplicação oficial do Projeto Tor (gratuita)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Abrir o Orbot → tocar em Iniciar**

Selecione **Coin Wallet** na lista para que apenas o wallet utilize o Tor (opcional mas recomendado)

Aguarde até que seja indicado **"Ligado "** (10-30 segundos)


3. **Abrir Coin Wallet → Definições → Rede**

Ativar **Utilizar o Tor**


4. **Verificar o estado

Um **ícone Tor onion roxo** aparece na barra superior → todo o tráfego é agora encaminhado através do Tor


![image](assets/en/06.webp)


E pronto - o seu telemóvel Coin Wallet está totalmente anónimo.


Desfrute da gestão privada de criptomoedas!


## 📝 Conclusão


[Coin Wallet](https://coin.space/) - um dos verdadeiros pioneiros do Bitcoin wallet com uma história de desenvolvimento de 10 anos.

É deliberadamente simples e mantém-se concentrado na sua missão principal: armazenar de forma segura a sua moeda criptográfica.

Não há publicidade, nem feed de notícias, nem subscrições, nem funcionalidades sociais, nem distracções - apenas um wallet limpo, rápido e auto-custodial que faz exatamente o que é suposto fazer.

Coin O Wallet coloca a simplicidade e a segurança em primeiro lugar - sempre o fez e sempre o fará.


## 📖 Recursos


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39