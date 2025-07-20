---
name: passphrase BIP39 Trezor
description: Kako da dodam passphrase u svoj Trezor portfolio?
---
![cover](assets/cover.webp)



passphrase BIP39 je opcionalna lozinka koja, u kombinaciji sa Mnemonic frazom, pruža dodatni Layer sigurnosti za determinističke i hijerarhijske Bitcoin portfolije. U ovom vodiču ćemo zajedno otkriti kako postaviti passphrase na vašem sigurnom Bitcoin Wallet na Trezoru (Safe 3, Safe 5 i Model One).



![Image](assets/fr/01.webp)



Pre nego što započnete ovaj tutorijal, ako niste upoznati sa konceptom passphrase, kako funkcioniše i njegovim implikacijama za vaš Bitcoin Wallet, toplo preporučujem da se konsultujete sa ovim drugim teorijskim člankom gde objašnjavam sve (ovo je veoma važno, jer korišćenje passphrase bez potpunog razumevanja kako funkcioniše može ugroziti vaše bitkoine) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase na Trezoru se obrađuje na klasičan način ako ste se odlučili za BIP39 standard tokom konfiguracije (što preporučujem ako vam nije potreban *Multi-share Backup*). Ono što je posebno kod Trezora je da možete uneti passphrase direktno na Hardware Wallet, ili putem tastature vašeg računara koristeći Trezor Suite softver. Ova druga opcija je znatno manje sigurna, jer računar ima neuporedivo veću površinu za napad nego Hardware Wallet. Međutim, kucanje složenog passphrase može biti brže na konvencionalnoj tastaturi nego na Hardware Wallet, što bi moglo podstaći korišćenje jakih lozinki. Stoga je uvek bolje koristiti passphrase, čak i ako mora biti otkucan, nego ga uopšte ne koristiti. Važno je, međutim, ostati svestan povećanog rizika od numeričkih napada koje to podrazumeva.



Ove opcije nisu dostupne na svim softverima za upravljanje portfeljem kompatibilnim sa Trezorom. Na primer, za Model One, passphrase se može uneti putem tastature na Sparrow Wallet. Za Model T, modele Safe 3 i Safe 5, morate koristiti Trezor Suite ili uneti passphrase direktno na Hardware Wallet, jer je opcija unosa putem Sparrow-a onemogućena od strane HWI pre nekoliko godina.



![Image](assets/fr/02.webp)



U Trezor Suite, imate dva različita načina upravljanja potražnjom za passphrase. Možete aktivirati opciju "*passphrase*" u kartici "*Device*". Ako je omogućeno, Trezor Suite i sav drugi softver za upravljanje portfeljem će sistematski tražiti da unesete svoj passphrase svaki put kada pokrenete sistem. Ako preferirate diskretniji pristup korišćenju passphrase, možete zadržati postavku na "*Standard*". U tom slučaju, moraćete ručno pristupiti meniju vašeg Hardware Wallet u gornjem levom uglu i kliknuti na dugme "*+ passphrase*" svaki put kada ga pokrenete.



Pre nego što započnete ovaj vodič, molimo vas da se uverite da ste već inicijalizovali vaš Trezor i generisali vašu Mnemonic frazu. Ako niste, a vaš Trezor je nov, pratite vodič specifičan za model dostupan na Plan ₿ Network. Kada završite ovaj korak, možete se vratiti na ovaj vodič.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Dodavanje passphrase na Safe 3 ili Safe 5



Kada kreirate svoj Wallet, sačuvate svoj Mnemonic i postavite PIN, bićete preusmereni na početni meni Trezor Suite-a. U gornjem levom uglu, trebalo bi da se pojavi prozor koji vas poziva da aktivirate passphrase BIP39.



![Image](assets/fr/03.webp)



Ako se ovaj prozor ne pojavi, moraćete ručno da aktivirate opciju "*passphrase*" u kartici podešavanja "*Device*".



![Image](assets/fr/04.webp)



Ovaj prozor vas pita da unesete vaš passphrase. Izaberite jak passphrase i odmah napravite fizičku rezervnu kopiju, na mediju kao što je papir ili metal. U ovom primeru, izabrao sam passphrase: `fH3&kL@9mP#2sD5qR!82`. Ovo je primer; međutim, preporučujem da izaberete malo duži passphrase. Između 30 i 40 karaktera bi bilo idealno (kao dobra lozinka).



naravno, nikada ne bi trebalo da delite svoj passphrase na Internetu, kao što to radim u ovom vodiču. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan na kraju vodiča.**_



Za konkretnije preporuke o odabiru vašeg passphrase, pozivam vas da još jednom pogledate ovaj drugi članak:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Ako želite da unesete svoj passphrase putem tastature računara, unesite ga u predviđeno polje, a zatim kliknite na "*Access passphrase Wallet*".



![Image](assets/fr/05.webp)



Vaš Hardware Wallet će zatim prikazati vaš passphrase. Uverite se da se podudara sa vašom fizičkom rezervnom kopijom (papirnom ili metalnom) pre nego što kliknete na ekran da nastavite.



![Image](assets/fr/06.webp)



Ovo će vam omogućiti pristup vašem passphrase-zaštićenom portfoliju.



![Image](assets/fr/07.webp)



Ako želite da poboljšate sigurnost unosom vašeg passphrase samo na vašem Trezoru, kada se to zatraži, kliknite na "*Enter passphrase on Trezor*".



![Image](assets/fr/08.webp)



Na vašem Trezoru će se pojaviti T9 tastatura, omogućavajući vam da unesete vaš passphrase. Kada završite unos, kliknite na Green kvačicu da primenite passphrase na vaš Wallet.



![Image](assets/fr/09.webp)



Imaćete tada pristup vašem passphrase sigurnom Wallet.



![Image](assets/fr/10.webp)



Da biste koristili Sparrow Wallet, procedura je slična, ali za modele T, Safe 3 i Safe 5, passphrase mora biti unet na Hardware Wallet, a ne putem tastature računara.



Kad god Sparrow Wallet zahteva pristup vašem Trezoru, a passphrase još nije primenjen od poslednjeg pokretanja, moraćete da ga unesete koristeći T9 tastaturu.



![Image](assets/fr/11.webp)



## Dodavanje passphrase na Model One



Na Modelu One, upotreba passphrase BIP39 je gotovo neophodna. Kako ovaj uređaj ne uključuje Secure Element, relativno je lako izvući osetljive informacije. Stoga nije otporan na fizičke napade. Međutim, pošto se passphrase ne zadržava na uređaju nakon što je isključen, korišćenje jakog (neprobojivog) passphrase može vas zaštititi od većine poznatih fizičkih napada na ovom modelu.



Na Modelu One, nije moguće uneti passphrase direktno na Hardware Wallet. Moraćete da ga unesete putem tastature vašeg računara.



Jednom kada kreirate svoj Wallet, sačuvate svoj Mnemonic i postavite PIN, bićete prebačeni na početni meni Trezor Suite-a. U gornjem levom uglu trebalo bi da se pojavi prozor koji vas poziva da aktivirate passphrase BIP39.



![Image](assets/fr/12.webp)



Ako se ovaj prozor ne pojavi, potrebno je da aktivirate opciju "*passphrase*" u kartici "*Device*" podešavanja.



![Image](assets/fr/13.webp)



Ovaj prozor traži da unesete vaš passphrase. Izaberite jak passphrase i odmah napravite fizičku rezervnu kopiju, na mediju kao što je papir ili metal. U ovom primeru, izabrao sam passphrase: `fH3&kL@9mP#2sD5qR!82`. Ovo je samo primer; međutim, preporučujem da izaberete malo duži passphrase. Između 30 i 40 karaktera bi bilo idealno (kao dobra lozinka).



Za konkretnije preporuke o odabiru vašeg passphrase, ponovo vas pozivam da pogledate ovaj drugi članak:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Unesite svoj passphrase u predviđeno polje, zatim kliknite na dugme "*Access passphrase Wallet*".



![Image](assets/fr/14.webp)



Vaš Hardware Wallet će prikazati vaš passphrase. Uverite se da se podudara sa vašom fizičkom rezervnom kopijom (papirnom ili metalnom), zatim kliknite na dugme sa desne strane da nastavite.



![Image](assets/fr/15.webp)



Ovo će vas odvesti do vašeg passphrase-zaštićenog portfolija.



![Image](assets/fr/16.webp)



Da biste koristili Sparrow Wallet nakon toga, procedura ostaje ista. Svaki put kada Sparrow zahteva pristup vašem Hardware Wallet, a passphrase nije unet od poslednjeg pokretanja uređaja, moraćete da ga unesete.



![Image](assets/fr/17.webp)



Čestitamo, sada ste upoznati sa korišćenjem passphrase BIP39 na Trezor hardverskim novčanicima. Ako želite da unapredite svoju Wallet sigurnost, pogledajte ovaj vodič o Trezorovim *Multi-share* sistemima za bekap (*Shamir's Secret Sharing Scheme*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Ako ste smatrali ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!