---
name: Seed Signer

description: Configuração do seu Seed Signer
---

![capa](assets/cover.jpeg)

# Seed Signer

## Material:

1. Raspberry Pi Zero (versão 1.3)

Raspberry Pi Zero

Para uma solução completamente isolada, certifique-se de usar a versão 1.3 sem capacidade WiFi ou Bluetooth, mas qualquer modelo Raspberry Pi 2/3/4 ou Zero funcionará.

Observação: Raspberry Pi geralmente não vem com pinos conectados; os pinos precisarão ser soldados ou algo chamado "GPIO Hammer" pode ser usado.
GPIO Hammer

Se você não tem muita experiência em soldagem ou ainda não possui um ferro de solda, pode usar o "GPIO Hammer" como alternativa à soldagem.

2. Chapéu LCD WaveShare 1,3 polegadas com tela de 240 × 240 pixels

WaveShare LCD Hat

Waveshare 1.3″ 240×240 pxl LCD

Observação: Escolha cuidadosamente a tela Waveshare; certifique-se de comprar o modelo com resolução de 240×240 pixels.
mais informações

3. Módulo de câmera compatível com Pi Zero

Câmera Raspberry Pi

Aokin / AuviPal 5MP 1080p com módulo de câmera de sensor OV5647; outras marcas com o módulo de sensor OV5647 também devem funcionar, mas podem não ser compatíveis com a caixa Orange Pill.

Observação: Você precisará de um cabo de fita de câmera especificamente compatível com o Raspberry Pi Zero.

4. Cartão MicroSD com pelo menos 4 GB de capacidade

recursos extensivos: https://seedsigner.com/explainers/

## Software:

Instalação do Software

1. Baixe o arquivo "seedsigner_x_x_x.img.zip" mais recente
   versão mais recente

2. Descompacte o arquivo "seedsigner_x_x_x.img.zip"

3. Use o Balena Etcher ou uma ferramenta similar para gravar o arquivo de imagem .img descompactado em um cartão microsd
   BALENA ETCHER

4. Instale o cartão microsd no SeedSigner.
   Chave Pública GPG do SeedSigner
   seedsigner_pubkey.gpg

## tutorial em vídeo

_guia retirado de Southerbitcoiner, criado por Cole_

### Uma coleção de guias em vídeo sobre SeedSigner: uma carteira de hardware/DIY de código aberto

![imagem](assets/1.jpeg)

SeedSigner é um dispositivo de assinatura de Bitcoin que você pode construir do zero. Parece difícil, mas esta série de 4 partes deve ajudar você :) Sugiro que você assista à parte 1 e 2 e depois decida se deseja usar um computador (assista à parte 3) ou um dispositivo móvel (assista à parte 4).

Tudo o que você precisa saber estará abaixo. Outros links úteis incluem o site do SeedSigner, o Github deles, o Keybase deles, a versão mais recente e os requisitos de hardware.

### Parte 1: Como construir um SeedSigner:

Neste vídeo, mostro como baixar e verificar o software do SeedSigner, quais peças são necessárias e como montar seu SeedSigner.

![video](https://youtu.be/mGmNKYOXtxY)

### Parte 2: Testando seu SeedSigner

Antes de usar meu SeedSigner, fiz alguns testes para garantir que ele não estava fazendo nada malicioso. Pensei em compartilhar essa etapa também. Aqui está como verificar se o seu SeedSigner exporta a carteira correta (xpub), como verificar os cálculos dos dados do SeedSigner e como verificar as sementes filhas do bip-85 do SeedSigner.

### Parte 3: Como usar o SeedSigner com a carteira Sparrow (desktop)

O SeedSigner é capaz de gerar sementes e assinar transações de bitcoin. Mas, por si só, não é capaz de construir transações. Você precisa usar um "coordenador" de carteira com seu SeedSigner. Veja como usar a carteira Sparrow com seu SeedSigner:

![video](https://youtu.be/IQb8dh-VTOg)

### Parte 4: Como usar o SeedSigner com a carteira Blue (mobile)

O SeedSigner é capaz de gerar sementes e assinar transações de bitcoin. Mas, por si só, não é capaz de criar transações. Você precisa usar um "coordenador" de carteira com seu SeedSigner. Veja como usar a carteira Blue com seu SeedSigner:

![video](https://youtu.be/x0Ee35Ct0r4)

Esses são todos os guias do SeedSigner, por enquanto! Me avise se achar que estou esquecendo algo. Esses estão na minha lista para possíveis vídeos:

> Revisão geral do SeedSigner. É uma boa escolha para um dispositivo de assinatura? Prós/contras?

> Como usar o Bip-85 com o SeedSigner
> Como ser o tio Jim com o SeedSigner

Achou esses vídeos úteis? Considere enviar uma gorjeta para ajudar a financiar futuros vídeos:

https://www.southernbitcoiner.com/donate/
