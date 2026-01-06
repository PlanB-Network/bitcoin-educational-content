---
name: Matrix
description: Um guia para compreender, configurar e utilizar Matrix, a plataforma de comunicações segura, aberta e descentralizada.
---

![cover](assets/cover.webp)



## O que é a Matrix?



O Matrix é um **protocolo de comunicação descentralizado** concebido para permitir a troca de mensagens, ficheiros e chamadas de áudio/vídeo entre utilizadores e aplicações, sem dependência de uma empresa central. Ao contrário das plataformas de mensagens tradicionais, o Matrix é uma **infraestrutura aberta**, comparável ao correio eletrónico: qualquer pessoa pode escolher um servidor ou geri-lo ela própria, mantendo a capacidade de trocar mensagens com o resto da rede.



A Matrix distingue-se por três princípios fundamentais:



### Um protocolo, não uma aplicação



O Matrix não é uma aplicação como o WhatsApp ou o Telegram.


Trata-se de uma linguagem normalizada que pode ser utilizada por muitas aplicações.


Por outras palavras, uma grande variedade de software Element, FluffyChat, Cinny, Nheko e outros, dão acesso à mesma rede Matrix.



Isto garante uma liberdade total: mudança de aplicação sem perda de contactos, diversidade de interfaces, independência de um único fornecedor.



![capture](assets/fr/03.webp)



### Uma rede descentralizada e federada



A estrutura do Matrix baseia-se na **federação**, um modelo em que vários servidores independentes cooperam entre si.


Cada servidor (denominado _homeserver_) pode alojar utilizadores, salas de conversação e sincronizar mensagens com outros servidores na rede.


Assim :





- nenhuma entidade controla todo o sistema;
- um servidor pode desaparecer sem afetar o resto da rede;
- cada organização ou indivíduo pode gerir o seu próprio espaço.



Este modelo garante uma **elevada resiliência** e reflecte os valores da soberania tecnológica.



![capture](assets/fr/03.webp)



### Um sistema seguro e encriptado



O Matrix suporta a encriptação **de extremo a extremo (E2EE)** para trocas privadas e grupos encriptados.


As mensagens só podem ser lidas pelos participantes e não pelos servidores intermédios.


Esta abordagem permite comunicar sem expor o conteúdo das trocas a terceiros, mantendo a transparência do protocolo e a possibilidade de alojar o seu próprio servidor.



![capture](assets/fr/05.webp)



### Interoperabilidade única



Um dos principais trunfos do Matrix é a sua capacidade de atuar como uma **ponte entre diferentes sistemas de comunicação**. Graças às _bridges_, é possível ligar :





- Telegram
- WhatsApp
- Signal
- Mensageiro
- Slack
- Discórdia
- IRC, XMPP, etc.



Isto permite unificar comunidades dispersas por várias plataformas, mantendo o controlo sobre a infraestrutura.



![capture](assets/fr/06.webp)



## Como é que o Matrix funciona?



Esta secção apresenta a estrutura interna da rede Matrix para compreender como os utilizadores, os servidores e as aplicações interagem dentro deste ecossistema descentralizado. A Matrix é baseada em três elementos essenciais: _homeservers_, identidades e _clientes_ usados para comunicar.



### Servidores: servidores domésticos



O Matrix é executado em servidores independentes chamados _homeservers_.


Cada servidor doméstico gere :





- as contas de utilizador que aloja,
- conversas privadas e salas de convívio em que estes utilizadores participam,
- sincronização com outros servidores de rede.



Todos os servidores domésticos ligados à rede Matrix trocam automaticamente mensagens e eventos de salas de estar partilhadas. Por exemplo:





- um utilizador registado no servidor A pode conversar com um utilizador no servidor B,
- um salão de beleza pode ser distribuído por dezenas de servidores,
- ninguém tem controlo sobre um salão ou uma comunidade no seu conjunto.



Este modelo é altamente resiliente e permite a cada organização ou indivíduo gerir a sua própria infraestrutura.



### Identificadores de matrizes



Cada utilizador tem um identificador único, denominado **MXID** (_Matrix ID_), que se assemelha a um endereço:



```bash
@nomdutilisateur:serveur.xyz
```



É constituído por :





- um nome de utilizador, precedido de **@**
- o nome do servidor em que a conta foi criada, precedido de **:**



Exemplos:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Este identificador permite a comunicação com qualquer outro utilizador Matrix, independentemente do servidor de origem.



### Clientes matriciais (aplicações)



