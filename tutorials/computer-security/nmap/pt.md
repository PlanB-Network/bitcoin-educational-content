---
name: Nmap
description: Master Nmap para mapeamento de redes e análise de vulnerabilidades
---

![cover](assets/cover.webp)



*Este tutorial é baseado no conteúdo original de Mickael Dorigny publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Foram efectuadas alterações ao texto original.*



___



Bem-vindo a este tutorial de introdução ao Nmap, concebido para qualquer pessoa que deseje dominar esta poderosa ferramenta de scanning de redes. O objetivo é fornecer-lhe os conhecimentos fundamentais necessários para utilizar o Nmap de forma eficaz no dia a dia.



O Nmap é uma ferramenta versátil, amplamente utilizada por profissionais de TI, redes e cibersegurança para diagnóstico, descoberta de redes e auditoria de segurança. Este tutorial destina-se àqueles que são novos nestes domínios e desejam aprender os conceitos básicos do Nmap. Recomenda-se um conhecimento básico de administração de sistemas e redes.



Aprenderá as noções básicas do Nmap, como efetuar rastreios de portas, identificar anfitriões activos numa rede, detetar versões de serviços e sistemas operativos, efetuar rastreios de vulnerabilidades e muito mais. Cada secção inclui explicações detalhadas e exemplos práticos para o ajudar a dominar a utilização do Nmap numa variedade de contextos.



Ao final deste tutorial, você terá um sólido entendimento do Nmap e será capaz de usá-lo efetivamente para melhorar a segurança e o gerenciamento de suas redes. Boa leitura.



## 1 - Introdução ao Nmap: O que é o Nmap?



### I. Apresentação



Nesta primeira secção, vamos dar uma vista de olhos à ferramenta de scanning de rede Nmap. Vamos ver os principais Elements que precisa de saber sobre esta ferramenta e como funciona em geral. Isso nos ajudará a entender melhor o resto do tutorial.



### II. Apresentação da ferramenta Nmap



O Nmap, para _Network Mapper_, é uma ferramenta gratuita e de código aberto utilizada para **descoberta de redes, mapeamento e auditoria de segurança**. Também pode ser utilizado para outras tarefas, como **inventário de redes, diagnóstico ou supervisão**.



Ele pode determinar se os hosts em uma rede alvo estão ativos e acessíveis, quais serviços de rede estão expostos, quais versões e tecnologias estão em uso, e outras informações úteis de análise. O Nmap pode ser utilizado para analisar um único serviço numa máquina específica, ou em grandes extensões da rede, até toda a Internet.



Os pontos fortes do Nmap são muitos:





- Poderoso e flexível**: O Nmap pode analisar grandes redes e utilizar técnicas de deteção avançadas. Suporta UDP, TCP, ICMP, IPv4 e IPv6, e pode efetuar deteção de versões, scans de vulnerabilidades ou interações específicas de protocolos. A sua arquitetura é modular, graças, em particular, aos scripts NSE (Nmap Scripting Engine), que veremos mais à frente neste tutorial.
- Facilidade de utilização**: a documentação oficial é abundante e da mais elevada qualidade. Estão também disponíveis inúmeros recursos da comunidade para o ajudar a começar.
- Popularidade e longevidade**: O Nmap tem sido uma referência no seu domínio desde 1998. A versão atual, no momento desta atualização, é a 7.95. Apesar de existirem outras ferramentas para tarefas específicas, o Nmap continua a ser imprescindível para o mapeamento e análise de redes.



**Nmap no cinema*



O Nmap é uma das poucas ferramentas de segurança que adquiriu uma certa notoriedade entre o público em geral. Aparece no filme _Matrix Reloaded_, numa cena emblemática em que Trinity a utiliza para invadir um sistema:



![nmap-image](assets/fr/01.webp)



matriz: Cena recarregada com o Nmap



Participa também noutras obras cinematográficas.



**Feedback



Como administrador de sistemas e depois auditor de cibersegurança e pentester, **utilizo o Nmap quase diariamente** e **recomendo-o regularmente** a administradores de sistemas que pretendam reforçar o seu domínio das redes e melhorar as suas capacidades de diagnóstico.



### III. Funcionamento de alto nível



O Nmap está disponível para Linux, Windows e macOS. É escrito principalmente em C, C++ e Lua (para scripts NSE). É usado principalmente na linha de comando, embora interfaces gráficas como o Zenmap também estejam disponíveis. No entanto, aconselhamos vivamente que comece pela linha de comandos para compreender melhor o seu funcionamento.



Um exemplo simples:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Este comando será explicado em pormenor mais tarde. Neste tutorial, estaremos usando o Nmap no Linux, mas seu uso é similar em outros sistemas. No Windows, o Nmap se baseia na biblioteca **Npcap** (substituindo o agora obsoleto WinPcap) para capturar e injetar pacotes de rede.



O Nmap é utilizado como um binário convencional, como o `ls` ou o `ip`. Algumas funcionalidades avançadas podem requerer direitos elevados, já que a ferramenta às vezes manipula pacotes de formas não convencionais para provocar reações específicas nos sistemas alvo (notavelmente para deteção de serviços ou vulnerabilidades).



### IV. Impacto da utilização do Nmap



Antes de utilizar o Nmap, é essencial estar ciente do seu potencial impacto nas redes e sistemas:





- Pode enviar **milhares ou mesmo milhões de pacotes** num curto espaço de tempo, o que pode saturar certas infra-estruturas de rede.
- Pode generate **pacotes malformados ou não normalizados**, susceptíveis de perturbar certos equipamentos (especialmente sistemas industriais).
- Pode produzir **comportamento semelhante a um ataque**, que pode acionar alertas em sistemas de segurança (firewalls, IDS/IPS, etc.).



De um modo geral, o **Nmap é uma ferramenta muito faladora**, uma vez que gera muito tráfego para extrair o máximo de informação possível. Portanto, é aconselhável entender completamente como ele funciona antes de usá-lo em ambientes sensíveis ou de produção.



### V. Conclusão



Esta secção apresenta o Nmap e as suas principais caraterísticas. Nós vimos que ele é uma ferramenta de mapeamento de rede essencial, poderosa e flexível. Nós também discutimos como ele funciona e as precauções que você precisa tomar ao usá-lo, para preparar o cenário para as próximas partes do tutorial.



## 2 - Porquê utilizar o Nmap?



### I. Apresentação



Nesta secção, vamos dar uma vista de olhos às principais utilizações da ferramenta de exploração de redes Nmap. Veremos que é uma ferramenta amplamente utilizada em muitos contextos e profissões, e que tê-la em sua caixa de ferramentas e saber como dominá-la é definitivamente uma habilidade útil.



### II. Utilização do Nmap para diagnóstico e supervisão



O Nmap pode ser usado para diagnóstico de rede e, mais amplamente, para monitoramento. Da mesma forma que um ping pode ser usado para determinar se dois hosts estão se comunicando, o Nmap pode ser usado para determinar rapidamente se um host está ativo, ou se um serviço em particular está operacional. Graças ao [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), podemos obter dados precisos sobre o tempo de resposta de um hospedeiro, o caminho percorrido pelos pacotes, a resposta dada por um serviço específico, etc.



O seguinte comando e resultado podem ser utilizados, por exemplo, para descobrir rapidamente se um servidor Web no anfitrião **192.168.1.18** está ativo e a responder corretamente:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Utilize o Nmap para obter o estado do serviço Web de um servidor remoto



Portanto, usar o Nmap vai além do famoso "teste de ping" durante as fases de depuração ou diagnóstico. Veremos mais adiante que existem vários métodos usados pelo Nmap para identificar qual serviço está escutando em uma determinada porta, incluindo sua versão.



### III. Utilização do Nmap para mapeamento de redes



Como um _Network Mapper_, o mapeamento de rede é o principal objetivo desta ferramenta. Ele pode ser usado dentro de uma rede local, ou através de múltiplas redes, sub-redes e VLANs, para listar todos os hosts e serviços alcançáveis. O Nmap torna esta tarefa muito mais rápida e eficiente do que qualquer método manual.



Por exemplo, o comando a seguir pode ser usado para identificar rapidamente hosts ativos na rede **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Nota: a opção `-sP` é obsoleta e foi substituída por `-sn`.*



![nmap-image](assets/fr/03.webp)



*Utilizar o Nmap para descobrir anfitriões acessíveis numa rede*



Veremos mais tarde que há vários métodos usados pelo Nmap para determinar se um host pode ser considerado "ativo", mesmo que ele não exponha nenhum serviço a priori.



### IV. Utilizar o Nmap para avaliar uma política de filtragem



O Nmap tem a vantagem de ser factual: os seus resultados permitem estabelecer conclusões concretas, ao contrário de qualquer documento de arquitetura ou política de filtragem. É uma ferramenta fundamental para avaliar a eficácia da compartimentação dos sistemas de informação, uma vez que permite **verificar se a política de filtragem está realmente a ser aplicada**.



Numa rede empresarial, as melhores práticas ditam que os sistemas sejam segmentados de acordo com a sua função, criticidade ou localização. As regras de filtragem (frequentemente implementadas através de firewalls) devem restringir as comunicações entre zonas. Mas estas configurações são frequentemente complexas e susceptíveis de erros.



Assim, para validar que a política foi respeitada, nada melhor do que um teste concreto. Por exemplo, pode verificar se os serviços de administração sensíveis (SSH, WinRM, MSSQL, MySQL, etc.) não estão acessíveis a partir de uma zona de utilizador.



A utilização do **Nmap para testar a política de filtragem** deve ser sistemática antes de essa política ser posta em produção. Infelizmente, esta verificação é frequentemente negligenciada.



Na minha experiência, muitos erros de configuração passam despercebidos na ausência de testes de validação. Um simples erro num intervalo de IPs ou um descuido de regra pode deixar vulnerável uma zona supostamente isolada.



### V. Utilização do Nmap para auditorias de segurança e testes de penetração



O Nmap tem **muitas caraterísticas úteis para avaliação de segurança**, testes de penetração (pentests) e, infelizmente, também para atacantes.



As funções de descoberta de rede são cruciais para um atacante, que precisa de compreender a topologia da rede após um compromisso inicial. Mas o Nmap oferece muito mais do que isso: integra um motor de scripting, **muitos dos quais são dedicados à deteção de vulnerabilidades**.



Por exemplo, este comando pode ser utilizado para verificar se um serviço FTP permite uma ligação anónima, sem ter de se ligar manualmente:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Utilização de um script NSE para verificar a autenticação FTP anónima através do Nmap.*



A deteção de vulnerabilidades do Nmap é um dos primeiros passos numa auditoria ou num teste de penetração. Permite-lhe identificar rapidamente determinados pontos fracos e otimizar os seus esforços de análise.



Mas atenção: **As ferramentas de verificação de vulnerabilidades têm os seus limites**. O Nmap cobre apenas uma fração das ameaças e não garante que um sistema é seguro se não forem detectados problemas. Por isso, é essencial **compreender como funcionam os scripts utilizados** e não confiar apenas no seu veredito.



### VI. Conclusão



Vimos que o domínio do Nmap pode cobrir uma ampla gama de casos de uso, desde diagnósticos e monitoramento até mapeamento, avaliação de políticas de segurança e escaneamento de vulnerabilidades. Na próxima secção, vamos ao que interessa e instalar o Nmap.




## 3 - Instalação e configuração do Nmap



### I. Apresentação



Nesta secção, vamos aprender como instalar a ferramenta de scan de rede Nmap nos sistemas operativos Linux e Windows. No final desta secção, teremos tudo o que precisamos para começar a utilizar o Nmap em módulos futuros. Finalmente, veremos quais os privilégios que pode requerer quando utilizado e porquê.



### II. Instalando o Nmap no Linux



