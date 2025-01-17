---
name: Trezor model One
description: Configuração e uso do Trezor modelo One
---

![capa](assets/cover.webp)

Portfólio de hardware frio - 60€ - Iniciante - Seguro entre 2 000€ e 50 000€.

Como carteira física fria, o Trezor é ideal para começar no Bitcoin. É fácil de usar, não é muito caro e funcional.

Já fizemos tutoriais sobre como usá-lo:

1. Configurando
2. Recuperando bitcoins
3. Usando, enviando e recebendo bitcoins

Você gostaria de ter o seu próprio Trezor também?
Você pode contribuir para o projeto clicando abaixo!

configuração - https://www.youtube.com/watch?v=q-BlT6R4_bE

recuperação: https://www.youtube.com/watch?v=3n4d4egjiFM

uso: https://www.youtube.com/watch?v=syouZjLC1zY

## guia de escrita

guia proposto por https://armantheparman.com/trezor/

## Configurando o Trezor

O Trezor vem com seu próprio cabo micro USB. Certifique-se de usar esse cabo e não apenas qualquer cabo velho que estiver por aí. Alguns cabos USB são apenas de energia. Este transmite dados E energia. Se você usar o dispositivo com um cabo USB de carregamento de telefone, o dispositivo pode falhar ao se conectar.

Conecte-o ao seu computador e o dispositivo será ligado. Você receberá uma mensagem que diz "Vá para Trezor.io/start". Faça isso e baixe o Trezor Suite para o seu computador.

![imagem](assets/0.webp)

Clique no botão de download ("Obter aplicativo para desktop")

![imagem](assets/1.webp)

Observe os links de Assinatura e Chave de Assinatura. Para verificar o download (verificar se o download não foi adulterado), existem etapas adicionais que são opcionais se você estiver começando, mas OBRIGATÓRIAS se você tiver uma riqueza significativa para proteger. As instruções para isso estão no Apêndice A (final do guia).

Conecte o Trezor ao computador com o cabo micro USB e instale e execute o programa. Veja como ele se parece em um Mac:

![imagem](assets/2.webp)

Você receberá um aviso bobo após executar o programa, apenas continue:

![imagem](assets/3.webp)

Clique em Configurar Trezor

![imagem](assets/4.webp)

Se o firmware estiver desatualizado, permita que o Trezor atualize o firmware.

Em seguida, você pode criar uma nova semente ou restaurar uma carteira de um dispositivo diferente com uma semente que você já possui. Vou passar pela criação de uma nova semente.

![imagem](assets/5.webp)

Clique em "Criar nova carteira" - e confirme que deseja fazer isso no próprio dispositivo clicando no botão de confirmação.

Em seguida, clique na única opção "Backup de semente padrão"

![imagem](assets/6.webp)

Em seguida, clique em "criar backup"

![imagem](assets/7.webp)

Clique nas três marcas de seleção para deixá-las verdes (é claro, leia cada mensagem) e, em seguida, clique em "começar backup".

![imagem](assets/8.webp)

Em seguida, você verá isso:

![imagem](assets/9.webp)

No dispositivo, veja as palavras apresentadas a você uma por uma e anote-as DE FORMA ORGANIZADA e NA ORDEM.

![imagem](assets/10.webp)

Defina um PIN para bloquear o dispositivo (isso não faz parte da sua semente, é apenas para bloquear o dispositivo para que ninguém possa acessar a semente contida nele).

![imagem](assets/11.webp)

Você tem opções para adicionar shitcoins à sua carteira - eu peço que você não faça isso e salve apenas em Bitcoin, como eu explico aqui (por que bitcoin) e aqui (por que apenas bitcoin).

![image](assets/12.webp)

Nomeie sua carteira e clique em "Acessar Suite":

![image](assets/13.webp)

É mais simples criar uma carteira sem frase de acesso, mas é melhor criar uma com uma frase de acesso (sua carteira real) E uma sem frase de acesso (sua carteira falsa). Cada vez que você acessar o dispositivo através do Trezor Suite, será perguntado se você deseja "aplicar" a frase de acesso ou não.

![image](assets/14.webp)

Eu selecionei "Carteira Oculta" e digitei uma frase de acesso que inventei "craigwrightisaliarandafraud"

![image](assets/15.webp)

Gosto de como é chamada de "carteira oculta", pois explica parcialmente como as frases de acesso funcionam.

Confirme a frase de acesso no dispositivo.

Como esta carteira está vazia, fui solicitado a confirmar se a frase de acesso está correta:

![image](assets/16.webp)

Em seguida, você será perguntado se deseja habilitar a rotulagem. Não é algo que eu tenha explorado, mas parece ser uma maneira de rotular suas transações e salvar os dados em seu computador ou nuvem.

![image](assets/17.webp)

Finalmente, sua carteira estará disponível:

![image](assets/18.webp)

O que você tem em seu computador é o que chamamos de "carteira de observação", porque possui suas chaves públicas (e endereços), mas não suas chaves privadas. Você precisa das chaves privadas para gastar (assinando transações com as chaves privadas). A maneira de fazer isso é conectando a carteira de hardware. O objetivo da carteira de hardware é que as transações possam ser enviadas de volta e para frente entre o computador e o Trezor, uma assinatura possa ser aplicada dentro do Trezor e a chave privada sempre permaneça contida dentro do dispositivo (para segurança contra malware de computador).

O Trezor Suite é uma carteira de observação ruim por várias razões. É bom para o mínimo necessário, mas se você quiser avançar, continue lendo e aprenda como conectar o dispositivo à Sparrow Bitcoin Wallet.

## Carteira de Observação

Em artigos anteriores, expliquei como baixar e verificar a Sparrow Bitcoin Wallet e como conectá-la ao seu próprio nó ou a um nó público. Você pode seguir estes guias:

- Instalar o Bitcoin Core
- Instalar a Sparrow Bitcoin Wallet
- Conectar a Sparrow Bitcoin Wallet ao Bitcoin Core

Uma alternativa ao uso da Sparrow Bitcoin Wallet é a Electrum Desktop Wallet, mas vou prosseguir explicando a Sparrow Bitcoin Wallet, pois considero que seja a melhor para a maioria das pessoas. Usuários avançados podem preferir usar o Electrum como alternativa (veja meu guia).

Agora vamos carregá-la no Sparrow e conectar o Trezor (com a frase de recuperação, mas agora com uma frase de acesso). Esta carteira nunca foi exposta ao Trezor Suite porque será criada DEPOIS de conectarmos o dispositivo ao Trezor Suite. Certifique-se de nunca mais conectá-lo ao Trezor Suite para não expor sua nova carteira. (Você pode conectá-lo sem frase de acesso, pois essa pode ser sua carteira falsa).

Crie uma Nova Carteira:

![image](assets/19.webp)

Dê um nome bonito para ela

![image](assets/20.webp)

Clique em "Carteira de Hardware Conectada".

![image](assets/21.webp)

![image](assets/22.webp)

Clique em "Digitalizar" e depois em "definir frase de acesso" na próxima tela para criar uma nova carteira (use uma nova frase de acesso, por exemplo, a antiga frase de acesso com um número depois funcionaria). Em seguida, "envie a frase de acesso" e confirme-a no dispositivo.

'![image](assets/23.webp)

Em seguida, clique em "importar keystore".

Não há nada para editar na próxima tela, o Trezor preencheu para você. Clique em "Aplicar".

![image](assets/24.webp)

A próxima tela permite que você adicione uma senha. Não confunda isso com "frase de acesso"; muitas pessoas confundem. A nomenclatura é infeliz. A senha permite que você bloqueie esta carteira em seu computador. É específica para este software neste computador. Não faz parte da sua chave privada do Bitcoin.

Clique em "Aplicar".

![image](assets/25.webp)

Após uma pausa, enquanto o computador pensa, você verá os botões à esquerda mudarem de cinza para azul. Parabéns, sua carteira está pronta para uso. Faça transações e envie-as à vontade.

![image](assets/26.webp)

Recebendo

