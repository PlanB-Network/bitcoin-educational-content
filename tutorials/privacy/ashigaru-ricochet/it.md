---
name: Ashigaru - Ricochet
description: Comprendere e utilizzare le transazioni Ricochet
---
![cover ricochet](assets/cover.webp)



> *Uno strumento di qualità superiore che aggiunge un'ulteriore cronologia alle transazioni. Stupisce le blacklist e aiuta a difendersi da chiusure ingiuste di account di terze parti.*

## Cos'è un Ricochet?



Ricochet è una tecnica che consiste nell'eseguire diverse transazioni fittizie verso se stessi per simulare un trasferimento di proprietà di bitcoin. Questo strumento si differenzia dalle altre transazioni di Ashigaru (ereditate da Samurai Wallet) in quanto non fornisce un anonimato prospettico, ma piuttosto una forma di anonimato retrospettivo. In effetti, Ricochet sfuma le specificità che possono compromettere la fungibilità di un pezzo Bitcoin.



Ad esempio, se si effettua un coinjoin, il pezzo che esce dal mix sarà identificato come tale. Gli strumenti di analisi delle catene sono in grado di rilevare i paternostri delle transazioni coinjoin e di assegnare un'etichetta ai pezzi che ne escono. In effetti, coinjoin mira a rompere i legami storici di una moneta, ma il suo passaggio attraverso coinjoin rimane rilevabile. Per analogia, questo fenomeno è simile alla crittografia di un testo: sebbene non sia possibile accedere al testo originale in chiaro, è facile identificare che è stata applicata una crittografia.



L'etichetta "coinjoined" può influenzare la fungibilità di una UTXO. Le entità regolamentate, come le piattaforme di scambio, possono rifiutarsi di accettare un UTXO coinjoined o addirittura chiedere spiegazioni al suo proprietario, con il rischio di vedersi bloccare il conto o congelare i fondi. In alcuni casi, la piattaforma può persino segnalare il vostro comportamento alle autorità statali.



È qui che entra in gioco il metodo Ricochet. Per attenuare l'impronta lasciata da una coinjoin, Ricochet esegue quattro transazioni successive in cui l'utente trasferisce i propri fondi a se stesso a diversi indirizzi. Dopo questa sequenza di transazioni, lo strumento Ricochet indirizza infine i bitcoin verso la loro destinazione finale, ad esempio una piattaforma di scambio. L'obiettivo è creare una distanza tra la transazione originale di coinjoin e l'atto finale di spesa. In questo modo, gli strumenti di analisi della blockchain presumono che ci sia stato probabilmente un trasferimento di proprietà dopo il coinjoin e che quindi non sia necessario agire contro l'emittente.



![image](assets/fr/01.webp)



Di fronte al metodo Ricochet, si potrebbe immaginare che il software di analisi della catena approfondisca l'esame oltre i quattro rimbalzi. Tuttavia, queste piattaforme si trovano di fronte a un dilemma nell'ottimizzazione della soglia di rilevamento. Devono stabilire un numero limite di hop dopo il quale accettano che probabilmente si è verificato un cambio di proprietà e che il collegamento a una coinjoin precedente deve essere ignorato. Tuttavia, la determinazione di questa soglia è rischiosa: ogni estensione del numero di salti osservati aumenta esponenzialmente il volume di falsi positivi, cioè di individui erroneamente contrassegnati come partecipanti a una coinjoin, mentre in realtà l'operazione è stata effettuata da qualcun altro. Questo scenario rappresenta un grosso rischio per queste aziende, in quanto i falsi positivi portano all'insoddisfazione, che può spingere i clienti interessati a rivolgersi alla concorrenza. A lungo termine, una soglia di rilevamento troppo ambiziosa porta una piattaforma a perdere più clienti dei suoi concorrenti, il che potrebbe minacciare la sua redditività. È quindi complicato per queste piattaforme aumentare il numero di rimbalzi osservati, e 4 è spesso un numero sufficiente per contrastare le loro analisi.



