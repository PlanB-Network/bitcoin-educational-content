---
name: Sparrow Wallet - Multisig
description: Criar uma carteira multi-assinatura no Sparrow
---
![cover](assets/cover.webp)


Uma carteira multi-assinatura (frequentemente chamada "*Multisig*") é uma estrutura de carteira Bitcoin que exige várias assinaturas criptográficas, provenientes de chaves diferentes, para autorizar um gasto. Ao contrário de uma carteira convencional ("*singlesig*"), em que uma única chave privada é suficiente para desbloquear um UTXO, a Multisig baseia-se num modelo **m-de-n**: das _n_ chaves associadas à carteira, _m_ têm imperativamente de coassinar cada transação.


Este mecanismo permite partilhar o controlo de uma carteira entre várias entidades ou dispositivos. Por exemplo, numa configuração 2-de-3, são gerados três conjuntos de chaves independentes, mas apenas dois são necessários para libertar fundos. Esta arquitetura reduz drasticamente os riscos associados ao comprometimento ou à perda de uma chave: um ladrão com acesso a apenas uma chave não consegue esvaziar a carteira, e um utilizador que perca uma delas continua a poder aceder aos seus fundos com as outras duas.


![Image](assets/fr/01.webp)


No entanto, esta maior segurança tem como contrapartida uma maior complexidade. Configurar uma carteira Multisig exige guardar várias frases mnemónicas (uma por fator de assinatura) e chaves públicas alargadas ("*xpub*"). De facto, se estiver a utilizar uma carteira Multisig 2-de-3, para recuperar a carteira precisa de ter as três frases mnemónicas, ou pelo menos duas das três frases. Mas, se tiver apenas duas das três frases, também precisa de aceder aos três *xpubs*, sem os quais será impossível recuperar as chaves públicas necessárias para aceder aos bitcoins que protegem.


Resumindo, para recuperar uma carteira Multisig, tem de:


- Ou aceder a todas as frases mnemónicas associadas a cada fator de assinatura;
- Ou ter o número mínimo de frases mnemónicas exigido pelo limiar para poder assinar, e ter também acesso aos xpubs de todos os fatores, de forma a recuperar as chaves públicas necessárias.


![Image](assets/fr/02.webp)


Esta gestão das cópias de segurança da carteira Multisig é facilitada pelos *Descritores de Script de Saída*, que reúnem todos os dados públicos necessários para aceder aos fundos. No entanto, esta funcionalidade ainda não está implementada em todos os programas de gestão de carteiras.


A Multisig é particularmente adequada para bitcoiners que procuram maior segurança ou gestão coletiva de fundos: empresas, associações, famílias ou utilizadores individuais que detêm uma quantidade significativa de bitcoins. Pode ser utilizada para criar esquemas de governação descentralizada, por exemplo, para distribuir a autoridade de assinatura entre vários gestores ou membros de uma equipa.


Neste tutorial, vamos aprender a criar e utilizar uma carteira multi-assinatura clássica com o **Sparrow Wallet**. Se pretender criar uma carteira multi-assinatura personalizada com timelocks, recomendo antes o uso do Liana:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Pré-requisitos


