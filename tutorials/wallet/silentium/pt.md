---
name: Silentium
description: Web progressiva wallet com suporte para pagamentos silenciosos (BIP-352)
---

![cover](assets/cover.webp)



A reutilização de endereços Bitcoin é uma das ameaças mais diretas à confidencialidade do utilizador. Quando um destinatário partilha um único endereço para receber vários pagamentos, qualquer observador pode rastrear todas as transacções associadas e reconstruir o seu historial financeiro. Este problema afecta particularmente os criadores de conteúdos, as instituições de caridade ou os activistas que pretendem apresentar publicamente um endereço de donativo sem comprometer a sua privacidade.



O Silentium responde a este problema com uma solução elegante acessível diretamente a partir do seu navegador. Esta aplicação Web progressiva (PWA) de código aberto, lançada em maio de 2024 por Louis Singer, implementa o Silent Payments (BIP-352): um endereço estático reutilizável em que cada pagamento acaba num endereço blockchain separado, sem qualquer interação prévia ou ligação observável entre as transacções.



**Aviso importante**: O Silentium é um projeto experimental que serve como *prova de conceito* para os wallet leves da Silent Payments. Não deve ser usado como um wallet diário ou para armazenar quantias significativas. Os criadores afirmam explicitamente:



> Utilizar por sua conta e risco.

Note-se que este wallet pode ser utilizado como testnet ou regtest.



## O que é o Silentium?



### Filosofia e objectivos



O Silentium serve de demonstração técnica para a implementação de pagamentos silenciosos num navegador wallet leve. Embora também suporte endereços Bitcoin convencionais, a ênfase é colocada nos pagamentos silenciosos para permitir que os utilizadores experimentem esta tecnologia de privacidade de uma forma simples.



### Como funcionam os pagamentos silenciosos?



Os pagamentos silenciosos (BIP-352) utilizam a chave Elliptic Curve Diffie-Hellman Exchange (ECDH). O destinatário gera um endereço estático (`sp1...` no mainnet, `tsp1...` na testnet) que consiste em duas chaves públicas: uma chave de scan para detetar pagamentos e uma chave de spend para os utilizar.



O remetente combina as suas chaves de entrada privadas com a chave de digitalização do destinatário para calcular um segredo partilhado que gera um "tweak" criptográfico. Este "tweak", adicionado à chave de despesa, cria um endereço Taproot único para cada transação. O destinatário reproduz este cálculo com a sua chave de leitura privada para detetar e gastar os fundos sem qualquer interação prévia.



Vantagens: maior confidencialidade para o remetente e o destinatário, não é necessário um servidor de terceiros, as transacções são indistinguíveis dos pagamentos Taproot convencionais. Desvantagem principal: controlo intensivo do blockchain para detetar pagamentos.



Para saber mais sobre o funcionamento teórico dos Pagamentos Silenciosos, ver a última parte do curso BTC,204 sobre Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Plataformas suportadas



O Silentium é uma Progressive Web App (PWA) acessível a partir de qualquer navegador moderno (móvel ou desktop). Utilize-o diretamente em `app.silentium.dev`, instale-o como uma aplicação nativa através do seu browser, ou implemente-o localmente. A instalação é feita diretamente a partir do navegador, sem passar pelas lojas oficiais.



## Utilizar a aplicação Web



### Acesso e instalação



[Aceda a `https://app.silentium.dev/` a partir do seu browser] (https://app.silentium.dev/). A aplicação é carregada instantaneamente e apresenta o ecrã inicial.



Para o instalar como uma aplicação nativa no iOS, prima o botão de partilha (quadrado com seta para cima) e selecione "No ecrã inicial". No Android, o navegador oferece normalmente uma notificação "Adicionar ao ecrã inicial" diretamente. Uma vez instalado, o Silentium aparece com o seu ícone dedicado e funciona como uma aplicação nativa, mas requer uma ligação à Internet para sincronizar as transacções.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Criação de portefólio



No primeiro lançamento, selecione "Create Wallet" (Criar Wallet) para gerar um novo wallet ou "Restore Wallet" (Restaurar Wallet) para restaurar a partir de uma frase de recuperação existente.



Selecione "Criar Wallet". A aplicação gera uma frase de 12 palavras que deve escrever cuidadosamente. Esta frase é a única forma de recuperar os teus fundos. Mesmo na testnet, adopte boas práticas de cópia de segurança. Prima "Continuar" depois de guardar a frase.



A aplicação pede-lhe então que defina uma palavra-passe para proteger o acesso ao wallet. Escolha uma palavra-passe forte e confirme-a.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Quando a frase tiver sido confirmada e a palavra-passe definida, será conduzido à interface principal.



### Interface principal e parâmetros



A interface principal apresenta o seu saldo em satoshis (inicialmente 0 sats), com três botões na parte inferior:




- Sync**: sincroniza o wallet com o blockchain
- Receive**: receber fundos
- Enviar**: para enviar bitcoins



Aceder às Definições através do ícone no canto superior direito (três barras horizontais). O menu Definições oferece várias opções:





- Sobre**: informações sobre a candidatura
- Backup**: backup da frase de recuperação
- Explorer**: selecionar o explorador blockchain (Mempool por defeito) e o servidor Silentiumd
- Rede**: seleção da rede (mainnet/testnet)
- Palavra-passe**: alterar a palavra-passe
- Recarregar**: recarregar o wallet
- Reiniciar**: reiniciar completamente
- Tema**: alterar o tema



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



A secção **Explorer** é particularmente importante: permite-lhe escolher o explorador blockchain utilizado (Mempool por defeito) e também apresenta o URL do servidor Silentiumd (`https://bitcoin.silentium.dev/v1` para mainnet). Se alojar o seu próprio servidor Silentiumd ou desejar utilizar a testnet, é aqui que configura estes parâmetros.



### Receber fundos



A partir da interface principal, prima o botão "Receive" (Receber). Por defeito, o Silentium apresenta um endereço de Pagamento Silencioso com o seu código QR. O endereço começa por `sp1...` no mainnet ou `tsp1...` na testnet.



Pode alternar entre o pagamento silencioso e os endereços Bitcoin clássicos utilizando o botão "Mudar para endereço clássico" / "Mudar para endereço silencioso" na parte inferior do ecrã.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Uma vez transmitida a transação, aguarde alguns minutos. Para os pagamentos silenciosos, o Silentium procura automaticamente no blockchain as transacções que lhe são destinadas. As transacções aparecem com o estado "Não confirmada" antes de serem progressivamente confirmadas.



### Enviar um pagamento



A partir da interface principal, prima o botão "Enviar". O ecrã de envio perguntar-lhe-á :



1. **Address**: colar um endereço de pagamento silencioso (`sp1...` ou `tsp1...`) ou um endereço Bitcoin clássico. Pode utilizar o ícone QR scan para digitalizar um endereço.


2. **Montante**: introduzir o montante em satoshis a enviar. É apresentado um teclado numérico para facilitar a introdução. O seu saldo disponível é apresentado na parte superior para referência.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Depois de introduzir o endereço e o montante, prima "Prosseguir" para continuar. A aplicação pedir-lhe-á que selecione o nível de taxa pretendido antes de confirmar a transação.



## Auto-hospedagem wallet



### Porquê auto-hospedar?



O alojamento local do Silentium oferece total soberania, verificação do código, um ambiente de desenvolvimento e resiliência face a falhas do sítio oficial.



### Pré-requisitos



Node.js (versão 14+), npm ou yarn, Git e cerca de 500 MB de espaço em disco.



### Instalação local



Clone o repositório e instale o arquivo :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Lançamento e utilização



Iniciar a aplicação em modo de desenvolvimento:



```bash
yarn start
```



Ir para `http://localhost:3000` no seu browser. Para uma versão de produção optimizada :



```bash
yarn build
```



Os arquivos gerados em `build/` podem ser servidos com nginx, Apache ou qualquer servidor web. Por padrão, o Silentium se conecta ao servidor público `bitcoin.silentium.dev`. Modifique esta configuração nos parâmetros para usar o testnet ou seu próprio servidor.



## O servidor Silentiumd



### Papel e funcionamento



O Silentium utiliza um servidor de indexação **Silentiumd** para otimizar a deteção de pagamentos. A verificação de todas as transacções Taproot seria demasiado pesada para um browser ou telemóvel.



O Silentiumd pré-calcula dados intermédios (tweaks) para cada transação do Taproot. O seu wallet descarrega estes ajustes (alguns bytes por transação) e efectua o cálculo final localmente, verificando a propriedade do pagamento. O servidor nunca conhece as suas chaves ou pode identificar as suas transacções, ao contrário dos servidores Electrum convencionais.



Os filtros compactos BIP158 permitem que o wallet determine quais os blocos a analisar sem revelar os seus endereços, preservando assim a sua confidencialidade.



### Servidor público



O servidor público `bitcoin.silentium.dev` (mainnet), patrocinado pela Vulpem Ventures, oferece uma experiência simples e imediata. Embora a confidencialidade seja preservada, esta abordagem implica uma confiança relativa na infraestrutura de terceiros.



### Alojar o seu próprio servidor Silentiumd



Para total soberania, hospede seu próprio servidor Silentiumd. Pré-requisitos: Nó Bitcoin Core não-elagged com `txindex=1` e `blockfilterindex=1`, Go 1.21+, 10-20 GB de espaço em disco, habilidades de administração de sistemas.



**Instalação



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Configure através de variáveis de ambiente (veja o `config.md` do repositório para detalhes). O servidor indexa o blockchain e expõe um API que pode ser consultado pelo seu wallet.



Não existem atualmente soluções em pacote para o Umbrel ou o Start9, o que limita a acessibilidade a utilizadores não técnicos.



## Vantagens e limitações



### Destaques





- Máxima acessibilidade**: utilização a partir de qualquer browser, sem necessidade de instalação pesada
- Multi-plataforma**: funciona em dispositivos móveis (Android/iOS) e no ambiente de trabalho graças à tecnologia PWA
- Auto-hospedagem simples**: instalação local possível com alguns comandos
- Código-fonte aberto**: código totalmente auditável no GitHub
- Focado na privacidade**: sem rastreio, sem análises, cálculos criptográficos locais
- Arquitetura separada**: separação clara entre o wallet (cliente) e o servidor de indexação
- Sem conta**: não é necessário qualquer registo ou dados pessoais



### Restrições a considerar





- Projeto experimental**: apenas prova de conceito, não se destina a utilização ou produção diária
- Sem garantias**: risco de bugs, vulnerabilidades, possível perda de fundos
- Suporte limitado**: pouca documentação do utilizador, pequena comunidade, nenhum suporte oficial
- Dependência de servidor**: requer um servidor Silentiumd em funcionamento (público ou auto-hospedado)
- Verificação intensiva**: A deteção silenciosa de pagamentos consome largura de banda
- Funcionalidade reduzida**: sem controlo de moedas, sem Lightning, sem multi-signatures



## Melhores práticas



### Segurança seed



Mesmo na testnet, trata a tua frase de recuperação com seriedade. Escreva-a e guarde-a num local seguro. Mantenha wallets separados para testnet e mainnet: nunca use um seed de teste num wallet destinado a fundos reais.



### Verificação do código fonte



Uma das vantagens da auto-hospedagem é a possibilidade de verificar o código-fonte antes de o executar. Se estiver a planear utilizar o Silentium com fundos reais, dedique algum tempo a auditar o código ou peça a um programador de confiança para o fazer. Compare também o hash do código implantado em `app.silentium.dev` com o do repositório GitHub para garantir a autenticidade.



### Cópia de segurança e restauro



A recuperação de fundos de pagamentos silenciosos requer um wallet compatível com o protocolo BIP-352. Um wallet padrão não pode digitalizar o blockchain para recuperar seus pagamentos silenciosos do UTXO. Mantenha o Silentium instalado ou certifique-se de que tem acesso a outro wallet compatível (como o Cake Wallet ou outras implementações futuras) para restaurar os seus fundos, se necessário.



## Conclusão



O Silentium proporciona um campo de ensaio acessível para compreender os pagamentos silenciosos sem fricção técnica. Como prova de conceito, demonstra como esta tecnologia de privacidade pode ser integrada num navegador wallet, preservando a auto-custódia. Experimente na testnet para descobrir este promissor avanço na privacidade do on-chain.



## Recursos



### Documentação oficial




- Silentium Repositório GitHub (wallet): https://github.com/louisinger/silentium
- Silentiumd Repositório GitHub (servidor): https://github.com/louisinger/silentiumd
- Aplicação Web: https://app.silentium.dev/
- Sítio comunitário Silent Payments: https://silentpayments.xyz
- Especificação BIP-352: https://bips.dev/352



### Artigos e recursos




- Anúncio oficial (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Pagamentos silenciosos: https://bitcoinops.org/en/topics/silent-payments/



### Ferramentas Testnet




- Torneira Testnet: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet