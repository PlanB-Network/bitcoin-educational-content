---
name: PearPass
description: Recupere o controlo das suas palavras-passe com um gestor de palavras-passe local, ponto-a-ponto e sem nuvem
---

![cover](assets/cover.webp)



Numa altura em que cada indivíduo gere dezenas, ou mesmo centenas, de contas em linha, a segurança dos logins tornou-se uma questão central da segurança informática. Redes sociais, sistemas de mensagens, serviços profissionais, plataformas financeiras: cada um destes acessos depende de um segredo, cujo comprometimento pode ter consequências graves para a sua vida.



E, no entanto, apesar do número crescente de ataques, as más práticas continuam generalizadas entre a população: palavras-passe fracas, palavras-passe reutilizadas, palavras-passe armazenadas em texto claro ou palavras-passe aproximadamente memorizadas. Para resolver estes problemas sem tornar a vida mais complicada no dia a dia, a solução é utilizar um gestor de palavras-passe.



Já existem dezenas de gestores de palavras-passe, e o Plan ₿ Academy oferece um tutorial para a maioria deles. Mas neste tutorial, gostaria de vos apresentar um que se destaca claramente dos restantes em termos de funcionamento: **PearPass**.



**O PearPass é um gestor de senhas de código aberto, local e ponto a ponto, concebido para dar aos utilizadores controlo total sobre os seus dados



![Image](assets/fr/01.webp)



## Porquê escolher o PearPass?



Um gestor de palavras-passe é um programa de software que gera, armazena e organiza todas as suas palavras-passe de forma segura. Em vez de memorizar ou reutilizar as palavras-passe, tem apenas um segredo para proteger: a palavra-passe mestra, que encripta todo o seu cofre. Esta abordagem permite utilizar palavras-passe únicas, longas e aleatórias para cada serviço, reduzindo o risco de esquecimento e de comprometimento, ao mesmo tempo que limita o impacto de uma eventual fuga de informação. Atualmente, é uma ferramenta informática básica que todos deveriam utilizar.



Existem duas categorias principais de gestores de palavras-passe. Por um lado, existe software apenas local, que é muito seguro, uma vez que os dados nunca são armazenados num servidor central, mas não é muito prático, uma vez que não permite sincronizar facilmente as suas credenciais entre vários dispositivos (computador, smartphone, tablet...). Por outro lado, os gestores de senhas baseados na nuvem armazenam as suas credenciais nos seus servidores e sincronizam-nas em todos os seus dispositivos. A sua principal vantagem é a comodidade, mas implicam um compromisso em termos de segurança, uma vez que as suas palavras-passe são armazenadas em infra-estruturas sobre as quais não tem qualquer controlo.



O PearPass rompe deliberadamente com ambos os modelos. Posiciona-se entre os gestores locais e as soluções na nuvem: permite a sincronização das suas palavras-passe, garantindo que estas nunca são armazenadas em servidores remotos. Como resultado, todas as suas credenciais são armazenadas localmente nos seus dispositivos, e a sincronização entre várias máquinas é exclusivamente ponto a ponto. Esta arquitetura elimina os pontos únicos de falha associados às bases de dados centralizadas: não existem servidores para comprometer e nenhuma infraestrutura de terceiros para aceder às suas credenciais. As comunicações entre os seus dispositivos são encriptadas de ponta a ponta, garantindo que apenas as chaves que detém permitem o acesso aos dados.



![Image](assets/fr/02.webp)



Para tornar isso possível, como o próprio nome sugere, o PearPass se baseia no **Pears**, um ecossistema de tecnologia peer-to-peer dedicado à criação e execução de aplicativos sem servidor. O Pears fornece o ambiente de execução, os mecanismos de distribuição e as camadas de rede necessárias para executar aplicações totalmente descentralizadas, capazes de sincronizar diretamente entre pares, sem qualquer infraestrutura central. No caso do PearPass, o Pears fornece descoberta de dispositivos, estabelecimento de conexão criptografada e sincronização de cofre de senhas entre suas máquinas. Essa abordagem garante que o PearPass permaneça funcional, resiliente e independente de qualquer autoridade externa.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Para além desta arquitetura inovadora, o PearPass é inteiramente de código aberto e todas as suas funções são gratuitas. O software também foi auditado de forma independente pela Secfault Security. Para além da sua arquitetura específica, o PearPass oferece, naturalmente, todas as caraterísticas clássicas esperadas de um bom gestor de senhas, que iremos descobrir ao longo deste tutorial.



Em suma, enquanto os gestores de palavras-passe tradicionais lhe pedem para confiar numa empresa e nos seus servidores, o PearPass adopta uma lógica de soberania: sem nuvem, sem contas centralizadas, sem intermediários. O utilizador mantém o controlo exclusivo das suas credenciais, beneficiando simultaneamente da sincronização entre os seus dispositivos.



