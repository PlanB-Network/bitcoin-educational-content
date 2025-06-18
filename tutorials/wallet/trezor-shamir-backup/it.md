---
name: Backup di Trezor Shamir
description: Frasi Mnemonic a condivisione singola e multipla su Trezor
---
![cover](assets/cover.webp)



*Credito immagine: [Trezor.io](https://trezor.io/)*



## Nuove opzioni di backup su Trezor



Dal 2023, Trezor offre un nuovo formato di backup chiamato ***Single-share Backup***, che sostituisce gradualmente il classico approccio basato sul BIP39 presente nella maggior parte dei portafogli. A differenza delle tradizionali frasi Mnemonic di 12 o 24 parole, questo nuovo formato si basa su una singola frase di 20 parole derivata da uno standard sviluppato dai SatoshiLabs: **SLIP39**. L'obiettivo è quello di migliorare la robustezza e la leggibilità dei backup, consentendo al contempo una migrazione senza problemi verso un modello di backup distribuito.



Questo modello distribuito è chiamato ***Multi-share Backup***. Si basa sullo stesso principio, ma invece di generare una singola frase Mnemonic, la divide in diversi frammenti chiamati ***quote***, ognuna delle quali è una frase Mnemonic a sé stante. Per ripristinare il portafoglio, è necessario riunire un certo numero di queste *parti* (definito da una *soglia*). Ad esempio, in uno schema 3 su 5, qualsiasi 3 *quote* delle 5 ripristinerà il portafoglio. Si noti che il sistema di backup distribuito di Trezor è diverso da quello dei portafogli Multisig. Per spendere i bitcoin, è necessario solo il proprio Hardware Wallet Trezor. È necessaria una sola firma. La distribuzione si applica solo al livello della frase Mnemonic, cioè al backup.



![Image](assets/fr/01.webp)



Questo sistema risolve il problema del singolo punto di guasto della frase Mnemonic senza gli svantaggi associati alla gestione di un Multisig o passphrase BIP39. Il processo di recupero non si basa più su un'unica informazione, ma su diverse, con l'ulteriore vantaggio della tolleranza alla perdita grazie alla soglia.



Gli utenti che hanno creato un portafoglio con *Single-share Backup* possono passare a *Multi-share Backup* in qualsiasi momento senza dover migrare il portafoglio. Gli indirizzi e gli account di ricezione rimarranno identici. Il sistema *Multi-share* riguarda solo il backup, mentre il resto del portafoglio rimane invariato.



Il backup multi-comparto* è disponibile su Trezor Model T, Safe 3 e Safe 5. Questa funzione non è supportata dal Trezor Model One.



**Nota importante:** Il sistema *Multi-share* di Trezor è crittograficamente sicuro, in quanto utilizza lo schema *Shamir's Secret Sharing* per la distribuzione. Si sconsiglia vivamente di applicare un sistema simile manualmente, dividendo da soli una frase classica di Mnemonic. È una pratica scorretta che comporta una significativa perdita di tempo. È una pratica scorretta che aumenta significativamente il rischio di furto e perdita dei bitcoin, quindi non fatelo. Una frase classica Mnemonic viene memorizzata nella sua interezza.



## La condivisione del segreto di Shamir in SLIP39



Il meccanismo crittografico alla base dei backup *multi-share* su Trezor è lo *Shamir's Secret Sharing Scheme* (SSSS). Il suo principio è il seguente: le informazioni segrete (in questo caso, il seed del portafoglio) vengono trasformate in un polinomio matematico. Vengono quindi calcolati diversi punti di questo polinomio, ognuno dei quali diventa una quota. Il segreto originale viene ricostruito per interpolazione polinomiale, raccogliendo un numero minimo di punti (la soglia).



Nessuna informazione segreta può essere dedotta da un numero di azioni inferiore alla soglia, garantendo una perfetta sicurezza teorica dell'informazione segreta. In altre parole, anche un attaccante con una potenza di calcolo illimitata non può indovinare seed se la soglia non viene raggiunta.



SLIP39 usa questo schema per distribuire il portfolio seed. Ogni azione è una frase di 20 parole, costruita a partire da un elenco di 1024 parole (diverso da quello di BIP39).



## Impostazione di un backup a condivisione multipla su Trezor



Quando create il vostro portafoglio su Trezor, avete tre diverse opzioni:




- Utilizzare una frase classica BIP39 Mnemonic di 12 o 24 parole;
- Utilizzare una frase Mnemonic a condivisione singola (SLIP39);
- Configurare più frasi Mnemonic in Multi-share (SLIP39).



Se si opta per una frase SLIP39 Mnemonic a quota singola, si potrà passare in un secondo momento a una frase a quota multipla senza dover reimpostare il portafoglio. D'altra parte, se iniziate con un portafoglio BIP39 classico (frase di 12 o 24 parole), non potrete convertirlo direttamente in un Multi-quote. Dovrete creare un nuovo portafoglio multi-azionario da zero e trasferire i vostri fondi dal vecchio portafoglio a quello nuovo tramite una o più transazioni Bitcoin. Si tratta di un'operazione più complessa e costosa. Si tratta di un'operazione più complessa e costosa. Se volete effettuare questa migrazione, vi consiglio di acquistare un nuovo Hardware Wallet Trezor per evitare di dover inserire il vostro seed in un software di portafoglio.



In questo tutorial vedremo innanzitutto come impostare una Multi-quota quando si crea un portafoglio, quindi, in una sezione successiva, vedremo come convertire una Singola-quota in una Multi-quota su un portafoglio esistente.



Se avete bisogno di aiuto per la configurazione iniziale del dispositivo, abbiamo anche un'esercitazione dettagliata per ogni modello di Trezor:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Su un nuovo portafoglio



Ora avete completato la configurazione iniziale del vostro Trezor e siete pronti a creare il portafoglio. In Trezor Suite, fare clic sul pulsante "*Crea nuovo Wallet*".



![Image](assets/fr/02.webp)



Scegliere l'opzione "*Multi-share Backup*", quindi fare clic su "*Crea Wallet*".



![Image](assets/fr/03.webp)



Accettare le condizioni d'uso sul proprio Trezor e confermare la creazione del portafoglio.



![Image](assets/fr/04.webp)



In Trezor Suite, fare clic su "*Continua il backup*".



![Image](assets/fr/05.webp)



Leggere attentamente le istruzioni, confermarle, quindi fare clic su "*Crea backup Wallet*".



![Image](assets/fr/06.webp)



Per ulteriori informazioni sul modo corretto di salvare e gestire le frasi Mnemonic, vi consiglio di seguire quest'altra guida, soprattutto se siete principianti:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sul Trezor, selezionare il numero totale di azioni che si desidera configurare. Le configurazioni più comuni sono 2-de-3 e 3-de-5. Per questo esempio, creerò un 2-de-3, quindi selezionerò 3 azioni. Ogni azione rappresenterà una frase Mnemonic di 20 parole.



*Per gli utenti di Safe 5, anche se sullo schermo apparirà la scritta "*Tap per continuare*", in realtà sarà necessario scorrere il dito verso l'alto per confermare



![Image](assets/fr/07.webp)



Confermare quindi la soglia, ossia il numero di azioni necessarie per riottenere l'accesso al Wallet e ai bitcoin in esso contenuti.



![Image](assets/fr/08.webp)



Il Trezor creerà le varie azioni (frasi Mnemonic) utilizzando il suo generatore di numeri casuali. Assicuratevi di non essere osservati durante questa operazione. Scrivete le parole fornite sullo schermo su un supporto fisico di vostra scelta. È importante che le parole siano numerate e in ordine sequenziale.



Vi consiglio di annotare ogni condivisione su un supporto separato e di gestirne attentamente l'archiviazione per evitare che diverse siano accessibili nello stesso luogo. Ad esempio, per una configurazione 2 su 3 come la mia, si potrebbe tenere una quota a casa mia, un'altra presso un amico fidato e l'ultima in una cassaforte della banca. La scelta dei luoghi di conservazione dipenderà dalla vostra strategia di sicurezza personale.



Nella parte superiore dello schermo è possibile vedere quale condivisione si sta visualizzando.



naturalmente, non dovete mai condividere queste parole su Internet, come sto facendo io in questa esercitazione. Questo esempio di Wallet sarà utilizzato solo sul Testnet e sarà cancellato alla fine del tutorial.**_



![Image](assets/fr/09.webp)



Per passare alle parole successive, fare clic sulla parte inferiore dello schermo. È possibile andare indietro scivolando verso il basso. Una volta scritte tutte le parole, tenere il dito sullo schermo per passare alla quota successiva e ripetere l'operazione.



![Image](assets/fr/10.webp)



Alla fine di ogni registrazione di condivisione, vi verrà chiesto di selezionare le parole della vostra frase Mnemonic per confermare che le avete scritte correttamente.



![Image](assets/fr/11.webp)



Ecco fatto, il backup del portafoglio è stato eseguito con successo utilizzando l'opzione Multi-share. Ora potete continuare con le altre istruzioni di configurazione.



### Su un portafoglio esistente di azioni singole



Se si possiede già un Trezor Wallet con un backup a condivisione singola (una frase SLIP39 Mnemonic, non la classica frase BIP39) e si desidera migliorare la disponibilità e la sicurezza del proprio backup Wallet, è possibile impostare un sistema a condivisione multipla senza dover trasferire i bitcoin.



A tal fine, collegare e sbloccare il Hardware Wallet. In Trezor Suite, andare su Impostazioni.



![Image](assets/fr/12.webp)



Andare alla scheda "*Device*".



![Image](assets/fr/13.webp)



Quindi fare clic su "*Crea backup multidiviso*".



![Image](assets/fr/14.webp)



Leggete le istruzioni, quindi fate clic su "*Crea backup multiscala*".



![Image](assets/fr/15.webp)



Dovrete quindi inserire la vostra attuale frase Mnemonic (a condivisione singola) sullo schermo del vostro Trezor. Selezionare il numero di parole (l'impostazione predefinita è 20).



![Image](assets/fr/16.webp)



Quindi utilizzare la tastiera su schermo del Trezor per inserire ogni parola della frase Mnemonic corrente.



![Image](assets/fr/17.webp)



A questo punto è possibile scegliere la configurazione del backup multisala seguendo le istruzioni fornite nella sezione precedente.



![Image](assets/fr/18.webp)



Una volta creato il backup multidividuale, è necessario decidere cosa fare con la frase Mnemonic originale a condivisione singola. Poiché il portafoglio Bitcoin rimane lo stesso, questa frase singola consentirà sempre di accedervi. Ciò dipende dalla vostra strategia di sicurezza, ma in generale è consigliabile distruggere questa frase per eliminare questo singolo punto di errore, che è proprio l'obiettivo di Multi-share Backup. Se decidete di distruggerla, assicuratevi di farlo in modo sicuro, poiché **dà ancora accesso ai vostri bitcoin**.



Congratulazioni, ora siete al corrente dell'uso dei backup a condivisione singola e multipla sui portafogli hardware Trezor. Se volete fare un ulteriore passo avanti nella sicurezza del Wallet, date un'occhiata a questo tutorial sulle passphrase BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Se avete trovato utile questa esercitazione, vi sarei grato se lasciaste un pollice Green qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie mille!



## Risorse aggiuntive





- [SLIP-0039: Condivisione del segreto di Shamir per codici Mnemonic](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Backup multi-condiviso su Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Condivisione segreta di Shamir](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).