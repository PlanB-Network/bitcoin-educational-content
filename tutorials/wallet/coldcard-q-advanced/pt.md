---
name: COLDCARD Q - Avançado
description: Utilizar as opções avançadas do COLDCARD Q
---
![cover](assets/cover.webp)

Num tutorial anterior, abordámos a configuração inicial do COLDCARD Q e as suas funções básicas para principiantes. Se acabou de receber o seu COLDCARD Q e ainda não o configurou, recomendo que comece por esse tutorial antes de continuar aqui:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
Este novo tutorial é dedicado às opções avançadas do COLDCARD Q, concebido para utilizadores avançados e paranóicos. De facto, os COLDCARDs distinguem-se de outras carteiras de hardware pelas suas muitas caraterísticas de segurança avançadas. Naturalmente, não é necessário utilizar todas estas opções. Basta escolher as que se adequam à sua estratégia de segurança.

**Aviso**, a utilização incorrecta de algumas destas opções avançadas pode resultar na perda dos seus bitcoins ou na destruição da sua carteira de hardware. Por isso, recomendo vivamente que leia atentamente os conselhos e explicações de cada opção.

Antes de começar, certifique-se de que tem acesso a uma cópia de segurança física da sua frase mnemónica de 12 ou 24 palavras e verifique a sua validade através do seguinte menu: `Avançado/Ferramentas > Zona de Perigo > Funções de Semente > Ver Palavras de Semente`.

![CCQ](assets/fr/01.webp)

## A frase-passe BIP39

Se não sabe o que é uma frase-chave BIP39 ou se não sabe muito bem como funciona, recomendo vivamente que consulte previamente este tutorial, que cobre as bases teóricas necessárias para compreender os riscos associados à utilização de uma frase-chave:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Tenha em atenção que, depois de definir a frase-chave na sua carteira, a mnemónica não será suficiente para recuperar o acesso aos seus bitcoins. É necessário tanto a mnemónica como a frase-chave. Além disso, terá de introduzir a frase-chave de cada vez que desbloquear o seu COLDCARD Q. Isto aumenta a segurança ao tornar o acesso físico ao COLDCARD e o conhecimento do PIN insuficientes sem a frase-chave.

Nos COLDCARDs, tem duas opções para gerir a sua frase-chave:

1. **Entrada clássica:** Introduz a frase-chave manualmente sempre que utiliza a carteira de hardware, tal como faz com outras carteiras de hardware. COLDCARD Q simplifica esta tarefa com o seu teclado completo.

2. **Pode optar por encriptar a sua frase-chave e guardá-la num cartão microSD. Neste caso, terá de inserir o microSD no COLDCARD Q sempre que o utilizar. Note que este microSD só funcionará no seu COLDCARD Q e não é uma cópia de segurança. Por isso, é muito importante que guarde também uma cópia da sua frase-chave num suporte físico, como papel ou metal.

Para definir a sua frase-chave BIP39, aceda ao menu "*Frase-chave*".

![CCQ](assets/fr/02.webp)

Introduza a sua frase-chave utilizando o teclado. Certifique-se de que escolhe uma frase-chave forte (longa e aleatória) e faça uma cópia de segurança física.

![CCQ](assets/fr/03.webp)

Depois de definir a sua frase-chave, COLDCARD Q mostrar-lhe-á a impressão digital da chave mestra da nova carteira associada a esta frase-chave. Não se esqueça de guardar esta impressão digital. Quando voltar a introduzir a frase-chave quando utilizar o dispositivo no futuro, poderá verificar se a impressão digital apresentada corresponde à que guardou. Esta verificação garante que não cometeu um erro ao introduzir a frase-chave.

![CCQ](assets/fr/04.webp)

Pode agora premir "*ENTER*" para aplicar esta frase-chave à sua frase mnemónica e ativar a nova carteira. Se preferir guardar esta frase-chave num microSD, insira o cartão na ranhura adequada e prima "*1*".

![CCQ](assets/fr/05.webp)

A sua frase-chave está agora aplicada. A impressão da chave aparece no ecrã inicial e na parte superior do ecrã.

![CCQ](assets/fr/06.webp)

Cada vez que desbloquear o seu COLDCARD Q, terá de aceder ao menu "*Passphrase*" e introduzir a sua frase-chave da mesma forma que acima, para a aplicar à mnemónica armazenada no dispositivo e aceder à carteira Bitcoin correta.

![CCQ](assets/fr/07.webp)

Se guardou a frase-chave num cartão microSD, de cada vez que o utilizar, insira-o no COLDCARD e aceda ao menu "*Passphrase*". O seu COLDCARD carregará a frase-chave diretamente do microSD, pelo que não terá de a introduzir manualmente. Clique em "*Restore Saved*".

![CCQ](assets/fr/08.webp)

Verifique se o comprimento e a primeira letra da frase-chave carregada estão corretos.

![CCQ](assets/fr/09.webp)

Confirme que a impressão digital apresentada corresponde à da sua carteira e clique em "*Restore*".

![CCQ](assets/fr/10.webp)

Tenha em atenção que utilizar uma frase-chave significa que terá de importar um novo conjunto de chaves derivadas da combinação da sua frase mnemónica e da frase-chave para o seu software de gestão de carteiras (como a Sparrow Wallet). Para o fazer, siga o passo "*Configurar uma nova carteira no Sparrow*" neste outro tutorial :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
## Opções de desbloqueio

Os COLDCARDs também beneficiam de uma série de opções para o processo de desbloqueio do dispositivo. Vamos saber mais sobre estas opções avançadas.

### PINs de truque

Um Trick PIN é um código PIN secundário distinto daquele definido durante a configuração inicial do dispositivo. Este código é utilizado para desencadear acções específicas pré-configuradas assim que é introduzido quando o COLDCARD é ligado. É possível configurar vários Trick PINs, cada um associado a uma ação diferente. Estas caraterísticas permitem-lhe adaptar o seu COLDCARD à sua estratégia de segurança pessoal. São particularmente úteis em casos de coação física, como durante um assalto (normalmente referido na comunidade Bitcoin como um "*$5 wrench attack*").

Para ativar um Trick PIN e associá-lo a uma ação, aceda ao menu `Definições > Definições de início de sessão > Trick PINs`.

![CCQ](assets/fr/11.webp)

Selecionar "*Adicionar novo truque*".

![CCQ](assets/fr/12.webp)

Defina o código PIN a associar à ação e não se esqueça de o guardar.

![CCQ](assets/fr/13.webp)

Em seguida, escolha a ação a executar automaticamente sempre que introduzir este PIN de truque. Aqui está a lista de acções disponíveis para um PIN:


- "*Brick Self*: Esta ação destrói os dois chips COLDCARD Q se o PIN Trick for introduzido, tornando o dispositivo totalmente inutilizável. Será então impossível revender, reutilizar ou mesmo devolvê-lo à Coinkite. O dispositivo tornar-se-á irremediavelmente obsoleto. Esta funcionalidade pode ser utilizada em caso de roubo para convencer o assaltante de que nunca conseguirá aceder aos seus bitcoins. **Atenção**: sem uma cópia de segurança física da sua frase mnemónica e de qualquer frase-passe, os seus bitcoins ficarão permanentemente perdidos.

![CCQ](assets/fr/14.webp)


- "*Wipe Seed*": Este menu propõe várias acções para apagar a semente, ou seja, reiniciar o COLDCARD sem o destruir. Ao contrário da opção "*Brick Self*", será possível reconfigurar o dispositivo utilizando um backup da sua frase mnemónica. No entanto, sem esta cópia de segurança, os teus bitcoins perder-se-ão. Aqui estão as opções disponíveis:
 - "*Wipe & Reboot* : Remove a semente e reinicia a COLDCARD sem apresentar qualquer informação no ecrã.
 - "*Silent Wipe*": Limpa silenciosamente a semente e desbloqueia o COLDCARD numa carteira falsa aleatória como se nada tivesse acontecido.
 - "*Wipe -> Wallet*": Remove a semente discretamente e desbloqueia o COLDCARD numa carteira secundária pré-configurada, concebida como um isco. Essa carteira pode conter uma pequena parte da sua poupança de bitcoin para satisfazer um atacante.
 - "*Sementes Apagadas, Parar*": Apaga a semente e apresenta no ecrã a mensagem "Semente apagada, Stop".

![CCQ](assets/fr/15.webp)


- "*Carteira de Perseguição*": Com esta ação, o código PIN do Trick desbloqueia uma carteira derivada da semente utilizando o BIP85. Esta carteira secundária pode ser utilizada como isco para satisfazer um atacante. O COLDCARD actua como se fosse a carteira real, mas sem o PIN mestre (diferente do Trick PIN), o atacante nunca conseguirá aceder à carteira real. Esta estratégia foi concebida para fazer as pessoas acreditarem que a carteira associada ao Trick PIN é a única que existe.

![CCQ](assets/fr/16.webp)


