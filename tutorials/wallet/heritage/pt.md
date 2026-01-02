---
name: Heritage
description: Uma carteira Bitcoin com mecanismo de herança integrado através de scripts Taproot
---

![cover](assets/cover.webp)



A transmissão de bitcoins em caso de morte ou incapacidade representa um grande desafio para qualquer detentor de criptoactivos. Sem um plano de herança adequado, estes activos tornam-se irrecuperáveis para os seus entes queridos.



A Heritage fornece uma resposta elegante ao implementar um mecanismo de comutação de homem morto diretamente na blockchain Bitcoin. Este wallet de código aberto permite configurar as condições de sucessão do on-chain: se o proprietário não fizer mais transacções durante um período definido, chaves alternativas pré-designadas podem libertar os fundos.



## O que é o Património?



Heritage é uma carteira Bitcoin que integra nativamente um mecanismo de herança através de scripts Taproot. Desenvolvido sob licença MIT por Jérémie Rodon, este software de código aberto garante transparência e durabilidade.



O património utiliza scripts Taproot codificados em endereços Bitcoin. Cada UTXO integra dois tipos de condições de despesa:





- Caminho primário** : O proprietário pode gastar os seus bitcoins em qualquer altura com a sua chave primária
- Caminhos alternativos**: Para cada herdeiro designado, um script combina a sua chave pública com um bloqueio de tempo



Cada transação do proprietário adia automaticamente a data de ativação das cláusulas sucessórias. Em caso de inatividade prolongada (morte, incapacidade), as condições são automaticamente activadas.



## Serviço do património (opcional)



O património oferece duas opções de utilização:



**Faça você mesmo (gratuito)**: Apenas a aplicação de código aberto. O utilizador gere tudo de forma autónoma com o seu próprio nó. Esta opção oferece acesso a cópias de segurança incorporadas, herança incorporada e controlo exclusivo dos seus bitcoins. No entanto, é necessário criar os seus próprios alertas (calendário, lembretes) para não se esquecer de renovar os seus timelocks, e não existem notificações automáticas para os seus herdeiros.



**Utilizar o serviço (0,05% por ano)** : O serviço btc-heritage.com acrescenta funcionalidades para simplificar a gestão:




- Lembretes automáticos antes do fim dos prazos
- Notificações automáticas aos herdeiros para os orientar no processo de recuperação
- Apoio prioritário
- Gestão simplificada de descritores



Taxa: 0,05% do montante gerido por ano, mínimo de 0,5 mBTC/ano. Primeiro ano gratuito.



O serviço permanece sem custódia: as suas chaves privadas nunca saem do seu dispositivo. A Heritage não pode aceder aos seus fundos.



## Património CLI



Para os utilizadores avançados que preferem o terminal, a Heritage oferece uma ferramenta de linha de comando (CLI) para o controlo granular e o funcionamento da máquina com ar comprimido.



![Page Heritage CLI](assets/fr/03.webp)