Para este tutorial, vou mostrar-lhe como criar uma Multisig com o [software de gestão de carteiras Sparrow Wallet](https://sparrowwallet.com/download/). Se ainda não instalou este software, faça-o agora. Se precisar de ajuda, também temos um tutorial detalhado sobre a configuração do Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Para configurar uma carteira multi-assinatura, vai precisar de diferentes Hardware Wallets. Para uma Multisig 2-de-3, por exemplo, poderia utilizar:


- Uma Trezor Model One;
- Uma Ledger Flex;
- Uma Passport Core.


![Image](assets/fr/03.webp)


É uma boa ideia utilizar Hardware Wallets de marcas diferentes na sua configuração Multisig. Isto garante que, se um modelo específico apresentar um problema grave, isso não afetará a segurança geral da sua Multisig. Além disso, permite-lhe beneficiar das vantagens específicas de cada dispositivo. Por exemplo, na minha configuração:



- A Trezor Model One é totalmente open-source, o que permite verificar a geração da seed. No entanto, como não está equipada com um Secure Element, continua vulnerável a ataques físicos;



- A Ledger Flex, por outro lado, beneficia de firmware proprietário não verificável, mas incorpora um Secure Element que oferece uma excelente proteção física;



- A Passport Core combina firmware totalmente open-source, um Secure Element e trocas air-gapped por código QR. É um terceiro assinante independente, capaz de verificar endereços e assinar PSBTs sem ligação de dados USB.


Antes de configurar a sua carteira Multisig, certifique-se de que cada Hardware Wallet está corretamente configurada (geração e guarda da frase mnemónica, definição do PIN). Para instruções detalhadas, pode consultar os nossos tutoriais para cada Hardware Wallet, por exemplo:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Como veremos mais adiante neste tutorial, também é possível integrar na sua configuração Multisig um fator que não está associado a uma Hardware Wallet, mas cujas chaves privadas ficam guardadas no seu PC. Este método é obviamente menos seguro do que o uso exclusivo de Hardware Wallets, mas pode ser relevante em certos casos. Por exemplo, numa Multisig 2-de-3, poderia optar por duas Hardware Wallets e uma Software Wallet.

> ⚠️ **Aviso de segurança para a Coldcard MK3:** não crie uma nova seed numa MK3 com firmware anterior à versão 4.2.0. As seeds geradas em firmware anterior devem ser substituídas e os fundos transferidos. Por este motivo, este tutorial utiliza a Passport Core como referência de assinante air-gapped.


## Criar uma carteira Multisig


Abra o Sparrow Wallet, clique no separador "*File*" e, em seguida, selecione "*New Wallet*".


![Image](assets/fr/04.webp)


Atribua um nome à sua carteira multi-assinatura e clique em "*Create Wallet*" para confirmar.


![Image](assets/fr/05.webp)


No menu suspenso "*Policy Type*", selecione a opção "*Multi Signature*".


![Image](assets/fr/06.webp)


No canto superior direito, pode agora definir o número total de chaves da sua Multisig, bem como o número de coassinantes necessários para autorizar uma despesa. No meu exemplo, trata-se de um esquema 2-de-3.


![Image](assets/fr/07.webp)


Na parte inferior da janela, o Sparrow Wallet apresenta três "*Keystore*". Cada um representa um conjunto de chaves. Aqui, estou a utilizar três Hardware Wallets, pelo que cada "*Keystore*" corresponde a uma delas. Vamos agora configurá-las.


Começo pela Passport Core. No separador "*Keystore 1*", escolho a opção "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Na Passport, abra a conta que pretende utilizar e selecione "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". A Passport apresenta um código QR animado contendo a informação da sua chave pública.

No Sparrow, selecione "*Scan...*" junto a "*Passport*" e digitalize esse código QR animado com a webcam do seu computador. Verifique a impressão digital da chave mestra apresentada pelo Sparrow em relação à mostrada pela Passport e, em seguida, importe o keystore.

O xpub da sua Passport já foi importado. Repita o procedimento adequado para a Ledger Flex e a Trezor Model One.


Para a Ledger Flex, seleciono "*Keystore 2*" e, em seguida, clico em "*Connected Hardware Wallet*". Certifique-se de que a Ledger está ligada ao computador, desbloqueada e com a aplicação Bitcoin aberta.


![Image](assets/fr/15.webp)


Em seguida, clique no botão "*Scan...*".


![Image](assets/fr/16.webp)


Junto ao nome da sua Hardware Wallet, clique em "*Import Keystore*".


![Image](assets/fr/17.webp)


O segundo signatário está agora corretamente registado no Sparrow Wallet.


![Image](assets/fr/18.webp)


Repito exatamente o mesmo procedimento com a Trezor One para finalizar a configuração da Multisig.


![Image](assets/fr/19.webp)


Na minha configuração não abordamos este caso, mas se quiser incluir uma assinatura através de uma carteira de software no Sparrow (hot wallet) na sua Multisig, basta clicar no botão "*New or Imported Software Wallet*".


Agora que todos os seus dispositivos de assinatura estão importados no Sparrow Wallet, pode finalizar a criação da Multisig clicando em "*Apply*".


![Image](assets/fr/20.webp)


Escolha uma palavra-passe forte para proteger o acesso à sua carteira Sparrow Wallet. Esta palavra-passe protege as suas chaves públicas, endereços, labels e histórico de transações contra acessos não autorizados.


Lembre-se de guardar esta palavra-passe num local seguro, como um gestor de palavras-passe, para evitar perdê-la.


![Image](assets/fr/21.webp)


## Fazer a cópia de segurança de uma carteira Multisig


Vamos agora guardar o *Descritor de Script de Saída* num suporte independente e manter dele várias cópias.


O *Descritor* contém todos os xpubs da sua carteira Multisig, bem como os caminhos de derivação utilizados para gerar as chaves. Lembre-se do que vimos na Parte 1: para restaurar uma carteira Multisig, tem de ter **todas** as frases mnemónicas, ou apenas o número mínimo necessário para atingir o limiar de assinatura. No entanto, neste último caso, é também essencial ter **os xpubs** dos signatários em falta. O *Descritor* contém todos os xpubs da sua Multisig.


Se isto não estiver claro, lembre-se apenas disto: para recuperar uma Multisig, precisa do número mínimo de frases mnemónicas para cada Hardware Wallet utilizada, em função do limiar (no meu caso: 2 frases), bem como do *Descritor*.


Este *Descritor* não contém nenhuma chave privada, apenas chaves públicas. Isto significa que não dá acesso aos fundos. Por isso, não é tão crítico como as frases mnemónicas, que dão acesso total aos seus bitcoins. O risco associado ao *Descritor* está unicamente relacionado com a confidencialidade: em caso de comprometimento, um terceiro poderia observar todas as suas transações, mas não poderia gastar os seus fundos.


Recomendo vivamente que crie várias cópias deste *Descritor* e as guarde junto de cada dispositivo de assinatura da sua Multisig. Por exemplo, no meu caso, imprimo o *Descritor* em papel e guardo uma cópia junto da Passport, outra junto da Trezor e outra junto da Ledger. Guardo também este *Descritor* em ficheiro PDF em três pens USB, cada uma armazenada junto de uma das Hardware Wallets. Desta forma, maximizo as hipóteses de nunca perder este *Descritor* e tenho a certeza de ter duas cópias (uma física e uma digital) junto de cada dispositivo.


Assim que a sua carteira Multisig for criada, o Sparrow fornece-lhe automaticamente este *Descritor*. Clique no botão "*Save PDF...*" para o guardar tanto em texto como em código QR.


![Image](assets/fr/22.webp)


Pode depois imprimir este PDF e copiá-lo para as suas pens USB.


![Image](assets/fr/23.webp)


A Passport utiliza a configuração multisig importada pelo Sparrow para apresentar e verificar a informação de chave relevante durante o processo de emparelhamento por QR e de assinatura. Guarde o *Descritor* de forma independente: continua a ser essencial para recuperar a carteira caso um signatário fique indisponível.


Para além de guardar o *Descritor*, não se esqueça de prestar especial atenção à guarda das frases mnemónicas de cada um dos seus dispositivos de assinatura. Se está a começar agora, recomendo vivamente que consulte este outro tutorial para aprender a guardar e a gerir corretamente essas frases:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Antes de receber os seus primeiros bitcoins na sua Multisig, **aconselho vivamente que faça um teste de recuperação com a carteira vazia**. Anote algumas informações de referência, como o primeiro endereço de receção, e depois reponha as suas Hardware Wallets enquanto a carteira ainda está vazia. Em seguida, tente restaurar a sua carteira Multisig nas Hardware Wallets utilizando as suas cópias em papel das frases mnemónicas e, depois, no Sparrow, utilizando o *Descritor*. Verifique se o primeiro endereço gerado após a restauração corresponde ao que anotou originalmente. Se for esse o caso, pode ficar tranquilo quanto à fiabilidade das suas cópias de segurança em papel.


Para saber mais sobre como efetuar um teste de recuperação, sugiro que consulte este outro tutorial:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Receber bitcoins na sua Multisig


A sua carteira está agora pronta para receber bitcoins. No Sparrow, clique no separador "*Receive*".


![Image](assets/fr/30.webp)


Antes de utilizar o endereço gerado pelo Sparrow Wallet, tire um momento para o verificar diretamente no ecrã das suas Hardware Wallets. Isto garante que o endereço não foi alterado e que os seus dispositivos possuem as chaves privadas necessárias para gastar os fundos associados. Isto ajuda a proteger-se contra vários vetores de ataque.


Para tal, clique em "*Display Address*" para apresentar o endereço na sua Trezor ou Ledger, quando ligadas por cabo.


![Image](assets/fr/31.webp)


Com a Passport, selecione a conta multisig e escolha "*Verify Address*". Digitalize o código QR do endereço de receção apresentado pelo Sparrow. A Passport confirma no seu ecrã se o endereço pertence à carteira multisig.


Verifique se o endereço apresentado em cada Hardware Wallet corresponde exatamente ao apresentado no Sparrow Wallet. É aconselhável fazer isto imediatamente antes de partilhar o endereço com o pagador, para garantir a sua integridade.


Pode então atribuir um "*Label*" a este endereço, para indicar a origem dos bitcoins recebidos. É uma boa forma de organizar a gestão dos seus UTXOs.


![Image](assets/fr/34.webp)


Depois de verificado, pode utilizar o endereço para receber bitcoins.


![Image](assets/fr/35.webp)


## Enviar bitcoins com a sua Multisig


Agora que recebeu os seus primeiros sats na sua carteira Multisig, também os pode gastar! No Sparrow, vá ao separador "*Send*" para construir uma nova transação.


![Image](assets/fr/36.webp)


Se quiser utilizar o *Coin Control*, ou seja, selecionar manualmente os UTXOs que deseja gastar, vá ao separador "*UTXOs*". Escolha os UTXOs que pretende gastar e clique em "*Send Selected*". Será automaticamente redirecionado para o separador "*Send*", com os UTXOs já pré-preenchidos.


![Image](assets/fr/37.webp)


Introduza o endereço de destino. Podem ser adicionados vários endereços clicando em "*+ Add*".


![Image](assets/fr/38.webp)


Adicione um "*Label*" para descrever a finalidade desta despesa, para facilitar o acompanhamento das suas transações.


![Image](assets/fr/39.webp)


Introduza o montante a enviar para o endereço selecionado.


![Image](assets/fr/40.webp)


Ajuste a taxa de acordo com as condições atuais da rede. Por exemplo, consulte o [Mempool.space](https://Mempool.space/) para selecionar um nível de taxa adequado.


Depois de verificar todos os parâmetros da transação, clique em "*Create Transaction*".


![Image](assets/fr/41.webp)


Se estiver satisfeito com tudo, clique em "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Na parte inferior do ecrã, verá que o Sparrow está à espera de 2 assinaturas. Isto é normal: a carteira aqui utilizada é uma Multisig 2-de-3.


![Image](assets/fr/43.webp)


Começo por assinar com a minha Passport. No Sparrow, clique em "*Show QR*" para apresentar a PSBT (*Partially Signed Bitcoin Transaction*, ou Transação Bitcoin Parcialmente Assinada) sob a forma de códigos QR animados. Na Passport, selecione a conta multisig e escolha "*Sign with QR Code*", depois digitalize o código QR apresentado pelo Sparrow.


No ecrã da sua Hardware Wallet, verifique cuidadosamente os parâmetros da transação: o endereço do destinatário, o montante enviado e as taxas. Depois de confirmada a transação, valide para prosseguir para a assinatura.


Depois de aprovar a transação, a Passport apresenta a PSBT assinada sob a forma de códigos QR animados. No Sparrow, clique em "*Scan QR*" e digitalize esses códigos com a sua webcam. A assinatura da Passport é então adicionada. Utilizo agora a Ledger para a segunda assinatura necessária: ligo-a e desbloqueio-a, depois clico em "*Sign*" no Sparrow.


![Image](assets/fr/48.webp)


Clique em "*Sign*" junto ao nome da sua Hardware Wallet.


![Image](assets/fr/49.webp)


Na primeira vez que utilizar a sua Ledger com esta Multisig, o Sparrow vai pedir-lhe que verifique as chaves públicas alargadas (xpubs) dos coassinantes. Tal como com a Passport, este passo evita que assine às cegas mais tarde. Para validar esta informação, compare o xpub apresentado no ecrã da Ledger com os fornecidos diretamente pelas suas outras Hardware Wallets.


![Image](assets/fr/50.webp)


Verifique o endereço do destinatário, o montante transferido e a taxa da transação, depois assine a transação.


![Image](assets/fr/51.webp)


Pressione o ecrã para assinar.


![Image](assets/fr/52.webp)


O Sparrow tem agora as duas assinaturas necessárias para libertar os fundos da carteira Multisig. Verifique a transação uma última vez e, se estiver tudo em ordem, clique em "*Broadcast Transaction*" para a transmitir através da rede.


![Image](assets/fr/53.webp)


Encontrará esta transação no separador "*Transactions*" do Sparrow Wallet.


![Image](assets/fr/54.webp)


Parabéns, agora já sabe como configurar e utilizar uma carteira multi-assinatura no Sparrow. Se achou este tutorial útil, ficaria grato se deixasse um polegar verde abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Obrigado por partilhar!


Para ir mais longe, recomendo que consulte este tutorial sobre outro método para aumentar a segurança da sua carteira Bitcoin, a passphrase BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
