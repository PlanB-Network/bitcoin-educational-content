---
name: Ambiente de trabalho Specter
description: Gerir as suas carteiras Bitcoin multi-assinaturas em total soberania com o seu próprio nó
---

![cover](assets/cover.webp)



O Specter Desktop é um aplicativo de código aberto (licença MIT) desenvolvido pela Cryptoadvance desde 2019 que facilita o gerenciamento de carteiras Bitcoin com suas carteiras de hardware (Ledger, Trezor, Coldcard, BitBox02, Passport, etc.) e sua própria infraestrutura Bitcoin (nó Bitcoin core ou Electrum Server). A aplicação destaca-se particularmente nas configurações multi-assinatura, permitindo-lhe proteger grandes somas distribuindo o poder de assinatura entre várias carteiras de hardware independentes.



**Neste tutorial, irá aprender a:**




- Instalar e configurar o Specter Desktop no seu computador (Windows, macOS ou Linux)
- Ligar o Specter a um Electrum Server (neste exemplo, utilizaremos o Umbrel)
- Criar um Wallet simples com um Hardware Wallet (Coldcard)
- Receber e enviar bitcoins com total soberania
- Configuração de um Wallet de assinatura múltipla 2 em 3 com várias carteiras de hardware
- Instalar o Specter num servidor Umbrel (bónus avançado)



Todas as suas transacções serão validadas localmente através da sua própria infraestrutura, sem transmitir qualquer informação a servidores externos, garantindo a sua confidencialidade e soberania financeira. Verifique sempre as transacções no seu ecrã Hardware Wallet antes de assinar.



## Descarregamento e instalação



Visite o sítio Web oficial do Specter Desktop para transferir a aplicação.



