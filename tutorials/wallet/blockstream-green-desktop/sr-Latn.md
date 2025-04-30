---
name: Blockstream Green - Desktop
description: Korišćenje Green Wallet na vašem računaru
---
![cover](assets/cover.webp)


U ovom vodiču ćemo istražiti kako koristiti Blockstream Green softver na vašem računaru za upravljanje sigurnim Wallet na Hardware Wallet. Kada koristite Hardware Wallet, neophodno je koristiti softver na vašem računaru za upravljanje Wallet. Ovaj softver za upravljanje nema pristup privatnim ključevima; koristi se isključivo za konsultovanje vašeg Wallet stanja, generate adresa za primanje, i izgradnju i distribuciju transakcija koje će biti potpisane od strane Hardware Wallet. Green je samo jedno od mnogih rešenja dostupnih za upravljanje vašim Bitcoin Hardware Wallet.


U 2024. godini, Blockstream Green je kompatibilan samo sa Ledger Nano S (stara verzija), Ledger Nano X, Trezor One, Trezor T i Blockstream Jade uređajima.


## Predstavljamo Blockstream Green


Blockstream Green je softverska aplikacija dostupna na mobilnim uređajima i desktop računarima. Ranije poznat kao Green Address, ovaj Wallet je postao Blockstream projekat nakon akvizicije 2016. godine.


Green je veoma jednostavna aplikacija za korišćenje, što je čini posebno pogodnom za početnike. Nudi razne funkcionalnosti, kao što su upravljanje Hot novčanicima, hardverskim novčanicima, kao i novčanicima na Liquid Sidechain. Takođe je možete koristiti za postavljanje Watch-only wallet.


![GREEN-DESKTOP](assets/fr/01.webp)


U ovom uputstvu, fokusiraćemo se isključivo na korišćenje softvera na računaru. Da biste istražili druge upotrebe Green, molimo vas da pogledate naša druga posvećena uputstva:


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Instaliranje i konfiguracija Blockstream Green softvera


