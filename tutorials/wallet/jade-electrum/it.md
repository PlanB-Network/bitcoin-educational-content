---
name: Jade - Electrum
description: Come usare il tuo Jade o Jade Plus con Electrum (desktop)
---

![cover](assets/cover.webp)

_Questa guida è tratta da una [lezione di Officine Bitcoin](https://officinebitcoin.it/lezioni/jadeele/index.html)_

Il tutorial è realizzato con Jade Classic, ma le operazioni sono valide anche per chi ha Jade Plus.

Dopo aver inizializzato Jade, puoi iniziare ad usarlo e – per farlo – scegli un wallet di visualizzazione.

Jade è un dispositivo che può essere usato con diversi wallet, o companion app come le specifica Blockstream sul suo sito.

In questo tutorial vedrai le fasi di utilizzo con Electrum Wallet, tramite connessione con cavo USB.

## Trasferimento chiave pubblica

Prendi e accendi il tuo Jade inizializzato. Appena acceso si presenta così:


![img](assets/en/32.webp)

Selezionando _Unlock Jade_, ti compare il menu in cui si deve scegliere come connettere il tuo dispositivo alla companion app.

Con Electrum è possibile connettere Jade solo via USB, pertanto scegli questo metodo.

Lancia Electrum, che si aprirà proponendo come opzione di default l’apertura dell’ultimo wallet utilizzato.

Se è la prima volta che connetti Jade ad Electrum, seleziona _Create New Wallet_ e poi _Finish_.

![img](assets/en/34.webp)

Dai un nome al wallet.

![img](assets/en/35.webp)

Seleziona Standard Wallet.

![img](assets/en/36.webp)

Nella scelta del keystore è fondamentale selezionare _Use a hardware device_.

![img](assets/en/37.webp)

Electrum inizia la scansione alla ricerca del dispositivo hardware.

![img](assets/en/38.webp)

Collegando l’USB al computer (già connesso dalla parte dell’USB C a Jade), l’hardware wallet ti appare in modalità di blocco. Jade si sblocca mettendo il PIN a sei cifre impostato durante il setup.


![img](assets/en/39.webp)

Sbloccato il dispositivo Hardware, Electrum rileva Jade. Prosegui cliccando _Next_.

![img](assets/en/40.webp)

A questo punto Electrum ti chiede di impostare lo script policy: scegli _Native Segwit_.

![img](assets/en/41.webp)

Inizia la fase del trasferimento della chiave pubblica dal wallet da Jade all'Electrum di visualizzazione.

Al termine dell’esportazione della chiave pubblica, il procedimento è terminato.

Il watch-only è pronto ed Electrum avvisa del completamento con la schermata che segue.

![img](assets/en/42.webp)

Il wallet è effettivamente creato ed è possibile iniziare ad esplorarlo: si vedono gli _addresses_, le _wallet information_ e – soprattutto – è possibile notare in basso a destra l’indicazione che si tratta del dispositivo di Blockstream. Il pallino verde accanto al logo Blockstream indica che il dispositivo è acceso e connesso correttamente in rete locale.

![img](assets/en/43.webp)

## Transazioni di ricezione e di spesa

Dal menu _Receive_ di Electrum, genera uno `scriptPubKey` (indirizzo) per ricevere dei fondi. Inizia sempre con un importo piccolo e fai un test di ricezione+spesa.

![img](assets/en/44.webp)

Ricevuti i sats, puoi controllarne l’arrivo nel menu _History_.

![img](assets/en/45.webp)

![img](assets/en/46.webp)

Una volta confermata la transazione, puoi spendere questo UTXO e terminare il test.

La spesa prevede l’utilizzo di Jade per firmare.

Vai nel menu _Send_ di Electrum, incolla uno scriptPubKey e controllalo bene.

![img](assets/en/47.webp)

Una volta terminato premi _Pay_.

Si apre la finestra di transazione, nella quale è importante impostare le corrette fee di transazione. Finiti tutti i settaggi clicca su _Preview_ in basso a destra.

![img](assets/en/48.webp)

La finestra di transazione mostra alcuni dettagli importanti, primo fra tutti lo status: `Unsigned`.

In questa fase è possibile vedere anche il comando _Sign_, che devi cliccare per apporre la firma con Jade.

![img](assets/en/49.webp)

Inizia ora una fase di comunicazione tra il wallet di visualizzazione e il dispositivo hardware, in cui Electrum ti avvisa di seguire le istruzioni sul dispositivo hardware, acceso e pronto per firmare.

![img](assets/en/50.webp)

**Prima, però, è meglio che verifichi cosa stai firmando: tutti i parametri della transazione appena impostata, compaiono anche su Jade** ed è possibile verificarli tutti.

![img](assets/en/51.webp)

Per proseguire accertati di posizionare il cursore sempre sulla freccina `→` che porta alle fasi successive e mai sulla `X` a meno che non vuoi terminare l’operazione senza portarla a termine.

La parte delle verifiche finisce con la visualizzazione delle fee. A questo punto la conferma equivale a mettere la firma.

![img](assets/en/52.webp)

Per un breve istante Jade processa l'operazione, quando ha terminato torna al menu iniziale.

![img](assets/en/53.webp)

Mentre su Electrum puoi constatare lo status della transazione, che da `Unsigned` è cambiato in `Signed` e adesso è possibile, per te, propagarla cliccando _Broadcast_.

![img](assets/en/54.webp)

Il wallet, così testato, è utilizzabile per ricevere UTXO destinati ad essere conservati in modo sicuro.

![img](assets/en/55.webp)

Questa guida è un esempio di come utilizzare il tuo Jade, connesso via USB, ad un wallet watch-only. Electrum è un classico esempio, ma potresti preferire altri software wallet. Jade esporta la chiave pubblica su molti altri wallet: trova le funzioni simili che hai letto in questo tutorial, per orientarti e trovare come impiegarlo la tua companio app preferita.