- "*Contagem decrescente do início de sessão*": Este menu agrupa acções com uma contagem decrescente antes de serem executadas. **Aviso**, algumas delas podem destruir o teu dispositivo ou resultar na perda dos teus bitcoins. Aqui estão as sub-acções disponíveis:
 - "*Wipe & Countdown* : Limpa a semente da memória do COLDCARD e depois inicia uma contagem decrescente de uma hora. Sem guardar a mnemónica ou a frase-chave, os seus bitcoins serão perdidos. Esta opção foi concebida para enganar um atacante, levando-o a pensar que o dispositivo será desbloqueado no final da contagem decrescente, quando na realidade será reposto para as definições de fábrica.
 - "*Countdown & Brick*": Inicia uma contagem decrescente de uma hora, no final da qual o COLDCARD destrói os seus dois chips seguros, tornando-o permanentemente inutilizável. Sem backup, seus bitcoins serão perdidos. Esta ação foi concebida para enganar um atacante, que pensa que está à espera de um desbloqueio, quando na realidade o dispositivo se autodestrói.
 - "*Just Countdown* : Desencadeia uma contagem decrescente simples de uma hora, após a qual o COLDCARD é reiniciado sem qualquer outra ação. A semente não é eliminada e o dispositivo permanece intacto. Tenha cuidado para não confundir esta ação com a opção "*Login Countdown*", discutida nas secções seguintes, que adiciona uma contagem decrescente ao PIN principal enquanto dá acesso à carteira real.

![CCQ](assets/fr/17.webp)


- "*Olhar em branco*": Esta ação faz com que o COLDCARD pareça vazio, dando a impressão de que a semente foi eliminada. Na realidade, nada acontece e a semente permanece intacta. Esta ação simula um COLDCARD não utilizado ou reposto.

![CCQ](assets/fr/18.webp)


- "*Just Reboot* : Quando o Trick PIN é utilizado, o COLDCARD é simplesmente reiniciado. Não é executada qualquer outra ação.

![CCQ](assets/fr/19.webp)


- "*Delta Mode*": Esta ação complexa, reservada a utilizadores experientes, foi concebida para contrariar ataques de coação altamente sofisticados, provenientes de um Estado ou de um familiar com informação privilegiada. Quando o Modo Delta é ativado, COLDCARD dá acesso à carteira real, permitindo a um atacante navegar e verificar se é a carteira correta. No entanto, as assinaturas das transacções são bloqueadas, impedindo assim qualquer transferência de bitcoin. Além disso, o acesso à frase mnemónica é desativado e qualquer tentativa de a recuperar resultará na sua eliminação. Para aumentar a credibilidade, o Trick PIN utilizado com o Delta Mode deve partilhar o mesmo prefixo que o PIN real (para apresentar as mesmas palavras anti-phishing), mas o sufixo deve ser diferente.

![CCQ](assets/fr/20.webp)

Depois de ter selecionado uma ação, confirme a sua escolha.

![CCQ](assets/fr/21.webp)

Pode então visualizar todos os Trick PINs configurados no menu dedicado.

![CCQ](assets/fr/22.webp)

Ao selecionar um PIN de Truque existente, pode verificar a ação associada. Também pode ocultá-lo com "*Ocultar truque*", tornando-o invisível no menu PIN do truque. Pode apagá-lo clicando em "*Apagar Truque*" ou alterar o código PIN, mantendo a ação associada, com "*Alterar PIN*".

![CCQ](assets/fr/23.webp)

A opção "*Adicionar se errado*", disponível no menu "*Trick PIN*", permite-lhe configurar uma ação específica que é automaticamente desencadeada após um determinado número de tentativas incorrectas de introdução do código PIN mestre. O número de tentativas permitidas pode ser definido durante a configuração.

### Chaves de embaralhamento

A opção de codificação das teclas permite-lhe codificar os dígitos apresentados nos botões do teclado quando introduz o seu código PIN. Esta função protege a confidencialidade do seu código PIN, mesmo em caso de vigilância por pessoas ou câmaras.

Para ativar esta opção, aceda ao menu `Definições > Definições de início de sessão > Teclas de codificação`.

![CCQ](assets/fr/24.webp)

Selecionar a opção "*Chaves de codificação*".

![CCQ](assets/fr/25.webp)

A partir de agora, quando desbloquear o seu COLDCARD Q, serão atribuídos novos números às teclas do teclado, de forma aleatória, sempre que as utilizar.

![CCQ](assets/fr/26.webp)

### Contagem decrescente do início de sessão

Esta opção permite-lhe impor uma contagem decrescente sistemática de cada vez que tenta desbloquear o seu COLDCARD. Pode ser integrada na sua estratégia de segurança, atrasando o acesso ao dispositivo em caso de roubo ou impondo um atraso antes de assinar uma transação, por exemplo, para se proteger em caso de assalto. No entanto, esta contagem decrescente aplica-se a todas as suas utilizações, incluindo quando está a utilizar legitimamente o seu COLDCARD, o que também o obriga a ser paciente. Atenção para não confundir esta opção com a ação "*Contar regressivamente*", que só é activada quando é utilizado um Trick PIN específico.

Para configurar esta opção, aceda ao menu `Definições > Definições de início de sessão > Contagem decrescente de início de sessão`.

