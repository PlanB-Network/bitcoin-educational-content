---
term: COINJOIN

---
Coinjoin é uma técnica utilizada para quebrar a rastreabilidade das bitcoins. Baseia-se numa transação colaborativa com uma estrutura específica com o mesmo nome: a transação coinjoin. As transacções Coinjoin ajudam a melhorar a proteção da privacidade dos utilizadores de Bitcoin, dificultando a análise das transacções por parte de observadores externos. Esta estrutura permite a mistura de várias moedas numa única transação, dificultando a determinação das ligações entre os endereços de entrada e de saída.

O funcionamento geral do coinjoin é o seguinte: diferentes utilizadores que desejem misturar depositam um montante como entrada de uma transação. Estas entradas serão apresentadas como saídas diferentes do mesmo montante. No final da transação, é impossível determinar que saída pertence a que utilizador. Tecnicamente, não existe qualquer ligação entre os inputs e os outputs da transação coinjoin. A ligação entre cada utilizador e cada UTXO é quebrada, da mesma forma que o histórico de cada moeda.

![](../../dictionnaire/assets/4.webp)

Para permitir a junção de moedas sem que nenhum utilizador perca o controlo sobre os seus fundos em qualquer momento, a transação é primeiro construída por um coordenador e depois transmitida a cada utilizador. Cada um assina a transação do seu lado depois de verificar que lhe convém e, em seguida, todas as assinaturas são adicionadas à transação. Se um utilizador ou o coordenador tentar roubar os fundos de outros modificando os resultados da transação coinjoin, as assinaturas serão inválidas e a transação será rejeitada pelos nós. Quando o registo dos resultados dos participantes é efectuado utilizando as assinaturas cegas de Chaum para evitar a ligação com os resultados, esta operação é designada por "Chaumian coinjoin".

Este mecanismo aumenta a confidencialidade das transacções sem exigir modificações no protocolo Bitcoin. Implementações específicas de coinjoin, tais como Whirlpool, JoinMarket, ou Wabisabi, oferecem soluções para facilitar o processo de coordenação entre os participantes e aumentar a eficiência da transação coinjoin. Aqui está um exemplo de uma transação coinjoin:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

É difícil determinar com certeza quem foi o primeiro a introduzir a ideia de coinjoin no Bitcoin e quem teve a ideia de usar as assinaturas cegas de David Chaum neste contexto. Pensa-se frequentemente que Gregory Maxwell foi o primeiro a discuti-la em [uma mensagem no BitcoinTalk em 2013] (https://bitcointalk.org/index.php?topic=279249.0):

Usando assinaturas cegas Chaum: Os utilizadores ligam-se e fornecem entradas (e mudam de endereço), bem como uma versão criptograficamente oculta do endereço para o qual desejam enviar as suas moedas privadas; o servidor assina os tokens e devolve-os. Os utilizadores voltam a ligar-se anonimamente, desmascaram os seus endereços de saída e enviam-nos novamente para o servidor. O servidor pode ver que todas as saídas foram assinadas por ele e que, consequentemente, todas as saídas provêm de participantes válidos. Mais tarde, as pessoas voltam a ligar-se e a assinar.

Maxwell, G. (2013, 22 de agosto). *CoinJoin: Privacidade Bitcoin para o mundo real*. Fórum BitcoinTalk. https://bitcointalk.org/index.php?topic=279249.0

No entanto, há menções anteriores, tanto para assinaturas Chaum no contexto de mistura, como para coinjoins. [Em junho de 2011, Duncan Townsend apresenta no BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) um misturador que utiliza assinaturas Chaum de uma forma bastante semelhante às modernas coinjoins Chaumianas. No mesmo tópico, há [uma mensagem de hashcoin em resposta a Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) para melhorar seu mixer. Esta mensagem apresenta o que mais se assemelha a coinjoins. Há também uma menção a um sistema semelhante em [uma mensagem de Alex Mizrahi em 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), quando ele estava a aconselhar os criadores da Tenebrix. O termo "coinjoin" em si não foi inventado por Greg Maxwell, mas surgiu de uma ideia de Peter Todd.

> ► *O termo "coinjoin" não tem uma tradução francesa. Alguns bitcoiners utilizam também os termos "mix", "mixing" ou "mixage" para se referirem à transação coinjoin. A mistura é antes o processo utilizado no centro da coinjoin. Além disso, é importante não confundir a mistura através de coinjoins com a mistura através de um ator central que toma posse dos bitcoins durante o processo. Isto não tem nada a ver com a coinjoin em que o utilizador não perde o controlo dos seus bitcoins durante o processo*