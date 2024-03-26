---
name: JoinBot
description: Comprendere e utilizzare JoinBot
---

![DALL·E – samurai robot in a red forest, 3D render](assets/cover.jpeg)

JoinBot è un nuovo strumento che si aggiunge alla suite Samourai Wallet con l'ultima versione 0.99.98f del famoso software di portafoglio Bitcoin. Ti consente di effettuare facilmente una transazione collaborativa per ottimizzare la tua privacy, senza dover necessariamente trovare un partner.

**Un ringraziamento all'eccellente Fanis Michalakis per l'idea di utilizzare DALL-E per la miniatura!**

## Cosa è una transazione collaborativa su Bitcoin?

Bitcoin si basa su un registro dei conti distribuito e trasparente. Chiunque è in grado di tracciare le transazioni degli utenti di questo sistema di denaro elettronico. Per garantire una certa privacy, l'utente di Bitcoin può effettuare transazioni con una struttura specifica, al fine di aggiungere plausibile negabilità nell'interpretazione delle stesse.

L'idea non è nascondere direttamente le informazioni, ma confonderle tra le altre. Questo obiettivo viene utilizzato in particolare nei Coinjoin, transazioni che consentono di rompere la cronologia di una moneta su Bitcoin e rendere complesso il suo tracciamento. Per ottenere questo risultato, è necessario creare più input e output dello stesso importo nella transazione.

Gli input rappresentano gli input di una transazione Bitcoin, mentre gli output rappresentano le uscite. La transazione consuma i suoi input per creare nuove uscite, modificando le condizioni di spesa di una moneta. Questo meccanismo consente di spostare bitcoin tra gli utenti.
Ne parlo in dettaglio in questo articolo: Meccanismo di una transazione Bitcoin: UTXO, input e output.

Un modo per confondere le tracce in una transazione Bitcoin è effettuare una transazione collaborativa. Come suggerisce il nome, si tratta di un accordo tra più utenti che depositano ciascuno una somma di bitcoin come input nella stessa transazione e ne recuperano una somma come output.

Come accennato in precedenza, la struttura di transazione collaborativa più conosciuta è il Coinjoin. Ad esempio, nel protocollo Coinjoin Whirlpool, le transazioni coinvolgono 5 partecipanti in input e output, ognuno con la stessa quantità di bitcoin.

![Schema di una transazione Coinjoin su Whirlpool](assets/1.webp)

Un osservatore esterno a questa transazione non sarà in grado di sapere a quale output appartiene ciascun utente in input. Ad esempio, prendendo l'esempio dell'utente n°4 (viola), possiamo riconoscere il suo UTXO in input, ma non sapremo quale dei 5 output sia effettivamente il suo. L'informazione iniziale non è nascosta, ma confusa all'interno di un gruppo.
L'utente è in grado di negare il possesso di un certo UTXO in output. Questo fenomeno è chiamato "plausibile negabilità" e consente di ottenere la privacy in una transazione Bitcoin altrimenti trasparente.
Per saperne di più su Coinjoin, ti spiego TUTTO in questo lungo articolo: Comprendere e utilizzare CoinJoin su Bitcoin.

Sebbene molto efficace nel rompere il tracciamento di un UTXO, Coinjoin non è adatto alla spesa diretta. Infatti, la sua struttura implica l'uso di input di importi predefiniti e output dello stesso valore (modulo le commissioni di mining). Tuttavia, la transazione di spesa su Bitcoin è un momento critico per la privacy in quanto spesso collega fisicamente l'utente alla sua attività on-chain. Pertanto, sembra essenziale utilizzare strumenti di privacy per la spesa. Esistono quindi altre strutture di transazioni collaborative pensate appositamente per le transazioni di pagamento effettivo.

## La transazione StonewallX2

Tra la miriade di strumenti di spesa offerti da Samourai Wallet, c'è la transazione collaborativa StonewallX2. Si tratta di un mini Coinjoin tra due utenti pensato per il pagamento. Da un punto di vista esterno, questa transazione può portare a diverse possibili interpretazioni. Si ottiene quindi una plausibile negabilità e di conseguenza, privacy per l'utente.

Questa configurazione di transazione collaborativa StonewallX2 è disponibile su Samourai Wallet e su Sparrow Wallet. Questo strumento è interoperabile tra i due software.

Il suo meccanismo è abbastanza semplice da capire. Ecco come funziona nella pratica:

> - Un utente desidera effettuare un pagamento in bitcoin (ad esempio, presso un commerciante).
> - Recupera l'indirizzo di ricezione del destinatario effettivo del pagamento (il commerciante).
> - Costruisce una transazione specifica con più input: almeno uno di sua proprietà e uno di proprietà di un collaboratore esterno.
> - La transazione avrà 4 output, di cui 2 dello stesso importo: uno all'indirizzo del commerciante per pagarlo, uno di resto che torna all'utente, un output dello stesso valore del pagamento che va al collaboratore e un altro output che torna anche al collaboratore.

