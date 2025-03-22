---
name: Fénix
description: Instalar e utilizar a Phoenix Wallet
---
![cover](assets/cover.webp)

Phoenix é uma carteira Lightning autocustodial e um nó desenvolvido pela ACINQ, uma empresa francesa especializada em soluções de software baseadas em Lightning. Ao contrário das carteiras Lightning com custódia, como a Wallet of Satoshi, onde as bitcoins são guardadas por terceiros, a Phoenix permite que os utilizadores mantenham o controlo total das suas chaves privadas.

Phoenix funciona como um verdadeiro nó Lightning integrado ao seu telefone, que abre automaticamente um canal com o nó Lightning da ACINQ. O aplicativo é baseado no Lightning-KMP, uma implementação multiplataforma da Lightning Network em Kotlin, otimizada para carteiras móveis. Ao contrário de outras soluções de nós Lightning, o Phoenix simplifica significativamente a gestão. O usuário não precisa gerenciar a abertura e o fechamento de canais, executar um nó Bitcoin ou administrar sua liquidez na rede Lightning. O Phoenix cuida de todas essas operações técnicas em segundo plano.

Esta aplicação combina a facilidade de utilização e a comodidade das carteiras Lightning móveis com a segurança e a soberania de um verdadeiro nó Lightning pessoal. A Phoenix torna possível utilizar a Lightning Network de forma segura, eficiente e autónoma, enquanto desfruta de uma experiência de utilizador fluida e intuitiva.

Em contrapartida, aplicam-se determinadas taxas:


- O envio via Lightning custa 0,4% do montante mais 4 sats ;
- Se for necessário dinheiro para receber através do Lightning, é cobrado 1% do montante;
- Cada canal custa 1000 sats para ser aberto.

Na minha opinião, o Phoenix representa uma excelente solução intermédia entre as carteiras Lightning de custódia e a gestão manual de um nó Lightning. Esta aplicação é igualmente adequada para principiantes e utilizadores avançados que preferem não lidar com os detalhes da gestão do seu próprio LND ou Core Lightning. Vamos descobrir como a utilizar!

![Image](assets/fr/01.webp)

## Instalar a aplicação

Aceda à sua loja de aplicações e instale o Phoenix :


