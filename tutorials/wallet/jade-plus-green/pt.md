---
name: Jade Plus - Verde
description: Configure facilmente o Jade Plus com o Green
---
![cover](assets/cover.webp)

A Jade Plus é uma carteira de hardware exclusiva para Bitcoin concebida pela Blockstream. É a sucessora da clássica Jade, com melhorias de software, mais opções e ergonomia redesenhada para uma utilização mais intuitiva. Esta nova versão possui um magnífico ecrã LCD de 1,9 polegadas, com uma gama de cores mais ampla do que a sua antecessora. Os botões e a navegação nos menus também foram optimizados.

A Jade Plus pode ser utilizada de várias formas: através de uma ligação USB-C com fios, em modo "*Air-Gap*" com um cartão micro SD (é necessário um adaptador), por Bluetooth ou ainda através da troca de códigos QR graças à câmara integrada. Esta carteira de hardware é alimentada por bateria.

Está disponível a partir de 149,99 dólares na versão básica em preto, e o preço pode aumentar até 20 dólares para as versões "*Genesis Grey*" ou "*Lunar Silver*". A Jade Plus é, portanto, uma escolha interessante, com funcionalidades avançadas comparáveis às das carteiras de hardware topo de gama, como a Coldcard Q ou a Passport V2, mas a um preço bastante baixo, próximo dos modelos de gama média.

![JADE-PLUS-GREEN](assets/fr/01.webp)

O Jade Plus é compatível com a maioria dos softwares de gestão de carteiras. Aqui está um resumo da compatibilidade no momento da redação (janeiro de 2025):

| Desktop | Móvel | USB | Bluetooth | QR | JadeLink | Software de gestão

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

pardal | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 |

nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |

| Keeper | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

Neste tutorial, vamos configurar e utilizar o Jade Plus com a aplicação móvel Green Wallet da Blockstream através de uma ligação Bluetooth. Esta configuração é ideal para principiantes. Se estiver à procura de uma abordagem mais avançada, recomendo que dê uma vista de olhos a este tutorial onde utilizamos o Jade Plus com a Sparrow Wallet no modo de códigos QR:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## O modelo de segurança Jade Plus

O Jade Plus utiliza um modelo de segurança baseado num "elemento seguro virtual", materializado por um "oráculo cego". Em termos concretos, este mecanismo combina o PIN escolhido pelo utilizador, um segredo alojado no Jade e um segredo detido pelo oráculo (um servidor mantido pela Blockstream), para criar uma chave AES-256 distribuída por duas entidades. Durante a iniciação, uma troca de ECDH protege a comunicação com o oráculo e encripta a frase de recuperação na carteira de hardware. Em termos práticos, quando se pretende aceder à seed para assinar transacções, é necessário aceder ao :


- Para o próprio dispositivo Jade Plus;
- Para o PIN para desbloquear o dispositivo ;
- E ao segredo do oráculo.

A principal vantagem desta abordagem é a ausência de um ponto único de falha ao nível do hardware, uma vez que, se um atacante conseguir aceder ao seu Jade, a extração das chaves requer o comprometimento simultâneo do Jade e do oráculo. Este modelo significa também que o Jade Plus é inteiramente open-source, evitando os constrangimentos associados à utilização de verdadeiros elementos físicos de segurança, como os utilizados no Ledger, por exemplo.

A desvantagem deste sistema é que a utilização do Jade Plus depende do oráculo mantido pela Blockstream. Se este oráculo se tornar inacessível, deixa de ser possível utilizar a carteira de hardware diretamente com o PIN. No entanto, isso não significa que seus bitcoins estão perdidos, pois eles ainda podem ser recuperados usando sua frase de recuperação, que pode ser inserida no Jade Plus no modo "*stateless*". Para contornar esta dependência, também é possível configurar e gerir o seu próprio servidor oracle.

## Desembalar o Jade Plus

Quando receber o seu Jade Plus, verifique se a caixa e o selo estão em boas condições para garantir que a embalagem não foi aberta.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Na caixa encontrará :


- Le Jade Plus;
- Cabo USB-C;
- Cartões para gravar a sua frase mnemónica como palavras ou como "*CompactSeedQR*";
- Algumas instruções de utilização ;
- Um cordão;
- Alguns autocolantes.

![JADE-PLUS-GREEN](assets/fr/03.webp)

O dispositivo tem 4 botões de navegação:


- O botão no canto inferior direito liga o Jade;
- O botão grande na frente do dispositivo é utilizado para selecionar um item;
- Os dois pequenos botões no topo permitem-lhe navegar para a esquerda e para a direita;
- Também pode selecionar um item clicando simultaneamente nos dois botões na parte superior do dispositivo.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Configurar uma nova carteira Bitcoin