Para utilizar o Matrix, é necessário ligar-se a uma aplicação chamada **client Matrix**.



Os mais conhecidos são :





- Elemento (web, telemóvel, ambiente de trabalho)
- FluffyChat (telemóvel)
- Cinny (Web/desktop minimalista)
- Nheko (ambiente de trabalho)



Estas aplicações são meras interfaces para :





- para ver as mensagens,
- enviar texto, imagens ou ficheiros,
- aderir ou criar feiras comerciais,
- efetuar chamadas áudio/vídeo.



Todas as aplicações comunicam com os servidores através do mesmo protocolo normalizado.



### Salas e mensagens privadas (DM)



Em Matrix, as trocas têm lugar em **salas** :





- uma sala pode ser pública ou privada
- pode conter duas pessoas ou milhares
- pode ser partilhado entre vários servidores
- tem um identificador único que começa por **!**



As mensagens privadas são simplesmente salas de conversação com dois participantes, frequentemente designadas por **DM (Diret Messages)**.



A sincronização dos salões de beleza ocorre em tempo real entre os servidores participantes, garantindo uma experiência perfeita e mantendo a descentralização.



## Porquê utilizar Matrix?



Matrix não é apenas uma alternativa aos sistemas de mensagens centralizados: é uma tecnologia que responde a necessidades reais em termos de soberania digital, segurança e interoperabilidade. Há muitas razões pelas quais cada vez mais pessoas, empresas e instituições estão a escolher este protocolo para comunicar.



### Recuperar o controlo das suas comunicações



A maioria das plataformas de mensagens funciona segundo um modelo centralizado: um único interveniente controla os servidores, o acesso, os dados e as regras de utilização. Este modelo implica uma dependência total do fornecedor.


A Matrix adopta uma abordagem diferente.


Qualquer pessoa pode escolher onde alojar a sua conta, ou mesmo instalar o seu próprio servidor. Nenhuma entidade está em posição de bloquear um utilizador, exigir uma identificação intrusiva ou impor uma mudança de política.


Esta arquitetura devolve a autonomia aos indivíduos e às organizações. As comunicações já não se baseiam na confiança numa empresa, mas num protocolo aberto, documentado e verificável.



### Comunicação segura e encriptada



O Matrix suporta a encriptação de ponta a ponta para conversas e grupos privados. Este mecanismo garante que apenas os participantes podem ler as mensagens, mesmo que estas passem por servidores de terceiros na federação.



O protocolo utiliza o algoritmo Megolm/Olm, concebido especificamente para proporcionar uma segurança forte em ambientes distribuídos e com vários dispositivos.



Isto torna possível :





- proteger as conversas sensíveis,
- impedir o acesso não autorizado (mesmo a partir do servidor anfitrião),
- manter a confidencialidade a longo prazo.



A encriptação não é uma opção: é um componente essencial do protocolo.



### Deixar de estar dependente de uma única aplicação



Matrix não é uma aplicação, mas sim um protocolo.



Esta diversidade de clientes garante :





- uma escolha adaptada às necessidades individuais,
- a capacidade de utilizar o Matrix em qualquer tipo de dispositivo,
- não dependem de um único software.



Se um cliente não for adequado ou deixar de ser mantido, basta selecionar outro: a conta continua a funcionar normalmente.



### Federar e interligar diferentes comunidades



A federação permite que diferentes servidores trabalhem em conjunto, embora sejam geridos de forma independente.


Assim :





- uma organização pode gerir o seu próprio servidor doméstico,
- os indivíduos podem juntar-se a servidores públicos,
- todos podem comunicar uns com os outros como se estivessem na mesma plataforma.



Esta flexibilidade permite criar espaços de comunicação adaptados a cada necessidade: equipas, associações, comunidades, instituições ou projectos open source.



A Matrix é particularmente popular nos círculos técnicos, colectivos de activistas, investigadores, governos e, cada vez mais, nas comunidades Bitcoin.



### Interoperabilidade única no panorama das mensagens



Um dos principais trunfos do Matrix é a sua capacidade de **extender** as trocas graças a pontes capazes de ligar :





- WhatsApp
- Telegram
- Signal
- Slack
- Discórdia
- IRC
- XMPP
- e muitas outras plataformas



A Matrix torna-se assim uma camada unificadora das comunicações, reunindo várias comunidades dispersas por diferentes aplicações.



Esta interoperabilidade reduz a fragmentação e simplifica a colaboração.



### Um protocolo livre, aberto e sustentável



