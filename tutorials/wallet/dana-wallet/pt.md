---
name: Dana Wallet
description: Carteira minimalista para pagamentos silenciosos (BIP-352)
---

![cover](assets/cover.webp)



A reutilização de endereços Bitcoin é uma das ameaças mais diretas à confidencialidade do utilizador. Quando um destinatário partilha um único endereço para receber vários pagamentos, qualquer observador pode rastrear todas as transacções associadas e reconstruir o seu historial financeiro. Este problema afecta particularmente os criadores de conteúdos, as instituições de caridade ou os activistas que pretendem apresentar publicamente um endereço de donativo sem comprometer a sua privacidade ou a dos seus doadores.



A Dana Wallet responde a este problema com uma solução elegante: Silent Payments. Este wallet minimalista e de código aberto, lançado em 2024, gera um endereço estático reutilizável, garantindo que cada pagamento recebido acabe num endereço separado na cadeia de blocos. O remetente não precisa de interação prévia com o destinatário, e nenhum observador externo pode ligar transacções individuais entre si. Na cadeia de blocos, estes pagamentos parecem transacções Taproot perfeitamente normais.



A Dana Wallet está disponível na Mainnet e na Signet, mas os criadores ainda a consideram experimental e recomendam que não deposite fundos que não esteja preparado para perder. Neste tutorial, vamos utilizar a versão Signet para descobrir o Silent Payments sem arriscar quaisquer fundos reais.



## O que é a Dana Wallet?



### Filosofia e objectivos



Dana Wallet adopta uma abordagem "SP-first": o wallet gera exclusivamente endereços Silent Payments e aceita apenas este tipo de pagamento. Não será possível criar um endereço Bitcoin clássico (legacy, SegWit ou Taproot standard) com esta aplicação. Esta restrição deliberada permite-lhe concentrar-se totalmente na aprendizagem do protocolo BIP-352 sem se distrair com outras funcionalidades. A interface organizada favorece deliberadamente a facilidade de utilização em detrimento de uma profusão de opções, tornando a ferramenta acessível mesmo para utilizadores novos nos conceitos de confidencialidade on-chain.



O projeto é inteiramente de código aberto, desenvolvido com Flutter para a interface móvel e Rust para a lógica criptográfica interna. Esta arquitetura combina uma experiência de utilizador fluida com um desempenho ótimo para operações de digitalização intensivas.



### Como funcionam os pagamentos silenciosos?



Os pagamentos silenciosos (BIP-352) baseiam-se num mecanismo criptográfico sofisticado que utiliza a chave Elliptic Curve Diffie-Hellman Exchange (ECDH). O destinatário gera um endereço estático (começando com `sp1...` no mainnet ou `tsp1...` no Signet) que consiste em duas chaves públicas distintas: uma chave de scan ($B_{scan}$) para detetar pagamentos recebidos e uma chave de spend ($B_{spend}$) para gastar os fundos recebidos. Esta separação permite manter a chave de despesa no hardware wallet e utilizar a chave de leitura num dispositivo ligado.



Quando um remetente deseja efetuar um pagamento, o seu wallet combina a soma das chaves privadas dos seus inputs com a chave pública de digitalização do destinatário para calcular um segredo ECDH partilhado. Este segredo gera um "tweak" criptográfico que, adicionado à chave de despesa do destinatário, cria um endereço Taproot único para essa transação.



O destinatário pode reproduzir este cálculo utilizando a sua chave de digitalização privada e as chaves públicas visíveis na transação (propriedade matemática de Diffie-Hellman). Isto permite-lhe detetar e gastar os fundos sem qualquer interação prévia com o remetente.



Esta abordagem oferece várias vantagens:




- Confidencialidade do destinatário**: cada pagamento é enviado para um endereço diferente
- Confidencialidade do remetente**: não há identificador persistente que ligue os pagamentos
- Sem servidor de terceiros**: o protocolo funciona de forma autónoma
- Transacções indistinguíveis**: Os pagamentos silenciosos assemelham-se a transacções Taproot normais



