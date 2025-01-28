---
term: COINJOIN

---
Coinjoin è una tecnica utilizzata per rompere la tracciabilità dei bitcoin. Si basa su una transazione collaborativa con una struttura specifica che porta lo stesso nome: la transazione coinjoin. Le transazioni Coinjoin contribuiscono a migliorare la protezione della privacy degli utenti Bitcoin rendendo più difficile l'analisi delle transazioni da parte di osservatori esterni. Questa struttura consente di mescolare più monete in una singola transazione, rendendo difficile determinare i collegamenti tra gli indirizzi di ingresso e di uscita.

Il funzionamento generale di coinjoin è il seguente: diversi utenti che desiderano mescolare depositano un importo come input di una transazione. Questi input verranno restituiti come output diversi dello stesso importo. Alla fine della transazione, è impossibile determinare quale uscita appartiene a quale utente. Tecnicamente non c'è alcun legame tra gli input e gli output della transazione coinjoin. Il legame tra ogni utente e ogni UTXO è interrotto, così come lo è la storia di ogni moneta.

![](../../dictionnaire/assets/4.webp)

Per consentire la coinjoin senza che nessun utente perda il controllo sui propri fondi in qualsiasi momento, la transazione viene prima costruita da un coordinatore e poi trasmessa a ciascun utente. Ciascuno firma la transazione dal proprio lato dopo averne verificato l'adeguatezza, e poi tutte le firme vengono aggiunte alla transazione. Se un utente o il coordinatore tenta di rubare i fondi degli altri modificando gli output della transazione coinjoin, le firme non saranno valide e la transazione sarà rifiutata dai nodi. Quando la registrazione dell'output dei partecipanti viene effettuata utilizzando le firme cieche di Chaum per evitare il collegamento con l'input, si parla di "Chaumian coinjoin".

Questo meccanismo aumenta la riservatezza delle transazioni senza richiedere modifiche al protocollo Bitcoin. Implementazioni specifiche di coinjoin, come Whirlpool, JoinMarket o Wabisabi, offrono soluzioni per facilitare il processo di coordinamento tra i partecipanti e migliorare l'efficienza della transazione coinjoin. Ecco un esempio di transazione coinjoin:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

È difficile stabilire con certezza chi abbia introdotto per primo l'idea di coinjoin su Bitcoin e chi abbia avuto l'idea di utilizzare le firme cieche di David Chaum in questo contesto. Spesso si pensa che Gregory Maxwell sia stato il primo a parlarne in [un messaggio su BitcoinTalk del 2013](https://bitcointalk.org/index.php?topic=279249.0):

Utilizzando le firme cieche di Chaum: Gli utenti si connettono e forniscono gli input (e cambiano gli indirizzi) e una versione crittograficamente blindata dell'indirizzo a cui desiderano inviare le loro monete private; il server firma i token e li restituisce. Gli utenti si riconnettono in modo anonimo, smascherano i loro indirizzi di uscita e li inviano nuovamente al server. Il server può vedere che tutti gli output sono stati firmati da lui e che, di conseguenza, tutti gli output provengono da partecipanti validi. In seguito, le persone si riconnettono e firmano.

Maxwell, G. (2013, 22 agosto). *CoinJoin: La privacy dei Bitcoin per il mondo reale*. Forum BitcoinTalk. https://bitcointalk.org/index.php?topic=279249.0

Tuttavia, esistono menzioni precedenti, sia per le firme Chaum nel contesto della miscelazione, sia per le coinjoin. [Nel giugno 2011, Duncan Townsend presenta su BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) un mixer che utilizza le firme Chaum in modo del tutto simile alle moderne coinjoin chaumiane. Nello stesso thread, c'è [un messaggio di hashcoin in risposta a Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) per migliorare il suo mixer. Questo messaggio presenta ciò che più si avvicina alle coinjoin. Un accenno a un sistema simile si trova anche in [un messaggio di Alex Mizrahi del 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), mentre consigliava i creatori di Tenebrix. Il termine "coinjoin" non è stato inventato da Greg Maxwell, ma è nato da un'idea di Peter Todd.

> *Il termine "coinjoin" non ha una traduzione francese. Alcuni bitcoiners usano anche i termini "mix", "mixing" o "mixage" per riferirsi alla transazione coinjoin. La miscelazione è piuttosto il processo utilizzato alla base del coinjoin. Inoltre, è importante non confondere la miscelazione tramite coinjoin con la miscelazione tramite un attore centrale che prende possesso dei bitcoin durante il processo. Questo non ha nulla a che vedere con il coinjoin, dove l'utente non perde il controllo dei propri bitcoin durante il processo.*