- Na [Google Play Store] (https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet);
- Na [App Store] (https://apps.apple.com/fr/app/phoenix-wallet/id1544097028?l=en-GB).

![Image](assets/fr/02.webp)

Também pode instalar a aplicação [com o ficheiro apk no seu repositório GitHub] (https://github.com/ACINQ/phoenix/releases).

![Image](assets/fr/03.webp)

## Criação de portefólio

Uma vez iniciada a aplicação, clique no botão "*Next*" para saltar a apresentação e, em seguida, em "*Start*".

![Image](assets/fr/04.webp)

Selecione "*Criar uma nova carteira*".

![Image](assets/fr/05.webp)

E pronto, a sua carteira Lightning e o seu nó estão agora criados.

![Image](assets/fr/06.webp)

## Guardar frase mnemónica

Antes de começarmos, precisamos de guardar a nossa frase mnemónica de 12 palavras. Esta frase dá acesso completo e sem restrições a todos os seus bitcoins. Qualquer pessoa na posse desta frase pode roubar os seus fundos, mesmo sem acesso físico ao seu telemóvel.

A frase de 12 palavras restaura o acesso aos seus bitcoins em caso de perda, roubo ou quebra do seu telemóvel. Por isso, é muito importante guardá-la cuidadosamente e guardá-la num local seguro.

Pode escrevê-la em papel ou, para maior segurança, gravá-la em aço inoxidável para a proteger de incêndios, inundações ou desmoronamentos. A escolha do suporte para a sua mnemónica dependerá da sua estratégia de segurança, mas se utilizar o Phoenix como uma carteira de despesas com montantes moderados, o papel deverá ser suficiente.

Para mais informações sobre a forma correta de guardar e gerir a sua frase mnemónica, recomendo vivamente que siga este outro tutorial, especialmente se for um principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Clique na mensagem apresentada na parte superior da interface "*Guarde a sua carteira...*".

![Image](assets/fr/07.webp)

Em seguida, clique em "*Guardar a minha carteira*".

![Image](assets/fr/08.webp)

Em seguida, clique em "*Ver a minha chave*" e guarde a sua frase mnemónica num suporte físico.

![Image](assets/fr/09.webp)

Verifique as duas caixas na parte inferior da interface para confirmar que a cópia de segurança foi concluída com êxito.

![Image](assets/fr/10.webp)

## Configuração da aplicação

Antes de efetuar as suas primeiras transacções, pode personalizar as definições clicando no ícone da roda dentada no canto inferior esquerdo da interface.

![Image](assets/fr/11.webp)

No menu "*Display*", pode escolher o tema da aplicação, a denominação utilizada para a bitcoin e a sua moeda fiduciária local.

![Image](assets/fr/12.webp)

Em "*Opções de pagamento*", encontrará várias definições avançadas para os pagamentos Lightning. Pode manter as definições predefinidas.

![Image](assets/fr/13.webp)

Em "*Gestão de canais*", defina a taxa máxima que está disposto a pagar ao abrir um canal Lightning.

![Image](assets/fr/14.webp)

No menu "*Controlo de acesso*", recomendo vivamente que active um sistema de autenticação para proteger o acesso à aplicação no seu telefone. Isto evitará que qualquer pessoa com acesso ao teu telemóvel desbloqueado aceda ao Phoenix e roube os teus bitcoins.

![Image](assets/fr/15.webp)

No menu "*Servidor Electrtrum*", se tiver um servidor Electrs, pode ligá-lo para transmitir as suas transacções.

![Image](assets/fr/16.webp)

Para aumentar a confidencialidade das suas ligações, active as ligações via Tor no menu "*Tor*". Embora a utilização do Tor possa tornar os seus pagamentos ligeiramente mais lentos e exija que a aplicação Phoenix esteja aberta em primeiro plano durante a receção, aumenta significativamente a sua privacidade.

![Image](assets/fr/17.webp)

## Receber bitcoins na cadeia

Na primeira utilização, tem a opção de carregar a sua carteira Phoenix com fundos on-chain. Você também pode fazer este primeiro depósito diretamente do Lightning (veja a próxima seção), mas em ambos os casos, taxas adicionais serão aplicadas para abrir seu primeiro canal.

Clique no botão "*Receber*".

![Image](assets/fr/18.webp)

Deslize o código QR para a direita para revelar um endereço de receção de Bitcoin. Envia-lhe o montante que pretendes depositar na Phoenix.

![Image](assets/fr/19.webp)

O montante recebido na cadeia aparecerá primeiro como pendente no saldo da sua carteira. Serão necessárias 3 confirmações para que os fundos fiquem disponíveis para utilização.

![Image](assets/fr/20.webp)

Assim que os fundos forem recebidos, o Phoenix abre automaticamente um canal Lightning para si. Agora pode enviar e receber bitcoins através da Lightning Network.

![Image](assets/fr/21.webp)

## Receber bitcoins via Lightning

Para receber sats através da Lightning Network, clique no botão "*Receber*".

![Image](assets/fr/22.webp)

O Phoenix gera uma fatura Lightning. Pode digitalizá-la ou enviá-la à pessoa que pretende transferir sats para si.

![Image](assets/fr/23.webp)

Ao clicar no botão "*Editar*", pode adicionar uma descrição que será visível para o pagador na fatura e definir um montante específico que o pagador deve enviar.

![Image](assets/fr/24.webp)

As facturas clássicas acima mencionadas só podem ser utilizadas uma vez. Para uma opção de pagamento reutilizável, pode utilizar o seu código QR reutilizável, que é uma oferta BOLT12.

![Image](assets/fr/25.webp)

Assim que a fatura ou a oferta BOLT12 for liquidada, a transação aparecerá na sua carteira Lightning.

![Image](assets/fr/26.webp)

## Enviar bitcoins via Lightning

Agora que tem o sats no Phoenix, está pronto para efetuar pagamentos através da Lightning Network. Comece por clicar no botão "*Enviar*".

![Image](assets/fr/27.webp)

Tem várias opções à sua disposição. Ao clicar em "*Digitalizar código QR*", pode digitalizar uma fatura Lightning, uma oferta BOLT12 ou mesmo um endereço de receção para pagamento na cadeia.

![Image](assets/fr/28.webp)

Também pode introduzir estas informações manualmente através do teclado no campo situado na parte superior da interface, ou introduzir um endereço Lightning (BOLT12 ou LNURL). Também pode colar as informações diretamente utilizando o botão "*Colar*".

![Image](assets/fr/29.webp)

Para este exemplo, digitalizei uma fatura de 10.000 sats. Para efetuar o pagamento, basta clicar em "*Pagar*".

![Image](assets/fr/30.webp)

A transação está concluída.

![Image](assets/fr/31.webp)

Parabéns, agora já sabe como configurar e utilizar o Phoenix. Se este tutorial foi útil para si, agradecia que deixasse um polegar verde abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Obrigado por partilhar!

Para dar um passo em frente, consulte este tutorial sobre o Alby Hub, outra solução inovadora e fácil de utilizar para lançar o seu próprio nó Lightning:

https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

E para saber mais sobre o funcionamento técnico da Rede Relâmpago, pode encontrar a excelente formação gratuita de Fanis Michalakis sobre o Plano ₿ Network :

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
