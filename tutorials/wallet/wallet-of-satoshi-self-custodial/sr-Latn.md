---
name: Wallet of Satoshi - Samostalno čuvanje
description: Saznajte kako da konfigurišete režim samostalnog čuvanja za Wallet of Satoshi portfelj
---

![cover](assets/cover.webp)



***Nisu tvoji ključevi, nisu tvoji novčići* je više od izreke, to je fundamentalni princip Bitcoin, što znači da ako ne kontrolišeš **privatne ključeve** koji otključavaju tvoje bitkoine, zapravo ih ne poseduješ.



Mnogi korisnici obično počinju sa **skrbničkim wallet**, zatim prelaze na **samostalno skrbnički wallet**, gde sami kontrolišu svoje privatne ključeve.


U ovom vodiču, nećemo vas upoznati sa novim samostalnim čuvanjem wallet. Umesto toga, predstavićemo vam novu funkciju ***Wallet of Satoshi*** wallets: **način samostalnog čuvanja**.



Cilj ove nove integracije je omogućiti korisnicima da zadrže kontrolu nad svojim privatnim ključevima, dok istovremeno uživaju u jednostavnosti i fluidnom korisničkom iskustvu.



Pre nego što pređemo na suštinu stvari, hajde da odvojimo trenutak da ispitamo poseban režim samostalnog čuvanja koji nudi Wallet of Satoshi (WoS).



## Posebna karakteristika režima samostalnog čuvanja



Jednostavnost i fluidnost WoS-ovog režima samostalnog čuvanja eliminiše složenost otvaranja Lightning kanala, upravljanja čvorovima... Ali kako je to moguće?



Wallet of Satoshi-ov režim samostalnog čuvanja pokreće **Spark**. Ovo je Layer 2 rešenje za Bitcoin, kreirano od strane Lightspark-a, koristeći tehnologiju **statechains**.



Kao rezultat toga, ne obavljate svoje transakcije direktno na Lightning Network. Interakcije između mreže **LN** i **Spark** odvijaju se putem **atomskih zamena**.



Na primer, Bob želi da plati Lightning fakturu koristeći WoS. On prenosi svoje satoshi, ali u pozadini, oni se usmeravaju ka **Spark Service Provider (SSP)** na Spark, koji zatim izvršava plaćanje na Lightning mreži.



Nasuprot tome, Alice želi da dobije sredstva direktno iz svog WoS portfolija. U ovom slučaju, **SSP** prima sats preko LN i odmah pripisuje Alice portfoliju.



Dakle, važno je napomenuti da, kako biste iskoristili jednostavnost i fluidnost WoS-a, morate se osloniti na Spark-ove servere. Međutim, u smislu sigurnosti, ako SSP postane zlonameran ili nedostupan, imate mehanizam **jednostranog izlaza**, sigurnosnu meru koja vam omogućava da povratite svoja sredstva na Bitcoin on-chain (čak i ako to može biti sporo i skupo), garantujući iskustvo samostalnog čuvanja sredstava uporedivo sa privatnim Lightning čvorom.



Uzimajući u obzir sve ove parametre, možete zatim odlučiti koliko sats želite zadržati u svom WoS samostalnom čuvanju.



Ako ste novi u Wallet of Satoshi, prirodno ćete morati preuzeti mobilnu aplikaciju wallet. Međutim, ako je već koristite i želite da saznate kako da koristite **mod samostalnog čuvanja**, molimo vas da odmah pređete na odeljak **Konfiguracija moda samostalnog čuvanja** ovog vodiča.



## Početak sa Wallet of Satoshi



Idite u svoju prodavnicu aplikacija i preuzmite WoS.



![screen](assets/fr/03.webp)



Otvorite aplikaciju kada se preuzimanje završi i pritisnite **Start**.



![screen](assets/fr/04.webp)



Bićete preusmereni na glavni interfejs aplikacije. U stvari, kada prvi put pristupite WoS-u, portfolio je već funkcionalan i sistematski se otvara u režimu starateljstva po podrazumevanim postavkama.



![screen](assets/fr/05.webp)



