---
name: SAFU Ninja
description: Salvate il vostro seed con il metodo SAFU Ninja
---

![cover](assets/cover.webp)


## 1. Introduzione



Il metodo **Ninja SAFU** è una soluzione **DIY (Do It Yourself)** che consente di creare un backup **sostenibile, sicuro e discreto** della propria **frase seed** (una frase Mnemonic di 12 o 24 parole definita dallo standard **BIP-39**). Questa frase è essenziale per ripristinare un Bitcoin Wallet o qualsiasi altro Wallet compatibile.



Invece di scrivere le vostre parole su carta - un metodo semplice ma vulnerabile - le inciderete su **rondelle in acciaio inossidabile**, assemblate su un **Bolt**. Il risultato è un backup compatto, resistente al fuoco, alla corrosione, all'acqua e agli urti. A differenza della carta, che può essere distrutta dalle fiamme, dall'umidità o dal tempo, l'acciaio inossidabile garantisce una conservazione a lungo termine, anche in condizioni estreme (fino a 1300°C o 20 tonnellate di pressione).



L'approccio Ninja SAFU offre diversi vantaggi:





- **Riservatezza**: Non si acquista un prodotto identificato come destinato al backup delle criptovalute. I componenti sono standard (rondelle, bulloni, scatola metallica), disponibili nei negozi di ferramenta, il che riduce il rischio di essere presi di mira in caso di fuga di dati da un fornitore specializzato.





- **Convenienza**: Questa soluzione costa tra i **15 e i 140 euro**, a seconda degli strumenti già in vostro possesso.





- **Affidabilità**: Testato dal 2020, il metodo è stato provato e testato da esperti di sicurezza come [Jameson Lopp](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/), che lo hanno sottoposto a rigorosi stress test (calore estremo, corrosione, pressione meccanica).



Questa guida passo passo vi mostrerà come realizzare il vostro backup Ninja SAFU, per proteggere meglio i vostri bitcoin da perdite o distruzioni. Se volete saperne di più sul backup e sulla protezione di una frase seed, consultate le appendici.




## 2. Hardware



Per creare un backup Ninja SAFU, sono necessari i seguenti componenti, tutti disponibili presso i negozi di hardware o online.



### 2.1 Materiali necessari





- Rondelle in acciaio inox (consigliate M8):
- **Materiale**: Acciaio inox (ad es. 304 o V4A per una maggiore resistenza alla corrosione)
- **Dimensioni**: M8 (diametro interno 8 mm, diametro esterno ~24 mm). Le rondelle M6 sono troppo piccole e difficili da incidere.
- **Quantità**: 12 o 24 rondelle per una frase standard seed, più le rondelle opzionali (vedere sezione 3.4) e una decina per i test o gli errori.





- Bolt e dado (M8) in acciaio inox ** :
- **Specifiche**: Bolt Lunghezza da 2,5 a 5 cm, a seconda del numero e dello spessore delle rondelle, diametro 8 mm. Un dado ad alette facilita l'apertura senza attrezzi, ma è possibile utilizzare anche un semplice dado.



![image](assets/fr/03.webp)





- **Set di punzoni per lettere e numeri (3 mm o 6 mm)**:
- **Specifiche**: i caratteri alti 6 mm facilitano la leggibilità e possono essere preferiti se parte della scritta è degradata. Scegliere un set robusto per un uso ripetuto.



![image](assets/fr/04.webp)





- **Martello o mazza**:
    - Per ottenere una forza di stampaggio sufficiente e precisa, è preferibile utilizzare una mazza