Ad esempio, ecco una transazione StonewallX2 classica in cui ho effettuato un pagamento di 50.125 sats. Il primo input di 102.588 sats proviene dal mio portafoglio Samourai. Il secondo input di 104.255 sats proviene dal portafoglio del mio collaboratore:

![Schema di una transazione StonewallX2](assets/2.webp)

Possiamo osservare 4 output di cui 2 dello stesso importo per confondere le tracce:

> - 50.125 sats che vanno al destinatario effettivo del mio pagamento.
> - 52.306 sats che rappresentano il mio resto e quindi tornano a un indirizzo del mio portafoglio.
> - 50.125 sats che tornano al mio collaboratore.
> - 53 973 sats qui reviennent vers mon collaborateur.
>   Alla fine dell'operazione, il collaboratore ritrova tutto il suo saldo iniziale (meno le commissioni di mining), e l'utente avrà pagato il commerciante. Ciò permette di aggiungere un'enorme entropia alla transazione e di rompere i legami indiscutibili tra il mittente e il destinatario del pagamento.

La forza della transazione di tipo StonewallX2 è che contrasta completamente una delle regole empiriche utilizzate dagli analisti di blockchain: la proprietà comune degli input in una transazione multi-input. In altre parole, nella maggior parte dei casi, se si osserva una transazione Bitcoin con più input, si può presumere che tutti questi input appartengano alla stessa persona. Satoshi Nakamoto aveva già identificato questo problema per la privacy dell'utente nel suo White Paper:

> "Come ulteriore misura di sicurezza, una nuova coppia di chiavi potrebbe essere utilizzata per ogni transazione al fine di mantenerle non collegate a un proprietario comune. Tuttavia, il collegamento è inevitabile con le transazioni multi-input, che rivelano necessariamente che i loro input erano detenuti da un unico proprietario."

Questa è una delle molte regole empiriche utilizzate nell'analisi on-chain per costruire cluster di indirizzi. Per saperne di più su queste euristiche, ti consiglio di leggere questa serie di 4 articoli di Samourai che introduce molto bene l'argomento.

La forza della transazione StonewallX2 risiede nel fatto che un osservatore esterno penserà che i diversi input della transazione appartengano a un proprietario comune. In realtà, sono due utenti diversi che collaborano. L'analisi del pagamento viene quindi indirizzata verso una falsa pista e la privacy degli utenti è preservata.

Dall'esterno, una transazione StonewallX2 non può essere differenziata da una transazione Stonewall. La differenza effettiva tra queste risiede semplicemente nel fatto che Stonewall non è collaborativo. Utilizza solo gli UTXO di un singolo utente. Ma nelle loro strutture sul registro dei conti, Stonewall e StonewallX2 sono perfettamente identici. Ciò consente di aggiungere ancora più possibili interpretazioni a questa struttura di transazione poiché un osservatore esterno non potrà sapere se gli input provengono dalla stessa persona o da due collaboratori.

Inoltre, il vantaggio di StonewallX2 rispetto a un PayJoin di tipo Stowaway è che può essere utilizzato in tutte le situazioni. Il destinatario effettivo del pagamento non inserisce alcun input nella transazione. Pertanto, è possibile utilizzare un StonewallX2 per pagare presso qualsiasi commerciante che accetta Bitcoin, anche se quest'ultimo non utilizza Samourai o Sparrow.
En revanche, l’inconvénient principal de cette structure de transaction est qu’elle nécessite un collaborateur qui veuille bien utiliser ses bitcoins pour participer à votre paiement. Si vous avez des amis bitcoiners prêts à vous aider en toute circonstance, cela n’est pas un problème. En revanche, si vous ne connaissez pas d’autres utilisateurs de Samourai Wallet, ou bien si personne n’est disponible pour collaborer, alors vous êtes bloqué.

