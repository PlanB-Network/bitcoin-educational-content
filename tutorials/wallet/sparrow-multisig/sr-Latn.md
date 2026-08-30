---
name: Sparrow Wallet - Multisig
description: Kreirajte novčanik sa više potpisa u Sparrow-u
---
![cover](assets/cover.webp)


Novčanik sa više potpisa (često nazvan "*Multisig*") je struktura Bitcoin novčanika koja zahteva nekoliko kriptografskih potpisa, sa različitih ključeva, da bi se odobrilo trošenje. Za razliku od konvencionalnog ("*singlesig*") novčanika, gde je jedan privatni ključ dovoljan da otključa UTXO, Multisig se zasniva na modelu **m-od-n**: od _n_ ključeva povezanih sa novčanikom, _m_ njih mora obavezno da ko-potpiše svaku transakciju.


Ovaj mehanizam omogućava da kontrola nad novčanikom bude podeljena između nekoliko subjekata ili uređaja. Na primer, u konfiguraciji 2-od-3 generišu se tri nezavisna skupa ključeva, ali su samo dva potrebna da se sredstva oslobode. Ova arhitektura drastično smanjuje rizike povezane sa kompromitovanjem ili gubitkom ključa: lopov koji ima pristup samo jednom ključu ne može da isprazni novčanik, a korisnik koji jedan izgubi i dalje može da pristupi svojim sredstvima pomoću preostala dva.


![Image](assets/fr/01.webp)


Međutim, ova veća bezbednost dolazi sa većom složenošću. Podešavanje Multisig novčanika zahteva da obezbedite nekoliko mnemoničkih fraza (jednu po faktoru potpisivanja) i proširene javne ključeve ("*xpub*"). Naime, ako koristite Multisig novčanik 2-od-3, da biste povratili novčanik morate imati ili sve tri mnemoničke fraze, ili najmanje dve od tri fraze. Ali ako imate samo dve od tri fraze, potreban vam je i pristup trima *xpub*-ovima, bez kojih će biti nemoguće povratiti javne ključeve potrebne za pristup bitkoinima koje oni štite.


Da rezimiramo, da biste povratili Multisig novčanik, morate:


- Ili pristupiti svim mnemoničkim frazama povezanim sa svakim faktorom potpisivanja;
- Ili imati minimalan broj mnemoničkih fraza koji prag zahteva da biste mogli da potpišete, a takođe imati pristup xpub-ovima svih faktora kako biste povratili potrebne javne ključeve.


![Image](assets/fr/02.webp)


Ovo upravljanje rezervnim kopijama Multisig novčanika olakšavaju *Output Script Descriptors*, koji na jednom mestu grupišu sve javne podatke potrebne za pristup sredstvima. Međutim, ova funkcionalnost još nije implementirana u svim softverima za upravljanje novčanicima.


Multisig je posebno prikladan za bitkoinere koji traže povećanu bezbednost ili kolektivno upravljanje sredstvima: kompanije, udruženja, porodice ili pojedinačne korisnike koji drže značajnu količinu bitkoina. Može se koristiti za kreiranje decentralizovanih šema upravljanja, na primer da se ovlašćenje za potpisivanje raspodeli između nekoliko rukovodilaca ili članova tima.


U ovom vodiču naučićemo kako da kreiramo i koristimo klasičan novčanik sa više potpisa pomoću **Sparrow Wallet**-a. Ako želite da kreirate prilagođen novčanik sa više potpisa sa timelock-ovima, preporučujem da umesto toga koristite Lianu:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prethodni uslovi


