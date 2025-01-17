---
name: LNP2PBot
description: Guia completo sobre o LNP2PBot e o comércio de bitcoin P2P
---
![cover](assets/cover.webp)

## Introdução

As trocas peer-to-peer (P2P) sem KYC são essenciais para preservar a confidencialidade e a autonomia financeira dos utilizadores. Permitem transacções diretas entre indivíduos sem necessidade de verificação de identidade, o que é crucial para quem valoriza a privacidade. Para uma compreensão mais aprofundada dos conceitos teóricos, consulte o curso BTC204:

https://planb.network/courses/btc204
A compra e venda de bitcoin peer-to-peer (P2P) é um dos métodos mais privados de aquisição ou alienação de bitcoins. O LNP2PBot é um bot de Telegrama de código aberto que facilita as trocas P2P na rede Lightning, permitindo transacções rápidas, de baixo custo e sem KYC.

### Por que usar o Lnp2pbot?


- Não é necessário KYC
- Transacções rápidas na Lightning Network
- Custos reduzidos
- Interface simples através do Telegram, uma popular aplicação de mensagens acessível a partir de qualquer parte do mundo
- Sistema de reputação integrado
- Caução automática para uma negociação segura
- Suporte a várias moedas
- Comunidade ativa e em crescimento

### Pré-requisitos

Para usar o Lnp2pbot, você precisará de :

1. Carteira Lightning Network (recomenda-se a Breez, Phoenix ou Blixt)

