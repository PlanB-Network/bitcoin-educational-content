---
name: Trezor Modelo Um
description: Configuração e utilização do Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Crédito da imagem: [Trezor.io](https://trezor.io/)*



O Trezor Model One é o primeiro Hardware Wallet de sempre, lançado em 2014 pela SatoshiLabs. Após mais de dez anos de existência, continua a ser uma escolha interessante, particularmente para os utilizadores que procuram um Hardware Wallet que seja acessível tanto tecnicamente como em termos de orçamento. De facto, o seu preço é de 49 euros no site oficial da Trezor. É uma das únicas carteiras de hardware nesta gama de preços. Situa-se a meio caminho entre os dispositivos de entrada de gama a cerca de 20 euros, como o Tapsigner, que muitas vezes não têm ecrã, e os dispositivos de gama média a cerca de 80 euros, como o Ledger Nano S Plus ou o Trezor Safe 3.



O Model One possui um ecrã OLED monocromático de 0,96 polegadas e dois botões físicos. Funciona sem bateria, utilizando apenas uma ligação micro-USB para alimentação e dados Exchange.



![Image](assets/fr/01.webp)



A principal desvantagem do Model One é a falta de um elemento seguro, o que o torna vulnerável a uma variedade de ataques físicos, alguns dos quais são relativamente simples de executar. Estes ataques podem incluir a análise de canais auxiliares para determinar o PIN do dispositivo, ou técnicas mais avançadas para extrair o seed encriptado, a fim de o forçar posteriormente. Note-se que estes ataques requerem acesso físico ao dispositivo. No entanto, esta vulnerabilidade pode ser consideravelmente reduzida através da utilização de um passphrase BIP39 sólido. Se optar por este Hardware Wallet, aconselho-o vivamente a configurar um passphrase.



O Model One oferece duas vantagens importantes:




- Baseia-se numa arquitetura totalmente de código aberto. Ao contrário dos modelos mais recentes com Secure Element, todos os componentes de hardware e software do Model One são auditáveis;
- Está equipado com um ecrã. Tanto quanto sei, este é o único Hardware Wallet no mercado nesta gama de preços com um ecrã. Trata-se de uma caraterística muito importante, pois permite verificar as informações assinadas e os endereços de receção, evitando assim muitos ataques digitais.



O Trezor Model One pode, por conseguinte, representar uma escolha sensata para principiantes e utilizadores intermédios com um orçamento limitado. No entanto, é importante ter em conta as suas limitações em termos de proteção física, devido à ausência do Secure Element. Se o seu orçamento for limitado, esta é uma boa opção, mas se puder optar por um modelo superior, como o Trezor Safe 3 a 79 euros, é preferível, uma vez que inclui um elemento seguro.



## Desembalar o Trezor Model One



Quando receber o seu Model One, certifique-se de que a caixa e o Seal estão intactos para confirmar que a embalagem não foi aberta. Uma verificação de software da autenticidade e integridade do dispositivo será também efectuada aquando da sua configuração posterior.



O conteúdo da caixa inclui :




- O Trezor Model One;
- Cartolina para gravar a sua frase Mnemonic, autocolantes e instruções;
- Cabo USB-A para micro-USB.



![Image](assets/fr/02.webp)



A navegação no dispositivo é muito simples:




- Clique com o botão direito do rato para confirmar e avançar para os passos seguintes;
- Utilize o botão esquerdo para voltar atrás.



## Pré-requisitos



Neste tutorial, vou mostrar-lhe como utilizar o Trezor Model One com o [software de gestão de carteiras Sparrow Wallet] (https://sparrowwallet.com/download/). Se ainda não instalou este software, faça-o agora. Se precisar de ajuda, também temos um tutorial detalhado sobre a configuração do Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Também é necessário o software Trezor Suite para configurar o Model One, verificar a sua autenticidade e instalar o firmware. Só utilizaremos este software para esse efeito e, posteriormente, só será necessário para actualizações de firmware. Para a gestão diária do Wallet, utilizaremos exclusivamente o Sparrow Wallet, uma vez que está optimizado para o Bitcoin e é fácil de utilizar, mesmo para principiantes (o Sparrow apenas suporta o Bitcoin, não altcoins).



[Descarregar o Trezor Suite a partir do sítio Web oficial] (https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Para ambos os programas, recomendo vivamente que verifique a sua autenticidade (com o GnuPG) e a sua integridade (através do Hash) antes de os instalar na sua máquina. Se não sabe como fazer isso, pode seguir este outro tutorial :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Iniciar o Trezor Model One



Ligue o Model One ao seu computador onde o Trezor Suite e o Sparrow Wallet já estão instalados.



![Image](assets/fr/04.webp)



Abra o Trezor Suite e, em seguida, clique em "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Selecione "*Bitcoin-only firmware*" e, em seguida, clique em "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



O Trezor Suite instalará então o firmware no seu Model One. Aguarde durante a instalação.



![Image](assets/fr/07.webp)



Clique em "*Continuar*".



![Image](assets/fr/08.webp)



## Criar uma carteira Bitcoin



No Trezor Suite, clique no botão "*Create new Wallet*" (Criar novo Wallet).



![Image](assets/fr/09.webp)



Aceitar os termos de utilização do Hardware Wallet.



![Image](assets/fr/10.webp)



No Trezor Suite, clique em "*Continue to backup*".



![Image](assets/fr/11.webp)



O software fornece instruções sobre como gerir a sua frase Mnemonic.



Este Mnemonic dá-lhe acesso total e sem restrições a todos os seus bitcoins. Qualquer pessoa na posse desta frase pode roubar os seus fundos, mesmo sem acesso físico ao seu Trezor Model One.



A frase de 24 palavras restaura o acesso aos seus bitcoins em caso de perda, roubo ou quebra do seu Hardware Wallet. Por conseguinte, é muito importante guardá-la cuidadosamente e guardá-la num local seguro.



Pode gravá-lo no cartão fornecido na caixa ou, para maior segurança, recomendo que o grave numa base de aço inoxidável para o proteger de incêndios, inundações ou desmoronamentos.



Confirme as instruções e, em seguida, clique no botão "*Criar cópia de segurança do Wallet*".



![Image](assets/fr/12.webp)



O Model One criará a sua frase Mnemonic utilizando o seu gerador de números aleatórios. Certifique-se de que não está a ser observado durante esta operação. Escreva as palavras fornecidas no ecrã no suporte físico da sua escolha. Dependendo da sua estratégia de segurança, pode considerar fazer várias cópias físicas completas da frase (mas, acima de tudo, não a divida). É importante manter as palavras numeradas e em ordem sequencial.



***Obviamente, nunca deve partilhar estas palavras na Internet, como eu faço neste tutorial. Este exemplo Wallet será utilizado apenas no Testnet e será apagado no final do tutorial



Para mais informações sobre a forma correta de guardar e gerir a tua frase Mnemonic, recomendo vivamente que sigas este outro tutorial, especialmente se fores um principiante:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Para passar para as palavras seguintes, clique com o botão direito do rato. Quando tiver escrito todas as palavras, clique novamente no botão direito para passar ao passo seguinte.



![Image](assets/fr/13.webp)



O seu Hardware Wallet mostra-lhe novamente todas as suas palavras. Verifique se as escreveu todas.



![Image](assets/fr/14.webp)



## Definir o código PIN



Segue-se o passo do código PIN. O código PIN desbloqueia o Trezor. Por conseguinte, oferece proteção contra o acesso físico não autorizado. Este código PIN não está envolvido na derivação das chaves criptográficas do seu Wallet. Assim, mesmo sem acesso ao código PIN, a posse da sua frase de 12 palavras Mnemonic permitir-lhe-á recuperar o acesso aos seus bitcoins.



No Trezor Suite, clique em "*Continue to PIN*" e, em seguida, no botão "*Set PIN*".



![Image](assets/fr/15.webp)



Confirmar no Modelo Um.



![Image](assets/fr/16.webp)



Recomendamos que escolha um código PIN que seja o mais aleatório possível. Certifique-se de que guarda este código num local separado do local onde o Trezor está guardado (por exemplo, num gestor de palavras-passe). Pode definir um código PIN entre 8 e 50 dígitos. Recomendo que escolha um código PIN tão longo quanto possível para aumentar a segurança.



O código PIN deve ser introduzido no Trezor Suite no seu computador, clicando nos pontos correspondentes aos dígitos, de acordo com a configuração do teclado apresentada no Trezor Model One.



Este método específico de introdução do PIN é necessário sempre que desbloqueia o Trezor Model One, quer seja através do Trezor Suite ou do Sparrow Wallet.



![Image](assets/fr/17.webp)



Uma vez terminado, clique no botão "*Enter PIN*".



![Image](assets/fr/18.webp)



Escreva novamente o seu PIN para confirmar.



![Image](assets/fr/19.webp)



No Trezor Suite, clique no botão "*Complete setup*".



![Image](assets/fr/20.webp)



A configuração do seu Model One está agora concluída. Se desejar, pode alterar o nome e a página inicial do seu Hardware Wallet.



![Image](assets/fr/21.webp)



O software Trezor Suite já não é necessário, exceto para atualizar regularmente o firmware do Hardware Wallet ou para efetuar um teste de recuperação. Vamos agora utilizar o Sparrow para gerir a carteira, uma vez que este software é perfeitamente adequado para uma utilização exclusiva do Bitcoin.



## Configurar o portefólio no Sparrow Wallet



Comece por descarregar e instalar o Sparrow Wallet [a partir do site oficial] (https://sparrowwallet.com/) no seu computador, caso ainda não o tenha feito.



Depois de abrir o Sparrow Wallet, certifique-se de que o software está ligado a um nó Bitcoin, o que é indicado pelo visto no canto inferior direito do Interface. Se estiver a ter problemas em ligar o Sparrow, recomendo que consulte o início deste tutorial:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Clique no separador "*File*" (Ficheiro) e, em seguida, em "*New Wallet*" (Novo Wallet).



![Image](assets/fr/22.webp)



Dê um nome à sua carteira e, em seguida, clique em "*Criar Wallet*".



![Image](assets/fr/23.webp)



No menu pendente "*Script Type*", selecione o tipo de script que será utilizado para proteger os seus bitcoins. Eu recomendo "*Taproot*" ou, se não for possível, "*Native SegWit*".



![Image](assets/fr/24.webp)



Clique no botão "*Connected Hardware Wallet*". O seu Model One deve, naturalmente, estar ligado ao computador.



![Image](assets/fr/25.webp)



Clique no botão "*Scan*". O seu Model One deve aparecer.



Quando ligar o seu Model One a um computador com o Sparrow Wallet aberto, ser-lhe-á pedido que introduza um passphrase BIP39 no Sparrow. Esta opção avançada será abordada num futuro tutorial. Por agora, pode simplesmente selecionar "*Toggle passphrase Off*" para evitar que o Trezor lhe peça para introduzir um passphrase sempre que arrancar.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Clique em "*Importar Keystore*".



![Image](assets/fr/27.webp)



Agora pode ver os detalhes do seu Wallet, incluindo a chave pública alargada da sua primeira conta. Clique no botão "*Apply*" (Aplicar) para finalizar a criação do Wallet.



![Image](assets/fr/28.webp)



Escolha uma senha forte para proteger o acesso ao Sparrow Wallet. Esta palavra-passe garantirá o acesso seguro aos seus dados Sparrow Wallet, protegendo as suas chaves públicas, endereços, etiquetas e histórico de transacções contra o acesso não autorizado.



Aconselho-o a guardar esta palavra-passe num gestor de palavras-passe para não se esquecer dela.



![Image](assets/fr/29.webp)



E agora a sua carteira foi importada para o Sparrow Wallet!



![Image](assets/fr/30.webp)



Antes de receberes as tuas primeiras bitcoins no teu Wallet, **aconselho-te vivamente a fazeres um teste de recuperação vazio**. Anote algumas informações de referência, como o seu xpub, depois reinicie o seu Trezor Model One enquanto o Wallet ainda está vazio. Em seguida, tente restaurar o seu Wallet no Trezor utilizando as suas cópias de segurança em papel. Verifique se o xpub gerado após o restauro corresponde ao que escreveu originalmente. Se corresponder, pode ter a certeza de que as suas cópias de segurança em papel são fiáveis.



Para saber mais sobre como efetuar um teste de recuperação, sugiro que consulte este outro tutorial:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Como receber bitcoins com o Trezor Model One?



No Sparrow, clique no separador "*Receber*".



![Image](assets/fr/31.webp)



Antes de utilizar o Address proposto pelo Sparrow Wallet, verifique-o no ecrã do seu Trezor. Esta prática permite-lhe confirmar que o Address apresentado no Sparrow não é fraudulento e que o Hardware Wallet possui efetivamente a chave privada necessária para gastar posteriormente os bitcoins garantidos com este Address. Isto ajuda-o a evitar vários tipos de ataques.



Para efetuar esta verificação, clique no botão "*Display Address*".



![Image](assets/fr/32.webp)



Verifique se o Address apresentado no seu Trezor corresponde ao Wallet do Sparrow. É também aconselhável efetuar esta verificação imediatamente antes de comunicar o seu Address ao remetente, para ter a certeza da sua validade. Pode premir o botão direito para confirmar.



![Image](assets/fr/33.webp)



Também pode adicionar um "*Label*" para descrever a fonte de bitcoins que será protegida com este Address. Esta é uma boa prática que te permite gerir melhor os teus UTXOs.



![Image](assets/fr/34.webp)



Pode então utilizar este Address para receber bitcoins.



![Image](assets/fr/35.webp)



## Como enviar bitcoins com o Trezor Model One?



Agora que já recebeu os seus primeiros Satss no seu Wallet protegido pelo Model One, também os pode gastar! Ligue o Trezor ao computador, inicie o Sparrow Wallet e vá ao separador "*Enviar*" para criar uma nova transação.



![Image](assets/fr/36.webp)



Se pretender *Controlar as moedas*, ou seja, escolher especificamente os UTXOs a consumir na transação, vá ao separador "*UTXOs*". Selecione os UTXOs que pretende gastar e, em seguida, clique em "*Enviar selecionados*". Será redireccionado para o mesmo ecrã no separador "*Enviar*", mas com os seus UTXOs já selecionados para a transação.



![Image](assets/fr/37.webp)



Introduzir o Address de destino. Também pode introduzir vários endereços clicando no botão "*+ Adicionar*".



![Image](assets/fr/38.webp)



Escreva um "*Rótulo*" para se lembrar do objetivo desta despesa.



![Image](assets/fr/39.webp)



Selecionar o montante a enviar para este Address.



![Image](assets/fr/40.webp)



Ajuste a taxa da sua transação de acordo com o mercado atual. Por exemplo, pode utilizar [Mempool.space] (https://Mempool.space/) para escolher uma taxa de comissão adequada.



Certifique-se de que todos os parâmetros da transação estão corretos e, em seguida, clique em "*Criar transação*".



![Image](assets/fr/41.webp)



Se tudo estiver a seu gosto, clique em "*Finalizar transação para assinatura*".



![Image](assets/fr/42.webp)



Clique em "*Assinar*".



![Image](assets/fr/43.webp)



Clique em "*Sign*" junto ao seu Trezor Model One.



![Image](assets/fr/44.webp)



Verifique os parâmetros da transação no seu ecrã Hardware Wallet, incluindo o Address de receção do destinatário, o montante enviado e a taxa. Quando a transação tiver sido verificada no Trezor, clique com o botão direito do rato para a assinar.



![Image](assets/fr/45.webp)



A sua transação está agora assinada. Verifique uma última vez se tudo está OK e clique em "*Broadcast Transaction*" para a transmitir na rede Bitcoin.



![Image](assets/fr/46.webp)



Pode encontrá-lo no separador "*Transacções*" do Sparrow Wallet.



![Image](assets/fr/47.webp)



Parabéns, agora estás a par da utilização básica do Trezor Model One com o Sparrow Wallet! Para avançar um pouco mais, recomendo este tutorial completo sobre a utilização de um Trezor Hardware Wallet com um BIP39 passphrase para reforçar a sua segurança:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Se achou este tutorial útil, agradecia que deixasse um polegar Green abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!