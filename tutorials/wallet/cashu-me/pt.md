---
name: Cashu.me
description: Guia Cashu.me para utilizar o ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Aqui está um tutorial em vídeo da BTC Sessions, um guia em vídeo que o orienta sobre como configurar e utilizar o Cashu.me Bitcoin Wallet, que lhe dá acesso a transacções Bitcoin simples, baratas e privadas - sem necessidade de uma loja de aplicações!*


Neste tutorial, vamos explorar o Cashu.me, um Wallet baseado em navegador para pagamentos privados de Bitcoin usando Chaumian ecash. Antes de mergulharmos, vamos fazer uma breve introdução sobre o ecash e como ele funciona.


## Introdução ao ecash


Imagine ter dinheiro digital que funciona exatamente como as notas físicas no seu bolso - privado, instantâneo e utilizável peer-to-peer sem intermediários. É isso que o ecash permite: uma abordagem de pagamento digital que traz de volta a privacidade do dinheiro físico para o mundo digital. Ao contrário do onchain-Bitcoin, que regista todas as transacções num Ledger público visível para qualquer pessoa, o ecash cria tokens privados que representam o valor real do Bitcoin, mantendo os seus hábitos de consumo confidenciais.


Pense no ecash como um instrumento digital ao portador armazenado no seu dispositivo - se o tiver, é seu, tal como o dinheiro físico. Estes tokens são emitidos por serviços de confiança chamados `Mints` que detêm as reservas Bitcoin subjacentes. Quando utiliza o ecash, não está a transmitir as suas transacções a toda a rede. Em vez disso, está a trocar tokens privados diretamente com outros, criando uma experiência de pagamento que se assemelha mais a entregar dinheiro a alguém do que a fazer um pagamento digital tradicional.


Cashu é um protocolo Chaumian ecash livre e de código aberto construído para Bitcoin. A tecnologia baseia-se na pesquisa criptográfica pioneira de David Chaum nos anos 80, usando "assinaturas cegas" para garantir a privacidade. Quando recebe tokens ecash, a casa da moeda assina-os sem saber onde serão gastos a seguir - uma caraterística crucial que impede o rastreio da transação. É importante salientar que o ecash não substitui o Bitcoin, mas complementa-o, resolvendo algumas questões críticas que surgem com os requisitos de arquitetura do Bitcoin. Oferece a privacidade que o dinheiro físico oferece (que o Ledger transparente do Bitcoin não tem) e permite microtransacções instantâneas sem taxas Blockchain ou atrasos de confirmação.


O ecash integra-se perfeitamente com o Lightning Network. Usa o Lightning para depositar Bitcoin numa casa da moeda (convertendo o seu valor de Bitcoin em tokens ecash) e para levantar mais tarde (convertendo os tokens de volta em saldo Lightning utilizável). Juntos, eles formam uma combinação poderosa: O Bitcoin fornece a liquidação segura Layer, o Lightning permite transacções rápidas e a interoperabilidade da rede e o ecash adiciona a privacidade Layer que faz com que os pagamentos digitais voltem a ser verdadeiramente privados.


## Cashu.me


Cashu.me é um `Progressive Web App (PWA)` que implementa o protocolo Cashu - uma implementação específica do ecash Chaumian projetado para Bitcoin. Como um PWA, ele funciona diretamente no seu navegador sem precisar de instalação em lojas de aplicativos, embora você possa `instalá-lo` no seu dispositivo para facilitar o acesso. Esta abordagem baseada na Web garante uma ampla compatibilidade entre sistemas operativos, mantendo a segurança através de protocolos criptográficos em vez de restrições de plataforma.


## 🎉 Caraterísticas principais


Vamos mergulhar nas funcionalidades e explorar o que o Cashu.me tem para oferecer:



- Chaumian ecash no Lightning**: Utiliza assinaturas cegas para que as casas da moeda não consigam rastrear os saldos dos utilizadores ou os históricos de transacções
- Auto-custódia de fichas**: Controla os tokens ecash localmente com a sua frase seed
- Backups de frases seed**: frase de recuperação de 12 palavras para restauração do Wallet
- Independência das casas da moeda**: Funciona com várias casas da moeda independentes - não está preso a um único fornecedor
- Transacções instantâneas e gratuitas**: Dentro da mesma casa da moeda, os pagamentos são finalizados em segundos com zero taxas
- Arquitetura de preservação da privacidade**: As casas da moeda não podem ver quem transacciona com quem
- Ecash offline**: Enviar/receber fichas através de um protocolo de transmissão local, como NFC, código QR, Bluetooth, etc., sem ligação à Internet
- Descubra as casas da moeda ecash através do Nostr**: Encontre e verifique as casas da moeda de confiança através do protocolo Nostr
- Troque ecash entre casas da moeda**: Todas as casas da moeda falam Lightning, o que significa que pode transferir valor entre elas.
- Controle remotamente o seu Wallet com o Nostr Wallet Connect (NWC)**: Conecte-se a outros aplicativos como o Nostr Client e comece a fazer zapping via NWC


A troca crítica é `confiança`: enquanto você controla os tokens em si, você deve confiar nas casas da moeda para custodiar as reservas subjacentes de Bitcoin. Como diz a documentação da Cashu:


> ...a casa da moeda está a gerir a infraestrutura Lightning e guarda os satoshis para os utilizadores de ecash da casa da moeda. Os utilizadores têm de confiar na casa da moeda para Redeem o seu ecash quando quiserem mudar para Lightning.