A documentação completa do CLI está disponível em [btc-heritage.com/heritage-cli] (https://btc-heritage.com/heritage-cli). Aqui encontrará instruções para descarregar, ligar ao serviço, criar carteiras (com Ledger ou chaves locais), gerir herdeiros e transacções.



Este tutorial centra-se na aplicação Desktop, que é mais acessível à maioria dos utilizadores.



## Ambiente de trabalho do património



O Heritage Desktop é uma aplicação gráfica com uma interface intuitiva que guia o utilizador em todas as etapas do processo de configuração.



### Descarregar



Aceda a [btc-heritage.com] (https://btc-heritage.com) e clique em "Download application".



![Page d'accueil Heritage](assets/fr/01.webp)



Escolha a versão correspondente ao seu sistema operativo (Linux 64bits ou Windows 64bits). Os binários não são assinados digitalmente, o que pode acionar avisos de segurança.



![Page de téléchargement](assets/fr/02.webp)



### Instalação no Linux



No Linux, a aplicação é distribuída no formato AppImage. Antes de a poder executar, é necessário instalar a dependência `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Em seguida, torne o ficheiro executável e execute-o:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Primeiro lançamento



No primeiro lançamento, o assistente de integração oferece-lhe três opções:



![Onboarding initial](assets/fr/05.webp)





- Criar um Wallet Heritage**: Criar um novo wallet com plano de património
- Herdar bitcoins**: Recuperar bitcoins como herdeiro
- Explorar sozinho**: Explorar funções sem ajuda



Selecione "Setup an Heritage Wallet" para criar o seu primeiro wallet.



### Ligação de rede Bitcoin



Escolha a forma de ligação à rede Bitcoin:



![Choix connexion](assets/fr/06.webp)





- Utilizar o Serviço de Património**: Infraestrutura gerida, mais simples para os herdeiros
- Utilizar o meu próprio nó**: Ligar ao seu próprio nó Bitcoin Core ou Electrum



Para este tutorial, estamos a utilizar o nosso próprio nó.



### Gestão de chaves privadas



Selecione como gerir as suas chaves privadas:



![Gestion des clés](assets/fr/07.webp)





- Com um dispositivo de hardware Ledger** : Segurança máxima com o hardware wallet (recomendado)
- Armazenamento local com palavra-passe**: Chaves armazenadas localmente com proteção por palavra-passe
- Restaurar um wallet existente** : Restaurar a partir de um seed existente



### Configuração do nó



Se estiver a utilizar o seu próprio nó, a aplicação guia-o através da sua configuração. Certifique-se de que o seu nó Bitcoin ou Electrum é :




- Instalado e a funcionar
- Sincronizado com a rede Bitcoin
- Configurado para aceitar ligações RPC (para Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Clique em "My Bitcoin node is up and running" (O meu nó Bitcoin está a funcionar) quando o seu nó estiver pronto.



### Painel de estado



Clique em "Estado" no canto superior direito e depois em "Abrir configuração" para aceder aos parâmetros de ligação.



![Panneau Status](assets/fr/09.webp)



Defina a URL do seu servidor Electrum (por exemplo, `umbrel.local:50001` se estiver a utilizar o Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Criação do wallet



Uma vez estabelecida a ligação, clique em "Criar Wallet" no separador WALLETS.



![Créer wallet](assets/fr/11.webp)



Uma janela pop-up explica a arquitetura dividida do Heritage :



![Architecture split](assets/fr/12.webp)



1. **Provedor de chaves (offline)**: Gere as suas chaves privadas e assina as transacções. Pode ser um software Ledger ou wallet.


2. **Online Wallet**: Trata da sincronização com a rede Bitcoin, da criação de endereços e da difusão de transacções.



Preencher o formulário de criação :



![Formulaire création wallet](assets/fr/13.webp)





- Nome do Wallet**: Um nome único para identificar o seu wallet
- Fornecedor de chaves**: Escolha Armazenamento de chave local para este tutorial
- Novo/Restaurar**: Selecionar "New" (Novo) para criar um novo generate
- Contagem de palavras**: 24 palavras recomendadas para segurança máxima



Introduza uma palavra-passe forte e escolha as opções para Wallet online:



![Options Online Wallet](assets/fr/14.webp)





- Nó local**: Utiliza o seu próprio nó central Electrum ou Bitcoin
- Serviço Heritage**: Utiliza o serviço Heritage (recomendado para funções de notificação)



Clique em "Criar Wallet" para finalizar a criação.



### Interface a partir de wallet



O seu wallet está agora criado. A interface apresenta :



![Interface wallet](assets/fr/15.webp)





- Equilíbrio
- Botões SEND e RECEIVE
- Histórico de transacções
- História da configuração do património
- Endereços wallet



### Criação de herdeiros



Aceda ao separador "HERDEIROS" para criar os seus herdeiros.



![Page Heirs](assets/fr/16.webp)



O pop-up de informações explica:




- Os herdeiros são chaves públicas Bitcoin associadas a indivíduos
- Cada herdeiro tem a sua própria frase mnemónica
- O primeiro herdeiro deve ser um "Backup" para si próprio (em caso de perda do seu wallet principal)



#### Criação de um herdeiro de cópia de segurança



Clique em "Create Heir" (Criar herdeiro) e dê-lhe o nome "Backup" (Cópia de segurança).



![Création héritier Backup](assets/fr/17.webp)



A janela pop-up explica porque é que uma frase de 12 palavras sem passphrase é segura para os herdeiros:


1. **Não há acesso imediato**: As chaves de herdeiros não podem aceder aos fundos até que o bloqueio de tempo tenha expirado


2. **Deteção de comprometimento**: Se alguém aceder à frase, pode atualizar a configuração do Património


3. **Acessibilidade a longo prazo**: Um passphrase pode ser esquecido ao fim de muitos anos



Configurar o herdeiro :



![Configuration héritier](assets/fr/18.webp)





- Fornecedor de chaves** : Armazenamento local de chaves
- Novo**: Gerar um novo seed
- Contagem de palavras**: 12 palavras



Finalizar a criação :



![Finalisation héritier](assets/fr/19.webp)





- Tipo de herdeiro**: Chave pública alargada
- Exportar para o serviço**: Opcional, permite a notificação automática dos herdeiros



O herdeiro da cópia de segurança é agora criado:



![Héritier créé](assets/fr/20.webp)



#### Guardar a frase mnemónica do herdeiro



Clique no herdeiro da cópia de segurança e depois em "Show Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**IMPORTANTE: Tome nota destas 12 palavras e guarde-as num local seguro. Esta é a chave para recuperar os fundos.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Remover o seed da aplicação



Depois de ter escrito a frase, aceda aos parâmetros do herdeiro (ícone da roda dentada):



![Paramètres héritier](assets/fr/23.webp)



Utilize "Strip Heir Seed" para remover a chave privada da aplicação. Confirme que guardou a frase.



![Strip Heir Seed](assets/fr/24.webp)



Trata-se de uma medida de segurança: apenas a chave pública permanece na aplicação, suficiente para configurar a herança.



#### Criação de um segundo herdeiro



Repita o processo para criar um segundo herdeiro (por exemplo, "Satoshi"). Agora tem dois herdeiros:



![Deux héritiers](assets/fr/25.webp)





- Cópia de segurança**: A sua chave de emergência pessoal
- Satoshi**: Um herdeiro designado



### Configuração do património



Regresse ao seu wallet e clique no ícone Definições:



![Paramètres wallet](assets/fr/26.webp)



Na secção "Configuração do património", clique em "Criar":



![Heritage Configuration](assets/fr/27.webp)



Estabelecer limites de tempo para cada herdeiro:



![Configuration délais](assets/fr/28.webp)





- Backup**: 180 dias (6 meses) - Data de vencimento: 2026-06-18
- Satoshi**: 455 dias (15 meses) - Data de vencimento: 2027-03-20



**Importante**: Cada herdeiro deve ter um atraso maior do que o anterior. O primeiro herdeiro (Backup) terá acesso aos fundos primeiro.



Configurar também :



![Configuration finale](assets/fr/29.webp)





- Data de referência**: Data de início do cálculo dos prazos de entrega
- Prazo mínimo de vencimento**: Prazo mínimo após uma transação (recomenda-se 10 dias)



Clique em "Criar" para validar a configuração.



A configuração do Património está agora ativa:



![Configuration active](assets/fr/30.webp)



Apresenta ambos os herdeiros com os respectivos prazos e datas de expiração.



### Guardar descritores



**Importante**: Guarde os seus descritores wallet. Sem eles, mesmo com a frase mnemónica, a recuperação de fundos é impossível.



Clique em "Backup Descriptors" :



![Bouton Backup](assets/fr/31.webp)



Guarde o ficheiro JSON que contém os seus descritores Bitcoin:



![Backup descripteurs](assets/fr/32.webp)



Este ficheiro deve ser transmitido aos seus herdeiros, juntamente com as respectivas frases mnemónicas.



### Receber bitcoins



Clicar em "RECEBER" para generate um endereço de receção:



![Recevoir bitcoins](assets/fr/33.webp)



Parabéns! A sua Heritage Wallet está pronta para receber bitcoins. Cada endereço gerado incorpora automaticamente as suas condições Heritage.



Depois de receber uma transação, o seu saldo é atualizado:



![Solde mis à jour](assets/fr/34.webp)



O histórico apresenta a transação e a configuração do Património associada.



---

## Recuperação por um herdeiro



Decorrido o tempo estabelecido, o herdeiro pode reclamar os fundos.



### Pré-requisitos



O herdeiro precisa de :


1. A sua frase mnemónica de 12 palavras


2. O ficheiro original de cópia de segurança do descritor wallet (JSON)



### Criar um herdeiro Wallet



No separador "HERANÇAS", uma janela pop-up recorda-lhe estes pré-requisitos:



![Page Heir Wallets](assets/fr/35.webp)



**Atenção**: Sem o ficheiro de backup do descritor, o acesso aos fundos é IMPOSSÍVEL, mesmo com a frase mnemónica correta.



Clique em "Criar herdeiro Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Preencher o formulário:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Nome do herdeiro Wallet**: Um nome para identificar este herdeiro wallet
- Fornecedor de chaves** : Armazenamento local de chaves
- Restaurar**: Selecionar esta opção para introduzir uma frase existente



Introduzir as 12 palavras da frase mnemónica do herdeiro e configurar o Fornecedor de Herança:



![Entrée mnemonic](assets/fr/38.webp)





- Fornecedor de Património**: "Local" para utilizar o seu próprio nó com o ficheiro de cópia de segurança



Carregar o ficheiro de cópia de segurança JSON e clicar em "Create Heir Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Herdeiro Wallet



É criado o Heir Wallet. Inicialmente, se o bloqueio de tempo ainda não tiver expirado, não está disponível qualquer herança:



![Pas d'héritage disponible](assets/fr/40.webp)



Depois de decorrido o prazo e de os fundos terem sido sincronizados com a rede Bitcoin, aparecem na lista de heranças:



![Héritage disponible](assets/fr/41.webp)



A interface apresenta :




- Tipo de chave e impressão digital
- Total dos fundos hereditários
- Montante atual que pode ser gasto (0 sat se o bloqueio de tempo ainda não tiver expirado)
- Datas de vencimento e de expiração



Quando a data de vencimento é atingida, o botão "Spend" transfere os bitcoins para um wallet pessoal.



---

## Melhores práticas



### Guardar descritores



Os descritores wallet são essenciais para reconstruir os endereços do seu património. **Sem os descritores, mesmo com a sua frase mnemónica, não conseguirá encontrar os seus fundos.



### Segurança das chaves





- Utilizar uma Ledger para a chave principal, se possível
- Nunca guarde as sentenças dos herdeiros no mesmo sítio que as suas
- Divulgar informações em vários meios de comunicação e locais



### Documentação para os seus entes queridos



Escreva instruções claras que expliquem cada passo do processo de recuperação. Os seus herdeiros podem não estar familiarizados com o Bitcoin no momento crítico.



## Alternativas



Existem outras soluções para gerir a transmissão dos seus bitcoins, incluindo o Liana e o Bitcoin Keeper. Encontrará os nossos tutoriais abaixo:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Conclusão



O Heritage permite-lhe planear a sua sucessão do Bitcoin de uma forma soberana através da aplicação Desktop. A implementação requer uma consideração cuidadosa dos prazos adequados e da proteção dos segredos. Não se esqueça de transmitir aos seus herdeiros:




- A sua frase mnemónica de 12 palavras
- O ficheiro de cópia de segurança do descritor
- Instruções de recuperação



## Recursos





- [Sítio Web oficial do património](https://btc-heritage.com)
- [Documentação CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)