Čak i ako ne želite da koristite WoS u kustodijalnom režimu, preporučujemo da ga prvo konfigurišete. Da biste to uradili, pogledajte ovaj vodič.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Pređimo na konfiguraciju našeg WoS-a u samostalnom čuvanju.



## Konfiguracija režima samostalnog čuvanja



Kliknite na hamburger meni (ikona sa 3 trake) u gornjem desnom uglu glavnog interfejsa.



![screen](assets/fr/06.webp)



Zatim, u meniju koji se pojavi, kliknite na podmeni **Open Self Custody Wallet**.



![screen](assets/fr/07.webp)



WoS vam odmah kaže da *način samostalnog čuvanja dolazi sa frazom za oporavak. Takođe, vi ste isključivo odgovorni za sigurnost vaših sredstava*.



![screen](assets/fr/08.webp)



Označite dugme "**Razumem**" (1), zatim pritisnite dugme **Otvori Samostalno Čuvanje Wallet** (2), koje se pojavljuje u svetlo žutoj boji.



![screen](assets/fr/09.webp)



### Kreiranje portfolija sa samostalnim starateljstvom



Nakon što kliknete na dugme **Open Self Custody Wallet**, kliknite na dugme **Create a New Wallet**.



![screen](assets/fr/10.webp)



WoS će zatim kreirati portfolio za samostalno čuvanje za vas, ponovo unutar iste aplikacije. Moći ćete da se prebacujete između **custodial** režima (dostupnog u određenim regionima) i **self-custodial** režima po vašem nahođenju i u bilo koje vreme.



![screen](assets/fr/11.webp)



Jednom kada se kreira, bićete preusmereni na glavni WoS interfejs za samostalno čuvanje. Primetićete da nema razlika između opšteg pregleda i interfejsa WoS portfolija sa čuvanjem i onih WoS portfolija sa samostalnim čuvanjem.



### Čuvanje vaše mnemoničke fraze



Dodirnite ikonu **Keychain + Backup Wallet** koja se nalazi na vrhu ekrana između imena Wallet of Satoshi i hamburger menija.



![screen](assets/fr/12.webp)



WoS nudi dva različita načina čuvanja vaših 12 reči (mnemonik fraza): **bekap putem Google Drive-a** i **ručni bekap**.



Iako predlažemo ručno pravljenje rezervne kopije, što je najsigurnije, pokazaćemo vam i kako da napravite rezervnu kopiju putem Google Drive-a.



#### Bekap putem Google Drive



Kliknite na dugme **Google Drive Backup**.



![screen](assets/fr/13.webp)



Ako se odlučite za bekap sa Google Drive-om, postoji visok rizik da će vaš Google nalog biti kompromitovan. Zlonamerna osoba bi imala pristup fajlu koji sadrži vaših 12 reči, i na taj način bi mogla da dobije pristup vašem wallet.



Dodavanje lozinke za šifrovanje fajla koji sadrži vaših 12 reči svakako je dobar način da dodate dodatni sloj sigurnosti.



Dakle, aktivirajte dugme **Šifruj sa lozinkom** u naprednim opcijama.



![screen](assets/fr/14.webp)



Na novom interfejsu koji se pojavljuje, postavite jaku lozinku, a zatim je ponovo potvrdite.



![screen](assets/fr/15.webp)



Važno je zapamtiti da kada odaberete lozinku, ne smete je zaboraviti ili izgubiti medij na kojem ste je zapisali. Ako je zaboravite ili izgubite, nikada više nećete moći da pristupite svojih 12 reči, a samim tim ni svojim sredstvima.



Nakon što odaberete svoju lozinku, izaberite Google nalog za rezervnu kopiju, zatim odobrite pristupe koje zahteva WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Sačekajte nekoliko sekundi. Bingo! Vaša rezervna kopija je uspešno završena.



![screen](assets/fr/18.webp)



Uvek imate opciju da napravite dodatnu rezervnu kopiju odabirom druge metode bekapa: ručni bekap.


#### Ručno pravljenje rezervne kopije