- **Incudine o superficie robusta**:
 - Una superficie spessa e Hard (ad esempio, un'incudine da 1 kg o una pietra di 10 cm) per assorbire gli urti.



Se non volete investire in un set di punzoni, potete anche incidere le vostre rondelle con una penna da incisione. Questa soluzione è spesso più economica, ma richiede maggiore attenzione per ottenere un risultato soddisfacente.



### 2.2 Strumenti opzionali





- **Dispositivo di timbratura**: Trattiene la rondella e guida il punzone, consentendo una timbratura precisa e pulita, un migliore orientamento e una spaziatura uniforme delle lettere



![image](assets/fr/05.webp)





- **Dispositivi di sigillatura**: Sacchetto sigillato o striscia sigillante



![image](assets/fr/06.webp)





- **Contenitore ermetico**: Per conservare il blocco di rondelle



![image](assets/fr/07.webp)


### 2.3 Sicurezza





- Si consigliano **guanti** e **occhiali di sicurezza**.
- Chiave per tubi in cui infilare il punzone, in modo da tenere il punzone con la chiave per tubi e non con le dita.



### 2.4 Quantità e costi stimati





- **Quantità per un backup di 24 parole**: 24 rondelle (minimo), 1 Bolt, 1 dado ad alette, 1 set di punzoni, 1 martello/massetta, 1 incudine/supporto.





- **Costo totale**:
 - Rondelle e bulloni/dadi: ~ 15 EUR
 - Set di punzoni: ~ 45 EUR
 - Custodia protettiva: ~ 55 EUR
 - Con tutti gli accessori: ~ 140 EUR





- Vedere l'appendice per l'attrezzatura campione.




## 3. Istruzioni passo-passo



1. **Preparazione:**




 - Luogo privato, senza telecamere (compresi gli smartphone)
 - Superficie robusta che assorbe gli urti
 - Guanti e occhiali di sicurezza
 - Pulire le rondelle da grasso e sporco
 - Pratica sulle rondelle di prova


2. **L'incendio di Mnemonic parole** :




    - Incidere la parola completa su un lato. Non limitatevi alle prime 4 lettere, nel caso in cui la quarta sia danneggiata.
    - Colpire con forza con il martello, tenendo il punzone con una chiave per tubi


3. **Numero delle rondelle** :




    - Sullo stesso lato, incidere la parola numero di posizione, indispensabile se le rondelle si allentano.


4. **Informazioni di registrazione** (facoltative e consigliate) :




    - Incidere la parola ridondante sull'altro lato del disco
    - Incisione di un identificativo Wallet su una rondella aggiuntiva
    - Incidere il percorso di derivazione del conto in uso su una rondella aggiuntiva. Queste informazioni si trovano nelle impostazioni del software di portafoglio. Ad esempio, per un portafoglio standard Taproot, il percorso di derivazione predefinito sarà: `m / 86' / 0' / 0' /`
    - Digitare il codice PIN per sbloccare il Hardware Wallet o le parole anti-phishing se si utilizza una COLDCARD.


5. **Non bruciare il passphrase :**




 - Se si usa un passphrase, assicurarsi di non scriverlo sulla stessa scheda del Mnemonic. Il passphrase è stato concepito per proteggere il Wallet in caso di furto del Mnemonic. Ulteriori informazioni nell'appendice.


6. **Controllo della leggibilità** :




    - Assicuratevi che ogni parola e numero sia chiaro e leggibile.


7. **Montare le rondelle** :




    - Infilare le rondelle sul Bolt nell'ordine dei numeri.
    - Opzionale: aggiungere rondelle vuote alle estremità.
    - Avvitare il dado ad alette per fissare la batteria.
    - Serrare saldamente per aumentare la protezione contro l'acqua, il fuoco e le sollecitazioni meccaniche.


8. **Test backup** :




    - Dal nuovo backup, provare a ripristinare il portfolio
- **Sigillatura del backup** (facoltativa e consigliata):
 - In strisce sigillate o in buste sigillate.
 - Se utilizzate una busta, annotate il suo numero di identificazione unico, in modo da poter verificare che si tratti della busta giusta e non di un'esca che sostituisce l'originale.




## 4. Immagazzinamento



### 4.1 Scegliere un luogo adatto



Conservare il backup in un **luogo discreto**, lontano da occhi indiscreti e accessibile per controlli periodici. Scegliete un **deposito ignifugo e impermeabile**, a casa o in un luogo sotto il vostro **esclusivo controllo**.



Evitate i luoghi in cui dipendete da una terza parte (cassaforte bancaria, notaio): perderete l'accesso autonomo ai vostri fondi, il che va contro i principi di sovranità della Bitcoin.



Non rivelate mai che utilizzate un metodo come Ninja SAFU. La discrezione è un Layer di sicurezza a tutti gli effetti.



### 4.2 Ridondanza



Se necessario, creare **diverse copie** e conservarle in **luoghi geografici diversi**.


Anche se i materiali scelti per il vostro dispositivo sono resistenti all'acqua e al fuoco, non sarete in grado di accedervi se è sepolto sotto m3 di macerie nella vostra casa e sarà molto difficile, se non impossibile, recuperarlo.




## 5. Follow-up e manutenzione



Anche se ben conservato, il backup deve essere **controllato regolarmente**:





- Non in vista, ispezionare il backup **una o due volte l'anno**.
- In caso di **degradazione delle incisioni**, ricreare un nuovo backup, **verificarlo**, quindi **distruggere con cura la vecchia copia**.
- Se il backup è in una busta sigillata :
 - Controllare il proprio login
 - Verificare la sua integrità
 - Aprite regolarmente la busta per controllare le condizioni delle incisioni e, se tutto è a posto, mettete la copia di riserva in una nuova tasca




**STAY SAFU !**


![image](assets/fr/08.webp)




## APPENDICI



### A.1 Salvare la frase di recupero



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### A.2 Comprensione del passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

### A.3 Come funzionano i portafogli Bitcoin



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### A.4 Classificazione del metodo Ninja SAFU



Secondo Jameson Lopp:





- [Relazione](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/) sul metodo Ninja SAFU





- Tabella di confronto [completa](https://jlopp.github.io/metal-Bitcoin-storage-reviews/?ref=blog.lopp.net)





- Tabella parziale :


![image](assets/fr/09.webp)



### A.5 Esempio di hardware





- **Rondelle** per
 - [Titano](https://pleb.style/fr-fr/products/disques-de-seed-supplementaires-titan-Wallet)
- Rondelle + dado + **custodia protettiva** (per le rondelle)
 - [Titano](https://pleb.style/fr-fr/products/titan-Wallet-premium-acier-steel-Wallet-backup?variant=50022696419664)
 - [TerraSteel](https://pleb.style/fr-fr/products/terrasteel-Wallet-plebstyle-acier-backup)
- Set di punzoni
 - [PlebStyle](https://pleb.style/fr/products/schlagstempelset-a-z-0-9-3mm)
- **Base della tipizzazione**
 - [PlebStyle](https://pleb.style/fr/products/schlagunterlage-10cm-x-10cm-x-1-5cm)
- **Dispositivo di maschiatura** (guida)
 - [TerraSteel](https://pleb.style/fr-fr/products/zubehor-einschlag-vorrichtung?_pos=1&_sid=2767fd66f&_ss=r)
- Dispositivo di tenuta
 - [Astuccio sigillato](https://pleb.style/fr/products/zubehor-5x-sicherheitstasche-tamper-evident)
 - [Strisce di tenuta](https://pleb.style/fr/products/zubehor-5x-siegel-streifen-fur-dein-seed-backup)
- **Kit completo**
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-diy-kit-premium-seed-backup-steelwallet-plebstyle?pr_prod_strat=e5_desc&pr_rec_id=aa9f36359&pr_rec_pid=8728733155664&pr_ref_pid=8730877788496&pr_seq=uniform)
 - [TerraSteel](https://pleb.style/fr-fr/products/kopie-von-terrasteel-Wallet-starter-kit)



Nota: i link ai negozi online sono forniti solo a titolo informativo.


Non esiste alcuna partnership commerciale tra Plan B e i venditori e produttori sopra citati.


Plan B non può essere ritenuta responsabile per difetti, variazioni di prezzo o problemi relativi alla qualità o alla consegna dei prodotti. **DYOR**




### A.6 Crediti fotografici



https://pleb.style/fr/


https://x.com/lopp/status/1463155802345193475


https://bitcointalk.org/index.php?topic=5389446.0


https://x.com/econoalchemist/status/1329271981712289797


https://www.waivio.com/@themarkymark/create-your-own-metal-seed-key-backup


https://github.com/minibolt-guide/minibolt/blob/main/bonus/Bitcoin/safu-ninja.md