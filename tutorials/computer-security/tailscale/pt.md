---
name: Escala de cauda
description: Tutorial avançado de Tailscale
---
![cover](assets/cover.webp)



## 1. Introdução



O Tailscale é uma VPN de próxima geração que cria uma rede em malha encriptada entre os seus dispositivos. Permite-lhe ligar máquinas remotas como se estivessem na mesma rede local, sem configurações complexas ou abertura de portas.



Para a auto-hospedagem, o Tailscale atribui a cada dispositivo um IP privado fixo numa rede virtual, oferecendo um acesso estável aos seus serviços, mesmo quando o seu IP público muda. Isto significa que pode gerir os seus servidores remotamente, sem expor os seus serviços diretamente à Internet.



**Aplicações principais




- Gerir um servidor pessoal a partir do exterior
- Gerir os nós Umbrel/Lightning mais rapidamente do que o Tor
- Acesso seguro a um Raspberry Pi ou NAS
- Ligue-se aos seus serviços através de SSH ou HTTP sem configurações de rede complexas



Esta abordagem centrada na simplicidade permite que os auto-hospedistas acedam aos seus serviços de forma segura, evitando as armadilhas das VPNs tradicionais.



## 2. Como funciona o Tailscale



Ao contrário das VPNs tradicionais, que encaminham todo o tráfego através de um servidor central, o Tailscale cria uma rede em malha em que os dispositivos comunicam diretamente entre si. O servidor central apenas trata da autenticação e da distribuição de chaves, sem ver os dados do utilizador.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Figura 1: VPN tradicional com arquitetura hub-and-spoke em que todo o tráfego passa por um servidor central*



Com base no WireGuard, cada dispositivo gera as suas próprias chaves criptográficas. O servidor de coordenação distribui as chaves públicas aos nós, que depois estabelecem túneis encriptados de ponta a ponta diretamente entre si. Para ultrapassar as firewalls, o Tailscale utiliza a travessia NAT e, como último recurso, retransmissões DERP que mantêm a encriptação.



![VPN maillé (mesh)](assets/fr/02.webp)


*Figura 2: Rede em malha de escala de cauda em que os dispositivos comunicam diretamente entre si*



Todas as comunicações são encriptadas com o WireGuard. O Tailscale apenas vê os metadados (ligações), mas nunca o conteúdo das trocas. Para uma maior soberania, o Headscale permite que o servidor de coordenação seja auto-hospedado.



**Segurança e confidencialidade:** Graças ao WireGuard, todas as comunicações no Tailscale são encriptadas de ponta a ponta. O Tailscale não consegue ler o seu tráfego - apenas os seus dispositivos possuem as chaves privadas necessárias. O serviço apenas vê metadados: Endereços IP, nomes de dispositivos, carimbos de data/hora de ligação e registos de ligação ponto a ponto (sem conteúdo).



No entanto, esta arquitetura está dependente da Tailscale Inc. para a coordenação da rede. Para eliminar esta dependência, a Headscale propõe uma alternativa open-source que lhe permite alojar o servidor de controlo de forma autónoma, utilizando os clientes oficiais Tailscale, garantindo assim uma soberania total sobre a sua infraestrutura de rede, à custa de uma configuração mais técnica.



**Para uma explicação detalhada do funcionamento interno do Tailscale, incluindo a gestão do plano de controlo, a travessia de NAT e os relés DERP, recomendamos o excelente artigo [How Tailscale Works] (https://tailscale.com/blog/how-tailscale-works) no blogue oficial. Este artigo explica em profundidade os conceitos técnicos que tornam o Tailscale tão poderoso.



## 3. Instalar o Tailscale



O Tailscale funciona nos sistemas operativos **mais comuns** (Windows, macOS, Linux, iOS, Android). Diz-se que a instalação é "rápida e fácil" em todas as plataformas. Vamos começar por ver o Interface e como criar uma conta, depois passamos aos procedimentos de instalação para diferentes ambientes.



### 3.1 Criação de conta Tailscale



Aceda a [https://tailscale.com/] (https://tailscale.com/) e clique no botão "Get Started" (Iniciar) no canto superior direito da página.




![Page d'accueil Tailscale](assets/fr/03.webp)


*A página inicial do Tailscale explica o conceito e oferece um início gratuito*



Para utilizar o Tailscale, é necessário criar uma conta através de um fornecedor de identidade:



![Page de connexion Tailscale](assets/fr/04.webp)


*Escolha do fornecedor de identidade para ligação ao Tailscale (Google, Microsoft, GitHub, Apple, etc.)*



Depois de iniciar a sessão, o Tailscale pedir-lhe-á algumas informações sobre a utilização pretendida:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Formulário para compreender melhor o seu caso de utilização (pessoal ou profissional)*



Depois de criar a sua conta, pode instalar o Tailscale nos seus dispositivos:



![Ajout du premier appareil](assets/fr/07.webp)


*O Tailscale permite-lhe instalar a aplicação em diferentes sistemas*



### 3.2 Instalação em diferentes plataformas





- No Windows e no macOS:** Basta descarregar a aplicação gráfica do sítio Web oficial do Tailscale e instalá-la (ficheiro .msi no Windows, ficheiro .dmg no Mac). Uma vez instalada, a aplicação lança um Interface gráfico que lhe permite ligar-se (através de um browser) à sua conta Tailscale para autenticar a máquina.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Ligar um MacBook ao taipal traseiro*



![Connexion réussie](assets/fr/09.webp)


*Confirmação de que o dispositivo está ligado à rede Tailscale*





- No Linux (Debian, Ubuntu, etc.):** Tem várias opções. O método mais simples é executar o script de instalação oficial: por exemplo, no Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Este script irá adicionar o repositório oficial do Tailscale e instalar o pacote. Também é possível [adicionar manualmente o repositório APT](https://pkgs.tailscale.com) ou usar pacotes Snap ou apt comuns. Uma vez instalado, o daemon `tailscaled` será executado em segundo plano. Será então necessário **autenticar o nó** (veja Interface CLI vs web abaixo). Em outras distribuições (Fedora, Arch...), o pacote também está disponível através dos repositórios padrão ou do script de instalação universal. Para um servidor headless, use CLI: por exemplo `sudo tailscale up --auth-key <key>` se estiver usando uma chave de autenticação pré-gerada, ou simplesmente `tailscale up` para um login interativo (que fornecerá uma URL a ser visitada para autenticar o dispositivo).





- Em sistemas baseados em ARM (Raspberry Pi, etc.):** Estamos geralmente em Linux, por isso a mesma abordagem acima (script ou pacote). Note que o Tailscale suporta a arquitetura ARM32/ARM64 sem qualquer problema. Muitos utilizadores instalam o Tailscale no Raspberry Pi OS via apt ou em distribuições leves (DietPi, etc.) para aceder ao seu Pi em qualquer lugar.





- No iOS e Android:** Tailscale fornece aplicações móveis **oficiais**. Basta instalar *Tailscale* na [App Store] (https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) ou na [Play Store] (https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Passos para instalar o Tailscale no iPhone: boas-vindas, privacidade, notificações, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Ligar à rede da cauda, selecionar a conta e validar no iPhone*



Uma vez instalada a aplicação, no primeiro lançamento ser-lhe-á pedida a autenticação através do fornecedor escolhido (Google, Apple ID, Microsoft, etc., dependendo do que estiver a utilizar para o Tailscale) - é o mesmo procedimento que noutras plataformas, normalmente um redireccionamento para uma página Web OAuth. Depois disso, a aplicação móvel cria a VPN (no iOS, terá de aceitar o suplemento de configuração da VPN). A aplicação pode então ser executada em segundo plano, dando-lhe acesso à sua rede de cauda a partir de qualquer lugar. *Atenção:* no telemóvel, só pode ter **uma VPN ativa de cada vez** - por isso, certifique-se de que não tem outra VPN ligada ao mesmo tempo, ou o Tailscale não conseguirá estabelecer a sua própria VPN. No Android, pode configurar um perfil de trabalho separado se pretender isolar determinadas utilizações (por exemplo, um perfil com o Tailscale ativo para uma determinada aplicação).



### 3.3 Adicionar vários dispositivos e validação



Assim que o primeiro dispositivo estiver ligado, o Tailscale pede-lhe para adicionar outros dispositivos à sua rede:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface mostrando o primeiro dispositivo ligado e à espera de outros dispositivos*



Depois de adicionar vários dispositivos, pode verificar se estes conseguem comunicar entre si:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Confirmação de que os dispositivos podem comunicar entre si através de ping*



O Tailscale sugere então configurações adicionais para melhorar a sua experiência:



![Suggestions de configuration](assets/fr/14.webp)


*Sugestões para configurar o DNS, partilhar dispositivos e gerir o acesso*



### 3.4 Painel de controlo administrativo



A consola de administração web permite-lhe ver e gerir todos os dispositivos ligados:



![Tableau de bord des machines](assets/fr/15.webp)


*Lista de dispositivos ligados com as suas caraterísticas e estado*



**Interface Web vs Interface CLI:** O Tailscale oferece duas formas complementares de interação com a rede: a **administração Web do Interface** e o **cliente de linha de comandos (CLI)**.





- Interface Web (Consola de Administração)**: acessível em [https://login.tailscale.com](https://login.tailscale.com), esta consola web é o painel de controlo central da sua rede Tailscale. Apresenta uma lista de todos os dispositivos (*Máquinas*), o respetivo estado online/offline, os respectivos endereços IP Tailscale e muito mais. Aqui pode **gerir dispositivos** (renomear, expirar chaves, autorizar rotas, desativar um nó), **gerir utilizadores** (num contexto organizacional) e definir regras de segurança (ACLs). É também aqui que se configuram opções globais como MagicDNS, tags ou chaves de autenticação (chaves de autenticação pré-generate para adição automática de dispositivos). O Interface web é muito útil para obter uma visão geral e aplicar alterações que serão propagadas através do servidor de coordenação para todos os nós. *Exemplo:* Ativar uma **rota de sub-rede** ou um **nó de saída** é feito com um único clique na consola, uma vez que o nó em questão se tenha anunciado como tal.





- Linha de comando Interface (CLI):** O comando `tailscale` está disponível no CLI em todos os dispositivos onde o Tailscale está instalado. Este CLI permite fazer tudo localmente: conectar (`tailscale up`), inspecionar o status (`tailscale status` para ver quais peers estão conectados), debug (`tailscale ping <ip>`), e assim por diante. Algumas funcionalidades são até **exclusivas do CLI** ou mais avançadas, por exemplo:





  - `tailscale up --advertise-routes=192.168.0.0/24` para anunciar uma rota de sub-rede,
  - `tailscale up --advertise-exit-node` para propor sua máquina como um nó de saída,
  - `tailscale set --accept-routes=true` (ou `--exit-node=<IP>`) para consumir uma rota ou utilizar um nó de saída,
  - `tailscale ip -4` para visualizar o IP Tailscale do dispositivo,
  - `tailcale lock/unlock` (se estiver a utilizar *tailnet-lock*, funcionalidade de segurança avançada),
  - ou `tailscale file send <node>` para utilizar **Taildrop** (transferência de ficheiros entre dispositivos).


O CLI é muito útil em servidores sem gráficos do Interface e para criar scripts de determinadas acções. **Diferenças de uso:** A maioria das configurações básicas podem ser feitas tanto via Web quanto via CLI. Por exemplo, a adição de um dispositivo pode ser feita através de uma solicitação via console, ou executando `tailscale up` no dispositivo e validando via web. Da mesma forma, renomear um dispositivo pode ser feito através do console ou com `tailscale set --hostname`. **Em resumo**, o console web é ideal para administração global da rede (especialmente com múltiplas máquinas/usuários), enquanto o CLI é útil para controle fino sobre uma determinada máquina, scripts de automação, ou uso em um sistema sem uma GUI.



## 4. Utilizar o Tailscale no Umbrel



A Umbrel é uma plataforma popular de auto-hospedagem (utilizada nomeadamente para nós Bitcoin/Lightning e outros serviços auto-hospedados, através da sua App Store). Para instalar e configurar a Umbrel, recomendamos que siga o nosso tutorial dedicado:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Usar o Umbrel e o Tailscale juntos é um caso de uso particularmente interessante, pois o Umbrel integra nativamente um módulo Tailscale fácil de implantar. Veja como o Tailscale se integra ao Umbrel e o que ele oferece:



### 4.1 Instalação e configuração do guarda-chuva





- Instalar o Tailscale na Umbrel:** A Umbrel tem uma aplicação oficial do Tailscale na sua App Store. A instalação não poderia ser mais simples:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Página da aplicação Tailscale na Umbrel App Store*



A partir do Interface Web Umbrel, abra a App Store, procure por **Tailscale** e clique em *Install*. Alguns segundos depois, o aplicativo é instalado no Umbrel. Ao abri-lo, o Umbrel exibe uma página que permite vincular seu nó ao Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Ecrã de ligação da escala de cauda no Interface* da Umbrel



Basta **clicar em "Log in "**, que o redireccionará para a página de autenticação Tailscale:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Ligue-se ao Tailscale através de um fornecedor de identidade*



Pode autenticar-se através da sua conta Tailscale (Google/GitHub/etc.) ou introduzir o seu e-mail. Normalmente, na Umbrel, o Interface pede-lhe para visitar [https://login.tailscale.com](https://login.tailscale.com) e iniciar sessão - isto autentica a aplicação Tailscale da Umbrel.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Confirmação de que o dispositivo Umbrel está ligado à rede Tailscale*



Uma vez concluído, o seu Umbrel está "na" sua rede Tailscale e aparece na sua consola com um nome (por exemplo, *umbrel*). Pode então clicar no IP Address dos seus dispositivos para o copiar, recuperar o IPv6 Address ou o seu MagicDNS associado ao seu dispositivo.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*A consola de administração do Tailscale mostra vários dispositivos ligados, incluindo o Umbrel*




### 4.2 Acesso remoto aos serviços Umbrel



Assim que o Umbrel estiver ligado ao Tailscale, **pode aceder ao Interface Umbrel e às aplicações nele executadas, a partir de qualquer lugar, como se estivesse na rede local**. Esta é uma das principais vantagens em relação ao Tor.



O acesso é extremamente simples: em vez de utilizar `umbrel.local` (que só funciona na sua rede local), utiliza o IP Address da sua Tailscale da Umbrel (`http://100.x.y.z`) diretamente a partir de qualquer dispositivo ligado à sua tailnet. Isto funciona independentemente do local onde se encontra ou da ligação à Internet que está a utilizar (4G, Wi-Fi pública, rede empresarial).



**Exemplos de aplicações alojadas na Umbrel acessíveis através do Tailscale:**





- Interface Umbrel principal**: Aceda ao seu painel de controlo da Umbrel escrevendo simplesmente `http://100.x.y.z` no seu browser
- Nó Bitcoin**: Gerir o seu nó Bitcoin sem latência, ver a sincronização e as estatísticas
- Nó do Lightning**: Use o ThunderHub, RTL ou outras interfaces de gerenciamento do Lightning com capacidade de resposta imediata
- Mempool**: Visualizar transacções Bitcoin e Mempool sem atrasos no Tor
- noStrudel**: Aceder aos seus serviços Nostr alojados na Umbrel



**Ligar carteiras externas ao seu Bitcoin ou lightning nodes através do Tailscale:**



O Tailscale também permite que suas carteiras Bitcoin e Lightning instaladas em outros dispositivos se conectem diretamente ao seu nó Umbrel:





- Sparrow wallet (Bitcoin)**: Este Wallet Bitcoin externo pode ligar-se diretamente ao servidor Electrum da Umbrel utilizando o Tailscale IP Address:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Configuração de um servidor Electrum privado no Sparrow wallet usando o Tailscale IP Address* da Umbrel



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Lista de aliases de servidor Electrum em Sparrow com Umbrel Tailscale IP Address*



Leia o nosso guia completo para configurar o Sparrow wallet com o seu nó Bitcoin:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Relâmpago)**: Este Lightning móvel Wallet pode se conectar ao seu nó Lightning na Umbrel. Em vez de configurar o ponto final como `.onion', basta definir o IP Tailscale do seu Umbrel e a porta API do Lightning. A conexão será instantânea em comparação com o Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Configurando o Zeus para se conectar ao nó do Lightning através do IP Address do Tailscale*



Para configurar o Zeus com o seu nó Lightning, consulte o nosso tutorial detalhado:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Para saber mais sobre o Lightning Network e como funciona na Umbrel, visite:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Vantagens em relação ao Tor



Umbrel oferece nativamente acesso remoto via Tor (fornecendo endereços `.onion` para seus serviços web). Embora o Tor tenha a vantagem da confidencialidade (anonimato) e não necessite de registo, muitos utilizadores consideram o **Tor lento e instável** para a utilização quotidiana (as páginas carregam lentamente, os tempos limite, etc.) - *"O Umbrel via Tor é tão lento "*, queixam-se alguns.



O Tailscale oferece uma ligação geralmente **mais rápida e de baixa latência**, uma vez que o tráfego passa diretamente (ou através de um retransmissor rápido) em vez de passar por 3 nós Tor. Além disso, o Tailscale proporciona uma experiência de "rede local": são utilizados IPs privados e as aplicações podem ser mapeadas diretamente (por exemplo, unidade de rede SMB em \100.x.y.z).



Dito isso, o Tor tem a vantagem de ser descentralizado e "pronto para uso" na Umbrel, enquanto o Tailscale envolve confiar em terceiros (ou hospedar o headscale). O Tor também é útil para acesso sem cliente (a partir de qualquer navegador Tor, pode consultar a interface de utilizador da Umbrel, enquanto o Tailscale requer o cliente instalado no dispositivo de acesso).



**Resumindo**, para uma utilização interactiva (carteiras Lightning, interfaces Web frequentes), o Tailscale oferece um conforto e uma rapidez apreciáveis em comparação com o Tor, ao preço de uma ligeira dependência externa. Muitas pessoas optam por usar *ambos*: Tailscale no dia a dia, e Tor como alternativa ou para partilhar o acesso com alguém sem o convidar para a sua VPN.



### 4.4 Segurança



Ao utilizar o Tailscale com a Umbrel, evita expor a Umbrel à Internet. O nó Umbrel é acessível apenas aos outros dispositivos autenticados na rede de cauda, reduzindo consideravelmente a superfície de ataque (nenhuma porta aberta a estranhos, nenhum risco de ataque ao serviço Web através da Internet).



As comunicações são encriptadas (WireGuard) para além de qualquer encriptação que os seus serviços já estejam a fazer (por exemplo, mesmo o HTTP interno está no túnel). Pode ainda aplicar ACLs Tailscale para, por exemplo, impedir que um determinado dispositivo tailnet aceda à Umbrel se quiser dividir a rede. O próprio Umbrel não vê a diferença - pensa que está a servir localmente.



---

Para concluir esta secção, a integração do Tailscale no Umbrel demora apenas alguns cliques e **melhoria muito a acessibilidade** do seu nó auto-hospedado. Poderá administrar o Umbrel e os seus serviços a partir de qualquer lugar, de forma segura e eficiente, tal como se estivesse em casa. Esta é uma solução particularmente útil para aplicações em tempo real (Lightning) que sofrem com a latência do Tor, ou mais geralmente para qualquer auto-hospedeiro que procure uma simples ligação privada. Tudo sem expor uma única porta** na sua caixa, e sem configuração de rede complicada.



## 5. Gestão avançada e casos de utilização



### 5.1 Caraterísticas avançadas do Tailscale



**Gestão da rede:** A consola de administração (login.tailscale.com) permite-lhe gerir os seus dispositivos, visualizar ligações e configurar regras de acesso.



**MagicDNS:** Resolve automaticamente nomes de dispositivos (por exemplo, `raspberrypi.tailnet.ts.net`) para evitar a memorização de endereços IP.



**ACL e controlo de acesso:** Defina com precisão quem pode aceder a quê na sua rede através de regras JSON, ideais para isolar determinados dispositivos ou restringir o acesso a serviços específicos.



**A partilha de dispositivos permite-lhe convidar alguém para aceder a uma máquina específica sem lhe dar acesso a toda a sua rede.



**Router de sub-rede:** Uma máquina Tailscale pode atuar como gateway para uma sub-rede inteira, permitindo o acesso a dispositivos não Tailscale (IoT, impressoras, etc.) através de uma única máquina configurada.



**Nó de saída:** Utilizar uma máquina como gateway de Internet para sair com o seu IP. Útil para Wi-Fi público ou para contornar restrições geográficas.



**Taildrop:** Uma alternativa segura ao AirDrop, que permite transferir ficheiros entre os seus dispositivos Tailscale, independentemente da plataforma ou localização. Ao contrário do AirDrop, que está limitado ao ecossistema Apple e à proximidade física, o Taildrop funciona entre todos os seus dispositivos (Windows, Mac, Linux, Android, iOS), mesmo que estejam em países diferentes. Os ficheiros são transferidos diretamente entre dispositivos com encriptação de ponta a ponta, sem passar por um servidor central. Utilize a linha de comando `tailscale file cp` ou a aplicação gráfica Interface, dependendo do seu sistema.



### 5.2 Comparação com outras soluções



**Vs OpenVPN:** O Tailscale é muito mais simples de configurar (sem portas para abrir, sem gestão de certificados) mas envolve a dependência de um serviço de terceiros. O OpenVPN é totalmente controlável, mas requer mais experiência.



**Como concorrente direto, o ZeroTier funciona em Layer 2 (Ethernet), permitindo a difusão/multicast, enquanto o Tailscale funciona em Layer 3 (IP). O ZeroTier oferece maior flexibilidade de rede, enquanto o Tailscale favorece a simplicidade de utilização.



**Vs Tor:** O Tor oferece anonimato que o Tailscale não oferece, mas é muito mais lento. O Tor é descentralizado e não requer uma conta, enquanto o Tailscale é mais rápido e oferece uma experiência semelhante a uma LAN.



**Tailscale automatiza toda a gestão de chaves e ligações que o WireGuard em bruto exige que seja tratada manualmente. É essencialmente o WireGuard + um Layer de gestão simplificado.



Em conclusão, o Tailscale posiciona-se como uma solução moderna e orientada para a simplicidade, ideal para utilização pessoal e para pequenas equipas. Para os puristas do controlo total, o Headscale oferece uma alternativa de auto-hospedagem.



## 6. Conclusão



**Vantagens do Tailscale:** O Tailscale oferece várias vantagens para a auto-hospedagem:





- Simplicidade e desempenho** - Instalação rápida em todas as plataformas sem configuração de rede complexa. O tráfego segue o caminho mais direto entre as suas máquinas (malha P2P), com o desempenho do protocolo WireGuard e sem servidor central para limitar o débito.
- Segurança e flexibilidade** - Encriptação de ponta a ponta, superfície de ataque reduzida e funcionalidades avançadas (ACL, autenticação SSO/MFA). Funciona mesmo atrás de NATs ou em movimento, com routers de sub-rede e nós de saída para adaptar a rede às suas necessidades.



**Limites:** Ter também em atenção:





- Dependência externa** - Na sua versão standard, o serviço depende da infraestrutura da Tailscale Inc.. Esta dependência pode ser contornada através do Headscale (alternativa de auto-hospedagem).
- Outros condicionalismos** - Código fonte parcialmente fechado, limitações da versão gratuita para determinadas utilizações avançadas, ausência de suporte para Layer 2 (difusão/multicast) e necessidade de acesso à Internet para estabelecer ligações.



**O Tailscale é ideal para auto-hosts individuais e pequenas equipas, programadores que necessitem de aceder a recursos dispersos, iniciantes em VPN e utilizadores móveis. Para as empresas que necessitam de controlo total, podem ser preferíveis outras soluções, como o Headscale ou o WireGuard diretamente.



**Explore o Headscale para uma auto-hospedagem completa, API e integrações DevOps (Terraform), ou alternativas como o Innernet (semelhante mas totalmente auto-hospedado) e o Netmaker.



O Tailscale é uma ferramenta essencial para a auto-hospedagem, graças à sua simplicidade e eficiência, tornando a sua infraestrutura privada tão acessível como se estivesse na nuvem, mantendo o controlo em casa.



## 7. Recursos úteis



### Documentação oficial





- Centro de Documentação Tailscale**: [docs.tailscale.com](https://docs.tailscale.com) - Documentação completa em inglês, guias de instalação, tutoriais e referências técnicas.
- Como funciona o Tailscale**: [Como funciona o Tailscale](https://tailscale.com/blog/how-tailscale-works) - Artigo detalhado que explica o funcionamento interno do Tailscale.
- Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Acompanhamento de actualizações e novas funcionalidades.



### Guias práticos





- Tutoriais Homelab**: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Guias específicos para auto-hospedagem.
- Configuração de um nó de saída**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Guia detalhado para a configuração de nós de saída.
- Utilizar o Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Transfere ficheiros entre dispositivos Tailscale.



### Comparações





- Tailscale vs. outras soluções**: [tailscale.com/compare](https://tailscale.com/compare) - Comparações detalhadas com outras soluções VPN e de rede (ZeroTier, OpenVPN, etc.).



### Comunidade





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Discussões, perguntas e comentários.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Código-fonte do cliente, onde pode acompanhar o desenvolvimento e comunicar problemas.
- Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Comunidade de utilizadores e programadores.



A Tailscale disponibiliza regularmente novos conteúdos e funcionalidades. Visite o [blogue oficial] (https://tailscale.com/blog/) para obter as últimas notícias e estudos de casos.