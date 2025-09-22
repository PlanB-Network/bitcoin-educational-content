---
name: Nunchuk
description: Wallet móvel adequado para todos
---
![cover](assets/cover.webp)



## Um poderoso Wallet


O Nunchuk chegou no final de 2020 com uma filosofia clara: tornar a multi-assinatura um padrão. Por conseguinte, foi concebido para executar funções muito avançadas, com a valiosa escolha de construir o design diretamente no Bitcoin Core, o software de referência para o ecossistema Bitcoin.



Após mais de 4 anos de desenvolvimento e utilização, está pronto para ser experimentado em grande escala. Se é um principiante e não está familiarizado com o Nunchuk, este guia ajudá-lo-á a dar os primeiros passos e a descobrir este software, cujas funções avançadas poderá conhecer depois de ultrapassar o primeiro impacto. O tutorial em si é dedicado aos utilizadores intermédios que possuem as competências necessárias para seguir todas as etapas, mas pode servir de inspiração para que todos descubram como aumentar as suas competências. Começaremos com a versão móvel, e este apontamento é necessário, uma vez que o Nunchuk tem o software para correr também em computadores.



## Descarregar


O primeiro passo é, sem dúvida, decidir onde descarregar a aplicação. Vá ao [site oficial] (https://nunchuk.io/) onde pode encontrar alguma documentação (não é muito, mas é um começo), a apresentação das funcionalidades, bem como, no final da página, todas as ligações de transferência.



para este tutorial, decidi mostrar como baixar o Software Wallet do repositório do Github e como verificar a versão antes de instalá-lo no seu celular. **O procedimento a seguir só pode ser feito a partir do seu computador**, então eu recomendo que você faça todos esses passos a partir do seu desktop ou laptop e - depois de todas as verificações - transfira o arquivo `.apk` para o seu celular.



![image](assets/en/01.webp)



Se os seus conhecimentos não forem muito avançados, pode decidir descarregar o `.apk` das lojas oficiais e passar diretamente para a parte de configuração deste tutorial. Se, por outro lado, quiseres dar o salto, continua a seguir passo a passo.



Assim, a partir do seu computador de secretária, clique em _Visitar o nosso repositório de código aberto_



O link levá-lo-á à página do Github do Nunchuk, onde encontrará vários repositórios. Vamos concentrar-nos no _nunchuk-android_



![image](assets/en/02.webp)



No ecrã seguinte, localize à direita a secção _Releases_ e selecione _Latest_



![image](assets/en/03.webp)



Em _Assets_, transfira a versão (neste exemplo, 1.67.apk), juntamente com o ficheiro SHA256SUMS e SHA256SUMS.asc.



![image](assets/en/04.webp)



Para encontrar a chave GPG do programador, volte à secção _Releases_ do repositório e procure a versão 1.9.53 (ou anterior) que contém a ligação para obter e transferir a _GPG Key_



![image](assets/en/05.webp)



Vamos proceder à verificação através de uma ferramenta prática oferecida pelo Sparrow wallet, que tem uma janela dedicada para este efeito e suporta assinaturas PGP e Manifestos SHA256.



Em seguida, inicie o Sparrow e, no menu _Tools_, selecione _Verify Download_.



![image](assets/en/06.webp)



Na janela que aparece, encontrará campos para "preencher": escolha o botão _Browse_ à direita e selecione, para cada campo, os ficheiros correspondentes que acabou de descarregar do Github. Quando tiver concluído todas as etapas, a janela terá o seguinte aspeto, com as marcas de verificação Green e a confirmação Hash do manifesto.



![image](assets/en/07.webp)


**A captura de ecrã é de um PC com Windows, a mesma prática pode ser utilizada em qualquer sistema operativo no seu computador, basta ter o Sparrow wallet instalado. E verificado!**



Pode encontrar o guia do Sparrow wallet para descarregar este Software Wallet


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Pode então transferir o ficheiro `.apk` do seu computador para o seu telemóvel



![image](assets/en/08.webp)



e instalar o Nunchuk



![image](assets/en/09.webp)



Antes de lançar o Nunchuk no seu telefone, abra o Orbot e coloque o recém-chegado na lista de aplicações a serem encaminhadas pelo Tor.



![image](assets/en/11.webp)



Agora, execute o Nunchuk. Para as funcionalidades do projeto - que não são o assunto deste tutorial - o Nunchuk, uma vez aberto, convidá-lo-á a iniciar sessão através de um e-mail ou perfil Google. Até que planeie tirar partido dos planos avançados da Nunchuk Inc, **evite iniciar sessão** e prossiga escolhendo a opção _Continuar como convidado_.



![image](assets/en/12.webp)



## Definições


O Nunchuk apresenta-se com uma janela de apresentação _Home_, onde é fácil compreender a sua filosofia de funcionamento e sobre a qual nos debruçaremos de seguida.



Na parte inferior, encontram-se os menus e, como primeiro passo, escolha _Profile_ para aceder às definições.



![image](assets/en/10.webp)



Em seguida, selecione _Configurações de visualização_, continuando a ignorar o convite para criar uma conta.



![image](assets/en/14.webp)



No ecrã que se segue, pode verificar se o Wallet está em linha e pode ligar o seu servidor, prestando muita atenção às instruções da ligação que lhe é oferecida clicando em _este guia_.



![image](assets/en/15.webp)



Guardar as definições com o comando _Guardar definições de rede_, voltar ao menu _Perfil_ e selecionar _Definições de segurança_.



![image](assets/en/16.webp)



A partir deste menu, define como defender a abertura da aplicação. Para evitar acessos indesejados, pode proteger o Nunchuk com a biometria do telemóvel e/ou adicionar um PIN de segurança.



![image](assets/en/17.webp)



Consulte também o menu _About_, que se encontra sempre na janela _Profile_



![image](assets/en/18.webp)



que lhe permitirá verificar a versão da aplicação ou contactar os criadores, se necessário.



![image](assets/en/19.webp)



## Geração de chaves e Wallet


Como é fácil de adivinhar a partir da filosofia do Nunchuk, o software destina-se a ser uma ferramenta útil para gerir carteiras com várias assinaturas. Para realizar esta função, o Nunchuk permite a criação de Wallet, separando-os das chaves necessárias para organizar as assinaturas digitais.



De facto, o funcionamento ideal do Nunchuk passa pela criação de Carteiras que podem ser só de relógio, dependentes de chaves que podem ser "Frias"



Nos ecrãs anteriores deves ter reparado que existe um menu na parte inferior chamado _Keys_. Se acabaste de descarregar o Nunchuk, tanto em _Home_ como em _Keys_ verás um grande botão que te convida a adicionar uma tecla, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**É assim que o Nunchuk funciona:** primeiro, o generate/importa as chaves e, em seguida, cria o Wallet, configurando-o para escolher quais as chaves que autorizam o desbloqueio dos fundos nele armazenados.



Mesmo no caso do Wallet singlesig, cria-se primeiro a chave e só depois o Wallet. E é exatamente isso que vamos fazer agora, começando com um Wallet singlesig para quebrar o gelo e descobrir as funções do Nunchuk.



Clique em _Adicionar chave_



![image](assets/en/22.webp)



O Nunchuk mostra uma série de dispositivos de assinatura suportados mas, para começar, selecione _Software_.



![image](assets/en/23.webp)



O matraquilho irá criar um generate que será guardado no dispositivo. De seguida, é necessário escrever a sequência de palavras para a cópia de segurança, criando as melhores condições ambientais e certificando-se de que tem tempo para o fazer bem e em silêncio. O software mostra o Mnemonic apenas uma vez, quer opte por mostrá-lo agora ou mais tarde, por isso escolha _Criar e fazer a cópia de segurança agora_.



![image](assets/en/24.webp)



O Nunchuk gera frases Mnemonic de 24 palavras, que aparecem imediatamente no ecrã seguinte



![image](assets/en/25.webp)



e, em seguida, procedeu a uma verificação rápida, pedindo-lhe para selecionar a palavra correta, de entre 3 opções, correspondente ao número na sequência Mnemonic.


Se tiver escrito o Mnemonic corretamente, o botão _Continuar_ fica operacional. Prima-o para continuar.



![image](assets/en/26.webp)



Dê um nome à sua tecla e prima _Continuar_.



![image](assets/en/27.webp)



No final destes passos, ser-lhe-á perguntado se quer adicionar um [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39) à sua frase Mnemonic. Se não tiver o conhecimento necessário sobre como utilizar o passphrase, organizar o seu backup ou como funciona, recomendo que escolha _Não preciso de uma frase-passe_.



![image](assets/en/28.webp)



A chave é finalmente criada e é-lhe apresentada no menu:




- Com _Key Spec_ é indicada a impressão digital principal
- Tem definições, os três pontos no canto superior direito, onde pode apagar a chave ou assinar uma mensagem
- Ao lado do nome da chave, encontrará um ícone de ponta, clicando no qual pode editar o nome da chave, por exemplo, para manter as suas chaves em ordem no futuro.
- Como último comando, pode verificar o estado de saúde da chave: premindo _Executar verificação de saúde_, pode fazer com que a aplicação verifique se uma chave está comprometida.



Quando estiver tudo pronto, clique em _Done_



![image](assets/en/29.webp)



No menu _Teclas_ verá aparecer a sua primeira tecla.



![image](assets/en/30.webp)



Ao aceder ao menu _Home_, aparece a opção de criar Wallet. Clique em _Criar nova carteira_.



![image](assets/en/31.webp)



O Nunchuk mostra-lhe uma série de possibilidades que têm a ver, na sua maioria, com serviços que a empresa oferece e que não são objeto deste tutorial.



Neste guia, vamos criar uma _Hot Wallet e uma _Custom wallet_ detalhando os pormenores.


Comecemos pela _Carteira personalizada_.



![image](assets/en/32.webp)



De uma forma simples, a aplicação pedir-lhe-á que dê um nome a este novo Wallet e que escolha o script para os endereços. Para o tutorial, optei por deixar a configuração padrão, _Native segwit_. Quando tiveres terminado, escolhe _Continuar_



![image](assets/en/33.webp)



A configuração do Wallet pede-lhe que defina com que chave os fundos deste Wallet serão desbloqueados. Se existirem várias chaves, ser-lhe-á apresentada uma lista para escolher. De momento, criámos apenas uma, pelo que optámos por colocar uma marca de verificação nessa chave. No canto inferior direito, podes ver como a Nunchuk te pedirá para configurares as tuas futuras assinaturas múltiplas do Wallet, aumentando o número de _Chaves necessárias_.



![image](assets/en/34.webp)



Como estamos a criar um singlesig, deixamos `1` e clicamos em _Continuar_.



Por último, aparece um ecrã de verificação, onde pode verificar as caraterísticas do Wallet:




- o nome
- o `1/1 Multisig` tage, que é como a Nunchuk nomeia o Wallet singlesig
- o tipo de script, `Native SegWit`
- a chave `Keys`, com a sua impressão digital e caminho de derivação



Quando estiver satisfeito, prima _Criar carteira_



![image](assets/en/35.webp)



O Wallet foi criado e pode descarregar o ficheiro [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) como cópia de segurança. Para voltar ao menu principal, clique na seta no canto superior esquerdo.



![image](assets/en/36.webp)



Encontra-se em _Home_, onde é apresentado o Wallet recém-criado, que indica o saldo e o estado da ligação. Ao clicar no espaço azul, pode aceder às principais funções do Wallet.



![image](assets/en/37.webp)





- O ícone da lente no canto superior direito permite-lhe fazer uma pesquisa de transacções;
- `View Wallet config` dá acesso ao menu de configuração, onde pode editar o nome do Wallet e ativar as opções avançadas, no canto superior direito (das quais não é possível obter screenshots). Aqui pode exportar a configuração do Wallet, etiquetas, substituir teclas, alterar o [gap limit] (https://planb.network/en/resources/glossary/gap-limit) e mais.



## Transacções com o Nunchuk



Prémios _Receber_



![image](assets/en/38.webp)



A aplicação está programada para mostrar o código QR do Address ou copiar/partilhar o scriptPubKey para receber fundos onchain.



![image](assets/en/39.webp)



Tivemos um UTXO a chegar a este primeiro Address,



![image](assets/en/40.webp)



mas continuamos a clicar em _Receive_ para receber outro.



![image](assets/en/41.webp)



O objetivo é que descubras que o Nunchuk te reporta este novo Address como um _endereço não utilizado_ mas também te mostra que tens _endereços utilizados_ e a sua contagem.



### Transação de despesas com controlo de moedas



Quando este segundo UTXO também tiver chegado, volte ao ecrã principal do Wallet para verificar o estado das duas transacções recebidas e, mais importante, clique na opção _Ver moedas_



![image](assets/en/42.webp)



onde lhe serão mostrados UTXOs individuais. Aqui pode optar por ver um em particular, clicando na pequena seta junto ao montante



![image](assets/en/43.webp)



e verificar quando chegou, a descrição, bloquear o UTXO para que não seja gasto e muito mais.



![image](assets/en/44.webp)



Mas se voltares ao menu _Coins_ clicando na seta no canto superior direito, podes ativar o "Coin Control" para gastares os teus UTXOs de uma forma mais controlada.



No exemplo seguinte, optei por selecionar UTXO de 21.000 Sats e, em seguida, clicar no símbolo no canto inferior esquerdo.



![image](assets/en/45.webp)



O Nunchuk abre automaticamente a janela _Nova transacção_ para gastar este UTXO. Na transação de gasto, em primeiro lugar, é preciso definir o montante manualmente ou selecionando _Enviar tudo seleccionado_ para enviar todo o saldo do controlo de moedas, sem gerar restos. Uma vez definido o montante, selecionar _Continuar_



![image](assets/en/46.webp)



Agora o Nunchuk mostra onde colar o Address para o qual transferir estes fundos, detalhar uma descrição e finalizar a transação.



![image](assets/en/47.webp)



A escolha de _Criar transacção_ delega a gestão automática de taxas e transacções na aplicação. Recomendo que escolha _Custom transaction_ para ter mais controlo.



Neste novo ecrã, é importante selecionar




- _Subtrair a taxa do montante enviado_, para evitar que as taxas sejam pagas por outro UTXO presente no Wallet, gastando-as e gerando um resto (o que constitui uma perda de privacidade evitável);
- e, em seguida, definir as taxas manualmente depois de verificar no explorador.



Depois de ter efectuado todos estes passos, clique em _Continuar_



![image](assets/en/48.webp)



O ecrã seguinte apresenta o resumo completo da transação. Se tudo estiver bem, confirme selecionando _Confirmar e criar transacção_.



![image](assets/en/49.webp)



Com _Assinaturas pendentes_, o Nunchuk avisa-o de que a transacçãop está à espera da sua assinatura para aprovar a despesa, que apõe clicando em _Assinar_.



![image](assets/en/50.webp)



O comando _Broadcast_ aparece na parte inferior para propagar a transação finalizada e assinada.



![image](assets/en/51.webp)



### Transação de despesas a partir do menu _Enviar_



Enquanto na página principal do Wallet vemos a transação a sair e a aguardar confirmação, utilizamos o menu _Send_ para simular uma despesa diária.



![image](assets/en/52.webp)



Com efeito, ao clicar em _Enviar_, aparece o ecrã de envio da transação, que é idêntico ao que acabamos de ver, mas sem passar pelo controlo das moedas.



Também neste segundo exemplo decidi selecionar _Custom transaction_ e enviar o montante total, mas poderia tê-lo definido manualmente. Quando tiver decidido o montante a enviar, prima _Continuar_.



![image](assets/en/53.webp)



Em seguida, verifique sempre se as taxas são subtraídas do UTXO em questão (neste exemplo, a escolha é forçada, porque só há um), ajuste manualmente as taxas de acordo com a situação no momento no Mempool e prima _Continuar_.



![image](assets/en/54.webp)



Se o ecrã de resumo for satisfatório, selecionar _Confirmar e criar a transacção_.



![image](assets/en/55.webp)



Assinar a transação com _Sign_



![image](assets/en/56.webp)



e propagá-lo para a rede.



![image](assets/en/57.webp)



O Wallet encontra-se neste momento com o saldo a zero e o histórico a ser atualizado.



![image](assets/en/58.webp)



## Criação de um "Hot Wallet"



Por último, e para não deixar de fora nada das fases iniciais do Nunchuk mobile, vamos ver como isto cria o que a aplicação chama "Hot Wallet"



No menu _Home_ do Nunchuk, onde aparece a lista de carteiras, clica no `+` no canto superior direito.



![image](assets/en/59.webp)



Selecionar _Hot wallet_ entre as opções



![image](assets/en/60.webp)



A matraca dá alguns conselhos sobre o manuseamento das carteiras Hot na página de apresentação, onde deves selecionar _Continuar_ para prosseguir.



![image](assets/en/61.webp)



Após alguns momentos, o Wallet é criado e aparece na lista com uma cor acastanhada. Esta é a cor com que o Nunchuk o alerta de que ainda não efectuou o backup do Wallet.



![image](assets/en/62.webp)



Clique no nome do Wallet, para aceder às suas configurações, e poderá ver um convite para fazer imediatamente uma cópia de segurança da frase do Mnemonic.



![image](assets/en/63.webp)



O procedimento é o mesmo que já vimos antes, por isso não o vamos repetir. Uma vez terminado, o Nunchuk leva-o para a página da chave relevante, que pode editar como a que criou com o procedimento _Custom_.



![image](assets/en/64.webp)



Tente também _Executar exame de saúde_



![image](assets/en/65.webp)



ou para ver como apresentar todas as suas Carteiras no _Home_ da aplicação.



![image](assets/en/66.webp)



## A ter em mente para continuar de forma independente


Tal como existe uma ordem para a criação, ou seja, primeiro gerar as chaves e depois o Wallet, terá de manter a ordem inversa para eliminar estes itens da sua aplicação.



Se precisar de apagar uma das chaves, deve primeiro ter a precaução de apagar o Wallet, ou as Carteiras, que utilizam uma das chaves de assinatura para as transacções: primeiro apague as Carteiras e só depois as chaves. Se não seguir esta ordem, não conseguirá remover a chave.



Agora que já sabe como começar a utilizar o Nunchuk, pode continuar a estudar esta aplicação e descobrir os seus segredos. Neste tutorial, demos apenas os primeiros passos, mas há aplicações mais sofisticadas e necessidades avançadas que este Software Wallet pode ajudar a satisfazer.