O principal inconveniente é o custo da verificação: o destinatário tem de analisar cada nova transação Taproot para detetar as que lhe são destinadas.



Se quiser saber mais sobre o funcionamento técnico do Silent Payments, recomendamos o curso BTC204 sobre confidencialidade no Bitcoin, que inclui um capítulo dedicado ao Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Plataformas suportadas



O Dana Wallet está disponível como uma aplicação Android. O APK pode ser descarregado através do repositório dedicado F-Droid fornecido pelos programadores, através do Obtainium ou diretamente do GitHub. Para os utilizadores de Linux, é tecnicamente possível compilar a aplicação Flutter para o ambiente de trabalho.



A aplicação não está disponível no iOS nem nas lojas oficiais (Google Play, App Store), o que reflecte o seu estatuto experimental e o facto de se centrar num público técnico.



## Instalação



### Pré-requisitos essenciais



Para instalar o Dana Wallet no Android, é necessário um dispositivo Android com a opção "Fontes desconhecidas" activada nas definições de segurança. Não é necessária qualquer conta ou registo.



### Adicionar depósito F-Cold



O método recomendado é adicionar o repositório F-Droid dedicado da Dana Wallet. Vá a `fdroid.silentpayments.dev` onde encontrará a ligação ao repositório e um código QR para digitalizar. O repositório oferece atualmente 3 aplicações: a versão Mainnet, Development e Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Instalação através do F-Droid



Abra a aplicação F-Droid no seu dispositivo Android e, em seguida, aceda a Definições através do ícone no canto inferior direito. Selecione "Repositórios" para gerir as fontes das aplicações. Prima o botão "+" para adicionar um novo repositório e, em seguida, digitalize o código QR ou cole a ligação `https://fdroid.silentpayments.dev/fdroid/repo`. Quando o repositório tiver sido adicionado, verá as três versões do Dana Wallet disponíveis. Selecione "Dana Wallet - Marcador" e prima "Instalar".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Configuração inicial



### Criação de portefólio



No primeiro lançamento, o Dana Wallet apresenta um ecrã de boas-vindas que introduz a sua missão: "Enviar e receber donativos sem intermediários". Prima "Iniciar" para continuar. O ecrã seguinte apresenta as três principais vantagens da aplicação:




- Donativos sem esforço**: comece a receber donativos em segundos
- Privacidade por defeito**: sem necessidade de servidores ou infra-estruturas complexas
- Experiência semelhante à do correio eletrónico**: enviar e receber bitcoins tão simplesmente como um correio eletrónico



Pode escolher entre "Restore" (Restaurar) para restaurar uma carteira existente ou "Create new wallet" (Criar novo wallet) para criar uma nova carteira. Prima "Criar novo wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



A aplicação gera então uma frase de recuperação, que deve ser cuidadosamente anotada num suporte físico. Mesmo para fundos de teste sem valor real, adopte boas práticas de cópia de segurança.



### Interface e parâmetros



Uma vez criada a carteira, é conduzido à interface principal, dividida em dois separadores: "Transação" e "Definições".



O separador **Transact** apresenta o seu saldo de bitcoin (e a respectiva conversão em dólares), uma lista de transacções recentes e dois botões de ação: "Pagar" para enviar fundos e um botão de receção (ícone de transferência).



O separador **Definições** oferece quatro opções:




- Mostrar a frase seed**: apresenta a sua frase de recuperação para segurança
- Alterar moeda fiduciária**: alterar a moeda de apresentação (USD por defeito)
- Set backend url**: configurar o URL do servidor Blindbit (ver secção seguinte)
- Wipe wallet**: apaga completamente o wallet do dispositivo



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### O servidor Blindbit



Dana Wallet utiliza um servidor de indexação chamado **Blindbit** para detetar os seus pagamentos silenciosos. Compreender como funciona é importante para avaliar o modelo de confiança da aplicação.



**Porque é que precisamos de um servidor?



Para detetar um pagamento silencioso, o wallet deve teoricamente analisar todas as transacções Taproot em cada bloco e efetuar um cálculo criptográfico (ECDH) para cada uma delas. Num telemóvel, esta operação seria demasiado intensiva em termos de computação e de largura de banda.



O servidor Blindbit resolve este problema pré-calculando dados intermédios (chamados "tweaks") para todas as transacções Taproot. O seu wallet descarrega então estes tweaks (33 bytes por transação) e executa o cálculo final **localmente** para verificar se um pagamento lhe pertence.



**Confidencialidade preservada



Ao contrário de um servidor Electrum convencional, em que o utilizador revela as suas moradas, o servidor Blindbit não sabe quais os pagamentos que lhe pertencem. Fornece os mesmos dados a todos os utilizadores e é o seu telefone que efectua a verificação final. A sua confidencialidade é assim preservada em relação ao servidor.



**Servidor predefinido



Dana Wallet utiliza o servidor público `silentpayments.dev/blindbit/signet` (para Signet) ou `silentpayments.dev/blindbit/mainnet` (para Mainnet). Pode alterar este URL nas definições se alojar o seu próprio servidor.



**Hospede seu próprio servidor Blindbit



Para utilizadores que desejem total soberania, é possível alojar o seu próprio servidor Blindbit Oracle. Isso requer :




- Um nó central Bitcoin completo **não emaranhado** (não-pruned)
- Instalando o Blindbit Oracle (disponível no GitHub: `setavenger/blindbit-oracle`)
- Aprox. 10 GB de espaço adicional em disco
- Competências técnicas (compilação Go, configuração do servidor)



Ainda não está disponível nenhuma aplicação em pacote para o Umbrel ou o Start9. Por enquanto, a instalação continua a ser manual. Este é um domínio em evolução ativa e, no futuro, poderão surgir soluções mais acessíveis.



## Utilização diária



### Receber fundos



Para receber bitcoins, prima o botão de receção (ícone de download) no ecrã principal. A Dana Wallet apresenta então o seu endereço Silent Payment completo no formato `tsp1q...` no Bookmark. A interface oferece várias opções:




- Mostrar código QR**: apresenta o código QR do seu endereço para facilitar a leitura
- Partilhar**: partilhar o endereço através das aplicações do seu telemóvel
- Copiar**: copia o endereço para a área de transferência



Como se vê no ecrã, pode partilhar este endereço publicamente nas suas redes sociais sem comprometer a sua privacidade.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Para obter os seus primeiros fundos de teste em Signet, utilize a torneira dedicada Silent Payments acessível em `silentpayments.dev/faucet/signet`. Copie o seu endereço `tsp1...`, cole-o no campo fornecido na torneira e, em seguida, valide o pedido. Aguarde até que um bloco seja extraído (cerca de 10 minutos no Signet).



### Enviar um pagamento



Para enviar fundos, prima o botão "Pagar" no ecrã principal. Aparece o ecrã "Escolher destinatário(s)" com três opções para especificar o destinatário:




- Introduzir manualmente as informações de pagamento
- Colar da área de transferência**: colar um endereço da área de transferência
- Digitalizar código QR**: digitalizar um código QR que contenha o endereço



Uma vez validado o endereço do destinatário, o ecrã "Introduzir o montante" permite-lhe introduzir o montante a enviar em satoshis. O seu saldo disponível é apresentado como referência. Para continuar, prima "Passar à seleção da taxa".



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



O ecrã seguinte apresenta três níveis de taxas, consoante a urgência requerida:




- Rápido** (10-30 minutos): taxas mais elevadas para confirmação rápida
- Normal** (30-60 minutos): custos moderados
- Lento** (1 hora ou mais): taxa mínima para transacções não urgentes



