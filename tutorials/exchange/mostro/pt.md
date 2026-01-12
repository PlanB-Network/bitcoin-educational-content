---
name: Mostro
description: Plataforma de troca Bitcoin P2P sem KYC via Lightning e Nostr
---

![cover](assets/cover.webp)



Como é que adquire ou vende bitcoins sem comprometer a sua soberania financeira? As plataformas centralizadas impõem procedimentos KYC invasivos que expõem os seus dados pessoais, com a possibilidade de congelamento arbitrário de contas ou vigilância estatal.



*o *Mostro P2P** oferece uma alternativa descentralizada que combina o Lightning Network, o protocolo Nostr e a retenção de facturas. A sua principal inovação: um sistema de caução automatizado em que os seus bitcoins permanecem sob o seu controlo durante toda a troca, eliminando o risco de roubo, falência da troca ou confisco arbitrário.



## O que é o Mostro P2P?



Mostro P2P é um protocolo de troca Bitcoin de código aberto criado por **grunch**, desenvolvedor do popular bot do Telegram **lnp2pbot** lançado em 2021. Embora o lnp2pbot já permitisse trocas P2P sem KYC via Lightning, ele apresentava uma grande vulnerabilidade: **O Telegram constitui um ponto de falha centralizado** suscetível de ser censurado pelos governos.



A Mostro representa a **evolução descentralizada** deste conceito: ao substituir o Telegram pelo protocolo **Nostr** (uma rede incensurável de relés distribuídos), a Mostro elimina este risco sistémico. O protocolo combina o Lightning Network para transacções instantâneas, o Nostr para uma comunicação resistente à censura e o **hold invoices** para criar um verdadeiro depósito automatizado sem custódia.



### Arquitetura técnica



Mostro funciona através de três componentes:




- Daemon Mostrod**: coordena os intercâmbios entre os utilizadores e o Lightning Network
- Nó Lightning**: cria facturas de retenção (depósito criptográfico de ~24h)
- Clientes Mostro**: interfaces de utilizador (CLI, móvel, Web)



As ordens são publicadas no Nostr como eventos públicos (tipo 38383), enquanto as transacções privadas são transmitidas através de mensagens encriptadas de ponta a ponta (NIP-59, NIP-44). Cada instância do Mostro define as suas próprias comissões (geralmente entre 0,3% e 1%) e limites de transação (entre alguns milhares e várias centenas de milhares de sats, consoante a instância).



### Vantagens decisivas



**Resistente à censura**: Nenhum governo pode fechar o Mostro enquanto existirem retransmissores Nostr algures no mundo. Ao contrário do vulnerável lnp2pbot via Telegram, Mostro permite trocas que são **à prova de censura**.



**Não custodial**: As facturas de retenção Lightning bloqueiam os seus bitcoins sem os transferir permanentemente. Os seus fundos permanecem sob o seu controlo e são-lhe automaticamente devolvidos em caso de problema (~24h).



**Confidencialidade desde a conceção**: Dois modos disponíveis para atender às suas necessidades. Modo Reputação** liga sua reputação à sua chave Nostr para construir uma confiança duradoura. O modo totalmente privado** favorece o anonimato absoluto com chaves efémeras de uso único.



## Principais caraterísticas



**Comunicação descentralizada**: Todos os pedidos são publicados no Nostr através de eventos assinados criptograficamente. As negociações privadas são transmitidas através de mensagens criptografadas de ponta a ponta, garantindo absoluta confidencialidade.



**Sistema de reputação**: classificação de 5 estrelas com cálculo iterativo permanentemente armazenado no Nostr. Permite-lhe construir gradualmente uma reputação de comerciante fiável.



**Arbitragem descentralizada**: Em caso de litígio, um árbitro imparcial examina as provas e toma uma decisão com base em critérios transparentes. Cada litígio gera um token único para efeitos de rastreabilidade.



**Flexibilidade de pagamento**: Suporte para muitas moedas fiduciárias através do serviço de taxas de câmbio yadio.io. Aceita transferências SEPA, PayPal, Revolut, dinheiro e qualquer método acordado entre as partes.



## Clientes Mostro disponíveis



