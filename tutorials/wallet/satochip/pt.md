---
name: Satochip
description: Configurando e utilizando um cartão inteligente Satochip
---
![cover](assets/cover.webp)

Uma carteira de hardware é um dispositivo eletrônico dedicado a gerenciar e proteger as chaves privadas de uma carteira Bitcoin. Diferentemente das carteiras de software (ou carteiras quentes) instaladas em máquinas de propósito geral frequentemente conectadas à Internet, as carteiras de hardware permitem o isolamento físico das chaves privadas, reduzindo os riscos de hacking e roubo.

O principal objetivo de uma carteira de hardware é minimizar as funcionalidades do dispositivo para reduzir sua superfície de ataque. Uma superfície de ataque menor também significa menos vetores de ataque potenciais, ou seja, menos fraquezas no sistema que os atacantes poderiam explorar para acessar os bitcoins.

É recomendado usar uma carteira de hardware para proteger seus bitcoins, especialmente se você possui quantidades significativas, seja em valor absoluto ou como proporção de seus ativos totais.

Carteiras de hardware são usadas em combinação com software de gerenciamento de carteira em um computador ou smartphone. Este software gerencia a criação de transações, mas a assinatura criptográfica necessária para validar essas transações é feita exclusivamente dentro da carteira de hardware. Isso significa que as chaves privadas nunca são expostas a um ambiente potencialmente vulnerável.

Carteiras de hardware oferecem dupla proteção para o usuário: por um lado, elas protegem seus bitcoins contra ataques remotos mantendo as chaves privadas offline, e por outro lado, geralmente oferecem melhor resistência física contra tentativas de extrair as chaves. E é precisamente nesses 2 critérios de segurança que se pode julgar e classificar os diferentes modelos disponíveis no mercado.

Neste tutorial, proponho descobrir uma dessas soluções: o Satochip.

## Introdução ao Satochip

O Satochip é uma carteira de hardware na forma de um cartão com um chip certificado *EAL6+*, que é um padrão de segurança muito alto (*NXP JCOP*). É produzido por uma empresa belga.

![SATOCHIP](assets/notext/01.webp)

Este cartão inteligente é vendido por €25, o que é muito acessível comparado a outras carteiras de hardware no mercado. O chip é um elemento seguro que garante muito boa resistência contra ataques físicos. Além disso, seu código é de código aberto (*AGPLv3*).
No entanto, devido ao seu formato, o Satochip não oferece tantas opções quanto outras carteiras de hardware. Obviamente, não há bateria, câmera, nem leitor de cartão micro SD, pois é um cartão. Sua maior desvantagem, na minha opinião, é a falta de uma tela na carteira de hardware, o que a torna mais vulnerável a certos tipos de ataques remotos. De fato, isso força o usuário a assinar às cegas e a confiar no que vê na tela do seu computador.

Apesar de suas limitações, o Satochip permanece interessante devido ao seu preço reduzido. Esta carteira pode notavelmente ser usada para aumentar a segurança de uma carteira de gastos além de uma carteira de poupança protegida por uma carteira de hardware equipada com tela. Também constitui uma boa solução para aqueles que possuem pequenas quantidades de bitcoins e não desejam investir cem euros em um dispositivo mais sofisticado. Além disso, o uso de Satochips em configurações multisig, ou potencialmente em sistemas de carteira com timelock no futuro, pode oferecer vantagens interessantes.

A empresa Satochip também oferece 2 outros produtos. Há o Satodime, que é um cartão portador projetado para armazenar bitcoins offline, mas não permite transações. É uma espécie de carteira de papel que é muito mais segura, que pode ser usada, por exemplo, para fazer um presente. Finalmente, há o Seedkeeper, que é um gerenciador de frase mnemônica. Pode ser usado para salvar nossa semente de forma segura sem que ela seja diretamente anotada em um pedaço de papel.

