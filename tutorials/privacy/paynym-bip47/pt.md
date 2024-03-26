---
name: BIP47 - PayNym

description: Como o PayNym funciona
---

> "Ele é muito grande", todos diziam, e o galo da Índia, que nasceu com esporas e se achava o imperador, inflou-se como um navio com todas as velas içadas e avançou furioso em sua direção, vermelho até os olhos. O pobre patinho não sabia se devia parar ou continuar andando: ele ficou muito triste por ser ridicularizado por todos os patos da corte.

![BIP47, ilustração do patinho feio](assets/1.webp)

Uma das maiores preocupações no protocolo Bitcoin é a reutilização de endereços. A transparência e a distribuição da rede tornam essa prática perigosa para a privacidade do usuário. Para evitar problemas relacionados a isso, é recomendado usar um novo endereço de recebimento vazio para cada novo pagamento recebido em uma carteira, o que pode ser complicado em alguns casos.

Esse compromisso é tão antigo quanto o White Paper. Satoshi já nos alertava sobre esse risco em seu trabalho publicado no final de 2008:

> "Como uma medida adicional de segurança, um novo par de chaves pode ser usado para cada transação, para que elas não estejam vinculadas a um proprietário comum."

Existem várias soluções para receber múltiplos pagamentos sem reutilizar endereços. Cada uma delas tem seus próprios compromissos e desvantagens. Entre todas essas soluções, há o [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki), uma proposta desenvolvida por Justus Ranvier e publicada em 2015, que permite gerar códigos de pagamento reutilizáveis. Seu objetivo é realizar várias transações com a mesma pessoa sem reutilizar endereços.

Inicialmente, essa proposta foi recebida com desprezo por parte da comunidade e nunca foi adicionada ao Bitcoin Core. No entanto, alguns softwares decidiram implementá-la por conta própria. Assim, o [Samourai Wallet](https://samouraiwallet.com/) desenvolveu sua própria implementação do BIP47: o PayNym. Hoje, essa implementação está disponível no Samourai Wallet para smartphones e também no [Sparrow Wallet](https://sparrowwallet.com/) para PCs.

Com o tempo, o Samourai adicionou novos recursos diretamente relacionados ao PayNym. Agora, existe todo um ecossistema de ferramentas para otimizar a privacidade do usuário baseado no PayNym e no BIP47.
Neste artigo, você descobrirá o princípio do BIP47 e do PayNym, os mecanismos desses protocolos e as aplicações práticas resultantes. Vou abordar apenas a primeira versão do BIP47, atualmente usada para o PayNym, mas as versões 2, 3 e 4 funcionam praticamente da mesma maneira.

> A única diferença importante está na transação de notificação. A versão 1 usa um endereço simples com OP_RETURN para notificação, a versão 2 usa um script multisig (bloom-multisig) com OP_RETURN e as versões 3 e 4 usam apenas um script multisig (cfilter-multisig). Os mecanismos discutidos neste artigo, incluindo os métodos criptográficos estudados, são aplicáveis às quatro versões. Até o momento, a implementação do PayNym no Samourai Wallet e Sparrow usa a primeira versão do BIP47.

## Sumário:

1- O problema da reutilização de endereços.

2- Princípios do BIP47 e do PayNym.

3- Tutoriais: uso do PayNym.

- Construindo uma transação BIP47 com o Samourai Wallet.

- Construindo uma transação BIP47 com o Sparrow Wallet.

4- Os mecanismos do BIP47.

- O código de pagamento reutilizável.
- O método criptográfico: troca de chaves Diffie-Hellman estabelecida em curvas elípticas (ECDH).

- A transação de notificação.
- Construção da transação de notificação.
- Recebimento da transação de notificação.
- A transação de pagamento BIP47.
- Recebimento do pagamento BIP47 e derivação da chave privada.
- Reembolso do pagamento BIP47.

5- Usos derivados do PayNym.

6- Minha opinião pessoal sobre o BIP47.

## O problema da reutilização de endereços.

Um endereço de recebimento é usado para receber bitcoins. Ele é gerado a partir de uma chave pública, aplicando-se a ela um formato específico. Assim, ele permite criar uma nova condição de gasto em uma moeda para alterar o proprietário.

> Para saber mais sobre a geração de um endereço de recebimento, recomendo a leitura da última parte deste artigo: O portfólio Bitcoin - trecho [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Além disso, você provavelmente já ouviu de um entusiasta de Bitcoin que os endereços de recebimento são de uso único e que é necessário gerar um novo para cada novo pagamento recebido em sua carteira. Certo, mas por quê?
Fundamentalmente, a reutilização de endereços não coloca diretamente seus fundos em perigo. O uso de criptografia em curvas elípticas permite provar à rede que você possui uma chave privada sem revelar essa chave. Portanto, você pode bloquear várias UTXOs em um mesmo endereço e gastá-los em momentos diferentes. Se você não revelar a chave privada associada a esse endereço, ninguém poderá acessar seus fundos. O problema da reutilização de endereços está mais relacionado à privacidade.

Como mencionado na introdução, a transparência e a distribuição da rede Bitcoin permitem que qualquer usuário, desde que tenha acesso a um nó, possa observar as transações do sistema de pagamento. Assim, ele pode ver os diferentes saldos dos endereços. Satoshi Nakamoto mencionou a possibilidade de gerar novos pares de chaves e, portanto, novos endereços, para cada novo pagamento recebido em uma carteira. O objetivo seria ter uma camada adicional de proteção caso haja associação entre a identidade do usuário e um de seus pares de chaves.

Hoje, com a presença de empresas de análise de blockchain e o desenvolvimento do KYC, o uso de endereços novos não é mais uma camada adicional de proteção, mas uma obrigação para qualquer pessoa que se preocupe minimamente com sua privacidade.

A busca pela privacidade não é um conforto ou fantasia de maximalistas do Bitcoin. É um parâmetro específico que afeta diretamente sua segurança pessoal e a segurança de seus fundos. Para ilustrar isso, aqui está um exemplo muito concreto:

- Bob compra Bitcoin através do DCA (custo médio em dólares), ou seja, ele adquire uma pequena quantidade de Bitcoin em intervalos regulares para suavizar seu preço de entrada. Bob sempre envia os fundos comprados para o mesmo endereço de recebimento. Ele compra 0,01 Bitcoin todas as semanas e os envia para esse mesmo endereço. Após dois anos, Bob acumulou um Bitcoin inteiro nesse endereço.

- O padeiro da esquina aceita pagamentos em Bitcoin. Feliz por poder gastar seus Bitcoins, Bob vai comprar seu pão em satoshis. Para pagar, ele usa os fundos bloqueados em seu endereço. Agora, o padeiro sabe que ele possui um Bitcoin. Essa quantia significativa pode despertar inveja e Bob pode potencialmente sofrer um ataque físico posteriormente.

A reutilização de endereços permite que um observador faça uma conexão inegável entre suas diferentes UTXOs e, às vezes, entre sua identidade e toda a sua carteira.
É por essa razão que a maioria dos softwares de carteira Bitcoin geram automaticamente um novo endereço de recebimento quando você clica no botão "Receber". Para o usuário regular, acostumar-se a usar endereços vazios não é um grande inconveniente. No entanto, para um comércio online, uma exchange ou uma campanha de doação, essa restrição pode rapidamente se tornar inviável.
Existem muitas soluções para essas organizações. Cada uma delas tem suas vantagens e desvantagens, mas até o momento, e como veremos mais adiante, o BIP47 se diferencia verdadeiramente das outras.

Esse problema de reutilização de endereço não é negligenciável no Bitcoin. Como você pode ver no gráfico abaixo, extraído do site [oxt.me](http://oxt.me/), a taxa global de reutilização de endereço pelos usuários do Bitcoin é atualmente de 52%:
Gráfico OXT.me mostrando a evolução da taxa global de reutilização de endereços na rede Bitcoin.

![image](assets/2.webp)

Crédito: https://oxt.me/charts

A maioria dessas reutilizações vem das exchanges que, por razões de eficiência e facilidade, reutilizam o mesmo endereço várias vezes. Até o momento, o BIP47 seria a melhor solução para conter esse fenômeno nas exchanges. Isso permitiria reduzir essa taxa global de reutilização de endereço, sem causar muitos atritos para essas entidades.

Essa medida global em toda a rede é um dado particularmente coerente nesse caso. De fato, a reutilização de endereço não é apenas um problema para a pessoa que pratica esse tipo de prática, mas também para qualquer pessoa que realiza transações com ela. A perda de privacidade no Bitcoin age como um vírus e se propaga de usuário para usuário. Estudar uma medida global em todas as transações da rede nos permite perceber a magnitude desse fenômeno.

## Princípios do BIP47 e do PayNym.

O BIP47 visa oferecer uma maneira simples de receber vários pagamentos sem reutilizar endereços. Seu funcionamento é baseado no uso de um código de pagamento reutilizável.

Assim, vários remetentes podem enviar vários pagamentos para um único código de pagamento reutilizável de outro usuário, sem que o destinatário precise fornecer um novo endereço vazio para cada nova transação.

Um usuário pode então comunicar livremente seu código de pagamento (nas redes sociais, em seu site...) sem o risco de perda de privacidade, ao contrário de um endereço de recebimento comum ou uma chave pública.
Para realizar uma transação, ambos os usuários devem ter uma carteira Bitcoin com uma implementação do BIP47, como o PayNym no Samourai Wallet ou Sparrow Wallet. A associação dos códigos de pagamento dos dois usuários permite estabelecer um canal secreto entre eles. Para estabelecer corretamente esse canal, o remetente deve realizar uma transação na cadeia Bitcoin: a transação de notificação (falarei mais sobre isso em breve).
A associação dos códigos de pagamento dos dois usuários gera segredos compartilhados que por sua vez geram um grande número de endereços de recebimento Bitcoin únicos (exatamente 2^32). Assim, na realidade, o pagamento com o BIP47 não é enviado para o código de pagamento, mas sim para endereços totalmente comuns, derivados dos códigos de pagamento dos envolvidos.

O código de pagamento age como um identificador virtual, derivado da semente da carteira. Na estrutura de derivação da carteira HD, o código de pagamento está na profundidade 3, no nível das contas da carteira.

![image](assets/3.webp)

Seu objetivo de derivação é marcado como 47' (0x8000002F) em referência ao BIP47. Um caminho de derivação de um código de pagamento reutilizável seria, por exemplo:

> m/47'/0'/0'/

Para que você possa imaginar como é um código de pagamento, aqui está o meu:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Ele também pode ser codificado em um QRcode para facilitar a comunicação:

![image](assets/4.webp)

Quanto aos PayNym Bots, esses robôs que vemos no Twitter são simplesmente representações visuais do seu código de pagamento, criadas pelo Samourai Wallet. Eles são criados usando uma função de hash, o que os torna quase únicos. Aqui está o meu com seu identificador:

> +throbbingpond8B1

![image](assets/5.webp)

Esses Bots não têm utilidade técnica real. Em vez disso, eles facilitam as interações entre os usuários, criando uma identidade visual virtual.

Para o usuário, o processo de pagamento BIP47 com a implementação PayNym é extremamente simples. Vamos supor que Alice queira enviar pagamentos para Bob:

1. Bob compartilha seu código QR, ou diretamente seu código de pagamento reutilizável. Ele pode colocá-lo em seu site, em suas diferentes redes sociais públicas ou enviá-lo para Alice por meio de outro método de comunicação.
2. Alice abre seu software Samourai ou Sparrow e digitaliza ou cola o código de pagamento de Bob.
3. Alice conecta seu PayNym com o de Bob ("Follow" em inglês). Essa operação ocorre fora da blockchain e é completamente gratuita.

4. Alice conecta seu PayNym com o de Bob ("Connect" em inglês). Essa operação ocorre "on chain". Alice deve pagar as taxas de mineração da transação, bem como uma taxa fixa de 15.000 sats pelo serviço no Samourai. As taxas de serviço são gratuitas no Sparrow. Essa etapa é o que chamamos de transação de notificação.

5. Após a confirmação da transação de notificação, Alice pode criar uma transação de pagamento BIP47 para Bob. Sua carteira irá gerar automaticamente um novo endereço de recebimento vazio, para o qual apenas Bob possui a chave privada.

Realizar a transação de notificação, ou seja, conectar seu PayNym, é uma etapa prévia obrigatória para realizar pagamentos BIP47. No entanto, uma vez que isso seja feito, o remetente poderá realizar múltiplos pagamentos para o destinatário (exatamente 2^32), sem precisar realizar novamente uma transação de notificação.

Você pôde ver que existem duas operações diferentes que permitem vincular PayNyms entre si: seguir e conectar. A operação de conexão ("connecter") corresponde à transação de notificação do BIP47, que é simplesmente uma transação Bitcoin com algumas informações transmitidas por meio de uma saída OP_RETURN. Assim, ela ajuda a estabelecer uma comunicação criptografada entre os dois usuários para produzir os segredos compartilhados necessários para gerar novos endereços de recebimento vazios.

Por outro lado, a operação de vinculação ("follow" ou "relier") permite estabelecer uma conexão no Soroban, um protocolo de comunicação criptografado baseado no Tor, especialmente desenvolvido pelas equipes do Samourai.

Resumindo:

- Vincular dois PayNyms ("follow") é totalmente gratuito. Isso ajuda a estabelecer comunicações criptografadas "off chain", especialmente para usar as ferramentas de transações colaborativas do Samourai (Stowaway ou StonewallX2). Essa operação é específica do PayNym. Não está descrita no BIP47.

- Conectar dois PayNyms é pago. Isso envolve realizar a transação de notificação para iniciar a conexão. Seu custo é composto por eventuais taxas de serviço, taxas de mineração da transação e 546 sats enviados para o endereço de notificação do destinatário para informá-lo sobre a abertura do túnel. Essa operação está relacionada ao BIP47. Uma vez realizada, o remetente pode realizar vários pagamentos BIP47 para o destinatário.

Para poder conectar dois PayNyms, eles já devem estar vinculados.

## Tutoriais: uso do PayNym.

Agora que vimos a teoria, vamos estudar a prática juntos. A ideia dos tutoriais abaixo é vincular meu PayNym na minha carteira Sparrow com meu PayNym na minha carteira Samourai. O primeiro tutorial mostra como fazer uma transação usando o código de pagamento reutilizável do Samourai para o Sparrow, e o segundo tutorial descreve o mesmo mecanismo do Sparrow para o Samourai.

> Eu fiz esses tutoriais na Testnet. Eles não são bitcoins reais.

### Construindo uma transação BIP47 com a Samourai Wallet.

Para começar, você obviamente precisará do aplicativo Samourai Wallet. Você pode baixá-lo diretamente da Google Play Store ou com o arquivo APK disponível no site oficial do Samourai.

Depois de inicializar a carteira, se você ainda não o fez, solicite seu PayNym clicando no sinal de mais (+) no canto inferior direito e depois em "PayNym".

O primeiro passo para fazer um pagamento BIP47 é obter o código de pagamento reutilizável do nosso destinatário. Em seguida, poderemos nos conectar a ele e, posteriormente, fazer a conexão:

![video](assets/6.mp4)

Depois que a transação de notificação for confirmada, posso enviar vários pagamentos ao meu destinatário. Cada transação será automaticamente feita com um novo endereço vazio para o qual o destinatário possui as chaves. Ele não precisa fazer nada, tudo é calculado do meu lado.

Aqui está como fazer uma transação BIP47 na Samourai Wallet:

![video](assets/7.mp4)

### Construindo uma transação BIP47 com a Sparrow Wallet.

Da mesma forma que com o Samourai, você obviamente precisa ter o software Sparrow. Ele está disponível para computador. Você pode baixá-lo em seu [site oficial](https://sparrowwallet.com/).

Certifique-se de verificar a assinatura do desenvolvedor e a integridade do software baixado antes de instalá-lo em sua máquina.

Crie uma carteira e solicite seu PayNym clicando em "Show PayNym" no menu "Tool" na barra superior:

![image](assets/8.webp)

Em seguida, você precisará vincular e conectar seu PayNym ao do seu destinatário. Para fazer isso, insira o código de pagamento reutilizável dele na janela "Find Contact", siga-o e, em seguida, faça a transação de notificação clicando em "Link Contact":

![image](assets/9.webp)

Depois que a transação de notificação for confirmada, podemos enviar pagamentos para o código de pagamento reutilizável. Aqui está o procedimento:

![video](assets/10.mp4)

Agora que pudemos estudar o aspecto prático da implementação do PayNym do BIP47, vamos ver como todos esses mecanismos funcionam e quais métodos criptográficos são usados.

## Os mecanismos do BIP47.

Para estudar os mecanismos do BIP47, é essencial entender a estrutura da carteira determinística hierárquica (HD), os mecanismos de derivação de pares de chaves filhas e os princípios da criptografia de curvas elípticas. Felizmente, você pode encontrar todas essas informações necessárias para entender esta parte no meu blog:

- [Compreendendo os caminhos de derivação de uma carteira Bitcoin](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [A carteira Bitcoin - trecho do ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### O código de pagamento reutilizável.

Como explicado na segunda parte deste artigo, o código de pagamento reutilizável está localizado na profundidade três da carteira HD. Ele é de certa forma semelhante a um xpub, tanto em sua posição e estrutura quanto em seu papel.

Aqui estão as diferentes partes que compõem um código de pagamento de 80 bytes:

- Byte 0: A versão. Se estivermos usando a primeira versão do BIP47, este byte será igual a 0x01.

- Byte 1: O campo de bits. Este espaço é reservado para fornecer informações adicionais em caso de uso específico. Se estivermos apenas usando o PayNym, este byte será igual a 0x00.

- Byte 2: A paridade de y. Este byte indica 0x02 ou 0x03, dependendo da paridade (número par ou número ímpar) do valor da ordenada de nossa chave pública. Para obter mais informações sobre essa prática, leia a etapa 1 da parte "derivação de um endereço" deste artigo.

- Do byte 3 ao byte 34: O valor de x. Esses bytes indicam a abscissa de nossa chave pública. A concatenação de x e da paridade de y nos dá nossa chave pública comprimida.

- Do byte 35 ao byte 66: O código de cadeia. Este espaço é reservado para o código de cadeia associado à chave pública mencionada acima.

- Do byte 67 ao byte 79: O preenchimento. Este espaço é reservado para possíveis futuras evoluções. Para a versão 1, simplesmente colocamos zeros para preencher até 80 bytes, que é o tamanho dos dados de uma saída OP_RETURN.

Aqui está a representação hexadecimal do meu código de pagamento reutilizável, apresentado na parte anterior, com as cores correspondentes aos bytes apresentados acima:
Em seguida, também é necessário adicionar o byte de prefixo "P" para identificar imediatamente que se trata de um código de pagamento. Esse byte é 0x47.

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000

Por fim, calculamos o checksum desse código de pagamento com o HASH256, ou seja, um hash duplo com a função SHA256. Recuperamos os quatro primeiros bytes desse resumo e os concatenamos no final (em rosa).

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000567080c4

O código de pagamento está pronto, só precisamos convertê-lo para Base 58:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Como você pode ver, essa construção se assemelha muito à estrutura de uma chave pública estendida do tipo "xpub".

Durante esse processo que leva ao nosso código de pagamento, usamos uma chave pública comprimida e um código de cadeia. Esses dois elementos são o resultado de uma derivação determinística e hierárquica, a partir da semente da carteira, seguindo o caminho de derivação a seguir: m/47'/0'/0'/
Concretamente, para obter a chave pública e o código de cadeia do código de pagamento reutilizável, vamos calcular a chave privada mestra a partir da semente e, em seguida, derivar um par filho com o índice 47 + 2^31 (derivação reforçada). Em seguida, derivamos duas vezes pares filhos com o índice 2^31 (derivação reforçada).

> Se você quiser saber mais sobre a derivação de pares de chaves filhas em uma carteira determinística hierárquica Bitcoin, eu recomendo fazer CRYPTO301.

### O método criptográfico: troca de chaves Diffie-Hellman estabelecida em curvas elípticas (ECDH).

O método criptográfico usado como base do BIP47 é o ECDH (Elliptic-Curve Diffie-Hellman = Troca de chaves Diffie-Hellman estabelecida em curvas elípticas). Este protocolo é uma variante da troca de chaves Diffie-Hellman clássica.

Diffie-Hellman, em sua primeira versão, é um protocolo de acordo de chaves apresentado em 1976 que permite a duas pessoas, a partir de dois pares (chaves públicas e chaves privadas), determinar um segredo compartilhado trocando informações em um canal de comunicação não seguro.

![image](assets/11.webp)

Esse segredo compartilhado (a chave vermelha) pode então ser usado para realizar outras tarefas. Tipicamente, esse segredo compartilhado pode ser usado para criptografar e descriptografar uma comunicação em uma rede não segura:

![image](assets/12.webp)

Para ter sucesso nessa troca, Diffie-Hellman usa aritmética modular para calcular o segredo comum. Aqui está uma explicação simplificada de como funciona:

- Alice e Bob escolhem uma cor comum, aqui o amarelo. Essa cor é conhecida por todos. É um dado público.

- Alice escolhe uma cor secreta, aqui o vermelho. Ela mistura as duas cores, o que resulta em laranja.

- Bob escolhe uma cor secreta, aqui o azul pato. Ele mistura as duas cores, o que resulta em azul céu.

- Alice e Bob podem trocar as cores obtidas: laranja e azul céu. Essa troca pode ocorrer em uma rede não segura e ser observada por atacantes.

- Alice mistura a cor azul céu recebida de Bob com sua cor secreta (vermelho). Ela obtém marrom.

- Bob mistura a cor laranja recebida de Alice com sua cor secreta (azul pato). Ele também obtém a cor marrom.

![image](assets/13.webp)

> Crédito: Ideia original: A.J. Han VinckVersão vetorial: FlugaalTradução: Dereckson, Domínio público, via Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg

Nesta explicação simplificada, a cor marrom representa o segredo compartilhado entre Alice e Bob. É preciso imaginar que, na realidade, é impossível para o atacante separar as cores laranja e azul claro, a fim de descobrir os segredos de Alice ou Bob.

Agora, vamos estudar seu funcionamento real. À primeira vista, o Diffie-Hellman parece complexo de entender. Na realidade, o princípio de funcionamento é quase infantil. Antes de detalhar seus mecanismos, vou lembrar rapidamente de dois conceitos matemáticos que vamos precisar (e que, por sinal, também são usados em muitos outros métodos criptográficos).

1. Um número primo é um número natural que tem apenas dois divisores: 1 e ele mesmo. Por exemplo, o número 7 é primo, porque só pode ser dividido por 1 e 7 (ele mesmo). Por outro lado, o número 8 não é primo, porque pode ser dividido por 1, 2, 4 e 8. Portanto, ele não tem apenas dois divisores, mas sim quatro divisores inteiros e positivos.

2. O "módulo" (indicado por "mod" ou "%") é uma operação matemática que permite, entre dois números inteiros, retornar o resto da divisão euclidiana do primeiro pelo segundo número. Por exemplo, 16 mod 5 é igual a 1.

A troca de chaves Diffie-Hellman entre Alice e Bob funciona da seguinte maneira:

- Alice e Bob determinam dois números comuns: p e g. p é um número primo. Quanto maior esse número p, mais seguro será o Diffie-Hellman. g é uma raiz primitiva de p. Esses dois números podem ser comunicados em texto claro em uma rede não segura, são equivalentes à cor amarela na explicação acima. Apenas Alice e Bob precisam ter exatamente os mesmos valores de p e g.

- Depois de escolher os parâmetros, Alice e Bob determinam, cada um por si, um número aleatório secreto. O número aleatório obtido por Alice é chamado de a (equivalente à cor vermelha) e o número aleatório obtido por Bob é chamado de b (equivalente à cor azul-pato). Esses dois números devem permanecer em segredo.

- Em vez de trocar esses números a e b, cada parte vai calcular A (maiúsculo) e B (maiúsculo) da seguinte forma:

> A é igual a g elevado a a módulo p:
> A = g^a % p

> B é igual a g elevado a b módulo p:
> B = g^b % p

- Esses números A (equivalente à cor laranja) e B (equivalente à cor azul claro) serão trocados entre as duas partes. A troca pode ser feita em texto claro em uma rede não segura.

- Alice, que agora conhece B, vai calcular o valor de z da seguinte forma:

> z é igual a B elevado a a módulo p:
> z = B^a % p

- Como lembrete, B = g^b % p. Portanto:

  > z = B^a % p
  > z = (g^b)^a % p
  >
  > De acordo com as regras de cálculo de potências:
  >
  > (x^n)^m = x^nm
  >
  > Portanto:
  >
  > z = g^ba % p

- Bob, que agora tem conhecimento de A, também calculará o valor de z da seguinte forma:

> z é igual a A elevado a b modulo p:
>
> z = A^b % p
>
> Portanto:
>
> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Graças à distributividade do operador módulo, Alice e Bob encontram exatamente o mesmo valor de z. Esse número representa o segredo compartilhado entre eles, ou seja, o equivalente à cor marrom na explicação anterior. Eles podem usar esse segredo compartilhado para criptografar uma comunicação entre eles em uma rede não segura.

![Diagrama do funcionamento técnico do Diffie-Hellman](assets/14.webp)

Um atacante que possua p, g, A e B será incapaz de calcular a, b ou z. Fazer essa operação seria o mesmo que inverter a exponenciação. Esse cálculo é impossível de ser realizado de outra forma que não seja tentando todas as possibilidades uma por uma, já que estamos trabalhando em um corpo finito. Isso seria equivalente a calcular o logaritmo discreto, ou seja, a recíproca da exponenciação em um grupo cíclico finito.

Portanto, desde que escolhamos a, b e p suficientemente grandes, o Diffie-Hellman é seguro. Tipicamente, com parâmetros de 2.048 bits (um número com 600 dígitos em decimal), testar todas as possibilidades para a e b seria quimérico. Até o momento, com números desse tamanho, o algoritmo é considerado seguro.

É justamente nesse ponto que reside a principal desvantagem do protocolo Diffie-Hellman. Para ser seguro, o algoritmo deve usar números grandes. Como resultado, hoje em dia preferimos usar o algoritmo ECDH, uma variante do Diffie-Hellman que usa uma curva algébrica, especificamente uma curva elíptica. Isso nos permite trabalhar com números muito menores, mantendo uma segurança equivalente e, portanto, reduzindo os recursos necessários para o cálculo e o armazenamento.

O princípio geral do algoritmo permanece o mesmo. No entanto, em vez de usar um número aleatório a e um número A calculado a partir de a com exponenciação modular, usaremos um par de chaves estabelecidas em uma curva elíptica. Em vez de depender da distributividade do operador módulo, usaremos aqui a lei de grupo em curvas elípticas, mais especificamente a associatividade dessa lei.
Se você não tem nenhum conhecimento sobre como funcionam as chaves privadas e públicas em uma curva elíptica, vou explicar os conceitos básicos dessa metodologia nas seis primeiras partes deste artigo.

Resumidamente, uma chave privada é um número aleatório entre 1 e n-1 (sendo n a ordem da curva), e uma chave pública é um ponto único na curva determinado pela chave privada através da adição e duplicação de pontos a partir do ponto gerador, como:

> K = k·G

Onde K é a chave pública, k é a chave privada e G é o ponto gerador.

Uma das propriedades desse par de chaves é que é muito fácil determinar K conhecendo k e G, mas é atualmente impossível determinar k conhecendo K e G. É uma função unidirecional.

Em outras palavras, é fácil calcular a chave pública conhecendo a chave privada, mas é impossível calcular a chave privada conhecendo a chave pública. Essa segurança é baseada na impossibilidade de calcular o logaritmo discreto.

Vamos usar essa propriedade para adaptar nosso algoritmo Diffie-Hellman. Assim, o princípio de funcionamento do ECDH é o seguinte:

- Alice e Bob concordam em uma curva elíptica criptograficamente segura e seus parâmetros. Essas informações são públicas.

- Alice gera um número aleatório ka que será sua chave privada. Essa chave privada deve permanecer secreta. Ela determina sua chave pública Ka através da adição e duplicação de pontos na curva elíptica escolhida.

> Ka = ka·G

- Bob também gera um número aleatório que será sua chave privada kb. E ele calcula a chave pública associada Kb.

> Kb = kb·G

- Alice e Bob trocam suas chaves públicas Ka e Kb em uma rede pública não segura.

- Alice calcula um ponto (x,y) na curva aplicando sua chave privada ka à chave pública de Bob Kb.

> (x,y) = ka·Kb

- Bob calcula um ponto (x,y) na curva aplicando sua chave privada kb à chave pública de Alice Ka.

> (x,y) = kb·Ka

- Alice e Bob obtêm o mesmo ponto na curva elíptica. O segredo compartilhado será a abscissa x desse ponto.

Eles obtêm o mesmo segredo compartilhado porque:

> (x,y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

Um possível atacante que observa a rede pública não segura só pode obter as chaves públicas de cada um e os parâmetros da curva escolhida. Como explicado anteriormente, apenas essas duas informações não permitem determinar as chaves privadas, portanto, o atacante não pode acessar o segredo.
ECDH é um algoritmo que permite a troca de chaves. Frequentemente, ele é usado em conjunto com outros métodos criptográficos para definir um protocolo. Por exemplo, o ECDH é usado no coração do TLS (Transport Layer Security), um protocolo de criptografia e autenticação usado para a camada de transporte da internet. O TLS usa o ECDHE para a troca de chaves, uma variante do ECDH onde as chaves são efêmeras para fornecer confidencialidade persistente. Além disso, o TLS também usa um algoritmo de autenticação como o ECDSA, um algoritmo de criptografia como o AES e uma função de hash como o SHA256.

O TLS define o "s" em "https", bem como o pequeno cadeado que você vê no canto superior esquerdo do seu navegador, que garante a criptografia da comunicação. Portanto, você está usando o ECDH ao ler este artigo e provavelmente o usa diariamente sem perceber.

### A transação de notificação.

Como descobrimos na parte anterior, o ECDH é uma variante da troca de chaves Diffie-Hellman envolvendo pares de chaves estabelecidas em uma curva elíptica. Isso é conveniente, pois temos muitos pares de chaves que seguem esse padrão em nossas carteiras de Bitcoin!

A ideia é usar os pares de chaves das carteiras determinísticas hierárquicas do Bitcoin das duas partes envolvidas para estabelecer segredos compartilhados e efêmeros entre elas. Dentro do BIP47, usamos o ECDHE (Elliptic Curve Diffie-Hellman Ephemeral).

O ECDHE é usado pela primeira vez no BIP47 para transmitir o código de pagamento do remetente para o destinatário. Essa é a famosa transação de notificação. Na verdade, para que o BIP47 possa ser usado, é necessário que ambas as partes (o remetente que envia pagamentos e o destinatário que recebe pagamentos) estejam cientes do código de pagamento da outra parte. Isso será necessário para derivar as chaves públicas efêmeras e, portanto, os endereços de recebimento dedicados.

Antes dessa troca, o remetente já está ciente do código de pagamento do destinatário, pois ele pode tê-lo obtido off-chain, por exemplo, em seu site ou em suas redes sociais. No entanto, o destinatário não necessariamente está ciente do código de pagamento do remetente. Ele precisará recebê-lo, caso contrário, não poderá derivar suas chaves efêmeras e, portanto, não poderá saber onde estão seus bitcoins e desbloquear seus fundos. Poderíamos transmiti-lo off-chain, com outro sistema de comunicação, mas isso seria um problema em caso de recuperação da carteira a partir da semente.
De fato, como já mencionei, os endereços BIP47 não são derivados da semente do destinatário (caso contrário, seria melhor usar um dos seus xpub diretamente), mas são o resultado de um cálculo envolvendo os dois códigos de pagamento: o do destinatário e o do remetente. Portanto, se o destinatário perder sua carteira e tentar recuperá-la a partir da semente, ele precisará ter todos os códigos de pagamento das pessoas que lhe enviaram bitcoins via BIP47.

Seria possível usar o BIP47 sem essa transação de notificação, mas cada usuário teria que fazer backup dos códigos de pagamento de seus pares. Essa situação será difícil de gerenciar até que se encontre uma maneira simples e resiliente de realizar, armazenar e manter esses backups atualizados. Portanto, a transação de notificação é praticamente obrigatória no estado atual das coisas.

Além de sua função de backup dos códigos de pagamento, como o próprio nome sugere, essa transação também desempenha um papel de notificação para o destinatário. Ela informa ao cliente que um túnel acaba de ser aberto.

Antes de explicar em detalhes o funcionamento técnico da transação de notificação, gostaria de falar um pouco sobre o modelo de privacidade. De fato, o modelo do BIP47 justifica certas precauções tomadas ao construir essa transação inicial.

O código de pagamento em si não representa diretamente um risco de perda de privacidade. Ao contrário do modelo clássico do Bitcoin, que permite quebrar o fluxo de informações entre a identidade do usuário e as transações, mantendo as chaves públicas anônimas, o código de pagamento pode ser associado diretamente a uma identidade. Isso não é obrigatório, é claro, mas essa associação não é perigosa.

De fato, o código de pagamento não deriva diretamente os endereços usados para receber pagamentos BIP47. Em vez disso, os endereços são obtidos aplicando ECDHE entre chaves filhas dos códigos de pagamento das duas partes.

Portanto, um código de pagamento isolado não representa um risco direto de perda de privacidade, pois apenas o endereço de notificação é derivado dele. É possível obter algumas informações, mas normalmente não será possível saber com quem você está realizando transações.

Portanto, é essencial manter uma separação estrita entre os códigos de pagamento dos usuários. Com esse objetivo, a etapa de comunicação inicial do código é um momento crítico para a privacidade do pagamento, e ainda é obrigatória para o bom funcionamento do protocolo. Se um dos códigos de pagamento puder ser recuperado publicamente (por exemplo, em um site), o segundo código, ou seja, o do remetente, não deve ser associado ao primeiro.

Por exemplo, vamos imaginar que eu queira fazer uma doação com BIP47 para um movimento de protesto pacífico no Canadá:

- Essa organização publicou seu código de pagamento diretamente em seu site ou em suas redes sociais.
- Esse código está associado ao movimento.
- Eu recupero esse código de pagamento.
- Antes de poder enviar uma transação para eles, eu preciso garantir que eles estejam cientes do meu código de pagamento pessoal, que também está associado à minha identidade, já que eu o uso para receber transações das minhas redes sociais.
- Como posso transmitir isso para eles? Se eu enviar usando um meio de comunicação convencional, a informação pode vazar e eu posso ser marcado como uma pessoa que apoia movimentos pacíficos.
- A transação de notificação não é a única solução para transmitir o código de pagamento do remetente secretamente, mas por enquanto ela desempenha perfeitamente esse papel aplicando várias camadas de segurança.
- No esquema abaixo, as linhas vermelhas representam o momento em que o fluxo de informação deve ser interrompido, e as setas pretas representam os links inegáveis que podem ser feitos por um observador externo:
- Na realidade, para o modelo de privacidade clássico do Bitcoin, muitas vezes é difícil interromper completamente o fluxo de informação entre o par de chaves e o usuário, especialmente ao realizar transações à distância. Por exemplo, no caso de uma campanha de doação, o destinatário será obrigado a revelar um endereço ou chave pública em seu site ou redes sociais. O uso adequado do BIP47, ou seja, com a transação de notificação, resolve isso através do ECDHE e da camada de criptografia que vamos estudar.
- Obviamente, o modelo de privacidade clássico do Bitcoin ainda é observado no nível das chaves públicas efêmeras derivadas da associação dos dois códigos de pagamento. Os dois modelos são interdependentes. Eu só quero destacar aqui que, ao contrário do uso convencional de uma chave pública para receber bitcoins, o código de pagamento pode ser associado a uma identidade, porque a informação "Bob faz uma transação com Alice" é interrompida em outro momento. O código de pagamento é usado para gerar os endereços de pagamento, mas observando apenas o blockchain, é impossível associar uma transação de pagamento BIP47 aos códigos de pagamento usados para realizá-la.

### Construção da transação de notificação.

Agora, vamos ver como funciona essa transação de notificação. Vamos supor que Alice queira enviar fundos para Bob com o BIP47. No meu exemplo, Alice age como remetente e Bob como destinatário. Este último publicou seu código de pagamento em seu site. Alice já está ciente do código de pagamento de Bob.

1. Alice calcula um segredo compartilhado com ECDH:

- Ela seleciona um par de chaves de sua carteira HD que está em um ramo diferente de seu código de pagamento. Atenção, esse par não deve ser facilmente associado ao endereço de notificação de Alice, nem à identidade de Alice (ver parte anterior).
- Alice seleciona a chave privada desse par. Chamamos de "a" (minúsculo).

> a

- Alice recupera a chave pública associada ao endereço de notificação de Bob. Essa chave é a primeira filha derivada do código de pagamento de Bob (índice 0). Chamamos essa chave pública de "B" (maiúsculo). A chave privada associada a essa chave pública é chamada de "b" (minúsculo). "B" é determinado pela adição e duplicação de pontos na curva elíptica a partir de "G" (o ponto gerador) com "b" (a chave privada).

> B = b·G

- Alice calcula um ponto secreto "S" (maiúsculo) na curva elíptica através da adição e duplicação de pontos aplicando sua chave privada "a" à chave pública de Bob "B".

> S = a·B

- Alice calcula o fator de cegamento "f" que será usado para criptografar seu código de pagamento. Para isso, ela gera um número pseudoaleatório usando a função HMAC-SHA512. Como segunda entrada dessa função, ela usa um valor que apenas Bob será capaz de encontrar: (x), que é a abscissa do ponto secreto calculado anteriormente. A primeira entrada é (o), que é a UTXO consumida como entrada dessa transação (outpoint).

> f = HMAC-SHA512(o, x)

2. Alice converte seu código de pagamento pessoal para base 2 (binário).

3. Ela usa esse fator de cegamento como chave para realizar uma criptografia simétrica na carga útil de seu código de pagamento. O algoritmo de criptografia usado é simplesmente um XOR. A operação realizada é semelhante ao cifra de Vernam, também conhecida como "máscara descartável" (em inglês: "One-Time Pad"):

- Alice separa inicialmente seu fator de cegamento em dois: os primeiros 32 bytes são chamados de "f1" e os últimos 32 bytes são chamados de "f2". Temos então:

> f = f1 || f2

- Alice calcula o texto cifrado (x') da abscissa da chave pública (x) de seu código de pagamento e o texto cifrado (c') de seu código de cadeia (c) separadamente. "f1" e "f2" atuam como chaves de criptografia. A operação usada é o XOR (ou exclusivo).

> x' = x XOR f1
>
> c>' = c XOR f2

- Alice substitui os valores reais da abscissa da chave pública (x) e do código de cadeia (c) em seu código de pagamento pelos valores criptografados (x') e (c').

Antes de continuar a descrição técnica desta transação de notificação, vamos nos deter por um momento nesta operação XOR. XOR é um operador lógico de nível de bits baseado na álgebra de Boole. A partir de dois operandos em bits, ele retorna 1 se os bits na mesma posição forem diferentes e retorna 0 se os bits na mesma posição forem iguais. Aqui está a tabela verdade do XOR em função dos valores dos operandos D e E:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Por exemplo:

> 0110 XOR 1110 = 1000

Ou ainda:

> 010011 XOR 110110 = 100101

Com ECDH, o uso do XOR como camada de criptografia é particularmente coerente. Primeiro, graças a esse operador, a criptografia é simétrica. Isso permitirá que o destinatário descriptografe o código de pagamento com a mesma chave que foi usada para criptografá-lo. A chave de criptografia e descriptografia é calculada a partir do segredo compartilhado por meio do ECDH.

Essa simetria é permitida pelas propriedades de comutatividade e associatividade do operador XOR:

- Outras propriedades:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Comutatividade:
  D ⊕ E = E ⊕ D

- Associatividade:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Simetria:
  Se: D ⊕ E = L
  Então: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
  Em seguida, este método de criptografia se assemelha muito ao cifra de Vernam (One-Time Pad), o único algoritmo de criptografia conhecido até hoje que possui segurança incondicional (ou absoluta). Para que o cifra de Vernam tenha essa característica, a chave de criptografia deve ser perfeitamente aleatória, ter o mesmo tamanho da mensagem e ser usada apenas uma vez. No método de criptografia usado aqui para o BIP47, a chave tem o mesmo tamanho da mensagem, o fator cegante tem exatamente o mesmo tamanho da concatenação da abscissa da chave pública com o código de cadeia do código de pagamento. Essa chave de criptografia é usada apenas uma vez. No entanto, essa chave não é gerada a partir de uma aleatoriedade perfeita, pois é um HMAC. É mais pseudo-aleatória. Portanto, não é um cifra de Vernam, mas o método se aproxima disso.
  Vamos voltar para a construção da transação de notificação:

4. Alice agora tem seu código de pagamento com uma carga útil criptografada. Ela vai construir e transmitir uma transação envolvendo sua chave pública "A" como entrada, uma saída para o endereço de notificação de Bob e uma saída OP_RETURN composta por seu código de pagamento com a carga útil criptografada. Essa transação é a transação de notificação.

OP_RETURN é um Opcode, ou seja, um script, que permite marcar uma saída de transação Bitcoin como inválida. Hoje, é usado para transmitir ou ancorar informações na blockchain do Bitcoin. Até 80 bytes de dados podem ser armazenados lá, que são registrados na cadeia e, portanto, visíveis para todos os outros usuários.

Como vimos na parte anterior, o Diffie-Hellman é usado para gerar um segredo compartilhado entre dois usuários que se comunicam em uma rede não segura e potencialmente observada por atacantes. No BIP47, o ECDH é usado para poder se comunicar na rede Bitcoin, que por natureza é uma rede de comunicação transparente e observada por muitos atacantes. O segredo compartilhado calculado por meio da troca de chaves Diffie-Hellman na curva elíptica é então usado para criptografar a informação secreta a ser transmitida: o código de pagamento do remetente (Alice).

Aqui está um diagrama extraído do BIP47 que ilustra o que acabamos de descrever:

![Diagrama Alice envia seu código de pagamento mascarado para o endereço de notificação de Bob](assets/16.webp)

Crédito: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Se correspondermos esse diagrama ao que descrevi anteriormente:

- "Wallet Priv-Key" do lado de Alice corresponde a: a.

- "Child Pub-Key 0" do lado de Bob corresponde a: B.
- "Notification Shared Secret" corresponde a: f.
- "Masked Payment Code" corresponde ao código de pagamento mascarado, ou seja, com a carga útil criptografada: x' e c'.

- "Notification Transaction" é a transação que contém o OP_RETURN.

Vou resumir as etapas que acabamos de ver juntos para realizar uma transação de notificação:

- Alice obtém o código de pagamento e o endereço de notificação de Bob.

- Alice seleciona uma UTXO que lhe pertence em sua carteira HD com o par de chaves correspondente.

- Ela calcula um ponto secreto na curva elíptica usando ECDH.

- Ela usa esse ponto secreto para calcular um HMAC que é o fator de cegamento.

- Ela usa esse fator de cegamento para criptografar a carga útil de seu código de pagamento pessoal.

- Ela usa uma saída de transação OP_RETURN para transferir o código de pagamento mascarado para Bob.

Para entender mais detalhadamente como funciona, especialmente o uso do OP_RETURN, vamos estudar juntos uma transação de notificação real. Eu fiz uma transação desse tipo na Testnet, que você pode encontrar clicando aqui:

https://mempool.space/fr/testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e

TXID:

> 0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e

![Transação de notificação BIP47](assets/17.webp)

Crédito: https://blockstream.info/

Ao observar essa transação, já podemos ver que ela possui apenas uma entrada e 4 saídas:

- A primeira saída é o OP_RETURN que contém meu código de pagamento mascarado.

- A segunda saída de 546 sats aponta para o endereço de notificação do meu destinatário.

- A terceira saída de 15.000 sats representa as taxas de serviço, pois usei a carteira Samourai para construir essa transação.

- A quarta saída de dois milhões de sats representa o troco, ou seja, a diferença restante da minha entrada que retorna para outro endereço meu.

O mais interessante de estudar é obviamente a saída 0 usando o OP_RETURN. Vamos dar uma olhada mais detalhada no que ela contém:

![Saída OP_RETURN da transação de notificação BIP47](assets/18.webp)

Crédito: https://blockstream.info/

Nele, descobrimos o script da saída em hexadecimal:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

Nesse script, podemos analisar várias partes:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000>
> Os opcodes:
>
> 6a4c
>
> Um byte que indica o tamanho da carga útil (80 bytes):
>
> 50
>
> Os metadados do meu código de pagamento em texto claro:
>
> 010002
>
> A coordenada x criptografada da chave pública do meu código de pagamento:
>
> b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164
>
> O código de cadeia criptografado do meu código de pagamento:
> 927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d8
>
> Preenchimento para chegar a 80 bytes:
> 00000000000000000000000000

Entre os opcodes, podemos reconhecer 0x6a, que representa o OP_RETURN, e 0x4c, que representa o OP_PUSHDATA1. O byte seguinte a este último opcode indica o tamanho da carga útil que segue. Ele indica 0x50, ou seja, 80 bytes.

Em seguida, vem o código de pagamento com a carga útil criptografada.

Aqui está o meu código de pagamento em texto claro usado nesta transação:

> Em base 58:
>
> PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
>
> Em base 16 (HEX):
> 4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Se compararmos meu código de pagamento em texto claro com o OP_RETURN, podemos ver que o HRP (em marrom) e o checksum (em rosa) não são transmitidos. Isso é normal, essas informações são destinadas aos humanos.
Em seguida, podemos reconhecer (em verde) a versão (0x01), o campo de bits (0x00) e a paridade da chave pública (0x02). E, no final do código de pagamento, os bytes vazios em preto (0x00) que são usados para preencher até um total de 80 bytes. Todos esses metadados são transmitidos em texto claro (não criptografados).
Por fim, podemos observar que a abscissa da chave pública (em azul) e o código de cadeia (em vermelho) foram criptografados. Isso constitui a carga útil do código de pagamento.

### Recebendo a transação de notificação.

Agora que Alice enviou a transação de notificação para Bob, vamos ver como ele a interpreta.

Como lembrete, Bob deve obrigatoriamente ter acesso ao código de pagamento de Alice. Sem essa informação, como veremos na próxima parte, ele não poderá derivar os pares de chaves criados por Alice e, portanto, não poderá acessar seus bitcoins recebidos com o BIP47. Por enquanto, a carga útil do código de pagamento de Alice está criptografada. Vamos ver juntos como Bob a descriptografa.

1. Bob monitora as transações que criam saídas com seu endereço de notificação.

2. Quando uma transação tem uma saída em seu endereço de notificação, Bob a analisa para ver se ela contém uma saída OP_RETURN que segue o padrão BIP47.

3. Se o primeiro byte da carga útil do OP_RETURN for 0x01, Bob inicia sua busca por um possível segredo compartilhado com ECDH:

- Bob seleciona a chave pública de entrada da transação. Ou seja, a chave pública de Alice chamada "A" com:

> A = a·G

- Bob seleciona a chave privada "b" associada ao seu próprio endereço de notificação:

> b

- Bob calcula o ponto secreto "S" (segredo compartilhado ECDH) na curva elíptica através da adição e duplicação de pontos, aplicando sua chave privada "b" à chave pública de Alice "A":

> S = b·A

- Bob determina o fator de cegamento "f" que permitirá descriptografar a carga útil do código de pagamento de Alice. Da mesma forma que Alice calculou anteriormente, Bob encontrará "f" aplicando HMAC-SHA512 em (x) o valor da abscissa do ponto secreto "S" e em (o) o UTXO consumido como entrada dessa transação de notificação:

> f = HMAC-SHA512(o, x)

4. Bob interpreta os dados do OP_RETURN na transação de notificação como um código de pagamento. Ele simplesmente descriptografa a carga útil desse potencial código de pagamento usando o fator de cegamento "f":

- Bob divide o fator cegante "f" em duas partes: os primeiros 32 bytes de "f" serão "f1" e os últimos 32 bytes serão "f2".
- Bob descriptografa o valor da abscissa criptografada (x') da chave pública do código de pagamento de Alice:

> x = x' XOR f1

- Bob descriptografa o valor do código de cadeia criptografado (c') do código de pagamento de Alice:

> c = c' XOR f2

5. Bob verifica se o valor da chave pública do código de pagamento de Alice faz parte do grupo secp256k1. Se for o caso, ele interpreta isso como um código de pagamento válido. Caso contrário, ele ignora essa transação.

Agora que Bob conhece o código de pagamento de Alice, ela pode enviar até 2^32 pagamentos para ele, sem nunca mais precisar fazer uma transação de notificação desse tipo.

Por que isso funciona? Como Bob consegue determinar o mesmo fator cegante que Alice e, portanto, descriptografar seu código de pagamento? Vamos analisar mais detalhadamente a ação do ECDH no que acabamos de descrever.

Primeiro, estamos lidando com uma criptografia simétrica. Isso significa que a chave de criptografia e a chave de descriptografia são o mesmo valor. Essa chave na transação de notificação é o fator cegante (f = f1 || f2). Portanto, Alice e Bob precisam obter o mesmo valor para f, sem transmiti-lo diretamente, pois um atacante poderia roubá-lo e descriptografar a informação secreta.

Esse fator cegante é obtido aplicando HMAC-SHA512 a dois valores: a abscissa de um ponto secreto e o UTXO consumido como entrada na transação. Portanto, Bob precisa ter essas duas informações para descriptografar a carga útil do código de pagamento de Alice.

Para o UTXO de entrada, Bob pode simplesmente recuperá-lo observando a transação de notificação. Para o ponto secreto, Bob terá que usar o ECDH.

Como visto na parte sobre Diffie-Hellman, simplesmente trocando suas respectivas chaves públicas e aplicando secretamente suas chaves privadas à chave pública do outro, Alice e Bob podem encontrar um ponto preciso e secreto na curva elíptica. A transação de notificação se baseia nesse mecanismo:

> O par de chaves de Bob:
>
> B = b·G
>
> O par de chaves de Alice:
>
> A = a·G
>
> Para um ponto secreto S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Diagrama de geração de um segredo compartilhado com ECDHE](assets/19.webp)
Agora que Bob conhece o código de pagamento de Alice, ele será capaz de detectar os pagamentos BIP47 dela e poderá derivar as chaves privadas bloqueando os bitcoins recebidos.
![Bob interpreta a transação de notificação de Alice](assets/20.webp)

Crédito: Códigos de Pagamento Reutilizáveis para Carteiras Determinísticas Hierárquicas, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Se correspondermos esse esquema ao que eu descrevi anteriormente:

- "Wallet Pub-Key" do lado de Alice corresponde a: A.

- "Child Priv-Key 0" do lado de Bob corresponde a: b.

- "Notification Shared Secret" corresponde a: f.

- "Masked Payment Code" corresponde ao código de pagamento de Alice mascarado, ou seja, com a carga útil criptografada: x' e c'.

- "Notification Transaction" é a transação que contém o OP_RETURN.

Vou recapitular as etapas que acabamos de ver juntos para receber e interpretar uma transação de notificação:

- Bob monitora as saídas de transação para seu endereço de notificação.

- Quando ele detecta uma, ele recupera as informações contidas no OP_RETURN.

- Bob seleciona a chave pública de entrada e calcula um ponto secreto usando ECDH.

- Ele usa esse ponto secreto para calcular um HMAC que é o fator de cegamento.

- Ele usa esse fator de cegamento para descriptografar a carga útil do código de pagamento de Alice contido no OP_RETURN.

### A transação de pagamento BIP47.

Agora vamos estudar juntos o processo de pagamento com BIP47. Para lembrar o estado atual da situação:

- Alice conhece o código de pagamento de Bob que ela simplesmente recuperou em seu site.

- Bob conhece o código de pagamento de Alice através da transação de notificação.

- Alice fará um primeiro pagamento para Bob. Ela poderá fazer muitos outros da mesma maneira.

Antes de explicar esse processo, acho importante lembrar em quais índices estamos trabalhando atualmente:

Descrevemos o caminho de derivação de um código de pagamento da seguinte forma: m/47'/0'/0'/.

A próxima profundidade distribui os índices da seguinte maneira:

- O primeiro par de filhos normais (não reforçados) é usado para gerar o endereço de notificação que discutimos na parte anterior: m/47'/0'/0'/0/.

- Os pares de chaves filhas normais são usados dentro do ECDH para gerar endereços de recebimento de pagamento BIP47, como veremos nesta parte: m/47'/0'/0'/ de 0 a 2.147.483.647/.

- Os pares de chaves filhas reforçadas são códigos de pagamento efêmeros: m/47'/0'/0'/ de 0' a 2.147.483.647'/.
  Sempre que Alice deseja enviar um pagamento para Bob, ela deriva um novo endereço único em branco, mais uma vez usando o protocolo ECDH:
- Alice seleciona a primeira chave privada derivada do seu código de pagamento reutilizável pessoal:

> a

- Alice seleciona a primeira chave pública não utilizada derivada do código de pagamento de Bob. Chamaremos essa chave pública de "B". Ela está associada à chave privada "b", que apenas Bob conhece.

> B = b·G

- Alice calcula um ponto secreto "S" na curva elíptica através da adição e duplicação de pontos, aplicando sua chave privada "a" à chave pública de Bob "B":

> S = a·B

- A partir desse ponto secreto, Alice calcula o segredo compartilhado "s" (minúsculo). Para fazer isso, ela seleciona a abscissa do ponto secreto "S", chamada de "Sx", e passa esse valor pela função de hash SHA256.

> s = SHA256(Sx)

Não confie. Verifique! Se você deseja entender os princípios básicos de uma função de hash, encontrará informações úteis neste artigo. E se você não confia no NIST (você está certo) e deseja entender em detalhes como o SHA256 funciona, eu explico tudo neste artigo em francês.

- Alice usa esse segredo compartilhado "s" para calcular um endereço de recebimento de pagamento Bitcoin. Primeiro, ela verifica se "s" está contido na ordem da curva secp256k1. Se não estiver, ela incrementa o índice da chave pública de Bob para derivar outro segredo compartilhado.

- Em seguida, ela calcula uma chave pública "K0" adicionando os pontos "B" e "s·G" na curva elíptica. Em outras palavras, Alice adiciona a chave pública derivada do código de pagamento de Bob "B" a outro ponto calculado na curva elíptica por adição e duplicação de pontos com o segredo compartilhado "s" a partir do ponto gerador da curva secp256k1 "G". Esse novo ponto representa uma chave pública e o chamamos de "K0":

> K0 = B + s·G

- Com essa chave pública "K0", Alice pode derivar um endereço de recebimento em branco de forma padrão (por exemplo, SegWit V0 em Bech32).

Depois de obter esse endereço de recebimento "K0" pertencente a Bob, Alice pode construir uma transação Bitcoin comum, selecionando uma UTXO que ela possui em outro ramo de sua carteira HD e gastando para o endereço "K0" de Bob.

![Alice envia bitcoins com BIP47 para Bob](assets/21.webp)

Crédito: Códigos de Pagamento Reutilizáveis para Carteiras Determinísticas Hierárquicas, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Se correspondermos esse esquema com o que eu descrevi anteriormente:

- "Child Priv-Key" do lado da Alice corresponde a: a.

- "Child Pub-Key 0" do lado do Bob corresponde a: B.

- "Payment Secret 0" corresponde a: s.

- "Payment Pub-Key 0" corresponde a: K0.

Vou recapitular as etapas que acabamos de ver juntos para enviar um pagamento BIP47:

- Alice seleciona a primeira chave privada filha derivada do seu código de pagamento pessoal.

- Ela calcula um ponto secreto na curva elíptica usando ECDH a partir da primeira chave pública filha não utilizada derivada do código de pagamento do Bob.

- Ela usa esse ponto secreto para calcular um segredo compartilhado com SHA256.

- Ela usa esse segredo compartilhado para calcular um novo ponto secreto na curva elíptica.

- Ela adiciona esse novo ponto secreto à chave pública do Bob.

- Ela obtém uma nova chave pública efêmera para a qual apenas o Bob possui a chave privada associada.

- Alice pode enviar uma transação comum para o Bob com o endereço de recebimento derivado efêmero.

Se ela quiser fazer um segundo pagamento, ela repetirá as etapas acima, exceto que ela selecionará a segunda chave pública derivada do código de pagamento do Bob. Ou seja, a próxima chave não utilizada. Ela terá então um segundo endereço de recebimento pertencente ao Bob "K1".

![Alice deriva três endereços de recebimento BIP47 para Bob](assets/22.webp)

Crédito: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Ela pode continuar assim e derivar até 2^32 endereços em branco pertencentes ao Bob.

Do ponto de vista externo, ao observar o blockchain do Bitcoin, teoricamente é impossível diferenciar um pagamento BIP47 de um pagamento comum. Aqui está um exemplo de uma transação de pagamento BIP47 no Testnet:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Isso se parece com uma transação comum com uma entrada consumida, uma saída de pagamento de 210.000 sats e um troco:

![Transação de pagamento Bitcoin com BIP47](assets/23.webp)

Crédito: https://blockstream.info/

### Recebendo o pagamento BIP47 e derivando a chave privada.

Alice acabou de fazer seu primeiro pagamento para um endereço BIP47 vazio pertencente a Bob. Agora vamos ver juntos como Bob recebe esse pagamento. Também veremos por que Alice não tem acesso à chave privada do endereço que ela acabou de gerar e como Bob encontra essa chave para gastar os bitcoins que ele acabou de receber.

Assim que Bob recebe a transação de notificação de Alice, ele deriva a chave pública BIP47 "K0" antes mesmo de ela enviar qualquer pagamento para lá. Ele, portanto, observa qualquer pagamento para o endereço associado. Na verdade, ele até deriva imediatamente várias chaves que ele vai observar (K0, K1, K2, K3...). Aqui está como ele deriva essa chave pública "K0":

- Bob seleciona a primeira chave privada filha derivada de seu código de pagamento. Essa chave privada é chamada de "b". Ela está associada à chave pública "B" com a qual Alice fez seus cálculos na etapa anterior:

> b

- Bob seleciona a primeira chave pública de Alice derivada de seu código de pagamento. Essa chave é chamada de "A". Ela está associada à chave privada "a" com a qual Alice fez seus cálculos e que apenas Alice conhece. Bob pode realizar esse processo porque ele tem conhecimento do código de pagamento de Alice que lhe foi transmitido com a transação de notificação.

> A = a·G

- Bob calcula o ponto secreto "S", adicionando e dobrando pontos na curva elíptica, aplicando sua chave privada "b" à chave pública de Alice "A". Aqui, usamos o ECDH, que nos garante que esse ponto "S" será o mesmo para Bob e para Alice.

> S = b·A

- Da mesma forma que Alice fez, Bob isola a abscissa desse ponto "S". Chamamos esse valor de "Sx". Ele passa esse valor pela função SHA256 para encontrar o segredo compartilhado "s" (minúsculo).

> s = SHA256(Sx)

- Ainda da mesma forma que Alice, Bob calcula o ponto "s·G" na curva elíptica. Em seguida, ele adiciona esse ponto secreto à sua chave pública "B". Ele obtém então um novo ponto na curva elíptica que ele interpreta como uma chave pública "K0":

> K0 = B + s·G

Depois que Bob tem essa chave pública "K0", ele pode derivar a chave privada associada para poder gastar seus bitcoins. Ele é o único que pode gerar esse número.

- Bob adiciona sua chave privada filha "b" derivada de seu código de pagamento pessoal. Ele é o único que pode obter o valor de "b". Em seguida, ele adiciona "b" ao segredo compartilhado "s" para obter k0, a chave privada de K0:

> k0 = b + s
> Graças à lei de grupo da curva elíptica, Bob obtém exatamente a chave privada correspondente à chave pública utilizada por Alice. Portanto, temos:
> K0 = k0·G

![Bob gera seus endereços de recebimento BIP47](assets/24.webp)

Crédito: Códigos de Pagamento Reutilizáveis para Carteiras Determinísticas Hierárquicas, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Se relacionarmos esse esquema com o que eu descrevi anteriormente:

- "Child Priv-Key 0" do lado de Bob corresponde a: b.

- "Child Pub-Key 0" do lado de Alice corresponde a: A.

- "Payment Secret 0" corresponde a: s.

- "Payment Pub-Key 0" corresponde a: K0.

- "Payment Priv-Key 0" corresponde a: k0.

Vou recapitular as etapas que acabamos de ver juntos para receber um pagamento BIP47 e calcular a chave privada correspondente:

- Bob seleciona a primeira chave privada filha derivada de seu código de pagamento pessoal.

- Ele calcula um ponto secreto na curva elíptica usando ECDH a partir da primeira chave pública filha derivada do código de cadeia de Alice.

- Ele usa esse ponto secreto para calcular um segredo compartilhado com SHA256.

- Ele usa esse segredo compartilhado para calcular um novo ponto secreto na curva elíptica.

- Ele adiciona esse novo ponto secreto à sua chave pública pessoal.

- Ele obtém uma nova chave pública efêmera, para a qual Alice enviará seu primeiro pagamento.

- Bob calcula a chave privada associada a essa chave pública efêmera adicionando sua chave privada filha derivada de seu código de pagamento e o segredo compartilhado.

Como Alice não pode obter "b", a chave privada de Bob, ela é incapaz de determinar k0, a chave privada associada ao endereço de recebimento BIP47 de Bob.

Esquematicamente, podemos representar o cálculo do segredo compartilhado "S" da seguinte forma:

![Cálculo do segredo compartilhado com ECDHE](assets/25.webp)

Depois de encontrar o segredo compartilhado com ECDH, Alice e Bob calculam a chave pública de pagamento BIP47 "K0", e Bob também calcula a chave privada associada "k0":

![Derivação do endereço de recebimento BIP47 a partir do segredo compartilhado](assets/26.webp)

### Reembolso do pagamento BIP47.

Como Bob conhece o código de pagamento reutilizável de Alice, ele já possui todas as informações necessárias para enviar um reembolso a ela. Ele não precisará entrar em contato com Alice para solicitar qualquer informação. Ele apenas precisa notificá-la com uma transação de notificação, especialmente para que ela possa recuperar seus endereços BIP47 com sua semente, e então ele também pode enviar até 2^32 pagamentos para ela.
Bob pode então reembolsar Alice da mesma forma que ela enviou os pagamentos para ele. Os papéis se invertem:

![Bob envia um reembolso para Alice com o BIP47](assets/27.webp)

Crédito: Códigos de Pagamento Reutilizáveis para Carteiras Determinísticas Hierárquicas, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Agora você conhece todos os detalhes dessa maravilhosa solução que é o BIP47.

## Usos derivados do PayNym.

A implementação do BIP47 no Samourai Wallet resultou no PayNym, que são identificadores calculados a partir dos códigos de pagamento dos usuários. Hoje em dia, sua utilidade vai muito além do uso do BIP47.

A equipe do Samourai está gradualmente desenvolvendo todo um ecossistema de ferramentas e serviços baseados no PayNym do usuário. Entre eles, estão, é claro, todas as ferramentas de gastos que permitem otimizar a privacidade do usuário adicionando entropia a uma transação, e assim, adicionando negação plausível.

O uso conjunto do Soroban, a rede de comunicação criptografada baseada no Tor, e do PayNym tem sido fundamental para otimizar a experiência do usuário na construção de transações colaborativas, mantendo um bom nível de segurança. Assim, é possível realizar facilmente transações Stowaway (PayJoin) e StonewallX2 sem precisar realizar manualmente as várias trocas de transações não assinadas necessárias para configurar uma transação colaborativa desse tipo.

Ao contrário do uso do BIP47, uma vez que essas transações colaborativas não exigem uma transação de notificação, basta vincular os PayNyms para usar essas ferramentas. Não é necessário conectá-los.

Se você quiser saber mais sobre transações colaborativas e, mais amplamente, sobre todas as ferramentas de gastos do Samourai Wallet, você pode ler a seção "Ferramentas de Gastos" neste artigo. Lá você encontrará uma explicação técnica e um tutorial detalhado para cada ferramenta.

Além dessas transações colaborativas, recentemente foi observado que a equipe do Samourai está trabalhando em um protocolo de autenticação relacionado ao PayNym: Auth47. Essa ferramenta já está implementada e permite, por exemplo, autenticar-se em um site que aceita esse método usando um PayNym. No futuro, acredito que além dessa possibilidade de autenticação na web, o Auth47 fará parte de um projeto mais amplo em torno do ecossistema BIP47/PayNym/Samourai. Talvez esse protocolo seja usado para otimizar ainda mais a experiência do usuário na carteira Samourai Wallet, especialmente no uso das ferramentas de gastos. Fique de olho...

## Minha opinião pessoal sobre o BIP47.

Obviamente, a principal desvantagem do BIP47 é a transação de notificação. Isso leva o usuário a ter que pagar taxas para minerá-la, o que pode ser inconveniente para alguns. Por outro lado, o argumento de "spam" na blockchain do Bitcoin é absolutamente inaceitável. Qualquer pessoa que pague as taxas para sua transação deve ser capaz de registrá-la no registro, não importa qual seja o objetivo. Afirmar o contrário é se posicionar a favor da censura.
É possível que no futuro sejam encontradas outras soluções menos custosas para comunicar o código de pagamento do remetente ao destinatário e para que este possa armazená-lo com segurança. Mas, por enquanto, a transação de notificação continua sendo a solução com menos compromissos.
Essa desvantagem é insignificante quando se observam todos os benefícios do BIP47. Entre todas as propostas existentes para resolver esse problema de reutilização de endereço, ele me parece a melhor solução.
Como explicado anteriormente, a maioria das reutilizações de endereço vem das exchanges. O BIP47 é a única solução razoável que realmente resolve esse problema na fonte. Qualquer proposta para reduzir o número de reutilizações de endereço deve abordar esse aspecto e adaptar a solução à fonte principal do problema.
Em termos de uso, embora seus mecanismos sejam bastante complexos, o procedimento de pagamento do BIP47 é simples. Os códigos de pagamento reutilizáveis podem ser facilmente adotados, mesmo por usuários inexperientes.
Em termos de privacidade, o BIP47 é muito interessante. Como expliquei na parte sobre a transação de notificação, o código de pagamento não revela nenhuma informação sobre os endereços efêmeros derivados. Isso permite interromper o fluxo de informações entre a transação do Bitcoin e o identificador do destinatário, ao contrário do uso tradicional de um endereço de recebimento.
E, acima de tudo, a implementação PayNym do BIP47 funciona! Está disponível no Samourai Wallet desde 2016 e no Sparrow Wallet desde o início deste ano. Não é um projeto científico, mas uma solução testada ontem e completamente funcional hoje.
Esperamos que no futuro esses códigos de pagamento reutilizáveis sejam adotados pelos atores do ecossistema, implementados em softwares de carteira e usados pelos usuários de Bitcoin.
Qualquer solução verdadeiramente positiva para a privacidade do usuário deve ser discutida, impulsionada e defendida, para que o Bitcoin não se torne o playground das autoridades centrais e a ferramenta de vigilância dos governos.

> Ele pensava na maneira como havia sido perseguido e insultado em todos os lugares, e agora ouvia todos dizerem que ele era o mais bonito de todos aqueles belos pássaros! E até mesmo o sabugueiro inclinava seus galhos para ele, e o sol espalhava uma luz tão quente e benéfica! Então suas penas se encheram, seu pescoço elegante se ergueu, e ele exclamou de todo o coração: "Como pude sonhar com tanta felicidade quando eu era apenas um patinho feio."

## Para ir mais longe:

- Compreender e usar o CoinJoin no Bitcoin.

- Compreender os caminhos de derivação de uma carteira Bitcoin.

- Instalar e usar seu próprio nó Bitcoin RoninDojo.

### Recursos externos e agradecimentos:

Agradecimentos a LaurentMT e Théo Pantamis pelos muitos conceitos que eles me explicaram e que utilizei neste artigo. Espero ter conseguido transmiti-los com precisão.

Agradecimentos a Fanis Michalakis pela revisão deste texto e seus conselhos de especialista.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols
