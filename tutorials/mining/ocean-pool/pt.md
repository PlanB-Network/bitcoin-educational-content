---
name: Ocean Mining
description: Introdução à Mineração Oceânica
---

![signup](assets/cover.webp)

**Maio de 2024**

A Mineração Oceânica é um pool de mineração um tanto único. Aqui, não são necessárias contas, endereços de e-mail, nem senhas. Assim como o Bitcoin, tudo é transparente, pseudônimo, e os contribuidores podem escolher entre quatro diferentes modelos de blocos.

### Sistema de Compensação

O sistema de compensação da Oceânica é chamado TIDES, "Índice Transparente de Participações Distintas e Ampliadas". Esse sistema registra o trabalho fornecido pelos mineradores, conhecido como "participações". O pool calcula a porcentagem de "participações" para cada contribuidor, depois adiciona o endereço Bitcoin deles no modelo de bloco do pool como beneficiário dessa porcentagem da recompensa do bloco.

O modelo de bloco é atualizado aproximadamente a cada 10 segundos para levar em conta as novas transações mais lucrativas e para mudar a distribuição da recompensa do bloco, se necessário.

![signup](assets/rem.webp)

Não importa se suas máquinas estão conectadas ou não no momento em que o pool mina um novo bloco. O trabalho já enviado é mantido para os próximos oito blocos encontrados pelo pool.

Manter o trabalho por oito blocos, em vez de zerar os contadores a cada novo bloco minerado, significa que sua compensação só será 100% uma vez que o pool tenha encontrado oito blocos depois que você começou a contribuir. Isso também significa que você continuará sendo compensado por oito blocos se parar de contribuir para o pool.

Este mecanismo suaviza a compensação e desencoraja o "pool hopping", que envolve trocar de pools regularmente dependendo de qual deles tem mais chances de encontrar o próximo bloco.

### Saques

A operação da Mineração Oceânica permite que seus contribuidores recuperem bitcoins "limpos", ou seja, bitcoins que são emitidos diretamente pela recompensa do bloco.

Ao contrário da maioria dos outros pools, a Oceânica não recebe os bitcoins recém-minerados; os endereços dos contribuidores são diretamente integrados ao modelo de bloco.

Por enquanto, a quantidade mínima para realmente se beneficiar dos bitcoins limpos é de 1.048.576 sats. Com cada bloco minerado pelo pool, sua parcela de "participações" deve lhe dar direito a mais de 1.048.576 sats para que eles sejam pagos diretamente a você pela recompensa do bloco.
Caso contrário, seus sats serão mantidos pela Oceânica até que suas recompensas totais excedam esse valor.

Todos os bitcoins temporariamente mantidos pela Oceânica estão neste endereço: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, tudo é verificável na TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
Também é possível sacar seus sats via Lightning usando BOLT12. Veremos como configurar isso.

### Taxas do Pool

As taxas variam de 0% a 2% dependendo do modelo de bloco escolhido.

## A Transparência da Oceânica

### Dados dos Contribuidores

![signup](assets/1.webp)

Todas as informações sobre o pool são transparentes, incluindo todos os dados dos usuários. Para entender esse ponto, vamos tomar um exemplo:

[No painel da Oceânica](https://ocean.xyz/dashboard), você tem várias informações como a taxa de hash nos últimos seis meses, o número de participantes no pool, o número total de bitcoins minerados, etc.

Vamos nos concentrar na seção "Contribuidores". Você pode ver a lista de todos os contribuidores com sua taxa de hash média nas últimas três horas, bem como a porcentagem de **"participações"** e **"hash"** em relação ao restante do pool.
**"Shares %"** é a porcentagem do trabalho fornecido pelo contribuidor na janela dos últimos oito blocos em comparação com o restante da pool.
**"Hash %"** é a porcentagem da taxa de hash média fornecida pelo contribuidor nas últimas três horas em comparação com o restante da pool.

![signup](assets/2.webp)

Você notará que os "Contribuidores" são identificados por um endereço Bitcoin. Você pode clicar em qualquer um desses endereços para mais detalhes.

Se pegarmos o primeiro, aquele com a maior taxa de hash [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), você pode ver todos os detalhes sobre este usuário: taxa de hash, número de bitcoins minerados, com qual bloco, e até os detalhes de cada uma de suas máquinas (ASICs). No entanto, eles permanecem anônimos, como no Bitcoin.

### Modelo de Bloco

No canto superior esquerdo do painel, você tem "Próximo bloco". Nesta página, existem quatro modelos de blocos diferentes. Ocean permite que cada contribuidor escolha o modelo de bloco que deseja apoiar. Isso não tem um impacto direto na sua compensação. Quando a pool minera um bloco, todos os contribuidores são compensados independentemente do modelo que escolheram. Isso simplesmente permite que todos "votem" pelo modelo de bloco que lhes convém.

![signup](assets/3.webp)

**CORE:** Taxa de 2%, este é o clássico modelo Bitcoin Core sem filtro, como escrito em sua página "Inclui transações e a maioria do spam"

**CORE+ANTISPAM:** Taxa de 0%, Bitcoin Core com um filtro contra certas transações como Ordinals "Inclui transações e limita spam"

**OCEAN:** Taxa de 0%, Bitcoin Knot "Inclui apenas transações e dados razoavelmente pequenos"

**DATA-FREE:** Taxa de 0%, Bitcoin Knot "Inclui apenas transações sem nenhum dado arbitrário"

### Distinção entre Bitcoin Core e Bitcoin Knot
Bitcoin Core é o software que permite que cerca de 99% dos nós Bitcoin ao redor do mundo operem. Bitcoin é um protocolo, o que significa que, assim como a Internet, onde existem vários navegadores, podem existir vários programas de software diferentes coexistindo na mesma TimeChain. No entanto, por preocupação com a compatibilidade e para limitar o risco de bugs que deixariam traços indeléveis na TimeChain, quase todos os desenvolvedores de Bitcoin trabalham no Bitcoin Core. Bitcoin Knots é um fork do Bitcoin Core, o que significa que compartilha a maioria de seu código, limitando grandemente o risco de bugs. Este fork foi criado por Luke Dashjr, que queria aplicar regras mais restritivas do que o Bitcoin Core sem criar um hard fork. Agora, Bitcoin Core e Bitcoin Knots coexistem graças ao consenso de Nakamoto.

## Adicionando um Trabalhador

Para adicionar um trabalhador, comece escolhendo seu modelo de bloco. Esta escolha determinará a URL da pool a ser inserida no seu minerador (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Em seguida, para o campo do usuário, insira um endereço Bitcoin de sua propriedade. Aqui está a lista de tipos de endereços compatíveis:
- **P2PKH** (Tipo de endereço original. Começa com “1”)
- **P2SH** (Multisignatura ou P2SH-Segwit. Começa com “3”)
- **Bech32** (Segwit. Começa com “bc”.)
- **Bech32m** (Taproot. Começa com “bc”. Mais longo que Bech32.)

Se você tem múltiplos mineradores, você pode inserir o mesmo endereço para todos eles para que suas taxas de hash sejam combinadas e apareçam como um único minerador. Você também pode distingui-los adicionando um nome distinto para cada um. Para fazer isso, simplesmente adicione “.nomedotrabalhador” após o endereço Bitcoin.

Finalmente, para o campo de senha, use `x`.

**Exemplo:**
Se você escolher o template **OCEAN**, seu endereço Bitcoin é `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` e você deseja nomear seu minerador “Brrrr”, então você precisará inserir as seguintes informações na interface do seu minerador:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **USUÁRIO**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **SENHA**: `x`

Alguns minutos após iniciar a mineração, você poderá ver seus dados no site Ocean procurando pelo seu endereço.

### Visão Geral do Painel
- **Participações na Janela de Recompensa**: Esses dados indicam o número de participações, o trabalho que você enviou para a pool na janela dos últimos 8 blocos minerados pela pool.
- **Recompensas Estimadas na Janela**: Estimativa do número de sats que você ganhará com o trabalho já realizado. Isso não leva em conta as taxas de transação, mas apenas o coinbase, os novos bitcoins emitidos pela rede.
- **Ganhos Estimados no Próximo Bloco**: Estimativa do número de sats ganhos se um bloco for minerado agora. Lembre-se, se esse valor for menor que 1.048.576 sats, você não receberá diretamente os sats no seu endereço. Eles serão enviados para o endereço do Ocean até que seus ganhos ultrapassem esse limite.

Abaixo, você tem um gráfico mostrando o histórico da sua taxa de hash até 6 meses.

![signup](assets/4.webp)

Aqui, você tem sua taxa de hash média em diferentes escalas de tempo, de 60s a 24h, bem como o histórico de blocos minerados pela pool para os quais você contribuiu e foi recompensado.

![signup](assets/5.webp)

Você tem a opção de exportar um arquivo CSV deste histórico com o botão **Baixar CSV**.

![signup](assets/6.webp)

Na seção seguinte, você tem uma lista de todos os mineradores que você conectou à pool com este endereço. Você tem, claro, a taxa de hash individual deles, mas também o número de sats que eles receberam individualmente pelo trabalho.

![signup](assets/7.webp)

Você pode clicar no **Apelido** de qualquer minerador. Você então terá todas as informações que acabamos de ver, mas especificamente para aquele minerador.

E no final da página, algumas informações adicionais onde você pode ver o histórico de pagamentos no seu endereço, os sats que você minerou mas ainda não foram pagos, e o total de sats que você minerou.

![signup](assets/8.webp)

Aqui, você pode ver que na caixa **Tempo Estimado Até o Pagamento Mínimo**, está escrito Lightning porque configuramos uma oferta BOLT12.

### Configurando Saques via Lightning
Como você entendeu, a Ocean tem como objetivo maximizar a transparência e minimizar a custódia (guardar seus sats em seu nome).
É por isso que, para saques via Lightning, é necessário usar **ofertas BOLT12**. Esta é uma nova forma de fazer um pagamento na rede Lightning que está começando a surgir em 2024 e permite várias coisas:
- É um link de pagamento reutilizável, permitindo pagamentos automáticos e, ao contrário de um endereço Lightning, o BOLT12 é não custodial.
- Também é um método de pagamento que fornece prova de que o pagamento foi feito, o que não acontece com LNURLs.
- Muito importante, pode ser usado em conjunto com uma assinatura Bitcoin para provar que você é tanto o titular do endereço BTC quanto da oferta BOLT12.
Até hoje (maio de 2024), poucas soluções existem para usar este método. Neste exemplo, usaremos um servidor Start9 com Core Lightning. Quando outras ferramentas, como Phoenix Wallet, por exemplo, integrarem ofertas BOLT12, este tutorial permanecerá aplicável. Certifique-se de ter canais abertos com liquidez de entrada, caso contrário, os pagamentos não funcionarão.

Comece indo ao seu painel no site da Ocean inserindo seu endereço BTC, depois clique na aba **Configuration**.

![signup](assets/9.webp)

Vamos copiar o texto **Description**, aqui:
`OCEAN Payouts for bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Agora vá para a sua interface Core Lightning no seu servidor Start9 (ou qualquer carteira capaz de fornecer uma oferta BOLT12).

![signup](assets/10.webp)

Clique em **Receive**.

Marque **Offer**, depois cole o texto copiado anteriormente no campo **Description** e deixe o campo **Amount** vazio.

![signup](assets/11.webp)

Clique em **Generate Offer**.

![signup](assets/12.webp)

Você gerou um link de pagamento reutilizável e permanente que não requer um servidor central como é o caso com endereços Lightning. Copie o link e então retorne à página da Ocean.

No campo **Lightning BOLT12 Offer**, cole o link de pagamento e deixe o campo **Block Height** em seu valor padrão. Clique em **GENERATE**.

![signup](assets/13.webp)

Para a Ocean garantir que este link de pagamento é realmente seu sem usar um sistema de contas, você precisará assinar a mensagem que acabou de ser gerada com sua chave privada correspondente ao endereço Bitcoin que está usando. Existem muitas soluções para assinar uma mensagem com sua chave privada. Neste tutorial, tomaremos o exemplo da BlueWallet, mas o método é o mesmo para todas as carteiras.

![signup](assets/14.webp)

Supondo que sua chave privada esteja na BlueWallet (você pode fazer o mesmo com uma carteira de hardware), clique na carteira em questão.

![signup](assets/15.webp)

Depois no **…** no topo direito.

![signup](assets/15bis.webp)

E **Sign/Verify Message**.

![signup](assets/16.webp)

Nesta janela, você tem três campos: **Address**, **Signature** e **Message**.

No campo **Address**, insira seu endereço Bitcoin. Se voltarmos ao nosso exemplo, é o endereço: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Deixe o campo **Signature** vazio.
Cole o texto gerado no campo **Mensagem** na página do Ocean: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Clique em **Assinar**.

Isso gerará uma assinatura criptográfica que prova que você é o proprietário do endereço `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, e esta assinatura é única graças à mensagem fornecida pelo Ocean, gerada a partir do link de pagamento BOLT12.

![signup](assets/17.webp)

Copie a assinatura e cole-a na página do Ocean, depois clique em **CONFIRMAR**.

![signup](assets/18.webp)

Você deverá ver uma mensagem de confirmação.

![signup](assets/19.webp)

Agora vá para a aba **Minhas Estatísticas**. Informações adicionais são exibidas no topo com o link de pagamento BOLT12 que você gerou anteriormente com o Core Lightning no Start9.

![signup](assets/20.webp)