## Como comprar um Satochip?
O Satochip está disponível para venda [no site oficial](https://satochip.io/product/satochip/). Para comprá-lo em uma loja física, você também pode encontrar [a lista de revendedores certificados](https://satochip.io/resellers/) no site do Satochip.
Para interagir com o seu software de gestão de carteira, o Satochip oferece duas possibilidades: através da comunicação NFC ou via um leitor de cartão inteligente. Para a opção NFC, certifique-se de que sua máquina é compatível com esta tecnologia ou adquira um leitor NFC externo. O Satochip opera na frequência padrão de 13,56 MHz. Caso contrário, você também pode comprar um leitor de cartão inteligente. Você pode encontrar um no site do Satochip ou em outro lugar.

![SATOCHIP](assets/notext/02.webp)

## Como configurar um Satochip com Sparrow?

Uma vez que você tenha recebido seu Satochip, o primeiro passo é examinar a embalagem para garantir que ela não foi aberta. A embalagem do Satochip deve incluir um adesivo de selagem. Se este adesivo estiver faltando ou danificado, isso pode indicar que o cartão inteligente foi comprometido e pode não ser autêntico.
![SATOCHIP](assets/notext/03.webp)
Você encontrará o Satochip dentro.

![SATOCHIP](assets/notext/04.webp)

Para gerenciar a carteira, neste tutorial, sugiro usar o Sparrow. Se você ainda não tem o software, [visite o site oficial para baixá-lo](https://sparrowwallet.com/download/). Você também pode conferir nosso tutorial sobre Sparrow Wallet (em breve).

![SATOCHIP](assets/notext/05.webp)

Insira seu Satochip no leitor de cartão inteligente ou coloque-o sobre o leitor NFC, e conecte o leitor ao seu computador no qual o Sparrow está aberto.

![SATOCHIP](assets/notext/06.webp)

Abra o Sparrow Wallet e certifique-se de que você está devidamente conectado a um nó Bitcoin. Para fazer isso, verifique o sinal no canto inferior direito: ele deve estar amarelo se você estiver conectado a um nó público, verde para uma conexão com o Bitcoin Core, ou azul para o Electrum.

![SATOCHIP](assets/notext/07.webp)

No Sparrow Wallet, clique na aba "*File*".

![SATOCHIP](assets/notext/08.webp)

Em seguida, no menu "*New Wallet*".

![SATOCHIP](assets/notext/09.webp)

Escolha um nome para sua carteira e então clique em "*Create Wallet*".

![SATOCHIP](assets/notext/10.webp)

Clique no botão "*Connected Hardware Wallet*".

![SATOCHIP](assets/notext/11.webp)

Clique no botão "*Scan...*".

![SATOCHIP](assets/notext/12.webp)

Seu Satochip deve aparecer. Clique em "*Import Keystore*".

![SATOCHIP](assets/notext/13.webp)

Em seguida, você precisa configurar um código PIN para desbloquear seu Satochip. Escolha uma senha forte, entre 4 e 16 caracteres. Faça um backup desta senha.

Esteja ciente, esta senha não é uma passphrase. Isso significa que, mesmo sem esta senha, sua frase mnemônica permitirá que você reimporte sua carteira para o software, se necessário. A senha é usada apenas para garantir o acesso ao próprio Satochip. É equivalente ao código PIN encontrado em outras carteiras de hardware.

Uma vez que a senha for inserida, clique novamente no botão "*Import Keystore*".

![SATOCHIP](assets/notext/14.webp)

Anote a senha novamente, depois clique no botão "*Initialize*".
![SATOCHIP](assets/notext/15.webp)
Você então chega à janela para gerar sua frase mnemônica. Clique no botão "*Gerar Nova*".

![SATOCHIP](assets/notext/16.webp)
Faça uma ou mais cópias físicas da sua frase de recuperação, escrevendo-a em um papel ou meio metálico. Esteja ciente de que esta frase concede acesso total aos seus bitcoins sem qualquer proteção adicional. Portanto, se alguém a descobrir, poderá roubar instantaneamente seus bitcoins, mesmo sem acesso ao seu Satochip ou ao seu código PIN. É, portanto, importante proteger esses backups. Além disso, esta frase permite que você recupere o acesso aos seus bitcoins em caso de perda, dano ao Satochip ou se você esquecer seu código PIN.
![SATOCHIP](assets/notext/17.webp)

Sua carteira de Bitcoin foi criada com sucesso.

![SATOCHIP](assets/notext/18.webp)

Clique novamente no botão "*Importar Keystore*".

![SATOCHIP](assets/notext/19.webp)

Sua carteira está agora criada. Suas chaves privadas estão agora armazenadas no cartão inteligente do seu Satochip. Clique no botão "*Aplicar*" para continuar.

![SATOCHIP](assets/notext/20.webp)

É recomendado configurar uma senha adicional para proteger as informações públicas gerenciadas pelo Sparrow Wallet, além do código PIN do seu Satochip. Esta senha garantirá a segurança do acesso ao Sparrow Wallet, ajudando a proteger suas chaves públicas, endereços e histórico de transações contra qualquer acesso não autorizado.

![SATOCHIP](assets/notext/21.webp)

Digite sua senha nos dois campos e, em seguida, clique no botão "*Definir Senha*".

![SATOCHIP](assets/notext/22.webp)

E pronto, seu Satochip agora está configurado no Sparrow Wallet.

![SATOCHIP](assets/notext/23.webp)

Agora que sua carteira está criada, você pode desconectar seu Satochip. Guarde-o em um local seguro!

## Como receber bitcoins com o Satochip?

Uma vez na sua carteira, clique na aba "*Receber*".

![SATOCHIP](assets/notext/24.webp)

O Sparrow Wallet gera um endereço para sua carteira. Geralmente, para outras carteiras de hardware, é aconselhado clicar em "*Exibir Endereço*" para verificar o endereço diretamente na tela do dispositivo. Infelizmente, esta opção não está disponível com o Satochip, mas certifique-se de usá-la para suas outras carteiras.

![SATOCHIP](assets/notext/25.webp)

Você pode adicionar um "*Rótulo*" para descrever a fonte dos bitcoins que serão protegidos com este endereço. Esta é uma boa prática que ajuda a gerenciar melhor seus UTXOs.

![SATOCHIP](assets/notext/26.webp)

Para mais informações sobre rotulagem, também recomendo conferir este outro tutorial:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Você pode então usar este endereço para receber bitcoins.

![SATOCHIP](assets/notext/27.webp)
## Como Enviar Bitcoins com Satochip?
Agora que você recebeu seus primeiros sats em sua carteira segura com Satochip, você também pode gastá-los! Conecte seu Satochip ao seu computador, inicie o Sparrow Wallet e, em seguida, vá para a aba "*Enviar*" para construir uma nova transação.

![SATOCHIP](assets/notext/28.webp)
Se você deseja realizar o controle de moedas, ou seja, escolher especificamente quais UTXOs consumir na transação, vá para a aba "*UTXOs*". Selecione os UTXOs que deseja gastar e clique em "*Enviar Selecionados*". Você será redirecionado para a mesma tela da aba "*Enviar*", mas com seus UTXOs já selecionados para a transação.
![SATOCHIP](assets/notext/29.webp)

Insira o endereço de destino. Você também pode inserir múltiplos endereços clicando no botão "*+ Adicionar*".

![SATOCHIP](assets/notext/30.webp)

Note um "*Rótulo*" para lembrar o propósito deste gasto.

![SATOCHIP](assets/notext/31.webp)

Escolha a quantidade enviada para este endereço.

![SATOCHIP](assets/notext/32.webp)

Ajuste a taxa de comissão da sua transação de acordo com o mercado atual.

![SATOCHIP](assets/notext/33.webp)

Certifique-se de que todos os parâmetros da sua transação estão corretos, então clique em "*Criar Transação*".

![SATOCHIP](assets/notext/34.webp)

Se tudo estiver ao seu contento, clique em "*Finalizar Transação para Assinatura*".

![SATOCHIP](assets/notext/35.webp)

Clique em "*Assinar*".

![SATOCHIP](assets/notext/36.webp)

Clique novamente em "*Assinar*" ao lado do seu Satochip.

![SATOCHIP](assets/notext/37.webp)

Digite o código PIN do seu Satochip, então clique em "*Assinar*" novamente para assinar sua transação.

![SATOCHIP](assets/notext/38.webp)

Sua transação está agora assinada. Clique em "*Transmitir Transação*" para divulgá-la na rede Bitcoin.

![SATOCHIP](assets/notext/39.webp)

Você pode encontrá-la na aba "*Transações*" do Sparrow Wallet.

![SATOCHIP](assets/notext/40.webp)

Parabéns, você agora tem conhecimento sobre como usar o Satochip! Se você achou este tutorial útil, eu apreciaria um joinha abaixo. Sinta-se livre para compartilhar este artigo em suas redes sociais. Muito obrigado!