Pertanto, **il caso d'uso più comune di Ricochet si presenta quando è necessario nascondere una precedente partecipazione a una coinjoin su un UTXO di cui si è proprietari.** Idealmente, è meglio evitare di trasferire bitcoin che hanno subito una coinjoin a entità regolamentate. Tuttavia, nel caso in cui non vi sia altra scelta, in particolare nell'urgenza di liquidare i bitcoin in valuta statale, Ricochet offre una soluzione efficace.



## Come funziona Ricochet su Ashigaru?



Il Ricochet è semplicemente un metodo di invio di bitcoin a se stessi, originariamente inventato dagli sviluppatori di Samurai Wallet. È quindi perfettamente possibile simulare un Ricochet manualmente, senza bisogno di uno strumento specializzato. Tuttavia, per coloro che desiderano automatizzare il processo e godere di un risultato più curato, lo strumento Ricochet disponibile tramite l'applicazione Ashigaru (che è un Samourai fork) rappresenta una buona soluzione.



Poiché l'Ashigaru si fa pagare per il suo servizio, un Ricochet costa `100.000 sats` come tassa di servizio, più una tassa di mining. Il suo utilizzo è quindi consigliato per trasferimenti di importi significativi.



L'applicazione Ashigaru offre due varianti di Ricochet:





- Ricochet rinforzato, o "consegna scaglionata", che offre il vantaggio di distribuire le spese di servizio di Ashigaru sulle cinque transazioni successive. Questa opzione garantisce inoltre che ogni transazione venga trasmessa in un momento distinto e registrata in un blocco diverso, imitando il più possibile il comportamento di un cambio di proprietà. Anche se più lento, questo metodo è preferibile per chi non ha fretta, in quanto massimizza l'efficienza di Ricochet rafforzando la sua resistenza all'analisi della catena;





- Il classico Ricochet, che è progettato per eseguire l'operazione con velocità, trasmettendo tutte le transazioni in un intervallo di tempo ridotto. Questo metodo, quindi, offre meno riservatezza e meno resistenza all'analisi rispetto al metodo rinforzato. Dovrebbe essere utilizzato solo per le spedizioni urgenti.



## Come effettuare un Ricochet su Ashigaru?



Effettuare un rimbalzo su Ashigaru è molto semplice: basta attivare l'opzione corrispondente quando si crea una transazione di invio. Per iniziare, clicca sul pulsante `+`, poi su `Invio` e seleziona il conto da cui desideri inviare i fondi.



![Image](assets/fr/02.webp)



Compilare i dati della transazione: l'importo da inviare e l'indirizzo finale del destinatario dopo i salti di Ricochet. Quindi selezionare l'opzione "Ricochet".



![Image](assets/fr/03.webp)



Si può quindi scegliere tra le due modalità di Ricochet discusse nella sezione teorica: Ricochet classico, in cui tutte le transazioni sono incluse nello stesso blocco, o consegna scaglionata, che migliora la qualità di Ricochet al costo di un ritardo maggiore.



Una volta effettuata la scelta, premere la freccia in fondo allo schermo per confermare.



![Image](assets/fr/04.webp)



Nella schermata successiva viene visualizzato un riepilogo completo della transazione. Qui è anche possibile regolare il tasso di commissione per le transazioni Ricochet in base alle condizioni di mercato. Se tutto è di vostro gradimento, trascinate la freccia verde per firmare e distribuire le transazioni Ricochet.



![Image](assets/fr/05.webp)



Attendere che i vari salti vengano eseguiti automaticamente.



![Image](assets/fr/06.webp)



Le transazioni sono state trasmesse con successo.



![Image](assets/fr/07.webp)



Ora conoscete bene l'opzione Ricochet disponibile nell'applicazione Ashigaru. Per andare oltre, vi consiglio di seguire il mio corso di formazione BTC 204, che vi insegnerà in dettaglio come rafforzare la vostra riservatezza onchain.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c