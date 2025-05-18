---
name: Sparrow Wallet - Multisig
description: Kreirajte portfelj sa više potpisa na Sparrow
---
![cover](assets/cover.webp)



Višestruki potpis Wallet (često nazivan "*Multisig*") je Bitcoin Wallet struktura koja zahteva nekoliko kriptografskih potpisa, sa različitih ključeva, da bi se odobrila potrošnja. Za razliku od konvencionalnog ("*singlesig*") Wallet, gde je jedan privatni ključ dovoljan za otključavanje UTXO, Multisig se zasniva na **m-of-n** modelu: od _n_ ključeva povezanih sa Wallet, _m_ mora imperativno supotpisati svaku transakciju.



Ovaj mehanizam omogućava da kontrolu nad portfoliom dele više entiteta ili uređaja. Na primer, u konfiguraciji 2-od-3, generišu se tri nezavisna seta ključeva, ali su potrebna samo dva da bi se oslobodila sredstva. Ova arhitektura drastično smanjuje rizike povezane sa kompromitovanjem ili gubitkom ključa: lopov sa pristupom samo jednom ključu ne može isprazniti Wallet, a korisnik koji izgubi jedan i dalje može pristupiti svojim sredstvima sa preostala dva.



![Image](assets/fr/01.webp)



Međutim, ova veća sigurnost dolazi sa većom složenošću. Postavljanje Multisig Wallet zahteva obezbeđivanje nekoliko Mnemonic fraza (po jedna za svaki faktor potpisa) i proširenih javnih ključeva ("*xpub*"). Zaista, ako koristite Multisig 2-od-3 Wallet, da biste preuzeli Wallet morate imati ili sve tri Mnemonic fraze, ili bar dve od tri fraze. Ali ako imate samo dve od tri fraze, takođe vam je potreban pristup trima *xpubs*, bez kojih će biti nemoguće preuzeti javne ključeve potrebne za pristup bitcoinima koje štite.



Da rezimiramo, da biste povratili Multisig portfolio, morate:




- Ili pristupite svim Mnemonic frazama povezanim sa svakim faktorom potpisa;
- Imajte minimalan broj Mnemonic fraza potreban prema pragu da biste mogli potpisati, i takođe imajte pristup xpub-ovima svih faktora kako biste preuzeli potrebne javne ključeve.



![Image](assets/fr/02.webp)



Ovo upravljanje rezervnim kopijama portfolija Multisig olakšano je pomoću *Output Script Descriptors*, koji grupišu sve javne podatke potrebne za pristup sredstvima. Međutim, ova funkcionalnost još nije implementirana u sav softver za upravljanje portfolijem.



Multisig je posebno pogodan za bitkoinere koji traže poboljšanu sigurnost ili kolektivno upravljanje sredstvima: kompanije, udruženja, porodice ili individualne korisnike koji poseduju značajnu količinu bitkoina. Može se koristiti za kreiranje decentralizovanih šema upravljanja, na primer, za raspodelu ovlašćenja potpisivanja među nekoliko menadžera ili članova tima.



U ovom vodiču ćemo naučiti kako kreirati i koristiti klasični multisignature Wallet sa **Sparrow Wallet**. Ako želite kreirati prilagođeni multisignature portfelj sa vremenskim zaključavanjima, preporučujem korišćenje Liana umesto toga:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Preduslovi



Za ovaj vodič, pokazaću vam kako da napravite Multisig sa [Sparrow Wallet softverom za upravljanje portfoliom](https://sparrowwallet.com/download/). Ako još niste instalirali ovaj softver, molimo vas da to učinite sada. Ako vam je potrebna pomoć, imamo i detaljan vodič o konfigurisanju Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Da biste postavili višepotpisni Wallet, biće vam potrebni različiti hardverski novčanici. Za Multisig 2-de-3, na primer, možete koristiti :




- Trezor Model One;
- Ledger Flex;
- Coldcard MK3.



![Image](assets/fr/03.webp)



Dobra je ideja koristiti različite marke Hardware Wallet u vašoj Multisig konfiguraciji. Ovo osigurava da, ako određeni model naiđe na ozbiljan problem, to neće uticati na ukupnu sigurnost vašeg Multisig. Štaviše, omogućava vam da iskoristite specifične prednosti svakog uređaja. Na primer, u mojoj konfiguraciji :





- Trezor Model One je potpuno open-source, što omogućava verifikaciju seed generacije. Međutim, kako nije opremljen Secure Element-om, ostaje ranjiv na fizičke napade;





- S druge strane, Ledger Flex koristi neverifikabilni vlasnički firmware, ali uključuje Secure Element koji nudi odličnu fizičku zaštitu;





- Coldcard je opremljen Secure Element-om i njegov kod je pretraživ. To je zanimljiv izbor za našu konfiguraciju, jer nudi verifikacione funkcije koje nisu dostupne na drugim modelima.



Pre nego što konfigurišete svoj Multisig Wallet, uverite se da je svaki Hardware Wallet pravilno konfigurisan (generisanje i čuvanje Mnemonic, definisanje PIN-a). Za detaljna uputstva, možete konsultovati naše tutorijale za svaki Hardware Wallet, na primer :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Kao što ćemo videti kasnije u ovom vodiču, takođe je moguće integrisati u vašu Multisig konfiguraciju faktor koji nije povezan sa Hardware Wallet, ali čiji su privatni ključevi sačuvani na vašem računaru. Ovaj metod je očigledno manje siguran od isključive upotrebe hardverskih novčanika, ali može biti relevantan u određenim slučajevima. Na primer, za Multisig 2-de-3, mogli biste se odlučiti za dva hardverska novčanika i jedan Software Wallet.



## Kreiranje Multisig portfolija



Otvorite Sparrow Wallet, kliknite na karticu "*File*", zatim izaberite "*New Wallet*".



![Image](assets/fr/04.webp)



Dodelite ime svom multisignature portfoliju, zatim kliknite na "*Create Wallet*" da potvrdite.



![Image](assets/fr/05.webp)



U padajućem meniju "*Policy Type*", izaberite opciju "*Multi Signature*".



![Image](assets/fr/06.webp)



U gornjem desnom uglu sada možete definisati ukupan broj ključeva u vašem Multisig, kao i broj sa-potpisnika potrebnih za odobravanje troška. U mom primeru, ovo je šema 2-od-3.



![Image](assets/fr/07.webp)



Na dnu prozora, Sparrow Wallet prikazuje tri "*Keystore*". Svaki predstavlja skup ključeva. Ovde koristim tri hardverska portfolija, tako da svaki "*Keystore*" odgovara jednom od njih. Sada ćemo ih konfigurisati.



Počinjem sa Coldcard. Na kartici "*Keystore 1*" biram opciju "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Na Coldcard-u, kada je uređaj otključan, idem na meni "*Settings*", zatim na "*Multisig Wallets*".



![Image](assets/fr/09.webp)



Ovaj meni vam omogućava upravljanje Multisig portfolijima u kojima Coldcard učestvuje. Želim da kreiram novi, pa biram "*Export XPUB*".



![Image](assets/fr/10.webp)



Za polje "*Broj računa*", ako upravljate samo jednim računom, možete ga ostaviti praznim i direktno potvrditi pritiskom na dugme za potvrdu.



![Image](assets/fr/11.webp)



Coldcard će zatim generate datoteku koja sadrži vaš xpub, sačuvanu na Micro SD kartici.



![Image](assets/fr/12.webp)



Umetnite ovu Micro SD karticu u vaš računar. U Sparrow Wallet, kliknite na dugme "*Import File...*" pored "*Coldcard Multisig*", zatim izaberite fajl kreiran od strane Coldcard-a na kartici.



![Image](assets/fr/13.webp)



Vaš xpub je uspešno uvezen. Sada ćemo ponoviti proceduru sa druga dva hardverska novčanika.



![Image](assets/fr/14.webp)



Za Ledger Flex, biram "*Keystore 2*", zatim kliknem na "*Connected Hardware Wallet*". Uverite se da je Ledger povezan sa računarom, otključan, i da je aplikacija Bitcoin otvorena.



![Image](assets/fr/15.webp)



Zatim kliknite na dugme "*Skeniraj...*".



![Image](assets/fr/16.webp)



Pored imena vašeg portfolija hardvera, kliknite na "*Import Keystore*".



![Image](assets/fr/17.webp)



Drugi potpisnik je sada ispravno registrovan u Sparrow Wallet.



![Image](assets/fr/18.webp)



Ponavljam potpuno isti postupak sa Trezor One da završim konfiguraciju Multisig.



![Image](assets/fr/19.webp)



U mojoj konfiguraciji ne pokrivamo ovaj slučaj, ali ako želite da uključite potpis putem Software Wallet u Sparrow (Hot Wallet) unutar vašeg Multisig, jednostavno kliknite na dugme "*Novi ili Uvezeni Software Wallet*".



Sada kada su svi vaši potpisni uređaji uvezeni u Sparrow Wallet, možete finalizirati kreiranje Multisig klikom na "*Apply*".



![Image](assets/fr/20.webp)



Izaberite jaku lozinku kako biste osigurali pristup vašem Sparrow Wallet Wallet. Ova lozinka štiti vaše javne ključeve, adrese, oznake i istoriju transakcija od neovlašćenog pristupa.



Zapamti da sačuvaš ovu lozinku na sigurnom mestu, kao što je menadžer lozinki, kako bi izbegao/la njen gubitak.



![Image](assets/fr/21.webp)



## Pravljenje rezervne kopije portfolija Multisig



Sada ćemo sačuvati naš *Output Script Descriptor* na Coldcard-u (ovo se odnosi samo na korisnike sa Coldcard-om u njihovom Multisig), i iznad svega, napravićemo rezervnu kopiju na nezavisnom medijumu.



*Descriptor* sadrži sve xpub-ove u vašem Multisig portfoliju, kao i putanje derivacije korišćene za generate ključeve. Setite se šta smo videli u Prvom delu: da biste obnovili Multisig portfolijo, morate imati **sve** Mnemonic fraze, ili samo minimalni broj potreban da dostignete prag potpisa. Međutim, u ovom drugom slučaju, takođe je neophodno imati **xpub-ove** nedostajućih potpisnika. *Descriptor* sadrži sve xpub-ove vašeg Multisig.



Ako ovo nije jasno, samo zapamtite sledeće: da biste preuzeli Multisig, potrebno je minimalan broj Mnemonic fraza za svaki korišćeni Hardware Wallet, u zavisnosti od praga (u mom slučaju: 2 fraze), kao i *Descriptor*.



Ovaj *Descriptor* ne sadrži privatne ključeve, već samo javne. To znači da ne omogućava pristup sredstvima. Stoga nije toliko kritičan kao Mnemonic fraze, koje omogućavaju potpuni pristup vašim bitcoinima. Rizik sa *Descriptor*-om je isključivo povezan sa poverljivošću: u slučaju kompromitovanja, treća strana bi mogla da posmatra sve vaše transakcije, ali ne bi mogla da troši vaša sredstva.



Toplo preporučujem da napravite nekoliko kopija ovog *Descriptor*-a i držite ih uz svaki uređaj za potpisivanje na vašem Multisig. Na primer, u mom slučaju, štampam *Descriptor* na papiru i držim jednu kopiju uz Coldcard, drugu uz Trezor, i jednu uz Ledger. Takođe čuvam ovaj *Descriptor* kao PDF fajl na tri USB memorije, svaka pohranjena uz jedan od hardverskih portfolija. Na ovaj način, maksimiziram svoje šanse da nikada ne izgubim ovaj *Descriptor*, i siguran sam da imam dve kopije (jednu fizičku i jednu digitalnu) uz svaki uređaj.



Jednom kada vaš Multisig portfolio bude kreiran, Sparrow vam automatski pruža ovaj *Descriptor*. Kliknite na dugme "*Save PDF...*" da biste ga sačuvali i kao tekst i kao QR kod.



![Image](assets/fr/22.webp)



Možete zatim odštampati ovaj PDF i kopirati ga na vaše USB stikove.



![Image](assets/fr/23.webp)



Takođe ćemo registrovati ovaj *Descriptor* u Coldcard (ako ga koristite u vašoj konfiguraciji). Ovo će omogućiti Coldcard-u da verifikuje da svaka kasnije potpisana transakcija odgovara originalnom Wallet: ispravni xpubs, ispravan Address format, ispravna putanja derivacije... Bez ovog uvezenog *Descriptor*-a, Coldcard ne može potvrditi da Exchange adrese nisu otete ili da PSBT nije izmenjen.



Ovo je ono što čini Coldcard tako zanimljivim u Multisig: nudi dodatne provere protiv određenih sofisticiranih napada, što drugi hardverski novčanici ne dozvoljavaju (pod uslovom, naravno, da ga koristite za potpisivanje).



U Sparrow-u, pristupite meniju "*Settings*", zatim kliknite na "*Export...*".



![Image](assets/fr/24.webp)



Pored opcije "*Coldcard Multisig*", kliknite na "*Export File...*" i sačuvajte tekstualni fajl na Micro SD karticu.



![Image](assets/fr/25.webp)



Zatim umetnite karticu u Coldcard. Idite na meni "*Settings*", zatim "*Multisig Wallets*", i izaberite "*Import from SD*".



![Image](assets/fr/26.webp)



Odaberite odgovarajuću datoteku i potvrdite uvoz.



![Image](assets/fr/27.webp)



Kliknite na ime vašeg novouvezenog Multisig.



![Image](assets/fr/28.webp)



Proveri parametre konfiguracije Multisig, zatim potvrdi registraciju.



![Image](assets/fr/29.webp)



Vaš Multisig je sada ispravno sačuvan u vašem Coldcard-u. Ako imate nekoliko Coldcard-a u istom Multisig, ponovite ovaj postupak za svaki od njih.



Pored čuvanja *Descriptor*-a, ne zaboravite da obratite posebnu pažnju na čuvanje Mnemonic fraza za svaki od vaših potpisnih uređaja. Ako tek počinjete, toplo preporučujem da se posavetujete sa ovim drugim vodičem kako biste naučili kako ih pravilno sačuvati i upravljati njima:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pre nego što primite svoje prve bitkoine na vaš Multisig, **snažno vam savetujem da izvršite test praznog oporavka**. Zabeležite neke referentne informacije, kao što je prvi prijemni Address, zatim resetujte svoje hardverske novčanike dok je Wallet još uvek prazan. Zatim pokušajte da obnovite svoj Multisig Wallet na Hardverskim Novčanicima koristeći svoje Mnemonic fraze sa papirnih rezervnih kopija, a zatim na Sparrow koristeći *Descriptor*. Proverite da li prvi Address generisan nakon obnove odgovara onom koji ste prvobitno zapisali. Ako odgovara, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.



Da biste saznali više o tome kako izvesti test oporavka, predlažem da pogledate ovaj drugi vodič:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Primajte bitkoine na vašem Multisig



Vaš Wallet je sada spreman da prima bitkoine. U Sparrow-u, kliknite na karticu "*Receive*".



![Image](assets/fr/30.webp)



Pre nego što upotrebite Address generisan od strane Sparrow Wallet, odvojite vreme da ga proverite direktno na ekranu vaših hardverskih novčanika. Ovo će osigurati da Address nije izmenjen i da vaši uređaji poseduju privatne ključeve potrebne za trošenje povezanih sredstava. Ovo pomaže u zaštiti od brojnih vektora napada.



Da biste to uradili, kliknite na "*Display Address*" da prikažete Address na vašem Trezoru ili Ledger, kada je povezan kablom.



![Image](assets/fr/31.webp)



Sa Coldcard, ova verifikacija se može izvršiti bez ikakve interakcije sa Sparrow. Jednostavno otvorite meni "*Address Explorer*", zatim izaberite vaš Multisig na samom dnu.



![Image](assets/fr/32.webp)



Videćete adrese prijema koje generiše Multisig.



![Image](assets/fr/33.webp)



Proverite da Address prikazan na svakom Hardware Wallet tačno odgovara onom u Sparrow Wallet. Preporučljivo je to uraditi neposredno pre deljenja Address sa platiocem, kako biste bili sigurni u njegov integritet.



Zatim možete dodeliti "*Label*" ovom Address, kako biste označili poreklo primljenih bitkoina. Ovo je dobar način organizovanja upravljanja vašim UTXO-ima.



![Image](assets/fr/34.webp)



Kada se ovo verifikuje, možete koristiti Address za primanje bitkoina.



![Image](assets/fr/35.webp)



## Slanje bitkoina sa vašim Multisig



Sada kada ste primili svoje prve Satss na vašem Multisig Wallet, možete ih i potrošiti! U Sparrow-u, idite na karticu "*Send*" da napravite novu transakciju.



![Image](assets/fr/36.webp)



Ako želite da koristite *Coin Control*, tj. ručno odaberete UTXO-e koje želite da potrošite, idite na karticu "*UTXOs*". Izaberite UTXO-e koje želite da potrošite, zatim kliknite na "*Send Selected*". Bićete automatski preusmereni na karticu "*Send*", sa već popunjenim UTXO-ima.



![Image](assets/fr/37.webp)



Unesite odredište Address. Više adresa može se dodati klikom na "*+ Dodaj*".



![Image](assets/fr/38.webp)



Dodajte "*Oznaku*" da opišete svrhu ovog troška, kako biste lakše pratili svoje transakcije.



![Image](assets/fr/39.webp)



Unesite iznos koji treba poslati na odabrani Address.



![Image](assets/fr/40.webp)



Podesite stopu punjenja u skladu sa trenutnim uslovima mreže. Na primer, konsultujte [Mempool.space](https://Mempool.space/) da biste odabrali odgovarajući nivo punjenja.



Nakon što proverite sve parametre transakcije, kliknite na "*Create Transaction*".



![Image](assets/fr/41.webp)



Ako ste zadovoljni svime, kliknite na "*Finalize Transaction for Signing*".



![Image](assets/fr/42.webp)



Na dnu ekrana, videćete da Sparrow čeka 2 potpisa. Ovo je normalno: Wallet korišćen ovde je Multisig 2-de-3.



![Image](assets/fr/43.webp)



Počinjem sa potpisivanjem koristeći svoj Coldcard. Da bih to uradio, ubacujem Micro SD karticu u računar, zatim kliknem na "*Save Transaction*".



![Image](assets/fr/44.webp)



Postoje 3 načina prenosa transakcije koja treba da se potpiše na vaš Hardware Wallet, a zatim da se preuzme iz Sparrow-a. Prvi je korišćenje Micro SD kartice, kao što ćemo ovde uraditi za Coldcard. Drugi je putem kablovske veze, koju ćemo koristiti za drugi potpis (Ledger i Trezor). Na kraju, moguće je koristiti komunikaciju putem QR koda, za uređaje opremljene kamerom kao što su Coldcard Q, Jade Plus ili Passport V2.



Jednom kada je PSBT (*Partially Signed Bitcoin Transaction*) sačuvan na Micro SD, ubacujem ga u Coldcard MK3, zatim biram meni "*Ready to Sign*".



![Image](assets/fr/45.webp)



Na vašem Hardware Wallet ekranu, pažljivo proverite parametre transakcije: primaoca Address, poslatu sumu i naknade. Kada transakcija bude potvrđena, validirajte da biste nastavili sa potpisivanjem.



![Image](assets/fr/46.webp)



Zatim vratite Micro SD u računar i kliknite na "*Load Transaction*" u Sparrow. Izaberite PSBT potpisan od strane Coldcard iz vaših fajlova.



![Image](assets/fr/47.webp)



Možete videti da je Coldcard potpis dodat. Sada ću koristiti drugi uređaj, u ovom slučaju Ledger, da izvršim drugi potrebni potpis. Povezujem ga, otključavam, zatim kliknem na "*Sign*" na Sparrow.



![Image](assets/fr/48.webp)



Kliknite na "*Sign*" pored imena vašeg Hardware Wallet.



![Image](assets/fr/49.webp)



Prvi put kada koristite svoj Ledger sa ovim Multisig, Sparrow će vas zamoliti da verifikujete proširene javne ključeve (xpubs) ko-potpisnika. Kao i kod Coldcard-a, ovaj korak sprečava da kasnije potpisujete naslepo. Da biste potvrdili ove informacije, uporedite xpub prikazan na ekranu Ledger sa onima koje direktno pružaju vaši drugi hardverski novčanici.



![Image](assets/fr/50.webp)



Proverite primalac Address, iznos prenosa i naknadu za transakciju, zatim potpišite transakciju.



![Image](assets/fr/51.webp)



Pritisnite ekran da potpišete.



![Image](assets/fr/52.webp)



Sparrow sada ima dva potpisa potrebna za oslobađanje sredstava iz portfolija Multisig. Proveri transakciju još jednom, i ako sve bude u redu, klikni na "*Broadcast Transaction*" da je emituješ preko mreže.



![Image](assets/fr/53.webp)



Pronaći ćete ovu transakciju u kartici "*Transakcije*" u Sparrow Wallet.



![Image](assets/fr/54.webp)



Čestitamo, sada znate kako da postavite i koristite multisignature Wallet na Sparrow. Ako ste smatrali da je ovaj vodič koristan, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala što delite!



Da biste nastavili dalje, preporučujem da pogledate ovaj vodič o drugoj metodi za povećanje sigurnosti vašeg Bitcoin Wallet, passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7