![Page d'accueil Specter](assets/fr/01.webp)



Na página de transferência, escolha a versão correspondente ao seu sistema operativo: macOS, Windows ou Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Uma vez descarregada, instale a aplicação de acordo com as instruções habituais do seu sistema operativo. Para o macOS, arraste o ícone para Aplicações. No Windows, execute o instalador. Para Linux, siga as instruções do pacote.



## Configuração inicial



Na primeira inicialização, o Specter Desktop pede para escolher o tipo de conexão. Pode ligar-se a um nó Electrum Server ou ao seu próprio nó Bitcoin core.



![Choix du type de connexion](assets/fr/03.webp)



Neste exemplo, usaremos uma conexão com um Electrum Server em execução no Umbrel.



Para mais informações, consulte o nosso tutorial Umbrel:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Esta opção oferece uma sincronização mais rápida do que o Bitcoin core. Se preferir, pode selecionar "Bitcoin core" e configurar a ligação ao seu nó local. Os passos seguintes são os mesmos, independentemente da sua escolha.



Selecione "Ligação Electrum" e depois escolha "Introduzir o meu próprio" para configurar o seu próprio Electrum Server.



![Configuration Electrum](assets/fr/04.webp)



Digite o Address do seu Electrum Server. No nosso caso com a Umbrel, o Address será `umbrel.local` com a porta `50001`. Clique em "Connect" para estabelecer a ligação.



Uma vez ligado, aparece o ecrã de boas-vindas, com uma lista de verificação para começar. Agora é necessário adicionar as suas carteiras de hardware.



![Écran d'accueil](assets/fr/05.webp)



## Adicionar um Hardware Wallet



No menu do lado esquerdo, clique em "Adicionar dispositivo" para adicionar o seu Hardware Wallet.



O Specter Desktop suporta várias carteiras de hardware: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault e muitas outras.



Se quiser saber mais, consulte os nossos tutoriais sobre o Hardware Wallet.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Selecione o seu Hardware Wallet. Neste exemplo, estamos a utilizar um Coldcard MK4.



Veja abaixo o nosso tutorial para este Hardware Wallet :



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Para um Coldcard, é necessário exportar as chaves públicas do Hardware Wallet através de uma ligação USB ou de um cartão microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Siga as instruções apresentadas para exportar as chaves do seu Coldcard. Dê um nome ao seu Hardware Wallet (aqui "MK4 Tuto"). Uma vez importadas as chaves, pode criar um Wallet com uma única chave, ou adicionar outras carteiras de hardware para um Wallet multi-assinaturas.



![Dispositif ajouté](assets/fr/08.webp)



## Criação de portefólio



Depois de adicionar o seu Hardware Wallet, clique em "Criar chave única Wallet" para criar um Wallet de assinatura única.



Dê um nome à sua carteira (por exemplo, "Wallet para tuto") e selecione o tipo Address. Selecione "SegWit" para utilizar endereços BECH32 nativos, que optimizam os custos de transação.



![Configuration du portefeuille](assets/fr/09.webp)



Após a criação do seu portefólio, o Specter oferece-se para guardar um ficheiro PDF de cópia de segurança que contém todas as informações públicas necessárias para restaurar o seu portefólio (descritores, chaves públicas alargadas). Este ficheiro não contém as suas chaves privadas.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Receber bitcoins



Para receber bitcoins, selecione o seu Wallet no menu do lado esquerdo e clique no separador "Receber".



O Specter gera automaticamente uma nova receção Address com um código QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



Pode copiar o Address ou digitalizar o código QR. Verifique sempre o Address no ecrã do seu Hardware Wallet antes de o passar a alguém.



## Ver histórico e endereços



Depois de receber bitcoins, pode ver as suas transacções no separador "Transacções".



![Historique des transactions](assets/fr/12.webp)



O separador "Endereços" permite-lhe visualizar todos os endereços gerados pela sua carteira, com o respetivo estado de utilização e montantes associados.



![Liste des adresses](assets/fr/13.webp)



## Enviar bitcoins



Para enviar bitcoins, clique no separador "Enviar". Introduza o Address do destinatário, o montante a enviar e assinale as opções avançadas se pretender selecionar manualmente os UTXOs (controlo Coin).



![Création d'une transaction](assets/fr/14.webp)



Clique em "Criar transação não assinada" para criar a transação. O Specter pedirá então que assine a transação com o seu Hardware Wallet.



![Signature de la transaction](assets/fr/15.webp)



Se estiver a utilizar um Coldcard, pode optar por assinar via USB ou utilizar o cartão microSD (air-gapped). Confirme a transação no ecrã do seu Hardware Wallet, verificando cuidadosamente o Address de destino e o montante.



Uma vez que a transação tenha sido assinada, pode transmiti-la na rede Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Clique em "Enviar transação" para enviar a transação. O Specter confirmará que a transação foi enviada e pode acompanhar o seu estado no separador Transacções.



![Diffusion de la transaction](assets/fr/17.webp)



## Criar e utilizar uma carteira com várias assinaturas



Um dos principais recursos do Specter Desktop é sua capacidade de simplificar o gerenciamento de carteiras com várias assinaturas. Um Multisig Wallet requer várias assinaturas para autorizar uma transação, eliminando o ponto único de falha. Uma configuração 2 em 3, por exemplo, requer duas assinaturas de três carteiras de hardware separadas para validar qualquer despesa.



Para criar um Multisig Wallet, comece por adicionar todas as carteiras de hardware signatárias através de "Add device" (Adicionar dispositivo). Neste exemplo, utilizaremos três carteiras de hardware diferentes: um Coldcard MK4 (já adicionado anteriormente), um Passport e um Ledger. Esta diversificação de fabricantes reforça a segurança, evitando a dependência de uma única cadeia ou firmware Supply.



Aqui estão as ligações para os tutoriais Ledger e Passport:



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Adicione o Passport dando um nome ao Hardware Wallet (por exemplo, "Passport multi") e importando as suas chaves através do cartão microSD ou do código QR. Em seguida, clique em "Continuar" para prosseguir.



![Ajout du Passport](assets/fr/23.webp)



Em seguida, adicione o Ledger ligando-o através de USB e abrindo a aplicação Bitcoin no Hardware Wallet. Dê-lhe um nome (por exemplo, "Ledger multi") e clique em "Get via USB" e depois em "Continue" para importar as suas chaves públicas.



![Ajout du Ledger](assets/fr/24.webp)



Depois de ter registado as suas três carteiras de hardware no Specter, clique em "Add Wallet" (Adicionar Wallet) e selecione a opção "Multiple Signature" (Assinatura múltipla) para criar um Wallet com várias assinaturas.



![Choix du type de wallet](assets/fr/25.webp)



Selecione as três carteiras de hardware que pretende incluir no seu quorum de assinaturas múltiplas: MK4 Tuto, Passport multi e Ledger multi. Clique em "Continuar" para avançar para o passo seguinte.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Escolha a sua configuração multi-assinatura. Selecione "SegWit" como tipo de Address para beneficiar de taxas optimizadas. O parâmetro "Assinaturas necessárias para autorizar as transacções (m de 3)" permite definir o limiar: para uma configuração 2 em 3, são necessárias 2 assinaturas. Cada Hardware Wallet apresenta a chave Multisig correspondente. Clicar em "Criar Wallet" para finalizar a criação.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



O seu portfólio com várias assinaturas "Multi tuto" está agora criado. A Specter recomenda imediatamente que você salve o arquivo PDF de backup que contém o portfólio Descriptor. Clique em "Salvar PDF de backup" para fazer o download desse arquivo essencial.



![Wallet multisig créé](assets/fr/28.webp)



O Specter também permite exportar informações do Wallet para cada uma das suas carteiras de hardware através de código QR ou ficheiro. Isto permite que certas carteiras de hardware (como a Coldcard ou a Passport) armazenem a configuração do Multisig diretamente na sua memória.



Para o Passport, desbloqueie o dispositivo e aceda a "Gerir conta" > "Ligar Wallet" > "Specter" > "Multisig" > "Código QR" e, em seguida, leia o código QR gerado pelo Specter. O Passport pedir-lhe-á então que digitalize um Address recetor do seu Wallet para validar a configuração do Multisig.



Para o MK4, ligue-o ao seu PC e desbloqueie-o. Em seguida, clique em "Guardar ficheiro MK4 Tuto" e guarde o ficheiro no seu MK4. Da próxima vez que assinar o seu Hardware Wallet, o MK4 utilizará este ficheiro para terminar a configuração do Multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Para sua informação, pode aceder às cópias de segurança a qualquer momento a partir do separador "Definições" da sua carteira e, em seguida, "Exportar":



![Accès au backup PDF](assets/fr/30.webp)



A utilização quotidiana continua a ser semelhante à de um simples Wallet: os endereços de receção generate são normais. Para enviar bitcoins, vá ao separador "Enviar", introduza o Address do destinatário e o montante, depois clique em "Criar transação não assinada".



![Création d'une transaction multisig](assets/fr/31.webp)



O Spectre constrói um PSBT (Partially Signed Bitcoin Transaction) e mostra "Acquired 0 of 2 signatures". Agora tens de assinar com pelo menos duas das tuas três carteiras de hardware. Clique no primeiro Hardware Wallet (por exemplo, "MK4 Tuto") para assinar com o seu Coldcard e, em seguida, no segundo (por exemplo, "Passport multi") para obter a segunda assinatura necessária.



![Signature de la transaction](assets/fr/32.webp)



Depois de obter as 2 assinaturas necessárias (o Interface apresenta "Acquired 2 of 2 signatures" e "Transaction is ready to send"), clique em "Send Transaction" para transmitir a transação na rede Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Esta abordagem multi-assinatura é particularmente adequada para empresas (vários gestores têm de aprovar as despesas), famílias (proteção de uma herança multigeracional) ou indivíduos que gerem grandes somas (distribuição geográfica de carteiras de hardware para resistir a catástrofes localizadas).



### A importância crítica das cópias de segurança com várias assinaturas



**Atenção**: a cópia de segurança de uma carteira com várias assinaturas é fundamentalmente diferente da cópia de segurança de uma carteira única. As suas frases de recuperação (frases seed) por si só não são suficientes para restaurar uma carteira Multisig. Também é necessário efetuar uma cópia de segurança do **output descriptor** (output descriptor), que contém as informações de configuração da sua carteira com várias assinaturas.



O output descriptor inclui dados essenciais: as chaves públicas estendidas (xpubs) de cada co-assinante, o limite de assinatura (2 em 3 no nosso exemplo), o tipo de script usado (SegWit nativo, aninhado ou legado) e os caminhos de derivação para cada Hardware Wallet. Sem este Descriptor, mesmo que tenha duas das suas três frases de recuperação, não será capaz de reconstruir o seu Wallet ou aceder aos seus bitcoins. O Descriptor permite que o seu software saiba como combinar as chaves públicas para generate os endereços Bitcoin correspondentes aos seus fundos.



O Specter Desktop gera automaticamente um arquivo PDF de backup quando você cria seu portfólio Multisig. Este PDF contém o Descriptor completo, as impressões digitais de cada Hardware Wallet e todas as informações públicas necessárias para a restauração. **Este ficheiro não contém as suas chaves privadas** e, por isso, não lhe permite gastar os seus bitcoins, mas permite que qualquer pessoa que o aceda veja o seu histórico completo de transacções e o seu saldo.



Para fazer uma cópia de segurança correta da sua configuração de várias assinaturas, siga este procedimento: depois de criar a sua carteira, clique no separador "Definições", depois em "Exportar" e selecione "Guardar PDF de cópia de segurança". Crie várias cópias deste PDF: imprima pelo menos duas cópias em papel e guarde também uma cópia digital encriptada. Guarde uma cópia do PDF com cada uma das suas frases de recuperação, em locais geograficamente separados.



Grave as suas frases de recuperação em placas de metal à prova de fogo e de água para garantir a sua longevidade. Nunca subestime a importância destas cópias de segurança: se perder a pasta `~/.specter` do seu computador E perder uma das suas carteiras de hardware sem uma cópia de segurança do Descriptor, todos os seus fundos serão irremediavelmente perdidos, mesmo com uma configuração 2 em 3. A redundância de múltiplas assinaturas protege contra a perda de uma Hardware Wallet, mas apenas se tiver feito corretamente o backup da Wallet da Descriptor.



## Vantagens e limitações do Specter Desktop



**Vantagens**: Confidencialidade óptima com validação local completa sem servidores de terceiros. Flexibilidade de várias assinaturas para configurações avançadas (empresarial, familiar, individual). Suporte alargado do Hardware Wallet com total interoperabilidade (USB e air-gapped).



**Limitações**: Curva de aprendizagem significativa sobre conceitos avançados do Bitcoin (UTXOs, descritores, caminhos de derivação).



## Melhores práticas



Verifique sempre os endereços e os montantes no ecrã do Hardware Wallet antes da validação, para se proteger contra o malware.



Mantenha as cópias de segurança de PDF separadas das suas sementes. Estes descritores públicos podem ser armazenados num cofre bancário ou numa nuvem encriptada, facilitando a recuperação sem expor as suas chaves privadas.



Teste a recuperação de montantes token antes de utilizar as suas carteiras com grandes fundos. Criar, testar, apagar e restaurar para validar os seus procedimentos.



Mantenha o Specter e seu firmware atualizados. Distribua seus co-signatários com várias assinaturas geograficamente (casa/escritório/próximo) para resistir a desastres localizados. Use etiquetas descritivas para facilitar a contabilidade e a declaração de impostos.



## Bónus: Instalação num servidor Bitcoin (Umbrel, RaspiBlitz, Start9)



Se já possui um servidor Bitcoin como o Umbrel, RaspiBlitz, MyNode ou Start9, pode instalar o Specter Desktop diretamente a partir da sua loja de aplicações. Esta abordagem oferece várias vantagens significativas: a aplicação configura-se automaticamente com o seu nó Bitcoin core local, permanece acessível 24 horas por dia, 7 dias por semana, através de uma web Interface a partir de qualquer dispositivo na sua rede, e pode mesmo aceder-lhe remotamente de forma segura através do Tor. Toda a sua infraestrutura Bitcoin é centralizada num único servidor dedicado, simplificando a gestão e reforçando a sua soberania.



### Instalação a partir da Umbrel App Store



A partir do seu Umbrel Interface, aceda à App Store e procure o Specter Desktop. Clique em "Install" (Instalar) para iniciar a instalação.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Quando a instalação estiver concluída, abra o Specter Desktop no seu Umbrel. O ecrã de boas-vindas pede-lhe para escolher o tipo de ligação. Se estiver a utilizar o Specter no Umbrel, clique em "Atualizar definições" para configurar a ligação.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Selecione "Ligação USB do Specter remoto" para permitir a utilização de carteiras de hardware USB ligadas ao seu computador local enquanto utiliza o Specter no servidor Umbrel remoto.



![Configuration Remote Specter USB](assets/fr/20.webp)



Siga as instruções apresentadas para configurar a ponte HWI. É necessário aceder às definições da ponte do dispositivo e adicionar o domínio `http://umbrel.local:25441` à lista branca. Clique em "Atualizar" para guardar a configuração.



![HWI Bridge Settings](assets/fr/21.webp)



Se também pretender utilizar as carteiras de hardware USB a partir do seu computador local, transfira a aplicação Specter Desktop para a sua máquina e defina-a como "Sim, executo o Specter remotamente". Clique em "Salvar" para finalizar a configuração.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Conclusão



O Specter Desktop democratiza as configurações avançadas do Bitcoin, tornando acessível a assinatura múltipla sem sacrificar a soberania ou a confidencialidade. Para os utilizadores que gerem quantias significativas de dinheiro, transforma as práticas institucionais em soluções que podem ser implementadas por particulares.



Embora a aplicação exija um investimento inicial em infraestrutura e aprendizagem, oferece uma soberania completa: controlo da infraestrutura de validação, Ownership físico das chaves e transacções livres de vigilância por parte de terceiros. Quer seja um indivíduo a proteger as suas poupanças, uma família a criar um cofre multi-geracional ou uma empresa a gerir o fluxo de caixa, o Specter Desktop é a ferramenta de referência para conciliar segurança máxima e soberania absoluta.



## Recursos



### Documentação oficial




- [Sítio Web oficial do Specter Desktop](https://specter.solutions/desktop/)
- [Código-fonte do GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Documentação completa](https://docs.specter.solutions/)



### Comunidade e apoio




- [Grupo comunitário do Telegrama Specter] (https://t.me/spectersupport)
- [Fórum de discussão do Reddit](https://reddit.com/r/specterdesktop/)
- [Relatórios de erros do GitHub](https://github.com/cryptoadvance/specter-desktop/issues)