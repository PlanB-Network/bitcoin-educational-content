---
name: Payjoin - Sparrow Wallet
description: Como fazer uma transação Payjoin na carteira Sparrow?
---
![tutorial cover image sparrow payjoin](assets/cover.webp)

_**ATENÇÃO:** Após a prisão dos fundadores da Samourai Wallet e a apreensão de seus servidores em 24 de abril, os Payjoins Stowaway na Samourai Wallet agora funcionam apenas trocando manualmente os PSBT entre as partes envolvidas, desde que ambos os usuários estejam conectados ao seu próprio Dojo. No caso do Sparrow, os Payjoins via BIP78 ainda funcionam. No entanto, é possível que essas ferramentas sejam reiniciadas nas próximas semanas. Enquanto isso, você pode sempre consultar este artigo para entender o funcionamento teórico dos payjoins._

_Estamos acompanhando de perto a evolução deste caso, bem como os desenvolvimentos relacionados aos ferramentas associadas. Fique assegurado de que atualizaremos este tutorial à medida que novas informações estiverem disponíveis._

_Este tutorial é fornecido apenas para fins educativos e informativos. Não endossamos nem encorajamos o uso dessas ferramentas para fins criminosos. É responsabilidade de cada usuário cumprir as leis em sua jurisdição._

---

> *"Force os espiões da blockchain a repensarem tudo o que eles pensam que sabem."*

Payjoin é uma estrutura específica de transação Bitcoin que melhora a privacidade do usuário durante os gastos, colaborando com o destinatário do pagamento. Existem várias implementações que facilitam a configuração e automação do PayJoin. Entre essas implementações, a mais conhecida é o Stowaway desenvolvido pela equipe da Samourai Wallet. Este tutorial tem como objetivo orientá-lo no processo de fazer uma transação Payjoin Stowaway usando o software Sparrow Wallet.

## Como o Stowaway funciona?

Como mencionado anteriormente, a Samourai Wallet oferece uma ferramenta PayJoin chamada "Stowaway". Ela é acessível por meio do software Sparrow Wallet no PC ou do aplicativo Samourai Wallet no Android. Para realizar um Payjoin, o destinatário, que também atua como colaborador, deve usar um software compatível com o Stowaway, ou seja, Sparrow ou Samourai Wallet. Esses dois softwares são interoperáveis, permitindo transações Stowaway entre uma carteira Sparrow e uma carteira Samourai, e vice-versa.

O Stowaway se baseia em uma categoria de transações que a Samourai se refere como "Cahoots". Um Cahoot é essencialmente uma transação colaborativa entre vários usuários que requer a troca de informações fora da cadeia. Atualmente, a Samourai oferece duas ferramentas Cahoots: Stowaway (Payjoins) e StonewallX2 (que exploraremos em um artigo futuro).

As transações Cahoots envolvem a troca de transações parcialmente assinadas entre os usuários. Esse processo pode ser demorado e complicado, especialmente quando feito remotamente. No entanto, ainda pode ser feito manualmente com outro usuário, o que pode ser conveniente se os colaboradores estiverem fisicamente próximos. Na prática, isso envolve a troca manual de cinco códigos QR para serem escaneados sucessivamente.

Quando feito remotamente, esse processo se torna muito complexo. Para resolver esse problema, a Samourai desenvolveu um protocolo de comunicação criptografada baseado no Tor, chamado "Soroban". Com o Soroban, as trocas necessárias para um Payjoin são automatizadas por trás de uma interface amigável ao usuário. Este é o segundo método que exploraremos neste artigo.

Essas trocas criptografadas exigem o estabelecimento de uma conexão e autenticação entre os participantes do Cahoots. As comunicações do Soroban são baseadas nos Paynyms dos usuários. Se você não está familiarizado com Paynyms, convido você a consultar este artigo para mais detalhes: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)
Simplificando, um Paynym é um identificador único vinculado à sua carteira que permite várias funcionalidades, incluindo mensagens criptografadas. O Paynym é apresentado na forma de um identificador e uma ilustração representando um robô. Aqui está um exemplo do meu no Testnet: ![Paynym Sparrow](assets/pt/1.webp)

**Em resumo:**
- *Payjoin* = Estrutura específica de transação colaborativa;
- *Stowaway* = Implementação de Payjoin disponível nas carteiras Samourai e Sparrow;
- *Cahoots* = Nome dado pela Samourai a todos os seus tipos de transações colaborativas, incluindo Payjoin Stowaway;
- *Soroban* = Protocolo de comunicação criptografada estabelecido no Tor, permitindo colaboração com outros usuários no contexto de uma transação Cahoots.
- *Paynym* = Identificador único de uma carteira que permite a comunicação com outro usuário no Soroban, a fim de realizar uma transação Cahoots.

[**-> Saiba mais sobre transações Payjoin e sua utilidade**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Como estabelecer uma conexão entre Paynyms?
Para realizar uma transação remota Cahoots, especificamente um PayJoin (Stowaway) via Samourai ou Sparrow, é necessário "seguir" o usuário com quem você pretende colaborar, usando o Paynym deles. No caso de um Stowaway, isso significa seguir a pessoa para quem você deseja enviar bitcoins.
**Aqui está o procedimento para estabelecer essa conexão:**

Primeiro, você precisa obter o identificador Paynym do destinatário. Isso pode ser feito usando o apelido ou o código de pagamento deles. Para fazer isso, na carteira Sparrow do destinatário, selecione a guia `Ferramentas` e clique em `Mostrar PayNym`.
![Mostrar Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/pt/1.webp)
Do seu lado, abra sua carteira Sparrow e acesse o mesmo menu `Mostrar PayNym`. Se você estiver usando seu Paynym pela primeira vez, precisará obter um identificador clicando em `Recuperar PayNym`.
![Recuperar paynym](assets/notext/3.webp)
Em seguida, insira o identificador do Paynym do seu colaborador (seja o apelido `+...` ou o código de pagamento `PM...`) na caixa `Encontrar Contato` e clique no botão `Adicionar Contato`.
![adicionar contato](assets/notext/4.webp)
O software então oferecerá um botão `Vincular Contato`. Não é necessário clicar neste botão para o nosso tutorial. Esta etapa é apenas necessária se você planeja fazer pagamentos ao Paynym indicado no contexto do BIP47, que não está relacionado ao nosso tutorial.

Assim que o Paynym do destinatário for seguido pelo seu Paynym, repita essa operação na direção oposta para que o destinatário também o siga. Você pode então realizar um Payjoin.

## Como realizar um Payjoin na carteira Sparrow?
Se você concluiu essas poucas etapas preliminares, finalmente está pronto para realizar a transação Payjoin! Para fazer isso, siga nosso tutorial em vídeo:
![Tutorial Payjoin - Carteira Sparrow](https://youtu.be/ZQxKod3e0Mg)

**Recursos externos:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.