Clique no botão Iniciar.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Clicar em "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Selecione "Begin Setup" (Iniciar configuração). A opção "*Advanced Setup*" (Configuração avançada) faz o mesmo, mas com acesso a definições avançadas.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Em seguida, clique em "*Criar uma nova carteira*" para gerar uma nova semente.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Clique no botão "*Continuar*" para visualizar a sua nova frase de recuperação.

![JADE-PLUS-GREEN](assets/fr/09.webp)

O seu Jade Plus mostra a sua frase mnemónica de 12 palavras. **Esta mnemónica dá-te acesso total e sem restrições a todos os teus bitcoins. Qualquer pessoa que possua esta frase pode roubar os teus fundos, mesmo sem acesso físico ao teu Jade Plus. A frase de 12 palavras restaura o acesso aos seus bitcoins em caso de perda, roubo ou quebra do seu Jade. Por isso, é muito importante guardá-la cuidadosamente e armazená-la num local seguro.

Pode gravá-lo no cartão fornecido na caixa ou, para maior segurança, recomendo que o grave numa base de aço inoxidável para o proteger de incêndios, inundações ou desmoronamentos.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Para mais informações sobre a forma correta de guardar e gerir a sua frase mnemónica, recomendo vivamente que siga este outro tutorial, especialmente se for um principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Obviamente, nunca devem partilhar estas palavras na Internet, como eu faço neste tutorial. Este exemplo de portefólio será utilizado apenas na Testnet e será eliminado no final do tutorial

Clique na seta à direita do ecrã para visualizar as seguintes palavras.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Depois de ter guardado a sua frase, o Jade Plus pede-lhe que a confirme. Selecione a palavra correta de acordo com a ordem, utilizando os botões na parte superior do dispositivo, e clique no botão central para passar à palavra seguinte.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Ligar o Jade Plus à carteira verde

Neste tutorial, vamos utilizar a aplicação Green Wallet para gerir a carteira alojada no Jade Plus. Este método é particularmente adequado para iniciantes. Se quiser gerir a sua carteira Bitcoin mais detalhadamente, também pode usar a Sparrow Wallet, que será abordada num tutorial separado:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Para obter instruções sobre como instalar e configurar a aplicação Blockstream Green, consulte a primeira parte deste outro tutorial:

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Uma vez na aplicação Blockstream Green, clique no botão "*Configurar uma nova carteira*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Selecione "*Na carteira de hardware*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Active o Bluetooth no seu smartphone e, em seguida, clique no botão "*Connect your Jade*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Autorizar a aplicação Green a aceder às ligações Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

A aplicação está à procura do seu Jade Plus.

![JADE-PLUS-GREEN](assets/fr/17.webp)

No Jade Plus, clique no menu "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Selecione o seu dispositivo na aplicação Verde.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Confirme o código de emparelhamento no seu Jade Plus.

![JADE-PLUS-GREEN](assets/fr/20.webp)

A Green oferece-lhe um teste para garantir que a sua Jade é genuína. Clique no botão para o fazer.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Confirmar no Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

A cor verde confirma que o dispositivo é genuíno.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Definir o código PIN

Clique no botão "*Continuar*" para escolher o código PIN da sua Jade.

![JADE-PLUS-GREEN](assets/fr/24.webp)

O código PIN desbloqueia o seu Jade. É, portanto, uma proteção contra o acesso físico não autorizado. Este código PIN não está envolvido na derivação das chaves criptográficas da sua carteira. Assim, mesmo sem acesso a este código PIN, a posse da sua frase mnemónica de 12 palavras permitir-lhe-á recuperar o acesso aos seus bitcoins. Recomendamos que escolha um código PIN que seja o mais aleatório possível. E não se esqueça de guardar este código num local separado do local onde a sua Jade está armazenada (por exemplo, num gestor de palavras-passe).

Escolha o código PIN de 6 dígitos no seu Jade, utilizando os botões direito e esquerdo para percorrer os dígitos e o botão do meio para confirmar a introdução de um dígito.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Confirme o seu PIN uma segunda vez.

![JADE-PLUS-GREEN](assets/fr/26.webp)

A sua carteira de bitcoin foi criada.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Criar uma conta Bitcoin

Agora, tem de criar uma conta na sua carteira. Clique no botão "*Criar uma conta*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Escolha "*Standard*" se pretender criar uma carteira clássica de assinatura única.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Para mais informações sobre a opção "*2FA*", pode seguir este outro tutorial:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

A sua conta foi criada.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Se quiser personalizar a sua carteira verde, clique nos três pequenos pontos no canto superior direito.

![JADE-PLUS-GREEN](assets/fr/31.webp)

A opção "*Renomear*" permite-lhe personalizar o nome da sua carteira, o que é particularmente útil se gerir várias carteiras na mesma aplicação. O menu "*Unidade*" permite-lhe alterar a unidade básica do seu portefólio. Por exemplo, pode optar por apresentá-lo em satoshis em vez de bitcoins. Finalmente, o menu "*Parameters*" dá-lhe acesso a outras opções. Aqui, por exemplo, encontrará a sua chave pública alargada e o seu descritor, útil se estiver a planear criar uma carteira só para relógios a partir do seu Jade.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Para voltar a ligar-se ao seu Jade depois de o ter desligado, prima o botão ligar/desligar na parte inferior do dispositivo. Na aplicação Green, selecione o seu dispositivo na página inicial:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Em seguida, introduza o código PIN no seu Jade e ficará novamente ligado.

![JADE-PLUS-GREEN](assets/fr/34.webp)

O seu Jade é desbloqueado através do "elemento seguro virtual" da Blockstream (ver a primeira secção deste tutorial). Isto requer uma ligação Bluetooth com a aplicação Green. Se tiveres dificuldades com a ligação Bluetooth durante o desbloqueio, tenta dissociar e voltar a associar os dois dispositivos. Se o problema persistir, pode ainda desbloquear o seu Jade selecionando a opção "*QR Scan*" e seguindo as instruções disponíveis [no sítio Web da Blockstream] (https://jadefw.blockstream.com/pinqr/index.html).

Antes de receberes os teus primeiros bitcoins na tua carteira, **aconselho-te vivamente a fazeres um teste de recuperação vazio**. Tome nota de algumas informações de referência, como o seu xpub ou o primeiro endereço de receção, depois apague a sua carteira na aplicação Green e no Jade Plus enquanto ainda está vazia (`Opções -> Dispositivo -> Factory Reset`). Em seguida, tente restaurar a sua carteira utilizando as suas cópias de segurança em papel da frase mnemónica. Verifica se a informação do cookie gerada após o restauro corresponde à que escreveste originalmente. Se corresponder, pode ter a certeza de que as suas cópias de segurança em papel são fiáveis. Para saber mais sobre como efetuar um teste de recuperação, consulte este outro tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Receber bitcoins

Agora que a tua carteira Bitcoin está configurada, estás pronto para receber os teus primeiros sats! Basta clicar no botão "*Receber*" na aplicação Green.

![JADE-PLUS-GREEN](assets/fr/35.webp)

O verde apresenta um endereço de receção, mas antes de o utilizar, é essencial verificá-lo no Jade para confirmar que pertence efetivamente à nossa carteira. Para o fazer, clique no botão "*Verificar no dispositivo*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Verificar no Jade se o endereço é o mesmo que no Verde e, em seguida, clicar no botão para confirmar.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Pode agora partilhar o endereço com o pagador para receber bitcoins na sua carteira. Quando a transação for transmitida na rede, aparecerá na sua carteira. Aguarde até ter recebido confirmações suficientes para considerar a transação definitiva.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Enviar bitcoins

Com bitcoins na tua carteira, agora também podes enviar bitcoins. Clique em "*Enviar*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Na página seguinte, introduza o endereço do destinatário. Pode introduzi-lo manualmente ou digitalizar um código QR.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Selecionar o montante do pagamento.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Na parte inferior do ecrã, pode selecionar a taxa de comissão para esta transação. Tem a opção de seguir as recomendações da aplicação ou de personalizar as suas taxas. Quanto mais elevada for a taxa em relação a outras transacções pendentes, mais rapidamente a sua transação será processada. Para obter informações sobre o mercado de comissões, visite [Mempool.space](https://mempool.space/) na secção "*Transaction Fees*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Clique em "*Próximo*" para aceder ao ecrã de resumo da transação. Verifique se o endereço, o montante e os encargos estão corretos.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Se tudo correr bem, deslize o botão verde na parte inferior do ecrã para a direita para assinar e transmitir a transação na rede Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

É-lhe agora pedido que confirme a transação no Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Certifique-se de que o endereço do destinatário está correto. Clique na marca de verificação para confirmar.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Verificar se o montante do encargo está correto e, em seguida, validar.

![JADE-PLUS-GREEN](assets/fr/47.webp)

A sua transação foi assinada e transmitida pela Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Parabéns, agora já sabes como configurar e utilizar o Jade Plus com a aplicação móvel Blockstream Green, através de uma ligação Bluetooth. Se este tutorial foi útil para ti, agradecia que deixasses um polegar verde abaixo. Não hesite em partilhar este artigo nas suas redes sociais. Obrigado por partilhar!

Para ir um pouco mais longe, recomendo este tutorial sobre o Jade Plus, onde o configuramos com o software Sparrow Wallet em modo QR. Também aprenderá a utilizar as definições avançadas da sua carteira de hardware:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

