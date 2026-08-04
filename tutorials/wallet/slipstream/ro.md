---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

În mod normal, când semnezi o tranzacție, aceasta este transmisă automat (broadcast) către toate nodurile din rețeaua Bitcoin. Apoi așteaptă să fie minată.

Totuși, atâta timp cât nu se află într-un bloc, un atacator care a obținut cheia ta privată o poate înlocui și fura fondurile. Acesta este de obicei cazul dacă folosești un portofel hardware ColdCard.

Instrumentul Slipstream, oferit de compania de minerit MARA, îți permite să eviți transmiterea tranzacției către rețea: aceasta este trimisă direct (și exclusiv) unui miner, ceea ce o păstrează privată și evită expunerea ei în rețea. Tranzacția va dura probabil mai mult până va fi minată, dar va fi protejată împotriva unui atac de înlocuire (replacement attack).

Mai jos, îți oferim un tutorial care le permite utilizatorilor [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), precum și utilizatorilor portofelului [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), să folosească instrumentul Slipstream al minerului MARA prin intermediul paginii [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Avertisment**: acest instrument este destinat doar anumitor profiluri, în principal portofelelor Liana, portofelelor miniscript și anumitor tipuri de multisig. Wizardsardine **recomandă explicit să nu îl folosești** pentru portofele ale căror fonduri sunt deja expuse unui risc critic de furt, de exemplu cele a căror frază de recuperare a fost generată pe un dispozitiv ColdCard afectat de vulnerabilitatea generatorului de numere aleatorii. În această situație, cursa contra atacatorului se măsoară în secunde, iar o tranzacție trimisă către un singur miner durează mult mai mult să se confirme decât una transmisă în mod normal. Dacă acest lucru te privește, citește mai întâi tutorialul nostru dedicat:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Pentru utilizatorii Liana

Liana este întreținut de Wizardsardine, editorul paginii [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), astfel încât drumul este direct: pur și simplu exporți fișierul PSBT semnat în loc să-l transmiți către rețea.

*Cerință prealabilă: să ai fonduri în portofelul tău Liana.*

### Pasul 1: Creează tranzacția cu Liana

Ca de obicei, construiește-ți tranzacția adăugând adresa de destinație, descrierea și suma (aici, maximul disponibil în portofel).

Pentru a seta rata comisionului:

- selectează monedele pe care vrei să le cheltuiești făcând clic pe caseta mică din stânga jos, sub „Coins selection”;
- apoi introdu rata comisionului. Nu uita să setezi comisioane mult mai mari decât rata sugerată, așa cum este descris pe această pagină: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

În cele din urmă, dă clic pe „Next”.

![Building the transaction in Liana](assets/fr/01.webp)

### Pasul 2: Verifică detaliile tranzacției

Înainte de a da clic pe „Sign”, verifică detaliile tranzacției; în special:

- suma trimisă;
- numărul de satoshi alocați comisioanelor de tranzacție;
- dar mai presus de toate, adresa către care trimiți fondurile (nu uita să verifici primele 5/6 caractere, ultimele 5/6, și 5/6 caractere din mijlocul adresei pentru a evita atacurile de tip „address poisoning”).

![Checking the transaction details](assets/fr/02.webp)

### Pasul 3: Selectează portofelele de semnare

În continuare, selectează portofelele software și/sau hardware cu care ai nevoie să semnezi tranzacția. Un mic reminder: în cazul unui portofel multisig 2-din-2, ai nevoie de 2 semnături din 2.

### Pasul 4: Exportă fișierul PSBT al tranzacției

Tranzacția Bitcoin este acum semnată de cheile corespunzătoare. Nu da clic pe „Broadcast”, altfel va fi partajată cu întreaga rețea și, dacă folosești un portofel hardware ColdCard, tranzacția ta va fi expusă public iar fondurile tale vor fi în pericol.

Acum poți da clic pe „Export”, apoi salvezi fișierul PSBT local, pe calculatorul tău.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Pasul 5: Trimite tranzacția către miner prin outofband.wizardsardine.com

Acum urmează pașii finali. Pentru a trimite tranzacția către miner, tot ce trebuie să faci este să iei fișierul PSBT și să-l tragi (drag and drop) în zona desemnată.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

Tranzacția este apoi afișată așa cum se arată mai jos.

![Transaction in the queue](assets/fr/05.webp)

### Pasul 6: Trimite tranzacția prin Slipstream

În final, tot ce trebuie să faci este să dai clic pe „Send” pentru ca tranzacția să fie trimisă către MARA prin Slipstream.

![Sending the transaction via Slipstream](assets/fr/06.webp)

În câteva secunde, tranzacția trece apoi de la „Sending” la „Accepted”:

![Transaction accepted by Slipstream](assets/fr/07.webp)

Tot ce mai rămâne de făcut este să copiezi identificatorul tranzacției (TXID), apoi să-l lipești pe [mempool.space](https://mempool.space/) pentru a urmări cum este minată:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Reține: tranzacția va apărea ca „Transaction not found” până când minerul, MARA, minează un bloc și include tranzacția ta în el. Acest lucru poate dura câteva zeci de minute, sau chiar ore, deoarece MARA deține doar aproximativ 4,5% din puterea de calcul (hash rate) a rețelei Bitcoin. Începând cu 4 august 2026, acest lucru corespunde cu aproximativ un bloc minat la fiecare 3 ore și 45 de minute.

## Pentru utilizatorii altor portofele

Dacă nu folosești [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), dar tot vrei să folosești instrumentul, iată un tutorial care utilizează un portofel multisig 2-din-2. Pentru aceasta, vom folosi portofelul software [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Cerință prealabilă: să ai fonduri în portofelul tău Sparrow.*

### Pasul 1: Creează tranzacția

Cu [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), creează tranzacția pe portofelul tău multisig. Nu uita să setezi comisioane mult mai mari decât rata sugerată, așa cum este descris pe această pagină: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Odată creată, dă clic pe „Create Transaction”.

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Pasul 2: Finalizează tranzacția

Pentru a-ți finaliza tranzacția, trebuie acum să o semnezi. Pentru aceasta, dă clic pe „Finalize Transaction for Signing”.

![Finalizing the transaction for signing](assets/fr/10.webp)

### Pasul 3: Semnează tranzacția cu diferitele tale chei

Acum a venit momentul să semnezi tranzacția. Pentru aceasta, semneaz-o pur și simplu cu portofelul (portofelele) software sau hardware pe care le folosești.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Pasul 4: Descarcă tranzacția semnată și nu o transmite către rețea

Tranzacția Bitcoin este acum semnată de ambele chei ale multisig-ului nostru 2-din-2. Nu da clic pe „Broadcast Transaction”, altfel va fi partajată cu întreaga rețea și, dacă folosești un portofel hardware ColdCard, tranzacția ta va fi expusă public iar fondurile tale vor fi în pericol.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Pasul 5: Afișează scriptul tranzacției semnate sau descarcă fișierul PSBT

Pentru a afișa tranzacția Bitcoin semnată, dă acum clic pe „View Final Transaction”. Poți apoi copia scriptul tranzacției Bitcoin semnate:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Dacă vrei să descarci fișierul tranzacției, poți fie:

- să dai clic pe „File”, apoi pe „Save transaction…”;
- fie să dai clic pe butonul de conexiune la rețea din dreapta jos (butonul galben), apoi pe „Save Final Transaction”.

Tranzacția va fi apoi salvată local, pe calculatorul tău.

![Saving the final transaction locally](assets/fr/14.webp)

### Pasul 6: Trimite tranzacția către miner prin outofband.wizardsardine.com

Acum urmează pașii finali. Pentru a trimite tranzacția către miner, tot ce trebuie să faci este:

- să mergi pe [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- să lipești scriptul tranzacției semnate copiat la pasul anterior, apoi să dai clic pe „ADD TO QUEUE” mai jos;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- sau să iei fișierul și să-l tragi (drag and drop) în zona desemnată.

![Dropping the transaction file on the tool](assets/fr/16.webp)

Tranzacția este apoi afișată așa cum se arată mai jos.

![Transaction in the queue](assets/fr/17.webp)

Dacă un mesaj îți spune că suma totală de satoshi de la intrare (input) a tranzacției tale este necunoscută (și că, drept urmare, numărul de satoshi pentru comisioane nu poate fi calculat), trebuie pur și simplu să introduci manual suma totală de satoshi de la intrare. Pentru a o găsi, dă clic pe afișajul tranzacției tale în Sparrow, în mijlocul diagramei:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Apoi introdu acea sumă (15.904 sats în exemplul nostru) în instrumentul [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Manually entering the total input amount](assets/fr/19.webp)

În final, verifică dacă rata comisionului este corectă.

### Pasul 7: Trimite tranzacția prin Slipstream

În final, tot ce trebuie să faci este să dai clic pe „Send” pentru ca tranzacția să fie trimisă către MARA prin Slipstream.

![Sending the transaction via Slipstream](assets/fr/20.webp)

În câteva secunde, tranzacția trece apoi de la „Sending” la „Accepted”:

![Transaction accepted by Slipstream](assets/fr/21.webp)

Tot ce mai rămâne de făcut este să copiezi identificatorul tranzacției (TXID), apoi să-l lipești pe [mempool.space](https://mempool.space/) pentru a urmări cum este minată:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Reține: tranzacția va apărea ca „Transaction not found” până când minerul, MARA, minează un bloc și include tranzacția ta în el. Acest lucru poate dura câteva zeci de minute, sau chiar ore, deoarece MARA deține doar aproximativ 4,5% din puterea de calcul (hash rate) a rețelei Bitcoin. Începând cu 4 august 2026, acest lucru corespunde cu aproximativ un bloc minat la fiecare 3 ore și 45 de minute.
</content>
<parameter name="i">Write Romanian translation of Slipstream tutorial