Depois de selecionar o nível da taxa, o ecrã de confirmação "Pronto a enviar?" resume todos os detalhes: endereço de destino, montante, tempo estimado e taxa de transação. Verifique cuidadosamente estas informações e, em seguida, prima "Enviar" para enviar a transação.



Uma vez enviada, a transação aparece no seu histórico com o estado "Não confirmada" até ser incluída num bloqueio. O seu saldo é atualizado em conformidade.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Vantagens e limitações



### Destaques





- Pedagógico**: interface simplificada centrada na aprendizagem Pagamentos silenciosos
- Bidirecional**: suporta tanto o envio como a receção, ao contrário de outras carteiras
- Código-fonte aberto**: código totalmente auditável no GitHub
- Faucet** dedicado: facilita a obtenção de financiamento para ensaios
- Sem conta**: não é necessário qualquer registo ou dados pessoais



### Restrições a considerar





- Experimental**: software não auditado, utilizar com precaução no Mainnet
- Plataforma limitada**: principalmente Android, sem versão iOS
- Funcionalidade reduzida**: sem controlo de moedas, sem subcontas, sem Lightning
- Análise intensiva**: a deteção de pagamentos consome recursos significativos



## Melhores práticas



### Segurança seed



Mesmo nos testes Signet com fundos inúteis, a frase de recuperação deve ser levada a sério. Use a opção "Mostrar frase seed" nas definições para a escrever cuidadosamente. Por uma questão de boa prática, mantenha carteiras completamente separadas para o Signet e o Mainnet: nunca use um seed criado para testes num wallet destinado a receber fundos reais.



### Aviso sobre o estado experimental



O Dana Wallet ainda é considerado experimental pelos seus criadores. Como eles dizem claramente: "Não utilizem fundos que não estejam dispostos a perder". Para efeitos de aprendizagem, opte pela versão Signet. Se utilizar a versão Mainnet, limite-se aos montantes token.



### Cópia de segurança e restauro



A recuperação de fundos de pagamentos silenciosos requer um wallet compatível com o protocolo BIP-352. Um wallet padrão não pode escanear a cadeia de blocos para recuperar seus Pagamentos silenciosos UTXO. Mantenha o Dana Wallet instalado ou use a opção "Restaurar" na primeira inicialização para recuperar um wallet existente.



## Comparação com BIP-47 e PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Os pagamentos silenciosos eliminam a transação de notificação BIP-47 à custa de uma verificação mais dispendiosa. O PayJoin resolve um problema diferente (correlação de entrada) e pode ser combinado com pagamentos silenciosos.



## Conclusão



A Dana Wallet é uma ferramenta pedagógica valiosa para aprender sobre pagamentos silenciosos num ambiente sem riscos. A sua abordagem minimalista permite-lhe compreender os mecanismos fundamentais do protocolo BIP-352 sem se distrair com caraterísticas secundárias. Ao experimentar o Signet, desenvolverá uma compreensão prática desta tecnologia promissora para a confidencialidade das transacções Bitcoin.



Os pagamentos silenciosos representam um avanço significativo na conciliação entre a facilidade de utilização e o respeito pela privacidade. O entusiasmo da comunidade e as primeiras integrações em várias carteiras (Cake Wallet, BitBox02, BlueWallet para envio) apontam para um futuro em que a publicação de um endereço de donativo deixará de comprometer a privacidade financeira do seu proprietário.



## Recursos



### Documentação oficial




- Repositório GitHub de Dana Wallet: https://github.com/cygnet3/danawallet
- F-Cold depósito: https://fdroid.silentpayments.dev
- Sítio comunitário Silent Payments: https://silentpayments.xyz
- Especificação BIP-352: https://bips.dev/352



### Ferramentas de teste Signet




- Faucet Pagamentos silenciosos: https://silentpayments.dev/faucet/signet
- Explorador Signet Mempool: https://mempool.space/signet



### Servidor Blindbit (auto-hospedado)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle