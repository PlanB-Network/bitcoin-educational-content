---
name: Umbrel Nostr
description: Configuração e utilização de aplicações Nostr na Umbrel
---

![cover](assets/cover.webp)



## Pré-requisitos: Instalação do Umbrel



A Umbrel é uma plataforma de código aberto que permite alojar facilmente aplicações Bitcoin e outros serviços no seu próprio servidor pessoal. É uma solução tudo-em-um que simplifica muito a auto-hospedagem de nós Bitcoin e aplicações descentralizadas.



Certifique-se de que instalou o Umbrel seguindo o nosso guia de instalação:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Introdução ao Nostr



**Nostr** é um protocolo de rede aberto e descentralizado concebido para redes sociais. O seu nome significa _"Notes and Other Stuff Transmitted by Relays"_ (Notas e outras coisas transmitidas por retransmissores). Permite que qualquer pessoa publique mensagens (notas), geridas como eventos JSON, e as propague através de servidores de retransmissão em vez de uma plataforma centralizada. Cada utilizador possui um par de chaves criptográficas (privadas/públicas) que servem de identificador: a chave pública (npub) identifica o utilizador e a chave privada (nsec) permite assinar as mensagens. Graças a essa arquitetura distribuída, o **Nostr oferece resistência à censura** e grande flexibilidade: é possível usar vários clientes e conectar-se a quantos relés desejar, sem depender de um único servidor.



Em suma, o Nostr é um protocolo de comunicação descentralizado em que os **clientes** (aplicações dos utilizadores) enviam e recebem eventos através dos **relayers** (servidores). Este protocolo tem sido particularmente popular entre a comunidade Bitcoin desde 2023, devido aos seus valores de descentralização e soberania de dados.



**Nota: Para usar o Nostr, você precisa da sua chave privada (gerada por um cliente Nostr ou por uma extensão dedicada).** **Nunca compartilhe sua chave privada**, pois isso permitiria que qualquer pessoa se passasse por você. Guarde-a em um local seguro e use ferramentas de gerenciamento de chaves seguras (veja a dica abaixo).



## Aplicações de guarda-chuva para Nostr



A Umbrel oferece um ecossistema de aplicações integradas para tirar o máximo proveito do Nostr no seu nó pessoal. Vamos detalhar o uso dos principais aplicativos relacionados ao Nostr: **Nostr Relay**, **noStrudel**, **Snort** e **Nostr Wallet Connect**. Cada uma delas atende a uma necessidade específica: _Nostr Relay_ é um **servidor de retransmissão privado**, _noStrudel_ e _Snort_ são **clientes Nostr** (interfaces para ler/publicar notas), enquanto _Nostr Wallet Connect_ é uma ferramenta para ligar o seu **portfólio Lightning** ao Nostr.



### Nostr Relay - Seu retransmissor particular na Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



*o *Nostr Relay** é o aplicativo oficial da Umbrel para rodar seu **próprio relay do Nostr** no seu nó. O objetivo principal é ter um relay **privado** e confiável para fazer o **backup** de todas as suas atividades no Nostr** em tempo real. Por outras palavras, ao utilizar este relé pessoal para além dos relés públicos, garante que todas as suas notas, mensagens e reacções são copiadas para casa, a salvo de censura ou perda de dados.



**Instalação:** Na Umbrel App Store (categoria _Social_), instale o _Nostr Relay_. Uma vez iniciado, o aplicativo é executado em segundo plano (serviço docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Verá o seu Interface web através do Umbrel: fornece informações básicas e, acima de tudo, o URL do seu relé (canto superior direito), que terá de copiar para utilização posterior. Está também disponível um botão de sincronização (ícone do globo).



**Para tirar partido do seu relé Umbrel:**



**Adicione o relé ao seu cliente Nostr:** No seu aplicativo cliente (por exemplo, Damus no iOS, Amethyst no Android, Snort ou noStrudel no Umbrel, etc.), adicione a URL do seu relé privado que você copiou anteriormente. Por predefinição, o relé Umbrel escuta na porta **4848**. Se aceder a ele na rede local, isto dá um URL como: `ws://umbrel.local:4848` (ou use o IP local do Umbrel).



Se estiver a utilizar Tailscale (ver abaixo), pode até utilizar o alias DNS MagicDNS (normalmente `umbrel` ou um nome gerado automaticamente) para aceder a ele a partir de qualquer lugar, sempre na porta 4848.



Se preferir o Tor, obtenha o .onion Address da Umbrel e utilize-o com a porta 4848 através de um browser ou cliente compatível com o Tor (ver secção Tor)



Uma vez que a URL tenha sido adicionada à configuração de retransmissão do seu cliente Nostr, conecte-se a esta retransmissão. Você deve ver no seu cliente que o relay Umbrel está conectado (normalmente indicado por um ponto Green ou similar).



**Sincronizar histórico (opcional)**: No Interface web do _Nostr Relay_ na Umbrel, clique no ícone **globo** 🌐 (no topo da página). Essa ação forçará o seu relé Umbrel a se conectar aos seus outros relés (aqueles configurados no seu cliente) para **importar suas atividades públicas** antigas. Isto significa que as notas anteriores que publicou ou leu através de retransmissores públicos também serão transferidas e armazenadas no seu retransmissor privado. Aguarde até que a sincronização seja efectuada.



**Use o Nostr como de costume:** A partir de agora, qualquer nova atividade (notas publicadas, reações, mensagens privadas criptografadas, etc.) que você realizar no Nostr será encaminhada como de costume para os retransmissores públicos **e em paralelo para o seu retransmissor Umbrel**. Se o seu cliente Nostr estiver corretamente configurado, ele enviará cada evento para todos os retransmissores (incluindo o seu). O seu retransmissor privado funcionará como um backup em tempo real. Mesmo em caso de desconexão temporária, seus clientes poderão ressincronizar os dados perdidos mais tarde graças a esse relé. Assim, você tem controle total sobre os dados do Nostr



Em segundo plano, o _Nostr Relay_ da Umbrel baseia-se no projeto de código aberto **nostr-rs-relay** (implementação do protocolo Rust). Ele suporta todo o protocolo Nostr e vários NIPs padrão (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, etc.), garantindo a máxima compatibilidade com os clientes.



### noStrudel - Cliente Nostr para exploradores



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



O **noStrudel** é um cliente web Nostr orientado ao usuário, ideal para entender e explorar a rede Nostr em detalhes. É uma espécie de sandbox para inspecionar eventos e relés, e para experimentar os recursos avançados do protocolo. O Interface está em inglês e é relativamente técnico, o que o torna ideal para usuários experientes e curiosos sobre o funcionamento interno do Nostr.



**Instalação:** Instale _noStrudel_ a partir da Umbrel App Store (categoria _Social_). Uma vez iniciado, pode ser acedido através do seu browser no Address do seu Umbrel (por exemplo, `http://umbrel.local` ou através do seu .onion/Tailscale, ver secção de acesso externo).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Configurar relés:** Ao abrir o noStrudel, você verá um botão "Setup Relays" (Configurar relés) no canto superior direito. Clique nele para configurar os seus relés.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Nesta página, cole o URL do seu relé Umbrel que copiou anteriormente. Também pode adicionar outros relés propostos por defeito pela aplicação. Depois de ter configurado os seus relés, clique em "Sign in" (Iniciar sessão) no canto inferior esquerdo para continuar.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Conexão:** O noStrudel oferece várias opções de conexão. No nosso caso, vamos escolher "Private Key" e colar a chave privada do Nostr gerada anteriormente. Se ainda não tem uma chave, pode instalar a extensão [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) para criar e/ou guardar as suas chaves Nostr e assim comunicar de forma mais segura com as várias aplicações Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Uma vez ligado, pode utilizar o noStrudel para partilhar as suas notas através do Nostr. O Interface dá-lhe acesso a :





- Painel de controlo completo do Nostr com cronologia de notas, notificações, mensagens e pesquisa de perfis
- Gestão de relés e estado da ligação
- Ferramentas avançadas para examinar eventos e o seu conteúdo JSON
- Opções de configuração para filtros de cronologia e PINs



**Dica:** No _noStrudel_, você pode configurar _filtros de linha do tempo_ ou testar diferentes _NIPs (Nostr Implementation Possibilities)_. Por exemplo, verificar o suporte para NIP-05 (identificadores descentralizados) ou recursos mais recentes. Isto faz do _noStrudel_ uma excelente ferramenta para fazer experiências num ambiente controlado.



### Snort - Cliente moderno do Nostr na Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** é outro cliente web do Nostr disponível na Umbrel, oferecendo um **Interface** moderno, rápido e organizado para interagir com a rede social descentralizada. Ao contrário do noStrudel, que tem como alvo usuários avançados, o _Snort_ visa a simplicidade de uso sem sacrificar a funcionalidade. Ele é construído em React e oferece uma experiência de usuário elegante que lembra as redes sociais clássicas, tornando-o adequado para o uso diário.



**Instalação:** Instale o _Snort_ a partir da Umbrel App Store (categoria _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Quando abrir o Snort, verá um botão "Registar" no canto inferior esquerdo.



![Options de connexion dans Snort](assets/fr/10.webp)



Pode optar por se registar ou ligar-se a uma conta existente (que é o que vamos fazer para este tutorial).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



O Snort oferece vários métodos de conexão. Pode utilizar a extensão Nostr Connect previamente instalada ou outros métodos disponíveis. Uma vez ligado, poderá utilizar a aplicação na sua totalidade.



O Interface da _Snort_ oferece :





- Um ecrã **Posts/Conversas/Global** para navegar entre as suas notas, discussões por tópicos ou o feed global
- Separadores para **Notificações**, **Mensagens** (DM), **Pesquisa**, **Perfil**, etc.
- Um botão **+** ou _Escrever_ para publicar uma nova nota
- Gestão de **subscrições (seguintes)** e **listas**
- Menu de gestão de relés para adicionar/remover relés e controlar a sua disponibilidade



**Configuração recomendada do relé:** Para adicionar o seu relé Umbrel, vá a Settings - Relays (Definições - Relés). Introduza o URL do seu relé (`ws://umbrel:4848` ou outro URL dependendo da sua configuração) na lista de relés do Snort. Desta forma, o Snort publicará as suas notas no seu relé privado, para além dos públicos.



### Nostr Wallet Connect - Conecte seu Lightning Wallet ao Nostr



**O Nostr Wallet Connect (NWC)** é um aplicativo que **conecta seu nó Umbrel (Lightning)** a aplicativos Nostr compatíveis para fazer pagamentos Lightning (por exemplo, enviar _zaps_, aqueles micro-pagamentos por "curtir" conteúdo). Neste tutorial, veremos como conectar o noStrudel ao seu nó Lightning para fazer pagamentos diretamente do Interface.



**Instalação e configuração:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Instalar o _Nostr Wallet Connect_ da loja Alby na Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



No noStrudel, clique no seu perfil no canto superior direito e, em seguida, no botão "gerir".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Clique em "Lightning" e depois em "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Entre as opções de ligação disponíveis, selecione "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Clique em "Connect" para ser automaticamente redireccionado para a sua sessão Umbrel Nostr Wallet Connect.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Na página Nostr Wallet Connect, é possível :




   - Defina o seu orçamento máximo
   - Validar autorizações
   - Definir um tempo de expiração para a ligação


Clique em "ligar" para finalizar.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



És redireccionado para o noStrudel com uma mensagem de confirmação: agora já podes fazer zapping no mundo inteiro a partir do teu nó Wallet/LND!



Graças ao NWC, os pagamentos **Lightning via Nostr** (zaps para posts de recompensa, pagamentos _Value for Value_, etc.) começam no **seu próprio nó**. Você não precisa mais rotear suas transações através de serviços externos ou escanear um QR do seu telefone todas as vezes. A experiência do utilizador é muito melhorada, mantendo-se _não custodial_ e favorável à privacidade.



Se quiser saber como configurar o seu próprio nó Lightning na Umbrel, recomendo que consulte este outro tutorial abrangente:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Configuração e segurança avançadas



A utilização conjunta do Umbrel e do Nostr num nível avançado requer uma atenção especial à **segurança** e à **conetividade**. Aqui estão algumas dicas sobre como proteger sua configuração e acessá-la da melhor forma, onde quer que esteja.



### Acesso externo seguro: Tor e Tailscale



Por motivos de segurança, o Umbrel só é acessível por padrão na sua rede local (e via Tor). Para interagir com o Nostr fora de casa, existem duas soluções preferenciais: **Tor** (acesso anónimo via rede onion) e **Tailscale** (rede VPN privada).





- **Acesso via Tor:** A Umbrel configura automaticamente um **serviço Tor (.onion)** para a sua web e aplicações Interface. Isto significa que pode aceder ao Interface Umbrel (incluindo *noStrudel* ou *Snort*) a partir de qualquer lugar, utilizando o navegador Tor, sem expor o seu IP público. O Tor é utilizado para aceder aos seus serviços Umbrel a partir de fora da sua rede local, sem expor o seu dispositivo à Internet ([Configurar o Tor no seu sistema - Guias - Comunidade Umbrel](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww)). Para utilizar esta opção, vá às definições Umbrel e recupere o URL .onion do seu Umbrel (ou leia o código QR fornecido). Num navegador Tor, aceda a este .onion Address: obterá o mesmo Interface que localmente. Pode então utilizar as suas aplicações Nostr como se estivesse em casa.


**Relay do Nostr via Tor:** Se você quiser que seu relay do Nostr possa ser acessado via Tor por seus clientes (ou amigos autorizados), isso é possível. A Umbrel não fornece o .onion Address do relay diretamente, mas como ele roda na porta 4848, você pode usar o :





    - Utilize o .onion Address do UI Umbrel e configure o seu cliente para se ligar através deste Interface (impraticável para WebSocket),





    - Ou** expor a porta 4848 como um serviço onion separado. Isso requer mexer na configuração do Tor na Umbrel (reservado para usuários avançados e confortáveis com SSH). Alternativamente, considere um **Tor tunnel** noutro servidor que redirecciona para o Umbrel: no entanto, para uso pessoal, é mais fácil usar o Tailscale.





- Acesso através de **Tailscale:** [Tailscale](https://tailscale.com/) é uma solução VPN em malha que cria uma rede privada virtual entre os seus dispositivos e a Umbrel. A vantagem: funciona como se estivesse numa LAN, mas através da Internet, encriptada e sem configurações complexas. **O Tailscale atribui ao seu Umbrel um IP fixo e um nome de domínio privado, independentemente da sua localização na rede** ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard)). Na prática, uma vez instalado o Tailscale no Umbrel (na App Store da Umbrel, categoria *Networking*) **e** nos seus dispositivos (telemóvel, PC...), poderá aceder ao Umbrel através de um Address como `100.x.y.z` (IP do Tailscale) ou um nome como `umbrel.tailnet123.ts.net`.


para o Nostr_, o Tailscale é extremamente útil: seu celular, se tiver o Tailscale ativo, poderá se conectar ao `ws://umbrel:4848` (graças ao MagicDNS) ou diretamente ao IP do Tailscale e à porta 4848 para usar o relay. Clientes como Damus ou Amethyst verão seu Umbrel como se ele estivesse na mesma rede local. **Dica:** Habilite a opção **MagicDNS** no Tailscale para usar o hostname `umbrel` ao invés de memorizar o IP. Isso garante uma conexão sem problemas com o seu relé mesmo quando você estiver em movimento ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Além disso, o Tailscale permite-lhe aceder ao Interface Umbrel (e portanto aos clientes web _noStrudel/Snort_) através de um simples browser, usando o IP privado ou o nome de domínio atribuído. Não é necessário um navegador Tor, e as velocidades de transferência de dados são geralmente melhores do que através da rede Tor.




**Nota: Tor e Tailscale não são mutuamente exclusivos. Pode manter o Tor ativo para acesso anónimo ou serviços específicos, e usar o Tailscale no dia a dia pela sua simplicidade. Em ambos os casos, não é necessário abrir uma porta no seu router, o que reforça a segurança.**



### Protegendo seu relé Nostr (práticas recomendadas)



Se você hospedar um relé Nostr na Umbrel, especialmente em um contexto avançado, certifique-se de aplicar algumas boas práticas:





- **Relé privado ou restrito:** Por padrão, o seu relé Umbrel é privado (não anunciado publicamente) e, se você só acessá-lo via Tailscale ou sua LAN, ele permanecerá inacessível a estranhos. **Mantenha o link confidencial** - Não o divulgue em redes Nostr públicas, a menos que queira hospedar voluntariamente outros usuários, o que é uma questão totalmente diferente (moderação, largura de banda, etc.). Para uso pessoal, recomendamos limitar o acesso a si próprio e, se necessário, a alguns amigos e familiares de confiança.





- **Whitelist / Auth**: A implementação do nostr-rs-relay suporta um mecanismo de autenticação **NIP-42** assim como *whitelists* de chaves públicas. Ao habilitar essas opções, você pode restringir seu relay para que ele **só aceite eventos assinados por certas chaves (as suas)**, ou que os clientes tenham que se autenticar para publicar. Para configurar isso é necessário editar o arquivo de configuração `config.toml` do relay no Umbrel (via SSH no container Docker). *É uma manipulação avançada, mas por exemplo você pode listar os anúncios permitidos (`pubkey_whitelist`). Dessa forma, mesmo que alguém descubra seu relay, não poderá publicar nada lá se não estiver na lista.*





- **Actualizações e manutenção:** Mantenha o seu Umbrel e a aplicação *Nostr Relay* actualizados. As actualizações podem incluir melhorias de desempenho (por exemplo, melhor tratamento de spam) e correcções de segurança. Na Umbrel, verifique regularmente se há atualizações do *Nostr Relay* na App Store e aplique-as quando necessário.





- **Monitoramento e limites:** Fique de olho em como seu relé é usado. Se você o abrir para outros, fique de olho na carga (CPU/RAM) do seu Umbrel, já que um relay pode rapidamente acumular muitos dados. nostr-rs-relay oferece **limites de taxa e armazenamento** configuráveis (`limits` na configuração, por exemplo, número de eventos por segundo, tamanho máximo de eventos, purga de eventos antigos...). Para uso privado, provavelmente não precisará de lhes tocar, mas saiba que estes parâmetros existem se precisar deles ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- **Protegendo as chaves do Nostr:** Este ponto já foi mencionado, mas é crucial: nunca insira suas chaves privadas do Nostr em um Interface no qual você não confia totalmente. Em vez disso, use extensões de navegador ou dispositivos externos (como Nostr *signers* em telefones separados) para assinar ações sensíveis. No Umbrel, seus clientes web como *Snort* e *noStrudel* podem trabalhar sem saber sua chave secreta, via NIP-07. Aproveite esta oportunidade para combinar conforto e segurança.




Seguindo essas dicas, sua integração de um nó Umbrel com o Nostr será poderosa **e** segura. Terá um ambiente completo: um nó Bitcoin para pagamentos Lightning, um retransmissor Nostr privado para soberania de dados e clientes web Nostr de alto desempenho para navegar nesta nova rede social descentralizada. Divirta-se explorando o Nostr com a Umbrel!