O Nmap foi originalmente concebido para correr em sistemas operativos GNU/Linux. Como resultado, e graças à sua longevidade e popularidade, você vai encontrá-lo em todos os repositórios oficiais das maiores distribuições Unix. Neste tutorial, vou usar um sistema operativo baseado em Debian [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Mas pode usá-lo exatamente da mesma forma a partir de um Debian clássico, CentOS, Red Hat ou qualquer outro!



Em Debian, para verificar se o Nmap está presente nos seus repositórios actuais, pode utilizar o seguinte comando:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



A resposta aqui indica claramente que o pacote "nmap" existe nos repositórios (aqui, os do Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). A partir de agora, pode instalar o Nmap através dos comandos de instalação habituais, nada de desarmante para já 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Para verificar se o Nmap está corretamente instalado, vamos mostrar a sua versão:



```
nmap --version
```



Eis o resultado esperado:



![nmap-image](assets/fr/05.webp)



resultado da apresentação da versão atual do Nmap._



Note a presença neste ecrã da biblioteca "libpcap" (_Packet Capture Library_) e da sua versão. Também usada pelo Wireshark, a "libpcap" é usada pelo Nmap para criar e manipular pacotes e escutar o tráfego da rede.



### III Instalação do Nmap no Windows



Para instalar num sistema operativo Windows, comece por descarregar o binário do site oficial (e de nenhum outro!):





- Página de download do Nmap no sítio Web oficial: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Terá então de descarregar o binário denominado `nmap-<VERSÃO>-setup.exe`:



![nmap-image](assets/fr/06.webp)



página de download do binário de instalação do nmap para Windows



Uma vez que você tenha este binário no seu sistema, simplesmente execute-o para instalar o Nmap. Esta é uma instalação simples, e pode deixar todas as opções como padrão.



Meu reflexo é desmarcar a caixa "zenmap (GUI Frontend)". Este é um Interface gráfico para o Nmap que eu não uso e não será abordado neste tutorial, mas sinta-se à vontade para experimentá-lo depois de dominar a ferramenta de linha de comando do Nmap!



![nmap-image](assets/fr/07.webp)



anulação opcional da seleção do Zenmap ao instalar o Nmap no Windows



No final da instalação do Nmap, é proposta uma segunda instalação: a da biblioteca "Npcap":



![nmap-image](assets/fr/08.webp)



instalação da biblioteca "Npcap" ao instalar o Nmap no Windows



Esta é a biblioteca na qual o Nmap se baseia para gerir as comunicações de rede, ou seja, construir, enviar e receber pacotes de rede. Provavelmente já se deparou com esta biblioteca se utiliza o Wireshark no Windows, uma vez que também a utiliza e requer instalação.



Tal como no Linux, pode validar se o Nmap está instalado abrindo uma Prompt de Comando ou um terminal [Powershell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") e escrevendo o seguinte comando:



```
nmap --version
```



Eis o resultado esperado:



![nmap-image](assets/fr/09.webp)



resultado da apresentação da versão atual do Nmap._



O Nmap está agora instalado no Windows. Pode utilizá-lo exatamente da mesma forma que no Linux, seguindo este tutorial.



### IV. Privilégios locais necessários para utilizar o Nmap



Mas já agora, ao utilizar o Nmap, **é necessário ter privilégios locais elevados no sistema?** A resposta é: **depende**.



Na sua forma mais básica, ou seja, sem ir muito longe na utilização das suas opções, o Nmap não requer necessariamente direitos privilegiados. No entanto, rapidamente se aperceberá que é melhor utilizar o Nmap num contexto privilegiado ("root" no Linux, "administrador" ou equivalente no Windows) para o poder utilizar em todo o seu potencial, correndo o risco de receber uma mensagem de erro como esta:



![nmap-image](assets/fr/10.webp)



mensagem de erro no Linux quando as opções do Nmap requerem direitos de root._



Seja no Linux ou no Windows, há muitos casos em que o Nmap irá pedir-lhe acesso privilegiado. As principais razões são as seguintes (lista não exaustiva):





- Construção de pacotes de rede "brutos "**: O Nmap é capaz de uma ampla gama de métodos de scanning, incluindo manipulação e construção avançada de pacotes. Este é o caso, por exemplo, quando queremos efetuar scans TCP SYN, que não respeitam o clássico _Three-way handshake_ das trocas TCP. Para fazer isso, o Nmap precisa usar funções diferentes daquelas nativas dos sistemas operacionais, que só sabem respeitar as boas práticas em comunicações de rede (ele chama as bibliotecas "Npcap" e "libcap" vistas acima). É porque o Nmap não faz as coisas da maneira "padrão" que ele é capaz de deduzir certas informações sobre SOs, serviços e certas vulnerabilidades.





- Escutar o tráfego de rede**: algumas das opções do Nmap requerem que ele escute a rede para obter certas informações. Esta ação é considerada sensível nos sistemas operativos, uma vez que também permite escutar as comunicações de outras aplicações no sistema. Assim como o Wireshark, o Nmap precisa de privilégios específicos para fazer isso, que são mais fáceis de obter estando diretamente em uma sessão privilegiada.





- Escutar em portas privilegiadas**: nos sistemas operativos, diz-se que as portas de 0 a 1024 (TCP e UDP) são privilegiadas, ou seja, estão de alguma forma reservadas para utilizações muito específicas e, portanto, protegidas. Embora essa seja uma razão um tanto obsoleta hoje em dia, ainda é necessário ter certos privilégios para escutar nessas portas, o que o Nmap pode ter que fazer dependendo de como ele será usado.





- Enviar pacotes UDP:** Da mesma forma, ouvir uma aplicação de rede em portas UDP (um protocolo sem estado) requer direitos privilegiados nos sistemas operativos. Assim, será necessária uma sessão privilegiada se desejar efetuar um scan UDP, para o qual o Nmap terá de ouvir uma resposta de modo a analisar as respostas aos seus scans.




Para ser mais preciso, é possível, pelo menos no Linux, rodar o Nmap com todas as suas funções e opções sem ser realmente o root. Isso é conseguido concedendo as _capacidades_ corretas para o binário. No entanto, isso requer uma manipulação avançada e pode não ser tão prático quanto rodar o Nmap diretamente com privilégios. Além disso, essa abordagem é menos comum e pode causar problemas de segurança se mal configurada.



No entanto, isto é um pouco diferente do nosso tutorial do Nmap, por isso vamos dispensá-lo por agora.



Para o resto deste tutorial, assuma que o Nmap é sempre executado como "root" (a partir de um shell como "root" ou através do comando "sudo"), ou em um terminal de administrador no Windows, mesmo que isso não seja indicado. Caso contrário, poderá sentir diferenças subtis mas visíveis em relação ao tutorial.



### V. Conclusão



E pronto! O Nmap está agora instalado no nosso sistema operativo e pronto a ser utilizado, não necessitando de mais nenhuma configuração. Esta secção conclui a introdução e apresentação do Nmap. Espero que tenha deixado vocês com água na boca, e que estejam ansiosos para começar a praticar.



Numa nota mais séria, temos agora uma ideia melhor do que é a ferramenta de mapeamento Nmap e quais são as suas utilizações mais comuns, bem como as suas limitações. Vamos em frente!




## 4 - Varreduras de portas TCP e UDP com o Nmap



### I. Apresentação



Nesta secção, vamos aprender a realizar os nossos primeiros scans de portas utilizando a ferramenta de scanning de rede Nmap. Veremos como usá-la para compilar uma lista de serviços de rede expostos em um host, seja usando protocolos TCP ou UDP.



A partir de agora, lembre-se de verificar apenas os anfitriões num ambiente controlado para os quais tem autorização explícita.





- Para recordar: [Código Penal: Capítulo III: Ataques a sistemas automatizados de processamento de dados] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Se não tiver um à mão**, recomendo as seguintes soluções gratuitas, que são a solução ideal!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Plataforma de formação em hacking, a Hack The Box disponibiliza constantemente sistemas vulneráveis para que possa atacar como entender. Estão disponíveis várias centenas de sistemas, mas um conjunto renovado de 20 máquinas é oferecido gratuitamente durante todo o ano, com acesso através de uma VPN OpenVPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Esta plataforma oferece inúmeros sistemas intencionalmente vulneráveis para descarregar, que podem ser utilizados através do VirtualBox (também uma solução gratuita) ou por outros meios. Uma vez descarregados, não há necessidade de uma VPN - tudo é local.




Além disso, é livre de **criar uma máquina virtual** no seu sistema operativo favorito e instalar vários serviços nela como alvos de teste. A vantagem aqui será que também poderá ver o que está a acontecer no lado do servidor durante uma verificação, especialmente com o Wireshark, e ter uma mão na firewall local quando fizermos testes mais avançados.



Vamos ser práticos!



### II. Analisar as portas TCP de um anfitrião através do Nmap



#### A. Primeiro scan de portas TCP com o Nmap



Vamos agora realizar as nossas primeiras análises através do Nmap. O nosso objetivo aqui é simples: queremos descobrir que serviços estão expostos pelo servidor Web que acabámos de implementar, para ver se existe algo inesperado, como um serviço de administração que não deveria estar acessível, ou a exposição de um porto de uma aplicação que pensávamos estar descomissionada.



No meu exemplo, o anfitrião a ser analisado tem o IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Aqui está um resultado possível. Vemos um retorno clássico do Nmap com muita informação:



![nmap-image](assets/fr/11.webp)



resultados de um simples scan TCP efectuado com o Nmap._



Dando uma olhada rápida neste resultado, entendemos que as portas TCP/22 e TCP/80 estão acessíveis neste host.



Por predefinição, e se não lhe for dito para o fazer, o Nmap só irá analisar portas TCP.



#### B. Compreender os resultados de um simples scan do Nmap



No entanto, vamos mais longe para compreender este resultado: cada linha é importante, em primeiro lugar, para saber o que acabou de ser feito e, em segundo lugar, para interpretar corretamente os resultados do exame.



A primeira linha é essencialmente um lembrete da versão e da data da verificação (útil para registo e arquivo, afinal!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



A segunda linha mostra o início dos resultados da verificação para o anfitrião "debian.home (192.168.1.19)". Esta informação será útil quando começarmos a analisar vários anfitriões ao mesmo tempo:



```
Nmap scan report for debian.home (192.168.1.19)
```



A terceira linha diz-nos que o anfitrião em questão está "Up", ou seja, ativo:



```
Host is up (0.00022s latency).
```



Finalmente, o Nmap informa-nos que 998 portas TCP identificadas como fechadas não são apresentadas no ficheiro:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Isto poupa-nos quase 1.000 linhas de saída com o aspeto:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Obrigado a ele por nos ter poupado a isto!



Por que 998 portas "fechadas"? Adicionando as 2 portas abertas, chega-se a 1000, e esse é o número de portas que o Nmap irá escanear em sua configuração padrão, não as 65535 portas TCP existentes! Veremos mais tarde que isso é inteiramente e facilmente customizável. Mas se a máquina alvo tiver um serviço escutando numa porta bastante exótica, esse scan "padrão" não o descobrirá.



Após esta informação, encontramos o que é mais interessante: uma tabela organizada de acordo com as três colunas "PORT - STATE - SERVICE":





- A primeira coluna "PORT" simplesmente indica a porta/protocolo de destino, e é importante aqui verificar se é uma porta TCP (`<port>/tcp`) ou UDP (`<port>/udp`).





- A coluna "STATE" indica o estado do serviço de rede descoberto nesta porta e determinado pelo Nmap com base na resposta obtida. Este pode ser "open" (aberto), "closed" (fechado), "filtered" (filtrado) ou "unknown" (desconhecido). Veremos mais tarde como o Nmap distingue estes diferentes estados.





- A coluna "SERVICE" indica o serviço exposto na porta em questão. Note, no entanto, que não utilizámos aqui opções de descoberta de serviços activos. O Nmap baseia-se numa referência local entre um porto/protocolo e o serviço supostamente atribuído: o ficheiro "/etc/services




Se der uma vista de olhos ao ficheiro "/etc/services" num sistema Linux, encontrará uma ligação "port/protocol - service" semelhante à apresentada pelo Nmap:



![nmap-image](assets/fr/12.webp)



extrai o conteúdo do ficheiro "/etc/services" no Linux._



É importante entender que, por enquanto, o Nmap não realizou nenhuma descoberta ativa de serviço. Por exemplo, ele não teria sido capaz de identificar o serviço SSH por trás de uma porta TCP/80 se esse tivesse sido o caso. Daí a importância de saber como utilizar as opções corretas - está para breve!



Saber como interpretar o output do Nmap é uma parte importante do domínio da ferramenta. A boa notícia é que esse resultado será basicamente o mesmo, quaisquer que sejam as opções utilizadas.



#### C. Sob o capô: análise de rede via Wireshark



Se você olhar de perto o que está acontecendo na rede Interface do host que está fazendo o scan do servidor, ou na do próprio servidor, as ações do Nmap serão muito mais claras. É isso que vamos fazer aqui.



O que eu posso mostrar aqui é apenas parte do que é visível no Wireshark. Se quiser ir mais longe, sinta-se à vontade para fazer você mesmo uma captura de rede durante uma verificação e, em seguida, navegar pelo que foi capturado.



Neste teste, o meu anfitrião de análise (192.168.1.18) e o meu anfitrião de destino (192.168.1.19) estão na mesma rede local.



O Nmap começa por descobrir se o anfitrião alvo está ativo na rede local, enviando um pedido ARP. Se receber uma resposta, sabe que o anfitrião está ativo e inicia o scan da rede:



![nmap-image](assets/fr/13.webp)



_Pedido ARP emitido pelo Nmap para determinar se um anfitrião alvo está presente na rede local



Se o anfitrião a ser analisado estiver numa rede remota, o Nmap começa por enviar um pedido de ping e tenta chegar a algumas das portas mais frequentemente expostas (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



pedido de ping emitido pelo Nmap para determinar se um anfitrião alvo está acessível numa rede remota



Se obtiver uma resposta a qualquer um destes testes, considera que o alvo está ativo.



Uma vez que o Nmap tenha determinado que seu alvo está ativo, ele tentará resolver seu nome de domínio com o servidor DNS configurado na placa de rede:



![nmap-image](assets/fr/15.webp)



resolução dNS no alvo de scan do Nmap



Agora que o Nmap identificou seu alvo e sabe que ele está ativo, ele inicia o scan da porta TCP:



![nmap-image](assets/fr/16.webp)



tCP Transmissão de pacotes SYN e receção de RST/ACK durante a varredura do Nmap



Para fazer isso, ele irá, em cada porta TCP em seu intervalo padrão, **enviar pacotes TCP SYN e esperar por uma resposta**. Na captura de tela acima, ele recebe pacotes TCP RST/ACK do servidor examinado, o que significa "siga em frente, não há nada para ver aqui" - em outras palavras, essas portas estão fechadas. Como vimos no resultado, este será o caso para a maioria das portas analisadas. Com duas excepções:



![nmap-image](assets/fr/17.webp)



resposta a um pacote TCP SYN enviado na porta 22, ativo no alvo da pesquisa



Na captura de ecrã acima, vemos um pacote TCP SYN/ACK enviado pelo anfitrião alvo**. A porta está ativa e expõe um serviço. O Nmap acusa a receção da resposta e depois termina a ligação (TCP RST/ACK). **Foi assim que o Nmap soube que o porto TCP/22 estava ativo**.



Vimos aqui que o Nmap respeita o "Three Way Handshake" (Aperto de Mão de Três Vias) ao fazer o scan numa rede TCP. Por razões de desempenho, é possível pedir que ele não responda ao retorno do servidor, economizando assim vários milhares de pacotes ao escanear uma rede grande. Mas veremos estas opções e optimizações mais à frente no tutorial.



Nós agora temos uma idéia melhor de como fazer um scan TCP e o que realmente acontece quando ele é executado. Nós também vimos que, por padrão, o Nmap executa um scan de porta TCP num número limitado de portas.



### III. Analisar portas UDP com o Nmap



#### A. Primeiro scan de portas UDP com o Nmap



Agora vamos ver como escanear as portas UDP de um host. Como vimos, por padrão, o Nmap sempre faz o scan de portas TCP. Isso pode significar perder muita informação se não estivermos cientes disso.



Como lembrete, para os fins deste teste, meu host de verificação (192.168.1.18) e meu host de destino (192.168.1.19) estão na mesma rede local.



```
nmap -sU 192.168.1.19
```



Aqui, o retorno obtido tem o mesmo formato de uma verificação TCP, mas os serviços ativos exibidos estão em `<port>/UDP`, conforme solicitado!



![nmap-image](assets/fr/18.webp)



resultado de um simples scan UDP efectuado com o Nmap._



A opção "-sU" é usada para dizer ao Nmap que você quer trabalhar com UDP, ao invés de TCP como é o padrão.



A propósito, provavelmente notará que o Nmap requer direitos de "root" para scans UDP, como mencionado anteriormente no tutorial.



nota: Desde as versões mais recentes do Nmap, recomenda-se sempre que as análises UDP sejam efectuadas com privilégios de administrador para garantir resultados fiáveis, uma vez que algumas funcionalidades requerem um acesso não formal às tomadas de rede



Os scans UDP podem demorar muito tempo (1100 segundos para efetuar um scan a 1000 portas no meu exemplo), devido à ausência do "Three Way Handshake" no UDP, o que significa que o Nmap irá esperar por um retorno para cada pacote UDP enviado, e irá determinar a porta como "fechada" apenas se não houver retorno após um determinado tempo (timeout). Essa resposta dos hosts escaneados não é sistemática e é frequentemente limitada em termos do número de respostas por segundo, para evitar certos ataques de amplificação. Isto contrasta com o TCP, em que há uma resposta imediata do anfitrião verificado, quer o porto esteja aberto ou fechado. Veremos mais tarde como otimizar isto.



Uma segunda dificuldade com o UDP é **que os serviços nem sempre respondem aos pacotes de entrada**, simplesmente porque isso nem sempre é necessário e é o princípio do UDP. Quando este é o caso, e nenhum ICMP "port unreachable" é recebido, o serviço é marcado como "open|filtered" pelo Nmap, como mostrado na captura de ecrã acima.



#### B. Sob o capô: análise de rede via Wireshark



Assim como no nosso scan TCP, vamos dar uma olhada mais de perto no que acontece a nível de rede durante um scan UDP usando uma análise do Wireshark. O comportamento do Nmap para determinar se um host está ativo é o mesmo.



A única diferença real quando o scanning UDP é que o Nmap não espera por um "Three Way Handshake", uma vez que este mecanismo não existe no UDP (protocolo sem estado):



![nmap-image](assets/fr/19.webp)



transmissão de pacotes uDP e receção de ICMP (porta inalcançável) durante a exploração do Nmap



Podemos ver na imagem de ecrã acima que o Nmap envia um grande número de pacotes UDP e recebe, para a maioria deles, um pacote ICMP "Destination unreachable (Port unreachable)" em resposta. Isso é normal, pois é a resposta apropriada definida pela [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") quando uma porta UDP está inacessível:



![nmap-image](assets/fr/20.webp)



extrato do RFC 1122._



Vamos dar uma olhada mais de perto nesta captura do Wireshark, que mostra **os três cenários possíveis** em UDP:



![nmap-image](assets/fr/21.webp)



captura de rede durante um scan UDP em diferentes portas com o Nmap._



Os três casos são os seguintes:





- O primeiro Exchange é constituído pelos pacotes n. 3, 4 e 8, 9. O Nmap envia pacotes UDP na porta SNMP clássica e, por conseguinte, **constrói antecipadamente pacotes compatíveis com o protocolo**. Em seguida, obtém uma resposta do servidor (pacotes n.ºs 8 e 9). Resultado: O Nmap recebeu uma resposta, o serviço está "aberto".





- O segundo Exchange consiste nos pacotes 6 e 7. O Nmap envia um pacote UDP "vazio" (sem estrutura de protocolo) para a porta UDP/165 e recebe um pacote ICMP em resposta: "Destination unreachable (Port unreachable)" (Destino inalcançável (Porta inalcançável)). Resultado: O Nmap recebeu uma resposta (negativa), o anfitrião está ativo, mas o serviço que tentou alcançar não está operacional nesta porta, que será marcada como "fechada".





- O último Exchange consiste no pacote n.º 12: o Nmap envia um pacote UDP "vazio" para o porto UDP/1235. Não há resposta, nem mesmo uma recusa explícita do host escaneado. Resultado: O Nmap marca o porto como "aberto|filtrado", uma vez que é incapaz de dizer se tal se deve à presença de uma firewall, configurada para não responder, ou a um serviço UDP ativo que, de qualquer modo, não devolve qualquer resposta (não obrigatório em UDP).




Eis o resultado apresentado pelo Nmap após estes três casos:



![nmap-image](assets/fr/22.webp)



resultados possíveis de um scan UDP efectuado através do Nmap._



Agora temos uma idéia melhor de como fazer um scan UDP e o que realmente acontece quando ele é realizado. Até agora nós estávamos usando o Nmap de uma maneira muito simples, sem realmente decidir quais portas escanear, mas isso está prestes a mudar!



### IV. Afinação do scanning de portas com o Nmap



#### A. Lembrete do comportamento padrão do Nmap



Como vimos, o próprio Nmap escolhe o número e as portas a serem escaneadas se você não especificar nenhuma opção. Esta é a configuração "padrão" usada pelo Nmap quando não lhe dizemos exatamente o que fazer. Estas opções predefinidas foram concebidas para dar uma ideia dos principais portos expostos, sendo estes selecionados por frequência de exposição (portos mais comuns ou frequentes) em vez de por ordem numérica (porto 1, 2, 3, etc.) e também para evitar iniciar um scan dos 65535 portos possíveis se não especificar as opções apropriadas, o que seria demasiado longo e prolixo para um caso de utilização "predefinido".



**Como é que estes portos são escolhidos?



As 1000 portas analisadas no modo predefinido são escolhidas de acordo com a sua frequência de ocorrência. Estas estatísticas são mantidas pelo Nmap e actualizadas da mesma forma que o próprio binário e os seus scripts (módulos). Pode ver estas estatísticas no ficheiro "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



extraído do ficheiro "/usr/shares/nmap/nmap-services"._



Aqui, na terceira coluna, vemos o que parece ser probabilidades (entre 0 e 1) ou uma distribuição percentual. Esta é a frequência de ocorrência de cada par porta/protocolo. Podemos ver que as portas mais conhecidas (FTP, SSH, TELNET e SMTP neste extrato) têm um valor muito mais elevado do que as outras.



#### B. Especificar com precisão as portas alvo para um scan do Nmap



No entanto, no mundo real, podemos precisar escanear apenas uma porta específica, ou várias portas, ou um intervalo específico de portas. O Nmap facilita fazer exatamente isso, de maneira uniforme, tanto para escaneamentos UDP quanto TCP.



**Verificar uma porta específica através do Nmap



Se quisermos analisar uma única porta, e não 1000, podemos especificar essa porta através da opção "-p" ou "--port" do Nmap:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Como resultado, o scan será naturalmente muito mais rápido e o Nmap só emitirá os pacotes necessários para detetar se o host está ativo, e então se a porta especificada está acessível. Isso economiza tempo se você quiser apenas fazer um teste rápido para ver se o serviço web no seu site de demonstração ainda está ativo.



**Verificar várias portas através do Nmap



Da mesma forma, podemos especificar vários portos ao Nmap, utilizando a mesma opção e concatenando os portos especificados com uma vírgula:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Independentemente da ordem, o Nmap irá verificar todas essas portas, e apenas aquelas no host alvo. Você notará na saída do Nmap que ele **explicitamente nos diz todas as portas e seus status**, mesmo se elas estiverem "fechadas". Ao contrário do comportamento padrão, onde essa saída completa ocuparia muito espaço:



![nmap-image](assets/fr/24.webp)



*Resultado de um scan TCP do Nmap nos portos indicados



**Verificar uma série de portas



Se o número de portas que pretende analisar for demasiado grande, pode especificá-las por intervalo, por exemplo:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



É claro que pode misturar e combinar como achar melhor, por exemplo:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Verificação de portas TCP e UDP



Também é possível efetuar análises UDP e TCP ao mesmo tempo, em portas selecionadas:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Neste último exemplo, notará a presença de "U:" para indicar uma porta UDP e "T:" para indicar uma porta TCP. Aqui está um possível resultado desse tipo de varredura:



![nmap-image](assets/fr/25.webp)



*Resultado de um scan de portas TCP e UDP com o Nmap.*



Esta é uma forma interessante de personalizar as suas digitalizações!



**Verificar todas as portas



Finalmente, é possível especificar intervalos muito maiores ou menores para o Nmap. Nós vimos que a lista padrão selecionada pelo Nmap contém 1000 portas. Nós também podemos pedir as 100 portas mais frequentes, ou as 200 mais frequentes, usando a opção "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Finalmente, podemos pedir-lhe para analisar todas as portas possíveis (todas as 65535), utilizando a notação "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Este último demorará mais tempo, especialmente com o UDP, mas não perderá nenhuma porta aberta.



*Nota: A opção "-p-" é o método recomendado para efetuar o rastreio de todas as portas TCP. Para rastreios UDP, é aconselhável limitar o número de portas por motivos de desempenho, uma vez que os rastreios completos de todas as portas UDP podem demorar muito tempo.*



Mais adiante no tutorial, veremos como otimizar a velocidade dos scans do Nmap para atender às nossas necessidades, o que será particularmente útil para scans em todas as portas TCP e UDP.



### V. Conclusão



Nesta secção, temos finalmente alguma prática, por isso agora sabemos **como utilizar o Nmap de uma forma básica para analisar as portas TCP e UDP de um anfitrião**. Também vimos em detalhes o que está acontecendo no nível da rede e **como o Nmap determina se uma porta TCP ou UDP está ativa ou não**. Finalmente, nós sabemos como selecionar as portas que queremos escanear e **o que as opções padrão do Nmap realmente fazem**. No que se segue, vamos reutilizar este conhecimento e aplicá-lo ao scan de uma rede inteira, incluindo mapeamento global e descoberta de rede.




## 5 - Mapeamento e descoberta de redes com o Nmap



### I. Apresentação



Nesta secção, vamos aprender a utilizar a ferramenta de scan de rede Nmap para mapear a sua rede. Veremos como pode ser eficaz nesta tarefa, através das suas várias opções. Finalmente, veremos diferentes formas de especificar os alvos dos nossos scans para o Nmap.



Em particular, vamos utilizar o que aprendemos na secção anterior sobre como o Nmap determina se um anfitrião está ativo e acessível.



Como mencionado na introdução ao Nmap, este é um Mapeador de Rede. Como tal, é a ferramenta perfeita para desenhar uma lista de hosts acessíveis numa rede, seja ela local ou remota.



**Regresso do autor:**



De facto, como auditor de cibersegurança e pentester, utilizo sistematicamente o Nmap quando realizo testes de penetração internos para saber onde estou, quem são os meus vizinhos na rede local e que outras redes estão acessíveis, bem como os sistemas nelas localizados. O meu objetivo é simples: mapear a rede, determinar a dimensão do sistema de informação e, em particular, esboçar a sua superfície de ataque.



O mapeamento da rede também pode ser útil no contexto do diagnóstico da rede, da supervisão, do mapeamento de activos (tem mesmo a certeza de que o seu SI é constituído apenas pelo que está no Active Diretory ou no seu inventário GLPI/OCS? Também pode ser utilizado para detetar a presença de TI sombra no seu sistema de informação.



### II. Utilizar o Nmap para analisar uma gama de redes



#### A. Descobrir uma rede com um scan do Nmap



Gostaríamos agora de passar para um nível superior e analisar toda a nossa rede local. Nada poderia ser mais simples: tudo o que precisamos de fazer é reutilizar os comandos que vimos na secção anterior, mas especificando um CIDR em vez de um simples IP Address.



Um CIDR (**Classless Inter Domain Routing**) é a notação "clássica" para especificar um intervalo de rede e a sua extensão (utilizando a máscara). Por exemplo, "192.168.0.0/24" é uma "tradução" da notação de máscara decimal "255.255.255.0".



Para utilizar o Nmap especificando um CIDR, podemos utilizá-lo da seguinte forma



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Também é possível, tal como acontece com os portos na secção anterior, especificar vários anfitriões, várias redes ou um intervalo:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Aqui está um exemplo dos resultados que podemos obter ao executar uma verificação numa rede:



![nmap-image](assets/fr/26.webp)



resultados de uma análise do Nmap para mapear várias redes



Em particular, vemos vários anfitriões activos, e cada secção de anfitrião começa com uma linha como esta:



```
Nmap scan report for <name> (<IP>)
```



Isto permite-nos ver claramente a que hospedeiro se referem os resultados seguintes. A última linha também é importante:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Sabemos que, nas redes analisadas, o Nmap descobriu 5 hosts activos.



#### B. Sob o capô: análise de rede via Wireshark



Vamos agora ver mais de perto o que acontece ao nível da rede durante uma descoberta de rede efectuada através do Nmap.



Como vimos na secção anterior, por defeito o Nmap utiliza o protocolo ARP para detetar a presença de hospedeiros na rede local:



![nmap-image](assets/fr/27.webp)



pacotes aRP capturados durante a exploração de uma rede local utilizando o Nmap e as suas opções predefinidas



Assim, é capaz de detetar praticamente todos os anfitriões da rede local, uma vez que a resposta a um pedido ARP é geralmente fornecida por todos os anfitriões activos na rede e não parece suspeita de forma alguma.



Para redes remotas, o Nmap utiliza uma combinação de técnicas:



![nmap-image](assets/fr/28.webp)



pacotes iCMP e TCP capturados durante a exploração de uma rede remota utilizando o Nmap e as suas opções predefinidas



Para ser mais preciso, o Nmap utiliza um pacote ICMP echo (o caso clássico do ping) e um pacote ICMP Timestamp, normalmente utilizado para calcular os tempos de trânsito dos pacotes. Ele espera obter uma resposta de hosts em redes remotas.



Mas há mais do que isso. Pode ver-se na captura do Wireshark acima que os pacotes **TCP SYN** são sistematicamente enviados para as portas TCP/443 de todos os potenciais hospedeiros das redes a analisar, bem como os pacotes **TCP ACK** para a porta TCP/80.



**Por que enviar pacotes TCP para portas como parte da descoberta de rede?



Enviar um pacote SYN para uma determinada porta permite ao Nmap **determinar se um serviço está à escuta nessa porta**. Se um host responde a um pacote SYN com um pacote SYN/ACK, isso indica que ele está ativo e que um serviço está escutando naquela porta. Assim, o Nmap tenta a sua sorte neste serviço, **mesmo que não tenha sido obtida qualquer resposta ao ping**.



Enviar um pacote ACK para uma determinada porta permite que o Nmap **determine se um firewall está presente naquele host**. Se um host responde a um pacote ACK com um pacote RST (Reset), isso indica que um firewall provavelmente está presente nesse host e bloqueando o tráfego não solicitado. O anfitrião revela assim a sua presença na rede, mesmo que não tenha respondido a outros pedidos.



É importante notar, no entanto, que a deteção de firewall usando esta técnica pode não ser perfeitamente fiável em todos os casos. Alguns hosts podem ter respostas generate RST por outros motivos que não a presença de um firewall, como um serviço específico ou a configuração do sistema operacional. Além disso, os firewalls modernos podem ser configurados para não responder a tentativas de descoberta desse tipo.



Nós já percorremos um longo caminho e podemos realizar uma descoberta básica de rede. Vamos agora olhar para mais algumas opções que nos darão maior controlo sobre o comportamento do Nmap.



### III. Descoberta de redes sem scan de portas com o Nmap



Como você deve ter notado, por padrão o Nmap **realiza um scan de portas após a descoberta de um host ativo**, o que adiciona uma enorme quantidade de pacotes e espera por respostas ao nosso scan. Se tiver 5 hospedeiros na sua rede, o Nmap irá tentar verificar o estado de cerca de 5.000 portos, o que irá demorar mais tempo.



No entanto, é possível utilizar as opções do Nmap para efetuar **apenas uma descoberta de anfitriões activos** numa rede, sem descobrir os seus serviços.



Se quisermos apenas saber quais hosts estão acessíveis, sem qualquer informação sobre os serviços e portas que eles expõem, então podemos usar a opção "-sn" para executar **apenas uma varredura usando ICMP Echo (ping) e solicitações ARP**. Por outras palavras, desativar completamente o rastreio de portas:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Aqui está o resultado de uma descoberta de rede do Nmap realizada sem varredura de porta:



![nmap-image](assets/fr/29.webp)



Resultado de uma descoberta de rede sem scan de portas com o Nmap.



Já mencionámos as possíveis limitações de utilizar apenas o ICMP para a descoberta de anfitriões (para redes remotas). É por isso que o Nmap também usa alguns truques que podem trair a presença de um firewall ou serviço específico em hosts. Com a ajuda de opções, nós podemos reutilizar esses truques e até mesmo estendê-los, sem ter que começar novamente com um scan de portas completo de cada host descoberto.



Para fazer isso, usaremos as opções "-PS" (TCP SYN) e "-PA" (TCP ACK), que nos permitirão especificar as portas às quais queremos nos juntar como parte de nossa descoberta de host, bem como a opção "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Esta verificação já garante que a descoberta do anfitrião é um pouco mais completa do que com as opções predefinidas.



Estamos a começar a obter comandos bastante abrangentes, utilizando múltiplas opções. Isso é porque nós sabemos como o Nmap funciona e as limitações de suas opções "padrão", que às vezes podem nos fazer perder tempo ou deixar passar um Elements importante. Esse é o objetivo de dedicar um tempo para dominá-lo!



Para pormenorizar as opções da nossa última encomenda:





- "`-sn`: desativa o rastreamento de portas para cada host ativo descoberto pelo Nmap.





- "`-PP`: ativa o eco ICMP (ping scan) para a descoberta de anfitriões.





- "`-PS <PORT>`": envia um pacote TCP SYN na(s) porta(s) indicada(s) para detetar qualquer serviço ativo que traia a presença de um anfitrião que não tenha respondido ao ping.





- "`-PA <PORT>`": envia um pacote TCP ACK na(s) porta(s) indicada(s) para detetar qualquer firewall ativa que denuncie a presença de um anfitrião que não tenha respondido ao ping.




No exemplo acima, eu especifico as portas que considero serem as mais frequentemente expostas nos meus contextos do Nmap para a opção "-PS". Essas diferentes portas serão então testadas em cada hospedeiro, não para ver se o serviço que hospedam está realmente ativo, mas para ver se isso nos permite descobrir um hospedeiro que não respondeu ao nosso ICMP Echo enquanto ainda está ativo (através de uma resposta do serviço ou do firewall do hospedeiro).



Eis o que pode ser visto numa captura de rede obtida no momento de uma análise deste tipo, neste caso uma extração num único anfitrião alvo:



![nmap-image](assets/fr/30.webp)



pacotes enviados pelo Nmap durante a descoberta avançada de redes, sem rastreio de portas



Encontramos os nossos pacotes TCP SYN, o nosso TCP ACK na porta TCP/80 e o nosso ICMP echo. O Nmap realizará todos esses testes para cada host visado pelo nosso scan de descoberta de rede.



### IV. Utilizar um ficheiro de recursos como alvo do Nmap



Especificar alvos pode rapidamente se tornar complexo em sistemas de informação reais, que podem ser compostos por dezenas ou centenas de redes, sub-redes e VLANs. É por isso que é mais fácil utilizar um ficheiro como fonte para o Nmap do que especificá-los um a um na linha de comandos.



Para começar, crie um ficheiro simples com uma entrada por linha:



![nmap-image](assets/fr/31.webp)



ficheiro que contém um destino (anfitrião ou rede) por linha



Em seguida, podemos usar todas as opções do Nmap vistas até agora e especificar a opção "-iL <path/file>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



O Nmap irá então incluir no seu scan todos os alvos contidos no nosso ficheiro.



Se quiser ter a certeza de que todos os seus alvos serão tidos em conta, pode utilizar a opção "-sL -n". O Nmap irá então apenas interpretar os CIDRs e hosts no ficheiro e mostrá-los, sem enviar quaisquer pacotes através da rede:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Isto assegura que a lista de anfitriões a serem verificados é exacta.



Uma última dica importante que gostaria de partilhar convosco diz respeito à **exclusão do anfitrião ou da rede como parte de uma verificação**. Esta necessidade de excluir um anfitrião pode ser necessária em vários casos, especialmente se quisermos ter a certeza de que **um componente sensível do sistema de informação não é perturbado ou interrompido pelas nossas análises**.



Exemplos frequentes de tais necessidades são os casos em que uma empresa possui equipamento industrial (PLC) ou de saúde. Esses equipamentos são, por vezes, mal concebidos e não se destinam de todo a receber pacotes mal formatados ou em excesso. Por razões óbvias de disponibilidade ou de risco comercial/humano, é preferível excluí-los dos testes.



Para excluir endereços IP ou redes do nosso scan, podemos utilizar a opção "--exclude" do Nmap, por exemplo:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



Neste exemplo, estou a analisar a rede "192.168.1.0/24" mas a excluir o anfitrião "192.168.1.140" aí localizado. Nenhum pacote será enviado pelo Nmap para esse host. Outro exemplo com exclusão de sub-rede:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Da mesma forma, faço o scan da grande rede "10.0.0.0/16", mas a rede "10.0.100.0/24" não será analisada. Mais uma vez, recomendo a utilização da opção "-sL -n" para obter uma visão muito clara dos anfitriões que serão verificados e dos que serão excluídos da verificação, especialmente se estiver a operar num contexto sensível.



### V. Descoberta da rede e exploração de portas



Nós podemos agora combinar o que aprendemos nesta secção com o que aprendemos na secção anterior sobre as opções de scan de portas. Por padrão, nós vimos que o Nmap irá escanear as 1000 portas mais freqüentes em cada host ativo que ele descobrir. Vimos como evitar esse comportamento se não o quisermos, mas podemos controlá-lo totalmente, e até mesmo estendê-lo se for adequado às nossas necessidades.



Por exemplo, o seguinte comando irá verificar a presença de um serviço de escuta na porta TCP/22 em cada anfitrião analisado:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



O Nmap irá primeiro realizar uma descoberta de rede para listar os hosts ativos e, para cada um deles, verificar se um serviço está presente na porta TCP/22.



Da mesma forma, podemos efetuar uma verificação completa de todas as portas TCP em cada anfitrião descoberto na rede "192.168.0.0/24", excluindo o anfitrião "192.168.0.4", por exemplo:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



É livre de combinar todas as opções que aprendemos até agora de acordo com as suas próprias necessidades.



### VI. Conclusão



Nesta secção, nós vimos como usar o Nmap para mapear a rede usando várias opções. Nós agora temos um entendimento mais afinado dos alvos dos nossos scans, assim como o comportamento do scan de portas do Nmap e o método de descoberta de hosts. E o mais importante, sabemos qual é o comportamento padrão e as limitações do Nmap, e como usar suas principais opções para ir além.



Na próxima secção, veremos os mecanismos e opções para descobrir as versões dos serviços e sistemas operativos analisados pelo Nmap.




## 6 - Detetar versões de serviços e sistemas operativos com o Nmap



### I. Apresentação



Nesta secção, vamos aprender a utilizar o Nmap para descobrir e detetar com precisão as versões dos serviços e sistemas operativos utilizados pelos anfitriões analisados. Veremos em pormenor como o Nmap realiza esta tarefa, bem como as limitações da ferramenta para melhor compreender e interpretar os seus resultados.



Como vimos nas seções anteriores deste tutorial, por padrão, o Nmap não vai procurar saber qual serviço está exposto nas portas que ele escaneia e considera abertas. Então, se você estiver escutando um serviço web na porta TCP/22, o Nmap continuará a reportá-lo como aberto, mas como um serviço `SSH`. Isso acontece porque ele utiliza um [banco de dados](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) local do seu sistema para procurar por uma relação entre uma porta/protocolo e o nome de um serviço (o arquivo `/etc/services/`).



Na maioria dos casos, o [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) irá fornecer-lhe a informação correta, uma vez que é raro encontrar tais casos num ambiente de produção. No entanto, os restantes casos serão situações em que um serviço clássico ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, etc.) está exposto num porto não clássico (por exemplo, 2022 para um serviço SSH), caso em que o Nmap não encontrará uma correspondência na sua base de dados local, ou uma que não corresponde à realidade, e perderá informação importante.



Felizmente, o Nmap oferece opções e mecanismos muito precisos para descobrir que serviço exato pode estar escondido atrás de um porto aberto. Até tem uma base de dados de consultas e assinaturas para identificar tecnologias e versões exactas. Para além dos serviços, o Nmap também pode identificar a tecnologia utilizada e a sua versão.



É isso que vamos analisar nesta secção.



### II. Como detetar uma tecnologia ou versão



#### A. Lembrete de como identificar uma tecnologia ou versão



A identificação de uma tecnologia e de uma versão envolve a recuperação do nome do serviço, CMS, aplicação ou software que está a escutar na porta de destino. Por exemplo, uma página Web é gerida por um CMS (`WordPress`), executada por um serviço Web (`Apache`, IIS, Nginx) e alojada num servidor (Linux ou Windows). Mas como saber qual o serviço Web que está a ser executado?



A metodologia clássica para descobrir essas informações é o _banner grabbing_, que consiste simplesmente em localizar onde o serviço em questão exibe essas informações e ler os dados. Muitas vezes, na sua configuração ou processamento por defeito, os serviços apresentam o seu nome e até a sua versão como primeira resposta após uma ligação.



![nmap-image](assets/fr/32.webp)



apresentar uma versão assim que uma ligação TCP é estabelecida por um serviço FTP



Aqui vemos que uma simples conexão TCP com este serviço via `telnet` resulta em um pacote TCP contendo sua tecnologia e versão.



Assim que tiver uma ideia do tipo de serviço com que está a lidar, pode também enviar comandos ou pedidos específicos a esse serviço para extrair informações do mesmo. Estes pedidos/comandos também podem ser enviados às cegas (sem ter a certeza de que se trata do tipo de serviço correto), na esperança de que um deles provoque uma resposta do serviço em questão.



Noutros casos, mais avançados, é necessário enviar pacotes específicos para provocar uma reação, como um erro, que fornecerá informações pormenorizadas sobre a versão ou a tecnologia utilizada.



Como se pode imaginar, o Nmap utilizará todas estas técnicas para tentar identificar o tipo exato de serviço alojado num porto, bem como o nome da sua tecnologia e versão.



#### B. Entendendo as Sondas e Correspondências do Nmap



Para efetuar todas estas verificações em cada porta analisada, o Nmap utiliza uma base de dados local que é frequentemente actualizada (tal como o binário ou os seus módulos). Este é um ficheiro de texto com vários milhares de linhas: `/usr/share/nmap/nmap-service-probes`.



Este ficheiro é composto por várias entradas, todas organizadas em torno de duas orientações principais:





- A `Probe`: esta é a definição do pacote que o Nmap irá enviar na tentativa de provocar uma reação do serviço a ser identificado. Pense nisso como uma tentativa cega como _Hello? Guten Tag? Olá? Um... Buenos Dias talvez?_. Assim que o serviço alvo receber uma sonda que ele entenda (ou seja, falando o protocolo correto), ele responderá ao Nmap, que então terá a confirmação do tipo de serviço que ele é.





- Match": estas são expressões regulares que o Nmap aplica à resposta obtida. Se o envio de um pedido HTTP GET provocou uma resposta do serviço, o Nmap aplicará dezenas de expressões regulares a essa resposta para identificar a presença de, por exemplo, a palavra `Apache`, `Nginx`, `Microsoft IIS`, etc.




Existem algumas outras diretivas para casos específicos, mas as principais para entender como o Nmap funciona e personalizar seu uso são estas. Para tornar essa parte teórica mais concreta, aqui está um exemplo:



![nmap-image](assets/fr/33.webp)



exemplo de uma sonda no ficheiro `/usr/share/nmap/nmap-service-probes` do Nmap



Na primeira linha deste exemplo, vemos um Probe fácil de entender chamado `GetRequest`. Este é um pacote TCP que contém uma solicitação HTTP GET vazia para a raiz do serviço Web usando HTTP/1.0, seguida por um avanço de linha e uma linha vazia.



A linha `ports` diz ao Nmap para qual porta enviar este Probe. Isso permite priorizar os testes e economizar tempo.



Finalmente, temos dois exemplos de `match`. O primeiro, por exemplo, categorizará o serviço web verificado como `ajp13` se a expressão regular contida nesta linha corresponder à resposta do serviço recebido.



Para o ajudar a compreender o aspeto das Sondas, eis uma lista de algumas das Sondas que encontrará neste ficheiro (existem 188 no total no momento da redação deste tutorial).



![nmap-image](assets/fr/34.webp)



exemplo de várias sondas utilizadas pelo Nmap e presentes no ficheiro `/usr/share/nmap/nmap-service-probes`._



As duas primeiras (chamadas `NULL` e `GenericLines`) são de particular interesse aqui, pois elas simplesmente enviam um pacote TCP vazio ou um pacote contendo uma quebra de linha. Os serviços de servidor muitas vezes anunciam-se precisamente assim que uma ligação é recebida, sem qualquer ação específica, comando ou pedido do cliente.



Eis o caso de um _match_ ligeiramente mais complexo:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



A expressão regular exacta está contida aqui entre o `m|` e o `|`, que delimita qualquer expressão regular neste ficheiro. Por favor, reserve um tempo para ler este exemplo inteiro. Irá notar uma seleção na expressão regular: `([\d.]+)`, utilizada para isolar uma versão. Este exemplo também define outros Elements, como o nome do produto `p/nginx/`, a versão recuperada `v/$1/` e o CPE com a versão `cpe:/a:igor_sysoev:nginx:$1/`.



Um CPE (Common Platform Enumeration) é um sistema de notação normalizado utilizado para identificar e descrever software e hardware. Este formato permite uma gestão mais eficaz das vulnerabilidades e das configurações de segurança e, sobretudo, uma forma unificada de as representar, seja qual for o produto em causa. Aqui estão dois exemplos de CPE: `cpe:/o:microsoft:windows_8.1:r1` e `cpe:/a:apache:http_server:2.4.35`



Aqui identificamos claramente os seus tipos `o` para SO, `a` para aplicação, fornecedor, produto e versões.



Então, no caso de um _match_ com uma dessas expressões regulares, nós iremos obter não apenas o nome do serviço, mas também sua versão e CPE exato, tornando mais fácil encontrar CVEs que afetam essa versão. Encontrará esta informação no output standard do Nmap, e verá que é muito útil para outros propósitos que iremos cobrir em algumas secções.



A sintaxe exata do _matches_ e, mais geralmente, das diretivas no arquivo `/usr/share/nmap/nmap-service-probes` não pára por aí, e pode parecer um pouco complexa se você não está acostumado a manipular o Nmap e seus resultados. No entanto, deve pelo menos ter em mente sua existência e operação geral, o que será útil mais tarde quando quiser entender ou depurar um resultado, customizar um scan ou até mesmo contribuir para o desenvolvimento do Nmap.



### III. Utilizar o Nmap para detetar versões



Agora nós vamos utilizar toda essa complexa mecânica de _Probe_ e _Match_ através de uma simples opção: `-sV`. Isso simplesmente diz ao Nmap: tente descobrir exatamente quais serviços e versões de portas você definiu como abertas.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Eis um exemplo completo do resultado de um tal comando:



![nmap-image](assets/fr/35.webp)



resultados da deteção de versões do Nmap de aplicações expostas na rede



Aqui podemos ver que o Nmap conseguiu identificar todas as versões dos serviços de rede expostos por este alvo, e exibe esta informação numa nova coluna `VERSÃO`. É possível ver informações bastante precisas, até mesmo sobre o sistema operacional, se essas informações fizerem parte da assinatura recuperada.



Para entender em detalhes o que acontece durante uma verificação de vulnerabilidade, podemos usar a opção `--version-trace`. Isso fornecerá uma visão em modo debug, exibindo a _Probe_ que levou à deteção:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Como resultado, teremos muita informação para classificar. Tente identificar as linhas que começam com `Service scan Hard match`. Verá então linhas como estas:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Podemos ver claramente quais _Probes_ foram utilizadas para detetar a tecnologia e a versão (neste caso, as _Probes_ `NULL` e `GetRequest`), bem como as informações recuperadas.



### IV. Testes de domínio e precisão da deteção



Vamos agora voltar a uma diretiva no ficheiro `/usr/share/nmap/nmap-service-probes` que não vimos anteriormente:



![nmap-image](assets/fr/36.webp)



diretiva `rarity` das sondas no ficheiro `/usr/share/nmap/nmap-service-probes`._



Esta diretiva é utilizada para indicar a raridade (i.e. prioridade/probabilidade) associada a uma _Probe_. Esta notação de 1 a 9 permite-lhe controlar a completude da análise efectuada pelo Nmap quando envia _Probes_. No sistema de "notação" do Nmap, uma raridade de 1 fornece informações na grande maioria dos casos, enquanto uma raridade de 8 ou 9 representa um caso muito especial, específico para uma configuração ou serviço que raramente está presente.



Para ser mais claro, num caso predefinido, o Nmap irá enviar para cada serviço a ser identificado as _Probes_ que têm uma raridade de 1 a 7. Para vos dar uma melhor ideia da distribuição das _Probes_ por _raridade_, eis a sua contagem:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Pode parecer contra-intuitivo, mas existem mais sondas de `raridade` 8 e 9 do que as demais. Isso acontece justamente porque as Probes de raridade 1 são genéricas e funcionam na maioria dos casos, independente do serviço (lembre-se da Probe `NULL` que simplesmente envia um pacote TCP vazio). Já as Probes mais complexas são praticamente únicas por serviço.



Se quisermos gerenciar manualmente as Sondas que desejamos usar em nossa varredura de versão, podemos usar a opção `--version-intensity`. Aqui estão dois exemplos:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Para terminar este assunto, eis um exemplo de _Probe_ 9 e 8:



![nmap-image](assets/fr/37.webp)



exemplos de Probe com raridade 8 e 9 no ficheiro `/usr/share/nmap/nmap-service-probes`._



Estas duas _Probes_ detectam servidores de Quake1 e Quake2 (o videojogo). Interessante para o lado nostálgico, mas improvável que tenha muita utilidade no dia a dia.



Dependendo das suas necessidades de precisão ou rapidez, lembre-se que este princípio de "raridade" existe e pode influenciar o resultado.



### V. Utilizar o Nmap para detetar sistemas operativos



Nós vamos agora ver como o Nmap pode nos ajudar a detetar os sistemas operacionais dos hosts escaneados e detectados em uma rede. Para fazer isso, use a opção `-O` (para `OS Scan`) do Nmap.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Eis um exemplo dos resultados. Aqui, o Nmap diz-nos que se trata provavelmente de um sistema operativo Linux e oferece-nos várias estatísticas relativas à sua versão exacta.



![nmap-image](assets/fr/38.webp)



deteção da probabilidade de identificação de um sistema operativo pelo Nmap



Para o conseguir, o Nmap irá utilizar uma multiplicidade de técnicas que funcionam de forma muito semelhante às _Probes_ e _Matches_ para a deteção de tecnologias e versões. A principal diferença é que o Nmap utilizará parâmetros de "baixo nível" de ICMP, TCP, UDP e outros protocolos. Aqui estão dois exemplos de teste para detetar um sistema operativo Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



exemplos de testes efectuados pelo Nmap para detetar um sistema operativo Windows 11



Vamos encarar isso, esses testes são muito difíceis de interpretar, e nós não vamos tentar entendê-los em profundidade no contexto de um tutorial introdutório do Nmap. Se você quiser se aprofundar no assunto, o arquivo que contém essas informações é o `/usr/share/nmap/nmap-os-db`.



No entanto, é preciso estar ciente de que a deteção do SO é mais uma probabilidade estabelecida pelo Nmap do que uma certeza.



### VI. Conclusão



Nesta secção, aprendemos como utilizar as opções do Nmap para detetar as tecnologias, versões e sistemas operativos dos hosts e serviços analisados. Agora temos um bom entendimento de como o Nmap obtém essas informações remotamente. Também revimos as opções para gerir a verbosidade e a precisão dos testes, bem como as limitações da ferramenta nestes assuntos.



Na próxima secção, vamos aprender como utilizar os scripts NSE do Nmap para realizar uma análise de segurança do nosso sistema de informação. Se precisar, reserve um tempo para reler as últimas seções e não hesite em praticar e mergulhar nas entranhas da ferramenta para dominar melhor o que aprendemos até agora.




## 7 - Análise de segurança: deteção de vulnerabilidades



### I. Apresentação



Nesta secção, vamos aprender a utilizar a ferramenta de scan de rede Nmap para detetar e analisar vulnerabilidades nos alvos dos nossos scans. Em particular, veremos as várias opções disponíveis para realizar esta tarefa e estudaremos os limites das capacidades da ferramenta para melhor compreender e interpretar os seus resultados.



Nesta primeira seção, nós vamos dar uma olhada no scanner de vulnerabilidades do Nmap, e ver como usar as opções básicas de deteção de vulnerabilidades. Nas secções seguintes, vamos ver mais detalhadamente como esta funcionalidade funciona e como pode ser personalizada.



### II. Utilizar o Nmap para detetar vulnerabilidades



Queremos agora utilizar o scanner de rede Nmap para detetar vulnerabilidades nos serviços e sistemas do nosso sistema de informação. Isto significa que, para além de descobrir anfitriões activos, enumerar serviços expostos e detetar versões e tecnologias, o Nmap irá procurar vulnerabilidades.



Para o conseguir, o Nmap baseia-se em scripts NSE (_Nmap Scripting Engine_), que podem ser vistos como módulos que permitem uma abordagem granular aos testes.



Com as opções corretas, pediremos ao Nmap para utilizar os seus vários scripts NSE em cada serviço descoberto, permitindo-nos descobrir:





- Falhas de configuração ;





- Descobertas adicionais e mais avançadas de versões e sistemas operativos ;





- Vulnerabilidades conhecidas (CVEs) ;





- Identificadores fracos ;





- Elements caraterístico de uma infeção por malware ;





- Possibilidades de negação de serviço ;





- Etc.




Como se pode ver, os scripts NSE alargam significativamente as capacidades do Nmap em termos das operações de rede que pode efetuar. E isso para executar tarefas muito mais avançadas do que nunca. A boa notícia é que, como de costume, esses recursos podem ser usados simplesmente através de uma opção e num contexto padrão. É o que veremos a seguir.



### III. Exemplo de uma análise de vulnerabilidades



Os scripts NSE podem ser usados quando se utiliza o Nmap para fazer scan a uma única porta num host, a todos os serviços nesse host ou a todos os serviços detectados em várias redes. Portanto, podemos usar as opções que veremos em todos os contextos que estudamos até agora.



Para habilitar o scan de vulnerabilidades através de um scan do Nmap, nós precisamos usar a opção `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Lembre-se de que, por padrão, se você não especificar nada, o Nmap só fará o scan das 1000 portas mais comuns. Ele não detectará vulnerabilidades nas portas mais exóticas que seus alvos possam expor.



Antes de utilizar esta funcionalidade num sistema de informação de produção, convido-o a continuar a ler o tutorial. Nas secções seguintes, veremos como controlar melhor o impacto e os tipos de testes que serão executados.



Ao reutilizarmos o que aprendemos anteriormente, podemos, por exemplo, ser mais abrangentes e analisar todas as portas TCP de um alvo:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Aqui está o resultado de uma varredura do Nmap usando scripts NSE:



![nmap-image](assets/fr/40.webp)



exemplo dos resultados de uma verificação de vulnerabilidades num anfitrião através do Nmap._



Aqui vemos a apresentação de informações adicionais de interesse no contexto de uma análise de vulnerabilidade:





- O serviço FTP pode ser acedido de forma anónima, e não está protegido por autenticação. O script NSE responsável por essa verificação nos diz isso, e até exibe parte da estrutura de árvore do serviço FTP. Aqui vemos que temos acesso ao diretório `C` do sistema Windows!





- O script NSE responsável pela recuperação avançada do serviço Web apresenta o título da página, dando-nos uma ideia melhor do que o serviço Web está a alojar.





- Temos também uma mini análise da configuração do serviço SMB (scripts `smb2-time`, `smb-security-mode` e `smb2-security-mode`). As informações são exibidas de forma um pouco diferente, após o resultado da varredura de rede, para facilitar a leitura. Em particular, essas informações indicam a ausência de assinaturas SMB Exchange. Essa fraqueza de configuração permite que o alvo seja usado em um ataque SMB Relay, uma notável falha de segurança frequentemente explorada em testes de intrusão/ataque cibernético.




É claro que este é apenas um exemplo. O Nmap tem scripts NSE para muitos serviços, visando uma grande variedade de vulnerabilidades. Iremos olhar mais de perto para estas possibilidades na próxima secção.



Para concluir esta introdução à análise de vulnerabilidades, eis um comando completo para a descoberta de redes, análise de portas TCP, deteção de versões e vulnerabilidades:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Aqui está um comando que está a começar a parecer-se com casos de utilização mais realistas do Nmap!



### IV. Compreender as limitações do Nmap no scanning de vulnerabilidades



Sejamos claros: o Nmap não é capaz de efetuar um teste de penetração completo do seu sistema de informação ou de simular uma operação da Equipa Vermelha. Ele tem várias limitações das quais você precisa estar ciente para não ter uma falsa sensação de segurança:





- Cobertura limitada**: embora os scripts NSE do Nmap sejam poderosos, a sua cobertura de teste pode ser limitada em comparação com outras ferramentas especializadas de descoberta de vulnerabilidades. Algumas vulnerabilidades podem não ser cobertas pelos scripts NSE disponíveis, tais como vulnerabilidades do Active Diretory, exposição de dados sensíveis ou casos mais avançados de aplicações Web vulneráveis.





- Complexidade da vulnerabilidade**: certos tipos de vulnerabilidade podem ser difíceis de detetar utilizando scripts NSE devido à sua complexidade. Por exemplo, as vulnerabilidades que requerem uma interação complexa com um serviço remoto podem não ser detectadas eficazmente pelo Nmap (como no caso de permissões excessivas numa partilha de ficheiros ou de uma falha no controlo de permissões numa aplicação Web).





- Deteção passiva**: O Nmap concentra-se principalmente em exames activos para detetar vulnerabilidades, o que significa que pode não detetar eficazmente potenciais vulnerabilidades sem estabelecer uma ligação ativa com os anfitriões alvo. As vulnerabilidades que não se manifestam durante uma análise ativa podem, portanto, não ser detectadas (como no caso de uma injeção de código numa aplicação Web).





- Dependência de actualizações**: A [base de dados] do Nmap (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) de scripts NSE está em constante evolução, mas pode haver um atraso entre a descoberta de uma nova vulnerabilidade e a adição de um script correspondente ao Nmap. Como resultado, o Nmap pode não estar sempre atualizado com as últimas vulnerabilidades.





- Falsos positivos e falsos negativos**: como em qualquer ferramenta de segurança, os scripts NSE do Nmap podem produzir falsos positivos (falsos alertas de vulnerabilidade) ou falsos negativos (vulnerabilidades reais não detectadas). Isto é algo a ter em conta quando se analisam os resultados do Nmap.




Então é importante entender o que o Nmap faz e não faz, e da mesma forma saber como interpretar seus resultados. Em particular, nós vimos ao longo deste tutorial que as opções padrão podem nos levar a perder importantes Elements que podem ser descobertos com um uso cuidadoso.



Quer seja um administrador de sistemas de rede, um engenheiro de segurança ou mesmo um CISO, a utilização do Nmap dá-lhe uma visão geral do estado de segurança de um sistema de informação. Este é um primeiro passo importante para proteger um sistema, que pode ser realizado regularmente pela equipa de TI. No entanto, não deve substituir a intervenção e o aconselhamento de peritos [em cibersegurança] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), que poderão descobrir pontos fracos de forma muito mais abrangente do que o Nmap.



### V. Conclusão



Nesta primeira secção do Módulo 3, introduzimos o scan de vulnerabilidades através do Nmap. Agora sabemos como usar a opção principal para executar essa tarefa, mas também sabemos os limites do exercício. Na próxima secção, vamos analisar mais de perto esta funcionalidade, utilizando scripts NSE para aumentar dez vezes o poder do Nmap.



## 8 - Usando os scripts NSE do Nmap



### I. Apresentação



Nesta secção, iremos analisar em profundidade os scripts NSE (_Nmap Scripting Engine_). Em particular, veremos porque é que são um dos grandes pontos fortes desta ferramenta, como funcionam e como navegar e utilizar os muitos scripts existentes.



Esta secção vem no seguimento do tutorial anterior, no qual aprendemos a utilizar as funcionalidades de scan de vulnerabilidades do Nmap de uma forma básica. Agora vamos ver mais de perto como o [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) funciona nesse aspeto, para que possamos mais uma vez realizar scans mais precisos e controlados.



### II. O conceito de scripts NSE do Nmap



Os scripts NSE do Nmap permitem-lhe alargar as suas capacidades de uma forma altamente flexível. Eles são escritos em LUA, uma linguagem de scripting que é mais fácil de manusear e acessar do que o C ou C# usado pelo Nmap. A vantagem de utilizar um script LUA com o Nmap em vez de uma ferramenta autónoma é que nos permite tirar partido da velocidade de execução do Nmap e das funcionalidades padrão (descoberta de anfitrião, porto e versão, etc.).



Estes scripts estão organizados por categoria e um único script pode pertencer a mais do que uma categoria:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Tecnicamente, as categorias a que um script pertence são indicadas diretamente no seu código.



![nmap-image](assets/fr/41.webp)



categorias de scripts nSE `ftp-anon`._



Este exemplo mostra parte do código do script NSE `ftp-anon.nse`, cuja execução vimos na secção anterior.



### III. Lista dos guiões NSE existentes



Por padrão, os scripts NSE do Nmap estão localizados no diretório `/usr/share/nmap/scripts/`, sem nenhuma estrutura de árvore ou hierarquia específica. Aqui está uma visão geral do conteúdo deste diretório:



![nmap-image](assets/fr/42.webp)



extrai o conteúdo do diretório `/usr/share/nmap/scripts/` que contém os scripts NSE._



Este diretório contém mais de 5.000 scripts NSE. Na maioria dos casos, a primeira parte do nome do script contém o protocolo ou a categoria a que pertence. Isto permite-nos ordenar a lista, por exemplo, se quisermos listar todos os scripts direcionados para o serviço FTP:



![nmap-image](assets/fr/43.webp)



lista de scripts do NSE Nmap com nomes que começam por `ftp-`._



O Nmap não oferece uma opção para navegar e listar seus scripts NSE; você pode usar o comando `--script-help` seguido pelo nome de uma categoria ou uma palavra:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



No entanto, a saída será o nome de cada script e a sua descrição, o que não é o ideal se a pesquisa trouxer várias dezenas de scripts:



![nmap-image](assets/fr/44.webp)



resultado da utilização do comando `--script-help` do Nmap



Na minha opinião, o método mais eficaz é utilizar os comandos clássicos do Linux no diretório `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Pode consultar o código dos módulos que lhe interessam, para compreender melhor o funcionamento de um script NSE.



### IV. Utilizar os scripts NSE do Nmap



Agora vamos aprender a efetuar análises de vulnerabilidades, selecionando cuidadosamente os scripts NSE que nos interessam.



#### A. Selecionar guiões por categoria



Para começar, nós podemos escolher executar todos os scripts pertencentes a uma categoria específica. Nós precisamos indicar essa categoria ou essas categorias para o Nmap com o argumento `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Este primeiro comando é o equivalente ao comando `nmap -sC`. Por padrão, o Nmap irá selecionar scripts na categoria `default`, mas isso é apenas para fins de argumentação. O próximo comando, por exemplo, irá utilizar todos os scripts da categoria `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Como vimos, algumas categorias nos permitem identificar rapidamente o que os scripts NSE relacionados fazem (`discovery`, `vuln`, `exploit`), enquanto outras definem o nível de risco, deteção ou estabilidade do teste realizado. Se estivermos num contexto sensível e não tivermos uma boa noção das diferentes acções executadas pela nossa seleção de scripts, podemos optar por combinar as selecções para escolher apenas os scripts que estão nas categorias `discovery` e `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Se quiser excluir absoluta e explicitamente os scripts das categorias `dos` e `intrusive`, pode utilizar a seguinte notação:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Tenha em atenção que a especificação das condições de exclusão acima referidas resultará na utilização de todas as outras categorias que não estejam explicitamente excluídas. Para sermos mais justos, poderíamos especificar, por exemplo:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Aqui estão alguns exemplos de como lidar com scripts NSE por categoria, especialmente quando se usa o Nmap para análise de vulnerabilidades em contextos reais.



#### B. Selecionar os guiões como uma unidade



Também podemos optar por realizar um único teste específico durante uma análise, um teste correspondente a um script NSE. Para isso, é necessário especificar o nome do script no parâmetro `-script <nome>`. Tomando como exemplo o script `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Obtemos então um resultado muito preciso:



![nmap-image](assets/fr/45.webp)



resultado da utilização do script `ftp-anon` do NSE numa porta FTP através do Nmap._



Vemos o resultado da execução do script `ftp-anon` na porta 21, e em nenhuma outra porta, pois especificamos a opção `-p 21`. Poderíamos também ter realizado uma varredura básica de portas, executando o script `ftp-anon` NSE apenas nos serviços FTP descobertos:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Assim, o Nmap também teria executado este teste de ligação anónima se tivesse encontrado um serviço FTP noutro porto.



Para uma breve descrição do que um script NSE faz, pode usar a opção `--script-help` mencionada acima:



![nmap-image](assets/fr/46.webp)



ajuda para mostrar o resultado do script NSE `sshv1`._



Em suma, podemos voltar a reutilizar todas as opções, serviços, versões e tecnologias de descoberta de rede que utilizámos até agora!



#### C. Gerir argumentos de script



No decorrer do uso do Nmap, você irá se deparar com certos scripts NSE que requerem argumentos de entrada para funcionar corretamente. Nós veremos agora como passar argumentos para esses scripts através das opções do Nmap.



Como exemplo, vamos pegar o script `ssh-brute`, que permite realizar um ataque de força bruta no serviço SSH.



Um ataque de força bruta clássico consiste em testar várias palavras-passe (por vezes milhões) numa tentativa de autenticação numa conta específica. Ao tentar tantas palavras-passe, o atacante aposta na probabilidade de o utilizador ter utilizado uma palavra-passe fraca no dicionário de palavras-passe utilizado para o ataque.



Este script tem opções "padrão", que podemos personalizar para se adequar ao nosso contexto. No contexto desse ataque, por exemplo, podemos fornecer ao Nmap a lista de usuários e o dicionário de senhas a ser usado. Até onde eu sei, não é possível listar facilmente os argumentos necessários para um script, então a maneira mais confiável é visitar o site oficial do Nmap. Um link direto para a documentação de um script NSE pode ser obtido em resposta à opção `--script-help`:



![nmap-image](assets/fr/47.webp)



resultado da apresentação da ajuda para o script NSE `ssh-brute` com um link para nmap.org._



Ao clicar na hiperligação indicada, chegamos a esta página web do sítio [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



lista de argumentos que podem ser passados para o script `ssh-brute` NSE do Nmap



Aqui temos uma visão clara dos argumentos que podem ser utilizados, sendo os principais no nosso contexto `passdb` (ficheiro que contém uma lista de palavras-passe) e `userdb` (ficheiro que contém uma lista de utilizadores). A documentação aqui se refere a bibliotecas internas do Nmap, já que esses mecanismos de força bruta e opções associadas são mutualizados para serem usados uniformemente em vários scripts (`ssh-brute`, `mysql-brute`, `mssql-brute`, etc.) e portanto terão mais ou menos os mesmos argumentos:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Como pode ser visto neste último comando, nós podemos especificar os argumentos necessários para um script do Nmap usando a opção `--scripts-args key=value,key=value`. Aqui está um possível resultado da saída do Nmap ao executar uma força bruta SSH através do script `ssh-brute` do NSE:



![nmap-image](assets/fr/49.webp)



resultado da execução de força bruta SSH através do Nmap._



Como pode ver, a informação gerada pelos scripts NSE é prefixada com `NSE: [nome do script]` na saída interactiva (saída do terminal), tornando-a mais fácil de encontrar. Dentro da exibição usual dos resultados do Nmap, nós simplesmente temos um resumo indicando se identificadores fracos foram ou não descobertos (incluindo senhas, lembre-se).



Para dar mais um passo em frente, e para lembrar que tudo isto pode ser utilizado para além de todas as opções que já vimos, aqui está um comando que irá descobrir a rede `10.10.10.0/24`, analisar as 2000 portas TCP mais frequentes e executar uma pesquisa de acesso anónimo em serviços FTP e uma campanha de força bruta em serviços SSH:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Este é apenas um exemplo dos muitos scripts disponíveis e suas opções. Mas agora nós temos uma idéia melhor de como lidar com os scripts do NSE, se eles requerem argumentos e como passar esses argumentos para o Nmap.



### V. Conclusão



Nesta secção, aprendemos como utilizar os scripts NSE do Nmap para executar várias tarefas. Convido-o a dedicar algum tempo para descobrir as diferentes categorias de scripts e os próprios scripts, para ver quantos testes eles podem automatizar.



Durante várias secções, temos vindo a acumular opções mais ou menos avançadas de descoberta, scan e enumeração. Por esta altura, deve estar ciente de que o output do Nmap e a apresentação de resultados estão a começar a tornar-se bastante extensos, por vezes até demasiado verbosos para o nosso terminal. Na próxima secção, vamos aprender como controlar este output, em particular armazenando-o em ficheiros de vários formatos.






## 9 - Gerir os dados de saída do Nmap




### I. Apresentação



Nesta secção, vamos dar uma vista de olhos ao output produzido pelo Nmap e, em particular, às várias opções de formatação deste output. Veremos que o Nmap pode produzir vários formatos de saída para atender a diferentes necessidades, e que este também é um dos grandes pontos fortes desta ferramenta.



Por defeito, o Nmap oferece uma vista detalhada dos resultados dos exames e testes que efectua. Isso inclui hosts e serviços examinados, aqueles detectados como acessíveis, as especificidades das portas abertas, seu status e versão. Além disso, os detalhes dos scripts NSE também estão disponíveis na saída do terminal. No entanto, esta saída pode rapidamente tornar-se volumosa, mesmo com uma formatação clara das informações, o que pode dificultar a localização de informações precisas nos resultados.



### II. Dominar os formatos de saída do Nmap



#### A. Guardar os resultados da digitalização num ficheiro de texto



Para facilitar as coisas, o [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) torna muito fácil salvar sua saída em um arquivo de texto. Isso pode ser útil para arquivamento, comparação com outros testes, mas também para navegar nessa saída com ferramentas especializadas de processamento de texto ou linguagens de script, como Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, etc. Para armazenar a saída padrão do Nmap em um arquivo de texto, nós podemos utilizar a opção `-oN <filename>` (o "N" em "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Não é surpresa, pois o Nmap mostrará a sua saída padrão habitual no nosso terminal, mas também no ficheiro especificado.



#### B. Saída do generate Nmap em formato condensado



Existe também um segundo formato de saída no estilo "texto" que pode ser facilmente interpretado por um ser humano: o formato "greppable".



Esse formato foi criado para fornecer uma visão "condensada" da saída do Nmap, estruturada de forma a facilitar seu processamento por ferramentas como o `grep`. Vamos ver um exemplo desse tipo de saída:



![nmap-image](assets/fr/50.webp)



scan de rede nmap e saída em formato "greppable"._



Aqui, efectuei uma descoberta de rede, bem como um scan de portas e uma análise de tecnologias e versões numa rede /24 e, em seguida, armazenei os resultados num ficheiro em formato "greppable". Acabei com um ficheiro que contém 2 linhas por cada anfitrião ativo:





- A primeira linha diz-me que tal e tal anfitrião está _Up_;





- Uma segunda linha diz-me quais as portas que foram analisadas, o seu estado e a informação sobre a tecnologia e a versão recuperada num formato muito específico: `<porta>/<status/<protocolo>//<serviço>//<versão>/,`




Esta formatação com um delimitador fixo permite um processamento rápido por ferramentas de processamento de texto como o `grep`, ou linguagens de script e de programação. O seguinte comando, por exemplo, permite-me obter facilmente informação sobre o hospedeiro `10.10.10.5` no caso de um scan enorme efectuado pelo Nmap cujo output seria difícil de navegar:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Por outro lado, também posso listar facilmente todos os hosts que têm a porta 21 aberta, pois as portas e o IP estão na mesma linha:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Para generate essa saída, precisamos usar a opção `-oG <filename>.gnmap` (o "G" em "grep"). Por hábito, eu uso a extensão `.gnmap` aqui para esse arquivo, mas sinta-se livre para usar o que quiser:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Este formato pode ser utilizado para uma variedade de objectivos e é particularmente útil para a criação rápida de scripts/classificação. No entanto, tende a ser abandonado em favor do formato que veremos a seguir.



nota: o formato greppable `-oG` foi oficialmente descontinuado desde o Nmap 7.90. Ele ainda pode ser utilizado para fins de compatibilidade. Ele ainda pode ser utilizado para fins de compatibilidade, mas é recomendado que você utilize o formato XML ou normal para qualquer desenvolvimento ou análise automatizada._



#### C. Formato XML para os resultados do Nmap



O último formato que vale a pena mencionar neste tutorial é o XML. Ao contrário dos dois formatos anteriores, este não foi concebido para ser lido por humanos, mas sim por outras ferramentas ou scripts.



XML (_eXtensible Markup Language_) é uma linguagem de marcação utilizada para armazenar e transportar dados, oferecendo uma estrutura hierárquica através de etiquetas personalizadas.



No Nmap, o formato XML é utilizado para relatórios detalhados do generate sobre os exames efectuados, incluindo informações sobre anfitriões, portas e vulnerabilidades detectadas, bem como informações adicionais não apresentadas na saída padrão do Nmap.



Para generate um ficheiro de saída em formato XML, é necessário utilizar a opção `-oX` ("O" de "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



O resultado é a saída padrão do Nmap no seu terminal, bem como um ficheiro em formato XML no seu diretório atual.



Naturalmente, o formato XML não foi concebido para ser lido e interpretado por humanos. No entanto, se quiser fazer scripts ou análises automatizadas neste formato de saída do Nmap, precisa de ter uma ideia das etiquetas e da estrutura utilizadas. Por exemplo, aqui está parte do conteúdo do ficheiro XML criado pelo Nmap, que mostra os resultados do scan para 1 anfitrião:



![nmap-image](assets/fr/51.webp)



exemplo de um registo XML para 1 anfitrião durante uma exploração do Nmap



Há muita informação aqui, e estamos particularmente interessados nas duas portas abertas:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Entendemos que este formato facilitará a análise automática dos resultados, uma vez que cada informação está organizada numa etiqueta ou atributo dedicado e nomeado. Em particular, encontramos uma informação que não tínhamos encontrado antes: o CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Mencionámos brevemente o CPE na secção 2 do módulo 2, e esta informação é determinada em correspondências durante a deteção da versão. O Nmap utiliza os seus mecanismos de deteção de serviço, tecnologia e versão para encontrar o CPE associado.



Isto permite-nos reutilizar esta informação com as bases de dados e as aplicações que a utilizam. Estou a pensar, em particular, na base de dados NVD, que faz referência aos CVE. Para cada CVE, contém os CPEs afectados pela vulnerabilidade. Eis um exemplo de um CVE relativo a `a:microsoft:internet_information_services:7.5` da base de dados NVD:



![nmap-image](assets/fr/52.webp)



presença de um CPE nos pormenores de um CVE na base de dados NVD



Compreendemos agora melhor as vantagens deste formato, que oferece uma estrutura de informação muito clara e contém todos os dados recolhidos ou processados pelo Nmap.



Como um reflexo, eu sistematicamente salvo meus scans do Nmap em todos os três formatos de uma vez. Isso é possível graças à opção `-oA <nome>` ("A" de "All"), que irá criar um arquivo `<nome>.nmap`, um arquivo `<nome>.xml` e um arquivo `<nome>.gnmap`. Dessa forma eu tenho certeza que não vou ficar sem nada quando precisar rever os resultados.



Com estes três formatos, deve ter tudo o que precisa para guardar e eventualmente processar os resultados do Nmap de uma forma automatizada. Iremos utilizar o formato XML novamente na próxima secção, quando analisarmos a utilização do Nmap com outras ferramentas de segurança.



#### III. Gerando um relatório HTML a partir de um scan do Nmap



O formato XML oferece muitas possibilidades, nomeadamente a de servir de base para gerar um relatório em formato HTML, que será visualmente mais agradável de consultar.



Para transformar um ficheiro Nmap em formato XML numa página web, vamos utilizar a ferramenta `xsltproc`, que teremos de instalar primeiro:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Uma vez instalada esta ferramenta, basta fornecer-lhe o ficheiro XML a converter e o nome do relatório HTML a gerar:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Como resultado, teremos toda a nossa digitalização bem estruturada, até com algumas cores e ligações clicáveis no índice!



![nmap-image](assets/fr/53.webp)



extrato de um relatório de scan do Nmap em formato HTML gerado por xsltproc._



Em termos gerais, o ficheiro XML guardado pelo Nmap contém uma referência a outro ficheiro em formato XSL:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



A conversão para HTML é, portanto, uma função fornecida e facilitada pelo Nmap, sendo o `xsltproc` uma ferramenta comum e reconhecida para realizar esta tarefa (que não vem do conjunto de ferramentas do Nmap).



XSLT (_Extensible Stylesheet Language Transformations_) é um subconjunto de XSL que permite que os dados XML sejam apresentados numa página Web e "transformados", em paralelo com os estilos XSL, em informações legíveis e formatadas em formato HTML.



fonte: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



O nível de informação no relatório é equivalente ao do formato XML do Nmap e superior ao da saída normal do terminal (_saída interactiva_).



### IV. Gerir o nível de verbosidade do Nmap



Vamos agora dar uma olhada em algumas opções para o Debugger Nmap ou para acompanhar seu progresso.



A primeira opção que devemos mencionar é a opção `-v`, que aumenta a verbosidade do Nmap. Aqui está um exemplo:



![nmap-image](assets/fr/54.webp)



saída detalhada do nmap usando a opção `-v`._



Em uma varredura visando muitos hosts e portas, a saída do terminal se tornará difícil de explorar devido à quantidade de informação exibida. Por esta razão, esta opção deve ser usada em combinação com as opções vistas anteriormente, que permitem armazenar a saída padrão do Nmap num arquivo. Informações relacionadas ao uso de verbosidade não serão incluídas neste arquivo de saída. Como pode ver no exemplo acima, esta verbosidade permite-lhe seguir as acções e descobertas do Nmap de forma clara e direta. Para scans mais longos, onde a exibição de dados pode ser lenta, isso evita ficar cego para a atividade atual do Nmap e saber que as coisas estão progredindo e em que ritmo. Para aumentar o nível de verbosidade, pode-se utilizar a opção `-vvv`.



Para acompanhar melhor a atividade do Nmap durante o scan, você pode usar a opção `--packet-trace`. Com a opção `-v`, nós obtemos um log ao vivo de todas as portas abertas descobertas pelo Nmap, enquanto que com esta opção, nós obtemos uma linha de log para cada pacote enviado para uma porta. Isso naturalmente produz uma saída muito verbosa, mas permite um monitoramento detalhado da atividade do Nmap, aqui está um exemplo:



![nmap-image](assets/fr/55.webp)



monitorização detalhada da atividade do Nmap através do `--packet-trace`._



Novamente, esta informação não será gravada no arquivo de saída produzido pelo Nmap se as opções `-oN`, `-oG`, `-oX` ou `-oA` forem utilizadas.



Finalmente, o Nmap também oferece duas opções de depuração: `-d` e `-dd`. Essas opções se comportam de forma similar à opção de verbosidade `-v`, mas adicionam informações técnicas adicionais, como um resumo dos parâmetros técnicos no início do scan:



![nmap-image](assets/fr/56.webp)



as opções de temporização são apresentadas na vista de depuração do Nmap



Nas próximas secções, veremos quais são as opções de "Timing" e porque vale a pena conhecê-las.



Finalmente, se você quer apenas ter uma visão geral básica e sintética do progresso do scan do Nmap, você pode usar a opção `--stats-every 5s`. O "5s" aqui significa 5 segundos e pode ser modificado para se adequar às suas necessidades. Esta é a frequência com que nós receberemos feedback do Nmap sobre o seu progresso:



![nmap-image](assets/fr/57.webp)



informações exibidas pela opção `--stats-every` do Nmap



Em particular, podemos obter uma percentagem de progresso, bem como uma indicação da fase em que se encontra: fase de descoberta do hospedeiro via [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), fase de descoberta de portas TCP expostas, etc. Esta informação também pode ser obtida na saída do terminal, premindo "Enter" durante uma verificação.



No entanto, o Nmap não é muito bom em estimar quanto tempo uma tarefa levará, até porque ele não sabe de antemão quantos hosts e serviços ele terá que escanear.



### V. Conclusão



Nesta secção, nós vimos um número de opções para guardar os resultados de scan do Nmap em diferentes formatos de ficheiros. Isso será muito útil, já que em contextos realistas, os resultados de scan podem ocupar centenas ou até milhares de linhas! Também vimos como aumentar o nível de verbosidade do Nmap para fins de depuração ou para obter um relatório de progresso do scan.



O formato XML será particularmente útil na próxima secção, onde veremos algumas ferramentas que podem trabalhar com os resultados do Nmap.




## 10 - Utilizar o Nmap com outras ferramentas de segurança



### I. Apresentação



Nesta secção, vamos dar uma vista de olhos a algumas das utilizações clássicas do Nmap com outras ferramentas de segurança gratuitas e de código aberto. Em particular, nós vamos usar o que aprendemos nas secções anteriores para melhorar ainda mais o poder e a eficiência do Nmap.



A capacidade de guardar os resultados das análises do Nmap em XML torna os dados compatíveis com uma série de outras ferramentas. Uma vez que quase todas as linguagens de programação e de scripting têm atualmente bibliotecas capazes de analisar XML, é muito mais fácil processar estes dados. Várias ferramentas, particularmente aquelas voltadas para a segurança ofensiva, têm funções para processar o formato XML gerado pelo Nmap. Vamos dar uma olhada mais de perto.



Vou mencionar algumas ferramentas ofensivas sem explicar em pormenor como são utilizadas ou como funcionam. Vou partir do princípio de que o leitor está familiarizado com a sua utilização básica e que já estão operacionais. Esta secção será de particular interesse para profissionais [de cibersegurança] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), pessoas em formação ou que tenham decidido aprofundar o assunto.



### II. Importar resultados do Nmap para o Metasploit



A primeira ferramenta que vamos analisar para reutilizar os dados do Nmap em segurança ofensiva e pesquisa de vulnerabilidades é o Metasploit.



O Metasploit é uma estrutura de exploração e ataque. É uma solução gratuita e uma ferramenta reconhecida que contém um grande número de módulos escritos em Ruby ou Python. Estes permitem explorar vulnerabilidades, realizar ataques, gerar backdoors, gerir callbacks (funções C&C ou de comunicação e controlo) e utilizar tudo de forma uniforme.



Em particular, esta estrutura operacional bem conhecida e amplamente utilizada pode trabalhar com uma [base de dados] postgreSQL (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) na qual são armazenados hosts, portas, serviços, informações de autenticação e muito mais.





- Documentação oficial do Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)




É aqui que o Nmap e os seus resultados entram em ação, uma vez que o formato XML dos resultados do Nmap pode ser facilmente importado para a base de dados do Metasploit para preencher a sua base de dados de anfitriões e serviços, que podem então ser rapidamente designados como alvos para este ou aquele ataque.



Uma vez na minha shell interactiva do Metasploit, começo por criar um espaço de trabalho, uma espécie de espaço específico para o meu ambiente do dia:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Uma vez criado o meu espaço de trabalho, temos de validar se a comunicação com a base de dados está operacional:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Finalmente, podemos usar o comando `db_import` do Metasploit para importar nosso scan do Nmap no formato XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Aqui está o resultado da execução de todos estes comandos:



![nmap-image](assets/fr/58.webp)



importar uma análise do Nmap em formato XML para a base de dados do Metasploit



Aqui você pode ver que cada host é importado, junto com seus serviços. Esses dados podem então ser exibidos através do comando `services` ou `services -p <port>` para um serviço específico:



![nmap-image](assets/fr/59.webp)



lista de serviços importados do ficheiro XML para a base de dados do Metasploit



Finalmente, podemos rápida e facilmente reutilizar esses dados em um módulo graças à opção `-R`, que irá "converter" a lista de serviços obtidos como entrada para a diretiva `RHOSTS`, que é usada para especificar os alvos do ataque a ser realizado. Eis um exemplo com o módulo `ssh_login`, que permite efetuar um ataque de força bruta aos serviços [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



utilizar a opção `services -R` para importar os serviços especificados como alvo do ataque



Este é apenas um pequeno exemplo do que pode ser feito com os dados do Nmap no Metasploit, mas dá-lhe uma pequena ideia da rapidez e facilidade com que esta informação pode ser reutilizada como parte de um teste de penetração, scan de vulnerabilidades ou ciberataque. Também vale a pena mencionar que o Nmap pode ser executado diretamente do Metasploit para importar os resultados para o banco de dados (comando `db_nmap`), outro tópico interessante a ser abordado!



### III. Utilizar o Nmap com o scanner Web da Aquatone



A segunda ferramenta que gostaria de apresentar nesta secção sobre a reutilização dos resultados do Nmap para segurança ofensiva e análise de vulnerabilidades é o Aquatone.



O Aquatone é um scanner Web concebido para explorar eficazmente as aplicações Web numa rede. Oferece funcionalidades avançadas para a descoberta de serviços Web, identificação de subdomínios, análise de portas e impressão digital de aplicações Web. Tudo apresentado de forma clara e concisa em relatórios HTML, JSON e de texto para facilitar a análise de segurança da Web.



Tal como acontece com o Metasploit, o Aquatone pode processar diretamente o formato XML do Nmap e utilizá-lo como alvo para análise. Em particular, pode extrair apenas os anfitriões e serviços de interesse (serviços Web) de todos os dados que um relatório do Nmap possa conter.





- Ligação da ferramenta: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Para usar a saída XML do Nmap com o Aquatone, simplesmente envie o arquivo XML em um pipe que será consumido pelo Aquatone. Aqui está um exemplo:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Enquanto a Aquatone normalmente efectua a descoberta de portas nos anfitriões para encontrar serviços Web, neste contexto basear-se-á apenas nos resultados do Nmap, que já efectuou esta operação, poupando assim tempo:



![nmap-image](assets/fr/61.webp)



utilizar os resultados do Nmap em formato XML com `aquatone`._



Para vossa informação, eis um extrato do relatório elaborado pela Aquatone:



![nmap-image](assets/fr/62.webp)



exemplo de um relatório `aquatone



Pessoalmente, utilizo frequentemente o Aquatone para ter uma visão rápida dos tipos de sítios Web presentes na rede, graças, nomeadamente, à sua funcionalidade de captura de ecrã.



Mais uma vez, ter um relatório completo do Nmap em formato XML poupa tempo e facilita a sua reutilização noutra ferramenta.



### IV. Conclusão



Estes dois exemplos mostram claramente que o formato XML do Nmap facilita a utilização dos seus resultados por outras ferramentas, uma vez que se trata de um formato de dados estruturado e fácil de utilizar. Existem muitas outras ferramentas capazes de processar estes resultados, tais como ferramentas de relatórios automatizados, representações gráficas ou scanners de vulnerabilidades mais complexos e proprietários.



É claro que também pode desenvolver os seus próprios scripts e ferramentas em Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) ou qualquer outra linguagem com uma biblioteca de análise XML para manipular e reutilizar os dados de resultados do Nmap da forma que achar melhor.



Esta secção leva-nos ao fim do módulo tutorial sobre a utilização mais avançada do Nmap, em particular para o scan de vulnerabilidades através de scripts NSE.



A próxima seção do tutorial irá focar, entre outras coisas, em algumas práticas recomendadas adicionais e mais técnicas e dicas sobre os scans específicos que o Nmap pode realizar. Também vamos dar uma olhada nas opções de otimização de desempenho de scan, que são particularmente úteis quando se faz o scan de grandes redes.




## 11 - Melhorar o desempenho da análise de rede



### I. Apresentação



Neste capítulo, aprenderemos como otimizar a velocidade dos scans de rede realizados com o Nmap usando várias opções específicas. Em particular, aprenderemos mais sobre o funcionamento interno do Nmap, desde o gerenciamento do _timeout_ até as configurações pré-salvas da ferramenta.



Agora que já demos uma boa olhada nos recursos do Nmap, vamos nos familiarizar com a fera e seu poder. Se você já usou a ferramenta em grandes redes, você provavelmente notou que alguns scans podem levar muito tempo, apesar do poder da ferramenta. E por uma boa razão: um simples comando `nmap` com algumas opções pode generate milhões de pacotes visando centenas de milhares de sistemas e serviços potenciais.



Além disso, algumas configurações de equipamentos de rede podem impor intencionalmente uma taxa mais lenta (número de pacotes por segundo), correndo o risco de rejeitar os seus pacotes ou proibir o seu IP Address por razões de segurança.



Dependendo do contexto, pode valer a pena tentar otimizar tudo isto, como veremos neste capítulo.



Em qualquer caso, pode verificar os valores por defeito dos parâmetros que vamos analisar, bem como se as opções que vai utilizar foram corretamente tidas em conta, através do debug do Nmap (opção `-d` vista num capítulo anterior):



![nmap-image](assets/fr/63.webp)



visualizar as opções de tempo através da opção `-d` do Nmap._



### II. Gerir a velocidade dos exames do Nmap



#### A. Gerir a paralelização



Por padrão, o Nmap usa a paralelização em seus scans para otimizá-los, e todos os parâmetros que ele usa podem ser modificados através de várias opções. No entanto, os casos em que é realmente necessário modificar esses parâmetros são bastante raros, então nós não vamos entrar em detalhes sobre eles neste tutorial:





- `--min-hostgroup/max-hostgroup <size>`: tamanho dos grupos de varredura de hosts paralelos.





- `--min-paralelismo/max-paralelismo <numprobes>`: paralelização de Probes.





- `--scan-delay/--max-scan-delay <time>`: ajusta o atraso entre as sondas.




Basta saber que existem e que podem ser utilizados.



#### B. Gerir o número de pacotes por segundo



Por padrão, o próprio Nmap ajusta o número de pacotes por segundo que envia de acordo com a resposta da rede. Mas é possível forçar essa configuração definindo o valor máximo e/ou mínimo a ser seguido em termos de número de pacotes por segundo. Essa configuração é feita utilizando as opções `--min-rate <número>` e `--max-rate <número>` onde `número` representa um número de pacotes por segundo. Exemplo:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Estas opções permitem-lhe ajustar a velocidade dos scans de acordo com as suas necessidades específicas, quer para acelerar o processo, quer para limitar a largura de banda utilizada. O último caso (limitar a velocidade dos scans) é o que mais provavelmente o levará a estas opções, especialmente se tiver experiência com latência de rede quando utiliza o Nmap (o que é bastante raro).



### III. Gerir as falhas de ligação e os tempos limite



Outro parâmetro que podemos utilizar para otimizar a velocidade dos scans do Nmap (ou garantir uma maior precisão) é o _timeout_ e o _retry_.



Para _timeouts_, este é o **tempo limite sem resposta** após o qual o Nmap deixará de esperar por uma resposta e considerará o serviço ou anfitrião inacessível. Para _retry_, este é o **número de tentativas sucessivas de uma operação** que o Nmap irá realizar antes de seguir em frente.



Tal como acontece com a paralelização, a gestão de _timeout_ e _retry_ pode ser aplicada às fases de descoberta do anfitrião ou do serviço:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: especifica o tempo de ida e volta de um Exchange. Novamente, este parâmetro é calculado e adaptado durante a varredura. É improvável que você precise usá-lo, já que o Nmap calcula esse tempo rapidamente de acordo com a reação da rede.





- `--max-retries <número>`: limita o número de retransmissões de um pacote durante o scan de portas. Por padrão, o Nmap pode ir até 10 tentativas para um único serviço, especialmente se ele encontrar latências ou perdas a nível de rede, mas na maioria dos casos apenas uma é realizada.





- `--host-timeout <time>`: especifica o tempo máximo que o Nmap passará em um host para todas as suas operações, incluindo scan de portas, deteção de serviços e quaisquer outras operações relacionadas a esse host. Se este intervalo de tempo for excedido sem qualquer resposta ou **conclusão de operações**, o Nmap abandonará este hospedeiro sem mostrar quaisquer resultados relativos a ele, e passará para o próximo na sua lista. Isto permite-lhe controlar o tempo máximo que o Nmap passa num determinado anfitrião, evitando ficar preso em anfitriões recalcitrantes e optimizando o tempo total de scan.




No meu trabalho diário, utilizo as opções `--max-retries` e `--host-timeout` para otimizar os meus scans:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Estes parâmetros oferecem flexibilidade adicional para ajustar o comportamento da verificação a necessidades específicas e condições de rede. No entanto, é necessário estar ciente das suas implicações em termos de carga nos anfitriões analisados e potencial perda de precisão.



### IV. Utilização de configurações preparadas



As várias opções que vimos neste capítulo podem ser utilizadas individualmente ou como parte das configurações prontas oferecidas pelo Nmap. A opção que habilita esses _templates_ (modelos de configuração) a serem utilizados é `-T <número>` ou `-T <nome>`. Existem 5 níveis de _templates_ utilizáveis:



```
-T<0-5>: Set timing template (higher is faster)
```



Por defeito, o Nmap utiliza o _template_ 3 (_normal_), que é geralmente suficiente.



Pela minha parte, geralmente opero em contextos em que preciso de ser bastante rápido (mantendo-me o mais completo possível) e utilizo frequentemente a opção `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Eis o que nos mostra a informação de depuração para esta análise:



![nmap-image](assets/fr/64.webp)



utilização da configuração `-T4` durante um scan do Nmap



### V. Conclusão



Neste capítulo, nós vimos várias técnicas e opções que podem ser usadas para gerenciar o poder, a agressividade e o desempenho do Nmap. Essas opções são particularmente úteis quando se faz o scan de grandes redes, e mais raramente para fins furtivos.



No próximo capítulo, vamos dar uma olhada em algumas práticas recomendadas para usar o Nmap e garantir sua segurança.




## 12 - Segurança e confidencialidade dos dados na utilização do Nmap



### I. Apresentação



Neste capítulo, vamos analisar uma série de boas práticas a serem adoptadas no que diz respeito à segurança e, acima de tudo, à confidencialidade dos dados produzidos, processados e armazenados pelo Nmap.



A utilização do Nmap num sistema de informação pode ser rapidamente classificada como uma ação ofensiva. Consequentemente, é necessário tomar uma série de precauções para atuar dentro de um quadro legal, garantindo simultaneamente a segurança dos alvos pretendidos, dos dados recolhidos e do sistema utilizado para o scan.



### II. Obtenção das autorizações adequadas



Antes de analisar uma rede ou sistema, certifique-se de ter obtido as autorizações apropriadas. A pesquisa de vulnerabilidades nos sistemas (scripts `NSE`) sem autorização pode ser ilegal e ter consequências legais, especialmente se a segurança dos sistemas de informação não fizer parte das suas competências oficiais.





- Para recordar: [Código Penal: Capítulo III: Ataques a sistemas automatizados de processamento de dados] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Proteção de dados sensíveis



Os resultados produzidos pelo Nmap podem ser considerados sensíveis, particularmente quando contêm informações sobre fraquezas no sistema de informação que poderiam ser exploradas por um atacante. Mas também quando dizem respeito a sistemas que não são acessíveis a toda a gente (por exemplo, sistemas de informação sensíveis, industriais, de cuidados de saúde ou [de salvaguarda] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Também vimos que, dependendo dos scripts NSE utilizados, os resultados de scan NSE do [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) também podem conter identificadores.



Assim, um indivíduo mal-intencionado que consiga aceder a estes resultados de scan terá em mãos um mapa do sistema de informação e um manancial de informações técnicas, sem que ele próprio tenha realizado estas acções, correndo o risco de ser detectado.



Por conseguinte, é importante ter cuidado para não recolher ou armazenar indevidamente informações sensíveis ao utilizar o Nmap, incluindo, entre outras, as seguintes:





- Criptografar os dados de saída: se você precisar armazenar ou transmitir os resultados dos seus scans do Nmap, certifique-se de criptografá-los para proteger a confidencialidade dos dados. Isto irá prevenir a interceção não autorizada de informação sensível. Idealmente, os dados devem ser encriptados assim que saem do sistema utilizado para efetuar o scan (um arquivo ZIP encriptado com uma palavra-passe forte é um bom começo).





- Estabeleça controlos de acesso: certifique-se de que apenas pessoas autorizadas têm acesso aos resultados dos seus scans do Nmap, onde estes serão armazenados. Configure controlos de acesso apropriados para proteger informação sensível de acessos não autorizados.





- Vigilância no manuseamento dos dados: quando transitar, copiar ou processar dados de digitalização, certifique-se de que mantém a segurança dos dados sob controlo rigoroso. Isto significa: não os deixe no diretório `Download` de uma estação de trabalho ligada à Internet, não os deixe transitar pela sua aplicação interna de ficheiros HTTP Exchange, não deixe o seu Bloco de Notas aberto sem bloquear a estação de trabalho durante a sua pausa para almoço, etc.




### IV. Gerir exames agressivos



Como vimos ao longo deste tutorial, o Nmap pode ser muito verboso a nível de rede. Também pode enviar pacotes que não estão corretamente formatados, e que não respeitam rigorosamente a estrutura do protocolo nos frames e pacotes de rede que gera. Todas estas acções podem ter um impacto em certos sistemas e serviços, por vezes ao ponto de causar mau funcionamento ou saturação dos recursos do sistema e da rede.



Para evitar incidentes, é preciso dominar o comportamento do Nmap e saber como adaptá-lo ao contexto em que ele é utilizado, por meio das várias opções discutidas neste tutorial. Não utilizaremos necessariamente o Nmap da mesma forma num sistema de informação que contenha [hardware] industrial (https://www.it-connect.fr/actualites/actu-materiel/) do que numa rede de utilizadores constituída por sistemas Windows protegidos por uma firewall local ou num núcleo de rede.



Esperamos que as várias lições deste tutorial tenham lhe ensinado como dominar e analisar o comportamento do Nmap, mas a melhor maneira de aprender é fazendo. Então, certifique-se de estar familiarizado com as opções do Nmap que você vai usar.



### V. Proteção do sistema de digitalização



No primeiro capítulo, nós vimos que, na maioria dos casos, o Nmap precisa ser executado como `root` ou administrador local. Isso é porque ele executa operações de rede, algumas vezes em um nível razoavelmente baixo, através de bibliotecas de rede, que requerem permissões altas e arriscadas do ponto de vista da estabilidade do sistema ou da confidencialidade de outras aplicações.



Como resultado, o Nmap pode ser visto como um componente sensível do sistema no qual está instalado. Certifique-se de que utiliza a versão mais recente do Nmap, uma vez que as versões mais antigas podem conter vulnerabilidades de segurança conhecidas. Ao utilizar uma versão actualizada, pode minimizar os riscos associados à utilização da ferramenta.



Se você optou por usar o Nmap não através de uma sessão como `root`, mas concedendo privilégios específicos a um usuário privilegiado para que ele tenha tudo o que precisa para usar o Nmap (`sudo` ou _capabilities_), esteja ciente de que o Nmap pode ser usado como parte de uma elevação completa de privilégio:



![nmap-image](assets/fr/65.webp)



elevação de privilégios do Nmap através do `sudo`._



Aqui, eu estou usando o comando Nmap através do `sudo`, mas isso me permite ter um shell interativo como `root` no sistema, o que não era o objetivo original.



Também é altamente desaconselhável instalar o Nmap em sistemas que não foram projetados para realizar varreduras de rede. Estou a pensar, em particular, em servidores ou estações de trabalho. Por um lado, isso acrescentaria um potencial vetor de elevação de privilégios, mas acima de tudo daria ao atacante acesso sem esforço a uma ferramenta ofensiva.



Por último, a segurança do sistema utilizado para a digitalização deve ser garantida de forma mais ampla, para que não se torne um vetor de intrusão ou de fuga de informação. Enquanto administrador de sistemas, é preferível utilizar um sistema dedicado, idealmente com um tempo de vida limitado, em vez da sua própria estação de trabalho.



### VI. Conclusão



Em conclusão, certifique-se de que domina corretamente o Nmap antes de o utilizar em condições reais ou de produção, e esteja atento ao processar e gerir os seus resultados. Seria uma pena causar danos, vazar dados ou facilitar um comprometimento, quando a abordagem inicial tem como objetivo melhorar a segurança da sua empresa.



## 13 - Varredura de portas via TCP: SYN, Connect e FIN



### I. Apresentação



Neste capítulo e no próximo, nós vamos dar uma olhada mais de perto nos diferentes tipos de scan TCP disponíveis no Nmap, começando com os mais comumente usados: Scans SYN, Connect e FIN.



Como deve ter notado, o Nmap oferece várias opções para scans TCP:



![nmap-image](assets/fr/66.webp)



técnicas de scanning disponíveis no Nmap._



A ideia aqui é explicar alguns destes métodos, para o ajudar a compreender as suas diferenças, as suas vantagens e as suas limitações. Verá que, consoante o contexto ou o que pretende saber, é preferível optar por uma ou outra opção.



### II. Pesquisa TCP SYN ou "Pesquisa meio aberta



O primeiro tipo de scan TCP que vamos analisar é o `TCP SYN Scan`, também conhecido como `Half Open Scan`. Se você se lembra dos scans de rede que fizemos após os primeiros scans de porta, este é o tipo de scan utilizado por padrão pelo [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) quando executado com direitos de root.



A tradução ajudá-lo-á a compreender como funciona este scan. De facto, um scan TCP SYN enviará um pacote TCP SYN para cada porta alvo, que é o primeiro pacote enviado por um cliente (o que pede para estabelecer uma ligação) como parte do famoso _Three way handshake_ TCP. Normalmente, se a porta estiver aberta no servidor de destino, com um serviço em execução por trás dela, o servidor enviará de volta um pacote TCP SYN/ACK para validar o SYN do cliente e inicializar a conexão TCP. Essa resposta toma a forma de um pacote TCP com os sinalizadores SYN e ACK definidos como 1, permitindo-nos confirmar que a porta está aberta e conduzindo a um serviço.



Por outro lado, se a porta estiver fechada, o servidor nos enviará um pacote `TCP` com os sinalizadores RST e ACK definidos como 1 para encerrar o pedido de conexão, então saberemos que nenhum serviço parece estar ativo por trás dessa porta:



![nmap-image](assets/fr/67.webp)



diagrama de comportamento do tCP SYN Scan para portas abertas e fechadas



Para obter uma visão mais concreta do `TCP SYN Scan`, realizei um scan da porta TCP/80 para um host que tinha um servidor web ativo nesta porta. Executando um scan de rede com o Wireshark, podemos ver o seguinte fluxo (fonte do scan: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



captura de rede durante um exame TCP SYN para uma porta aberta



Na primeira linha, vemos que a origem da varredura está enviando um pacote TCP para o host `10.10.10.203` na porta TCP/80. Nesse pacote TCP, o sinalizador SYN é definido como 1 para indicar que se trata de uma solicitação de inicialização de conexão TCP.



Depois, na segunda linha, vemos que o alvo responde com um `TCP SYN/ACK`, o que significa que aceita iniciar uma ligação e, portanto, receber fluxos na porta TCP/80. Podemos, portanto, deduzir que a porta TCP/80 está aberta e que um servidor web está presente no servidor verificado.



Nosso host então envia de volta um pacote RST para fechar a conexão, permitindo que o host escaneado não mantenha uma conexão TCP aberta esperando por uma resposta. No caso de um scan em muitas portas, não fechar as ligações TCP pode levar a uma negação de serviço, saturando o número de ligações à espera de resposta que o servidor pode manter (ver [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



No Wireshark, você poderá ver o status dos sinalizadores TCP para cada teste que realizarmos. Isso mostrará se o pacote é um pacote SYN, SYN/ACK, ACK, etc:



![nmap-image](assets/fr/69.webp)



ver os sinalizadores TCP de um pacote no Wireshark (TCP SYN aqui)



Por outro lado, executei o mesmo teste entre as duas máquinas, mas desta vez analisando uma porta TCP/81 na qual nenhum serviço está ativo (fonte de análise: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



captura de rede durante um exame TCP SYN para uma porta fechada



O host verificado retorna um `TCP RST/ACK` em resposta ao meu `TCP SYN` quando a porta não está aberta.



Como mencionado, ao executar o Nmap a partir de um terminal privilegiado, o TCP SYN Scan é o modo padrão, e pode ser forçado através da opção `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




O `TCP SYN Scan` é o scan mais comumente usado por razões de velocidade. Por outro lado, o facto de um cliente não finalizar o _Three Way Handshake_ (ou seja, não enviar o ACK após o SYN/ACK do servidor) pode parecer suspeito se for observado demasiadas vezes num servidor ou a partir da mesma fonte na rede. De facto, o comportamento normal de um cliente após receber um pacote TCP SYN/ACK em resposta a um TCP SYN é enviar um "reconhecimento" (ACK) e depois iniciar o Exchange.



No entanto, ele fornece uma varredura um pouco mais rápida, pois não se preocupa em enviar um ACK para cada resposta positiva. A vantagem do SYN Scan é a sua velocidade, uma vez que apenas um pacote é enviado por porta a ser verificada, à custa de uma maior probabilidade de deteção.



Além disso, o exame TCP SYN é capaz de detetar se uma porta está filtrada (protegida) por uma firewall. De facto, uma firewall em frente ao anfitrião alvo pode ser detectada pela forma como se comporta quando recebe um pacote TCP SYN numa porta que é suposto proteger. Ele simplesmente não responde. No entanto, como vimos, em ambos os casos (porta aberta ou fechada), há uma resposta do host. Esse terceiro comportamento revelará a presença de um firewall entre o host escaneado e a máquina que está executando o scan. Aqui está o resultado que o Nmap pode retornar quando uma porta escaneada é filtrada por um firewall:



![nmap-image](assets/fr/71.webp)



visualização do nmap quando se efectua um scan numa porta filtrada



Quando efectuamos uma captura de rede durante o scan, podemos ver que não é dada qualquer resposta:



![nmap-image](assets/fr/72.webp)



captura de rede durante um exame TCP SYN para uma porta filtrada por um firewall



A diferença entre uma porta fechada e uma porta filtrada é a seguinte: uma porta filtrada é uma porta protegida por uma firewall, enquanto uma porta fechada é uma porta na qual nenhum serviço está a ser executado e que, portanto, é incapaz de processar os nossos pacotes TCP. Alguns tipos de scan TCP, como o scan TCP SYN, são capazes de detetar se uma porta está filtrada, enquanto outros tipos de scan não conseguem.



### III. Verificação de ligação TCP ou verificação de abertura total



O segundo tipo de scan TCP é o `TCP Connect scan`, também conhecido como _Full Open Scan_. Ele funciona da mesma forma que o scan TCP SYN, mas desta vez retorna um `TCP ACK` após uma resposta positiva do servidor (um SYN/ACK). É por isso que é chamado de `Full Open`, pois a conexão é totalmente aberta e iniciada em todas as portas abertas durante a varredura, respeitando assim o TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



diagrama de comportamento do tCP Connect Scan para portas abertas e fechadas



Aqui está o que pode ser visto transitando pela rede durante um `TCP Connect scan` visando uma porta aberta:



![nmap-image](assets/fr/74.webp)



deteção de rede durante um exame TCP Connect para uma porta aberta



Podemos ver que o primeiro pacote TCP enviado é um `TCP SYN` enviado pelo cliente, e o servidor irá então responder com um `TCP SYN/ACK`, indicando que a porta está aberta e hospedando um serviço ativo. Para simular um cliente legítimo até o fim, o Nmap irá então enviar um `TCP ACK` de volta para o servidor. Por outro lado, ao escanear uma porta fechada:



![nmap-image](assets/fr/75.webp)



captura de rede durante um exame TCP Connect para uma porta fechada



Note que a resposta do servidor ao nosso pacote `SYN` é mais uma vez um pacote `TCP RST/ACK`, então podemos deduzir que a porta está fechada e nenhum serviço está rodando nela.



Ao utilizar o Nmap, a opção `-sT` (`scan Connect`) é utilizada para realizar um scan TCP Connect. Por favor, note que quando o Nmap é utilizado a partir de uma sessão sem privilégios, este é o modo de scan TCP padrão:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



O `TCP Connect Scan` simula uma solicitação de conexão mais legítima, com comportamento mais parecido com o de um cliente lambda, por isso é mais difícil detetar uma varredura em um número reduzido de portas. É, no entanto, mais lento, pois inicializa completamente todas as conexões TCP nas portas abertas da máquina verificada.



Um scan Nmap de 10.000 portas ainda será facilmente detetável se os serviços de deteção e proteção contra intrusões na rede (IDS, IPS, EDR) estiverem instalados. Quando um atacante quer manter um perfil discreto, tende a concentrar-se num pequeno número de portas estrategicamente escolhidas, como a 445 (SMB) ou a 80 (HTTP), que estão frequentemente abertas nos servidores e apresentam vulnerabilidades comuns.



Uma vez que o TCP Connect Scan espera uma resposta em ambos os casos, também pode detetar a presença de uma firewall que possa estar a filtrar portas no anfitrião de destino.



### IV. TCP FIN scan ou "Stealth Scan



O `TCP FIN Scan`, também conhecido como _Stealth Scan_, usa o comportamento de um cliente que termina uma conexão TCP para detetar uma porta aberta.



Em TCP, fim de sessão significa o envio de um pacote TCP com o sinalizador FIN definido como 1. Num Exchange normal, o servidor cessa toda a comunicação com o cliente (sem resposta). Se o servidor não tiver uma ligação TCP ativa com o cliente, enviará um `RST/ACK`. Podemos, portanto, diferenciar entre portas abertas e fechadas enviando pacotes `TCP FIN` para um conjunto de portas:



![nmap-image](assets/fr/76.webp)



diagrama de comportamento do scan tCP FIN para portas abertas e fechadas



Voltei a capturar a rede durante um _Stealth scoutan_ e isto é o que se vê quando a porta analisada está aberta:



![nmap-image](assets/fr/77.webp)



captura de rede durante um scan TCP FIN para uma porta aberta



Podemos ver que o cliente envia um ou dois pacotes para terminar uma ligação TCP e que o servidor não responde. Simplesmente aceita o fim da ligação e pára de comunicar.



Eis o que vemos agora quando analisamos uma porta fechada:



![nmap-image](assets/fr/78.webp)



captura de rede durante um scan TCP FIN para uma porta fechada



Vemos que o servidor envia de volta um pacote `TCP RST/ACK`, então há uma diferença de comportamento entre uma porta aberta e uma fechada, e somos capazes de listar as portas abertas num servidor enviando um pacote TCP FIN. Usando o Nmap, a opção `-sF` (`scan FIN`) é usada para executar um scan TCP FIN:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



O TCP FIN Scan não funciona em hosts Windows, porque o sistema operacional tende a ignorar os pacotes TCP FIN quando eles são enviados para portas que não estão abertas. Assim, se executar um TCP FIN Scan num anfitrião Windows, ficará com a impressão de que todas as portas estão fechadas.



É por isso que é importante estar familiarizado com vários métodos de digitalização e compreender a diferença entre eles.



Uma vez que em ambos os casos o TCP FIN não espera por uma resposta, não será capaz de detetar a presença de uma firewall entre o anfitrião de destino e a fonte de scan.



Aqui está um exemplo do resultado do scan TCP FIN do Nmap:



![nmap-image](assets/fr/79.webp)



resultados de um scan TCP FIN efectuado pelo Nmap



De facto, uma não resposta do anfitrião numa determinada porta pode significar que a porta está filtrada, mas também que está aberta e ativa.



Esta verificação é referida como "furtiva", uma vez que não gera muito tráfego e geralmente não causa registo nos sistemas visados. Pode ser usado para descobrir discretamente portas numa rede sem levantar qualquer alarme. No entanto, como mencionado acima, a sua eficácia pode variar dependendo do sistema alvo, assim como a sua discrição dependendo da configuração do equipamento de segurança.



### V. Conclusão



Lá se foi o primeiro de dois capítulos sobre os diferentes tipos de scan TCP oferecidos pelo Nmap! No próximo capítulo, nós veremos os tipos de scan TCP XMAS, Null e ACK, que operam de maneiras diferentes para detetar portas abertas em um host.





## 14 - Varredura de portas via TCP: XMAS, Null e ACK



### I. Apresentação



Nesta secção, nós vamos continuar a explorar os vários métodos de scan TCP oferecidos pelo Nmap. Aqui nós veremos os métodos `XMAS`, `Null` e `ACK`, que utilizam caraterísticas específicas do TCP para obter informações sobre as portas e serviços abertos num determinado alvo.



### II. Verificação TCP XMAS



O XMAS Scan TCP é um pouco incomum, pois não simula o comportamento normal do usuário ou da máquina em uma rede. De facto, o XMAS Scan envia pacotes TCP com as bandeiras `URG` (Urgente), `PSH` (Push) e `FIN` (Finish) definidas para 1, de forma a contornar certas firewalls ou mecanismos de filtragem.



O nome XMAS vem do facto de que ver estas bandeiras ligadas é invulgar. Quando os três sinalizadores são definidos simultaneamente num pacote TCP, parece uma árvore de Natal iluminada:



![nmap-image](assets/fr/80.webp)



sinalizadores tCP utilizados na verificação XMAS



Sem entrar em detalhes sobre o papel dessas flags aqui, é importante saber que ao enviar um pacote com essas três flags habilitadas, um serviço ativo atrás da porta alvo não retornará nenhum pacote. Por outro lado, se a porta estiver fechada, receberemos um pacote TCP RST/ACK. Agora podemos diferenciar o comportamento de uma porta aberta e de uma porta fechada ao listar as portas de uma máquina:



![nmap-image](assets/fr/81.webp)



diagrama de comportamento do tCP XMAS Scan para portas abertas e fechadas



Ainda seguindo a mesma lógica, uma varredura de rede na porta TCP/80 de um host com um servidor web ativo mostra o seguinte comportamento ao detetar uma porta aberta (fonte de varredura `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



captura de rede durante um scan TCP XMAS para uma porta aberta



Podemos observar que a origem da varredura envia dois pacotes TCP XMAS (com as flags `FIN`, `PSH` e `URG` definidas como 1) para o host `10.10.10.203` e que não há retorno do destino, indicando que a porta está aberta. Por outro lado, ao executar um `TCP XMAS Scan` em uma porta fechada, o seguinte resultado é observado:



![nmap-image](assets/fr/83.webp)



captura de rede durante um scan TCP XMAS para uma porta fechada



A resposta ao nosso pacote TCP é então um `TCP RST/ACK`, indicando que a porta está fechada. Para utilizar esta técnica com o Nmap, a opção `-sX` (`scan XMAS`) permite-lhe efetuar um TCP XMAS Scan:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



É importante notar que o exame TCP XMAS não é capaz de detetar firewalls que possam estar entre o alvo e a máquina de exame, ao contrário de alguns outros tipos de exame como o TCP SYN ou Connect. De facto, uma firewall ativa entre os dois hospedeiros assegurará que não haja retorno TCP se a porta alvo estiver filtrada (ou seja, protegida pela firewall). Em caso de não resposta, é portanto impossível saber se a porta está protegida pela firewall ou se está aberta e ativa. Deve também ter em atenção que, tal como o exame TCP FIN, certas aplicações ou sistemas operativos como o Windows podem distorcer os resultados deste tipo de exame.



nota: o suporte para verificações XMAS/FIN/NULL em versões recentes do Windows permanece limitado e os resultados podem ser inconsistentes neste tipo de alvo. (Atualização 2025)



### III. TCP Null scan



Em contraste com o TCP XMAS scan, o TCP Null scan enviará pacotes TCP scan com todas as bandeiras definidas para 0. Este também é um comportamento que nunca será encontrado num Exchange normal entre máquinas, uma vez que o envio de um pacote TCP sem uma bandeira não é especificado no RFC que descreve o protocolo TCP. É por isso que ele pode ser detectado mais facilmente.



Tal como o exame TCP XMAS, este exame pode interferir com determinadas firewalls ou módulos de filtragem, permitindo a passagem de pacotes:



![nmap-image](assets/fr/84.webp)



diagrama de comportamento do tCP Null Scan para portas abertas e fechadas



Aqui está o que pode ser visto na rede durante uma verificação TCP Null numa porta aberta:



![nmap-image](assets/fr/85.webp)



captura de rede durante um scan TCP Null para uma porta aberta



A máquina de scanning envia um pacote sem bandeira (`[<None>]` no Wireshark) sem qualquer resposta do servidor. Por outro lado, quando a porta de destino está fechada:



![nmap-image](assets/fr/86.webp)



captura de rede durante um scan TCP Null para uma porta fechada



Para realizar um scan TCP Null com o Nmap, simplesmente utilize a opção `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Uma vez que a resposta quando uma porta está aberta e quando uma firewall está ativa (nenhum feedback do servidor em ambos os casos) é idêntica, o TCP Null scan não consegue detetar a presença de uma firewall. Além disso, o firewall pode até falsificar o resultado, sugerindo que uma porta está aberta, pois não responde a pacotes TCP sem sinalizadores, mesmo que a porta esteja filtrada. Esta é uma informação importante a ter em conta quando se utilizam scans que não conseguem diferenciar entre uma porta aberta e uma porta filtrada (protegida por firewall), como os scans `TCP Null`, `XMAS` ou `FIN`, de forma a manter a consistência na interpretação dos resultados obtidos.



### IV. Verificação TCP ACK



O exame TCP ACK é utilizado para detetar a presença de uma firewall no anfitrião de destino ou entre o destino e a origem do exame.



Ao contrário de outros scans, o scan TCP ACK não tenta identificar quais portas estão abertas no host, mas sim se um sistema de filtragem está ativo, respondendo para cada porta com `filtered` ou `unfiltered`. Alguns scans TCP, como o `TCP SYN` ou o `TCP Connect`, podem fazer as duas coisas ao mesmo tempo, enquanto outros, como o `TCP FIN` ou o `TCP XMAS`, não conseguem determinar a presença de filtragem. É por isso que a varredura TCP ACK pode ser útil:



![nmap-image](assets/fr/87.webp)



diagrama de comportamento do tCP ACK Scan para portas filtradas e não filtradas



Nós usaremos a opção `-sA` do Nmap para realizar esse tipo de scan. Aqui está o resultado de um scan TCP ACK se a porta estiver filtrada, ou seja, bloqueada e protegida por um firewall:



![nmap-image](assets/fr/88.webp)



visualização do nmap durante o TCP ACK Scan._



Exemplo de resultado para um host com um firewall e outro sem. O Nmap retorna `filtered` nas portas TCP/80 e TCP/81 do host `10.10.10.203`. Em uma análise de rede via Wireshark, o comportamento é o seguinte:



![nmap-image](assets/fr/89.webp)



captura de rede durante um scan TCP ACK para uma porta não filtrada por uma firewall



A máquina de destino não devolve nada se estiver presente uma firewall.



Para lançar este scan com o Nmap, utilize a opção `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Conclusão



Para além dos métodos já apresentados, analisámos três métodos diferentes de análise via TCP. Estes diferentes métodos devem ser utilizados em condições e contextos muito específicos, nomeadamente no contexto de testes de penetração ou de operações de equipas vermelhas, durante as quais estão presentes noções de discrição.



## 15 - Nmap CheatSheet - Resumo dos comandos do tutorial



### I. Apresentação



Aqui está um breve resumo dos muitos comandos do Nmap e casos de uso, para que você possa rapidamente encontrá-los e reutilizá-los no dia a dia.



### II. Nmap: CheatSheet IT-Connect



Aqui está uma folha de dicas dos comandos apresentados. Esta página torna fácil encontrar os usos mais comuns do Nmap.





- Verificação do porto




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Descobrir anfitriões activos




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



nota: A opção `-sP` está obsoleta há vários anos e deve ser substituída por `-sn`. (Atualização 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Deteção de versões




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Scripts NSE: à procura de vulnerabilidades




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Gestão dos resultados do Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Otimização do desempenho




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Tipos de varrimento TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Espero que estes comandos sejam úteis. Não se esqueça de adaptar o alvo dos seus exames ao seu contexto e de consultar a documentação oficial para dominar completamente os testes efectuados.



### III. Conclusão



O tutorial do Nmap está completo. Agora você tem o básico necessário para usar esta ferramenta abrangente e poderosa. Aconselhamo-lo vivamente a praticar em ambientes controlados (Hack The Box, VulnHub, máquinas virtuais) antes de o utilizar em produção.



Ainda há muito a ser explorado sobre o funcionamento interno da ferramenta e seus recursos avançados. No entanto, o domínio dos comandos e conceitos aqui apresentados permitir-lhe-á utilizar o Nmap com confiança e relevância.