A Mostro propõe dois clientes operacionais principais para as suas trocas P2P.



### Mostro CLI - Cliente de linha de comando



O **Mostro CLI** é o cliente mais maduro e funcional. Escrito em Rust, ele oferece toda a gama de recursos do Mostro por meio de uma interface de linha de comando. Compatível com macOS, Linux e Windows.



**Controlos principais** :




- `lista de encomendas`: Mostrar todas as encomendas disponíveis
- `neworder` : Criar uma nova ordem de compra ou venda
- `takesell` / `takebuy`: Aceitar uma ordem de compra ou venda
- `fiatsent`: Confirmar o envio de um pagamento fiduciário
- libertar: Libertar o depósito de garantia e finalizar a troca
- `getdm`: Ver mensagens diretas
- `rate` : Avaliar a sua contraparte após uma transação



Ideal para utilizadores técnicos, automação e ambientes que exijam a máxima segurança.



### Mostro Mobile - Aplicação para smartphone



A **aplicação móvel** em versão alfa permite negociar P2P diretamente a partir do seu smartphone. Interface gráfico intuitivo com navegação por separadores, visualização de ordens, filtros avançados e chat integrado para comunicar com as suas contrapartes.



Disponível para **Android** (via APK no GitHub), é a escolha ideal para os utilizadores que privilegiam a simplicidade e o comércio móvel ocasional.



### Mostro-web - Interface web (em desenvolvimento)



Aplicação Web JavaScript avançada Interface em desenvolvimento ativo. Concebida para oferecer uma experiência de utilizador completa com funcionalidades extensivas de negociação e gestão de carteiras. Acesso através do browser, sem necessidade de instalação.



## Instalação e configuração



Este tutorial irá guiá-lo através da instalação e utilização dos dois principais clientes Mostro: CLI e a aplicação móvel.



### Pré-requisitos essenciais



Antes de começar, é necessário :





- Um Lightning Network** wallet em funcionamento com liquidez suficiente (ou compatível com Lightning)
 - Recomendado: Phoenix, Breez, Wallet ou Satoshi...
 - Mínimo de 1000 satoshis de liquidez para testar



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Uma chave privada Nostr** (formato `nsec1...`)
 - Criar uma chave de negociação dedicada em [nostrkeygen.com](https://nostrkeygen.com/)
 - Importante**: Nunca utilize a sua chave Nostr pessoal principal
 - Guarde a sua chave privada num local seguro (gestor de palavras-passe)





- Opcional mas recomendado**: Ligação VPN ou Tor para mascarar o seu endereço IP



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Instalação do Mostro CLI



#### No macOS



**Passo 1: Verificação do Rust



Verifique se o Rust está instalado (é necessária a versão 1.64+):



```bash
rustc --version
```



Se o Rust não estiver instalado :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Passo 2: Clonagem do repositório



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Passo 3: Configuração



Copiar e editar o ficheiro :



```bash
cp .env-sample .env
```



Abra o arquivo `.env` e defina suas configurações:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Importante para a sincronização CLI/Mobile**: Para aceder às mesmas encomendas no CLI e na aplicação móvel, é necessário utilizar a **mesma Mostro Pubkey** e os **mesmos relés Nostr** em ambos os clientes. Verifique essas configurações em Configurações no aplicativo móvel.



![Configuration .env](assets/fr/02.webp)



**Passo 4: Instalação



Compilar e instalar o CLI :



```bash
cargo install --path .
```



A compilação leva de 1 a 2 minutos. O executável `mostro-cli` será instalado em `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Passo 5: Verificar



Verificar se tudo funciona:



```bash
mostro-cli --help
```



Deverá ver a lista completa de encomendas.



![Vérification avec --help](assets/fr/04.webp)



#### No Linux (Ubuntu/Debian)



Instalação idêntica à do macOS, com a adição do :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Em seguida, siga os passos 3 e 4 na secção macOS.



#### No Windows



Primeiro, instale o Rust via [rustup.rs](https://rustup.rs/) e, em seguida, use o PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Configuração idêntica: copie `.env-sample` para `.env` e preencha seus parâmetros.



### Instalar o Mostro Mobile



#### No Android



**Passo 1**: Ir para a [página de lançamentos do GitHub](https://github.com/MostroP2P/mobile/releases) e descarregar o ficheiro **app-release.apk** (aprox. 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Passo 2: Uma vez descarregado, abra o ficheiro APK a partir das suas transferências. O Android pedir-lhe-á para autorizar a instalação a partir desta fonte.



![Téléchargement et installation APK](assets/fr/11.webp)



**Passo 3**: Seguir os ecrãs de integração, que apresentam as funcionalidades:




- Negocie Bitcoin livremente - sem KYC** : Negocie sem verificação de identidade graças ao Nostr
- Privacidade por defeito**: Escolha entre o modo de reputação e o modo de privacidade total
- Segurança em cada passo**: Proteção com facturas de retenção sem custódia



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Passo 4**: Continuar a integração para descobrir :




- Conversa totalmente encriptada**: Comunicação encriptada de ponta a ponta
- Aceitar uma oferta**: Percorrer o livro de encomendas e selecionar uma oferta
- Não encontra o que precisa? ** : Crie a sua própria encomenda personalizada



![Suite onboarding](assets/fr/13.webp)



**Passo 5: Quando a integração estiver concluída, a aplicação gera automaticamente um par de chaves Nostr. Vá ao menu (☰) e depois a **Conta** para guardar as suas **Palavras Secretas** (frase de recuperação). É também neste ecrã que tem a opção de alterar o modo de privacidade anteriormente mencionado.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Importante**: Anote a sua frase de recuperação num local seguro (gestor de senhas, cofre de papel).



### Configuração inicial de segurança



Qualquer que seja a plataforma utilizada :





- Chave dedicada**: Use uma identidade Nostr separada para negociar
- Pequenas quantias**: Comece com menos de sats 10.000 para começar
- Múltiplos relés**: Configurar 3-5 relés geograficamente diferentes
- Proteção da rede**: Ativar VPN ou Tor para ocultar o seu endereço IP
- Wallet seguro**: Ativar o bloqueio automático do seu wallet Lightning



## Utilizar com CLI



Esta secção demonstra a compra de bitcoins através do Mostro CLI, seguindo um caso de utilização real.



### Passo 1: Listar as encomendas disponíveis



O comando `listar encomendas` apresenta todas as encomendas activas:



```bash
mostro-cli listorders
```



Verá uma tabela com os pormenores de cada encomenda: ID, tipo (compra/venda), montante, moeda, método de pagamento.



![Liste des ordres disponibles](assets/fr/05.webp)



Neste exemplo, é visível uma ordem para vender 5 EUR através do Revolut (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Passo 2: Receber a encomenda



Para comprar estes bitcoins, aceitar a encomenda com `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



A Mostro pedir-lhe-á que forneça uma **fatura Lightning** para receber as BTC. O montante exato em satoshis é indicado (aqui: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Passo 3: Forneça a sua fatura Lightning



Gere uma fatura Lightning a partir do seu wallet (Phoenix, Breez, etc.) com o montante exato e envie-a :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



O sistema confirma o envio e diz-lhe que deve esperar que o vendedor pague a fatura de retenção antes de ativar o depósito de garantia.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Passo 4: Contactar o vendedor



Uma vez ativado o depósito de garantia, utilize o `dmtouser` para solicitar os detalhes de pagamento ao vendedor:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Passo 5: Recuperar a resposta



Verifique as mensagens diretas para ver a resposta do vendedor:



```bash
mostro-cli getdm
```



O vendedor dá-lhe o seu ID de pagamento (neste caso, o seu Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Passo 6: Efetuar o pagamento fiduciário



Enviar o pagamento através do método acordado (Revolut, neste exemplo) para os dados de contacto fornecidos. **Conservar todos os documentos comprovativos** (capturas de ecrã, referências de transacções).



### Etapa 7: Confirmar o envio do pagamento



Uma vez efectuado o pagamento, notificar a Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Passo 8: Receção de bitcoins



Assim que o vendedor confirmar o recebimento da moeda fiduciária e liberar o depósito de garantia com o comando `release`, você receberá instantaneamente seus bitcoins na fatura Lightning que você forneceu.



### Etapa 9: Avaliação



Avaliar o vendedor para contribuir para a reputação descentralizada:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Comandos úteis



**Cancelar uma encomenda** (antes de ser aceite) :


```bash
mostro-cli cancel -o <order-id>
```



**Criar uma nova ordem de venda** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Abrir um litígio** :


```bash
mostro-cli dispute -o <order-id>
```



## Utilização com a aplicação móvel



Esta secção demonstra a venda de bitcoins através do Mostro Mobile, seguindo um caso de utilização real.



### Interface principal



A aplicação tem 3 separadores principais:





- Livro de ordens**: Procurar ordens de compra (BUY BTC) e venda (SELL BTC) disponíveis
- As minhas transacções**: Ver as suas ordens activas e históricas
- Chat**: Comunique com as suas contrapartes utilizando números



![Interface principale](assets/fr/14.webp)



### Configuração recomendada



Antes de negociar, configure algumas definições através do menu (☰) > **Definições** :





- Lightning Address** (opcional): Para receber pagamentos diretamente
- Relés**: Adicionar vários relays Nostr para resiliência (ex. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Verificar a chave pública da instância do Mostro que está a utilizar



![Paramètres de l'application](assets/fr/16.webp)



**Importante para a sincronização CLI/Mobile**: Se estiver a utilizar o CLI e a aplicação móvel, configure **exatamente os mesmos relés Nostr e Mostro Pubkey** em ambos os clientes. Sem esta configuração idêntica, não verá as mesmas encomendas disponíveis em ambas as interfaces. Os relays e Mostro Pubkey visíveis em Settings (screenshot acima) devem coincidir com os do arquivo `.env' do CLI.



### Passo 1: Criar uma ordem de venda



Prima o botão verde **"+"** no canto inferior direito e, em seguida, selecione **VENDER** (botão vermelho).



![Boutons de création d'ordre](assets/fr/17.webp)



Preencher o formulário de criação :



1. **Moeda**: Selecione a moeda que pretende receber (EUR, USD, etc.)


2. **Montante** : Introduzir o montante em moeda fiduciária (por exemplo, 1 a 3 EUR)


3. **Métodos de pagamento** : Selecionar o método (por exemplo, "Revolut")


4. **Tipo de preço**: Selecionar "Preço de mercado"


5. **Prémio**: Ajustar o prémio (cursor de -10% a +10%, recomendado: 0% para vender rapidamente)



Prima **Submeter** para publicar a sua encomenda.



### Etapa 2: Confirmação da publicação



A sua encomenda já foi publicada! Ela estará disponível durante 24 horas. Pode anulá-la a qualquer momento antes que um comprador a receba, executando o comando `cancel`.



![Ordre publié](assets/fr/18.webp)



A ordem aparece no separador **As minhas transacções** com o estado "Pendente" e o emblema "Criada por si".



### Passo 3: Um comprador recebe a sua encomenda



Quando um comprador aceita a sua encomenda, recebe uma notificação. Ver pormenores em **As minhas transacções**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Instruções importantes**: Deve agora **pagar a fatura de retenção** apresentada para bloquear os seus bitcoins (aqui 4674 sats por 1-5 EUR) no depósito de garantia. Tem **15 minutos no máximo**, caso contrário a troca será cancelada.



Copie a fatura de retenção e pague-a a partir do seu wallet Lightning (Phoenix, Breez, etc.).



### Passo 4: Comunicar com o comprador



Quando o depósito de garantia tiver sido ativado, prima **CONTACTAR** para abrir a conversa encriptada com o comprador.



O comprador (aqui "anonymous-gloriaZhao") entrará em contacto consigo para lhe pedir os seus dados de pagamento. Por favor, responda com os seus dados (Revtag, IBAN, etc.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Etapa 5: Receção do pagamento fiduciário



Espera até receberes o pagamento em moeda fiduciária na tua conta Revolut (ou noutro método acordado). **Verificar cuidadosamente**:




- O montante exato
- O remetente
- A referência, se solicitada



O comprador informá-lo-á através do chat que enviou o pagamento. O Mostro também mostrará uma mensagem a confirmar que o fiat foi enviado para ti.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Passo 6: Libertar o depósito de garantia



Depois de ter **confirmado a receção** do pagamento em moeda fiduciária na sua conta, prima o botão verde **RELEASE** e confirme o envio do satss para o comprador.



![Libération de l'escrow](assets/fr/20.webp)



As Bitcoins são transferidas instantaneamente para o comprador através da sua fatura Lightning.



### Etapa 7: Avaliar a consideração



Após o lançamento, premir **Classificação** para classificar o comprador. Selecionar de 1 a 5 estrelas (aqui 5/5) e premir **Enviar classificação**.



![Évaluation de la contrepartie](assets/fr/21.webp)



A troca terminou!



### Comprar bitcoins com a aplicação móvel



O processo para **comprar** bitcoins é semelhante, mas invertido:



1. Navegar no separador **Order Book** > **BUY BTC** para ver as ordens de venda


2. Clique numa encomenda interessante para ver os pormenores


3. Premir **Aceitar encomenda**


4. Forneça a sua fatura Lightning (gerada a partir do seu wallet)


5. Aguardar que o vendedor active o depósito de garantia


6. Contactar o vendedor através de **CONTACTO** para obter informações sobre o pagamento


7. Enviar pagamento fiduciário (guardar comprovativo)


8. O vendedor liberta o depósito de garantia após verificação


9. Receba bitcoins instantaneamente na sua fatura Lightning


10. Avaliar o vendedor (1-5 estrelas)



### Gestão de problemas



**Cancelar uma ordem**: Em **Minhas transacções**, prima a sua ordem e depois o botão **CANCELAR** (disponível apenas antes de ser tomada).



**Abrir um litígio**: Se surgir um desacordo, prima **DISPUTAr** nos detalhes da encomenda. Anexe todas as provas (capturas de ecrã do chat, referências de transacções bancárias).



## Vantagens e limitações



### Benefícios



**Soberania financeira**: Os seus bitcoins nunca deixam o seu controlo direto graças ao mecanismo de retenção de facturas, eliminando o risco de falência da bolsa ou de pirataria.



**Resistente à censura**: Nenhuma autoridade pode desligar a rede ou censurar as suas ordens. O sistema funciona enquanto os relés Nostr estiverem operacionais.



**Anonimato padrão**: Apenas uma chave Nostr pseudónima o identifica, sem KYC ou dados pessoais. Comunicações encriptadas de ponta a ponta.



**Flexibilidade de pagamento**: É possível qualquer método de pagamento mutuamente aceite (transferências, aplicações móveis, dinheiro, troca).



### Limitações



**Desenvolvimento inicial**: Interfaces rudimentares e curva de aprendizagem técnica necessárias.



**Liquidez limitada**: Número limitado de ordens, particularmente para grandes quantidades ou moedas raras.



**Requisitos técnicos**: Conhecimentos básicos de Lightning e Nostr necessários.



**Responsabilidade individual**: Sem apoio centralizado em caso de problemas, é necessário ter cuidado.



## Conclusão



A Mostro P2P representa uma alternativa promissora às bolsas centralizadas, combinando Lightning Network, Nostr e escrow automatizado para uma negociação verdadeiramente descentralizada. Apesar de seu desenvolvimento inicial e liquidez limitada, a plataforma já oferece soberania financeira, resistência à censura e anonimato padrão.



Para os bitcoiners que preferem autonomia e confidencialidade, a Mostro é uma opção viável que merece ser explorada progressivamente. A sua arquitetura descentralizada garante uma evolução comunitária e não comercial, abrindo caminho para um futuro de trocas Bitcoin verdadeiramente livres.



## Recursos



### Documentação oficial




- [Sítio Web oficial do Mostro](https://mostro.network)
- [Documentação técnica](https://mostro.network/docs-english/index.html)
- [Fundação Mostro](https://mostro.foundation)



### Código fonte e desenvolvimento




- [Repositório principal do GitHub](https://github.com/MostroP2P/mostro)
- [Cliente Web](https://github.com/MostroP2P/mostro-web)
- [Cliente CLI](https://github.com/MostroP2P/mostro-cli)



### Comunidade




- [Protocolo Nostr](https://nostr.com)
- [Guias Lightning Network](https://lightning.network)