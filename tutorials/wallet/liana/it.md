---
name: Liana
description: Impostazione e utilizzo di un portafoglio su Liana
---
![cover](assets/cover.webp)

In questo tutorial spiegheremo passo dopo passo come utilizzare l'applicazione Liana su un computer. Tra le altre cose, imparerete a impostare un piano di successione automatico, a ricevere e inviare bitcoin in situazioni normali e a recuperare i fondi da un portafoglio esistente dopo un determinato periodo.

Nel gennaio 2025, i portafogli hardware compatibili con Liana erano: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

Se desiderate recuperare fondi da un portafoglio Liana esistente, leggete la presentazione qui sotto e andate direttamente alla sezione "Recupero di bitcoin".

## Presentazione del software Liana

Liana è un pacchetto software open-source progettato per la creazione e la gestione di portafogli avanzati, in particolare come parte di un sistema di eredità automatizzato o di un robusto meccanismo di backup. Il progetto è stato sviluppato a partire dal 2022 da Wizardsardine, una società co-fondata da Kévin Loaec e Antoine Poinsot. Sul sito ufficiale, Liana viene presentato come "un semplice portfolio per la cura personale, con funzionalità di recupero ed ereditarietà". Il software funziona su computer - Linux, MacOS, Windows - e il suo codice sorgente (aperto) è disponibile [su GitHub](https://github.com/wizardsardine/liana).

Liana si basa sulla programmabilità di Bitcoin per creare un portafoglio avanzato. In particolare, sfrutta i blocchi temporali (*timelocks*), che consentono di spendere i fondi solo una volta trascorso un determinato periodo di tempo e che sono coinvolti nel recupero dei Bitcoin. Un portafoglio Liana è quindi composto da diversi percorsi di spesa:


- Un percorso di spesa principale, sempre disponibile;
- Almeno un percorso di recupero, che diventa accessibile dopo un certo tempo.

Il diagramma seguente illustra il funzionamento di un portafoglio con due percorsi di spesa:

![Schéma explicatif](assets/fr/01.webp)

Questa operazione consente di impostare varie configurazioni, tra cui :


- Un piano di successione (o eredità) che consente agli eredi di recuperare i fondi in caso di morte dell'utente. Per maggiori informazioni su questo argomento, si consiglia la lettura della [parte 4](https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) del corso BTC102.
- Un backup rinforzato con un tempo di ripristino, che offre all'utente la possibilità di utilizzare il proprio portafoglio senza dover conservare la frase segreta corrispondente e rischiare di vederselo rubare, ad esempio durante un furto.
- Una rete di sicurezza per le persone che iniziano a utilizzare i Bitcoin: esse gestiranno il proprio portafoglio e il loro "tutore" (un parente, ad esempio) si riserverà il diritto di recuperare i loro fondi dopo un determinato periodo.
- Uno schema di firma multiparte (*multisig*) con requisiti ridotti nel tempo, per far fronte alla scomparsa di uno o più partecipanti, come ad esempio i soci di un'azienda.

Il grande punto di forza di Liana è che introduce una modalità standardizzata per garantire il recupero dei fondi in caso di perdita della chiave principale, utilizzata per le spese correnti. Si tratta di un'enorme innovazione per la custodia pulita dei fondi, che è piena di rischi, soprattutto se non si è ben informati sull'argomento. Liana potrebbe quindi incoraggiare anche gli utenti più avversi al rischio a non utilizzare più un depositario (come una piattaforma di scambio) per custodire i propri fondi e a rientrare in possesso del proprio denaro, in linea con l'etica cypherpunk di Bitcoin.

Naturalmente, Liana ha i suoi svantaggi. Il primo è che bisogna aggiornare regolarmente il proprio portafoglio effettuando una transazione sulla blockchain di Bitcoin. Questa operazione può essere fastidiosa (a seconda della frequenza con cui si utilizza il software) e costosa (a seconda del livello delle commissioni del momento), ma è il prezzo da pagare per una maggiore sicurezza.

Un secondo punto negativo può essere la riservatezza. Quando si coinvolge un'altra persona nella configurazione, questa viene a conoscenza di tutti i vostri indirizzi e può quindi monitorare la vostra attività. Tuttavia, questo non sarà un problema se si opta per un backup rinforzato o per un piano di successione in cui il vostro erede non sia immediatamente a conoscenza dei dettagli del portafoglio.

## Preparazione

In questa esercitazione, imposteremo un piano di successione. Utilizzeremo il software :


- Una Ledger Nano S Plus, per le spese quotidiane;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- Un Blockstream Jade, utilizzato per recuperare i fondi;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Due supporti di memoria (chiavette USB) per memorizzare il descrittore del portafoglio;
- Una lettera di successione, contenente le istruzioni per il recupero dei fondi;
- Un sacchetto numerato e sigillato, per garantire che il dispositivo di recupero (la Giada) non sia stato utilizzato.

## Installazione e configurazione

Visitate il sito ufficiale di Wizardsardine e scaricate Liana all'indirizzo https://wizardsardine.com/liana/. È anche possibile scaricare l'ultima versione [dal repository GitHub](https://github.com/wizardsardine/liana/releases), dove è possibile verificare l'autenticità del software. La versione usata in questo tutorial è la 0.9.

![Télécharger Liana](assets/fr/02.webp)

Per sapere come verificare manualmente l'autenticità e l'integrità del software prima dell'installazione, vi consigliamo di consultare questo tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Installare il software sul computer e avviarlo. Scegliere l'opzione "*Crea un nuovo portafoglio Liana*" per configurare il portafoglio.

![Accueil Liana](assets/fr/03.webp)

Scegliere il tipo di portafoglio. Se si desidera impostare un backup avanzato con tempi di ripristino, è possibile selezionare l'opzione "*Costruisci il tuo*" e optare per lo schema predefinito. Il funzionamento sarà più o meno lo stesso, tranne per il fatto che non sarà necessario conservare la frase di ripristino del portafoglio hardware.

Ignoriamo qui il caso di *Multisig in espansione*, che prevede una configurazione più complessa.

Per gli scopi di questa esercitazione, utilizzeremo l'ereditarietà semplice.

![Choisir type de portefeuille](assets/fr/04.webp)

Segue una rapida spiegazione.

![Rapide explication](assets/fr/05.webp)

Una volta letta la spiegazione, sarete in grado di impostare le chiavi del vostro portafoglio Liana. Si tratta di una fase cruciale, in quanto determina le caratteristiche di spesa del vostro conto.

![Configurer clés](assets/fr/06.webp)

Innanzitutto, nel menu "Impostazioni avanzate" è possibile decidere il "tipo di descrittore", ossia il modo in cui il contratto verrà scritto sulla catena. È possibile scegliere tra due tipi: P2WSH (SegWit) o Taproot. In entrambi i casi, la semantica delle condizioni di spesa sarà la stessa. Mentre P2WSH rende il contratto più facile da capire, Taproot è superiore in quanto nasconde le condizioni non utilizzate e risparmia costi durante il recupero.

Questa scelta è facoltativa: in caso di dubbio, lasciare l'opzione predefinita (P2WSH nel caso della versione 0.9, ma è soggetta a modifiche).

![Choisir le type de descripteur](assets/fr/07.webp)

Quindi, configurare la chiave primaria (*chiave primaria*). Questa chiave (o meglio, questo insieme di chiavi) sarà utilizzata per la spesa corrente dei fondi, che non è soggetta ad alcuna condizione temporale. Facendo clic su "*Impostazione*", è possibile selezionare il corrispondente *dispositivo di firma*. Nel nostro caso, abbiamo scelto il portafoglio hardware Ledger Nano S Plus.

Autorizzare la condivisione della chiave pubblica estesa del dispositivo. Assegnare a questa chiave un nome significativo (in questo caso, "Nano S+"). Tutte le applicazioni installate sul dispositivo continueranno a funzionare normalmente.

![Configurer clé principale](assets/fr/08.webp)

Quindi, impostare il ritardo di rimborso, cioè il tempo dopo il quale i fondi possono essere spesi dalla *chiave di eredità*. Questo ritardo è definito in termini di blocchi, con ogni blocco separato da una media di 10 minuti. Può variare da 10 minuti (1 blocco) a circa 15 mesi (65.535 blocchi). Questo limite superiore è una limitazione del protocollo Bitcoin, poiché il tempo di blocco è codificato su 16 bit.

Salvo circostanze particolari, optate per il tempo di consegna più lungo: 15 mesi o 65.535 blocchi. Questo vi farà risparmiare sui costi. Vi consigliamo comunque di eseguire la procedura di aggiornamento (descritta nella sezione "Aggiornamento del portafoglio") una volta all'anno, sempre nello stesso periodo dell'anno, per "ritualizzare" questa pratica ed evitare dimenticanze.

Qui abbiamo impostato un tempo di recupero di un'ora (6 blocchi) per eseguire i nostri test.

![Configurer temps de verrouillage](assets/fr/09.webp)

Infine, impostate la vostra chiave di proprietà. Questa chiave (o meglio, insieme di chiavi) sarà utilizzata per recuperare i fondi in caso di scomparsa. Cliccare su "*Imposta*", scegliere il dispositivo di firma e convalidare la condivisione della chiave pubblica estesa su di esso.

Per questa esercitazione abbiamo scelto Jade. Assegnate alla chiave un nome evocativo (qui "Jade"). Come per il primo dispositivo, i conti convenzionali continueranno a funzionare.

![Configurer clé de succession](assets/fr/10.webp)

Una volta completate tutte queste operazioni, controllate che tutto sia in ordine e cliccate su "*Continua*" per confermare le vostre scelte.

![Confirmer clés](assets/fr/11.webp)

Il passo successivo consiste nel salvare il descrittore del portafoglio. Si tratta delle informazioni necessarie per trovare i fondi sul conto. Contrariamente alla frase mnemonica, il descrittore non consente di spendere i fondi, quindi la sua divulgazione porrà solo un problema di riservatezza (la persona conoscerà tutte le vostre transazioni).

Salvate due copie del descrittore su supporti elettronici, come le chiavette USB. Assicuratevi anche di stampare due copie su carta, in modo da potervi accedere in caso di danni ai supporti elettronici. Ogni backup deve essere associato a un dispositivo di firma.

![Sauvegarder descripteur](assets/fr/12.webp)

Il nostro descrittore (che viene analizzato alla fine del tutorial) è il seguente:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

La fase finale della configurazione iniziale del portfolio consiste nel verificare il descrittore in ciascuno dei portfolio hardware che fungono da dispositivi di firma.

![Enregistrer descripteur](assets/fr/13.webp)

Procedere allo stesso modo per ogni dispositivo di firma. È necessario controllare e confermare che il descrittore sia stato aggiunto a ciascun portafoglio hardware.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Le informazioni del portafoglio sono state registrate e non resta che configurare la modalità di connessione alla rete Bitcoin. Si può scegliere di utilizzare il proprio nodo (locale o remoto) o l'infrastruttura di WizardSardine. In quest'ultimo caso, dovrete collegare un indirizzo e-mail al vostro portafoglio, che vi permetterà di recuperare il descrittore. WizardSardine avrà accesso a tutte le vostre transazioni. Si consiglia quindi la prima opzione.

![Sélectionner connexion réseau](assets/fr/15.webp)

Abbiamo scelto di usare il nostro nodo. È possibile utilizzare un nodo esistente o installare un nodo "potato" sulla propria macchina. Se non avete accesso ad altri nodi, installate il vostro nodo sulla vostra macchina, il che richiederà un po' di tempo (dell'ordine di alcuni giorni).

![Choisir type de nœud](assets/fr/16.webp)

Per questa esercitazione abbiamo utilizzato un server Electrum esistente (pubblico). Ma attenzione! Aveva accesso a tutte le nostre attività con il portafoglio Liana. Utilizzate quindi il vostro nodo se volete proteggere la vostra privacy.

![Connexion serveur Electrum public](assets/fr/17.webp)

Una volta completata la configurazione del nodo, si aprirà la schermata principale che mostrerà il portafoglio Liana appena creato.

Cogliere l'occasione per conservare l'unità di recupero in un luogo sicuro. Dovrebbe essere conservata in una posizione strategica, in modo da poter essere trovata dagli eredi in caso di morte.

Per maggiore sicurezza, è possibile riporre i componenti utilizzati per il recupero in una busta sigillata (*borsa antimanomissione*) e annotare il numero di serie da qualche parte. In questo modo si garantisce che nessuno vi abbia avuto accesso e che il dispositivo rimanga valido.

Nel nostro esempio, abbiamo assemblato i seguenti elementi:


- Blockstream Jade come dispositivo di firma per la proprietà;
- Un cavo USB per il collegamento e la ricarica del dispositivo;
- Un backup cartaceo della frase in caso di malfunzionamento o danneggiamento del dispositivo (si noti che il supporto può anche essere metallico, e quindi protetto dalle intemperie, come nel caso delle capsule Cryptosteel, ad esempio);
- La chiave USB contenente il descrittore del portafoglio ;
- Un backup cartaceo del descrittore, in caso di malfunzionamento o danneggiamento della chiave USB (questo backup non è stato fotografato qui);
- Una lettera di successione che descriva le misure da adottare per recuperare i fondi.

![Éléments de récupération](assets/fr/18.webp)

E mettiamo questi articoli sotto sigillo!

![Sachet scellé récupération](assets/fr/19.webp)

## Ricezione dei fondi

La schermata principale di Liana mostra il saldo e le transazioni (passate e correnti) legate al portafoglio. Nel nostro caso, il saldo è pari a zero, il che è normale.

![Écran principal](assets/fr/20.webp)

Per ricevere i fondi, andare alla scheda "*Ricezione*" e cliccare su "*Generazione indirizzo*". Sullo schermo dovrebbe apparire un nuovo indirizzo. È più lungo di quello dei portafogli tradizionali: è un indirizzo collegato a un contratto autonomo (P2WSH o Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

È necessario verificare questo indirizzo sul portafoglio hardware facendo clic su "*Verifica sul dispositivo hardware*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Una volta inviati i fondi, la transazione appare nella schermata principale (prima come non confermata, poi come confermata). Per questo test abbiamo inviato 50.000 satoshis (poco più di 50 dollari al momento del trasferimento). È ovvio che nel vostro caso l'importo trasferito dovrà essere di un ordine di grandezza superiore a questo valore, a causa delle spese di transazione.

![Vérifier solde](assets/fr/23.webp)

È possibile controllare lo stato di scadenza dei propri fondi accedendo alla scheda "*Coins*". Questa scheda mostra le diverse monete (UTXO) presenti nel vostro portafoglio. Qui possiamo vedere che la moneta da 50.000 satoshis creata dalla nostra transazione scade lo stesso giorno (tra un'ora).

![Obtenir informations pièce](assets/fr/24.webp)

Per comprendere meglio il modello di rappresentazione UTXO utilizzato in Bitcoin, è possibile consultare la prima parte del corso sulla riservatezza in Bitcoin scritto da Loïc Morel :

https://planb.network/courses/btc204
## Spese correnti

La spesa corrente è la situazione normale per l'utilizzo di Liana. L'invio di bitcoin con la chiave master funziona come in tutti i portafogli Bitcoin classici, come Electrum o Sparrow.

Per effettuare un addebito, accedere alla scheda "*Invio*" e inserire le informazioni essenziali: l'indirizzo BTC del destinatario, l'importo da inviare e la tariffa desiderata. È inoltre possibile aggiungere una descrizione (salvata in locale) per comodità personale. Nel nostro esempio, abbiamo inviato 10.000 satoshis a un certo Bob, per un tasso di addebito di 4 sat/ov, ovvero 0,67 dollari al momento della transazione.

Liana offre anche il "controllo delle monete": si indica quale moneta (UTXO) si desidera spendere. Qui abbiamo scelto la moneta da 50.000 satoshis creata in precedenza.

![Envoyer fonds clé principale](assets/fr/25.webp)

Quindi firmare la transazione con il dispositivo di firma collegato alla chiave master facendo clic su "*Sign*". Dovrete verificare e confermare la transazione sul vostro portafoglio hardware. Qui abbiamo utilizzato il Nano S Plus per firmare la transazione.

![Signer transaction clé principale](assets/fr/26.webp)

Infine, trasmettere la transazione alla rete facendo clic su "*Broadcast*". Si noti che l'invio di fondi azzera il tempo di recupero delle monete usate.

![Diffuser transaction clé principale](assets/fr/27.webp)

La transazione viene visualizzata nella schermata principale e il saldo viene aggiornato.

![Solde après dépense](assets/fr/28.webp)

## Aggiornamento del portafoglio

Come spiegato in precedenza, il portafoglio Liana richiede di aggiornare regolarmente i propri fondi eseguendo una transazione sulla blockchain. Se non lo fate, i vostri fondi possono essere recuperati dal vostro erede (o dal vostro secondo dispositivo nel caso di un backup avanzato). Questa situazione non è estremamente pericolosa, ma vanifica lo scopo della creazione di questo meccanismo: mantenere il controllo dei propri bitcoin senza ricorrere a una terza parte fidata, beneficiando di una rete di sicurezza.

Prima che i fondi (o parte di essi) scadano e possano essere spesi con la chiave di recupero, verrà visualizzato un avviso. Indica che il "percorso di recupero" (*percorso di recupero*) sarà presto disponibile. Data la brevità del nostro tempo di recupero (un'ora), questo messaggio viene visualizzato direttamente nel nostro caso.

![Avertissement chemin récupération](assets/fr/29.webp)

Quando la scadenza si avvicina, appare un pulsante che invita ad aggiornare i fondi in questione.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

Per aggiornare le monete, accedere alla scheda "*monete*" e fare clic su "*Refresh coin*" nella casella corrispondente. Se avete diverse monete, dovreste aggiornarle una per una e a intervalli relativamente brevi, per motivi di riservatezza. Per contenere i costi, è possibile consolidare i fondi inviando l'intero portafoglio a un nuovo indirizzo di ricezione, ma ciò influirà sulla riservatezza.

![Actualiser pièce](assets/fr/31.webp)

Indicare il tasso di commissione desiderato per la transazione. Poiché si tratta di un bonifico a favore di se stessi, è possibile impostare un tasso di commissione piuttosto basso, soprattutto se viene effettuato alcuni giorni prima della scadenza.

![Transfert à soi-même](assets/fr/32.webp)

La transazione (con l'etichetta "*autotrasferimento*") sarà visibile solo nella scheda "*Transazioni*".

![Transactions après auto-transfert](assets/fr/33.webp)

Una volta confermata, la tua moneta è al sicuro! Potete stare tranquilli fino alla prossima data di scadenza.

## Recupero di Bitcoin

Quando si recuperano fondi dal portafoglio Liana, ci si può trovare di fronte a due situazioni. Potreste avere accesso al computer su cui è installato il software, nel qual caso non dovrete fare altro che aprirlo (cosa che avverrà nel caso del modello di backup avanzato). Tuttavia, è possibile che non si abbia accesso a questo computer, quindi si partirà da zero. La procedura di ripristino è la stessa in entrambi i casi.

Per iniziare, scaricate Liana da [il sito ufficiale di Wizardsardine](https://wizardsardine.com/liana/), o da [il repository GitHub](https://github.com/wizardsardine/liana/releases), dove potete verificare l'autenticità del software. Installare il software ed eseguirlo. La versione utilizzata nel nostro caso è la 0.9, quindi la grafica potrebbe essere cambiata. Nella schermata di benvenuto, selezionare l'opzione "Aggiungi un portafoglio Liana esistente".

![Ajouter portefeuille existant](assets/fr/34.webp)

Configurare la modalità di connessione alla rete. Si può scegliere di utilizzare il proprio nodo (locale o remoto) o di utilizzare l'infrastruttura di WizardSardine. In quest'ultimo caso, è necessario l'indirizzo e-mail utilizzato dal creatore del portafoglio, in modo che i fondi possano essere localizzati automaticamente. Se non si dispone di queste informazioni, scegliere la prima opzione.

![Sélectionner connexion réseau](assets/fr/35.webp)

Se si utilizza un proprio nodo, importare il descrittore del portafoglio. Si tratta di una descrizione tecnica del conto, che consente di recuperare i fondi in esso contenuti. Nel nostro caso, si tratta delle seguenti informazioni:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Liana chiede quindi di inserire una frase mnemonica. Se si dispone di un dispositivo di firma funzionante (portafoglio hardware), si può saltare questa parte. Se il dispositivo è mancante o danneggiato, ma si dispone delle 12 o 24 parole corrispondenti, è comunque possibile utilizzare questa opzione. Per sicurezza (se la quantità da recuperare è elevata), si consiglia comunque di procurarsi un nuovo portafoglio hardware e di utilizzare la frase mnemonica per ripristinare le chiavi su di esso.

Nel nostro caso, utilizziamo il portafoglio hardware Blockstream Jade come dispositivo di recupero e scegliamo di saltare ("*Skip*") questo passaggio.

![Passer phrase mnémotechnique](assets/fr/37.webp)

Controllare e salvare il descrittore nel dispositivo di firma selezionandolo sullo schermo. Se il portafoglio hardware non appare, verificare che sia collegato e sbloccato. Controllare e confermare che queste informazioni siano state aggiunte al dispositivo.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Configurare il nodo. È possibile utilizzare un nodo esistente o installare un nodo "potato" sulla propria macchina. Nel nostro caso, abbiamo usato un nodo esistente.

![Choisir type de nœud](assets/fr/39.webp)

Per questa esercitazione abbiamo utilizzato un server Electrum pubblico. Tuttavia, ha avuto accesso a tutte le nostre attività con il portafoglio Liana. Se si vuole proteggere la propria privacy, è meglio utilizzare un proprio nodo.

![Connexion serveur Electrum public](assets/fr/17.webp)

Una volta impostato il nodo, si accede alla schermata principale del portafoglio, dove è possibile visualizzare il saldo e le transazioni passate collegate al conto. Si può anche vedere se i fondi possono essere recuperati. Qui vediamo che è possibile recuperare una moneta.

![Accueil Liana récupération](assets/fr/40.webp)

Per recuperare i fondi del portafoglio, andare su Impostazioni ("*Impostazioni*") in basso a sinistra e cliccare su "*Recupero*".

![Récupération dans paramètres](assets/fr/41.webp)

Spendere la moneta nel portafoglio selezionando la casella appropriata. Indicare l'indirizzo BTC a cui si desidera inviare i fondi e la tariffa della transazione. Cliccare quindi su "*Avanti*".

![Récupération des pièces](assets/fr/42.webp)

Firmare la transazione facendo clic su "*Sign*" e convalidando la transazione sul proprio portafoglio hardware.

![Signer transaction clé de récupération](assets/fr/43.webp)

Quindi trasmetterla in rete facendo clic su "*Diffusione*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

La transazione dovrebbe apparire nella schermata principale. Una volta confermata, il recupero è completo!

![Écran principal après récupération](assets/fr/45.webp)

## Video

Se volete saperne di più su Liana, ci sono alcuni contenuti video che vi daranno un'idea più chiara del suo funzionamento. Ecco un video di presentazione di Liana con Kévin Loaec e Antoine Poinsot:

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

Ed ecco un tutorial su come usare Liana, con Antoine Poinsot:

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

Le manipolazioni mostrate in quest'ultima sono simili a quelle presentate in questa esercitazione.

## Bonus: analisi dei descrittori

Il descrittore è una stringa di caratteri leggibili dall'uomo che descrive in modo esaustivo un insieme di indirizzi. Combina una serie di informazioni essenziali per il recupero delle parti (UTXO) di un portafoglio avanzato. Il modo in cui il descrittore è scritto si basa su [Miniscript syntax](https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), il linguaggio di scripting sviluppato da Andrew Poelstra, Pieter Wuille e Sanket Kanjalkar nel 2019.

Per capire meglio perché questa stringa di caratteri è importante, analizziamo il descrittore del nostro esempio, che è :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Da questo descrittore si possono estrarre le seguenti informazioni:


- `wsh` (abbreviazione di *witness script hash*): È il tipo di output transazionale creato. Se si fosse scelto di usare Taproot, l'identificatore sarebbe stato `tr`.
- `o_d`: È un operatore logico che indica che *una delle due condizioni seguenti* deve essere soddisfatta affinché la spesa sia accettata (la `_d` indica una particolare sintassi).
- `pk` (abbreviazione di *public key*): Questo operatore verifica una data firma rispetto alla seguente chiave pubblica e fornisce una risposta booleana (VERO o FALSO).
- `[3689a8e7/48'/0'/0'/2']`: Questo elemento include l'*impronta digitale* della chiave master per il portafoglio hardware principale (in questo caso il Nano S Plus) e il percorso di derivazione della chiave privata estesa collegata (da cui derivano tutte le altre chiavi private).
- `xpub6FKY ... WQa`: È la chiave pubblica estesa collegata al portafoglio hardware principale (qui il Nano S Plus)
- `/<0;1>/*`: Questi sono i percorsi di derivazione per ottenere chiavi e indirizzi semplici: `0` per la ricezione, `1` per le operazioni interne (*cambiamento*), con un "jolly" (`*`) che consente la derivazione sequenziale di più indirizzi in modo configurabile, simile alla gestione del "gap limit" dei classici software di portafoglio.
- e_v`: È un operatore logico che indica che *le due seguenti* condizioni devono essere soddisfatte affinché la spesa sia accettata (la `_v` indica una particolare sintassi).
- `v:pkh` (abbreviazione di *verifica: hash di chiave pubblica*): Questo operatore verifica una firma e una chiave pubblica date rispetto all'hash della chiave pubblica (*hash*) che segue. Si tratta essenzialmente dello stesso controllo degli script P2PKH e P2WPKH.
- `[42e629dd/48'/0'/0'/2']`: Si tratta dello stesso elemento di cui sopra (costituito dalla traccia e dal percorso di derivazione), con l'eccezione che viene indicata la traccia della chiave master del portafoglio di recupero hardware (in questo caso il Jade).
- `xpub6DpQ ... WQd`: È la chiave pubblica estesa collegata al portafoglio di recupero hardware (qui il Jade).
- `older(6)`: questo operatore controlla che l'output transazionale creato debba avere un'età strettamente superiore a 6 blocchi per poter essere speso.

L'ultimo dato (`8alrve5h`) è la somma di controllo del descrittore e corrisponde all'identificatore del portafoglio.

Gli script creati da questo portfolio avranno la seguente forma:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Poiché la sicurezza del vostro portafoglio Bitcoin dipende anche dalla comprensione del suo funzionamento, vi suggerisco di studiare a fondo i meccanismi dei portafogli deterministici e gerarchici seguendo questo corso di formazione gratuito su Plan ₿ Network :

https://planb.network/courses/cyp201