Počnite instaliranjem Blockstream Green softvera na vašem računaru. Idite na [zvaničnu web stranicu](https://blockstream.com/Green/) i kliknite na dugme "*Download Now*". Zatim pratite proces instalacije u skladu sa vašim operativnim sistemom.


![GREEN-DESKTOP](assets/fr/02.webp)


Pokrenite aplikaciju, a zatim označite polje "Prihvatam uslove...*".


![GREEN-DESKTOP](assets/fr/03.webp)


Kada prvi put otvorite Green, početni ekran se pojavljuje bez konfigurisanog Wallet. Kasnije, ako kreirate ili uvezete novčanike, oni će se pojaviti u ovom Interface. Pre nego što pređete na kreiranje Wallet, preporučujem da prilagodite postavke aplikacije prema vašim potrebama. Kliknite na ikonu Postavke u donjem levom uglu.


![GREEN-DESKTOP](assets/fr/04.webp)


U meniju "*General*" možete promeniti jezik softvera i aktivirati eksperimentalne funkcije ako želite.


![GREEN-DESKTOP](assets/fr/05.webp)


U meniju "*Network*" možete omogućiti povezivanje putem Tor mreže, koja šifrira sve vaše veze i otežava praćenje vaših aktivnosti. Iako ova opcija može malo usporiti rad aplikacije, toplo se preporučuje za zaštitu vaše privatnosti, posebno ako ne koristite svoj sopstveni kompletan čvor.


![GREEN-DESKTOP](assets/fr/06.webp)


Za korisnike koji imaju svoj kompletan čvor, Green nudi opciju povezivanja putem Electrum servera, garantujući potpunu kontrolu nad informacijama mreže Bitcoin i distribucijom transakcija. Da biste to uradili, kliknite na meni "*Prilagođeni serveri i validacija*", zatim unesite detalje vašeg Electrum servera.


![GREEN-DESKTOP](assets/fr/07.webp)


Još jedna alternativna funkcija je opcija "*SPV Verification*", koja vam omogućava da direktno verifikujete određene Blockchain podatke i tako smanjite potrebu za poverenjem u podrazumevani čvor Blockstream-a, iako ova metoda ne pruža sve garancije Full node. Ova opcija se takođe može pronaći u meniju "*Custom servers and validation*".


![GREEN-DESKTOP](assets/fr/08.webp)


Kada prilagodite ove parametre svojim potrebama, možete izaći iz ovog Interface.


## Uvezi Bitcoin Wallet na Blockstream Green


Sada ste spremni da uvezete svoj Bitcoin Wallet. Kliknite na dugme "**Get Started**".


![GREEN-DESKTOP](assets/fr/09.webp)


Možete birati između kreiranja lokalnog Software Wallet ili upravljanja Cold Wallet putem Hardware Wallet. Za ovaj vodič, koncentrisaćemo se na upravljanje Hardware Wallet, tako da ćete morati odabrati opciju "*On Hardware Wallet*".


Opcija "*Watch-only*" omogućava vam da uvezete prošireni javni ključ (`xpub`) kako biste pregledali Wallet transakcije bez mogućnosti trošenja povezanih sredstava.


![GREEN-DESKTOP](assets/fr/10.webp)


Ako koristite Jade, kliknite na odgovarajuće dugme. U suprotnom, izaberite "*Poveži drugi hardverski uređaj*". U mom slučaju, koristim Ledger Nano S. Za korisnike Ledger, uverite se da ste instalirali aplikaciju "*Bitcoin Legacy*" na vaš Hardware Wallet, jer Green podržava samo ovu verziju.


![GREEN-DESKTOP](assets/fr/11.webp)


Povežite svoj Hardware Wallet sa računarom i izaberite Green.


![GREEN-DESKTOP](assets/fr/12.webp)


Sačekajte da Green uveze vaše Wallet informacije, nakon čega ćete im moći pristupiti.


![GREEN-DESKTOP](assets/fr/13.webp)


U ovom trenutku postoje dva moguća scenarija. Ako ste ranije koristili svoj Hardware Wallet, vaš nalog bi trebalo da se pojavi u softveru. Ali ako ste, kao ja, upravo inicijalizovali svoj Hardware Wallet generisanjem Mnemonic fraze bez prethodnog korišćenja, moraćete da kreirate nalog. Kliknite na "*Create Account*".


![GREEN-DESKTOP](assets/fr/14.webp)


Izaberite "*Standard*" ako želite koristiti klasični Wallet.


![GREEN-DESKTOP](assets/fr/15.webp)


Sada imate pristup svom nalogu.


![GREEN-DESKTOP](assets/fr/16.webp)


## Korišćenje Hardware Wallet sa Blockstream Green


Sada kada je vaš Bitcoin Wallet postavljen, spremni ste da primite svoj prvi Sats! Jednostavno kliknite na dugme "*Receive*".


![GREEN-DESKTOP](assets/fr/17.webp)


Kliknite na dugme "*Copy Address*" da kopirate Address, ili skenirajte njegov QR kod.


![GREEN-DESKTOP](assets/fr/18.webp)


Jednom kada je transakcija emitovana na mreži, pojaviće se u vašem Wallet. Sačekajte dok ne dobijete dovoljno potvrda da biste smatrali transakciju nepromenljivom.


![GREEN-DESKTOP](assets/fr/19.webp)


Sa bitcoinima u vašem Wallet, sada ste spremni da ih pošaljete. Kliknite na dugme "*Send*".


![GREEN-DESKTOP](assets/fr/20.webp)


Na sledećoj stranici unesite primalacov Address. Možete ga uneti ručno ili skenirati QR kod pomoću vaše veb kamere.


![GREEN-DESKTOP](assets/fr/21.webp)


Izaberite iznos plaćanja.


![GREEN-DESKTOP](assets/fr/22.webp)


Na dnu ekrana, možete odabrati stopu naknade za ovu transakciju. Imate izbor da pratite preporuke aplikacije ili da prilagodite svoje naknade. Što je naknada viša u odnosu na druge transakcije na čekanju, vaša transakcija će biti brže obrađena. Za informacije o tržištu naknada, posetite [Mempool.space](https://Mempool.space/) u sekciji "*Transaction Fees*".


![GREEN-DESKTOP](assets/fr/23.webp)


Ako želite da odaberete tačno koje UTXO-e da koristite u svojoj transakciji, kliknite na dugme "*Manual coin selection*".


![GREEN-DESKTOP](assets/fr/24.webp)


Proverite parametre transakcije i, ako je sve kako očekujete, kliknite na "*Dalje*".


![GREEN-DESKTOP](assets/fr/25.webp)


Dvostruko proverite da li su Address, iznos i naknade tačni, a zatim kliknite na "*Potvrdi transakciju*".


![GREEN-DESKTOP](assets/fr/26.webp)


Proverite da su svi parametri transakcije tačni na vašem Hardware Wallet ekranu, zatim potpišite transakciju koristeći ga.


![GREEN-DESKTOP](assets/fr/27.webp)


Jednom kada je transakcija potpisana sa Hardware Wallet, Green je automatski emituje na Bitcoin mrežu. Vaša transakcija će se zatim pojaviti na vašoj Bitcoin Wallet kontrolnoj tabli, čekajući potvrdu.


![GREEN-DESKTOP](assets/fr/28.webp)


Sada znate kako lako konfigurisati Blockstream Green za upravljanje vašim Bitcoin Wallet na Hardware Wallet.


Ako ste našli ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!


Takođe vam preporučujem da pogledate ovaj drugi sveobuhvatni vodič o mobilnoj aplikaciji Blockstream Green za postavljanje Hot Wallet:


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143