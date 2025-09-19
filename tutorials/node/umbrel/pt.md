---
name: Umbrel
description: Descubra e instale o Umbrel - Seu nó Bitcoin e servidor doméstico
---

![cover](assets/cover.webp)



## Introdução



### O que é um nó Bitcoin?



Um nó Bitcoin é um computador que participa na rede Bitcoin, executando o software Bitcoin Core ou um cliente alternativo. O seu papel é essencial para o funcionamento e a segurança da rede:





- **Armazenamento do Blockchain**: Mantém uma cópia completa e actualizada do Blockchain Bitcoin
- **Verificação da transação**: valida cada transação e bloco de acordo com as regras do protocolo
- **Divulgação de informações**: Partilha novas transacções e blocos com outros nós
- **Criação de consensos**: Contribui para a aplicação das regras da rede



Gerir o seu próprio nó Bitcoin é um passo crucial para a soberania financeira, oferecendo vários benefícios importantes:





- **Confidencialidade**: Partilhe as suas transacções sem revelar as suas informações a terceiros
- **Resistência à censura**: Ninguém o pode impedir de utilizar o Bitcoin
- **Verificação independente**: Não é necessário confiar nos nós de outras pessoas para verificar as suas transacções
- **Criação de consenso**: Contribuir para a aplicação das regras da rede Bitcoin
- **Apoio à rede**: Tornar-se um participante ativo na distribuição e descentralização da rede



### Umbrel: Uma solução simples para executar um nó Bitcoin



Umbrel é um sistema operacional de código aberto que simplifica a instalação e o gerenciamento de um nó Bitcoin. Ele também transforma seu computador em um servidor doméstico pessoal e privado, facilitando a hospedagem de :





- Um nó Bitcoin completo
- Bitcoin aplicações essenciais (Electrs, Mempool.space)
- Outros serviços pessoais (armazenamento em nuvem, streaming, VPN, etc.)



Com o seu elegante e intuitivo Interface utilizador Interface, a Umbrel torna os serviços auto-hospedados acessíveis a todos, mantendo o controlo total sobre os seus dados.



## Opções de instalação do guarda-chuva



