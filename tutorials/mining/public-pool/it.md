---
name: Public Pool
description: Introduzione a Public Pool
---

![signup](assets/cover.webp)

**Public Pool** non è una piscina qualunque; è ciò che viene anche definito un **Solo Pool**. Se il tuo miner riesce a minare un blocco, allora raccogli l'intera ricompensa del blocco, che non viene condivisa con altri partecipanti della piscina o con la piscina stessa.

**Public Pool** fornisce solamente un **template di blocco** per il tuo miner affinché possa svolgere il suo compito senza che tu debba avere un **nodo Bitcoin** e il software che comunica con il tuo miner. Dato che non stai unendo la tua potenza di calcolo con quella di altri partecipanti, le tue possibilità di minare con successo un blocco sono ovviamente molto basse, assomigliando in qualche modo a un sistema di lotteria, dove a volte un individuo fortunato vince il jackpot.

![signup](assets/1.webp)

Nel **Dashboard** di **Public Pool**, hai comunque alcune statistiche come l'**Hashrate Totale** della piscina così come una distribuzione dei diversi tipi di miner che sono connessi alla piscina.

![signup](assets/2.webp)

Nelle prime righe, possiamo vedere **Bitaxe** con 1323 **Bitaxe** connessi per un totale di 649TH/s. **Bitaxe** è un progetto **Open source** che permette il semplice riutilizzo di un chip da un **ASIC** come l'**Antminer S19** su una scheda elettronica **opensource** per creare un piccolo miner di 0.5TH/s per 15W. Questo è il miner che useremo come esempio per questo tutorial.

## Aggiungere un **Worker** 👷‍♂️

![signup](assets/cover.webp)

In cima alla pagina, puoi copiare l'indirizzo della piscina **stratum+tcp://public-pool.io:21496**.

Successivamente, per il campo **user**, inserisci un indirizzo **Bitcoin** che possiedi.

Se hai più miner, puoi inserire lo stesso indirizzo per tutti loro così che i loro **hashrate** siano combinati e appaiano come un singolo miner. Puoi anche distinguerli aggiungendo un nome distinto a ciascuno. Per fare ciò, aggiungi semplicemente **.workername** dopo l'indirizzo **Bitcoin**.

Infine, per il campo **password**, usa **‘x’**.

Esempio: Se il tuo indirizzo **Bitcoin** è **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** e desideri nominare il tuo miner **« Brrrr »**, allora inserirai le seguenti informazioni nell'interfaccia del tuo miner:

- **URL**: stratum+tcp://public-pool.io:21496
- **USER**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Password**: **‘x’**
Se il tuo miner è un **Bitaxe**, i campi sono un po' diversi, ma le informazioni rimangono le stesse:
- **URL**: public-pool.io (qui, devi rimuovere la parte all'inizio **‘stratum+tcp://’** e la parte alla fine **‘:21496’** che verrà riportata nel campo della porta)
- **Porta**: 21496
- **User**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Password**: **‘x’**

![signup](assets/3.webp)
Pochi minuti dopo aver iniziato il mining, sarai in grado di vedere i tuoi dati sul sito web del **Public Pool** cercando il tuo indirizzo.
## Dashboard

![signup](assets/4.webp)

Una volta connesso al **Public Pool**, puoi accedere alla tua **Dashboard** cercando con il tuo indirizzo **Bitcoin** che hai inserito nel campo **Utente**. Nel nostro caso qui, è **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

Sulla **Dashboard**, vengono visualizzate diverse informazioni sia sui tuoi dati che sulla rete.

![signup](assets/5.webp)

Hai il **Network Hash Rate** che corrisponde alla potenza lavorativa totale della rete **Bitcoin**.

La **Difficoltà di Rete** indica la difficoltà che deve essere raggiunta per validare un blocco.

E la **Tua Migliore Difficoltà** è la più alta difficoltà che hai raggiunto. Se, per caso 🍀, raggiungi la difficoltà della rete, allora vinci l'intera ricompensa del blocco... dopo 100 blocchi. Dovresti aspettare 100 blocchi prima di poterli spendere.

Hai anche l'**Altezza del Blocco** che è il numero dell'ultimo blocco che è stato minato così come il suo peso espresso in WU, il massimo essendo 4.000.000.

Qui sotto, puoi vedere tutte le statistiche di ciascuno dei tuoi dispositivi individualmente se hai dato loro un nome distinto aggiungendo **.name** dietro il tuo indirizzo **Bitcoin** nel campo **Utente**.