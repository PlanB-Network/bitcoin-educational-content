---
name: Minibits Wallet
description: Guia para Minibits Wallet
---

![cover](assets/cover.webp)


Neste tutorial, vou orientá-lo na configuração do Minibits Wallet para usar o ecash. Uma poderosa tecnologia de pagamento focada na privacidade que funciona em conjunto com o Bitcoin. Minibits é um ecash e Lightning Wallet que permite transferências de valor instantâneas, baratas e privadas, tornando-o ideal para transacções diárias onde a privacidade é importante.


Antes de nos debruçarmos sobre os Minibits, vamos estabelecer um entendimento claro sobre o que é e o que não é o ecash. Muitas pessoas confundem o ecash com a tecnologia Bitcoin ou Blockchain, mas são conceitos fundamentalmente diferentes.


O Ecash NÃO é um Bitcoin. Não substitui o seu Bitcoin Wallet autocustodial, mas complementa-o. O ecash NÃO é um Blockchain e NÃO vive em nenhum Ledger público. Curiosamente, o ecash NÃO é uma tecnologia nova - na verdade, é anterior à web mundial, com conceitos desenvolvidos nos anos 1980 e 1990.


O que é o ecash: incrivelmente privado (as transacções não deixam rasto), peer-to-peer (transferências diretas sem intermediários) e funciona como um instrumento digital ao portador (se o possuir, controla-o). Uma das principais vantagens é que o ecash PODE ser utilizado offline - tanto o remetente como o destinatário podem ser desligados da Internet durante as transacções. O ecash PODE ser cunhado por uma única parte ou por uma federação de entidades de confiança, e É uma tecnologia complementar perfeita para o Bitcoin, lidando com transacções pequenas e frequentes enquanto o Bitcoin serve como o Layer de liquidação.


Por favor, note que esta configuração Minibits representa uma `solução custodial`, o que significa que está a confiar no operador da Casa da Moeda para gerir os seus fundos. Isto introduz riscos específicos que deve compreender antes de prosseguir.


O projeto apresenta esta importante declaração de exoneração de responsabilidade:


- Este Wallet deve ser utilizado apenas para fins de investigação.
- O Wallet é uma versão beta com funcionalidades incompletas e erros conhecidos e desconhecidos.
- Não o utilize com grandes quantidades de ecash.
- O dinheiro eletrónico armazenado na Wallet é emitido pela casa da moeda
- confia que a casa da moeda a apoiará com Bitcoin até transferir as suas participações para outro Bitcoin relâmpago Wallet.
- O protocolo Cashu que o Wallet implementa ainda não foi objeto de uma análise ou de testes exaustivos.


Trate os Minibits como um Wallet do dia a dia, não como uma conta poupança, e nunca guarde aqui valores significativos.


## 1️⃣ Configurar o Wallet


Para começar, visite o [Minibits Website](https://www.minibits.cash/) onde encontrará opções de download para todas as principais plataformas. Os utilizadores iOS podem fazer o download a partir da [App Store](https://testflight.apple.com/join/defJQgTD), enquanto os utilizadores iOS da UE têm a opção adicional de instalar a partir da [Freedom Store](https://freedomstore.io/). Os utilizadores de Android podem obter a aplicação a partir da [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) ou transferir o ficheiro APK diretamente da página [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Ao instalar o Minibits, você verá telas introdutórias que explicam os conceitos básicos - você pode ler essas telas ou ignorá-las se já estiver familiarizado com a tecnologia. Depois de concluir essas etapas iniciais, será solicitado que você escolha entre:


- `Entendi, leve-me ao Wallet` para novos utilizadores ou
- `Recuperar Wallet perdido` se estiver a restaurar a partir de uma cópia de segurança.


![image](assets/en/01.webp)

Depois de concluir a configuração inicial, será apresentado o ecrã inicial, que tem vários Elements aspectos importantes a ter em conta. ① O ícone de perfil no canto superior leva-o para a sua página de perfil, onde pode aceder aos seus Minibits Wallet Address e selecionar as opções de "receção em lote". ② No meio do ecrã, verá os Mints que pode utilizar, com o Minibits mint selecionado por defeito. ③ A linha de ação abaixo fornece opções para enviar pagamentos ecash ou lightning, digitalizar um código QR e receber pagamentos. ④ Por fim, a barra de navegação inferior contém atalhos para o ecrã inicial, Histórico de transacções, Contactos e Definições.


![image](assets/en/02.webp)


## 2️⃣ Gerir pastilhas de menta


Por defeito, a casa da moeda Minibits é activada quando se inicia a aplicação. No entanto, um dos pontos fortes do ecash é a capacidade de usar várias casas da moeda para aumentar a descentralização e a segurança. Para adicionar outro mint, navegue até `Configurações`, depois selecione `Gerir mints`, e finalmente toque em `Adicionar mint`.


o [Bitcoinmints.com](Bitcoinmints.com) fornece uma lista abrangente de casas da moeda disponíveis com classificações de utilizadores para o ajudar a escolher opções respeitáveis. A utilização de várias casas da moeda reduz o seu risco. Se uma casa da moeda tiver problemas, os seus fundos noutras casas da moeda permanecem acessíveis.


![image](assets/en/04.webp)


## 3️⃣ Criar uma cópia de segurança


O backup é sem dúvida o passo mais crítico em todo o processo de configuração. Para aceder às opções de Backup, navegue até `Configurações`-> `Backup` Aqui encontrará duas opções essenciais:

1. a "sua frase seed", que contém "12 palavras", permite-lhe recuperar o seu saldo de dinheiro eletrónico em caso de perda do dispositivo. Esta frase seed é a sua chave mestra para todos os ecash de todas as casas da moeda que adicionou. Escreva-a num suporte físico (papel ou metal) e guarde-a em segurança em vários locais. Nunca guarde a sua frase seed num suporte digital onde possa ser comprometida. Considere visitar este [tutorial] (https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) para conhecer as melhores práticas de proteção do seu Wallet.

2. `Wallet backup` que contém uma longa cadeia de backup.


**Atenção**: Continuará a precisar da sua frase seed quando utilizar esta cópia de segurança para recuperar o seu Wallet.


![image](assets/en/05.webp)


## 4️⃣ Criar minibits Wallet Address


Em seguida, navegue até `Contactos` na parte inferior e personalize o seu `Minibits Wallet Address` dedicado tocando em `Alterar` -> `Alterar Wallet Address`. Introduza o seu Address preferido e verifique a disponibilidade.


![image](assets/en/07.webp)


Depois de definir o seu Address, ser-lhe-á pedido que faça uma pequena `Doação` para apoiar o projeto. Embora seja opcional, recomendo vivamente que a considere se tenciona utilizar o serviço regularmente. Projectos open-source como o Minibits dependem do apoio da comunidade para continuar o seu desenvolvimento e manutenção. Mesmo uma pequena contribuição ajuda a garantir a longevidade do projeto.


![image](assets/en/08.webp)


## 5️⃣ Nostr Setup


Se quiser dar gorjetas às pessoas que segue no Nostr, pode `Adicionar a sua chave npub` selecionando `Contactos` e depois `Público`. Isso conecta o seu Minibits Wallet à rede social Nostr, permitindo que você dê gorjetas sem problemas.


Você também tem a opção de `Usar seu próprio perfil` indo em `Configurações` e depois `Privacidade` para importar seu próprio Nostr Address e chave. No entanto, esteja ciente de que isso fará com que seu Wallet pare de se comunicar com os servidores Nostr e LNURL Address do minibits.cash, o que desabilita as funcionalidades do Address para receber zaps e pagamentos.


![image](assets/en/09.webp)


## 6️⃣ Receber fundos


Para receber fundos inicialmente, é necessário carregar o seu Wallet através de um Invoice relâmpago. Este processo é simples: toque em `Topup` , introduza o `Montante` que pretende adicionar, opcionalmente adicione um `Memo` e depois toque em `Create Invoice`. Depois terá de pagar este Invoice usando outro Lightning Wallet, o que converte os pagamentos Lightning Bitcoin em ecash tokens no seu Minibits Wallet.


![image](assets/en/10.webp)


## 7️⃣ Enviar fundos


Agora que já financiou o seu Wallet, pode enviar fundos de duas formas diferentes.


### Enviar dinheiro eletrónico


A primeira opção é enviar ecash diretamente. Toque em `Enviar` , selecione `Enviar ecash`, introduza o `Montante` e toque em `Criar token.` Isto irá generate criar um código QR que pode partilhar com o destinatário ou pedir-lhe que o digitalize diretamente com o seu dispositivo. O destinatário verá os tokens aparecerem no seu Wallet quase instantaneamente, sem taxas Blockchain ou atrasos de confirmação.


![image](assets/en/11.webp)


### Pagar com o Lightning


A segunda opção é pagar através do Lightning. Toque em "Enviar" e selecione "Pagar com Lightning". Pode escolher entre os seus contactos Nostr (se tiver ligado o seu npub), ou introduzir/colar um código de pagamento Lightning Address, Invoice, ou LNURL utilizando a opção `Colar` ou `scan`. Após `Confirmar` o destinatário, ser-lhe-á pedido que introduza o `Montante a pagar`, opcionalmente adicione um memorando e, em seguida, toque em `Confirmar` seguido de `Pagar agora` para concluir a transação Lightning.


![image](assets/en/12.webp)


## 8️⃣ Criar uma ligação NWC


Outra caraterística poderosa do Minibits é a capacidade de criar conexões `Nostr Wallet Connect (NWC)`, que permitem que outras aplicações solicitem pagamentos do seu Wallet sem expor suas chaves privadas.


Para o configurar, vá a `Configurações`, selecione `Nostr Wallet Connect` e toque em `Adicionar ligação`. Dê um nome descritivo à sua ligação para identificar a aplicação e a conta de utilizador associada. Defina um limite máximo diário razoável para controlar o quanto pode ser gasto através desta ligação e, em seguida, toque em `Salvar` para concluir a configuração.


Esta funcionalidade é particularmente útil para serviços como o Nostr Clients, em que se pretende ativar a atribuição automática de gorjetas sem ter de aprovar manualmente cada transação.


![image](assets/en/12.webp)


## 🎯 Conclusão


O Minibits fornece um ponto de entrada acessível no mundo do ecash, oferecendo pagamentos focados na privacidade que complementam as suas participações no Bitcoin. Lembre-se de manter sempre cópias de segurança adequadas, considere a utilização de várias casas da moeda para redundância e armazene apenas quantidades adequadas nesta solução de custódia.


Para obter recursos adicionais, consulte o repositório GitHub do Minibits, o site oficial e o canal Telegram, onde a comunidade discute ativamente os desenvolvimentos e resolve problemas


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Sítio Web](https://www.minibits.cash/)
- [Telegrama](https://t.me/MinibitsWallet)


O ecossistema ecash ainda está a evoluir, mas ferramentas como o Minibits estão a tornar esta poderosa tecnologia de privacidade cada vez mais acessível aos utilizadores comuns.