O protocolo Matrix é inteiramente de fonte aberta e desenvolvido de forma transparente.


Este facto garante várias vantagens:





- uma evolução contínua da norma,
- a possibilidade de qualquer pessoa verificar o código,
- independência em relação a mudanças comerciais ou políticas,
- resiliência a longo prazo.



Ao contrário dos sistemas de mensagens proprietários, o futuro do Matrix não depende de uma única empresa, mas de uma comunidade global e de uma norma aberta.



## Como é que crio uma conta Matrix?



Criar uma conta Matrix é simples e não requer conhecimentos técnicos. Os utilizadores podem juntar-se a um servidor existente, criar um início de sessão e começar a conversar imediatamente. Esta secção descreve os passos essenciais.



### Escolher um servidor (público ou privado)



Matrix é uma rede federada: existem numerosos servidores (homeservers) geridos por diferentes organizações, comunidades ou indivíduos. A escolha do servidor apenas determina _onde_ a conta é alojada, mas não impede a comunicação com toda a rede.


**Estão disponíveis duas opções



### - Utilizar um servidor público



Esta é a solução mais simples.


Exemplos de servidores populares:





- _matrix.org_ (o mais conhecido)
- _envs.net_
- servidores comunitários temáticos (tecnologia, privacidade, código aberto...)



Estes servidores são adequados para utilizadores principiantes que pretendam registar-se rapidamente.



### - Utilizar um servidor privado



Ideal para :





- uma organização,
- uma família,
- um projeto de fonte aberta,
- uma equipa de trabalho,
- ou para utilização soberana e auto-hospedada.



Neste caso, é necessário que alguém administre o servidor (Synapse, Dendrite, Conduit...).


Independentemente do servidor escolhido, os utilizadores podem falar uns com os outros graças à federação.



### Criar uma conta passo a passo



Como o Matrix é um protocolo aberto, pode ser acedido por várias aplicações.


Tal como descrito acima, oferecem diferentes interfaces e funcionalidades consoante os requisitos:





- Element**: o cliente mais completo, disponível em todas as plataformas.
- FluffyChat**: simples, moderno e ideal para telemóveis.
- Nheko**: cliente leve e ergonómico para PCs.
- SchildiChat**: Variante Element com melhorias ergonómicas.
- NeoChat**: integrado no ecossistema KDE.



A escolha do cliente não tem qualquer impacto na conta: todos funcionam com qualquer servidor Matrix.



### Etapas clássicas :





- Abrir a aplicação escolhida. No nosso caso, fá-lo-emos com [Element](app.element.io).
- Selecionar "Criar uma conta".



![cover-kali](assets/fr/10.webp)



Para simplificar, pode criar uma conta Matrix utilizando **Google, Facebook, Apple, GitHub ou GitLab**. Estes serviços apenas saberão que a sua conta foi utilizada para aceder ao Matrix: trata-se de uma **ligação social**.



Para maior confidencialidade, pode também registar-se manualmente, escolhendo um **nome de utilizador**, uma **palavra-passe** e um **endereço de correio eletrónico**.



Dependendo do servidor escolhido, pode ser necessário um **captcha**, bem como a aceitação dos **termos de utilização**.



Uma vez validado o registo, é enviada uma mensagem eletrónica de confirmação.


Basta clicar na ligação para ativar a sua conta e aceder à aplicação Web (Element) para participar nas suas primeiras conversas Matrix.



![cover-kali](assets/fr/11.webp)



Agora tem uma conta e utiliza a versão Web do Element.



## Adicionar o seu primeiro contacto



Para comunicar com alguém no Matrix, só precisa de saber o seu identificador completo, chamado **Matrix ID**.



Exemplo:



`@alice:matrix.org @bened:monserveur.bj`



### Adicionar um contacto



Para convidar amigos para a conversa de grupo, clique no círculo `i` no canto superior direito. Isto abre o painel do lado direito. Clique em "Pessoas" para ver a lista de membros desta sala: devem ser os únicos presentes neste momento.



![cover-kali](assets/fr/12.webp)



Clique em "Convidar para esta sala" na parte superior da lista de pessoas e abrir-se-á uma janela para que possa convidar os seus amigos a juntarem-se a si no Matrix. Se já tiverem iniciado sessão no Matrix, introduza a respectiva ID Matrix. Se não estiverem, introduza o seu endereço de correio eletrónico e serão convidados a juntar-se a nós.



Não existe um sistema de "amigos": um contacto é simplesmente uma pessoa com quem foi iniciada uma conversa.



![cover-kali](assets/fr/13.webp)



A pessoa que convidou pode aceitar ou recusar o convite. Se aceitar, deve vê-la entrar na sala. Quanto mais, melhor!



![cover-kali](assets/fr/14.webp)



### Configurar o seu próprio servidor



O Matrix torna-se realmente útil quando utilizado em conjunto com um servidor pessoal.


A implementação do seu próprio servidor doméstico permite-lhe :





- manter um controlo total sobre os dados,
- definir as suas próprias regras de utilização,
- alojar várias contas (amigos, equipa, comunidade),
- e garantir a máxima resiliência em caso de restrições ou censura.



**Soluções disponíveis: **





- Synapse**: a implementação histórica e mais completa.
- Dendrite**: mais leve, mais potente e concebido para o futuro do protocolo.
- Conduit**: uma variante minimalista que é fácil de implementar.



**Pré-requisitos





- um nome de domínio,
- uma máquina ou um VPS,
- competências mínimas de administração de sistemas.



Mesmo que exija um pouco de configuração, a gestão do seu próprio servidor transforma o Matrix numa ferramenta soberana e duradoura.



### Participar nas suas primeiras feiras



Matrix baseia-se fortemente em _rooms_ (salas de estar).


Existem feiras públicas, privadas, comunitárias, técnicas, locais e internacionais.



**Três formas de aderir a um salão de beleza



1. **Através de uma ligação de convite** (frequentemente sob a forma de um URL `matrix.to`).


2. **Procurar o nome do salão** na aplicação.


3. **Introduzindo o ID completo do espetáculo**, por exemplo, :


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Uma vez inscrito, o chat comporta-se como um grupo de notícias clássico, com histórico, encriptação, ficheiros, reacções e chamadas áudio/vídeo, dependendo do cliente utilizado.



![capture](assets/fr/09.webp)



## Ir mais longe



Depois de dominar as noções básicas, o Matrix oferece uma série de possibilidades avançadas. Quer pretenda ligar outros sistemas de mensagens, alojar o seu próprio servidor ou organizar uma comunidade, o ecossistema é muito rico.



### Pontes (WhatsApp, Telegram, Signal, etc.)



Uma ponte liga o Matrix a outros sistemas de mensagens.


Com ele, pode enviar e receber mensagens de :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discórdia
- Slack**
- IRC** (IRC)
- e muitos outros



### O que as pontes podem fazer





- Centralize todas as suas conversas no Matrix
- Fornecer uma interface aberta para interação com serviços proprietários
- Gerir uma comunidade multiplataforma a partir de um único local



Algumas pontes são oficiais, outras são comunitárias.


Consoante o departamento, podem exigir :





- um servidor pessoal,
- uma configuração adicional,
- ou a utilização de uma ponte pública existente.



### Utilizar a Matrix para uma organização, comunidade ou projeto Bitcoin



A Matrix não é apenas uma ferramenta pessoal.


Pode ser utilizado para estruturar grupos de trabalho, organizar comunidades locais ou gerir a comunicação de projectos.



**Exemplos de utilização





- Comunidades de código aberto
- Projectos de ecossistemas Bitcoin e Lightning
- Grupos de estudantes ou de programadores
- Organizações de cidadãos
- Meios de comunicação social independentes
- Grupos e associações locais



**Porque é que isto é interessante?





- ferramenta 100% open-source**
- Comunicação soberana e descentralizada**
- Espaços organizados em **lounges**, **subgrupos**, **lounges privados**, etc.
- Integrar com Nextcloud, GitLab, Mattermost ou bots personalizados
- Gestão aperfeiçoada de permissões e moderação



A Matrix torna-se assim um pilar de comunicação para qualquer estrutura que pretenda manter-se independente das grandes plataformas centralizadas.



## Conclusão



O Matrix representa uma solução moderna, aberta e segura para a comunicação em tempo real, oferecendo uma alternativa descentralizada às plataformas tradicionais. Graças à sua arquitetura federada e aos seus protocolos de encriptação avançados, permite que os utilizadores mantenham o controlo dos seus dados enquanto desfrutam de uma experiência fluida e interoperável. Quer seja para uso pessoal, profissional ou comunitário, o Matrix oferece uma estrutura robusta e escalável para a construção de ambientes de comunicação adaptados às necessidades actuais.



Para saber mais e descobrir todas as funcionalidades oferecidas pelo Matrix, pode consultar a documentação oficial disponível aqui :


[https://matrix.org/docs/](https://matrix.org/docs/)