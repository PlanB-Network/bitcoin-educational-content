---
name: Lipa
description: Configurar e utilizar a carteira móvel Lipa lightning
---
![cover](assets/cover.webp)

Uma carteira Bitcoin Lightning é uma aplicação móvel que permite transacções instantâneas e de baixo custo na rede Lightning da Bitcoin. Ao contrário das transacções na cadeia de blocos principal (on-chain), os pagamentos Lightning são quase instantâneos e exigem taxas mínimas, o que os torna particularmente adequados para pequenos pagamentos diários.

As carteiras Lightning, tal como todas as carteiras móveis, são consideradas carteiras "quentes" porque estão ligadas à Internet. Por conseguinte, destinam-se principalmente à gestão de pequenas quantias de dinheiro para as suas despesas quotidianas. Para quantias maiores, é preferível utilizar soluções de armazenamento mais seguras, como as carteiras de hardware.

Se quiser saber mais sobre a rede Lightning e perceber como funciona tecnicamente, recomendo que faça este curso:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
Neste tutorial, vamos dar uma olhada na **Lipa**, uma carteira Lightning simples e eficaz desenvolvida na Suíça.

## Apresentação da Lipa

Lipa é uma carteira Lightning sem custódia que se distingue pela sua simplicidade de utilização e interface simples. Desenvolvida por uma equipa suíça, privilegia a confidencialidade e a facilidade de utilização para os principiantes.

As principais caraterísticas incluem:


- Interface de utilizador intuitiva
- Gestão autónoma do canal Lightning
- Suporte ao protocolo LNURL
- Possibilidade de comprar bitcoins diretamente na aplicação

## Instalação e configuração do Lipa

O primeiro passo é descarregar a aplicação Lipa. De momento, só está disponível no iOS :


- [Para a Apple](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

A versão para Android está atualmente a ser desenvolvida e estará disponível em breve.

![Installation de Lipa](assets/fr/01.webp)

Depois de lançar a aplicação, chega ao ecrã inicial, que lhe oferece duas opções:


- Criar um novo portefólio
- Restaurar um portefólio existente a partir de uma cópia de segurança

Depois de ter escolhido a sua opção, a aplicação pede-lhe que active as notificações. Este passo é importante, uma vez que as notificações são necessárias para :


- Receber alertas quando os pagamentos são recebidos, mesmo quando a aplicação está fechada
- Ser informado dos passos envolvidos na compra de bitcoin através da sua solução integrada

Em seguida, a aplicação apresenta as suas principais funções através de uma série de ecrãs introdutórios:


- Recibo de pagamento sem falhas**: Os utilizadores podem receber pagamentos em Bitcoin mesmo quando a aplicação está fechada, garantindo fiabilidade e conveniência.
- Endereços Lightning sem custódia**: A Lipa agora suporta endereços Lightning sem custódia, aumentando a privacidade e a segurança, dando aos utilizadores controlo total sobre os seus bitcoins.
- Controlo dos dados analíticos** : Com transparência e confidencialidade primordiais, os utilizadores podem ver os tipos de dados recolhidos e escolher as suas preferências de partilha.
- Enviar através do número de telefone**: Não há necessidade de endereços complexos - basta selecionar um contacto, introduzir o montante e enviar bitcoins diretamente para o seu número de telefone.

A aplicação também beneficia de melhorias contínuas em termos de estabilidade, segurança e fiabilidade, para garantir uma experiência óptima para o utilizador.

## Navegação de aplicações

A interface do Lipa está organizada em torno de 4 separadores principais acessíveis através da barra de navegação na parte inferior do ecrã:

![Navigation principale](assets/fr/02.webp)


- Início**: Apresenta o saldo atual e o histórico de transacções
- Scanner**: Permite-lhe ler códigos QR para efetuar pagamentos
- Mapa**: Apresenta um mapa interativo das empresas que aceitam Bitcoin na sua área
- Definições**: Acesso às definições da aplicação, cópia de segurança e preferências

É possível aceder a um menu adicional puxando para baixo o ecrã inicial:

![Menu supplémentaire](assets/fr/03.webp)

Este gesto revela funções adicionais, tais como :


- Comprar bitcoins
- Depósito de bitcoin na cadeia
- Criar facturas Lightning para receber bitcoins
- Pagamento relâmpago de facturas

## Guardar a sua carteira

Para fazer uma cópia de segurança da sua carteira, vá ao separador "Definições" e selecione "Frase de recuperação". Lipa utiliza uma frase de recuperação que é essencial escrever cuidadosamente num suporte físico (papel, metal). Esta frase é a única forma de recuperar os seus fundos em caso de perda ou roubo do seu telemóvel. Para validar a sua cópia de segurança, a aplicação pedir-lhe-á que confirme 3 palavras aleatórias da sua frase.

![Backup](assets/fr/04.webp)

Para obter mais informações sobre como fazer cópias de segurança e gerir corretamente a sua frase de recuperação, recomendo vivamente que siga este outro tutorial, especialmente se for um principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Receber bitcoins

Para receber bitcoins, tem duas opções. Para aceder a estas opções, volte ao ecrã inicial e puxe o ecrã para baixo. Em seguida, pode :


- Selecione "Transferir BTC" para receber bitcoins on-chain. Depois, basta digitalizar o código QR com a sua outra carteira e concluir a transação.
- Selecione "Pedir" para receber através da rede Lightning e introduza o montante que pretende receber.

Em ambos os casos, terá de pagar uma taxa equivalente a 0,4% do montante, ou cerca de 2500 sats se a aplicação tiver de abrir um novo canal de pagamento (o que será inevitavelmente o caso para o primeiro pagamento).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Enviar bitcoins

Para enviar bitcoins, vá para o ecrã inicial, puxe o ecrã para baixo e selecione "Pagar". Em seguida, basta selecionar :


- introduzir um endereço LNURL relâmpago
- digitalizar um código QR relâmpago para efetuar o pagamento.

Também pode ir para o segundo separador na parte inferior do ecrã para digitalizar diretamente um código QR.

![Envoi de bitcoins](assets/fr/07.webp)

## Comprar bitcoins

A Lipa oferece a possibilidade de comprar bitcoins diretamente na aplicação por uma taxa de 1,5%. Para fazer uma compra, vá para o ecrã inicial e puxe para baixo para exibir o menu. Em seguida, selecione "Comprar BTC". Três ecrãs introdutórios guiá-lo-ão através do processo de compra.

![Menu d'achat](assets/fr/08.webp)

Em seguida, basta introduzir os dados bancários da conta que irá utilizar para efetuar a compra. Escolha a sua moeda e introduza o seu endereço de correio eletrónico.

Após o ecrã de carregamento, encontrará o número de referência a incluir na transferência que está prestes a efetuar, bem como os dados bancários para o câmbio.

![Sélection du montant](assets/fr/09.webp)

Basta utilizar o seu banco para transferir o montante pretendido, configurar a transferência indicando o RIB previamente recuperado e indicar a referência no momento da transação para que a Lipa possa associar este movimento bancário à sua carteira Lipa.

![Confirmation d'achat](assets/fr/10.webp)

## Vantagens e desvantagens

### Benefícios


- Interface intuitiva
- Taxas de serviço corretas
- Não custodial
- Solução integrada de compra de bitcoin
- Integração do BTCmap
- Suporte NFC

### Desvantagens


- Não é possível enviar bitcoins na cadeia
- Pagamento ligeiramente mais longo do que a média

A Lipa é uma excelente escolha para se iniciar na Lightning Network, particularmente adequada para utilizadores que procuram uma solução simples para pagamentos diários. A sua facilidade de utilização e a sua interface simples fazem dela uma carteira ideal para principiantes, ao mesmo tempo que oferece as funcionalidades essenciais para a utilização quotidiana da Lightning.

## Recursos


- [Sítio Web oficial de Lipa](https://lipa.swiss/)
- [Lipa support](https://getlipa.atlassian.net/servicedesk/customer/portal/1)