---
name: Sparrow Wallet - Multisig
description: Criar uma carteira com várias assinaturas no Sparrow
---
![cover](assets/cover.webp)



Um Wallet multi-assinatura (frequentemente designado por "*Multisig*") é uma estrutura Bitcoin Wallet que requer várias assinaturas criptográficas, a partir de chaves diferentes, para autorizar uma despesa. Ao contrário de um Wallet convencional ("*singlesig*"), em que uma única chave privada é suficiente para desbloquear um UTXO, o Multisig baseia-se num modelo **m-de-n**: das _n_ chaves associadas ao Wallet, _m_ deve imperativamente co-assinar cada transação.



Este mecanismo permite que o controlo de uma carteira seja partilhado entre várias entidades ou dispositivos. Por exemplo, numa configuração 2 de 3, são gerados três conjuntos independentes de chaves, mas apenas dois são necessários para libertar fundos. Esta arquitetura reduz drasticamente os riscos associados ao comprometimento ou à perda de uma chave: um ladrão com acesso a apenas uma chave não pode esvaziar o Wallet, e um utilizador que perca uma pode ainda aceder aos seus fundos com as duas restantes.



![Image](assets/fr/01.webp)



No entanto, esta maior segurança é acompanhada de uma maior complexidade. A configuração de um Multisig Wallet requer a segurança de várias frases Mnemonic (uma por fator de assinatura) e chaves públicas alargadas ("*xpub*"). De facto, se estiver a utilizar um Multisig 2-of-3 Wallet, para recuperar o Wallet tem de ter as três frases Mnemonic, ou pelo menos duas das três frases. Mas se só tiver duas das três frases, também precisa de ter acesso aos três *xpubs*, sem os quais será impossível recuperar as chaves públicas necessárias para aceder aos bitcoins que protegem.



Em resumo, para recuperar uma carteira Multisig, é necessário :




- Ou aceder a todas as frases Mnemonic associadas a cada fator de assinatura;
- Ter o número mínimo de frases Mnemonic exigido pelo limiar para poder assinar, e também ter acesso às xpubs de todos os factores para obter as chaves públicas necessárias.



![Image](assets/fr/02.webp)



Esta gestão das cópias de segurança da carteira Multisig é facilitada pelos *Output Script Descriptors*, que agrupam todos os dados públicos necessários para aceder aos fundos. No entanto, esta funcionalidade ainda não está implementada em todos os programas informáticos de gestão de carteiras.



O Multisig é particularmente adequado para bitcoiners que procuram maior segurança ou gestão colectiva de fundos: empresas, associações, famílias ou utilizadores individuais que detêm uma quantidade significativa de bitcoins. Pode ser utilizado para criar esquemas de governação descentralizados, por exemplo, para distribuir a autoridade de assinatura entre vários gestores ou membros da equipa.



Neste tutorial, aprenderemos a criar e usar uma carteira clássica com várias assinaturas Wallet com **Sparrow Wallet**. Se pretender criar uma carteira personalizada com várias assinaturas e relógios de ponto, recomendo a utilização do Liana:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Pré-requisitos



