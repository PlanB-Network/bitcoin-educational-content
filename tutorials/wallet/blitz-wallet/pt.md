---
name: Blitz Wallet
description: A carteira Bitcoin mais simples.
---

![cover](assets/cover.webp)

A experiência do utilizador é um dos fatores decisivos na escolha de uma carteira Bitcoin. Neste tutorial, apresentamos-lhe a Blitz Wallet, uma carteira que coloca a simplicidade no centro da sua abordagem: graças à integração do protocolo **Spark**, a Blitz oferece-lhe uma das carteiras Bitcoin mais simples e completas do mercado, com pagamentos instantâneos e sem gestão técnica.

## O que é a Blitz Wallet?

A Blitz Wallet é uma carteira Bitcoin **self-custodial** e **open source**, que aposta na sua soberania e numa experiência de utilizador fluida e intuitiva.

[Blitz Wallet](https://blitz-wallet.com/) é uma aplicação móvel disponível para Android (Play Store) e iOS (App Store).

Ao contrário das carteiras Lightning tradicionais que exigem a gestão de canais de pagamento e de liquidez de entrada, a Blitz Wallet apoia-se no **protocolo Spark** para eliminar essas complexidades técnicas. Resultado: pagamentos instantâneos desde o primeiro satoshi recebido, sem qualquer configuração prévia. O objetivo da Blitz é tornar os pagamentos em bitcoin tão simples como uma aplicação de pagamento convencional, sem nunca comprometer a self-custody dos seus fundos.

A Blitz Wallet também suporta **endereços legíveis** no formato `utilizador@dominio.com` (via LNURL), o que permite enviar bitcoins tão facilmente como um e-mail, sem ter de manipular longas invoices ou QR codes a cada transação.

## Compreender o protocolo Spark

Antes de passar à prática, é útil compreender a tecnologia que faz funcionar a Blitz Wallet nos bastidores: o **protocolo Spark**.

### O que é o Spark?

O Spark é um protocolo de camada superior open source construído sobre o Bitcoin, desenvolvido pela equipa da Lightspark. Permite efetuar transações instantâneas e de baixo custo, preservando a self-custody dos seus bitcoins.

Ao contrário do Lightning Network, que assenta em **canais de pagamento** entre duas partes, o Spark utiliza uma tecnologia chamada **statechain** (cadeia de estado). O princípio fundamental é o seguinte: em vez de mover os bitcoins na blockchain a cada transação, o Spark transfere o **direito de gasto** de um utilizador para outro, sem movimento on-chain.

### Como funciona?

Para compreender o Spark de forma intuitiva, imaginemos que gastar um bitcoin no Spark requer completar um puzzle de duas peças:
- Uma peça é detida pelo utilizador (por exemplo, Alice).
- A outra peça é detida por um grupo de operadores chamado **Spark Entity (SE)**.

Apenas a combinação das duas peças correspondentes permite gastar os bitcoins.

Quando Alice quer enviar os seus bitcoins a Bob, eis o que acontece: um novo puzzle é criado conjuntamente entre Bob e o SE. O puzzle mantém a mesma forma, mas as peças que o compõem mudam. A partir de agora, é a peça de Bob que corresponde à do SE. A antiga peça de Alice torna-se inutilizável, porque o SE destruiu a sua peça correspondente. A propriedade dos bitcoins mudou de mãos, **sem qualquer transação na blockchain**.

Bob pode então repetir o mesmo processo para enviar esses bitcoins a Carol, e assim por diante. Cada transferência funciona por substituição das peças do puzzle, não por um movimento de fundos on-chain.

### Porque é seguro?

Uma questão legítima coloca-se: o que acontece se o SE não destruir realmente a sua antiga peça?

A Spark Entity não é uma entidade única: é um grupo de operadores independentes. A peça do SE nunca é detida por um único operador. A substituição do puzzle requer a cooperação de vários operadores. Basta que **um único operador seja honesto** durante uma transferência para impedir a reativação de um puzzle antigo. Nenhum operador isolado pode secretamente conservar um puzzle antigo ativo ou recriá-lo posteriormente.

Além disso, o Spark integra um mecanismo de saída unilateral: pode sempre recuperar os seus bitcoins on-chain sem a cooperação do SE. Este mecanismo de segurança faz parte integrante da arquitetura do Spark e garante que nunca está dependente da rede para aceder aos seus fundos.

### Spark vs Lightning Network

O Spark e o Lightning não estão em concorrência: são **complementares**. A Blitz Wallet integra ambos, o que lhe permite beneficiar das vantagens de cada um.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Tecnologia**                | Statechains (cadeias de estado) | Canais de pagamento |
| **Gestão de canais**          | Não necessária               | Necessária            |
| **Liquidez de entrada**       | Não necessária               | Necessária            |
| **Transações instantâneas**   | Sim                          | Sim                   |
| **Self-custody**              | Sim                          | Sim                   |
| **Compatibilidade Lightning** | Sim (via atomic swaps)       | Nativo                |

O Lightning Network continua a ser um excelente protocolo para pagamentos instantâneos, mas impõe restrições técnicas (gestão de canais, liquidez de entrada, nó online...) que podem desencorajar os principiantes. O Spark elimina essas restrições mantendo-se compatível com o Lightning.

## Instalação e configuração

Neste tutorial, baseamo-nos na versão Android da Blitz Wallet, mas todos os processos apresentados abaixo são igualmente válidos no iOS.

![installation](assets/fr/01.webp)

Sendo a Blitz Wallet uma carteira em self-custody, tem a possibilidade de **criar uma nova carteira** ou **importar uma frase de recuperação** (12 ou 24 palavras) de uma carteira existente.

Aqui, optamos pela criação de uma nova carteira. Encontre abaixo as nossas recomendações sobre a cópia de segurança da sua frase de recuperação:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **IMPORTANTE**: Estas 12 ou 24 palavras de recuperação são **a única chave de acesso aos seus bitcoins**. A Blitz é uma carteira self-custodial: nem a Blitz nem o Spark têm acesso à sua frase de recuperação nem aos seus fundos. Se perder estas palavras, perderá definitivamente o acesso aos seus bitcoins. Não as partilhe com ninguém: quem as possuir pode gastar os seus bitcoins.

Em seguida, crie um **código PIN** para proteger o acesso à sua carteira.

![setup-wallet](assets/fr/02.webp)

## Começar a usar a Blitz

Efetuar transações com a Blitz é mais intuitivo do que na maioria das outras carteiras Bitcoin. A interface é minimalista e centrada em três ações principais: enviar, digitalizar e receber.

### Receber bitcoins

Para receber bitcoins na sua carteira Blitz, clique no ícone **"Seta para baixo"** (↓), introduza o montante em satoshis que deseja receber, adicione uma descrição opcional e a carteira gerará uma fatura (invoice) que poderá partilhar com o remetente.

⚠️ **NOTA**: O satoshi (ou "sat") é a menor unidade de bitcoin: **1 bitcoin = 100 000 000 satoshis**.

Uma das particularidades da Blitz Wallet é que suporta várias redes e protocolos do ecossistema Bitcoin:

- **Lightning Network**: Uma das camadas superiores do Bitcoin que permite efetuar micropagamentos instantaneamente com taxas muito baixas. Ideal para pequenos montantes do dia a dia.

- **Bitcoin (on-chain)**: A blockchain principal do protocolo Bitcoin, adequada para transações de montantes mais elevados onde a segurança máxima e a finalidade são prioritárias.

- **Liquid Network**: Uma sidechain (cadeia paralela) do Bitcoin desenvolvida pela Blockstream, que permite transações rápidas e confidenciais utilizando Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Por defeito, a Blitz gera uma fatura Lightning, mas pode escolher a rede na qual deseja receber os seus satoshis clicando no botão **"Choose format"** (Escolher o formato).

![receive-sats](assets/fr/03.webp)

### Criar contactos

A Blitz Wallet simplifica o envio recorrente de bitcoins graças ao seu sistema de contactos.

No menu **Contacts**, pode registar nomes de utilizadores Blitz ou endereços Lightning (LNURL) com os quais interage frequentemente.

Assim, poderá enviar satoshis para esses endereços em poucos cliques, sem ter de digitalizar um QR code ou introduzir manualmente um endereço a cada vez.

### Enviar bitcoins

Além dos métodos clássicos de envio de bitcoin (digitalização de QR code, introdução manual de endereço), a Blitz propõe várias opções práticas:

- **A partir de uma imagem** (*From Image*): Importe um QR code da sua galeria de fotos.
- **A partir da área de transferência** (*From Clipboard*): Cole um endereço ou uma fatura copiada anteriormente.
- **Introdução manual** (*Manual Input*): Introduza diretamente um endereço Bitcoin, uma fatura Lightning ou um endereço legível (por exemplo `utilizador@walletofsatoshi.com`).
- **A partir dos seus contactos**: Selecione um destinatário pré-registado para enviar em poucos cliques.

No menu **Wallet**, clique no botão **"Seta para cima"** (↑), escolha o seu método de envio, introduza o montante a enviar, adicione uma descrição e confirme a transação.

O montante mínimo para efetuar um envio é atualmente de **1 000 satoshis**.

![send-bitcoin](assets/fr/05.webp)

## A loja Blitz

Para além das operações de transferência de bitcoins, a Blitz Wallet integra uma loja na qual pode gastar os seus bitcoins para adquirir serviços digitais diretamente a partir da aplicação.

A partir do menu principal, clique no separador **Store** para aceder à loja. Encontrará também um acesso à plataforma **Bitrefill**, que permite comprar cartões presente junto de milhares de comerciantes em todo o mundo, diretamente em bitcoin.

- **Inteligência artificial**: Aceda aos últimos modelos de IA generativa (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) e pague os seus créditos diretamente em satoshis. Vários planos estão disponíveis conforme as suas necessidades (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **SMS anónimos**: Envie e receba SMS em qualquer parte do mundo sem revelar o seu número de telefone pessoal. O serviço é faturado em satoshis por cada mensagem enviada.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Proteja a sua privacidade online subscrevendo um plano VPN WireGuard (semanal, mensal ou trimestral), pagável em bitcoin diretamente a partir da loja Blitz. Basta descarregar a aplicação cliente WireGuard no seu dispositivo para usufruir do serviço.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet nos bastidores: ir mais longe

Por trás da simplicidade de utilização da Blitz Wallet esconde-se uma arquitetura técnica bem concebida que combina várias camadas do ecossistema Bitcoin.

### A distribuição do seu saldo

A Blitz Wallet gere o seu saldo de forma transparente, distribuindo os seus fundos entre os diferentes protocolos em função das necessidades. Quando o seu saldo é inferior a 500 000 satoshis, a Blitz utiliza o **Liquid Network** e trocas atómicas (*atomic swaps*) para lhe oferecer uma experiência fluida e permitir transações no Lightning Network mesmo com pequenos montantes.

Esta abordagem garante uma utilização simples para os novos utilizadores, sem que necessitem de compreender os mecanismos subjacentes. Pode consultar a distribuição do seu saldo entre as diferentes camadas no menu **Definições > Balance Info**.

![balance](assets/fr/09.webp)

### O modo Lightning (opcional)

Por defeito, a Blitz Wallet utiliza o Liquid Network e o protocolo Spark para lhe oferecer uma experiência fluida sem configuração técnica. No entanto, a Blitz dá-lhe a possibilidade de ativar o **modo Lightning**, que abrirá automaticamente um canal de pagamento quando atingir um saldo de **500 000 satoshis** (0,005 BTC).

Para ativar o modo Lightning, dirija-se às **Definições**, depois na secção **Definições Técnicas**, clique na opção **Node Info**.

![enable-lightning](assets/fr/10.webp)

Graças ao protocolo Spark, esta ativação é **opcional**: o Spark já permite efetuar pagamentos compatíveis com Lightning sem necessidade de abrir um canal nem de gerir liquidez de entrada. O modo Lightning nativo continua a ser útil para utilizadores avançados que desejam dispor do seu próprio nó Lightning integrado na aplicação.

### Ponto de venda (PoS)

A Blitz Wallet integra uma funcionalidade de **ponto de venda** que permite aos comerciantes aceitar pagamentos em bitcoin diretamente a partir da aplicação.

No menu **Definições > Point-of-sale**, pode configurar:

- O identificador único da sua loja
- A moeda fiduciária local na qual exibir os preços
- As instruções para os seus funcionários
- A opção de gorjeta para os seus clientes

Os seus clientes apenas precisam de digitalizar o QR code gerado para efetuar o pagamento em bitcoin, de forma instantânea.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Recursos utilizados para redigir este tutorial:
- Blog da [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