Ako se odlučite za ručno pravljenje rezervne kopije, toplo preporučujemo da pogledate ovaj vodič, koji istražuje najbolje prakse za sigurno čuvanje vaše mnemoničke fraze, kako ne biste izgubili pristup svojim bitcoinima.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pritisnite dugme **Manual Backup**.



![screen](assets/fr/19.webp)



Na sledećem interfejsu, WoS vas podseća na nekoliko mera predostrožnosti koje treba uzeti u obzir pre nego što nastavite sa ručnim bekapom.



Aktivirajte dugme **Razumem** i pritisnite dugme **Dalje**.



![screen](assets/fr/20.webp)



Zatim će vam biti prikazane vaše 12 reči. Sačuvajte ih, a zatim kliknite na dugme **Next**.



![screen](assets/fr/21.webp)



Na ovom novom interfejsu, pritisnite reči redosledom.



![screen](assets/fr/22.webp)



Konačno, kliknite na dugme **Next**. Čestitamo! Vaša rezervna kopija je sada završena.



![screen](assets/fr/23.webp)



## Obnova portfolija sa samostalnim čuvanjem



Kada želite da povratite ili obnovite svoj WoS samostalni nadzor wallet nakon promene telefona ili iz bilo kog drugog razloga, evo koraka koje treba pratiti.



Da biste otvorili WoS portfelj, kliknite na hamburger meni u gornjem desnom uglu glavnog interfejsa.


U meniju koji se pojavi, kliknite na podmeni **Open Self Custody Wallet**.


Na novom interfejsu koji se pojavi, pritisnite dugme **Restore Existing Wallet**.



![screen](assets/fr/24.webp)



Izaberite metod obnove i pređite na sledeći korak.



![screen](assets/fr/25.webp)



### Vraćanje putem Google Drive



1. Pritisnite dugme **Restore From Google Drive**.


2. Izaberite Google nalog i dozvolite WoS-u da preuzme podatke za oporavak sačuvane na vašem Google Drive-u.


3. Zatim unesite svoju lozinku za šifrovanje (ako ste je prethodno definisali, naravno) iz datoteke koja sadrži vaših 12 reči.


4. Sačekajte nekoliko trenutaka da obnova stupi na snagu, i ponovo ćete moći pristupiti svom portfoliju.



### Ručno obnavljanje



1. Pritisnite dugme **Restore Manually**.


2. Zatim unesite 12 reči vaše mnemoničke fraze, pišući svaku reč ispred njenog početnog broja.


3. Sačekajte nekoliko trenutaka da obnova stupi na snagu i ponovo ćete moći da pristupite svom portfoliju.




### Prenos bitkoina između WoS skrbništva i WoS samostalnog skrbništva



Kada imate bitkoine (sats) u vašem WoS starateljstvu wallet i kreirate WoS samostarateljstvo wallet, nećete izgubiti svoja sredstva. Još bolje, možete ih preneti u svoj samostarateljski portfolio i obrnuto.



Da biste to uradili :


Možete kopirati svoju lightning WoS adresu za samostalno čuvanje ili fakturu koju ste kreirali.



![screen](assets/fr/26.webp)



Sada otvorite svoj pritvor wallet i pritisnite dugme **Envoyer**.



Zatim nalepite adresu ili fakturu. Pritisnite **Envoyer** drugi put.



Vratite se u svoj portfelj sa samostalnim čuvanjem i videćete da ste zaista primili sredstva.



![screen](assets/fr/27.webp)



## Slanje i primanje bitkoina



Što se tiče slanja i primanja bitcoina u režimu samostalnog čuvanja, baš kao i opšti pregled i interfejsi, oni se ne razlikuju od slanja i primanja bitcoina putem WoS čuvanja wallet.



Molimo vas da pogledate osnovni vodič za korišćenje Wallet of Satoshi na Plan₿ mreži.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Sada možete sami konfigurisati i upravljati Wallet of Satoshi u režimu samostalnog čuvanja.



Ako ste smatrali ovaj vodič korisnim, molim vas ostavite mi zeleni palac ispod. Hvala vam puno!