## Como é que instalo o PearPass?



O PearPass está disponível em todas as plataformas: Windows, Linux, macOS, Android, iOS e extensões de browser. Não há necessidade de instalar o Pears na sua máquina: O PearPass funciona por si só.



### Instalação no Windows



No Windows, o PearPass é fornecido como um instalador clássico. Vá para [a página oficial de download] (https://pass.pears.com/download), depois clique no botão `Download Windows installer`.



Uma vez descarregado o ficheiro, abra o instalador e siga os passos indicados pelo assistente. A aplicação pode então ser acedida a partir do `Menu Iniciar` ou através de um atalho no ambiente de trabalho.



![Image](assets/fr/03.webp)



### Instalação no macOS



No macOS, o PearPass é distribuído como uma imagem de disco (`.dmg`). Vá para [a página oficial de download] (https://pass.pears.com/download) e escolha a versão correspondente à arquitetura do seu Mac (Intel ou Apple Silicon). Após o download, abra o ficheiro `.dmg` e inicie a aplicação a partir da pasta `Applications`.



No primeiro arranque, o macOS apresenta uma mensagem de segurança que indica que a aplicação veio da Internet: basta confirmar para continuar.



### Instalação no Linux



No Linux, PearPass está disponível no formato `.AppImage`, que garante ampla compatibilidade com a maioria das distribuições sem quaisquer dependências específicas. Faça o download do ficheiro `.AppImage` a partir da [página oficial de download] (https://pass.pears.com/download), e depois inicie-o diretamente com um duplo clique.



Dependendo do seu ambiente, pode ser necessário tornar o ficheiro executável através das propriedades do ficheiro (clique com o botão direito do rato) ou com o comando `chmod +x`. Uma vez autorizado, o PearPass é iniciado como uma aplicação autónoma.



### Instalação da extensão do navegador



O PearPass oferece uma extensão de browser para início de sessão automático e acesso rápido ao seu cofre enquanto navega na Web. A extensão está atualmente disponível para o Google Chrome e navegadores compatíveis. Para a instalar, aceda à [página oficial de transferência] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Uma vez adicionada, pode fixá-la na barra de ferramentas para acesso rápido. A ativação da extensão requer uma ligação com a aplicação PearPass instalada localmente no seu computador (voltaremos a este assunto mais tarde no tutorial).



### Instalação em iOS e Android



No iPhone e no Android, basta descarregar a aplicação da sua loja de aplicações:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Para além destes métodos de instalação clássicos, também é possível descarregar o software diretamente dos repositórios do GitHub, para cada :




- [Ambiente de trabalho](https://github.com/tetherto/pearpass-app-desktop);
- [Telemóvel](https://github.com/tetherto/pearpass-app-mobile);
- [Extensão do navegador](https://github.com/tetherto/pearpass-app-browser-extension).



Depois de o PearPass ter sido instalado numa ou mais plataformas, pode passar à configuração inicial. Neste tutorial, vamos começar por configurar o software no ambiente de trabalho e, em seguida, sincronizá-lo com a extensão do navegador e a aplicação móvel.



## Como é que crio um cofre PearPass?



Quando inicia o PearPass pela primeira vez no seu computador, a aplicação guia-o através de dois passos: definir a sua palavra-passe mestra e, em seguida, criar o seu primeiro cofre.



### Definir a palavra-passe principal



Quando a aplicação é iniciada pela primeira vez no ambiente de trabalho, clique no botão `Skip` e depois em `Continue` para passar pelo ecrã de introdução e chegar à fase de configuração da palavra-passe mestra.



![Image](assets/fr/06.webp)



Em seguida, vem o passo importante de escolher a sua palavra-passe mestra. Como vimos na introdução, esta palavra-passe é muito importante, pois dá-lhe acesso a todas as outras palavras-passe guardadas no gestor. Tecnicamente, é utilizada para derivar as chaves criptográficas utilizadas para encriptar os seus dados.



A palavra-passe mestra comporta dois riscos principais: perda e comprometimento. Se perder o acesso a esta palavra-passe, deixará de poder aceder aos seus dados de início de sessão. O PearPass nunca guarda a sua palavra-passe mestra: **Se ela for perdida, seus detalhes de login serão perdidos permanentemente**. Não existe nenhum mecanismo de recuperação. Por outro lado, se esta palavra-passe for comprometida e um atacante obtiver acesso a um dos seus dispositivos, poderá aceder a todas as suas contas.



Para limitar o risco de perda, pode fazer uma cópia de segurança física da sua palavra-passe principal, por exemplo, em papel, e guardá-la num local seguro. Idealmente, feche esta cópia de segurança num envelope para que possa verificar periodicamente se não foi acedida. Por outro lado, nunca faça uma cópia de segurança digital desta palavra-passe.



Para reduzir o risco de comprometimento, a sua palavra-passe principal deve ser forte. Deve ser tão longa quanto possível, incluir uma grande variedade de caracteres e ser escolhida de uma forma verdadeiramente aleatória. Em 2025, as recomendações mínimas exigem pelo menos 13 caracteres, incluindo letras maiúsculas e minúsculas, números e símbolos, desde que a palavra-passe seja aleatória. No entanto, eu recomendaria uma palavra-passe de pelo menos 20 caracteres, se não mais, com todos os tipos de caracteres, para garantir um nível de segurança mais duradouro.



Introduza a sua palavra-passe principal no campo fornecido, confirme-a uma segunda vez e, em seguida, clique no botão `Continuar`.



![Image](assets/fr/07.webp)



Será então redireccionado para o ecrã de início de sessão: introduza a sua palavra-passe principal para verificar se tudo está a funcionar corretamente.



![Image](assets/fr/08.webp)



### Criar o seu primeiro cofre



Depois de iniciar sessão, o PearPass irá pedir-lhe para criar o seu primeiro cofre. Um cofre é um contentor encriptado no qual as suas palavras-passe, IDs, notas seguras e outras informações são armazenadas. Cada cofre é isolado e pode ser identificado por um nome distinto, permitindo-lhe organizar os seus dados de acordo com as suas utilizações (pessoal, profissional, projectos específicos...).



Clique no botão `Criar uma nova abóbada`.



![Image](assets/fr/09.webp)



Escolha um nome para esta abóbada e, em seguida, clique novamente em `Criar uma nova abóbada` para finalizar a criação.



![Image](assets/fr/10.webp)



O seu cofre está imediatamente pronto a ser utilizado. Pode começar a adicionar palavras-passe, inícios de sessão ou notas seguras imediatamente.



![Image](assets/fr/11.webp)



## Como é que adiciono um início de sessão ao PearPass?



Depois de ter criado o seu cofre, pode começar a guardar os seus objectos nele. O PearPass suporta o registo de muitos tipos de artigos:




- iniciar sessão num sítio ou serviço ;
- identidade: as suas informações pessoais para preencher rapidamente formulários, mas também para armazenar documentos de identidade diretamente no PearPass ;
- cartão de crédito: os números do seu cartão de crédito para um pagamento mais rápido nas compras em linha;
- Wi-Fi: palavras-passe para as suas redes Wi-Fi ;
- PassPhrase: frase secreta composta por várias palavras (aviso: desaconselho vivamente a sua utilização para frases mnemónicas wallet Bitcoin);
- nota: criar notas seguras ;
- personalizado: esta funcionalidade permite-lhe criar um tipo de elemento personalizado, adaptado às suas necessidades específicas.



Comece por abrir o PearPass e inicie sessão com a sua palavra-passe principal.



![Image](assets/fr/12.webp)



Selecione o cofre no qual pretende guardar este identificador.



![Image](assets/fr/13.webp)



Na página inicial, clique no botão para adicionar um novo item, dependendo do tipo de informação que pretende registar. No meu caso, pretendo adicionar um início de sessão para a minha conta no sítio Web do Plan ₿ Academy: por isso, clico no botão `Criar um início de sessão`.



![Image](assets/fr/14.webp)



Uma vez selecionado o tipo de elemento que pretende acrescentar, aparece um formulário que permite introduzir as informações associadas ao serviço em questão. Em função das suas necessidades, pode introduzir o nome do serviço, o nome de utilizador, a palavra-passe e, se necessário, o endereço do sítio Web e notas complementares.



O PearPass também possui um gerador de senhas, que permite criar uma senha forte diretamente do formulário. Para utilizá-lo, clique no ícone que representa três pequenos pontos no campo `Senha`, escolha o tamanho desejado e clique em `Inserir senha`.



Quando todos os campos estiverem preenchidos, clique no botão `Guardar` para guardar o identificador no cofre.



![Image](assets/fr/15.webp)



O identificador é agora guardado. Aparece na lista de itens do cofre selecionado e pode ser visualizado clicando nele.



![Image](assets/fr/16.webp)



Pode modificar facilmente um elemento clicando nele e depois no botão `Editar`. Pode também eliminá-lo clicando nos três pequenos pontos no canto superior direito da interface e depois em `Eliminar elemento`.



![Image](assets/fr/22.webp)



No telemóvel, a lógica continua a ser a mesma, embora a interface tenha sido adaptada. Depois de iniciar sessão, selecionar o cofre pretendido, tocar no botão `+`, escolher o tipo de artigo a criar e, em seguida, preencher as informações necessárias.



![Image](assets/fr/17.webp)



## Como organizar o PearPass?



Como vimos nas secções anteriores, o PearPass permite-lhe criar vários cofres distintos. Isto torna possível separar diferentes utilizações e constitui um primeiro nível de organização para o seu gestor de senhas. A partir da página inicial, pode mudar facilmente de um cofre para outro, clicando na seta no canto superior esquerdo da interface.



![Image](assets/fr/18.webp)



Outra forma de organizar suas senhas, mesmo dentro de um cofre, é criar pastas. Para isso, na coluna da esquerda da interface, clique no símbolo `+` ao lado de `Todas as Pastas` e digite o nome da pasta que deseja criar.



![Image](assets/fr/19.webp)



Pode então guardar os identificadores da sua escolha, quer diretamente ao criar um item, quer mais tarde clicando em `Editar`. Para isso, basta selecionar a pasta desejada no canto superior esquerdo do formulário.



![Image](assets/fr/20.webp)



Depois de abrir um item, como um início de sessão, pode clicar no ícone de estrela no canto superior direito da interface para o adicionar aos seus favoritos. Os favoritos podem ser rapidamente encontrados numa pasta dedicada, para além da sua pasta de base.



![Image](assets/fr/21.webp)



Por último, existe uma barra de pesquisa na parte superior da interface, para que possa encontrar rapidamente o item que procura, mesmo que o seu cofre contenha muitos identificadores.



## Como é que sincronizo o PearPass no meu telemóvel?



Agora que tem um cofre funcional com itens armazenados no seu computador, provavelmente vai querer aceder às suas palavras-passe a partir do seu smartphone ou outro dispositivo. O PearPass permite-lhe sincronizar o seu gestor em várias máquinas de forma segura utilizando o Pears. Vamos descobrir como.



Para começar, na máquina de origem (o seu computador, por exemplo), inicie sessão no cofre utilizando a sua palavra-passe principal. Uma vez na página inicial, clique no botão `Adicionar um dispositivo`, localizado na parte inferior direita da interface.



![Image](assets/fr/23.webp)



O PearPass gera então uma ligação de convite, também disponível como um código QR, para sincronizar o cofre selecionado no dispositivo da sua escolha.



![Image](assets/fr/24.webp)



Se pretender sincronizar no seu dispositivo móvel, instale primeiro a aplicação e, em seguida, inicie-a. Ser-lhe-á pedido que crie uma palavra-passe mestra para o seu gestor móvel. Pode optar por utilizar a mesma palavra-passe do seu computador ou uma palavra-passe diferente. Em todos os casos, siga as mesmas recomendações: uma palavra-passe forte e aleatória guardada num suporte físico.



![Image](assets/fr/25.webp)



Pode então ativar a autenticação biométrica, se desejar, para evitar ter de introduzir manualmente a sua palavra-passe mestra sempre que desbloquear o telemóvel.



![Image](assets/fr/26.webp)



Volte a introduzir a sua palavra-passe principal e, em seguida, clique no botão `Continuar`.



![Image](assets/fr/27.webp)



Selecione a opção `Load a vault` e, em seguida, clique em `Scan QR Code` e digitalize o código QR do convite apresentado pelo PearPass na sua máquina de origem (o computador).



![Image](assets/fr/28.webp)



Os cofres do seu computador e do seu telemóvel estão agora sincronizados. Cada ID adicionada num dispositivo será armazenada e replicada de forma segura no outro.



![Image](assets/fr/29.webp)



Nos telemóveis, também é possível ativar o preenchimento automático de campos. Para o fazer, vá a `Definições > Avançadas` e, em seguida, clique no botão `Definir como predefinição` na secção `Preenchimento automático`.



![Image](assets/fr/30.webp)



## Como é que sincronizo o PearPass com a extensão do browser?



Ter um gestor de palavras-passe sincronizado entre o computador e o smartphone já é muito prático, mas integrá-lo diretamente no browser é ainda mais. Para isso, comece por [adicionar a extensão oficial do PearPass ao seu browser] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



A partir do software PearPass instalado na sua máquina local, aceda a `Configurações > Avançadas` e, em seguida, active a opção `Ativar extensão do browser`.



![Image](assets/fr/32.webp)



O PearPass gera um ficheiro de emparelhamento token. Copie-o.



![Image](assets/fr/33.webp)



Em seguida, abra a extensão PearPass no seu browser, cole o emparelhamento token e clique no botão `Verificar`, seguido de `Concluir`.



![Image](assets/fr/34.webp)



O seu gestor de palavras-passe está agora sincronizado com a extensão do browser.



![Image](assets/fr/35.webp)



Pode agora utilizá-lo para se ligar facilmente às suas várias contas Web.



![Image](assets/fr/36.webp)



Agora já sabe como utilizar o gestor de senhas PearPass. Para além desta ferramenta, a segurança digital quotidiana depende da utilização correta de soluções adequadas. Se quiser aprender a criar um ambiente digital pessoal seguro, estável e eficiente, convido-o a descobrir o nosso curso de formação dedicado a este tema:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1