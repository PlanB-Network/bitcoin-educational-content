---
name: Aqua
description: Bitcoin, Lightning e Liquid numa única carteira
---
![cover](assets/cover.webp)

Aqua é uma aplicação móvel que facilita a criação de uma hot wallet para Bitcoin e Liquid, oferecendo também a possibilidade de utilizar Lightning sem a complexidade de gerir um nó, graças a swaps integrados. Permite também gerir stablecoins USDT em várias redes.

Desenvolvida pela empresa JAN3 sob a direção de Samson Mow, a aplicação Aqua foi inicialmente concebida especificamente para as necessidades dos utilizadores na América Latina, embora seja adequada para qualquer utilizador em todo o mundo. É particularmente interessante para iniciantes e para aqueles que usam Bitcoin diariamente para seus pagamentos.

Neste tutorial, vamos descobrir como usar os vários recursos do Aqua. Mas antes de o fazermos, vamos tirar um momento para entender o que é uma sidechain no Bitcoin e como funciona o Liquid, para que possamos compreender totalmente o valor do Aqua.

![AQUA](assets/fr/01.webp)

## O que é um sidechain?

O protocolo Bitcoin tem limitações técnicas intencionais que ajudam a manter a descentralização da rede e a garantir que a segurança é distribuída por todos os utilizadores. No entanto, estas limitações podem por vezes frustrar os utilizadores, particularmente durante o congestionamento devido a um elevado volume de transacções simultâneas. O debate sobre a escalabilidade do Bitcoin há muito divide a comunidade, particularmente durante a Guerra dos Blocos. Desde esse episódio, é amplamente reconhecido dentro da comunidade Bitcoin que a escalabilidade deve ser assegurada por soluções fora da cadeia, em sistemas de segunda camada. Essas soluções incluem sidechains, que ainda são relativamente desconhecidas e pouco usadas em comparação com outros sistemas, como a Lightning Network.

Uma sidechain é uma blockchain independente que funciona em paralelo com a blockchain principal da Bitcoin. Utiliza a bitcoin como unidade de conta, graças a um mecanismo chamado "*two-way peg*". Este sistema permite bloquear bitcoins na cadeia principal para reproduzir o seu valor na cadeia lateral, onde circulam sob a forma de tokens apoiados pelos bitcoins originais. Estes tokens mantêm normalmente a paridade de valor com os bitcoins bloqueados na cadeia principal, e o processo pode ser revertido para recuperar fundos em Bitcoin.

O objetivo das sidechains é oferecer funcionalidades adicionais ou melhorias técnicas, tais como transacções mais rápidas, taxas mais baixas ou suporte para contratos inteligentes. Estas inovações nem sempre podem ser implementadas diretamente na blockchain da Bitcoin sem comprometer a sua descentralização ou segurança. As sidechains permitem, portanto, testar e explorar novas soluções, preservando a integridade do Bitcoin. No entanto, estes protocolos exigem muitas vezes compromissos, nomeadamente em termos de descentralização e de segurança, em função do modelo de governação e do mecanismo de consenso escolhidos.

## O que é líquido?

Liquid é uma sobreposição de sidechain federada para Bitcoin, desenvolvida pela Blockstream para melhorar a velocidade, confidencialidade e funcionalidade das transacções. Utiliza um mecanismo de ancoragem bilateral estabelecido numa federação para bloquear bitcoins na cadeia principal e criar Liquid-bitcoins (L-BTC) em troca, tokens que circulam no Liquid, mantendo-se apoiados pelos bitcoins originais.

![AQUA](assets/fr/02.webp)

A rede Liquid assenta numa federação de participantes, constituída por entidades reconhecidas do ecossistema Bitcoin, que validam os blocos e gerem a indexação bilateral. Para além do L-BTC, a Liquid também permite a emissão de outros activos digitais, como a stablecoin USDT e outras criptomoedas.

![AQUA](assets/fr/03.webp)

## Instalar a aplicação Aqua

O primeiro passo é, obviamente, descarregar a aplicação Aqua. Aceda à sua loja de aplicações:

- [Para Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Para a Apple](https://apps.apple.com/us/app/aqua-wallet/id6468594241).
![AQUA](assets/fr/04.webp)

Para os utilizadores de Android, existe também a opção de instalar a aplicação através do ficheiro `.apk` [disponível no GitHub] (https://github.com/AquaWallet/aqua-wallet/releases).

![AQUA](assets/fr/05.webp)

Inicie a aplicação e, em seguida, selecione a caixa "*Li e aceito os Termos de Serviço e a Política de Privacidade*".

![AQUA](assets/fr/06.webp)

## Criar o seu portefólio no Aqua

Clique no botão "*Criar carteira*".

![AQUA](assets/fr/07.webp)

E voilà, o seu portefólio já está criado!

![AQUA](assets/fr/08.webp)

Mas antes de mais, como esta é uma carteira de auto-custódia, é imperativo fazer um backup físico da sua mnemónica. **Esta mnemónica dá-lhe acesso total e sem restrições a todos os seus bitcoins. Qualquer pessoa na posse desta mnemónica pode roubar os seus fundos, mesmo sem acesso físico ao seu telefone.

Permite-lhe restaurar o acesso aos seus bitcoins em caso de perda, roubo ou quebra do seu telemóvel. Por conseguinte, é muito importante guardá-la cuidadosamente num suporte físico (não digital) e armazená-la num local seguro. Pode escrevê-lo num pedaço de papel ou, para maior segurança, se se tratar de uma carteira grande, recomendo que o grave num suporte de aço inoxidável para o proteger do risco de incêndio, inundação ou desmoronamento (para uma carteira quente concebida para proteger uma pequena quantidade de bitcoins, uma simples cópia de segurança em papel é provavelmente suficiente).

Para o fazer, clique no menu Definições.

![AQUA](assets/fr/09.webp)

Em seguida, clique em "*Ver frase-semente*". Faça uma cópia de segurança física desta frase de 12 palavras.

![AQUA](assets/fr/10.webp)

No mesmo menu de definições, pode também alterar o idioma da aplicação e a moeda fiduciária utilizada.

![AQUA](assets/fr/11.webp)

Antes de receberes os teus primeiros bitcoins na tua carteira, **aconselho-te vivamente a fazeres um teste de recuperação vazio**. Tome nota de algumas informações de referência, como o seu xpub ou o primeiro endereço de receção, e depois apague a sua carteira na aplicação Aqua enquanto ainda está vazia. Em seguida, tente restaurar a sua carteira na Aqua utilizando as suas cópias de segurança em papel. Verifique se as informações do cookie geradas após a restauração correspondem àquelas que você anotou originalmente. Se corresponder, pode ter a certeza de que as suas cópias de segurança em papel são fiáveis. Para saber mais sobre como efetuar uma recuperação de teste, consulte este outro tutorial:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Não é visível na minha tela porque estou usando um emulador, mas você também encontrará uma opção nas configurações para bloquear o aplicativo com um sistema de autenticação biométrica. Recomendo fortemente ativar essa segurança, pois sem ela qualquer pessoa com acesso ao seu telefone desbloqueado poderia roubar seus bitcoins. Você pode usar o Face ID no iOS ou sua impressão digital no Android. Se esses métodos falharem durante a autenticação, você ainda poderá acessar o aplicativo através do PIN do seu telefone.

## Receber bitcoins no Aqua

Agora que a tua carteira está configurada, estás pronto para receber os teus primeiros sats! Basta clicar no botão "*Receber*" no menu "*Carteira*".

![AQUA](assets/fr/12.webp)

Pode optar por receber bitcoins onchain, no Liquid ou via Lightning.

![AQUA](assets/fr/13.webp)

Para transacções onchain, a Aqua irá gerar um endereço de receção específico onde poderá receber os seus sats.

![AQUA](assets/fr/14.webp)

Do mesmo modo, ao escolher Liquid, a Aqua fornecer-lhe-á um endereço Liquid.

![AQUA](assets/fr/15.webp)

Se preferir receber fundos através do Lightning, terá primeiro de especificar o montante pretendido.

![AQUA](assets/fr/16.webp)

Em seguida, clique em "*Gerar fatura*".

![AQUA](assets/fr/17.webp)

Aqua criará uma fatura para receber fundos de uma carteira Lightning. Observe que, ao contrário das opções onchain e Liquid, os fundos recebidos via Lightning serão automaticamente convertidos em L-BTC no Liquid usando a ferramenta Boltz, já que o Aqua não é um nó Lightning. Este processo permite-lhe receber e enviar fundos através do Lightning, mas sem nunca armazenar os seus bitcoins no Lightning.

![AQUA](assets/fr/18.webp)

Pessoalmente, vou começar por enviar bitcoins via Lightning para a Aqua. Assim que a transação for concluída com a fatura fornecida, recebemos uma confirmação.

![AQUA](assets/fr/19.webp)

Para acompanhar o progresso da troca, volte à página inicial da sua carteira e clique na conta "*L2 Bitcoin*", que lista as transacções Lightning (via troca) e Liquid.

![AQUA](assets/fr/20.webp)

Aqui pode ver a sua transação e o seu saldo de L-BTC.

![AQUA](assets/fr/21.webp)

## Troca de Bitcoin com Aqua

Agora que tem activos na sua carteira Aqua, pode trocá-los diretamente a partir da aplicação, quer para os transferir para a blockchain principal da Bitcoin, quer para a Liquid. Também pode converter os seus bitcoins em stablecoin USDT (ou outros). Para o fazer, aceda ao menu "*Mercado*".

![AQUA](assets/fr/22.webp)

Clique em "*Swaps*".

![AQUA](assets/fr/23.webp)

Na caixa "*Transfer from*", selecione o ativo que pretende negociar. Atualmente, só possuo L-BTC, pelo que é esse o ativo que selecciono.

![AQUA](assets/fr/24.webp)

Na caixa "*Transfer to*", escolha o ativo alvo para o seu swap. Pela minha parte, optei pelo USDT na rede Liquid.

![AQUA](assets/fr/25.webp)

Introduza o montante que pretende converter.

![AQUA](assets/fr/26.webp)

Confirmar clicando em "*Continuar*".

![AQUA](assets/fr/27.webp)

Certifique-se de que está satisfeito com as definições de troca e, em seguida, confirme arrastando o botão "*Swap*" na parte inferior do ecrã.

![AQUA](assets/fr/28.webp)

A sua troca está agora confirmada.

![AQUA](assets/fr/29.webp)

Olhando para o nosso portfólio, podemos ver que agora temos USDT no Liquid.

![AQUA](assets/fr/30.webp)

## Enviar bitcoins com Aqua

Agora que tem bitcoins na sua carteira Aqua, pode enviá-los. Clique no botão "*Enviar*".

![AQUA](assets/fr/31.webp)

Escolha o ativo que pretende enviar ou selecione a rede para efetuar a transação. Pela minha parte, vou enviar bitcoins via Lightning.

![AQUA](assets/fr/32.webp)

Em seguida, introduza as informações necessárias para enviar o pagamento: para onchain ou Liquid bitcoins, terá de introduzir um endereço de receção; para Lightning, é necessária uma fatura. Pode colar estas informações diretamente no campo fornecido ou utilizar o ícone do código QR para abrir a sua câmara e digitalizar o endereço ou a fatura. Em seguida, clique em "*Continuar*".

![AQUA](assets/fr/33.webp)

Clique novamente em "*Continuar*" se todas as informações estiverem corretas.

![AQUA](assets/fr/34.webp)

Em seguida, a Aqua apresenta-lhe um resumo da transação. Certifique-se de que todas as informações estão corretas, incluindo o endereço de destino, as despesas e o montante. Para confirmar a transação, deslize o botão "*Deslizar para enviar*" na parte inferior do ecrã.

![AQUA](assets/fr/35.webp)

Receberá então a confirmação do envio.

![AQUA](assets/fr/36.webp)

Agora já sabe como utilizar a aplicação Aqua para receber e gastar fundos em Bitcoin, Lightning e Liquid, tudo a partir de uma única interface.

Se achou este tutorial útil, agradecia que deixasse um polegar verde abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!

Também recomendo que consulte este outro tutorial completo sobre a aplicação móvel Blockstream Green, que é outra solução interessante para configurar a sua carteira Liquid :

https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a