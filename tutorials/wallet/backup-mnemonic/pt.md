---
name: Guarde a sua frase mnemónica
description: Descubra as melhores práticas para proteger a sua carteira Bitcoin
---
![cover](assets/cover.webp)

Quando se cria uma nova carteira Bitcoin, seja através de uma carteira de software ou de hardware, recebe-se uma frase mnemónica composta por 12 ou 24 palavras. Esta frase é muito importante, pois é a fonte de derivação de todas as chaves privadas que protegem os seus Bitcoins. Por conseguinte, deve ser cuidadosamente salvaguardada para garantir a recuperação dos seus fundos em caso de quebra, roubo ou perda do suporte da sua carteira.

Neste tutorial, vamos explorar as melhores práticas para guardar a sua frase mnemónica de forma segura, para que não perca o acesso às suas bitcoins.

## Sensibilização para os riscos

A mnemónica dá-lhe acesso total e sem restrições a todos os seus bitcoins. Qualquer pessoa na posse desta frase pode roubar os seus fundos, mesmo sem acesso físico ao suporte que aloja a sua carteira.

Isto significa, por exemplo, que se utilizar uma carteira Bitcoin num Ledger, qualquer pessoa com acesso à sua frase mnemónica pode roubar todos os seus bitcoins, mesmo sem ter acesso ao próprio Ledger. É por isso que **nunca deve partilhar a sua frase mnemónica**, seja qual for a situação.

Esta frase é, portanto, a informação única que lhe permite restaurar o acesso aos seus bitcoins em caso de perda, roubo ou danificação do suporte da carteira. Voltemos ao exemplo da Ledger: se perder o dispositivo, pode recuperar os seus fundos introduzindo a sua frase mnemónica numa nova Ledger ou em qualquer outra carteira compatível, seja ela de software ou de hardware.

Por isso, é importante guardar esta frase com o máximo cuidado e mantê-la num local seguro, como iremos detalhar nas secções seguintes.

**A sua frase mnemónica está assim exposta a dois riscos principais: roubo e perda

O roubo pode ocorrer de duas formas principais:


- Alguém obteve acesso físico à sua cópia de segurança, por exemplo, durante um roubo ou através de um amigo;
- Partilhou, voluntária ou involuntariamente, a sua pena com outra pessoa.

Para evitar o roubo físico da cópia de segurança da sua frase mnemónica, é importante guardá-la num local seguro. Este ponto será analisado em pormenor nas secções seguintes.

Quando se trata de tentativas de roubo à distância, lembre-se sempre de nunca partilhar a sua frase mnemónica, seja qual for a situação. As tentativas de phishing são comuns: e-mails fraudulentos, sites que imitam os das carteiras oficiais ou pedidos diretos através de vários canais de comunicação. Se alguém lhe pedir a sua frase mnemónica, trata-se de uma fraude, mesmo em caso de emergência! É comum os ladrões fazerem passar-se por funcionários do fabricante da sua carteira de hardware, mas saiba que estas empresas nunca lhe pedirão a sua frase-chave, seja qual for a situação. Por isso, esteja extremamente atento a qualquer comunicação que receba, seja por correio eletrónico, telefone, correio, redes sociais ou mesmo pessoalmente.

Quando precisar de introduzir a sua frase numa carteira de hardware ou software para restaurar o acesso à sua carteira após um problema com o suporte inicial, reserve algum tempo para verificar a autenticidade e integridade do hardware ou software que está a utilizar. Não entre em pânico e proceda metodicamente.

Além disso, tenha cuidado ao manusear a sua frase mnemónica. Certifique-se de que não está a ser observado por outras pessoas ou por uma câmara.

No que diz respeito ao risco de perda, este pode surgir por três razões principais: a perda do suporte de cópia de segurança, a sua degradação ou um erro na sua classificação. Nas secções seguintes, veremos mais detalhadamente como evitar ou minimizar estes três riscos.

## O apoio

Para guardar a sua frase de recuperação, tem de a escrever num suporte físico, como papel ou metal. Nunca utilize um suporte digital: não a guarde num ficheiro de texto, não a fotografe nem a guarde num gestor de palavras-passe. Estes métodos aumentam consideravelmente a superfície de ataque em comparação com os suportes físicos. A regra é, portanto, clara: utilize papel, cartão ou metal para guardar a sua frase.

Se escrever a sua frase numa simples folha de papel já é uma boa prática, optar por um suporte de metal, como o aço inoxidável, oferece uma segurança acrescida. Este tipo de suporte protege a sua frase mnemónica dos riscos de incêndio, inundação ou desmoronamento que podem afetar o local de armazenamento.

Para quem procura uma opção económica para apoiar a sua frase em metal, [o método DIY do "*SAFU Ninja*"](https://jlopp.github.io/metal-bitcoin-storage-reviews/reviews/safu-ninja/) é uma excelente solução. Basta comprar anilhas metálicas, um parafuso e uma porca nas lojas. Em seguida, grava as palavras da sua frase em cada anilha, certificando-se de que as numera, e monta-as no parafuso com a porca. Este método de baixo custo já oferece uma boa resistência.

![SEED](assets/fr/01.webp)

Crédito da imagem: [*SAFU Ninja Review*, Jameson Lopp](https://jlopp.github.io/metal-bitcoin-storage-reviews/reviews/safu-ninja/).

Se preferir investir num dispositivo completo de suporte metálico, recomendo que consulte os [testes de resistência de Jameson Lopp] (https://jlopp.github.io/metal-bitcoin-storage-reviews/), que avaliam a maioria das soluções disponíveis no mercado. Aconselho-o a optar por suportes de uma só peça, como uma placa metálica para gravação, estampagem ou perfuração. Estes dispositivos oferecem geralmente uma resistência muito maior do que os sistemas que utilizam letras independentes para serem montadas.

Se optar por uma carteira de papel, tem várias opções: uma simples folha de papel em branco, a carteira de cartão frequentemente fornecida com a sua carteira de hardware, ou o nosso modelo descarregável que pode imprimir [clicando aqui] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/wallet-backup-sheet/assets/mnemonic-sheet.pdf).

![SEED](assets/fr/02.webp)

## Cópia de segurança

Agora que já escolheu o seu suporte físico, está na altura de escrever a sua frase de recuperação! Para evitar perder os seus bitcoins, siga estas boas práticas.

Em primeiro lugar, certifique-se de que não está a ser observado, nem por outras pessoas nem por câmaras, enquanto escreve a sua frase.

Depois, dedique algum tempo a escrever cada palavra de forma clara e legível. Poderá ter de reler a sua frase daqui a alguns anos, ou outra pessoa poderá ter de o fazer no âmbito de uma herança. Por conseguinte, é essencial escrever com cuidado.

Em teoria, é possível escrever apenas as primeiras 4 letras de cada palavra, porque na lista de 2048 palavras do BIP39, não há duas palavras que partilhem as mesmas 4 primeiras letras na mesma ordem. No entanto, se o seu suporte tiver espaço suficiente, recomendo que guarde cada palavra na sua totalidade. Isto pode ser útil em caso de degradação parcial do suporte. Por exemplo, se só gravar `accu` para a palavra `accuse` e a letra `u` desaparecer, pode ter de escolher entre `accuse`, `access`, `accident` ou `account`. Por outro lado, com a palavra completa, mesmo que falte uma letra, é fácil reconhecer a palavra correta.

Também é essencial escrever as palavras na ordem correta. Se tiver as suas 24 palavras mas não souber a sua sequência exacta, será impossível recuperar a sua carteira. A numeração das palavras é igualmente importante: se o suporte se danificar ou se as palavras ficarem desorganizadas, a numeração permitir-lhe-á voltar a colocá-las na ordem correta.

![SEED](assets/fr/03.webp)

Além disso, é importante compreender que, teoricamente, a frase mnemónica por si só nem sempre é suficiente para recuperar o acesso aos seus bitcoins. Também é necessário conhecer os caminhos de derivação utilizados para gerar as chaves. Se utilizar uma carteira SingleSig com um caminho padrão, será relativamente simples recuperar as suas chaves. No entanto, com um caminho não padrão, isso pode tornar-se impossível, mesmo na posse da frase mnemónica. Para evitar este problema, recomendo vivamente que anote, no seu suporte, o caminho de derivação da conta que está a utilizar. Pode encontrar esta informação nas definições do software da sua carteira. Por exemplo, para uma carteira Taproot padrão, o caminho de derivação padrão será :

```txt
m / 86' / 0' / 0' /
```

![SEED](assets/fr/04.webp)

Se utilizar uma carteira multisig ou uma carteira com scripts complexos incluindo chaves de recuperação, como as oferecidas pelo software Liana, é essencial guardar os seus **Output Script Descriptors**. Estes descritores contêm todas as informações necessárias, para além das frases de recuperação, para recuperar o acesso aos seus bitcoins.

Também pode enriquecer a sua cópia de segurança com informações adicionais relacionadas com o suporte da sua carteira. Por exemplo, anote o código PIN utilizado para desbloquear a sua carteira de hardware, ou as palavras anti-phishing se utilizar um COLDCARD.

![SEED](assets/fr/05.webp)

Por outro lado, se utilizar uma frase-chave, certifique-se de que não a escreve no mesmo suporte que a sua frase mnemónica. O objetivo da frase-chave é proteger a sua carteira em caso de roubo. Para saber mais sobre como utilizar uma frase-chave, consulte este tutorial complementar:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Depois de guardar a frase mnemónica num suporte físico, recomenda-se vivamente que efectue um teste de recuperação enquanto a carteira recém-criada ainda estiver vazia. Este teste consiste em escrever um exemplo de informação, apagar deliberadamente a carteira vazia e, em seguida, tentar restaurá-la utilizando apenas a cópia de segurança física da frase mnemónica. Isto permitir-lhe-á verificar se a sua cópia de segurança está completa e sem erros de introdução. Também lhe permite familiarizar-se com o processo de recuperação. Desta forma, se precisar de recuperar no futuro, estará mais bem preparado e evitará o stress de uma primeira tentativa numa situação real. Para saber mais sobre como efetuar este teste, consulte este outro tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
Por fim, há a questão do número de cópias de segurança. Esta escolha depende inteiramente da sua situação pessoal. Limitar o número de cópias, por exemplo, escrevendo a frase mnemónica apenas uma vez num suporte, reduz o risco de roubo, mas aumenta o risco de perda. Pelo contrário, fazer várias cópias reduz o risco de perda, mas aumenta o risco de roubo. Assim, cabe-lhe a si encontrar o equilíbrio certo para as suas necessidades e determinar o número de cópias que considera mais adequado.

## Armazenamento

Agora que fez uma cópia de segurança cuidadosa da sua frase mnemónica, está na altura de escolher um local de armazenamento adequado. Isto dependerá da sua estratégia de segurança. Em qualquer caso, escolha um local que esteja fora da vista, onde seja improvável que alguém tropece nele, mas que seja acessível para verificações periódicas. Certifique-se também de que está protegido das intempéries, para evitar danos no substrato.

Aconselho também a não guardar a sua mnemónica em locais onde não é soberano, como um cofre num notário ou num banco. Estas opções podem parecer seguras, mas implicam que depende de terceiros para aceder ao seu backup, o que vai contra os princípios fundamentais da Bitcoin.

Para maior segurança, recomendo a utilização de uma bolsa de plástico inviolável ou de um sistema de fecho semelhante. Isto permitir-lhe-á verificar se ninguém teve acesso à sua frase. Por exemplo, se guardar a sua frase em casa e receber visitas, pode ser impossível saber se alguém a viu, memorizou ou fotografou. Uma bolsa inviolável torna este tipo de verificação simples: se estiver intacta, pode ter a certeza de que a sua frase permaneceu secreta. Estas bolsas totalmente opacas estão disponíveis online ou em lojas especializadas em Bitcoin.

![SEED](assets/fr/06.webp)

Por último, quando a sua frase for guardada num envelope inviolável, não se esqueça de anotar o identificador único do envelope. Assim, poderá verificar a sua autenticidade durante os seus controlos.

## Gestão do tempo

Agora que a sua frase está cuidadosamente armazenada, é importante estabelecer um controlo regular. Periodicamente, verifique se a sua frase ainda está presente no local de armazenamento e se o envelope opaco não foi aberto.

Durante estes controlos, pode também abrir o envelope para examinar o estado do suporte. Certifique-se de que não está danificado e que a frase ainda é perfeitamente legível. Se detetar quaisquer sinais de danos, é melhor criar uma nova cópia a partir da sua carteira de hardware. Verifique se esta nova cópia está funcional e destrua a cópia de segurança danificada de forma limpa para evitar qualquer risco de fuga.

Por fim, a gestão das frases mnemónicas levanta também a questão da herança. Este assunto será abordado em pormenor num futuro tutorial.

## Ir mais longe

Para dar um passo em frente e reforçar ainda mais a sua estratégia de segurança, recomendo que aprenda o funcionamento técnico da sua carteira Bitcoin. Ao compreender como os vários elementos interagem, bem como a sua importância e implicações, será capaz de afinar a sua estratégia de segurança com plena consciência dos riscos envolvidos. Em particular, se compreender a nível técnico o que a frase mnemónica permite, poderá ajustar a forma como a regista, armazena e gere ao longo do tempo.

É por isso que o convido a fazer o curso de formação gratuito CYP201 oferecido pela Plan ₿ Network. Este curso de formação explica em pormenor todo o funcionamento das carteiras Bitcoin, permitindo-lhe dominar os aspectos técnicos essenciais para proteger eficazmente os seus fundos:

https://planb.network/courses/cyp201
Se achou este tutorial útil, agradecia que deixasse um polegar verde abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!