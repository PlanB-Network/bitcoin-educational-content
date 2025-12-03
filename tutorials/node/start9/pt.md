---
name: Início9

description: Tutorial sobre a configuração de um servidor privado Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Aqui está um tutorial em vídeo da Southern Bitcoiner, um guia em vídeo que mostra como configurar e usar um servidor pessoal Start9 / StartOS e como executar um nó de bitcoin.*


## 1️⃣ Introdução


### O que é exatamente o Start9?


A Start9 é uma empresa fundada em 2020, mais conhecida por desenvolver o [**StartOS**,](https://github.com/Start9Labs/start-os) um sistema operativo baseado em Linux concebido para servidores pessoais. Permite que os utilizadores alojem facilmente uma vasta gama de serviços de software - tais como nós Bitcoin e Lightning, aplicações de mensagens ou gestores de palavras-passe, mantendo o controlo total sobre os seus dados e eliminando a dependência de plataformas tecnológicas centralizadas. O StartOS apresenta uma interface fácil de utilizar e baseada no browser, um Marketplace com curadoria para instalar serviços e ferramentas de privacidade incorporadas, como a integração do Tor e a encriptação HTTPS em todo o sistema. A Start9 também fornece dispositivos de hardware pré-carregados com o SO, embora o software possa ser instalado em hardware compatível ou em máquinas virtuais (VMs).


### Quais são as opções disponíveis?


A Start9 oferece opções de implementação pré-construídas e DIY. O [**Server One**] (https://store.start9.com/collections/servers/products/server-one) e o [**Server Pure**] (https://store.start9.com/collections/servers/products/server-pure) são dispositivos de hardware oficiais com componentes de elevado desempenho: o Server One utiliza um processador **AMD Ryzen 7 5825U** com RAM configurável (16 GB-64 GB) e armazenamento (SSD NVMe de 2 TB-4 TB), enquanto o Server Pure está equipado com um **Intel i7-10710U**, oferecendo também opções de RAM e armazenamento configuráveis. Ambos incluem **apoio técnico vitalício** quando adquiridos diretamente à Start9. Para os utilizadores que preferem flexibilidade, o StartOS pode ser instalado gratuitamente numa vasta gama de hardware existente, incluindo computadores portáteis, computadores de secretária, mini PCs e computadores de placa única, ou em VMs.


![image](assets/en/01.webp)


### Quais são as diferenças em relação à Umbrel?


O StartOS e o Umbrel simplificam a instalação de serviços auto-hospedados, mas diferem na arquitetura e nas funcionalidades. O Umbrel funciona como uma camada de aplicação em sistemas Debian/Ubuntu ou VMs, enquanto o Start9 é um sistema operativo dedicado que requer instalação direta em hardware ou VM. O Umbrel apresenta uma interface polida, inspirada no macOS, enquanto o Start9 dá prioridade a um design funcional e minimalista. O Umbrel oferece uma maior [seleção de aplicações] (https://apps.umbrel.com/), enquanto o [Start9 Marketplace] (https://marketplace.start9.com/) compensa com capacidades técnicas avançadas. O Start9 simplifica o acesso a definições avançadas através de formulários de IU validados, reduzindo a necessidade de interação com a linha de comandos. Também se destaca na gestão de cópias de segurança com cópias de segurança encriptadas do sistema com um clique, uma caraterística que a Umbrel não possui nativamente. O StartOS fornece ferramentas de monitorização incorporadas e impõe a encriptação HTTPS para acesso à rede local, aumentando a segurança. A Umbrel usa HTTP não encriptado localmente, embora ambas as plataformas suportem acesso remoto seguro via Tor. A Umbrel é adequada para utilizadores que dão prioridade a um ecossistema de aplicações rico e a uma interface de utilizador polida. O Start9 é uma forte escolha para quem valoriza a segurança, a configurabilidade, a fiabilidade das cópias de segurança e a gestão avançada de serviços sem necessitar de conhecimentos de linha de comandos. Para saber mais sobre o Umbrel e as diferenças em relação ao Start9, visite este curso:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ Pré-requisitos DIY: Especificações mínimas e recomendadas


Para uma utilização básica com serviços mínimos, as **especificações mínimas** são: **1 núcleo vCPU (2.0GHz+ boost), 4GB de RAM, 64GB de armazenamento**, e uma porta Ethernet. Dito isto, eu recomendaria ir muito além disso, especialmente se estiver a executar um Nó Bitcoin. Pessoalmente, comecei com 1TB e rapidamente fiquei sem espaço. É melhor apontar para **pelo menos 2TB de armazenamento**, juntamente com uma ** CPU quad-core (2.5GHz+)** e **8GB+ RAM**. Isso faz uma enorme diferença no desempenho e na longevidade. Se quiser ir mais fundo, aqui está um tópico atualizado da comunidade sobre [Hardware Capable of Running StartOS] (https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Download e Flashing do Firmware


Para iniciar a configuração, use um computador separado para visitar o [site do Start9](https://start9.com/), e navegue até a seção de documentação clicando em `DOCS`. A partir daí, acesse os `Guias de flashing` para encontrar a versão apropriada do StartOS. Duas opções estão disponíveis:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Este tutorial cobre a opção `x86/ARM`.


A versão mais recente do SO pode ser descarregada a partir da [página de lançamento do Github](https://github.com/Start9Labs/start-os/releases/latest). versões [Pre-release](https://github.com/Start9Labs/start-os/releases) também estão disponíveis para usuários que desejam testar novas funcionalidades. Na parte inferior da página, em `Assets`, faça o download do `x86_64` ou `x86_64-nonfree.iso`.  A imagem `x86_64-nonfree.iso` contém software não-livre (de código fechado) necessário para o Server One e a maioria do hardware DIY, particularmente para gráficos e suporte a dispositivos de rede.


Recomenda-se verificar a integridade do arquivo verificando seu hash SHA256 contra o listado no GitHub. Para Linux, o comando `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` pode ser usado, com outros sistemas operacionais cobertos na documentação.


Depois de descarregar e verificar a imagem StartOS, esta deve ser flasheada para uma unidade USB. o `BalenaEtcher` é um software recomendado para esta tarefa. É uma ferramenta gratuita e de código aberto para gravar ficheiros de imagem do SO em unidades USB e cartões SD, disponível para Windows, macOS e Linux. Baixe a versão apropriada do site oficial [Balena Etcher website] (https://www.balena.io/etcher/) e execute o instalador. Conecte a unidade USB ou cartão SD de destino, abra o Balena Etcher e clique em `Flash from file` para selecionar a imagem do sistema operacional baixada. O Etcher detectará automaticamente as unidades conectadas; selecione o destino correto se houver várias unidades. Clique em `Flash!` para iniciar a gravação da imagem. O Etcher valida automaticamente o processo de gravação após a conclusão. Uma vez terminado, retire a unidade em segurança e utilize-a para arrancar o dispositivo.


![image](assets/en/19.webp)


## 4️⃣ Configuração inicial


Para a configuração inicial, consulte a página Start9 [documentation](https://docs.start9.com/0.3.5.x/) em `USER MANUAL` seguido de `Getting Started - Initial Setup`.  Este guia oficial deve ser consultado para obter as informações mais actualizadas.


São apresentadas duas opções:



- Começar de novo
- Opções de recuperação


Para uma nova instalação de servidor, selecione `Start Fresh`. Em primeiro lugar, ligue o servidor à corrente eléctrica e a um cabo Ethernet. Certifique-se de que o computador utilizado para a configuração está na mesma rede local. Remova a unidade USB recém-flashed do computador e insira-a no servidor.


É possível controlar o servidor remotamente a partir de qualquer computador na mesma rede. Abra um browser da Web e navegue até `http://start.local`.


**Nota**: Se ocorrerem problemas de ligação com este endereço, isso deve-se frequentemente ao facto de as redes domésticas não conseguirem resolver os nomes de domínio `.local'. O problema pode ser resolvido acedendo diretamente ao servidor através do seu endereço IP. O IP pode ser encontrado entrando na interface de administração do router (normalmente em `192.168.1.1` ou num endereço semelhante) e localizando o dispositivo na lista de clientes DHCP ou de mapas de rede. Em seguida, introduza o endereço IP completo (por exemplo, `http://192.168.1.105`) no browser. Isto evita a resolução de DNS. Se os problemas persistirem, consulte a página [Problemas comuns] (https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) ou [contacte o suporte] (https://start9.com/contact/)


Deverá aparecer o ecrã de configuração do StartOS. Clique em `Start Fresh` para iniciar a configuração do novo servidor.


![image](assets/en/03.webp)


O passo seguinte é selecionar a unidade de armazenamento onde os dados do StartOS serão armazenados.


![image](assets/en/04.webp)


Defina uma `Password` forte para o servidor. Grave-a como aconselhado pelo Start9, depois clique em `FINISH`.


![image](assets/en/05.webp)


Uma tela mostrará que o StartOS está inicializando e configurando o servidor. O próximo passo é `Download address info` já que o endereço `start.local` é apenas para fins de configuração e não funcionará depois.


![image](assets/en/06.webp)


O ficheiro de configuração contém dois endereços de acesso críticos: um para a `rede local (LAN)` e outro para o acesso seguro via `Tor`. Ambos os endereços devem ser salvos em um gerenciador de senhas seguro. O próximo passo é `Confiar na sua CA Raiz`. Abra um novo separador do browser e siga as instruções para confiar na Root CA e iniciar sessão. O certificado da Root CA também pode ser baixado clicando em `Download certificate` no arquivo baixado.


## 5️⃣ Confie na sua CA de raiz


Após o download do certificado, a `Root CA` do servidor deve ser confiável para o sistema operacional. Clique em `Ver Instruções` e encontre as diretrizes para o sistema operacional específico.


![image](assets/en/07.webp)


Para um sistema Linux, são utilizados os seguintes comandos. Primeiro, abra um Terminal e instale os pacotes necessários:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Navegue até o diretório onde o certificado foi baixado, normalmente `~/Downloads` . Execute estes comandos para adicionar o certificado ao armazenamento de confiança do sistema operacional. Mude para a pasta de downloads com `cd ~/Downloads`. Crie o diretório necessário com `sudo mkdir -p /usr/share/ca-certificates/start9`. Copiar o arquivo de certificado, substituindo `seu-filename.crt` pelo nome do arquivo, usando `sudo cp "seu-filename.crt" /usr/share/ca-certificates/start9/`. Registre o certificado permanentemente anexando seu caminho à configuração do sistema com `sudo bash -c "echo 'start9/seu-nome-do-filme.crt' >> /etc/ca-certificates.conf"`. Finalmente, reconstrua o trust store com `sudo update-ca-certificates`. É crucial usar o nome real do arquivo do certificado e verificar todos os caminhos antes de executar esses comandos. Este processo estabelece confiança permanente para as conexões HTTPS do servidor Start9.


Uma instalação bem sucedida será indicada por uma saída dizendo `1 added`. A maioria das aplicações será então capaz de se conectar de forma segura via `https`. Se estiver a utilizar o Firefox, é necessário um [passo final] adicional (https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). Para o Chrome ou Brave, é necessário um [passo final] diferente (https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) para configurar o navegador para respeitar a Root CA. Teste a ligação actualizando a página. Se o problema persistir, saia e reabra o navegador antes de revisitar a página.


![image](assets/en/08.webp)


## 6️⃣ Introdução ao StartOS


Deverá agora ser possível iniciar sessão utilizando uma ligação HTTPS segura. Introduza a `Senha` para aceder ao `Painel de Boas Vindas`.


![image](assets/en/09.webp)


Este ecrã fornece atalhos úteis para começar. A barra lateral esquerda contém os itens do menu principal para navegação.


## 7️⃣ Sistema


O separador Systems (Sistemas) no StartOS fornece acesso às principais funções do sistema para gerir o servidor pessoal. Oferece ferramentas para manutenção, segurança, diagnóstico e configuração do sistema sem exigir conhecimentos de linha de comandos.


A secção `Backups` permite a criação de backups completos do sistema, incluindo serviços, configurações e dados, que podem ser restaurados posteriormente. Isso é essencial para recuperação de desastres ou migração para um novo hardware. Os backups podem ser armazenados em unidades externas e são criptografados usando a senha mestra.


A secção `Gestão` no separador Sistemas permite o controlo das principais funções do sistema. Os utilizadores podem verificar e aplicar manualmente as actualizações do StartOS, mantendo o controlo sobre o processo de atualização do sistema. É possível efetuar o sideload de serviços personalizados ou de terceiros não disponíveis no mercado oficial. Se o servidor não estiver ligado através de Ethernet, as definições de Wi-Fi podem ser configuradas a partir desta secção. Os utilizadores avançados podem ativar o acesso SSH para gestão do sistema ao nível do terminal.


![image](assets/en/10.webp)


A secção `Insights` fornece monitorização em tempo real do desempenho e saúde do servidor, mostrando a utilização da CPU, RAM e disco através de gráficos. Também mostra a temperatura do sistema, o que é útil para dispositivos como o Raspberry Pi que não têm refrigeração ativa. As métricas de tempo de atividade e média de carga ajudam a avaliar a estabilidade do sistema, e os registos em tempo real estão disponíveis para a resolução de problemas de serviço ou do sistema.


A secção `Support` oferece acesso a FAQs incorporadas, documentação oficial e canais de suporte da comunidade. Os registos de depuração podem ser transferidos a partir desta secção para partilhar com o suporte Start9 para uma resolução mais rápida dos problemas.


![image](assets/en/11.webp)


## 8️⃣ Mercado


O `Marketplace` é usado para descobrir, instalar e gerenciar serviços no servidor pessoal. Ele fornece acesso a softwares como o Bitcoin Core, BTCPay Server, e electrs. O StartOS suporta múltiplos marketplaces, incluindo o Registo oficial do Start9 e registos geridos pela comunidade. Estes podem ser adicionados clicando em `CHANGE` e mudando para o `Community Registry`, que fornece acesso a uma gama mais ampla de serviços.


![image](assets/en/12.webp)


## 9️⃣ Instalação de um nó completo Bitcoin


A instalação de um Bitcoin full node no StartOS proporciona total soberania sobre a experiência do Bitcoin. Permite a validação de transacções e aumenta a privacidade e a segurança, eliminando a dependência de serviços externos que possam registar a atividade. O controle total sobre as transações é obtido, permitindo que elas sejam transmitidas diretamente para a rede. A opção padrão é `Bitcoin Core`, que se integra nativamente com o StartOS e permite a conexão com carteiras como Specter, Sparrow, ou Electrum para uma configuração de auto-custódia. Uma alternativa, `Bitcoin Knots`, também está disponível através do Community Registry.


Para instalar o Bitcoin Core, navegue até o Marketplace. No registro padrão, localize e instale o serviço Bitcoin Core. Após a instalação, um prompt `Needs Config` aparecerá, exigindo que as configurações sejam concluídas antes que o serviço possa ser executado. Isso geralmente ocorre após atualizações ou novas instalações e solicita uma revisão das `configurações do RPC`. Continue com a configuração padrão e clique em `Salvar`.


![image](assets/en/13.webp)


Uma vez totalmente sincronizado, o seu nó pode servir como um backend privado para carteiras como a Sparrow, proporcionando maior privacidade e validação de transacções. No entanto, para os utilizadores que armazenam quantidades significativas, é fundamental compreender os compromissos de segurança desta ligação direta. Quando um wallet se conecta diretamente ao Bitcoin Core, ele pode expor dados confidenciais, pois o Bitcoin Core armazena chaves públicas (xpubs) e saldos do wallet não criptografados na máquina host. Um sistema comprometido pode permitir que um invasor descubra seus acervos e o atinja.


Para mitigar esse risco e obter um modelo de segurança mais robusto, é possível configurar um Electrum Server privado. Este servidor actua como um intermediário, indexando a blockchain sem armazenar qualquer informação específica do wallet. Ao conectar seu wallet ao seu próprio servidor Electrum em vez de diretamente ao Bitcoin Core, você impede que o wallet acesse os dados confidenciais do nó.


![image](assets/en/14.webp)


## configurar os eléctricos


o `electrs` (Electrum Rust Server) é um indexador rápido e eficiente que se conecta ao seu nó Bitcoin Core e permite que carteiras compatíveis com o Electrum consultem o histórico de transações e saldos em tempo real. Ao executar o electrs no StartOS, você elimina a dependência de servidores Electrum de terceiros, melhorando significativamente a privacidade e a segurança - suas consultas wallet vão diretamente para o seu nó auto-hospedado.


Para o configurar, comece por instalar o serviço electrs a partir do StartOS Marketplace. O sistema exigirá que o Bitcoin Core seja totalmente sincronizado antes de prosseguir. Após a instalação, confirme as configurações `Needs Config` com os padrões recomendados e o electrs começa a indexar o blockchain, o que pode levar até um dia, dependendo do seu hardware.


![image](assets/en/15.webp)


Uma vez concluído, pode ligar carteiras como a Sparrow ou a Specter. Uma ligação bem sucedida permite que o seu wallet se sincronize diretamente com o seu nó, proporcionando uma experiência Bitcoin segura, privada e auto-hospedada.


## 1️⃣1️⃣ Ligar Sparrow Wallet


Para conectar o `Sparrow Wallet` ao seu nó StartOS usando a implementação do electrs, primeiro certifique-se de que o Bitcoin Core está totalmente sincronizado e o electrs está instalado e em execução. Abra o Sparrow Wallet no seu dispositivo e navegue até `File` -> `Settings` -> `Server`. Depois escolha `Private Electrum Server`. No campo URL, introduza o `Tor hostname` e `Port` do electrs, que pode ser encontrado no StartOS em `Services` -> `electrs` -> `Properties` (normalmente terminando em `.onion:50001`).


![image](assets/en/16.webp)


Em seguida, habilite o Tor marcando a opção `Use Proxy`, definindo o endereço do proxy como `127.0.0.1` e a porta como `9050`. Clique em `Testar Conexão` e aguarde alguns instantes. Uma conexão bem sucedida exibirá uma mensagem de confirmação como `Connected to electrs`. Uma vez verificada, feche as configurações e prossiga para criar ou restaurar seu wallet. Esta configuração garante que o seu wallet consulta o seu próprio nó através do electrs, fornecendo total privacidade e operação sem confiança.


![image](assets/en/17.webp)


## 🎯 Conclusão


O StartOS da Start9 é uma plataforma de fácil utilização e focada na privacidade, concebida para auto-hospedar serviços essenciais como nós Bitcoin e Lightning, carteiras e aplicações pessoais. Elimina a necessidade de competências de linha de comandos, oferecendo uma interface gráfica limpa, cópias de segurança automatizadas, monitorização da saúde e acesso seguro ao Tor, tornando-o ideal para utilizadores não técnicos. A sua arquitetura modular suporta uma integração perfeita com ferramentas como electrs ou Sparrow, dando-lhe controlo total sobre a sua soberania financeira e digital. Com um forte foco na transparência, controlo local e extensibilidade, o StartOS permite que os utilizadores recuperem a propriedade de plataformas centralizadas e executem a sua própria infraestrutura privada e resiliente.