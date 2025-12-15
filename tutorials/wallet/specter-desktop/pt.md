---
name: Specter Desktop
description: Gerir as suas carteiras Bitcoin multi-assinaturas em total soberania com o seu próprio nó
---

![cover](assets/cover.webp)



O Specter Desktop é um aplicativo de código aberto (licença MIT) desenvolvido pela Cryptoadvance desde 2019 que facilita o gerenciamento de carteiras Bitcoin com suas carteiras de hardware (Ledger, Trezor, Coldcard, BitBox02, Passport, etc.) e sua própria infraestrutura Bitcoin (nó Bitcoin Core ou servidor Electrum). A aplicação destaca-se particularmente em configurações multi-assinatura, permitindo-lhe proteger grandes somas distribuindo o poder de assinatura entre várias carteiras de hardware independentes.



**Neste tutorial, irá aprender a:**




- Instalar e configurar o Specter Desktop no seu computador (Windows, macOS ou Linux)
- Ligar o Specter a um servidor Electrum (neste exemplo, utilizaremos o Umbrel)
- Criar um wallet simples com hardware wallet (Coldcard)
- Receber e enviar bitcoins com total soberania
- Configurar um wallet de assinatura múltipla 2 em 3 com várias carteiras de hardware
- Instalar o Specter num servidor Umbrel (bónus avançado)



Todas as suas transacções serão validadas localmente através da sua própria infraestrutura, sem transmitir qualquer informação a servidores externos, garantindo a sua confidencialidade e soberania financeira. Verifique sempre as transacções no ecrã do seu hardware wallet antes de assinar.



## Descarregamento e instalação



Visite o sítio Web oficial do Specter Desktop para transferir a aplicação.