- Documentação Cashu, [Questões gerais de segurança e privacidade](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Isto faz do ecash uma solução de custódia para o próprio Bitcoin, embora o utilizador mantenha o controlo total dos tokens.


## 1️⃣ Configuração inicial


① Comece por visitar [Wallet.cashu.me](https://Wallet.cashu.me) no seu navegador. Como o Cashu.me é um `PWA`, você não precisa baixá-lo das lojas de aplicativos, basta abrir o site diretamente no seu navegador. Para um acesso mais fácil, pode opcionalmente instalá-lo no ecrã inicial do seu dispositivo.


② Para instalar o PWA, toque no botão de menu ⋮ no seu navegador e selecione `Adicionar à tela inicial`. Depois de instalado, feche o separador do navegador e inicie o Cashu.me a partir do ecrã inicial do seu dispositivo. No ecrã de boas-vindas, toque em `Próximo` para continuar.


③ A segurança é fundamental. Guarde a sua frase seed de forma segura num gestor de palavras-passe ou, melhor ainda, escreva-a num papel. Esta frase de recuperação de 12 palavras é a única forma de recuperar fundos se perder o acesso a este dispositivo. Toque no ícone 👁️ para revelar a sua frase seed, escreva cuidadosamente todas as 12 palavras por ordem e, em seguida, assinale a caixa `Eu escrevi-a`. Toque em `Next` para continuar e marque a caixa para confirmar que aceita os `termos` no ecrã seguinte.


![image](assets/en/01.webp)


Depois de completar a configuração, você precisará conectar-se a um `Mint`. Toque em `ADD MINT` seguido de `DISCOVER MINTS` para ver as moedas recomendadas pela comunidade Nostr. Para uma verificação adicional, pode rever as classificações das casas da moeda em [bitcoinmints.com](bitcoinmints.com).


Em seguida, toque em `Clique para navegar pelas balas` para ver a lista completa. Selecione uma hortelã copiando o seu URL, colando-o no campo URL e dando-lhe um nome reconhecível. Para este exemplo, vamos utilizar:


URL: `https://mint.minibits.cash/Bitcoin`

Nome: `Minibits`


![image](assets/en/02.webp)


Toque em `ADD MINT` para completar o processo. No ecrã de confirmação, verifique se confia no operador deste mint e depois toque em `ADD MINT` novamente. O Minibits mint aparecerá agora no seu ecrã inicial. Assim que o Wallet estiver configurado, é necessário carregá-lo antes de efetuar transacções.


![image](assets/en/03.webp)


## 2️⃣ Financiamento do seu Wallet


O Cashu.me oferece dois métodos distintos para financiar o seu Wallet. Quando tocar em `Receber` no ecrã inicial, verá opções para receber fundos via `ECASH` ou via `LIGHTNING`.


![image](assets/en/04.webp)


### Financiamento via LIGHTNING


A primeira opção é financiar o Wallet através do Lightning Invoice. selecione uma casa da moeda se tiver adicionado diferentes casas da moeda e defina o montante (Sats) que pretende receber. Em seguida, toque em `CRIAR Invoice`. Agora você recebe um QR-Code que pode ser digitalizado com outro Wallet relâmpago ou pode simplesmente `Copiar` o Invoice e colar em outro Wallet para pagar e financiar seu cashu.me Wallet.


![image](assets/en/05.webp)


### Receber dinheiro eletrónico


O método ecash permite-lhe receber fichas diretamente de outro ecash Wallet. Comece por tocar no botão `Receber` e selecione a opção `ECASH`. Poderá `Colar`, `Digitalizar` ou utilizar `NFC` para enviar um token Cashu de outro Wallet. Se optar por colar, introduza a cadeia de caracteres token que copiou de outro Wallet, o `Mont` e a `Mint` serão automaticamente apresentados. Toque em `RECEBER` para completar a transação e o Sats aparecerá no seu Wallet. Repare que o seu saldo está agora distribuído por várias moedas. Por exemplo, você pode ter 1.000 Sats na sua "Casa da Moeda" Minibits e mais 1.000 Sats na "Casa da Moeda" Coinos. Esta separação entre diferentes moedas é um aspeto importante da arquitetura da Cashu.


![image](assets/en/06.webp)


### Troca de balas


Se você não confia mais em uma determinada moeda que você adicionou, cashu.me oferece um recurso para `Swap` fundos de uma moeda para outra. Navegue até a aba das casas da moeda e role para baixo até ver `Multimint Swaps`. Selecione a casa da moeda `DESDE` e `PARA` nos menus suspensos e introduza o montante que pretende transferir. Toque em `SWAP` para mover os tokens entre as casas da moeda. Isso será executado por meio da transação Lightning, portanto, você precisa deixar espaço para possíveis taxas do Lightning. No meu exemplo, 1 sat foi suficiente.


![image](assets/en/07.webp)


## 3️⃣ Envio de fundos


Para enviar Sats, o Cashu.me oferece duas opções. Enviar via `ecash` ou via `lightning`. Vamos dar uma olhada nas duas opções.


### Envio via Lightning


Para enviar através do Lightning, siga estes passos:


1. Toque em `ENVIAR` no ecrã inicial e selecione `Raios`

2. A aplicação pedir-lhe-á que introduza um `Lightning Invoice` ou `-Address`. Pode colar o Invoice/Address diretamente ou utilizar a opção de leitura do código QR para o capturar visualmente e, em seguida, confirmar com `ENTER`

3. Selecione a Casa da Moeda a partir da qual pretende efetuar o pagamento utilizando o campo de lista pendente e toque em `PAGAR` para confirmar. **Nota**: existe também uma opção para utilizar o `Multinut` em `Configurações` -> `Experimental` que lhe permite pagar facturas de várias casas da moeda ao mesmo tempo.

4. Após a conclusão bem sucedida, verá a confirmação do pagamento e o montante deduzido do seu saldo.


![image](assets/en/08.webp)


### Envio via ecash


O envio de ecash é igualmente simples.


1. Toque em "ENVIAR" e, desta vez, selecione a opção "DINHEIRO".

2. selecione uma casa da moeda e introduza o `Montante` que pretende enviar em Sats e toque em `ENVIAR` para confirmar

3. Isto cria um `Código QR animado` que pode personalizar ajustando os parâmetros Velocidade e Tamanho. Qualquer pessoa pode digitalizar este Código QR para o Redeem do Sats imediatamente, ou pode tocar em COPIAR para enviar a cadeia token para outra pessoa através de canais alternativos como Bluetooth, NFC ou mensagens padrão.

4. Estou a abrir outro Wallet. Colo da área de transferência e selecciono `Receive ecash` no outro Wallet.


![image](assets/en/09.webp)


## 4️⃣ Caraterísticas adicionais


Para além da funcionalidade central de envio e receção, o Cashu.me oferece poderosas funcionalidades adicionais que melhoram a sua experiência Bitcoin dentro do ecossistema Nostr.


### Ligação Nostr Wallet


O Nostr Wallet Connect (`NWC`) transforma a forma como interage com as aplicações Nostr, criando uma ligação perfeita entre o seu Wallet e as aplicações sociais. Este protocolo permite que aplicações como [Damus](https://damus.io/) ou [Primal](https://primal.net/home) solicitem pagamentos diretamente através dos relés Nostr sem que seja necessário sair da aplicação.


Para configurar o `NWC` no Cashu.me:


1. Aceder a `Configurações` no menu superior esquerdo do Hambúrguer

2. Desloque-se para a secção `NOSTR Wallet CONNECT` e toque no botão `Enable`

3. Em seguida, definirá um subsídio para estabelecer o montante máximo que as aplicações podem gastar do seu Wallet.

4. Uma vez configurado, você pode copiar a string de conexão e colá-la em qualquer cliente Nostr que suporte `NWC`, permitindo a funcionalidade instantânea de zapping e tipping.


![image](assets/en/10.webp)


### Relâmpago Address via npub.cash


Cashu.me integra-se com [npub.cash] (https://npub.cash/) para lhe fornecer um Lightning Address que funciona perfeitamente com o protocolo Nostr. Aqui pode registar-se e reclamar o seu nome de utilizador fornecendo o seu Nostr `nsec`, que custa 5.000 Sats e apoia o projeto npub.cash, ou pode usar qualquer chave pública Nostr (`npub`) sem registo.


Primeiro, vá para `Configurações` e toque em `Ativar` Relâmpago Address com npub.cash. Isto irá criar um generate npub.cash Address utilizando uma cadeia `npub` derivada da sua frase Wallet seed por defeito.


Em alternativa, visite [esta página Web] (https://npub.cash/username) para obter um nome de utilizador personalizado utilizando o seu próprio Nostr `nsec`, o que lhe dará um Lightning Address personalizado como username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Conclusão


Cashu.me oferece pagamentos privados Bitcoin que funcionam como dinheiro físico - instantaneamente e ponto a ponto sem expor o seu histórico de transacções. Pessoalmente, aprecio a sua arquitetura PWA porque funciona sem restrições da loja de aplicações. Ao combinar a segurança do Bitcoin, a velocidade do Lightning e a privacidade do ecash, o Wallet oferece casos de utilização que podem aumentar a adoção quotidiana do Bitcoin.


Embora tenha controlo total sobre os seus tokens ecash através da auto-custódia, lembre-se que as casas da moeda actuam como terceiros de confiança que detêm as reservas Bitcoin subjacentes. A capacidade de usar várias casas da moeda e trocar entre elas proporciona flexibilidade, mantendo a privacidade.


Graças a funcionalidades como os endereços NWC e npub.cash, o Cashu.me é uma opção Wallet apelativa para clientes sociais que valorizam a privacidade e a soberania em detrimento das restrições das políticas das grandes tecnologias.


## 📚 Recursos


[https://github.com/cashubtc/cashu.me] (https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc] (https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu] (https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/] (https://cashu.space/)