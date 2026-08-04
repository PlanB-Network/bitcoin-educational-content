---
name: Slipstream
description: Odoslanie podpísanej transakcie priamo ťažiarovi pomocou nástroja Slipstream, bez jej vysielania do siete Bitcoin
---

![cover](assets/cover.webp)

Keď podpíšete transakciu, je za normálnych okolností automaticky rozoslaná všetkým uzlom Bitcoinu v sieti. Potom čaká na vyťaženie.

Kým však nie je v bloku, útočník, ktorý získal váš súkromný kľúč, ju môže nahradiť a prostriedky ukradnúť. To je typicky prípad, keď používate hardvérovú peňaženku ColdCard.

Nástroj Slipstream od ťažiarskej spoločnosti MARA umožňuje obísť vysielanie transakcie do siete: je odoslaná priamo (a len) jednému ťažiarovi, čo ju uchová v súkromí a zabráni jej vystaveniu v sieti. Vyťaženie transakcie bude pravdepodobne trvať dlhšie, ale bude chránená pred útokom nahradením.

Nižšie ponúkame návod, ktorý používateľom peňaženky [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), ako aj používateľom peňaženky [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), umožňuje používať nástroj Slipstream ťažiara MARA prostredníctvom stránky [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Upozornenie**: tento nástroj je určený len pre určité profily, predovšetkým pre peňaženky Liana, miniscriptové peňaženky a niektoré typy multisigu. Wizardsardine **výslovne neodporúča** jeho použitie pri peňaženkách, ktorých prostriedky sú už vystavené kritickému riziku krádeže, napríklad pri tých, ktorých obnovovacia fráza bola vygenerovaná na zariadení ColdCard postihnutom zraniteľnosťou generátora náhodných čísel. V takej situácii ide v pretekoch s útočníkom o sekundy a transakcia odoslaná jedinému ťažiarovi sa potvrdzuje oveľa dlhšie než transakcia bežne rozoslaná do siete. Ak sa vás to týka, prečítajte si najprv náš samostatný návod:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Pre používateľov peňaženky Liana

Lianu spravuje Wizardsardine, prevádzkovateľ stránky [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), takže cesta je priama: jednoducho exportujete podpísaný súbor PSBT namiesto toho, aby ste transakciu rozoslali do siete.

*Podmienka: mať prostriedky na svojej peňaženke Liana.*

### Krok 1: Vytvorte transakciu v Liane

Ako obvykle zostavte transakciu zadaním cieľovej adresy, popisu a sumy (tu maximum dostupné v peňaženke).

Nastavenie sadzby poplatkov:

- vyberte mince, ktoré chcete minúť, kliknutím na malé pole vľavo dole, pod "Coins selection";
- potom zadajte sadzbu poplatkov. Nezabudnite nastaviť poplatky oveľa vyššie, než je odporúčaná sadzba, ako je popísané na tejto stránke: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Nakoniec kliknite na "Next".

![Zostavenie transakcie v Liane](assets/fr/01.webp)

### Krok 2: Skontrolujte podrobnosti transakcie

Skôr než kliknete na "Sign", skontrolujte podrobnosti svojej transakcie, najmä:

- odosielanú sumu;
- počet satoshi vyhradených na transakčné poplatky;
- ale predovšetkým adresu, na ktorú prostriedky posielate (nezabudnite skontrolovať prvých 5/6 znakov, posledných 5/6 znakov a 5/6 znakov uprostred adresy, aby ste sa vyhli útokom typu "address poisoning").

![Kontrola podrobností transakcie](assets/fr/02.webp)

### Krok 3: Vyberte podpisujúce peňaženky

Ďalej vyberte softvérové a/alebo hardvérové peňaženky, ktorými potrebujete transakciu podpísať. Malá pripomienka: v prípade multisigovej peňaženky 2 z 2 potrebujete 2 podpisy z 2.

### Krok 4: Exportujte súbor PSBT svojej transakcie

Bitcoinová transakcia je teraz podpísaná príslušnými kľúčmi. Neklikajte na "Broadcast", inak bude zdieľaná s celou sieťou a v prípade, že používate hardvérovú peňaženku ColdCard, bude vaša transakcia verejne vystavená a vaše prostriedky budú ohrozené.

Teraz môžete kliknúť na "Export" a uložiť súbor PSBT lokálne do svojho počítača.

![Export súboru PSBT z Liany](assets/fr/03.webp)

### Krok 5: Odošlite transakciu ťažiarovi cez outofband.wizardsardine.com

Teraz k posledným krokom. Ak chcete transakciu odoslať ťažiarovi, stačí vziať súbor PSBT a presunúť ho myšou do vyznačenej oblasti.

![Presunutie súboru PSBT na outofband.wizardsardine.com](assets/fr/04.webp)

Transakcia sa potom zobrazí tak, ako je uvedené nižšie.

![Transakcia vo fronte](assets/fr/05.webp)

### Krok 6: Odošlite transakciu cez Slipstream

Nakoniec stačí kliknúť na "Send", aby bola transakcia odoslaná spoločnosti MARA cez Slipstream.

![Odoslanie transakcie cez Slipstream](assets/fr/06.webp)

V priebehu niekoľkých sekúnd transakcia prejde zo stavu "Sending" do stavu "Accepted":

![Transakcia prijatá nástrojom Slipstream](assets/fr/07.webp)

Zostáva už len skopírovať identifikátor transakcie (TXID) a vložiť ho do [mempool.space](https://mempool.space/), aby ste mohli sledovať jej ťaženie:

![Vyhľadanie TXID na mempool.space](assets/fr/08.webp)

Vezmite prosím na vedomie: transakcia sa bude zobrazovať ako "Transaction not found", kým ťažiar MARA nevyťaží blok a nezahrnie do neho vašu transakciu. Môže to trvať niekoľko desiatok minút, ba aj hodín, pretože MARA drží len zhruba 4,5 % hashrate siete Bitcoin. K 4. augustu 2026 to zodpovedá približne jednému vyťaženému bloku každé 3 hodiny a 45 minút.

## Pre používateľov iných peňaženiek

Ak nepoužívate [Lianu](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), ale napriek tomu chcete tento nástroj využiť, tu je návod využívajúci multisigovú peňaženku 2 z 2. Použijeme na to softvérovú peňaženku [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Podmienka: mať prostriedky na svojej peňaženke Sparrow.*

### Krok 1: Vytvorte transakciu

V [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) vytvorte transakciu na svojej multisigovej peňaženke. Nezabudnite nastaviť poplatky oveľa vyššie, než je odporúčaná sadzba, ako je popísané na tejto stránke: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Po vytvorení kliknite na "Create Transaction".

![Vytvorenie transakcie v Sparrow](assets/fr/09.webp)

### Krok 2: Finalizujte svoju transakciu

Aby ste svoju transakciu finalizovali, musíte ju teraz podpísať. Kliknite na "Finalize Transaction for Signing".

![Finalizácia transakcie na podpis](assets/fr/10.webp)

### Krok 3: Podpíšte transakciu svojimi rôznymi kľúčmi

Teraz prichádza čas transakciu podpísať. Jednoducho ju podpíšte softvérovou alebo hardvérovou peňaženkou (peňaženkami), ktoré používate.

![Podpísanie transakcie kľúčmi multisigu](assets/fr/11.webp)

### Krok 4: Stiahnite podpísanú transakciu a nevysielajte ju do siete

Bitcoinová transakcia je teraz podpísaná oboma kľúčmi nášho multisigu 2 z 2. Neklikajte na "Broadcast Transaction", inak bude zdieľaná s celou sieťou a v prípade, že používate hardvérovú peňaženku ColdCard, bude vaša transakcia verejne vystavená a vaše prostriedky budú ohrozené.

![Podpísaná transakcia, pripravená, ale nerozoslaná](assets/fr/12.webp)

### Krok 5: Zobrazte skript podpísanej transakcie alebo stiahnite súbor PSBT

Ak chcete zobraziť podpísanú bitcoinovú transakciu, kliknite teraz na "View Final Transaction". Potom môžete skopírovať skript podpísanej bitcoinovej transakcie:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Zobrazenie skriptu podpísanej transakcie](assets/fr/13.webp)

Ak chcete súbor transakcie stiahnuť, môžete buď:

- kliknúť na "File" a potom na "Save transaction…";
- alebo kliknúť na tlačidlo sieťového pripojenia vpravo dole (žlté tlačidlo) a potom kliknúť na "Save Final Transaction".

Transakcia sa potom uloží lokálne do vášho počítača.

![Uloženie finálnej transakcie lokálne](assets/fr/14.webp)

### Krok 6: Odošlite transakciu ťažiarovi cez outofband.wizardsardine.com

Teraz k posledným krokom. Ak chcete transakciu odoslať ťažiarovi, stačí:

- prejsť na [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- vložiť skript podpísanej transakcie skopírovaný v predchádzajúcom kroku a potom kliknúť na "ADD TO QUEUE" nižšie;

![Vloženie skriptu transakcie do nástroja](assets/fr/15.webp)

- alebo vziať súbor a presunúť ho myšou do vyznačenej oblasti.

![Presunutie súboru transakcie do nástroja](assets/fr/16.webp)

Transakcia sa potom zobrazí tak, ako je uvedené nižšie.

![Transakcia vo fronte](assets/fr/17.webp)

Ak vás správa upozorní, že celková vstupná suma satoshi vo vašej transakcii nie je známa (a že v dôsledku toho nemožno vypočítať počet satoshi na poplatky), stačí celkovú vstupnú sumu satoshi zadať ručne. Nájdete ju tak, že v Sparrow kliknete na zobrazenie svojej transakcie, doprostred diagramu:

![Celková vstupná suma zobrazená v Sparrow](assets/fr/18.webp)

Potom túto sumu (v našom príklade 15 904 satoshi) zadajte do nástroja [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Ručné zadanie celkovej vstupnej sumy](assets/fr/19.webp)

Nakoniec skontrolujte, či je sadzba poplatkov správna.

### Krok 7: Odošlite transakciu cez Slipstream

Nakoniec stačí kliknúť na "Send", aby bola transakcia odoslaná spoločnosti MARA cez Slipstream.

![Odoslanie transakcie cez Slipstream](assets/fr/20.webp)

V priebehu niekoľkých sekúnd transakcia prejde zo stavu "Sending" do stavu "Accepted":

![Transakcia prijatá nástrojom Slipstream](assets/fr/21.webp)

Zostáva už len skopírovať identifikátor transakcie (TXID) a vložiť ho do [mempool.space](https://mempool.space/), aby ste mohli sledovať jej ťaženie:

![Vyhľadanie TXID na mempool.space](assets/fr/22.webp)

Vezmite prosím na vedomie: transakcia sa bude zobrazovať ako "Transaction not found", kým ťažiar MARA nevyťaží blok a nezahrnie do neho vašu transakciu. Môže to trvať niekoľko desiatok minút, ba aj hodín, pretože MARA drží len zhruba 4,5 % hashrate siete Bitcoin. K 4. augustu 2026 to zodpovedá približne jednému vyťaženému bloku každé 3 hodiny a 45 minút.