Za ovaj vodič pokazaću vam kako da napravite Multisig pomoću [softvera za upravljanje novčanikom Sparrow Wallet](https://sparrowwallet.com/download/). Ako još niste instalirali ovaj softver, učinite to sada. Ako vam je potrebna pomoć, imamo i detaljan vodič o konfigurisanju Sparrow Wallet-a:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Da biste podesili novčanik sa više potpisa, biće vam potrebni različiti hardverski novčanici. Za Multisig 2-od-3, na primer, mogli biste koristiti:


- Trezor Model One;
- Ledger Flex;
- Passport Core.


![Image](assets/fr/03.webp)


Dobra je ideja da u svojoj Multisig konfiguraciji koristite hardverske novčanike različitih proizvođača. Time se osigurava da, ako određeni model naiđe na ozbiljan problem, to ne utiče na ukupnu bezbednost vašeg Multisig-a. Osim toga, tako iskorišćavate specifične prednosti svakog uređaja. Na primer, u mojoj konfiguraciji:



- Trezor Model One je potpuno otvorenog koda, što omogućava verifikaciju generisanja seed-a. Međutim, pošto nije opremljen Secure Element-om, ostaje ranjiv na fizičke napade;



- Ledger Flex, sa druge strane, koristi zatvoreni firmver koji se ne može verifikovati, ali sadrži Secure Element koji nudi odličnu fizičku zaštitu;



- Passport Core kombinuje potpuno open-source firmver, Secure Element i air-gapped razmenu podataka putem QR kodova. To je nezavisni treći potpisnik koji može da verifikuje adrese i potpisuje PSBT-ove bez USB veze za prenos podataka.


Pre nego što konfigurišete svoj Multisig novčanik, proverite da je svaki hardverski novčanik pravilno konfigurisan (generisanje i čuvanje mnemonika, definisanje PIN-a). Za detaljna uputstva možete pogledati naše vodiče za svaki hardverski novčanik, na primer:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Kao što ćemo videti kasnije u ovom vodiču, u svoju Multisig konfiguraciju možete uključiti i faktor koji nije povezan sa hardverskim novčanikom, već čiji su privatni ključevi sačuvani na vašem računaru. Ova metoda je očigledno manje bezbedna od isključive upotrebe hardverskih novčanika, ali u pojedinim slučajevima može biti relevantna. Na primer, za Multisig 2-od-3 mogli biste se odlučiti za dva hardverska novčanika i jedan softverski novčanik.

> ⚠️ **Bezbednosno obaveštenje za Coldcard MK3:** ne kreirajte novi seed na MK3 uređaju sa firmverom starijim od 4.2.0. Seed-ovi generisani na starijem firmveru moraju biti zamenjeni, a sredstva premeštena. Ovaj vodič zato koristi Passport Core kao svoj air-gapped referentni potpisnik.


## Kreiranje Multisig novčanika


Otvorite Sparrow Wallet, kliknite na karticu "*File*", zatim izaberite "*New Wallet*".


![Image](assets/fr/04.webp)


Dodelite ime svom novčaniku sa više potpisa, zatim kliknite na "*Create Wallet*" da potvrdite.


![Image](assets/fr/05.webp)


U padajućem meniju "*Policy Type*" izaberite opciju "*Multi Signature*".


![Image](assets/fr/06.webp)


U gornjem desnom uglu sada možete da definišete ukupan broj ključeva u svom Multisig-u, kao i broj ko-potpisnika potrebnih da odobre trošenje. U mom primeru to je šema 2-od-3.


![Image](assets/fr/07.webp)


Na dnu prozora Sparrow Wallet prikazuje tri "*Keystore*". Svaki predstavlja jedan skup ključeva. Ovde koristim tri hardverska novčanika, tako da svaki "*Keystore*" odgovara jednom od njih. Sada ćemo ih konfigurisati.


Počinjem sa Passport Core-om. U kartici "*Keystore 1*" biram opciju "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Na Passport-u otvorite nalog koji želite da koristite, zatim izaberite "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport prikazuje animirani QR kod koji sadrži informacije o njegovom javnom ključu.

U Sparrow-u izaberite "*Scan...*" pored "*Passport*" i skenirajte taj animirani QR kod veb-kamerom svog računara. Uporedite otisak master ključa koji prikazuje Sparrow sa onim koji prikazuje Passport, zatim uvezite keystore.

Vaš Passport xpub je sada uvezen. Ponovite odgovarajuću proceduru za Ledger Flex i Trezor Model One.


Za Ledger Flex biram "*Keystore 2*", zatim kliknem na "*Connected Hardware Wallet*". Proverite da je Ledger povezan sa računarom, otključan i da je Bitcoin aplikacija otvorena.


![Image](assets/fr/15.webp)


Zatim kliknite na dugme "*Scan...*".


![Image](assets/fr/16.webp)


Pored imena svog hardverskog novčanika kliknite na "*Import Keystore*".


![Image](assets/fr/17.webp)


Drugi potpisnik je sada pravilno registrovan u Sparrow Wallet-u.


![Image](assets/fr/18.webp)


Ponavljam potpuno istu proceduru sa Trezor One-om da bih finalizovao Multisig konfiguraciju.


![Image](assets/fr/19.webp)


U mojoj konfiguraciji ne obrađujemo ovaj slučaj, ali ako u svoj Multisig želite da uključite potpis putem softverskog novčanika u Sparrow-u (hot wallet), dovoljno je da kliknete na dugme "*New or Imported Software Wallet*".


Sada kada su svi vaši uređaji za potpisivanje uvezeni u Sparrow Wallet, možete finalizovati kreiranje Multisig-a klikom na "*Apply*".


![Image](assets/fr/20.webp)


Izaberite jaku lozinku da zaštitite pristup svom Sparrow Wallet novčaniku. Ova lozinka štiti vaše javne ključeve, adrese, oznake i istoriju transakcija od neovlašćenog pristupa.


Ne zaboravite da ovu lozinku sačuvate na bezbednom mestu, na primer u menadžeru lozinki, da je ne izgubite.


![Image](assets/fr/21.webp)


## Izrada rezervne kopije Multisig novčanika


Sada ćemo sačuvati *Output Script Descriptor* na nezavisnom medijumu i držati nekoliko njegovih kopija.


*Deskriptor* sadrži sve xpub-ove vašeg Multisig novčanika, kao i putanje derivacije koje se koriste za generisanje ključeva. Setite se onoga što smo videli u 1. delu: da biste obnovili Multisig novčanik, morate imati ili **sve** mnemoničke fraze, ili samo minimalan broj potreban da se dostigne prag potpisivanja. Međutim, u ovom drugom slučaju neophodno je imati i **xpub-ove** potpisnika koji nedostaju. *Deskriptor* sadrži sve xpub-ove vašeg Multisig-a.


Ako ovo nije jasno, samo zapamtite ovo: da biste povratili Multisig, potreban vam je minimalan broj mnemoničkih fraza za svaki upotrebljeni hardverski novčanik, u zavisnosti od praga (u mom slučaju: 2 fraze), kao i *Deskriptor*.


Ovaj *Deskriptor* ne sadrži privatne ključeve, samo javne. To znači da ne daje pristup sredstvima. Zato nije toliko kritičan kao mnemoničke fraze, koje daju pun pristup vašim bitkoinima. Rizik kod *Deskriptora* odnosi se isključivo na privatnost: u slučaju kompromitovanja, treća strana bi mogla da posmatra sve vaše transakcije, ali ne bi mogla da potroši vaša sredstva.


Toplo preporučujem da napravite nekoliko kopija ovog *Deskriptora* i da svaku držite zajedno sa jednim uređajem za potpisivanje u svom Multisig-u. Na primer, u mom slučaju štampam *Deskriptor* na papiru i držim jednu kopiju sa Passport-om, drugu sa Trezor-om, a jednu sa Ledger-om. Ovaj *Deskriptor* takođe čuvam kao PDF datoteku na tri USB stika, od kojih je svaki uskladišten sa jednim od hardverskih novčanika. Na ovaj način maksimalno povećavam šanse da nikada ne izgubim ovaj *Deskriptor* i siguran sam da imam dve kopije (jednu fizičku i jednu digitalnu) sa svakim uređajem.


Kada je vaš Multisig novčanik kreiran, Sparrow vam automatski daje ovaj *Deskriptor*. Kliknite na dugme "*Save PDF...*" da ga sačuvate i kao tekst i kao QR kod.


![Image](assets/fr/22.webp)


Zatim možete odštampati ovaj PDF i kopirati ga na svoje USB stikove.


![Image](assets/fr/23.webp)


Passport koristi multisig konfiguraciju uvezenu iz Sparrow-a da prikaže i verifikuje relevantne informacije o ključevima tokom QR uparivanja i potpisivanja. *Deskriptor* čuvajte nezavisno: on ostaje neophodan za obnavljanje novčanika ako jedan potpisnik nije dostupan.


Osim čuvanja *Deskriptora*, ne zaboravite da posvetite posebnu pažnju čuvanju mnemoničkih fraza za svaki od svojih uređaja za potpisivanje. Ako tek počinjete, toplo preporučujem da pogledate ovaj drugi vodič da naučite kako da ih pravilno sačuvate i njima upravljate:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pre nego što primite prve bitkoine na svoj Multisig, **toplo vam savetujem da izvedete test obnavljanja na praznom novčaniku**. Zapišite neke referentne informacije, kao što je prva adresa za primanje, zatim resetujte svoje hardverske novčanike dok je novčanik još prazan. Nakon toga probajte da obnovite svoj Multisig novčanik na hardverskim novčanicima koristeći papirne rezervne kopije mnemoničkih fraza, a zatim u Sparrow-u pomoću *Deskriptora*. Proverite da prva adresa generisana nakon obnavljanja odgovara onoj koju ste prvobitno zapisali. Ako odgovara, možete biti mirni da su vaše papirne rezervne kopije pouzdane.


Da naučite više o tome kako se izvodi test obnavljanja, predlažem da pogledate ovaj drugi vodič:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Primanje bitkoina na vaš Multisig


Vaš novčanik je sada spreman da prima bitkoine. U Sparrow-u kliknite na karticu "*Receive*".


![Image](assets/fr/30.webp)


Pre nego što upotrebite adresu koju je generisao Sparrow Wallet, odvojite vreme da je proverite direktno na ekranu svojih hardverskih novčanika. Time ćete se uveriti da adresa nije izmenjena i da vaši uređaji drže privatne ključeve potrebne za trošenje povezanih sredstava. Ovo vam pomaže da se zaštitite od većeg broja vektora napada.


Da to učinite, kliknite na "*Display Address*" da prikažete adresu na svom Trezor-u ili Ledger-u, kada su povezani kablom.


![Image](assets/fr/31.webp)


Sa Passport-om izaberite multisig nalog i izaberite "*Verify Address*". Skenirajte QR kod adrese za primanje koju prikazuje Sparrow. Passport na svom ekranu potvrđuje da li adresa pripada multisig novčaniku.


Proverite da adresa prikazana na svakom hardverskom novčaniku tačno odgovara onoj u Sparrow Wallet-u. Preporučljivo je to učiniti neposredno pre nego što adresu podelite sa platiocem, da biste bili sigurni u njen integritet.


Zatim ovoj adresi možete dodeliti "*Label*", da označite poreklo primljenih bitkoina. To je dobar način da organizujete upravljanje svojim UTXO-ima.


![Image](assets/fr/34.webp)


Kada je ovo provereno, možete koristiti adresu za primanje bitkoina.


![Image](assets/fr/35.webp)


## Slanje bitkoina pomoću vašeg Multisig-a


Sada kada ste primili prve satoshije na svoj Multisig novčanik, možete ih i potrošiti! U Sparrow-u idite na karticu "*Send*" da izgradite novu transakciju.


![Image](assets/fr/36.webp)


Ako želite da koristite *Coin Control*, tj. da ručno izaberete UTXO-e koje želite da potrošite, idite na karticu "*UTXOs*". Izaberite UTXO-e koje želite da potrošite, zatim kliknite na "*Send Selected*". Bićete automatski preusmereni na karticu "*Send*", sa već unapred popunjenim UTXO-ima.


![Image](assets/fr/37.webp)


Unesite adresu primaoca. Više adresa se može dodati klikom na "*+ Add*".


![Image](assets/fr/38.webp)


Dodajte "*Label*" da opišete svrhu ovog trošenja, kako biste lakše pratili svoje transakcije.


![Image](assets/fr/39.webp)


Unesite iznos koji treba poslati na izabranu adresu.


![Image](assets/fr/40.webp)


Prilagodite visinu naknade prema trenutnim uslovima na mreži. Na primer, pogledajte [Mempool.space](https://Mempool.space/) da izaberete odgovarajući nivo naknade.


Nakon što proverite sve parametre transakcije, kliknite na "*Create Transaction*".


![Image](assets/fr/41.webp)


Ako ste svime zadovoljni, kliknite na "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Na dnu ekrana videćete da Sparrow čeka 2 potpisa. To je normalno: novčanik koji se ovde koristi je Multisig 2-od-3.


![Image](assets/fr/43.webp)


Počinjem potpisivanje svojim Passport-om. U Sparrow-u kliknite na "*Show QR*" da prikažete PSBT (*Partially Signed Bitcoin Transaction*) kao animirane QR kodove. Na Passport-u izaberite multisig nalog i izaberite "*Sign with QR Code*", zatim skenirajte QR kod koji prikazuje Sparrow.


Na ekranu svog hardverskog novčanika pažljivo proverite parametre transakcije: adresu primaoca, poslati iznos i naknade. Kada je transakcija potvrđena, validirajte da nastavite na potpisivanje.


Nakon što odobrite transakciju, Passport prikazuje potpisani PSBT kao animirane QR kodove. U Sparrow-u kliknite na "*Scan QR*" i skenirajte te kodove svojom veb-kamerom. Passport potpis se tada dodaje. Sada koristim Ledger za drugi potreban potpis: povezujem ga i otključavam, zatim kliknem na "*Sign*" u Sparrow-u.


![Image](assets/fr/48.webp)


Kliknite na "*Sign*" pored imena svog hardverskog novčanika.


![Image](assets/fr/49.webp)


Prvi put kada svoj Ledger koristite sa ovim Multisig-om, Sparrow će vas zamoliti da verifikujete proširene javne ključeve (xpub-ove) ko-potpisnika. Kao i sa Passport-om, ovaj korak vas sprečava da kasnije potpisujete naslepo. Da potvrdite te informacije, uporedite xpub prikazan na ekranu Ledger-a sa onima koje direktno daju vaši drugi hardverski novčanici.


![Image](assets/fr/50.webp)


Proverite adresu primaoca, prenesen iznos i naknadu za transakciju, zatim potpišite transakciju.


![Image](assets/fr/51.webp)


Pritisnite ekran da potpišete.


![Image](assets/fr/52.webp)


Sparrow sada ima dva potpisa potrebna da se sredstva oslobode iz Multisig novčanika. Proverite transakciju poslednji put i, ako je sve u redu, kliknite na "*Broadcast Transaction*" da je emitujete na mrežu.


![Image](assets/fr/53.webp)


Ovu transakciju ćete naći u kartici "*Transactions*" u Sparrow Wallet-u.


![Image](assets/fr/54.webp)


Čestitamo, sada znate kako da podesite i koristite novčanik sa više potpisa u Sparrow-u. Ako vam je ovaj vodič bio koristan, bio bih vam zahvalan ako ispod ostavite zeleni palac. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala na deljenju!


Da idete dalje, preporučujem da pogledate ovaj vodič o drugoj metodi za povećanje bezbednosti vašeg Bitcoin novčanika, BIP39 lozinci:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