![CCQ](assets/fr/27.webp)

Selecionar o tempo de contagem decrescente. Por exemplo, se selecionar 1 hora, terá de esperar 1 hora por cada tentativa de desbloqueio do COLDCARD Q.

![CCQ](assets/fr/28.webp)

Sempre que desbloquear, ser-lhe-á pedido que introduza o seu código PIN.

![CCQ](assets/fr/29.webp)

Em seguida, aguarde o tempo definido pela contagem decrescente.

![CCQ](assets/fr/30.webp)

No final da contagem decrescente, terá de introduzir novamente o seu PIN para aceder ao dispositivo.

![CCQ](assets/fr/31.webp)

### Login da calculadora

Esta opção permite-lhe disfarçar o seu COLDCARD de calculadora aquando do desbloqueio. Para ativar esta função, aceda ao menu `Configurações > Configurações de início de sessão > Início de sessão da calculadora`.

![CCQ](assets/fr/32.webp)

Ativar a opção selecionando-a.

![CCQ](assets/fr/33.webp)

A partir de agora, sempre que o dispositivo for ligado, será apresentada uma calculadora funcional com comandos básicos.

![CCQ](assets/fr/34.webp)

Por exemplo, pode calcular o hash SHA256 de "*Rede do Plano B*".

![CCQ](assets/fr/35.webp)

Para desbloquear o COLDCARD a partir do modo calculadora, comece por introduzir o prefixo do seu código PIN seguido de um traço. Por exemplo, se o seu código PIN for `00-00` (este código é fraco e apenas um exemplo, por isso escolha um código PIN forte), digite `00-`. COLDCARD irá então exibir as suas duas palavras anti-phishing.

![CCQ](assets/fr/36.webp)

Em seguida, introduza o seu código PIN completo, separado por um espaço ou um traço, por exemplo: `00 00`.

![CCQ](assets/fr/37.webp)

A COLDCARD sairá então do modo de calculadora e desbloquear-se-á normalmente.

## Destruir de forma limpa o seu COLDCARD

Se está a planear desfazer-se do seu COLDCARD Q, por exemplo, porque está a utilizar outra carteira de hardware, é importante destruir o dispositivo corretamente. Isto garante que nenhuma informação relativa à sua carteira possa ser recuperada por terceiros.

Existem três níveis de destruição de informação, consoante as suas necessidades. Antes de começar, certifique-se de que a sua carteira foi importada para outra carteira de hardware, que tem acesso a todos os seus fundos e, acima de tudo, que tem a sua frase mnemónica e qualquer frase-passe, ambas funcionais. Sem um backup da carteira, a destruição do seu COLDCARD resultará na perda dos seus bitcoins.

O primeiro nível de destruição consiste em apagar apenas a semente. Esta opção elimina a sua frase mnemónica da memória do COLDCARD, deixando o aparelho funcional. É ideal se quiser voltar a utilizar o COLDCARD Q numa data posterior. Para apagar a semente da memória, aceda ao menu `Avançadas/Ferramentas > Zona de perigo > Funções da semente > Destruir a semente`.

![CCQ](assets/fr/38.webp)

O segundo nível de destruição consiste em desativar permanentemente os dois chips seguros do COLDCARD através do software. Esta ação torna o dispositivo completamente inutilizável. Não será possível revendê-lo, reutilizá-lo ou devolvê-lo à Coinkite: ele será permanentemente destruído. Para prosseguir, siga os passos descritos na secção anterior relativamente ao PIN "*Brick Me*" E, em seguida, introduza intencionalmente este PIN aquando do desbloqueio do COLDCARD.

O terceiro nível envolve a destruição física dos componentes seguros do seu COLDCARD Q. Tal como anteriormente, isto tornará o dispositivo irrevogavelmente inutilizável. Para o fazer, use um berbequim para fazer um buraco nos dois chips no canto superior direito do dispositivo (uma vez virado ao contrário), perto da inscrição "*SHOOT HERE*".

**Precauções importantes** :


- Para evitar o risco de choque elétrico, retire as pilhas do aparelho e desligue-o da corrente antes de o manusear.
- Aguardar alguns minutos após desligar o aparelho antes de iniciar a perfuração.
- Use luvas isoladas e óculos de proteção para garantir a sua segurança.

![CCQ](assets/fr/39.webp)

Uma vez perfuradas as fichas, não tentar voltar a ligar a COLDCARD Q.

Parabéns, está agora a par das opções avançadas do COLDCARD Q!

Se achou este tutorial útil, ficaria muito grato se deixasse um polegar verde abaixo. Não hesite em partilhar este tutorial nas suas redes sociais. Muito obrigado!

Recomendo também este outro tutorial, no qual discutimos a utilização de um concorrente direto do CCQ, o Ledger Flex :

https://planb.network/fr/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a