Para receber alguns bitcoins, vá para a guia "Endereços" à esquerda e escolha um dos endereços para receber. Clique com o botão direito no endereço desejado e selecione "copiar endereço". Em seguida, vá para sua exchange de onde o dinheiro está sendo enviado e cole-o lá. Ou você pode fornecer o endereço a um cliente que possa usá-lo para pagar você.

Quando você usa a carteira pela primeira vez, você deve receber uma quantia muito pequena, praticar gastando-a para outro endereço, seja dentro da carteira ou de volta para a exchange, para provar que a carteira está funcionando conforme o esperado.

Depois de fazer isso, você deve fazer backup das palavras que você anotou. Uma única cópia não é suficiente. Tenha pelo menos duas cópias em papel (metal é melhor) e mantenha-as em dois locais diferentes e bem seguros. Isso reduz o risco de um desastre natural destruir sua HWW e o backup em papel em um único incidente. Consulte "Usando Carteiras de Hardware Bitcoin" para uma discussão completa sobre isso.

## Enviando

![image](assets/27.webp)

Ao fazer um pagamento, você precisa colar o endereço para o qual está pagando no campo "Pagar para". Na verdade, você não pode deixar o campo "Rótulo" em branco, é apenas para os registros de suas próprias carteiras, mas o Sparrow não permite isso - apenas insira algo (apenas você verá). Insira o valor e você também pode ajustar manualmente a taxa desejada.

A carteira não pode assinar a transação a menos que a HWW esteja conectada. Essa é a função da HWW - receber a transação, assiná-la e devolvê-la, assinada. Certifique-se de que, ao assinar no dispositivo, você inspecione visualmente o endereço para o qual está pagando, que é o mesmo no dispositivo e na tela do computador, e a fatura que você recebe (por exemplo, você pode ter recebido um e-mail para pagar um determinado endereço).

Também preste atenção que, se você escolher usar uma moeda que seja maior que o valor do pagamento, o restante será enviado de volta para um dos endereços de troco de suas carteiras. Algumas pessoas não sabiam disso e procuraram sua transação em uma blockchain pública e pensaram que alguns bitcoins foram enviados para o endereço de um atacante, mas na verdade era o próprio endereço de troco deles.
Firmware

Para atualizar o firmware, você precisa se conectar ao Trezor Suite. Se você quiser fazer isso, certifique-se de ter suas palavras de backup e frase de acesso disponíveis para restaurar o dispositivo, caso o dispositivo seja redefinido.
Conclusão

Este artigo mostrou como usar um Trezor HWW de maneira mais segura e privada do que o anunciado - mas este artigo sozinho não é suficiente. Como eu disse no início, você deve combiná-lo com as informações fornecidas em "Usando Carteiras de Hardware Bitcoin".
Apêndice A - Verificar o download do software

## Apêndice A - Verificar o download do software

![image](assets/28 .webp)

Baixe a Assinatura (um arquivo de texto) e a Chave de Assinatura (um arquivo de texto) e anote os nomes dos arquivos e onde você os baixou.
Em seguida, para Mac, você precisará baixar o GPG Suite (Veja as instruções aqui).

Para Windows, você precisará do GPG4win (Veja as instruções aqui).

Para Linux, o GPG já faz parte de todos os pacotes. Caso você não o tenha, obtenha-o com o comando: sudo apt-get install gpg

Em seguida, para Mac/Windows ou Linux, abra o terminal e digite o comando:

```bash
gpg –import XXXXXXXXXX
```

onde XXXXXXXXXX é o caminho completo para o arquivo da chave de assinatura (caminho completo significa o diretório e o nome do arquivo onde o arquivo está). Você deverá ver uma confirmação de importação bem-sucedida da chave.

Então

```bash
gpg –verify ZZZZZZZZZZ WWWWWWWWWW
```

onde ZZZZZZZZZZ é o caminho completo para o arquivo de assinatura e WWWWWWWWWW é o caminho completo para o programa Trezor Suite que você baixou.

Você deverá ver uma mensagem "Boa assinatura de SatoshiLabs" em algum lugar da saída. Há um aviso na parte inferior que é seguro ignorar.
