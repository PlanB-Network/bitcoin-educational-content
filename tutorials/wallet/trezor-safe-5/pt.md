---
name: Trezor Safe 5
description: Configuração e utilização do Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Crédito da imagem: [Trezor.io](https://trezor.io/)*



O Trezor Safe 5 é um Hardware Wallet de última geração concebido pela SatoshiLabs e lançado em 2024. Está posicionado como uma versão topo de gama do Safe 3, com foco na ergonomia e durabilidade. Beneficia dos mesmos avanços de segurança que o seu antecessor, o Safe 3, em comparação com o Model One e o Model T.



Com um preço de 169 euros, o Safe 5 está posicionado na categoria de topo de gama Hardware Wallet, competindo com modelos como o Coldcard, Ledger Nano X e Flex, Jade Plus, Passport e Bitbox.



O Safe 5 distingue-se pelo seu ecrã tátil a cores de 1,54 polegadas, protegido por *Gorilla Glass 3*, que resiste a choques e riscos. Está também equipado com um motor háptico *Trezor Touch* que emite pequenas vibrações quando é tocado. Tal como o Safe 3, incorpora um elemento seguro e funciona através de uma ligação USB-C, com a adição de uma porta Micro SD.



A principal diferença entre o Safe 3 e o Safe 5 reside na qualidade do dispositivo, para além dos aspectos de segurança. Melhora significativamente a experiência do utilizador, com um funcionamento mais suave e um ecrã mais confortável. Em termos de segurança, é equivalente.



![Image](assets/fr/01.webp)



O Safe 5 tem todas as caraterísticas essenciais que se esperam de um bom Hardware Wallet, incluindo uma excelente integração do passphrase BIP39. No entanto, ainda não suporta Miniscript.



Este modelo é particularmente adequado para utilizadores principiantes e intermédios. Por outro lado, pode não corresponder a todas as expectativas dos utilizadores avançados que procuram caraterísticas mais específicas disponíveis em dispositivos como o Coldcard. No entanto, se não necessitar destas opções avançadas, o Trezor Safe 5 pode ser uma excelente escolha.



## O modelo de segurança Trezor Safe 5



Tal como o Safe 3, o Trezor Safe 5 está equipado com um **Secure Element** certificado EAL6+, um avanço significativo em relação aos modelos anteriores, como o Model One e o Model T. Trata-se do chip OPTIGA Trust M V3, que não armazena o seed diretamente, mas actua como um componente criptográfico para garantir o acesso ao mesmo. O Secure Element retém um segredo que só pode ser acedido depois de o utilizador ter introduzido corretamente o PIN. Este segredo é então utilizado para desencriptar o seed, que é armazenado encriptado na memória principal do dispositivo.



Este sistema de segurança híbrido oferece uma proteção física melhorada, nomeadamente contra ataques de extração ou análises invasivas, problemas aos quais o Model One era propenso, particularmente na gestão de PIN. Estas vulnerabilidades são agora contornadas graças à utilização do elemento seguro. Este modelo mantém igualmente uma arquitetura de software de código aberto: o código que gere a geração e a utilização das chaves privadas permanece totalmente acessível e verificável. A pastilha OPTIGA gere apenas o código PIN, um elemento externo à gestão das chaves Bitcoin Wallet. Limita-se a libertar um segredo que pode ser utilizado para decifrar o seed. Além disso, o chip OPTIGA Trust M V3 beneficia de uma licença relativamente livre, que autoriza a SatoshiLabs a publicar livremente potenciais vulnerabilidades (NDA-Free).



Este modelo de segurança representa, na minha opinião, um dos melhores compromissos atualmente disponíveis no mercado. Combina as vantagens de um elemento seguro com a gestão de software de código aberto. Anteriormente, os utilizadores tinham de escolher entre a segurança física reforçada com um chip e a transparência com o código aberto; com o Trezor Safe, é possível beneficiar de ambos.



Neste tutorial, aprenderá a configurar e a utilizar o Trezor Safe 5 de forma segura.



## Desembalagem do Trezor Safe 5



Quando receber o seu Safe 5, certifique-se de que a caixa e o Seal estão intactos para confirmar que a embalagem não foi aberta. Uma verificação de software da autenticidade e integridade do dispositivo também será efectuada quando este for configurado mais tarde.



O conteúdo da caixa inclui :




- Trezor Safe 5;
- Uma bolsa com cartolina para gravar a sua frase Mnemonic, autocolantes e instruções;
- Cabo USB-C para USB-C.



Quando aberto, o Trezor Safe 5 deve estar protegido por um plástico protetor e a porta USB-C deve estar protegida por um Seal holográfico. Certifica-te de que está lá.



![Image](assets/fr/02.webp)



A navegação no dispositivo é bastante intuitiva:




- Toque na metade inferior do ecrã para avançar;
- Deslize para baixo para voltar atrás ;
- Prima e mantenha premido o ecrã para confirmar uma operação.



## Pré-requisitos



Neste tutorial, vou mostrar-lhe como utilizar o Trezor Safe 5 com o [software de gestão de carteiras Sparrow Wallet](https://sparrowwallet.com/download/). Se ainda não instalou este software, faça-o agora. Se precisar de ajuda, também temos um tutorial detalhado sobre a configuração do Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Também é necessário o software Trezor Suite para configurar o Safe 5, verificar a sua autenticidade e instalar o firmware. Só utilizaremos este software para esse efeito e, posteriormente, só será necessário para actualizações de firmware. Para a gestão diária do Wallet, utilizaremos exclusivamente o Sparrow Wallet, uma vez que está optimizado para o Bitcoin e é fácil de utilizar, mesmo para principiantes (o Sparrow apenas suporta o Bitcoin, não altcoins).



[Descarregar o Trezor Suite a partir do sítio Web oficial] (https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Para ambos os programas, recomendo vivamente que verifique a sua autenticidade (com o GnuPG) e a sua integridade (através do Hash) antes de os instalar na sua máquina. Se não sabe como fazer isso, pode seguir este outro tutorial :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Iniciar o Trezor Safe 5



Ligue o Safe 5 ao seu computador onde o Trezor Suite e o Sparrow Wallet já estão instalados.



![Image](assets/fr/04.webp)



Abra o Trezor Suite e, em seguida, clique em "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Selecione "*Bitcoin-only firmware*" e, em seguida, clique em "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



O Trezor Suite instalará então o firmware no seu Safe 5. Aguarde durante a instalação.



![Image](assets/fr/07.webp)



Clique em "*Continuar*".



![Image](assets/fr/08.webp)



Em seguida, proceda ao teste de autenticidade para se certificar de que o seu Hardware Wallet não é falso ou está comprometido.



![Image](assets/fr/09.webp)



No seu Safe 5, prima o ecrã para confirmar.



![Image](assets/fr/10.webp)



Se o seu Trezor for genuíno, aparecerá uma mensagem de confirmação no Trezor Suite.



![Image](assets/fr/11.webp)



Pode então saltar as janelas com as instruções básicas de funcionamento.



![Image](assets/fr/12.webp)



## Criar uma carteira Bitcoin



No Trezor Suite, clique no botão "*Create new Wallet*" (Criar novo Wallet).



![Image](assets/fr/13.webp)



Para criar um Wallet BIP39 padrão, comece por selecionar "*Legacy Wallet backup types*" no menu pendente e, em seguida, escolha entre uma frase Mnemonic de 12 ou 24 palavras (atualmente recomenda-se 12 palavras). Isto permitir-lhe-á criar uma carteira clássica de assinatura única. Aconselho-o a optar por parâmetros compatíveis com o BIP39, para facilitar a recuperação e evitar ficar limitado a um ambiente específico. Para finalizar, clique em "*Criar Wallet*".



Se quiser saber mais sobre as outras opções de cópia de segurança disponíveis no Trezor, incluindo *Multi-share Backup*, recomendo que consulte também este tutorial :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Aceitar as condições de utilização do Hardware Wallet.



![Image](assets/fr/15.webp)



Prima e mantenha premido o ecrã para criar uma nova carteira.



![Image](assets/fr/16.webp)



No Trezor Suite, clique em "*Continue to backup*".



![Image](assets/fr/17.webp)



O software fornece instruções sobre como gerir a sua frase Mnemonic.



Este Mnemonic dá-lhe acesso total e irrestrito a todos os seus bitcoins. Qualquer pessoa na posse desta frase pode roubar os seus fundos, mesmo sem acesso físico ao seu Trezor Safe 5.



A frase de 12 palavras restaura o acesso aos seus bitcoins em caso de perda, roubo ou quebra do seu Hardware Wallet. Por isso, é muito importante guardá-la cuidadosamente e guardá-la num local seguro.



Pode gravá-lo no cartão fornecido na caixa ou, para maior segurança, recomendo que o grave numa base de aço inoxidável para o proteger de incêndios, inundações ou desmoronamentos.



Confirme as instruções e, em seguida, clique no botão "*Create Wallet backup*" (Criar cópia de segurança do Wallet).



![Image](assets/fr/18.webp)



O Safe 5 criará a sua frase Mnemonic utilizando o seu gerador de números aleatórios. Certifique-se de que não está a ser observado durante esta operação. Escreva as palavras fornecidas no ecrã no suporte físico da sua escolha. Dependendo da sua estratégia de segurança, pode considerar fazer várias cópias físicas completas da frase (mas acima de tudo, não a divida). É importante manter as palavras numeradas e em ordem sequencial.



***Obviamente, nunca deve partilhar estas palavras na Internet, como eu faço neste tutorial. Este exemplo Wallet será utilizado apenas no Testnet e será apagado no final do tutorial



Para mais informações sobre a forma correta de guardar e gerir a sua frase Mnemonic, recomendo vivamente que siga este outro tutorial, especialmente se for um principiante:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Para passar para as palavras seguintes, clique na parte inferior do ecrã. Pode retroceder deslizando para baixo. Quando tiver escrito todas as palavras, mantenha o dedo no ecrã para passar à etapa seguinte.



![Image](assets/fr/20.webp)



Selecione as palavras da sua frase Mnemonic de acordo com a sua ordem para confirmar que as escreveu corretamente.



![Image](assets/fr/21.webp)



Quando este procedimento de verificação estiver concluído, clique no ecrã para continuar.



![Image](assets/fr/22.webp)



## Definir o código PIN



Segue-se o passo do código PIN. O código PIN desbloqueia o Trezor. Assim, fornece proteção contra o acesso físico não autorizado. Este código PIN não está envolvido na derivação das chaves criptográficas do seu Wallet. Assim, mesmo sem acesso ao código PIN, a posse da sua frase de 12 palavras Mnemonic permitir-lhe-á recuperar o acesso aos seus bitcoins.



No Trezor Suite, clique em "*Continue to PIN*" e, em seguida, no botão "*Set PIN*".



![Image](assets/fr/23.webp)



Confirmar com Safe 5.



![Image](assets/fr/24.webp)



Recomendamos que escolha um código PIN que seja o mais aleatório possível. Certifique-se de que guarda este código num local separado do local onde o Trezor está guardado (por exemplo, num gestor de palavras-passe). Pode definir um código PIN entre 8 e 50 dígitos. Recomendo que escolha um código PIN tão longo quanto possível para aumentar a segurança.



Utilize o painel tátil para introduzir o seu PIN.



![Image](assets/fr/25.webp)



Quando terminar, clique na marca Green no canto inferior direito e, em seguida, confirme o seu PIN uma segunda vez.



![Image](assets/fr/26.webp)



O seu código PIN foi registado.



![Image](assets/fr/27.webp)



No Trezor Suite, clique no botão "*Complete setup*".



![Image](assets/fr/28.webp)



A configuração do seu Safe 5 está agora concluída. Se desejar, pode alterar o nome e a página inicial do seu Hardware Wallet.



![Image](assets/fr/29.webp)



O software Trezor Suite já não será necessário, exceto para efetuar actualizações regulares do firmware do Hardware Wallet ou para efetuar um teste de recuperação. Vamos agora utilizar o Sparrow para gerir a carteira, uma vez que este software é perfeitamente adequado para uma utilização exclusiva do Bitcoin.



## Configurar o portefólio no Sparrow Wallet



Comece por descarregar e instalar o Sparrow Wallet [a partir do sítio Web oficial] (https://sparrowwallet.com/) no seu computador, se ainda não o tiver feito.



Depois de abrir o Sparrow Wallet, certifique-se de que o software está ligado a um nó Bitcoin, o que é indicado pelo visto no canto inferior direito do Interface. Se estiver a ter problemas em ligar o Sparrow, recomendo que consulte o início deste tutorial:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Clique no separador "*File*" (Ficheiro) e, em seguida, em "*New Wallet*" (Novo Wallet).



![Image](assets/fr/30.webp)



Dê um nome à sua carteira e, em seguida, clique em "*Criar Wallet*".



![Image](assets/fr/31.webp)



No menu pendente "*Script Type*", selecione o tipo de script que será utilizado para proteger os seus bitcoins. Eu recomendo "*Taproot*" ou, se não for possível, "*Native SegWit*".



![Image](assets/fr/32.webp)



Clique no botão "*Connected Hardware Wallet*". O seu Safe 5 deve, obviamente, estar ligado ao computador e desbloqueado.



Quando ligar o Safe 5 a um computador com o Sparrow Wallet aberto, ser-lhe-á pedido que introduza um BIP39 passphrase no ecrã Hardware Wallet. Esta opção avançada será abordada num futuro tutorial. Por agora, pode simplesmente clicar no visto Green no canto superior direito para confirmar que pretende utilizar um passphrase vazio (ou seja, sem um passphrase). Para evitar que o Trezor lhe peça para introduzir um passphrase sempre que arranca, vá ao Trezor Suite, aceda às definições e altere a opção em "*Device*" > "*Wallet default*" para "*Standard*" em vez de "*passphrase*".



![Image](assets/fr/33.webp)



Clique no botão "*Scan*". O seu Safe 5 deve aparecer. Clique em "*Importar armazenamento de chaves*".



![Image](assets/fr/34.webp)



Pode agora ver os detalhes do seu Wallet, incluindo a chave pública alargada da sua primeira conta. Clique no botão "*Apply*" (Aplicar) para finalizar a criação do Wallet.



![Image](assets/fr/35.webp)



Escolha uma palavra-passe forte para proteger o acesso ao Sparrow Wallet. Esta palavra-passe garantirá o acesso seguro aos dados do Sparrow Wallet, protegendo as suas chaves públicas, endereços, etiquetas e histórico de transacções contra o acesso não autorizado.



Aconselho-o a guardar esta palavra-passe num gestor de palavras-passe para não se esquecer dela.



![Image](assets/fr/36.webp)



E agora a sua carteira foi importada para o Sparrow Wallet!



![Image](assets/fr/37.webp)



Antes de receber as suas primeiras bitcoins no seu Wallet, **aconselho-o vivamente a efetuar um teste de recuperação vazio**. Anote algumas informações de referência, como o seu xpub, depois reinicie o seu Trezor Safe 5 enquanto o Wallet ainda está vazio. Em seguida, tente restaurar o Wallet no Trezor utilizando as suas cópias de segurança em papel. Verifique se o xpub gerado após o restauro corresponde ao que escreveu originalmente. Se corresponder, pode ter a certeza de que as suas cópias de segurança em papel são fiáveis.



Para saber mais sobre como efetuar um teste de recuperação, sugiro que consulte este outro tutorial:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Como posso receber bitcoins com o Trezor Safe 5?



No Sparrow, clique no separador "*Receber*".



![Image](assets/fr/38.webp)



Antes de utilizar o Address proposto pelo Sparrow Wallet, verifique-o no ecrã do seu Trezor. Esta prática permite-lhe confirmar que o Address apresentado no Sparrow não é fraudulento e que o Hardware Wallet detém efetivamente a chave privada necessária para gastar posteriormente os bitcoins garantidos com este Address. Isto ajuda-o a evitar vários tipos de ataques.



Para efetuar esta verificação, clicar no botão "*Display Address*".



![Image](assets/fr/39.webp)



Verifique se o Address que aparece no seu Trezor corresponde ao Wallet do Sparrow. É também aconselhável efetuar esta verificação imediatamente antes de comunicar o seu Address ao remetente, para ter a certeza da sua validade. Pode premir o ecrã para confirmar.



![Image](assets/fr/40.webp)



Pode então adicionar um "*Label*" para descrever a fonte de bitcoins que será protegida com este Address. Esta é uma boa prática que te permite gerir melhor os teus UTXOs.



![Image](assets/fr/41.webp)



Pode então utilizar este Address para receber bitcoins.



![Image](assets/fr/42.webp)



## Como é que envio bitcoins com o Trezor Safe 5?



Agora que já recebeu os seus primeiros Satss no seu Wallet protegido por Safe 5, também os pode gastar! Ligue o Trezor ao seu computador, desbloqueie-o com o código PIN, inicie o Sparrow Wallet e vá ao separador "*Enviar*" para criar uma nova transação.



![Image](assets/fr/43.webp)



Se pretender *Controlar as moedas*, ou seja, escolher especificamente os UTXOs a consumir na transação, vá ao separador "*UTXOs*". Selecione os UTXOs que pretende gastar e, em seguida, clique em "*Enviar selecionados*". Será redireccionado para o mesmo ecrã no separador "*Enviar*", mas com os seus UTXOs já selecionados para a transação.



![Image](assets/fr/44.webp)



Introduzir o Address de destino. Também pode introduzir vários endereços clicando no botão "*+ Adicionar*".



![Image](assets/fr/45.webp)



Escreva um "*Rótulo*" para se lembrar do objetivo desta despesa.



![Image](assets/fr/46.webp)



Selecionar o montante a enviar para este Address.



![Image](assets/fr/47.webp)



Ajuste a taxa da sua transação de acordo com o mercado atual. Por exemplo, pode utilizar [Mempool.space] (https://Mempool.space/) para escolher uma taxa de comissão adequada.



Certifique-se de que todos os parâmetros da transação estão corretos e, em seguida, clique em "*Criar transação*".



![Image](assets/fr/48.webp)



Se tudo estiver a seu gosto, clique em "*Finalizar transação para assinatura*".



![Image](assets/fr/49.webp)



Clique em "*Assinar*".



![Image](assets/fr/50.webp)



Clique em "*Sign*" junto ao seu Trezor Safe 5.



![Image](assets/fr/51.webp)



Verifique os parâmetros da transação no ecrã do seu Hardware Wallet, incluindo o Address do destinatário, o montante enviado e o débito. Quando a transação tiver sido verificada no Trezor, prima e mantenha premido o ecrã para a assinar.



![Image](assets/fr/52.webp)



A sua transação está agora assinada. Verifique uma última vez se está tudo bem e, em seguida, clique em "*Broadcast Transaction*" para a transmitir na rede Bitcoin.



![Image](assets/fr/53.webp)



Pode encontrá-lo no separador "*Transacções*" do Sparrow Wallet.



![Image](assets/fr/54.webp)



Parabéns, está agora a par da utilização básica do Trezor Safe 5 com o Sparrow Wallet! Para dar um passo em frente, recomendo este tutorial completo sobre a utilização de um Trezor Hardware Wallet com um passphrase BIP39 para aumentar a sua segurança:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Se achou este tutorial útil, agradecia que deixasse um polegar Green abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!