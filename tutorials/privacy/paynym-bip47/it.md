---
name: BIP47 - PayNym
description: Utilizzate un codice di pagamento riutilizzabile su Ashigaru
---
![cover](assets/cover.webp)



Il peggior errore di privacy che si possa commettere su Bitcoin è il riutilizzo degli indirizzi. Ogni volta che lo stesso indirizzo riceve diversi pagamenti, queste transazioni vengono collegate tra loro, fornendo al mondo una mappa delle vostre transazioni. Per questo motivo, si raccomanda vivamente di inserire sempre un indirizzo generate unico per ogni ricevuta. Ma per alcune applicazioni Bitcoin questo non è semplice.



BIP47, proposto da Justus Ranvier nel 2015, fornisce una risposta elegante a questo problema. Introduce il concetto di **codice di pagamento riutilizzabile**: un identificatore unico che consente di ricevere un numero virtualmente illimitato di pagamenti onchain in bitcoin, senza mai riutilizzare un indirizzo. Grazie a un meccanismo crittografico basato su uno scambio ECDH (*Diffie-Hellman su curve ellittiche*), ogni pagamento allo stesso codice risulta in un indirizzo vuoto, specifico per la relazione tra mittente e destinatario.



![Image](assets/fr/01.webp)



Questo principio BIP47 è implementato in particolare da **PayNym**, il sistema originariamente sviluppato da Samourai Wallet e ora ripreso da Ashigaru. In questo tutorial vedremo come attivare il PayNym, scambiare i codici di pagamento con un corrispondente ed effettuare transazioni senza riutilizzare un indirizzo.



Non mi soffermerò qui sul funzionamento dettagliato del BIP47. Se desiderate approfondire l'argomento, consultate il capitolo 6.6 del mio corso di formazione BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Prerequisiti



Per seguire questa esercitazione, tutto ciò che serve è un wallet sull'applicazione Ashigaru. Se non sapete come scaricare, verificare, installare l'applicazione o creare un wallet, vi consiglio di consultare prima questa guida:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Richiesta PayNym



Il primo passo consiste nel richiedere il proprio PayNym. Questa operazione deve essere eseguita una sola volta per ogni wallet. Essa associa il codice di pagamento BIP47 derivato dal seed (`PM...`) a un identificativo unico specifico dell'implementazione PayNym. Questo identificativo, più breve e leggibile, può essere trasmesso ai vostri corrispondenti per facilitare gli scambi, senza dover condividere il lungo codice BIP47 completo.



Per farlo, cliccare sull'immagine di PayNym in alto a sinistra dell'interfaccia, quindi sul codice di pagamento `PM...`.



![Image](assets/fr/02.webp)



Cliccate quindi sui tre puntini in alto a destra e selezionate "Reclama PayNym".



![Image](assets/fr/03.webp)



Confermare facendo clic sul pulsante "RECLAMA IL TUO PAYNYM".



![Image](assets/fr/04.webp)



Aggiornate la pagina: il vostro ID PayNym è ora visualizzato sotto la vostra immagine, appena sopra il codice di pagamento BIP47.



![Image](assets/fr/05.webp)



Il vostro PayNym è ora attivo e pronto per essere utilizzato per le prime transazioni BIP47.



## Connettersi con un contatto



Esistono due tipi di connessione tra PayNym: **follow** e **connect**. L'operazione `follow` è completamente gratuita. Stabilisce un collegamento tra due PayNym attraverso Soroban, un protocollo di comunicazione criptato basato su Tor sviluppato dal team di Samourai e adottato da Ashigaru. Questo collegamento consente a due utenti che si seguono di scambiare informazioni privatamente, in particolare per coordinare transazioni collaborative come Stowaway o StonewallX2, di cui parleremo in un altro tutorial. Questo passaggio è specifico di PayNym e non fa parte del protocollo BIP47.



![Image](assets/fr/06.webp)



L'operazione di connessione (`connect`), invece, richiede una transazione on-chain. Consiste nell'eseguire una transazione di notifica come definito nel BIP47. Questa transazione Bitcoin contiene metadati in un output `OP_RETURN`, che stabilisce un canale di comunicazione criptato tra il pagatore e il destinatario. Da questo canale, l'ordinante sarà in grado di fornire indirizzi di ricezione univoci per ogni pagamento, mentre il destinatario riceverà una notifica di tali pagamenti e sarà in grado di fornire le chiavi private associate agli indirizzi per spendere i fondi in un secondo momento.



Questa transazione di notifica ha un costo: la tariffa mining e il 546 sats inviato all'indirizzo di notifica del destinatario per segnalare la connessione. Una volta stabilita la connessione, è possibile effettuare un numero quasi infinito di pagamenti tramite BIP47.



In poche parole:




- follow": gratuito, stabilisce una comunicazione criptata via Soroban, utile per gli strumenti collaborativi di Ashigaru;
- `Connect`: a pagamento, esegue la transazione di notifica BIP47 per attivare il canale tra pagatore e destinatario.



Per interagire con un PayNym, è necessario prima *seguirlo*. Questo è il primo passo prima di stabilire una connessione BIP47. Supponiamo di voler inviare pagamenti ricorrenti al PayNym `+instinctiveoffer10`.



Vai alla tua pagina PayNym su Ashigaru, poi clicca sul pulsante `+` in basso a destra dell'interfaccia.



![Image](assets/fr/07.webp)



È quindi possibile incollare il codice di pagamento completo del destinatario o scansionare il suo codice QR.



![Image](assets/fr/08.webp)



Se avete solo il suo ID PayNym, andate su [Paynym.rs](https://paynym.rs/) per trovare il codice QR associato al suo codice di pagamento.



![Image](assets/fr/09.webp)



Una volta scannerizzato il codice QR, fate clic sul pulsante `FOLLOW` per seguire il PayNym.



![Image](assets/fr/10.webp)



L'azione `FOLLOW` è sufficiente per le transazioni collaborative (*cahoots*). Tuttavia, per inviare pagamenti BIP47, è necessario stabilire una connessione: fare clic su `CONNECT` per eseguire la transazione di notifica.



![Image](assets/fr/11.webp)



La notifica della transazione viene quindi trasmessa in rete. Attendere almeno una conferma prima di effettuare il primo pagamento.



![Image](assets/fr/12.webp)



## Effettuare un pagamento BIP47



Ora siete collegati al destinatario e potete inviare un pagamento a un indirizzo unico, generato automaticamente con il protocollo BIP47, senza alcuno scambio preliminare con il destinatario.



Dalla pagina principale di PayNym, cliccare sul contatto a cui si desidera inviare un pagamento.



![Image](assets/fr/13.webp)



In alto a destra dell'interfaccia, fare clic sull'icona della freccia.



![Image](assets/fr/14.webp)



Inserire l'importo da inviare. Non è necessario inserire un indirizzo di ricezione: verrà ricavato automaticamente utilizzando il protocollo BIP47.



![Image](assets/fr/15.webp)



Controllare attentamente i dettagli della transazione, comprese le spese, quindi trascinare la freccia verde in fondo allo schermo per firmare e trasmettere la transazione.



![Image](assets/fr/16.webp)



La transazione è stata inviata.



![Image](assets/fr/17.webp)



In questo esempio, il pagamento è stato effettuato su un altro dei miei portafogli PayNym. Posso quindi vedere che è arrivato sull'altro mio Ashigaru wallet, senza che sia stato scambiato manualmente alcun indirizzo: è stato utilizzato solo l'identificativo PayNym.



![Image](assets/fr/18.webp)



Ora sapete come utilizzare i codici di pagamento riutilizzabili BIP47 grazie all'implementazione di PayNym nell'applicazione Ashigaru. Ora potete condividere questo codice di pagamento con chiunque voglia inviarvi pagamenti (soprattutto pagamenti ricorrenti). Potete anche pubblicare il vostro ID PayNym sul vostro sito web o sui social network per ricevere donazioni.



Per approfondire la conoscenza di questo protocollo, comprenderne in dettaglio il funzionamento e le implicazioni per la riservatezza, vi consiglio vivamente di seguire il mio corso BTC 204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c