Il existe toutefois un groupe Telegram où vous pouvez trouver d’autres utilisateurs de Samourai qui voudront bien collaborer avec vous. Vous pouvez le retrouver en [cliquant ici](https://telegram.me/joinchat/AAAAAEHxkD8t1v_3w7G5vA).

Pour résoudre cette problématique, les équipes de Samourai ont récemment ajouté une nouvelle fonctionnalité à leur application : JoinBot.

# C’est quoi JoinBot ?

Le principe de JoinBot est simple. Si vous ne trouvez personne avec qui collaborer pour une transaction StonewallX2, vous pouvez collaborer avec lui. Concrètement, vous allez en fait réaliser une transaction collaborative directement avec Samourai Wallet.

Ce service est très commode, notamment pour les utilisateurs novices, puisqu’il est disponible 24h/24 et 7j/7. Si vous devez effectuer un paiement urgent et que vous souhaitez faire un StonewallX2, vous n’aurez plus besoin de contacter un ami, ou bien de chercher un collaborateur en ligne. JoinBot se chargera de vous assister.

Un autre avantage de JoinBot est que les UTXO qu’il fournit en input sont issus exclusivement de postmix Whirlpool, ce qui vient améliorer la confidentialité de votre paiement. De plus, puisque JoinBot est tout le temps en ligne, vous devriez collaborer avec des UTXO qui disposent de larges Anonset prospectifs.

Évidemment, JoinBot dispose de certains compromis qu’il convient de signaler :

> Comme pour un StonewallX2 classique, votre collaborateur est forcément au courant des UTXO utilisés et de leur destination. Dans le cas de JoinBot, Samourai connait les détails de cette transaction. Ce n’est pas forcément une mauvaise chose, mais il faut le garder à l’esprit.
> Pour éviter les spams, Samourai prélève 3,5 % de frais de service sur le montant de la transaction effective, avec une limite maximale de 0,01 BTC. Par exemple, si j’envoie un paiement réel de 100 kilosats avec JoinBot, le montant des frais de service sera de 3 500 sats.
> Pour utiliser JoinBot, vous devez obligatoirement disposer d’au moins deux UTXO non liés et disponibles sur votre portefeuille.
> Sur un StonewallX2 classique, les frais de minage sont partagés équitablement entre les deux collaborateurs. Avec JoinBot, vous devrez évidemment payer l’intégralité des frais de minage.
> Affinché una transazione JoinBot sia esattamente uguale a una transazione classica StonewallX2 o Stonewall, il pagamento delle commissioni di servizio avviene su una transazione completamente separata. Il rimborso della metà delle commissioni di mining inizialmente pagate da Samourai avverrà durante questa seconda transazione. Per ottimizzare la tua privacy fino alla fine, il pagamento delle commissioni avviene tramite una transazione con struttura Stowaway (PayJoin).

## Come utilizzare JoinBot?

Per effettuare una transazione JoinBot, devi avere un portafoglio Samourai Wallet. Puoi scaricarlo qui, o dal Google Playstore.

A differenza della maggior parte degli strumenti sviluppati da Samourai, al momento Sparrow Wallet non ha ancora annunciato l'implementazione di JoinBot. Quindi questo strumento è disponibile solo su Samourai.

Scopri passo dopo passo come effettuare una transazione StonewallX2 con JoinBot in questo video:

![Come utilizzare Joinbot](https://youtu.be/80MoMz2Ne5g)

Ecco lo schema della transazione che abbiamo appena effettuato nel video:

![Schema della mia transazione StonewallX2 con JoinBot.](assets/3.webp)

Possiamo vedere 5 input:

> - 3 input di 100 kilosat provenienti da Samourai (JoinBot).
> - 2 input provenienti dal mio portafoglio personale, di 3.524 sat e 1,8 megasat.

I 4 output della transazione sono i seguenti:

> - 1 di 212.452 sat verso il destinatario effettivo del mio pagamento.
> - 1 altro dello stesso importo che ritorna a un indirizzo di Samourai.
> - 1 resto che ritorna anche a Samourai per 87.302 sat. Questo rappresenta la differenza tra il totale dei loro input (300.000 sat) e l'output di offuscamento (212.452 sat) meno le commissioni di mining.
> - 1 resto che ritorna a un altro indirizzo del mio portafoglio. Rappresenta la differenza tra il totale dei miei input e il pagamento effettivo, meno le commissioni di mining.

Come promemoria, le commissioni di mining non rappresentano un output delle transazioni. Rappresentano semplicemente la differenza tra il totale degli input e il totale degli output.

## Conclusioni

JoinBot è uno strumento aggiuntivo che permette di aggiungere più scelte e libertà per l'utente di Samourai. Permette di effettuare una transazione collaborativa StonewallX2 direttamente con Samourai come collaboratore. Questo tipo di transazione aiuta a migliorare la privacy degli utenti.

Se puoi effettuare una transazione classica StonewallX2 con un amico, ti consiglio comunque di preferire questa modalità di utilizzo dello strumento. Tuttavia, se sei bloccato e non trovi nessun collaboratore per effettuare un pagamento, sai che JoinBot sarà disponibile 24 ore su 24, 7 giorni su 7 per collaborare con te.

> Risorse esterne:
>
> - https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
> - https://youtu.be/vhUREWiY570
> - https://docs.samourai.io/wallet/privacy-enhanced-transactions
> - https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin
