---
name: Nakamochi
description: Node Running Made Easy - Como configurar e usar o Nakamochi Bitcoin e o Lightning node.
---
Executar o seu próprio nó completo Bitcoin e Lightning já não precisa de ser uma tarefa complexa limitada a especialistas técnicos. Tradicionalmente, a criação e gestão de nós exigia um conhecimento profundo de criptografia, redes e desenvolvimento de software. A Nakamochi muda isso ao tornar os nós acessíveis a todos, independentemente da formação técnica.

Com a Nakamochi, qualquer pessoa pode configurar e operar um nó a partir de casa, permitindo total privacidade e independência financeira. Operar um nó completo não só protege suas próprias transações, mas também contribui para a força da rede Bitcoin. Uma rede Bitcoin descentralizada e resiliente depende de uma ampla distribuição de nós para garantir sua segurança e independência.

### Índice


- O que é o Nakamochi e como funciona?
- Criação de Nakamochi
- Sobre a Lightning Network
- Abrir canais e efetuar transacções na Lightning Network

## O que é o Nakamochi e como funciona?

O Nakamochi é um nó completo somente de Bitcoin que suporta as redes Bitcoin e Lightning. Inclui uma carteira Bitcoin e Lightning integrada, permitindo que os utilizadores executem um nó Bitcoin seguro e auto-soberano enquanto beneficiam da velocidade e dos baixos custos de transação da Lightning Network.

O seu nó Nakamochi é gerido através de uma aplicação móvel, [BitBanana (Android)](https://bitbanana.app) e [Zeus (iOS)](https://bitbanana.app), permitindo-lhe controlá-lo convenientemente a partir de qualquer lugar. Estas aplicações funcionam como um controlo remoto para o seu nó, permitindo-lhe pagar diretamente com Bitcoin ou Lightning, gerir transacções, abrir ou fechar canais, verificar saldos e monitorizar o desempenho do seu nó, tudo com facilidade.

## A configuração do Nakamochi demora apenas 5 minutos

### Passo 1: Ligar e começar a trabalhar

1. Ligar o Nakamochi à corrente eléctrica e ao Wi-Fi.

2. Clique em **"Configurar nova carteira "** e guarde de forma segura a sua frase de recuperação de 24 palavras.

3. Use um aplicativo de gerenciamento de nós (Zeus ou BitBanana) para se conectar ao seu Nakamochi:

4. Abra a aplicação e leia o código QR apresentado na sua Nakamochi.

5. Para maior segurança, defina um código PIN no seu dispositivo.

![image](assets/en/01.webp)

_Ligue-se à corrente e escreva a sua frase-semente de 24 palavras_

![image](assets/en/02.webp)

_Espere até que a cadeia de blocos esteja a par_

![image](assets/en/03.webp)

_Configurar nova carteira no separador Relâmpago_

![image](assets/en/04.webp)

_Scan QR Code with Node Management App_

![image](asset/en/05.webp)

_Para maior segurança, definir um código PIN_

**Nota:** _Permite que o teu nó Nakamochi sincronize com a blockchain. Este processo pode demorar algum tempo, dependendo da tua ligação à Internet

## Sobre a Lightning Network

A Bitcoin Lightning Network revoluciona as transacções de Bitcoin, tornando-as mais rápidas, mais baratas e mais eficientes. É perfeita para o uso diário, permitindo pagamentos quase instantâneos com taxas mínimas, ideal para microtransações como comprar um café ou lidar com pequenas compras frequentes.

Ao operar fora da cadeia, o Lightning foi concebido para escalar, suportando milhares de transacções por segundo sem sobrecarregar a cadeia de blocos principal da Bitcoin. Isto torna-o um ator-chave na evolução da Bitcoin para um sistema de pagamento prático e global.

A privacidade é outra vantagem, uma vez que as transacções no Lightning são encaminhadas através de canais de pagamento privados em vez de serem registadas diretamente na cadeia de blocos. Isso garante uma maneira mais discreta de transacionar, mantendo a segurança robusta do Bitcoin.

#### Explicação dos canais de pagamento

A Lightning Network funciona através de canais de pagamento, que são ligações entre duas partes que permitem múltiplas transacções sem interagir diretamente com a cadeia de blocos. Quando um canal está aberto, o saldo entre as duas partes é atualizado nesta solução Lightning de segunda camada para cada transação, garantindo pagamentos rápidos e de baixo custo. Apenas a abertura e o fecho do canal são registados na cadeia, reduzindo o congestionamento na cadeia de blocos Bitcoin. Este design garante escalabilidade e privacidade, uma vez que as transacções individuais não são registadas no livro-razão público.

**Exemplo:** Alice e Bob abrem um canal ao comprometerem Bitcoin com ele. Alice envia Bitcoins para Bob, e os seus saldos fora da cadeia são actualizados instantaneamente sem um registo na cadeia. Se Alice pagar a Charlie, e Alice não tiver um canal direto para Charlie, o pagamento pode ser encaminhado através do canal de Bob para chegar a Charlie. O encaminhamento através de nós intermediários assegura os pagamentos mesmo sem ligações diretas, tornando a rede altamente eficiente.

## Abrir canais e efetuar transacções na Lightning Network

Assim que a sua Nakamochi estiver configurada e ligada a uma aplicação de gestão de nós, pode começar a utilizar a Lightning Network abrindo canais e efectuando transacções.

### Abrir canais no Zeus (iOS):

1. Aceder ao separador **"Canais "** (menu inferior).

2. Clique no **"+"** para abrir um novo canal.

3. Digitalize ou introduza a chave pública do nó ao qual pretende ligar-se.

4. Introduza o montante bloqueado (escolha com o seu par ou utilize o montante fixo mínimo para nós bem conhecidos).

5. Clique em **"Abrir canal "**.

![image](asset/en/06.webp)

captura de ecrã de _ZEUS_

Para obter mais informações: [Channels | Zeus Documentation](https://docs.zeusln.app/)

### Abrir canais na BitBanana (Android):

1. Abrir o menu de hambúrgueres (à esquerda).

2. Aceder a **"Canais "**.

3. Clique no **"+"** para adicionar/abrir um novo canal.

4. Digitalize ou cole a pubkey.

5. Introduza o montante bloqueado (escolha com o seu par ou utilize o montante fixo mínimo para nós bem conhecidos).

![image](asset/en/07.webp)

captura de ecrã de Bitbanana_

Para mais informações: [BitBanana](https://bitbanana.com)

Assim que o seu canal estiver aberto, os pagamentos podem ser encaminhados através dele para outros participantes na rede. Os saldos são ajustados fora da cadeia, assegurando que as transacções são quase instantâneas e incorrem em taxas mínimas.

Se já não precisar de um canal, pode fechá-lo. Esta ação estabelece o saldo final entre si e o seu par e regista-o na cadeia. O ideal é que ambas as partes concordem e estejam online para um "fechamento cooperativo" (mais rápido e com menos taxas do que um "fechamento forçado" com um par que não responde ou está offline).

Geralmente, recomendamos que deixe os canais abertos para reduzir os custos e aumentar a fiabilidade e eficiência da rede. Ao manter os canais abertos, minimiza as taxas de transação na cadeia, evita o tempo de inatividade para reconexões de canais e mantém uma capacidade de encaminhamento estável para um processamento de pagamentos sem falhas. Esta abordagem promove uma rede robusta e resistente, melhorando simultaneamente a experiência geral do utilizador e reduzindo as despesas operacionais.

### Ligações úteis


- [Sobre Nakamochi](https://nakamochi.io/)
- [Subscrever a newsletter da Nakamochi] (https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)