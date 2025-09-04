---
name: WireGuard
description: Configurando o WireGuard VPN no Debian e no Windows
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian BURNEL publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original



___



## I. Apresentação



Neste tutorial, vamos aprender a configurar uma VPN baseada no WireGuard, uma solução VPN gratuita e de código aberto que aumenta o desempenho sem descurar a segurança.



O WireGuard é uma solução relativamente recente, estando disponível como uma versão estável desde março de 2020, e teve a honra de ser integrado diretamente no **Kernel do Linux desde a versão 5.6**. Isto não impede que seja acessível a partir de distribuições Linux mais antigas que utilizem uma versão diferente do kernel. Comparado com soluções como o OpenVPN e o IPSec, o WireGuard é mais simples de usar e muito mais rápido, como veremos no final deste artigo.



Alguns pontos-chave sobre o WireGuard:





- Simples, leve e ultra-eficiente!
- Funcionamento apenas por UDP (o que pode ser uma desvantagem ao atravessar determinadas firewalls)
- Funciona num modelo peer-to-peer em vez de cliente-servidor
- Autenticação por chave Exchange, segundo o mesmo princípio que o SSH com chaves privadas/públicas
- Utilização de vários algoritmos: encriptação simétrica com ChaCha20, autenticação de mensagens com Poly1305, bem como outros como Curve25519, BLAKE2 e SipHash24
- Suporta tanto IPv4 como IPv6
- Multi-plataforma: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (e implementado no ProtonVPN)
- Apenas 4.000 linhas de código, em comparação com as centenas de milhares de outras soluções



No que diz respeito à parte criptográfica, os vários algoritmos utilizados são escolhidos a dedo, auditados de várias formas e examinados por investigadores de segurança especializados na matéria.



O sítio Web oficial do projeto: [wireguard.com](https://www.wireguard.com/)



Está convencido desta solução depois de ler esta introdução? Só falta continuar a ler!



## II. Diagrama do Lab WireGuard



Antes de apresentar o meu laboratório para configurar o WireGuard, deve saber que pode imaginar **usar o WireGuard para interligar duas infra-estruturas remotas**, mas também para **conectar um cliente remoto a uma infraestrutura como uma rede corporativa ou a sua rede doméstica**. Isto está no mesmo espírito do OpenVPN, como vimos recentemente no tutorial "[OpenVPN on Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Se o WireGuard não estiver configurado diretamente no roteador ou no firewall, como é possível com o OpenWRT, será necessário configurar o encaminhamento de porta para que o fluxo chegue ao par WireGuard.



![Image](assets/fr/034.webp)



Agora vou falar-vos do meu laboratório e do que vamos preparar hoje.



Vou usar uma máquina Debian 11 como servidor do WireGuard e um cliente Windows como cliente VPN do WireGuard. Embora seja um pouco enganador falar de uma relação cliente-servidor, porque o **WireGuard funciona num modelo "peer-to-peer "**. Isso é um pouco errado quando se está a tentar configurar uma ligação "cliente-para-site". Digamos, em vez disso, que vou ter dois pares ou **dois pontos de ligação WireGuard** se preferir: um em Debian 11 e outro em Windows.



Estes dois pares podem comunicar um com o outro em ambas as direcções, o que significa que a partir da minha máquina Windows posso aceder à LAN remota da máquina Debian 11, e vice-versa: tudo depende da configuração do túnel e da firewall do par WireGuard.



Neste exemplo, vou concentrar-me no seguinte caso: **Do meu Windows Peer 1 ligado à minha rede doméstica, quero aceder à minha rede empresarial para aceder aos servidores da empresa através do túnel VPN WireGuard**. Isto dá o seguinte diagrama:



![Image](assets/fr/035.webp)



Em termos de endereços IP, isto dá:





- Rede doméstica**: 192.168.1.0/24
- Rede corporativa**: 192.168.100.0/24
- Rede de túneis do WireGuard**: 192.168.110.0/24


+ IP Address do Par 1 (Windows) no túnel: 192.168.110.2/24


+ IP Address do Par 2 (Debian) no túnel: 192.168.110.121/24



É tudo o que há para fazer! Passemos à configuração!



**Nota: por padrão, o WireGuard opera no modo UDP na **porta 51820**.



## III Instalação e configuração do servidor WireGuard



Vou usar os termos "cliente" para a máquina Windows e "servidor" para a máquina Debian neste tutorial, porque apesar de ser peer-to-peer, parece mais significativo.



### A. Instalando o WireGuard no Debian 11



O pacote de instalação do WireGuard está disponível nos repositórios oficiais do Debian 11, então tudo o que temos que fazer é atualizar o cache de pacotes e instalá-lo:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



A parte do servidor WireGuard será instalada, juntamente com várias ferramentas que dão acesso a comandos úteis para gerir a configuração.



### B. Instalação de um Interface WireGuard



Utilizando o **comando "wg "** precisamos de generate uma chave privada e uma chave pública: essencial para a autenticação entre dois pares, ou seja, o servidor e um cliente (que também precisará de um par de chaves).



Vamos criar a chave privada "**/etc/wireguard/wg-private.key**" e a chave pública "**/etc/wireguard/wg-public.key**" com esta sequência de comandos:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



O valor da chave pública será devolvido na consola. No arquivo de configuração do WireGuard, precisamos **adicionar o valor da nossa chave privada**. Para recuperar esse valor, digite o comando abaixo e copie o valor:



```
sudo cat /etc/wireguard/wg-private.key
```



É hora de criar um arquivo de configuração em "**/etc/wireguard/**". Por exemplo, podemos nomear este ficheiro "**wg0.conf**", se pensarmos que a rede Interface associada ao WireGuard será "wg0", no mesmo princípio que "eth0", por exemplo.



```
sudo nano /etc/wireguard/wg0.conf
```



Neste ficheiro, temos de adicionar primeiro o seguinte conteúdo (voltaremos a completá-lo mais tarde):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



A secção `[Interface]` é utilizada para declarar a parte do servidor. Aqui estão algumas informações:





- Address**: o IP Address do WireGuard Interface dentro do túnel VPN (sub-rede diferente da LAN remota)
- SaveConfig**: a configuração é guardada (e protegida) durante o tempo em que o Interface estiver ativo
- ListenPort**: A porta de escuta do WireGuard. Neste caso, 51820 é a porta padrão, mas você pode personalizá-la
- PrivateKey**: o valor da chave privada do nosso servidor (*wg-private.key*)



Salve o arquivo e feche-o. Com o comando "**wg-quick**", podemos iniciar este Interface especificando o seu nome (wg0, uma vez que o ficheiro se chama wg0.conf):



```
sudo wg-quick up wg0
```



Se listar os endereços IP do seu servidor Debian 11, verá um novo Interface chamado "wg0" com o IP Address definido no ficheiro de configuração:



```
ip a
```



![Image](assets/fr/027.webp)



No mesmo espírito, podemos visualizar a configuração do Interface "wg0" através do comando "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Finalmente, temos de ativar o arranque automático do nosso WireGuard Interface wg0:



```
sudo systemctl enable wg-quick@wg0.service
```



Por enquanto, vamos deixar de lado a configuração do lado do servidor do WireGuard.



### C. Ativar o reencaminhamento de IP



Para que a nossa máquina Debian 11 seja capaz de **encaminhar pacotes entre redes diferentes (como um router)**, i.e. entre a rede VPN e a rede local, nós precisamos de ativar o [IP Forwarding] (https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Por defeito, esta funcionalidade está desactivada.



Modificar este ficheiro de configuração:



```
sudo nano /etc/sysctl.conf
```



Adicione a seguinte diretiva no final do ficheiro e guarde:



```
net.ipv4.ip_forward = 1
```



É tudo o que há para fazer.



### D. Ativar a máscara de IP



Para que o nosso servidor encaminhe os pacotes corretamente e para que a LAN remota seja acessível à máquina Windows, precisamos de ativar o IP Masquerade no nosso servidor Debian. Este é um tipo de ativação de NAT. Vou fazer essa configuração no firewall Linux através do UFW, que estou acostumado a usar ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Se ainda não tem o UFW e quer configurá-lo (também pode usar o Nftables), comece por instalar o:



```
sudo apt install ufw
```



Antes de mais, é necessário ativar o SSH para não perder o controlo do servidor remoto (adaptar o número da porta):



```
sudo ufw allow 22/tcp
```



A porta 51820 em UDP também deve ser autorizada, uma vez que a utilizamos para o WireGuard (mais uma vez, adapte o número da porta):



```
sudo ufw allow 51820/udp
```



Em seguida, continuaremos com a configuração para habilitar o IP masquerade. Para isso, precisamos recuperar o nome do Interface conectado à rede local. Se não souber o nome, execute "ip a" para ver o nome da placa. No meu caso, é a placa "**ens192**".



![Image](assets/fr/036.webp)



Vamos utilizar esta informação. Edite o seguinte ficheiro:



```
sudo nano /etc/ufw/before.rules
```



Adicione estas linhas no final do ficheiro para **ativar o IP masquerade no Interface ens192** (adaptar o nome do Interface) dentro da string POSTROUTING da tabela NAT da nossa firewall local:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



A imagem mostra:



![Image](assets/fr/037.webp)



Mantenha este ficheiro de configuração aberto e avance para o passo seguinte. 😉



### E. Configuração da firewall Linux para o WireGuard



Ainda no mesmo arquivo de configuração, vamos declarar a rede corporativa "192.168.100.0/24" para que possamos contactá-la. Aqui estão as duas regras a serem adicionadas (idealmente após a secção "*# ok icmp code for FORWARD*" para agrupar as regras):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Se pretender autorizar apenas um anfitrião, por exemplo "192.168.100.11", é fácil:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Agora pode guardar o ficheiro e fechá-lo. Só falta ativar o UFW e reiniciar o serviço para aplicar as nossas alterações:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



A primeira parte da configuração do servidor Debian está agora completa.



## IV. Cliente WireGuard para Windows



O cliente WireGuard está disponível para Windows, macOS, Android, etc... Esta é uma óptima notícia. Todos os downloads estão disponíveis nesta página: [WireGuard Client](https://www.wireguard.com/install/). Neste exemplo, vou configurar o cliente no Windows. Para configurar o cliente WireGuard no Linux, siga o mesmo princípio da criação do arquivo wg0.conf na máquina Debian (sem todo o NAT, etc.).



### A. Instalando o cliente WireGuard para Windows



Depois de ter descarregado o executável ou o pacote MSI, a instalação é simples: basta iniciar o instalador e... voilà, está feito! 🙂



![Image](assets/fr/038.webp)



### B. Criar um perfil do WireGuard



Comece por abrir o software para criar um novo túnel. Para o fazer, clique na seta à direita do botão "**Adicionar túnel**" e clique no botão "**Adicionar túnel vazio**".



![Image](assets/fr/028.webp)



Uma janela de configuração será aberta. Cada vez que uma nova configuração de túnel é criada, o WireGuard gera um par de chaves pública/privada específico para essa configuração. **Nesta configuração, precisamos de declarar o "peer", ou seja, o servidor remoto:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Precisamos de completar esta configuração, em particular para declarar o IP Address neste Interface (*Address*), mas também para declarar o servidor WireGuard remoto através de um bloco [Peer]. A imagem abaixo deve lembrá-lo do ficheiro de configuração que criámos no lado do servidor Linux.



Vamos começar com o bloco `[Interface]`, adicionando o IP Address "**192.168.110.2**"; lembre-se que o servidor tem o IP Address "**192.168.110.121**" neste segmento de rede. Isso dá:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



De seguida, temos de declarar o bloco "Peer" com três propriedades, o que resulta nesta configuração:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Em imagens:



![Image](assets/fr/029.webp)



**Algumas explicações sobre o bloco [Peer]:





- PublicKey**: esta é a chave pública do servidor WireGuard Debian 11 (pode obter o seu valor com o comando "*sudo wg*")
- AllowedIPs**: estes são os endereços IP / sub-redes acessíveis através desta rede VPN WireGuard, neste caso a sub-rede específica para a minha VPN WireGuard (*192.168.110.0/24*) e a minha LAN remota (*192.168.100.0/24*)
- Endpoint**: este é o IP Address do anfitrião Debian 11, uma vez que este é o nosso ponto de ligação WireGuard (terá de especificar o IP público Address)



Por fim, introduza um nome no campo "**Nome**" (sem espaços) e copie e cole a chave pública do cliente, uma vez que teremos de a declarar no servidor. Clique em "**Registar**".



### C. Declarar o cliente no servidor WireGuard



É altura de voltar ao servidor Debian para declarar o "**Peer**", i.e. o nosso PC Windows, na configuração do WireGuard. Antes de mais, precisamos de **parar o Interface "wg0"** de modo a modificar a sua configuração:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Em seguida, modifique o ficheiro de configuração criado anteriormente:



```
sudo nano /etc/wireguard/wg0.conf
```



Nesse arquivo, após o bloco `[Interface]`, precisamos declarar um bloco `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Este bloco [Peer] contém a chave pública do PC Windows 10 (**PublicKey**) e o IP Address do Interface do PC (**AllowedIPs**): o servidor comunicará neste túnel WireGuard apenas para contactar o cliente Windows, daí o valor "**192.168.110.2/32**".



Tudo o que resta é guardar o ficheiro (*CTRL+O e depois Enter e depois CTRL+X via Nano*). Reinicie o Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Para verificar se a declaração de pares funciona, pode utilizar este comando:



```
sudo wg show
```



Uma vez que o host remoto tenha configurado sua conexão WireGuard, seu IP Address será movido para o valor "endpoint".



![Image](assets/fr/033.webp)



Finalmente, vamos proteger os ficheiros de configuração para limitar o acesso root:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Primeira ligação WireGuard



Agora que a configuração está pronta, podemos iniciá-la a partir do PC Windows. Para tal, no cliente "**WireGuard**", clique no botão "**Activate**": a ligação irá **mudar de "Off" para "On "**, mas isso não significa que vá funcionar. Tudo depende se a sua configuração está correta ou não. **Quando a ligação é estabelecida, as nossas duas máquinas comunicam através do Interface WireGuard configurado em cada lado!



![Image](assets/fr/030.webp)



No caso de um problema, este será visível no separador "**Logbook**". Os dois anfitriões enviarão regularmente pacotes Exchange para verificar o estado da ligação, daí as mensagens "*Receiving keepalive packet from peer 1*".



![Image](assets/fr/031.webp)



Se o separador "**Journal**" do WireGuard apresentar uma mensagem como a que se segue, é necessário verificar se as chaves públicas declaradas em ambos os lados estão corretas.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Do meu PC remoto, posso fazer ping do IP Address do meu WireGuard Interface no lado do servidor, bem como de um host na minha LAN remota.



![Image](assets/fr/032.webp)



### E. Desempenho: OpenVPN vs WireGuard



A partir do meu PC remoto ligado à minha VPN WireGuard, consegui aceder a um servidor de ficheiros e transferir um ficheiro através de [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), para ver a taxa de transferência. **Com o WireGuard, o meu máximo é de cerca de 45 Mb/s, o que é ótimo, uma vez que estou em WiFi



![Image](assets/fr/025.webp)



Nas mesmas condições, mas desta vez através de uma ligação OpenVPN (em UDP), com o mesmo funcionamento, o débito é totalmente diferente: cerca de 3 MB/s. A diferença é evidente!



![Image](assets/fr/026.webp)



Isto é interessante, porque se, por exemplo, mudar de uma ligação Wi-Fi para uma ligação 4G/5G, a ligação será tão rápida que a interrupção não será visível.



### F. Bónus: túnel completo WireGuard



Com a configuração atual, parte do tráfego flui através da VPN e o restante através da ligação à Internet do cliente, incluindo a navegação na Internet. Se quisermos mudar para o WireGuard **full tunnel mode**, para que tudo passe pelo túnel VPN, precisamos de fazer algumas alterações à nossa configuração....



Primeiro, é necessário instalar o pacote "resolvconf" no diretório:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Uma vez feito isto, precisa de modificar o perfil "wg0.conf" na máquina Debian: pare o Interface, modifique-o, e reinicie.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Em seguida, **no bloco `[Interface]`, nós adicionamos o servidor DNS a ser usado**. No meu caso, é o controlador de domínio do meu laboratório, mas nós também poderíamos instalar o Bind9 na máquina Debian para ter um resolvedor local.



```
DNS = 192.168.100.11
```



Guardar o ficheiro e, em seguida, reiniciar o Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Por fim, na configuração do túnel na estação de trabalho Windows 10, é necessário modificar a secção "AllowedIPs" para indicar que tudo deve passar pelo túnel. Substituir:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Por:



```
AllowedIPs = 0.0.0.0/0
```



Pode ver que isto também ativa a opção "**Kill switch*".



![Image](assets/fr/040.webp)



Por fim, aproveitei este túnel cheio para efetuar um pequeno ensaio de caudal, cujos resultados são apresentados a seguir:



![Image](assets/fr/039.webp)



A configuração do WireGuard é bastante simples e fácil de entender e, acima de tudo, de manter. **O WireGuard é considerado o futuro das VPNs**, pelo que é melhor estarmos atentos a ele! Também podemos ver que o benefício é significativo em termos de desempenho, o que é uma enorme vantagem para o WireGuard em comparação com o OpenVPN.



Documentação adicional:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Homem - Comando wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**O seu WireGuard VPN está a funcionar! Parabéns!