![Page d'accueil Specter](assets/fr/01.webp)



Na página de transferência, escolha a versão correspondente ao seu sistema operativo: macOS, Windows ou Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Uma vez descarregada, instale a aplicação de acordo com as instruções habituais do seu sistema operativo. Para o macOS, arraste o ícone para Aplicações. No Windows, execute o instalador. Para Linux, siga as instruções do pacote.



## Configuração inicial



Na primeira inicialização, o Specter Desktop pede-lhe para escolher o tipo de ligação. É possível conectar-se a um servidor Electrum ou ao seu próprio nó Bitcoin Core.



![Choix du type de connexion](assets/fr/03.webp)



Neste exemplo, usaremos uma conexão com um servidor Electrum em execução na Umbrel.



Para mais informações, consulte o nosso tutorial Umbrel:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Esta opção oferece uma sincronização mais rápida do que o Bitcoin Core. Se preferir, pode selecionar "Bitcoin Core" e configurar a ligação ao seu nó local. Os passos seguintes permanecem os mesmos, independentemente da sua escolha.



Selecione "Ligação Electrum" e escolha "Introduzir o meu próprio" para configurar o seu próprio servidor Electrum.



![Configuration Electrum](assets/fr/04.webp)



Digite o endereço do seu servidor Electrum. No nosso caso com a Umbrel, o endereço será `umbrel.local` com a porta `50001`. Clique em "Connect" para estabelecer a ligação.



Uma vez ligado, aparece o ecrã de boas-vindas, com uma lista de verificação para começar. Agora é necessário adicionar as suas carteiras de hardware.



![Écran d'accueil](assets/fr/05.webp)



## Adição de hardware wallet



No menu do lado esquerdo, clique em "Adicionar dispositivo" para adicionar o hardware do wallet.



O Specter Desktop suporta várias carteiras de hardware: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault e muitas outras.



Se quiser saber mais, consulte os nossos tutoriais sobre hardware wallet.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Selecione o hardware do wallet. Neste exemplo, estamos a usar um Coldcard MK4.



Abaixo encontra o nosso tutorial para este hardware wallet:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Para um Coldcard, é necessário exportar as chaves públicas do hardware wallet através de uma ligação USB ou de um cartão microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Siga as instruções apresentadas para exportar as chaves do seu Coldcard. Dê um nome ao seu hardware wallet (aqui "MK4 Tuto"). Uma vez importadas as chaves, pode criar um wallet com uma única chave, ou adicionar outras carteiras de hardware para um wallet multi-assinaturas.



![Dispositif ajouté](assets/fr/08.webp)



## Criação de portefólio



Depois de adicionar o seu hardware wallet, clique em "Criar chave única wallet" para criar um wallet de assinatura única.



Dê um nome à sua carteira (por exemplo, "Wallet para tuto") e selecione o tipo de endereço. Selecione "Segwit" para utilizar endereços bech32 nativos que optimizam os custos de transação.



![Configuration du portefeuille](assets/fr/09.webp)



Após a criação do seu portefólio, o Specter oferece-se para guardar um ficheiro PDF de cópia de segurança que contém todas as informações públicas necessárias para restaurar o seu portefólio (descritores, chaves públicas alargadas). Este ficheiro não contém as suas chaves privadas.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Receber bitcoins



Para receber bitcoins, selecione o seu wallet no menu do lado esquerdo e, em seguida, clique no separador "Receber".



O Specter gera automaticamente um novo endereço de receção com um código QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



Pode copiar o endereço ou digitalizar o código QR. Verifique sempre o endereço no ecrã do hardware do wallet antes de o transmitir a alguém.



## Ver histórico e endereços



Depois de receber bitcoins, pode ver as suas transacções no separador "Transacções".



![Historique des transactions](assets/fr/12.webp)



O separador "Endereços" permite-lhe visualizar todos os endereços gerados pela sua carteira, com o respetivo estado de utilização e montantes associados.



![Liste des adresses](assets/fr/13.webp)



## Enviar bitcoins



Para enviar bitcoins, clique no separador "Enviar". Introduza o endereço do destinatário, o montante a enviar e assinale as opções avançadas se pretender selecionar manualmente os UTXOs (controlo de moedas).



![Création d'une transaction](assets/fr/14.webp)



Clique em "Criar transação não assinada" para criar a transação. O Specter pedir-lhe-á então para assinar a transação com o seu hardware wallet.



![Signature de la transaction](assets/fr/15.webp)



Se estiver a utilizar um Coldcard, pode optar por assinar via USB ou utilizar o cartão microSD (air-gapped). Confirme a transação no ecrã do seu hardware wallet, verificando cuidadosamente o endereço de destino e o montante.



Depois de a transação ter sido assinada, pode transmiti-la na rede Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Clique em "Enviar transação" para enviar a transação. O Specter confirmará que a transação foi enviada e pode acompanhar o seu estado no separador Transacções.



![Diffusion de la transaction](assets/fr/17.webp)



## Criar e utilizar uma carteira com várias assinaturas



Um dos principais recursos do Specter Desktop é sua capacidade de simplificar o gerenciamento de carteiras com várias assinaturas. Um wallet multisig exige várias assinaturas para autorizar uma transação, eliminando assim o ponto único de falha. Uma configuração 2 em 3, por exemplo, requer duas assinaturas de três carteiras de hardware separadas para validar qualquer despesa.



Para criar um wallet multisig, comece por adicionar todas as carteiras de hardware de assinatura através de "Add device" (Adicionar dispositivo). Neste exemplo, vamos utilizar três carteiras de hardware diferentes: um Coldcard MK4 (já adicionado anteriormente), um Passport e um Ledger. Esta diversificação de fabricantes reforça a segurança, evitando a dependência de uma única cadeia de fornecimento ou firmware.



Aqui estão as ligações para os tutoriais do Ledger e do Passport:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Adicione o Passport atribuindo um nome ao hardware wallet (por exemplo, "Passport multi") e importando as suas chaves através do cartão microSD ou do código QR. Em seguida, clique em "Continuar" para prosseguir.



![Ajout du Passport](assets/fr/23.webp)



Em seguida, adicione o Ledger ligando-o via USB e abrindo a aplicação Bitcoin no hardware wallet. Dê-lhe um nome (por exemplo, "ledger multi") e clique em "Get via USB" e depois em "Continue" para importar as suas chaves públicas.



![Ajout du Ledger](assets/fr/24.webp)



Depois de ter registado as suas três carteiras de hardware no Specter, clique em "Add wallet" (Adicionar wallet) e selecione a opção "Multiple Signature" (Assinatura múltipla) para criar um wallet com várias assinaturas.



![Choix du type de wallet](assets/fr/25.webp)



Selecione as três carteiras de hardware que pretende incluir no seu quorum de assinaturas múltiplas: MK4 Tuto, Passport multi e ledger multi. Clique em "Continuar" para avançar para o passo seguinte.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Escolha a sua configuração multi-assinatura. Selecione "Segwit" como tipo de endereço para beneficiar de taxas optimizadas. O parâmetro "Required Signatures to Authorize Transactions (m of 3)" permite-lhe definir o limiar: para uma configuração 2-on-3, são necessárias 2 assinaturas. Cada hardware wallet apresenta a sua chave multisig correspondente. Clicar em "Criar wallet" para finalizar a criação.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Seu portfólio com várias assinaturas "Multi tuto" foi criado. A Specter recomenda imediatamente que você salve o arquivo PDF de backup que contém o descritor do portfólio. Clique em "Salvar PDF de backup" para fazer o download desse arquivo essencial.



![Wallet multisig créé](assets/fr/28.webp)



O Specter também permite exportar informações wallet para cada uma das suas carteiras de hardware através de código QR ou ficheiro. Isto permite que certas carteiras de hardware (como a Coldcard ou a Passport) armazenem a configuração multisig diretamente na sua memória.



Para o Passport, desbloqueie o dispositivo e vá para "Gerir conta" > "Ligar Wallet" > "Specter" > "Multisig" > "Código QR" e, em seguida, digitalize o código QR gerado pelo Specter. O Passport pedir-lhe-á então que digitalize um endereço de receção do seu wallet para validar a configuração multisig.



Para o MK4, ligue-o ao seu PC e desbloqueie-o. Em seguida, clique em "Save MK4 Tuto file" e guarde o ficheiro no seu MK4. Na próxima vez que assinar o seu hardware wallet, o MK4 utilizará este ficheiro para terminar a configuração do multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Para sua informação, pode aceder às cópias de segurança a qualquer momento a partir do separador "Definições" da sua carteira e, em seguida, "Exportar":



![Accès au backup PDF](assets/fr/30.webp)



A utilização quotidiana é semelhante à de um simples wallet: recebe endereços generate normalmente. Para enviar bitcoins, vá ao separador "Enviar", introduza o endereço do destinatário e o montante, depois clique em "Criar transação não assinada".



![Création d'une transaction multisig](assets/fr/31.webp)



O Spectre constrói um PSBT (Partially Signed Bitcoin Transaction) e mostra "Acquired 0 of 2 signatures". Agora tem de assinar com pelo menos duas das suas três carteiras de hardware. Clica no primeiro hardware wallet (por exemplo, "MK4 Tuto") para assinar com o teu Coldcard e depois no segundo (por exemplo, "Passport multi") para obteres a segunda assinatura necessária.



![Signature de la transaction](assets/fr/32.webp)



Depois de obter as duas assinaturas necessárias (a interface apresenta "Acquired 2 of 2 signatures" e "Transaction is ready to send"), clique em "Send Transaction" para transmitir a transação na rede Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Esta abordagem multi-assinatura é particularmente adequada para empresas (vários gestores têm de aprovar as despesas), famílias (proteção de uma herança multigeracional) ou indivíduos que gerem grandes somas (distribuição geográfica de carteiras de hardware para resistir a catástrofes localizadas).



### A importância crítica das cópias de segurança com várias assinaturas



**Nota**: a cópia de segurança de uma carteira multisig é fundamentalmente diferente da cópia de segurança de uma única carteira. As suas frases de recuperação (frases seed) por si só não são suficientes para restaurar uma carteira multisig. Também é necessário fazer o backup do **output descriptor** (output descriptor), que contém as informações de configuração da sua carteira multisig.



O output descriptor inclui dados essenciais: as chaves públicas alargadas (xpubs) de cada cossignatário, o limiar de assinatura (2 em 3 no nosso exemplo), o tipo de script utilizado (Segwit nativo, aninhado ou legado) e os caminhos de desvio para cada hardware wallet. Sem este descritor, mesmo que tenha duas das suas três frases de recuperação, não será capaz de reconstruir o seu wallet ou aceder aos seus bitcoins. O descritor permite que o seu software saiba como combinar as chaves públicas para os endereços generate e Bitcoin correspondentes aos seus fundos.



O Specter Desktop gera automaticamente um arquivo PDF de backup quando você cria seu portfólio multisig. Este PDF contém o descritor completo, as impressões digitais de cada hardware wallet e todas as informações públicas necessárias para a restauração. **Este ficheiro não contém as suas chaves privadas** e, por conseguinte, não lhe permite, por si só, gastar os seus bitcoins, mas permite que qualquer pessoa que lhe aceda veja o seu histórico completo de transacções e o seu saldo.



Para fazer uma cópia de segurança correta da sua configuração de várias assinaturas, siga este procedimento: depois de criar a sua carteira, clique no separador "Definições", depois em "Exportar" e selecione "Guardar PDF de cópia de segurança". Crie várias cópias deste PDF: imprima pelo menos duas cópias em papel e guarde também uma cópia digital encriptada. Guarde uma cópia do PDF com cada uma das suas frases de recuperação, em locais geograficamente separados.



Grave as suas frases de recuperação em placas de metal à prova de fogo e de água para garantir a sua longevidade. Nunca subestime a importância destas cópias de segurança: se perder a pasta `~/.specter` no seu computador E perder uma das suas carteiras de hardware sem uma cópia de segurança do descritor, todos os seus fundos serão irremediavelmente perdidos, mesmo com uma configuração 2 em 3. A redundância multi-assinatura protege contra a perda do hardware do wallet, mas apenas se tiver feito o backup correto do descritor do seu wallet.



## Vantagens e limitações do Specter Desktop



**Vantagens**: Confidencialidade óptima com validação local completa sem servidores de terceiros. Flexibilidade de várias assinaturas para configurações avançadas (empresarial, familiar, individual). Suporte alargado de hardware wallet com total interoperabilidade (USB e air-gapped).



**Limitações**: Curva de aprendizagem significativa sobre conceitos avançados do Bitcoin (UTXOs, descritores, caminhos de derivação).



## Melhores práticas



Verifique sempre os endereços e os montantes no ecrã do hardware wallet antes da validação, para se proteger contra o malware.



Mantenha as cópias de segurança de PDF separadas das suas sementes. Estes descritores públicos podem ser armazenados num cofre bancário ou numa nuvem encriptada, facilitando a recuperação sem expor as suas chaves privadas.



Teste a recuperação em montantes token antes de utilizar as suas carteiras com grandes fundos. Criar, testar, apagar e restaurar para validar os seus procedimentos.



Mantenha o Specter e seu firmware atualizados. Distribua seus co-signatários com várias assinaturas geograficamente (casa/escritório/próximo) para resistir a desastres localizados. Use etiquetas descritivas para facilitar a contabilidade e a declaração de impostos.



## Bónus: Instalação num servidor Bitcoin (Umbrel, RaspiBlitz, Start9)



Se já possui um servidor Bitcoin como o Umbrel, RaspiBlitz, MyNode ou Start9, pode instalar o Specter Desktop diretamente a partir da sua loja de aplicações. Esta abordagem oferece várias vantagens significativas: a aplicação configura-se automaticamente com o seu nó Bitcoin Core local, permanece acessível 24 horas por dia, 7 dias por semana, através de uma interface Web a partir de qualquer dispositivo na sua rede, e pode mesmo aceder-lhe remotamente de forma segura através do Tor. Toda a sua infraestrutura Bitcoin é centralizada num único servidor dedicado, simplificando a gestão e reforçando a sua soberania.



### Instalação a partir da Umbrel App Store



A partir da interface Umbrel, aceda à App Store e procure o Specter Desktop. Clique em "Instalar" para iniciar a instalação.



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



O Specter Desktop democratiza as configurações avançadas do Bitcoin, tornando as assinaturas múltiplas acessíveis sem sacrificar a sua soberania ou confidencialidade. Para os utilizadores que gerem quantias significativas de dinheiro, transforma as práticas institucionais em soluções que podem ser implementadas por particulares.



Embora a aplicação exija um investimento inicial em infraestrutura e aprendizagem, oferece uma soberania completa: controlo da infraestrutura de validação, propriedade física das chaves e transacções livres de vigilância por parte de terceiros. Quer seja um indivíduo a proteger as suas poupanças, uma família a criar um cofre multi-geracional ou uma empresa a gerir o fluxo de caixa, o Specter Desktop é a ferramenta de referência para conciliar segurança máxima e soberania absoluta.



## Recursos



### Documentação oficial




- [Sítio Web oficial do Specter Desktop](https://specter.solutions/desktop/)
- [Código-fonte do GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Documentação completa](https://docs.specter.solutions/)



### Comunidade e apoio




- [Grupo comunitário do Telegrama Specter] (https://t.me/spectersupport)
- [Fórum de discussão do Reddit](https://reddit.com/r/specterdesktop/)
- [Relatórios de erros do GitHub](https://github.com/cryptoadvance/specter-desktop/issues)