2. Aplicação Telegram instalada (https://telegram.org/)

3. Uma conta Telegram com um nome de utilizador definido

## Instalação e configuração

### 1. Configurar a sua carteira Lightning

Comece por instalar uma carteira Lightning compatível. Aqui estão as nossas recomendações detalhadas:

**Carteiras recomendadas


- [Breez](https://breez.technology)**:
  - Excelente para principiantes
  - Interface intuitiva e moderna
  - Sem custódia (mantém o controlo dos seus fundos)
  - Perfeitamente compatível com o Lnp2pbot
  - Disponível em iOS e Android

Abaixo está o link para o tutorial desta carteira:

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Fénix](https://phoenix.acinq.co)** :
  - Simples e fiável
  - Configuração automática de canais
  - Suporte nativo para facturas BOLT11
  - Excelente para transacções diárias
  - Disponível em iOS e Android

Abaixo está o link para o tutorial desta carteira:

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io)** :
  - Mais técnico, mas muito completo
  - Opções de configuração avançadas
  - Perfeito para utilizadores experientes
  - Código aberto
  - Disponível no Android

Abaixo está o link para o tutorial desta carteira:

https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f
**Notas importantes sobre outras carteiras

⚠️ **Importante**: Antes de vender sats, certifique-se de que a sua carteira suporta facturas "hold", que são utilizadas pelo bot como um sistema de caução.


- Carteira de Satoshi**: Funciona bem para receber sats, mas pode ter atrasos na atualização do saldo se uma venda for cancelada.
- Não**: Não recomendado porque os pagamentos podem falhar devido aos limites da taxa de encaminhamento do bot (máximo de 0,2%).
- Aqua**: Funciona para receber sats, mas pode ter grandes atrasos (até 48 horas) nas actualizações do saldo em caso de cancelamento de uma venda.

💡 **Dica**: Para uma experiência óptima, opte pelas carteiras recomendadas (Breez, Phoenix ou Blixt).

⚠️ **Importante**: Não se esqueça de guardar as suas frases de recuperação num local seguro.

### 2. Como começar a usar o Lnp2pbot

1. Clique neste link para aceder ao bot: [@lnp2pBot](https://t.me/lnp2pbot)

2. O telegrama abre-se automaticamente

3. Clique em "Iniciar" ou envie o comando "/start"

4. O bot pedir-lhe-á para criar um nome de utilizador se ainda não tiver um

5. O bot guiá-lo-á através da configuração inicial

### 3. Juntar-se à comunidade


- Junta-te ao canal principal: [@p2plightning](https://t.me/p2plightning)
- Suporte: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)

## Comprar e vender Bitcoins

Há duas maneiras principais de trocar bitcoins no Lnp2pbot:

1. Procurar e responder a ofertas existentes no mercado

2. Criar a sua própria oferta de compra ou venda

Neste guia, veremos em pormenor como :


- Comprar bitcoins a partir de uma oferta existente
- Vender bitcoins criando a sua própria oferta

### Como comprar Bitcoins

**1. Procurar e selecionar uma oferta**

![Sélection d'une offre de vente](assets/fr/01.webp)

Navegue pelas ofertas em [@p2plightning] (https://t.me/p2plightning) e clique no botão "Comprar satoshis" por baixo do anúncio que lhe interessa.

**2. Validar a oferta e o montante**

![Validation de l'offre](assets/fr/02.webp)

1. Regressar ao chat de bots

2. Confirmar a sua escolha de oferta

3. Introduza o montante em moeda fiduciária que pretende comprar

4. O bot pedir-lhe-á que forneça uma fatura Lightning com o montante em satoshis

**3. Contactar o vendedor**

![Mise en relation](assets/fr/03.webp)

Após o envio da fatura, o bot coloca-o em contacto com o vendedor.

**4. Comunicação com o vendedor**

![Chat privé](assets/fr/04.webp)

Clique no nickname do vendedor para abrir um canal de conversação privado onde pode trocar detalhes de pagamento em moeda fiduciária.

**5. Confirmação do pagamento

![Confirmation du paiement](assets/fr/05.webp)

Depois de fazer o pagamento em moeda fiduciária, use o comando `/fiatsent` no chat do bot. Quando a transação estiver concluída, poderá avaliar o vendedor e a transação será fechada.

### Como vender Bitcoins

**1. Criar uma oferta de venda**

![Création d'une offre de vente](assets/fr/06.webp)

Para criar uma oferta de venda, basta utilizar o comando :

`/vender`

O bot guiá-lo-á passo a passo:

1. Escolha a sua moeda

2. Indicar a quantidade de satoshis a vender

3. Quanto ao preço, tem duas opções:


   - Definir um preço fixo para a quantidade de satoshis
   - Utilizar o preço de mercado com a possibilidade de aplicar um prémio (positivo ou negativo)

💡 **Dica**: O prémio permite-lhe ajustar o seu preço em relação ao preço de mercado. Por exemplo, um prémio de -1% significa que está a vender por menos 1% do que o preço de mercado.

**2. Confirmação da criação da encomenda**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Uma vez criada a encomenda, verá uma confirmação com a opção de cancelar a encomenda utilizando o comando `/cancel`.

**3. Gerir as vendas**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- Quando um comprador responde à sua oferta, recebe uma notificação com um código QR e uma fatura para pagar.
- Verificar o perfil e a reputação do comprador.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Clique no nickname do comprador para abrir um canal de discussão privado.
- Comunicar os dados de pagamento fiduciário ao comprador.
- Aguardar a confirmação do pagamento em moeda fiduciária por parte do comprador.
- Verificar se o pagamento foi recebido na sua conta.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Confirmar a transação com `/release` e concluir a encomenda. Terá a oportunidade de avaliar o comprador.

## Boas práticas e segurança

### Conselhos de segurança


- Comece com pequenas quantidades
- Verificar sempre a reputação dos utilizadores
- Utilizar apenas os métodos de pagamento sugeridos
- Manter todas as comunicações no chat do bot
- Nunca partilhar informações sensíveis

### Sistema de reputação


- Cada utilizador tem uma pontuação de reputação
- As transacções bem sucedidas aumentam a sua pontuação
- Escolher utilizadores com boa reputação
- Comunicar qualquer comportamento suspeito aos moderadores

### Resolução de litígios

1. Quando surgirem problemas, mantenha-se calmo e profissional

2. Utilize o comando `/dispute` para abrir um ticket

3. Fornecer todas as provas necessárias

4. Esperar por um moderador

## Comparação com outras soluções

O Lnp2pbot tem várias vantagens e desvantagens em relação a outras soluções de troca P2P, como Peach, Bisq, HodlHodl e Robosat:

### Vantagens do Lnp2pbot


- Não é necessário KYC** : Ao contrário de algumas plataformas, a Lnp2pbot não requer verificação de identidade, preservando assim a confidencialidade do utilizador.
- Transacções rápidas**: Graças à rede Lightning, as transacções são quase instantâneas.
- Taxas baixas** : Os custos de transação são inferiores aos das bolsas tradicionais.
- Disponibilidade móvel**: O LNP2PBot está acessível através do Telegram, o que facilita a sua utilização em dispositivos móveis.
- Fácil de usar** : A interface intuitiva do Lnp2pbot torna-o fácil de usar, mesmo para utilizadores menos experientes.

### Desvantagens do Lnp2pbot


- Dependência do Telegram**: O uso do Lnp2pbot requer uma conta no Telegram, que pode não ser adequada para todos os utilizadores.
- Menos liquidez**: Em comparação com plataformas mais estabelecidas como a Bisq, a liquidez pode ser mais limitada.

Em comparação, soluções como a Bisq oferecem maior liquidez e uma interface de desktop, mas podem envolver taxas mais elevadas e tempos de transação mais longos. A HodlHodl e a Robosat, por sua vez, também oferecem negociação sem KYC, mas com estruturas de taxas e interfaces diferentes.

## Recursos úteis


- Sítio Web oficial: https://lnp2pbot.com/
- Documentação: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Suporte: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)