---
name: Portal
description: Konfigurisanje i korišćenje TwentyTwo-Devices Hardware Wallet Portala
---
![cover](assets/cover.webp)


Portal je Bitcoin Hardware Wallet dizajniran od strane TwentyTwo Devices, kompanije specijalizovane za kreiranje open-source hardverskih novčanika za bitkoinere. Osnovao ga je Alekos Filini, kreator projekta Magical Bitcoin ([u daljem tekstu nazvan BDK](https://github.com/bitcoindevkit)) i koji je radio za Blockstream i BHB Network, TwentyTwo Devices ima za cilj da se fokusira na autonomiju korisnika, jednostavnost i sigurnost.


Ono što izdvaja Portal od drugih hardverskih novčanika na tržištu je njegova native integracija sa pametnim telefonima. Radi bez kablova ili baterija. Koristi NFC tehnologiju da se napaja i komunicira sa bilo kojim kompatibilnim mobilnim uređajem Wallet. Njegov intrigantan dizajn je osmišljen za ergonomsku upotrebu. Okrugli deo se postavlja na zadnju stranu pametnog telefona kako bi se otkrio ekran na kojem možete proveriti detalje svojih transakcija pre nego što ih potpišete posvećenim dugmetom.


![Image](assets/fr/01.webp)


Potpuno otvorenog koda, Portal se zasniva na firmveru napisanom u Rust i koristi BDK (Bitcoin Dev Kit) za upravljanje ključevima i transakcijama. Prodaje se za €89 [na zvaničnom sajtu](https://store.twenty-two.xyz/products/portal-hardware-Wallet).


U vreme pisanja, Portal je kompatibilan sa aplikacijama Nunchuk i Bitcoin Keeper. U ovom uputstvu, konfigurišemo ga sa Nunchuk-om.


## Unboxing


Kada primite svoj Portal, proverite da li su kutija i etiketa koja je zapečaćuje u dobrom stanju. Unutra ćete pronaći svoj Portal u zapečaćenoj vrećici.


Uverite se da je Seal netaknut kako biste potvrdili da torbica nije otvorena. Jedinstveni broj prikazan velikim slovima na torbici treba da odgovara onom napisanom crnom bojom ispod plavog Seal, onom na etiketi kutije, i onom koji će se pojaviti na vašem ekranu kada prvi put pokrenete uređaj.


![Image](assets/fr/02.webp)


## Instalacija nunchuka


Da biste upravljali Wallet hostovanim na Portalu, koristićemo aplikaciju Nunchuk. Preuzmite aplikaciju sa [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) ili direktno putem njenog [`.apk` fajla](https://github.com/nunchuk-io/nunchuk-android/releases).


![Image](assets/fr/03.webp)


Ako prvi put koristite Nunchuk, aplikacija će vas zatražiti da kreirate nalog. Za potrebe ovog tutorijala, nije neophodno da ga kreirate. Izaberite "*Nastavi kao gost*" da biste nastavili bez naloga.


![Image](assets/fr/04.webp)


## Konfiguracija portala


Na početnom ekranu Nunchuk-a, kliknite na "*NFC*" logo na vrhu ekrana.


![Image](assets/fr/05.webp)


Postavite svoj Portal na poleđinu pametnog telefona da biste ga aktivirali.


![Image](assets/fr/06.webp)


Nunchuk će prepoznati vaš Portal. Zatim kliknite na "*Continue*".


![Image](assets/fr/07.webp)


Da biste kreirali novi Wallet, izaberite "*generate seed na Portalu*" zatim kliknite na "*Nastavi*".


![Image](assets/fr/08.webp)


Možete birati između 12- ili 24-reči Mnemonic fraze. Bezbednost koju nude obe opcije je slična, tako da možete izabrati onu koju je najlakše sačuvati, tj. 12 reči.


![Image](assets/fr/09.webp)


Zatim će vam biti zatraženo da izaberete lozinku. Lozinka otključava vaš Portal. Stoga pruža zaštitu protiv neovlašćenog fizičkog pristupa. Ova lozinka nije uključena u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovoj lozinci, posedovanje vaše 12- ili 24-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima. Preporučljivo je izabrati lozinku koja je što je moguće nasumičnija i dovoljno dugačka. Uverite se da ste ovu lozinku sačuvali na odvojenom mestu od mesta gde je vaš Portal uskladišten (npr. u menadžeru lozinki).


![Image](assets/fr/10.webp)


Vaš Portal će prikazati vašu 12-rečnu Mnemonic frazu. Ova Mnemonic vam daje pun, neograničen pristup svim vašim bitcoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem Portalu.


Fraza od 12 reči vraća pristup vašim bitkoinima u slučaju gubitka, krađe ili oštećenja vašeg Portala. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete ga ispisati na komad papira, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.


Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**Naravno, nikada ne smete deliti ove reči na Internetu, kao što ja radim u ovom uputstvu. Ovaj uzorak Wallet će biti korišćen samo na Testnet i biće obrisan na kraju uputstva.**_


Pritisnite dugme na vašem Portalu čvrsto da pređete na sledeće reči. Uverite se da ste stavili ceo prst na dugme i držite pritisak nekoliko sekundi, kako bi interakcija bila pravilno detektovana.


![Image](assets/fr/11.webp)


Vaš Portal će zatim potvrditi lozinku koju ste uneli u Nunchuk.


![Image](assets/fr/12.webp)


Sada ste završili konfigurisanje vašeg Portala i kreiranje vaše Mnemonic fraze!


![Image](assets/fr/13.webp)


## Bitcoin Wallet konfiguracija


Na Nunchuk-u, kliknite na "*Continue*", i dalje držeći vaš Portal na zadnjoj strani telefona.


![Image](assets/fr/14.webp)


U ovom uputstvu, postaviću single-sig Wallet, tako da biram ovu opciju.


![Image](assets/fr/15.webp)


Koristite podrazumevani nalog, tj. prvi nalog u Wallet (broj 0). Nunchuk će zatim tražiti da potvrdite lozinku za Portal kako biste ga otključali.


![Image](assets/fr/16.webp)


Na Portalu, potvrdite izvoz vašeg xpub-a na Nunchuk. Ovo vam omogućava da upravljate Wallet sa vašeg pametnog telefona bez mogućnosti trošenja bitcoina bez Portala. Pritisnite dugme da potvrdite.


Imajte na umu da će putanja izvođenja u vašem slučaju biti drugačija od moje, jer se ovaj vodič izvodi na Testnet.


![Image](assets/fr/17.webp)


Nazovite svoj Wallet, na primer "*Portal*", zatim kliknite na "*Nastavi*".


![Image](assets/fr/18.webp)


Nunchuk vam zatim predstavlja vaš Descriptor. Dobro je napraviti rezervnu kopiju. Iako Descriptor ne omogućava trošenje bitkoina, omogućava praćenje putanja derivacije vaših ključeva iz vaše Mnemonic fraze u slučaju oporavka Wallet. Čuvajte ga na sigurnom mestu, jer iako njegovo curenje možda ne predstavlja sigurnosni problem, predstavlja problem poverljivosti.


Kliknite na "*Done*".


![Image](assets/fr/19.webp)


Sada ćete morati da generate javne ključeve za vaš Bitcoin Wallet. Da biste to uradili, kliknite na dugme "*Create new Wallet*".


![Image](assets/fr/20.webp)


Kliknite ponovo na "*Create new Wallet*". Zatim izaberite opciju "*Create a new Wallet using existing keys*".


![Image](assets/fr/21.webp)


Izaberite ime za vaš Wallet i kliknite na "*Nastavi*".


![Image](assets/fr/22.webp)


Izaberite svoj Portal kao uređaj za potpisivanje za ovaj novi set ključeva, zatim kliknite na "*Nastavi*".


![Image](assets/fr/23.webp)


Ako je sve po vašem zadovoljstvu, potvrdite kreaciju.


![Image](assets/fr/24.webp)


Zatim možete sačuvati vašu Wallet konfiguracionu datoteku. Ova datoteka sadrži samo vaše javne ključeve, što znači da čak i ako neko pristupi njoj, neće moći da ukrade vaše bitkoine. Međutim, moći će da prate sve vaše transakcije. Ova datoteka stoga predstavlja rizik samo za vašu privatnost. U nekim slučajevima, može biti neophodna za oporavak vašeg Wallet.


![Image](assets/fr/25.webp)


I to je sve što treba da se uradi!


![Image](assets/fr/26.webp)


## Kako mogu primiti bitkoine putem Portala?


Da biste primili bitkoine, izaberite svoj Wallet.


![Image](assets/fr/27.webp)


Pre nego što upotrebite generisani Address, proverite ga na ekranu Portala. Da biste to uradili, kliknite na "*Primi*".


![Image](assets/fr/28.webp)


Kliknite na tri tačke, zatim izaberite "*Verifikuj Address putem PORTALA*". Zatim unesite svoju lozinku.


![Image](assets/fr/29.webp)


Postavite svoj Portal na poleđinu telefona, zatim potvrdite pritiskom na dugme.


![Image](assets/fr/30.webp)


Proverite da li se Address prikazan na Portalu poklapa sa onim na vašem Nunchuk-u, zatim potvrdite pritiskom na dugme ponovo. Ako su adrese identične, možete dati ovaj Address platiocu.


![Image](assets/fr/31.webp)


Jednom kada je transakcija platioca emitovana, videćete je na vašem Wallet.


![Image](assets/fr/32.webp)


Kliknite na "*View corners*".


![Image](assets/fr/33.webp)


Odaberite svoj novi UTXO.


![Image](assets/fr/34.webp)


Kliknite na "*+*" pored "*Oznake*" da dodate oznaku vašem UTXO. Ovo je dobra praksa, jer vam pomaže da se setite odakle dolaze vaši novčići i optimizuje vašu privatnost prilikom trošenja u budućnosti.


![Image](assets/fr/35.webp)


Odaberite postojeću oznaku ili kreirajte novu, zatim kliknite na "*Sačuvaj*". Takođe možete kreirati "*kolekcije*" kako biste organizovali svoje delove na strukturiraniji način.


![Image](assets/fr/36.webp)


## Kako da pošaljem bitkoine koristeći Portal?


Sada kada imate bitkoine u svom Wallet, možete ih i poslati. Da biste to učinili, kliknite na Wallet po vašem izboru.


![Image](assets/fr/37.webp)


Kliknite na dugme "*Pošalji*".


![Image](assets/fr/38.webp)


Izaberite iznos za slanje, zatim kliknite na "*Nastavi*".


![Image](assets/fr/39.webp)


Dodajte "*napomenu*" svojoj budućoj transakciji da vas podseti na njenu svrhu.


![Image](assets/fr/40.webp)


Zatim unesite Address primaoca u predviđeno polje. Takođe možete skenirati Address kodiran kao QR kod klikom na ikonu u gornjem desnom uglu ekrana. Zatim kliknite na dugme "*Create Transaction*".


![Image](assets/fr/41.webp)


Proverite detalje transakcije, zatim kliknite na dugme "*Potpiši*" pored vašeg Portala i unesite vašu lozinku.


![Image](assets/fr/42.webp)


Postavite svoj Portal na poleđinu telefona. Proverite da li su Address primaoca i iznos tačni. Ako jesu, pritisnite dugme za nastavak.


![Image](assets/fr/43.webp)


Proverite da li je naknada za transakciju tačna, zatim ponovo pritisnite dugme da potpišete svoju transakciju.


![Image](assets/fr/44.webp)


Vaša transakcija je potpisana. Možete poslednji put proveriti njene detalje na Nunchuk, a zatim kliknite na dugme "*Broadcast transaction*" da biste je emitovali na Bitcoin mreži.


![Image](assets/fr/45.webp)


Vaša transakcija sada čeka potvrdu.


![Image](assets/fr/46.webp)


Čestitamo, sada ste savladali korišćenje Portala! Ako vam je ovaj vodič bio koristan, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!


Da biste saznali više, pogledajte naš kompletan kurs obuke o tome kako funkcionišu HD novčanici:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f