Neste tutorial, vou mostrar-lhe como criar um Multisig com o [software de gestão de portefólio Sparrow Wallet] (https://sparrowwallet.com/download/). Se ainda não instalou este software, faça-o agora. Se precisar de ajuda, também temos um tutorial detalhado sobre a configuração do Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Para configurar um Wallet com várias assinaturas, precisará de carteiras de hardware diferentes. Para um Multisig 2-de-3, por exemplo, pode utilizar :




- Um Trezor Modelo Um;
- Ledger Flex;
- Um Coldcard MK3.



![Image](assets/fr/03.webp)



É uma boa ideia utilizar diferentes marcas de Hardware Wallet na configuração do seu Multisig. Isto garante que, se um modelo específico tiver um problema grave, este não afectará a segurança geral do seu Multisig. Além disso, permite-lhe beneficiar das vantagens específicas de cada dispositivo. Por exemplo, na minha configuração :





- O Trezor Model One é totalmente de código aberto, o que permite verificar a geração seed. No entanto, como não está equipado com um elemento seguro, continua a ser vulnerável a ataques físicos;





- O Ledger Flex, por outro lado, beneficia de um firmware proprietário não verificável, mas incorpora um elemento seguro que oferece uma excelente proteção física;





- O Coldcard está equipado com um elemento seguro e o seu código é pesquisável. É uma escolha interessante para a nossa configuração, uma vez que oferece funcionalidades de verificação não disponíveis noutros modelos.



Antes de configurar o seu Multisig Wallet, certifique-se de que cada Hardware Wallet está corretamente configurado (geração e memorização do Mnemonic, definição do PIN). Para obter instruções detalhadas, pode consultar os nossos tutoriais para cada Hardware Wallet, por exemplo :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Como veremos mais adiante neste tutorial, é também possível integrar na configuração do Multisig um fator que não está associado a um Hardware Wallet, mas cujas chaves privadas estão armazenadas no seu PC. Este método é obviamente menos seguro do que o uso exclusivo de carteiras de hardware, mas pode ser relevante em certos casos. Por exemplo, para um Multisig 2-de-3, pode optar por duas carteiras de hardware e um Software Wallet.



## Criar uma carteira Multisig



Abra o Sparrow Wallet, clique no separador "*File*" e, em seguida, selecione "*New Wallet*".



![Image](assets/fr/04.webp)



Atribua um nome à sua carteira com várias assinaturas e, em seguida, clique em "*Criar Wallet*" para confirmar.



![Image](assets/fr/05.webp)



No menu pendente "*Tipo de política*", selecione a opção "*Multi-assinatura*".



![Image](assets/fr/06.webp)



No canto superior direito, pode agora definir o número total de chaves no seu Multisig, bem como o número de co-signatários necessários para autorizar uma despesa. No meu exemplo, este é um esquema 2 de 3.



![Image](assets/fr/07.webp)



Na parte inferior da janela, o Sparrow Wallet exibe três "*Keystore*". Cada um representa um conjunto de chaves. Aqui, estou a utilizar três carteiras de hardware, pelo que cada "*Keystore*" corresponde a uma delas. Vamos agora configurá-los.



Começo com o Coldcard. No separador "*Keystore 1*", escolho a opção "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



No Coldcard, quando o dispositivo está desbloqueado, vou ao menu "*Definições*" e depois a "*Carteiras Multisig*".



![Image](assets/fr/09.webp)



Este menu permite-lhe gerir as carteiras Multisig em que a Coldcard participa. Quero criar uma nova carteira, por isso selecciono "*Exportar XPUB*".



![Image](assets/fr/10.webp)



Para o campo "*Número de conta*", se gerir apenas uma conta, pode deixá-lo em branco e validar diretamente premindo o botão de confirmação.



![Image](assets/fr/11.webp)



O Coldcard irá então generate um ficheiro contendo o seu xpub, guardado no cartão Micro SD.



![Image](assets/fr/12.webp)



Insira este Micro SD no seu computador. No Sparrow Wallet, clique no botão "*Importar ficheiro...*" ao lado de "*Coldcard Multisig*", depois selecione o ficheiro criado pelo Coldcard no cartão.



![Image](assets/fr/13.webp)



O seu xpub foi importado com sucesso. Vamos agora repetir o procedimento com as outras duas carteiras de hardware.



![Image](assets/fr/14.webp)



Para o Ledger Flex, selecciono "*Keystore 2*" e, em seguida, clico em "*Connected Hardware Wallet*". Certifique-se de que o Ledger está ligado ao computador, desbloqueado e que a aplicação Bitcoin está aberta.



![Image](assets/fr/15.webp)



Em seguida, clique no botão "*Digitalizar...*".



![Image](assets/fr/16.webp)



Ao lado do nome do seu portfólio de hardware, clique em "*Importar Keystore*".



![Image](assets/fr/17.webp)



O segundo signatário está agora corretamente registado no Sparrow Wallet.



![Image](assets/fr/18.webp)



Repito exatamente o mesmo procedimento com o Trezor One para finalizar a configuração do Multisig.



![Image](assets/fr/19.webp)



Na minha configuração não cobrimos este caso, mas se quiser incluir uma assinatura através de um Software Wallet no Sparrow (Hot Wallet) dentro do seu Multisig, basta clicar no botão "*New or Imported Software Wallet*".



Agora que todos os seus dispositivos de assinatura foram importados para o Sparrow Wallet, pode finalizar a criação do Multisig clicando em "*Aplicar*".



![Image](assets/fr/20.webp)



Escolha uma palavra-passe forte para proteger o acesso ao seu Sparrow Wallet Wallet. Esta palavra-passe protege as suas chaves públicas, endereços, etiquetas e histórico de transacções contra o acesso não autorizado.



Lembre-se de guardar esta palavra-passe num local seguro, como um gestor de palavras-passe, para evitar perdê-la.



![Image](assets/fr/21.webp)



## Fazer o backup de uma carteira Multisig



Vamos agora guardar o nosso *Output Script Descriptor* no Coldcard (isto só se aplica a utilizadores com um Coldcard no seu Multisig) e, acima de tudo, vamos manter uma cópia de segurança num suporte independente.



O *Descriptor* contém todos os xpubs no seu portfólio Multisig, bem como os caminhos de derivação usados para generate as chaves. Lembre-se do que vimos na Parte 1: para restaurar um portfólio Multisig, você deve ter **todas** as frases Mnemonic, ou apenas o número mínimo necessário para atingir o limite de assinaturas. No entanto, neste último caso, é também essencial ter **as xpubs** dos signatários em falta. O *Descriptor* contém todas as xpubs do seu Multisig.



Se isto não for claro, lembre-se do seguinte: para recuperar um Multisig, precisa do número mínimo de frases Mnemonic para cada Hardware Wallet utilizado, dependendo do limiar (no meu caso: 2 frases), bem como do *Descritor*.



Este *Descritor* não contém chaves privadas, apenas públicas. Isto significa que não dá acesso aos fundos. Por conseguinte, não é tão crítico como as frases Mnemonic, que dão acesso total aos seus bitcoins. O risco com o *Descriptor* está apenas relacionado com a confidencialidade: em caso de comprometimento, um terceiro poderia observar todas as suas transacções, mas não poderia gastar os seus fundos.



Recomendo vivamente que crie várias cópias deste *Descriptor* e que as guarde em cada dispositivo de assinatura do seu Multisig. Por exemplo, no meu caso, imprimo o *Descriptor* em papel e guardo uma cópia com o Coldcard, outra com o Trezor e uma com o Ledger. Também guardo este *Descriptor* como ficheiro PDF em três pen drives USB, cada uma guardada com uma das carteiras de hardware. Desta forma, maximizo as minhas hipóteses de nunca perder este *Descriptor* e tenho a certeza de ter duas cópias (uma física e uma digital) em cada dispositivo.



Após a criação do seu portefólio Multisig, o Sparrow fornece-lhe automaticamente este *Descritor*. Clique no botão "*Guardar PDF...*" para o guardar como texto e como código QR.



![Image](assets/fr/22.webp)



Pode então imprimir este PDF e copiá-lo para as suas chaves USB.



![Image](assets/fr/23.webp)



Também registaremos este *Descriptor* no Coldcard (se utilizar um na sua configuração). Isto permitirá à Coldcard verificar se cada transação assinada posteriormente corresponde ao Wallet original: xpubs corretos, formato Address correto, caminho de derivação correto... Sem este *Descriptor* importado, a Coldcard não pode confirmar que os endereços Exchange não foram desviados ou que o PSBT não foi adulterado.



É isto que torna a Coldcard tão interessante numa Multisig: oferece verificações adicionais contra certos ataques sofisticados, que outras carteiras de hardware não permitem (desde que, obviamente, a utilize para assinar).



No Sparrow, aceda ao menu "*Configurações*" e, em seguida, clique em "*Exportar...*".



![Image](assets/fr/24.webp)



Junto à opção "*Coldcard Multisig*", clique em "*Exportar ficheiro...*" e guarde o ficheiro de texto no cartão Micro SD.



![Image](assets/fr/25.webp)



Em seguida, insira o cartão no Coldcard. Aceda ao menu "*Configurações*", depois "*Carteiras Multisig*" e selecione "*Importar de SD*".



![Image](assets/fr/26.webp)



Selecione o ficheiro adequado e confirme a importação.



![Image](assets/fr/27.webp)



Clique no nome do seu Multisig recentemente importado.



![Image](assets/fr/28.webp)



Verifique os parâmetros de configuração do Multisig e, em seguida, confirme o registo.



![Image](assets/fr/29.webp)



O seu Multisig está agora corretamente guardado na sua Coldcard. Se tiver vários Coldcards no mesmo Multisig, repita este procedimento para cada um deles.



Para além de guardar o *Descriptor*, não se esqueça de prestar especial atenção a guardar as frases Mnemonic para cada um dos seus dispositivos de assinatura. Se está a começar, recomendo vivamente que consulte este outro tutorial para aprender a guardá-las e geri-las corretamente:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Antes de receber os seus primeiros bitcoins no seu Multisig, **aconselho-o vivamente a efetuar um teste de recuperação vazio**. Tome nota de algumas informações de referência, como a primeira receção do Address, depois reinicie as suas carteiras de hardware enquanto o Wallet ainda está vazio. De seguida, tente restaurar o seu Multisig Wallet nas Carteiras de Hardware utilizando as suas cópias de segurança em papel da frase Mnemonic e depois no Sparrow utilizando o *Descriptor*. Verifique se o primeiro Address gerado após o restauro corresponde àquele que escreveu originalmente. Se corresponder, pode ter a certeza de que as suas cópias de segurança em papel são fiáveis.



Para saber mais sobre como efetuar um teste de recuperação, sugiro que consulte este outro tutorial:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Receber bitcoins no seu Multisig



O teu Wallet está agora pronto para receber bitcoins. No Sparrow, clique no separador "*Receive*".



![Image](assets/fr/30.webp)



Antes de usar o Address gerado pelo Sparrow Wallet, reserve um tempo para verificá-lo diretamente na tela de suas carteiras de hardware. Isso garantirá que o Address não foi alterado e que seus dispositivos possuem as chaves privadas necessárias para gastar os fundos associados. Isto ajuda a protegê-lo contra uma série de vectores de ataque.



Para o fazer, clique em "*Display Address*" para visualizar o Address no seu Trezor ou Ledger, quando ligado por cabo.



![Image](assets/fr/31.webp)



Com o Coldcard, esta verificação pode ser efectuada sem qualquer interação com o Sparrow. Basta abrir o menu "*Address Explorer*" e selecionar o seu Multisig na parte inferior.



![Image](assets/fr/32.webp)



Em seguida, verá os endereços de receção gerados pelo Multisig.



![Image](assets/fr/33.webp)



Verifique se o Address apresentado em cada Hardware Wallet corresponde exatamente ao Wallet do Sparrow. É aconselhável fazer isto mesmo antes de partilhar o Address com o pagador, para ter a certeza da sua integridade.



Pode então atribuir um "*Label*" a este Address, para indicar a origem dos bitcoins recebidos. Esta é uma boa forma de organizar a gestão dos teus UTXOs.



![Image](assets/fr/34.webp)



Uma vez verificado este facto, pode utilizar o Address para receber bitcoins.



![Image](assets/fr/35.webp)



## Enviar bitcoins com o seu Multisig



Agora que já recebeste os teus primeiros Satss no teu Multisig Wallet, também os podes gastar! No Sparrow, vá ao separador "*Enviar*" para criar uma nova transação.



![Image](assets/fr/36.webp)



Se pretender utilizar o *Controlo de Moedas*, ou seja, selecionar manualmente os UTXOs que pretende gastar, vá ao separador "*UTXOs*". Escolha os UTXOs que pretende gastar e, em seguida, clique em "*Enviar selecionados*". Será automaticamente redireccionado para o separador "*Enviar*", com os UTXOs já pré-preenchidos.



![Image](assets/fr/37.webp)



Introduzir o Address de destino. Podem ser adicionados vários endereços clicando em "*+ Adicionar*".



![Image](assets/fr/38.webp)



Adicione um "*Rótulo*" para descrever a finalidade desta despesa, de modo a facilitar o acompanhamento das suas transacções.



![Image](assets/fr/39.webp)



Introduzir o montante a enviar para o Address selecionado.



![Image](assets/fr/40.webp)



Ajuste a taxa de carregamento de acordo com as condições actuais da rede. Por exemplo, consulte [Mempool.space] (https://Mempool.space/) para selecionar um nível de carga adequado.



Depois de verificar todos os parâmetros da transação, clique em "*Criar transação*".



![Image](assets/fr/41.webp)



Se estiver satisfeito com tudo, clique em "*Finalizar transação para assinatura*".



![Image](assets/fr/42.webp)



Na parte inferior do ecrã, verá que a Sparrow está à espera de 2 assinaturas. Isto é normal: o Wallet utilizado aqui é um Multisig 2-de-3.



![Image](assets/fr/43.webp)



Começo a assinar com o meu Coldcard. Para o fazer, insiro um cartão Micro SD no computador e clico em "*Guardar transação*".



![Image](assets/fr/44.webp)



Existem 3 maneiras de transmitir a transação a ser assinada para o seu Hardware Wallet e depois recuperá-la do Sparrow. A primeira é usar um cartão Micro SD, como faremos aqui para o Coldcard. A segunda é através de uma ligação por cabo, que utilizaremos para a segunda assinatura (Ledger e Trezor). Finalmente, é possível utilizar a comunicação por código QR, para dispositivos equipados com câmara, como o Coldcard Q, o Jade Plus ou o Passport V2.



Depois de o PSBT (*Partially Signed Bitcoin Transaction*) ter sido guardado no Micro SD, insiro-o no Coldcard MK3 e selecciono o menu "*Ready to Sign*".



![Image](assets/fr/45.webp)



No seu ecrã Hardware Wallet, verifique cuidadosamente os parâmetros da transação: o Address do destinatário, o montante enviado e as despesas. Uma vez confirmada a transação, validar para proceder à assinatura.



![Image](assets/fr/46.webp)



De seguida, coloque o Micro SD no seu computador e clique em "*Load Transaction*" no Sparrow. Selecione o PSBT assinado pela Coldcard a partir dos seus ficheiros.



![Image](assets/fr/47.webp)



Pode ver que a assinatura Coldcard foi adicionada. Agora vou usar um segundo dispositivo, neste caso o Ledger, para realizar a segunda assinatura necessária. Conecto-o, desbloqueio-o e, em seguida, clico em "*Sign*" no Sparrow.



![Image](assets/fr/48.webp)



Clique em "*Sign*" junto ao nome do seu Hardware Wallet.



![Image](assets/fr/49.webp)



A primeira vez que utilizar o seu Ledger com este Multisig, o Sparrow pedir-lhe-á para verificar as chaves públicas alargadas (xpubs) dos co-signatários. Tal como com o Coldcard, este passo impede-o de assinar às cegas mais tarde. Para validar esta informação, compare o xpub apresentado no ecrã do Ledger com os fornecidos diretamente pelas suas outras carteiras de hardware.



![Image](assets/fr/50.webp)



Verificar o Address do destinatário, o montante transferido e a taxa de transação e, em seguida, assinar a transação.



![Image](assets/fr/51.webp)



Prima o ecrã para assinar.



![Image](assets/fr/52.webp)



O Sparrow agora tem as duas assinaturas necessárias para liberar os fundos da carteira Multisig. Verifique a transação uma última vez e, se tudo correr bem, clique em "*Broadcast Transaction*" para a transmitir pela rede.



![Image](assets/fr/53.webp)



Encontrará esta transação no separador "*Transacções*" do Sparrow Wallet.



![Image](assets/fr/54.webp)



Parabéns, agora você sabe como configurar e usar uma assinatura múltipla Wallet no Sparrow. Se este tutorial lhe foi útil, ficar-lhe-ia grato se deixasse um polegar Green abaixo. Não hesite em partilhar este artigo nas suas redes sociais. Obrigado por partilhar!



Para ir mais longe, recomendo que consulte este tutorial sobre outro método para aumentar a segurança do seu Bitcoin Wallet, o passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7