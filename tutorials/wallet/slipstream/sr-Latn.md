---
name: Slipstream
description: Slanje potpisane transakcije direktno rudaru pomoću Slipstream-a, bez emitovanja na Bitcoin mrežu
---

![cover](assets/cover.webp)

Kada potpišete transakciju, ona se po pravilu automatski emituje ka svim Bitcoin čvorovima na mreži. Zatim čeka da bude iskopana.

Međutim, sve dok nije u bloku, napadač koji je došao do vašeg privatnog ključa mogao bi da je zameni i ukrade sredstva. To je tipično slučaj ako koristite ColdCard hardware wallet.

Alat Slipstream rudarske kompanije MARA omogućava vam da zaobiđete emitovanje transakcije na mrežu: ona se šalje direktno (i isključivo) jednom rudaru, čime ostaje privatna i ne izlaže se na mreži. Transakciji će verovatno trebati više vremena da bude iskopana, ali će biti zaštićena od napada zamenom.

U nastavku nudimo vodič koji korisnicima [Liane](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), kao i korisnicima novčanika [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), omogućava da koriste Slipstream alat rudara MARA preko stranice [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Upozorenje**: ovaj alat je namenjen samo određenim profilima, prevashodno Liana novčanicima, miniscript novčanicima i pojedinim vrstama multisig-a. Wizardsardine **izričito savetuje da se ne koristi** za novčanike čija su sredstva već u kritičnoj opasnosti od krađe, na primer one čija je fraza za oporavak generisana na ColdCard uređaju pogođenom ranjivošću generatora slučajnih brojeva. U toj situaciji, trka sa napadačem meri se u sekundama, a transakciji poslatoj jednom jedinom rudaru treba mnogo više vremena da bude potvrđena nego onoj koja je normalno emitovana. Ako se ovo odnosi na vas, prvo pročitajte naš posebni vodič:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Za korisnike Liane

Lianu održava Wizardsardine, izdavač stranice [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), pa je put direktan: jednostavno izvezete potpisani PSBT fajl umesto da ga emitujete.

*Preduslov: imati sredstva na svom Liana novčaniku.*

### Korak 1: Kreirajte transakciju pomoću Liane

Kao i obično, sastavite transakciju dodavanjem odredišne adrese, opisa i iznosa (ovde, maksimum dostupan u novčaniku).

Da biste podesili stopu naknade:

- izaberite novčiće koje želite da potrošite klikom na malo polje dole levo, ispod „Coins selection”;
- zatim unesite stopu naknade. Ne zaboravite da podesite naknade znatno više od predložene stope, kako je opisano na ovoj stranici: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Na kraju kliknite na „Next”.

![Sastavljanje transakcije u Liani](assets/fr/01.webp)

### Korak 2: Proverite detalje svoje transakcije

Pre nego što kliknete na „Sign”, proverite detalje svoje transakcije, a naročito:

- poslati iznos;
- broj satošija namenjenih naknadama za transakciju;
- ali pre svega, adresu na koju šaljete sredstva (ne zaboravite da proverite prvih 5/6 karaktera, poslednjih 5/6 i 5/6 karaktera u sredini adrese, kako biste izbegli napade tipa „address poisoning”).

![Provera detalja transakcije](assets/fr/02.webp)

### Korak 3: Izaberite novčanike za potpisivanje

Zatim izaberite software i/ili hardware wallet-e kojima treba da potpišete transakciju. Kratak podsetnik: kod multisig novčanika 2 od 2, potrebna su vam 2 potpisa od 2.

### Korak 4: Izvezite PSBT fajl svoje transakcije

Bitcoin transakcija je sada potpisana odgovarajućim ključevima. Nemojte kliknuti na „Broadcast”, jer će u suprotnom biti podeljena sa celom mrežom i, ako koristite ColdCard hardware wallet, vaša transakcija će biti javno izložena, a vaša sredstva ugrožena.

Sada možete kliknuti na „Export” i sačuvati PSBT fajl lokalno na svom računaru.

![Izvoz PSBT fajla iz Liane](assets/fr/03.webp)

### Korak 5: Pošaljite transakciju rudaru preko outofband.wizardsardine.com

Sada dolaze poslednji koraci. Da biste transakciju poslali rudaru, dovoljno je da uzmete PSBT fajl i prevučete ga i otpustite u za to predviđeno polje.

![Otpuštanje PSBT fajla na outofband.wizardsardine.com](assets/fr/04.webp)

Transakcija se potom prikazuje kao na slici ispod.

![Transakcija u redu čekanja](assets/fr/05.webp)

### Korak 6: Pošaljite transakciju preko Slipstream-a

Na kraju, dovoljno je da kliknete na „Send” kako bi transakcija bila poslata kompaniji MARA preko Slipstream-a.

![Slanje transakcije preko Slipstream-a](assets/fr/06.webp)

U roku od nekoliko sekundi, transakcija zatim prelazi iz stanja „Sending” u „Accepted”:

![Transakcija prihvaćena od strane Slipstream-a](assets/fr/07.webp)

Preostaje samo da kopirate identifikator transakcije (TXID), a zatim ga nalepite u [mempool.space](https://mempool.space/) kako biste pratili kada bude iskopana:

![Pretraga TXID-a na mempool.space](assets/fr/08.webp)

Imajte u vidu: transakcija će se prikazivati kao „Transaction not found” sve dok rudar MARA ne iskopa blok i u njega ne uključi vašu transakciju. To može potrajati nekoliko desetina minuta, pa čak i satima, jer MARA drži samo oko 4,5% hashrate-a Bitcoin mreže. Zaključno sa 4. avgustom 2026. godine, to odgovara otprilike jednom iskopanom bloku na svaka 3 sata i 45 minuta.

## Za korisnike drugih novčanika

Ako ne koristite [Lianu](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) a ipak želite da koristite ovaj alat, evo vodiča na primeru multisig novčanika 2 od 2. Za to ćemo koristiti software wallet [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Preduslov: imati sredstva na svom Sparrow novčaniku.*

### Korak 1: Kreirajte transakciju

U [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)-u kreirajte transakciju na svom multisig novčaniku. Ne zaboravite da podesite naknade znatno više od predložene stope, kako je opisano na ovoj stranici: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Kada je sastavite, kliknite na „Create Transaction”.

![Kreiranje transakcije u Sparrow-u](assets/fr/09.webp)

### Korak 2: Finalizujte svoju transakciju

Da biste finalizovali transakciju, sada je treba potpisati. Za to kliknite na „Finalize Transaction for Signing”.

![Finalizovanje transakcije radi potpisivanja](assets/fr/10.webp)

### Korak 3: Potpišite transakciju svojim različitim ključevima

Sada je došlo vreme da potpišete transakciju. Za to je jednostavno potpišite pomoću software ili hardware wallet-a koje koristite.

![Potpisivanje transakcije multisig ključevima](assets/fr/11.webp)

### Korak 4: Preuzmite potpisanu transakciju i nemojte je emitovati na mrežu

Bitcoin transakcija je sada potpisana obama ključevima našeg multisig-a 2 od 2. Nemojte kliknuti na „Broadcast Transaction”, jer će u suprotnom biti podeljena sa celom mrežom i, ako koristite ColdCard hardware wallet, vaša transakcija će biti javno izložena, a vaša sredstva ugrožena.

![Potpisana transakcija, spremna ali ne i emitovana](assets/fr/12.webp)

### Korak 5: Prikažite skriptu potpisane transakcije ili preuzmite PSBT fajl

Da biste prikazali potpisanu Bitcoin transakciju, sada kliknite na „View Final Transaction”. Zatim možete kopirati skriptu potpisane Bitcoin transakcije:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Prikaz skripte potpisane transakcije](assets/fr/13.webp)

Ako želite da preuzmete fajl transakcije, možete:

- kliknuti na „File”, pa na „Save transaction…”;
- ili kliknuti na dugme za mrežnu konekciju dole desno (žuto dugme), a zatim na „Save Final Transaction”.

Transakcija će zatim biti sačuvana lokalno na vašem računaru.

![Čuvanje finalne transakcije lokalno](assets/fr/14.webp)

### Korak 6: Pošaljite transakciju rudaru preko outofband.wizardsardine.com

Sada dolaze poslednji koraci. Da biste transakciju poslali rudaru, dovoljno je da:

- odete na [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- nalepite skriptu potpisane transakcije kopiranu u prethodnom koraku, a zatim kliknete na „ADD TO QUEUE” ispod;

![Lepljenje skripte transakcije u alat](assets/fr/15.webp)

- ili uzmete fajl i prevučete ga i otpustite u za to predviđeno polje.

![Otpuštanje fajla transakcije u alat](assets/fr/16.webp)

Transakcija se potom prikazuje kao na slici ispod.

![Transakcija u redu čekanja](assets/fr/17.webp)

Ako vam poruka kaže da je ukupan ulazni iznos satošija u vašoj transakciji nepoznat (i da se, usled toga, broj satošija za naknade ne može izračunati), dovoljno je da ručno unesete ukupan ulazni iznos satošija. Da biste ga pronašli, samo kliknite na prikaz svoje transakcije u Sparrow-u, na sredini dijagrama:

![Ukupan ulazni iznos prikazan u Sparrow-u](assets/fr/18.webp)

Zatim unesite taj iznos (15.904 satošija u našem primeru) u alat [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Ručno unošenje ukupnog ulaznog iznosa](assets/fr/19.webp)

Na kraju, proverite da li je stopa naknade ispravna.

### Korak 7: Pošaljite transakciju preko Slipstream-a

Na kraju, dovoljno je da kliknete na „Send” kako bi transakcija bila poslata kompaniji MARA preko Slipstream-a.

![Slanje transakcije preko Slipstream-a](assets/fr/20.webp)

U roku od nekoliko sekundi, transakcija zatim prelazi iz stanja „Sending” u „Accepted”:

![Transakcija prihvaćena od strane Slipstream-a](assets/fr/21.webp)

Preostaje samo da kopirate identifikator transakcije (TXID), a zatim ga nalepite u [mempool.space](https://mempool.space/) kako biste pratili kada bude iskopana:

![Pretraga TXID-a na mempool.space](assets/fr/22.webp)

Imajte u vidu: transakcija će se prikazivati kao „Transaction not found” sve dok rudar MARA ne iskopa blok i u njega ne uključi vašu transakciju. To može potrajati nekoliko desetina minuta, pa čak i satima, jer MARA drži samo oko 4,5% hashrate-a Bitcoin mreže. Zaključno sa 4. avgustom 2026. godine, to odgovara otprilike jednom iskopanom bloku na svaka 3 sata i 45 minuta.