A Umbrel oferece duas formas principais de utilizar a sua solução: uma opção chave-na-mão (Umbrel Home) e uma versão gratuita de código aberto (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: A solução chave na mão



O Umbrel Home é um servidor doméstico pré-configurado, especialmente concebido para uma experiência óptima. Esta solução de hardware tudo-em-um inclui:



**Caraterísticas de hardware**




- Processador de alto desempenho optimizado para auto-hospedagem
- Armazenamento SSD de alta velocidade pré-instalado
- Sistema de arrefecimento silencioso
- Design compacto e elegante
- Portas USB e Ethernet integradas



**Vantagens exclusivas**




- Instalação "plug-and-play": ligar e pronto
- Suporte premium com assistência dedicada
- Actualizações automáticas garantidas
- Assistente de migração integrado
- Garantia total de hardware
- Suporte completo para todas as funcionalidades



**Preço**: 399 euros (o preço pode variar consoante a época)



### UmbrelOS: A versão de código aberto



O UmbrelOS é a versão gratuita e de código aberto do sistema operativo Umbrel. Esta solução flexível permite-lhe utilizar o seu próprio hardware enquanto beneficia das caraterísticas essenciais da Umbrel.



**Benefícios**




- Totalmente gratuito
- Código-fonte aberto e verificável
- Liberdade de escolha
- Opções avançadas de personalização



**Plataformas suportadas**




- Raspberry Pi 5: Uma solução popular e económica
- Sistemas X86: Para PCs ou servidores padrão
- Máquina virtual: Para testes ou utilização na infraestrutura existente



**Limitações**




- Apenas apoio comunitário
- Algumas funcionalidades avançadas reservadas para a Umbrel Home
- Configuração inicial mais técnica
- O desempenho depende do hardware selecionado



Esta versão é ideal para :




- Utilizadores técnicos
- Quem já possui equipamento compatível
- Pessoas que querem aprender e experimentar
- Os promotores que desejem contribuir para o projeto



Ligações oficiais de instalação :




- [Instalação em Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Instalação em sistemas x86 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Instalação de máquina virtual](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



Neste tutorial, vamos concentrar-nos na instalação do UmbrelOS num Raspberry Pi 5, mas os princípios básicos são semelhantes para outras plataformas.



## Instalar o Umbrel OS no Raspberry Pi 5



### Componentes necessários



Para esta instalação, é necessário :





- Raspberry Pi 5 (4 GB ou 8 GB de RAM)
- Um Raspberry Pi power Supply oficial (crucial para a estabilidade!)
- Cartão microSD (mínimo de 32 GB)
- Um leitor de cartões microSD
- Um SSD externo para armazenamento de dados
- Cabo Ethernet
- Um cabo USB para ligar o SSD



### Passos de instalação



**Descarregar o UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Visitar o [sítio Web oficial](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Descarregar a versão mais recente do UmbrelOS para Raspberry Pi 5



**Instalação de Balena Etcher**



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Descarregar e instalar [Balena Etcher] (https://www.balena.io/etcher/) no seu computador



**Preparar o cartão microSD**



![Insertion carte microSD](assets/fr/03.webp)




- Insira o seu cartão microSD no leitor de cartões do seu computador



**Imagem a piscar**



![Flashage UmbrelOS](assets/fr/04.webp)




- Lançamento do Balena Etcher
- Selecionar a imagem UmbrelOS descarregada
- Escolha o seu cartão microSD como destino
- Clique em "Flash!" e aguarde que o processo termine
- Ejetar o cartão com segurança



**Instalação do cartão microSD**



![Installation microSD](assets/fr/05.webp)




- Insira o cartão microSD no seu Raspberry Pi 5



**Ligação periférica**



![Connexion périphériques](assets/fr/06.webp)




- Ligar o SSD externo a uma porta USB disponível
- Ligar o cabo Ethernet entre o Pi e o seu router



**Ligar**



![Démarrage du Pi](assets/fr/07.webp)




- Ligar a alimentação oficial do Raspberry Pi Supply
- Aguardar alguns minutos para que o sistema arranque



**Primeiro acesso**



![Accès interface web](assets/fr/08.webp)




- Num dispositivo ligado à mesma rede, abra o seu browser
- Aceder ao sítio Web do Interface da Umbrel em: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Se `umbrel.local` não funcionar, terá de encontrar o IP Address da sua Raspberry Pi na sua rede local. Você pode :




- Consulte o Interface do seu router
- Utilizar um scanner de rede como o nmap
- Utilize o comando `arp -a` no terminal do seu computador



## Primeiro passo no Umbrel



Quando o Umbrel estiver iniciado e acessível através do seu browser, siga estes passos para começar:



### Configuração inicial



**Criar a sua conta**



![Création compte](assets/fr/10.webp)




- Escolher um nome de utilizador
- Definir uma palavra-passe segura
- Precisará destas credenciais para aceder ao seu Umbrel



**Confirmação da conta**



![Confirmation compte](assets/fr/11.webp)




- Clique em "Seguinte" para aceder ao seu painel de controlo



**Descoberta do Interface**



![Interface Umbrel](assets/fr/12.webp)




- Aceder à Umbrel App Store
- Descubra as muitas aplicações disponíveis
- Vamos começar por instalar as aplicações essenciais para o Bitcoin



### Instalação de aplicações Bitcoin



**Nó Bitcoin**



![Bitcoin Node](assets/fr/13.webp)




- Primeira aplicação a instalar
- Descarregar e verificar a totalidade do Blockchain Bitcoin



**Eleitores**



![Installation Electrs](assets/fr/14.webp)




- Servidor Electrum para ligar as carteiras Bitcoin
- Sincroniza-se com o seu nó Bitcoin



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Ecrã Interface para Blockchain
- Acompanha as transacções e os bloqueios em tempo real



## Seguimento de uma transação com o Mempool.space



O Mempool.space é um explorador Blockchain de código aberto que fornece visualização em tempo real da rede Bitcoin. Permite-lhe seguir as suas transacções e compreender como as transacções se propagam na rede.



### Compreender o Mempool e as confirmações



O "Mempool" (pool de memória) é como uma sala de espera virtual onde todas as transacções Bitcoin não confirmadas são armazenadas antes de serem incluídas num bloco. Eis como uma transação é processada:



1. **Difusão**: Quando se envia uma transação, esta é primeiro difundida na rede Bitcoin


2. **Em espera no Mempool**: À espera de ser selecionado por um Miner com base nos custos


3. **Primeira confirmação**: Um menor inclui-o num bloco (1ª confirmação)


4. **Confirmações adicionais**: Cada novo bloco extraído após aquele que contém a sua transação acrescenta uma confirmação



O número recomendado de confirmações depende do montante :




- Para pequenas quantidades: 1-2 confirmações podem ser suficientes
- Para montantes elevados: 6 confirmações são geralmente consideradas muito seguras



### Explorar o Interface a partir do Mempool.space



1. **A página inicial** dá-lhe uma visão geral da rede Bitcoin:




   - Blocos recentemente extraídos
   - Estimativas de custos para diferentes prioridades
   - O estado atual do Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Procurar uma transação**: Para seguir uma transação específica, cole o seu identificador (txid) na barra de pesquisa no topo da página.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analisar os detalhes da transação



Uma vez encontrada a sua transação, o Mempool.space apresenta-lhe uma análise completa:



1. **Informações essenciais** :




   - Estado (confirmado ou não)
   - Despesas pagas (em Sats/vB)
   - Tempo estimado de confirmação



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Estrutura de transação** :




   - Representação visual de entradas e saídas
   - Lista pormenorizada dos endereços envolvidos
   - Montantes transferidos



3. **Dados técnicos** :




   - Peso da transação
   - Tamanho virtual
   - Formato e versão utilizados
   - Outros metadados específicos



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Vantagens da utilização do Mempool.space na Umbrel



1. **Confidencialidade**: Os seus pedidos passam pelo seu próprio nó


2. **Independência**: Não é necessário depender de um serviço de terceiros


3. **Fiabilidade**: Acesso aos dados mesmo quando os navegadores públicos estão em baixo



Com esta aplicação, pode monitorizar eficazmente as suas transacções, compreender como as taxas afectam a velocidade de confirmação e obter uma melhor compreensão do funcionamento da rede Bitcoin.



## Ligação de um Wallet Bitcoin ao seu nó



### Configuração dos eléctricos



**Ligação local**



![Connexion locale](assets/fr/18.webp)




- Para utilização na sua rede local
- Mais rápido e mais fácil de configurar



**Ligação remota via Tor**



![Connexion Tor](assets/fr/19.webp)




- Para aceder ao seu nó a partir de qualquer lugar
- Mais seguro e privado



### Ligação com o Sparrow Wallet



**Acesso aos parâmetros**



![Paramètres Sparrow](assets/fr/20.webp)




- Pardal aberto Wallet
- Ir para Preferências > Servidor
- Clique em "Modificar ligação existente"



**Escolha do tipo de ligação**



O Sparrow oferece três modos de ligação:



***Servidor público***




- Ligação a servidores públicos (por exemplo, blockstream.info, Mempool.space)
- Simples mas menos privado



***Bitcoin Core***




- Ligação direta a um nó Bitcoin
- Privado mas mais lento



***Electrum privado***




- Ligar ao seu servidor Electrs
- Combina confidencialidade e desempenho



**Configuração dos eleitores**



Escolha o seu tipo de ligação utilizando as informações apresentadas na aplicação Electrs que vimos anteriormente:



Em ambos os casos, deixe as opções "Utilizar SSL" e "Utilizar proxy" desmarcadas.



**Ligação local**


Anfitrião: umbrel.local


Número do porto: 50001



**Ligação remota (Tor)**


Anfitrião : [your-Address-onion]


Número do porto: 50001



A ligação Tor é necessária se quiser aceder ao seu nó fora da sua rede local.



![Configuration connexion](assets/fr/21.webp)


Para mais informações sobre o software Sparrow Wallet, dispomos de um tutorial completo:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Conclusão



O seu Umbrel está agora pronto a ser utilizado. Participa ativamente na rede Bitcoin enquanto mantém o controlo total dos seus dados. Sinta-se à vontade para explorar as muitas outras aplicações disponíveis na Umbrel App Store para alargar as capacidades do seu servidor doméstico.



## Recursos úteis



### Documentação oficial




- [Sítio Web oficial da Umbrel](https://umbrel.com)
- [Documentação da Umbrel](https://github.com/getumbrel/umbrel/wiki)
- [Guarda-chuva da App Store] (https://apps.umbrel.com)



### Aplicações Bitcoin




- [Núcleo Bitcoin](https://Bitcoin.org/fr/)
- [Electros](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### Comunidade




- [Guarda-chuva do Fórum](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)