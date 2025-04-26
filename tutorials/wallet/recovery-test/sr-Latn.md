---
name: Test oporavka
description: Kako testirati svoje rezervne kopije kako biste osigurali da ne izgubite svoje bitkoine?
---
![cover](assets/cover.webp)


Kada kreirate Bitcoin Wallet, od vas se traži da zapišete Mnemonic frazu, koja obično sadrži 12 ili 24 reči. Ova fraza vam omogućava da povratite pristup svojim bitkoinima u slučaju gubitka, oštećenja ili krađe uređaja na kojem se nalazi vaš Wallet. Pre nego što počnete da koristite svoj novi Bitcoin Wallet, veoma je važno da proverite validnost ove Mnemonic fraze. Najbolji način da to uradite je izvođenjem testnog oporavka.


Ovaj test uključuje simulaciju obnove Wallet pre nego što se u njega deponuju bilo kakvi bitkoini. Dokle god je Wallet prazan, simuliramo situaciju u kojoj je uređaj koji čuva naše ključeve izgubljen, a sve što nam je ostalo je naša Mnemonic fraza kako bismo pokušali da povratimo naše bitkoine.


![RECOVERY TEST](assets/notext/01.webp)


## Koja je svrha?


Ovaj proces testiranja omogućava vam da proverite da li je fizička kopija vaše Mnemonic fraze, bilo na papiru ili metalu, funkcionalna. Neuspeh tokom ovog testa oporavka ukazuje na grešku u bekapu fraze, čime se vaši bitkoini dovode u rizik. S druge strane, ako je test uspešan, to potvrđuje da je vaša Mnemonic fraza potpuno operativna, i tada možete sa sigurnošću čuvati bitkoine koristeći ovaj Wallet.


Izvođenje testiranja oporavka na suvo ima dvostruku prednost. Ne samo da vam omogućava da proverite tačnost vaše Mnemonic fraze, već vam pruža i priliku da se upoznate sa procesom oporavka Wallet. Na ovaj način, otkrićete potencijalne poteškoće pre nego što se stvarna situacija pojavi. Na dan kada zaista budete morali da oporavite svoj Wallet, bićete manje pod stresom, jer ćete već znati proces, smanjujući rizik od greške. Zato je važno ne zanemariti ovaj korak testiranja i odvojiti potrebno vreme da ga pravilno obavite.


## Šta je test oporavka?


Proces testa je prilično jednostavan:


- Nakon što kreirate svoj novi Bitcoin Wallet, i pre nego što deponujete svoje prve satoshije, zabeležite informacije o svedoku kao što su xpub, prvi prijemni Address, ili čak otisak prsta glavnog ključa;
- Zatim, namerno obrišite još uvek praznu Wallet, na primer, vraćanjem Hardware Wallet na fabrička podešavanja;
- Zatim, simulirajte oporavak vašeg Wallet koristeći samo papirne rezervne kopije vaše Mnemonic fraze i vaše passphrase ako je koristite;
- Na kraju, proverite da li se informacije svedoka podudaraju sa informacijama regenerisanog Wallet. Ako se informacije podudaraju, možete biti sigurni u pouzdanost vaše fizičke rezervne kopije, i tada možete poslati svoje prve bitkoine na ovaj Wallet.

Budite pažljivi, tokom testa oporavka, **morate koristiti isti uređaj namenjen za vaš konačni Wallet**, kako ne biste povećali površinu napada vašeg Wallet. Na primer, ako kreirate Wallet na Trezor Safe 5, obavezno obavite test oporavka na tom istom Trezor Safe 5. Važno je da ne unosite vašu frazu za oporavak u bilo koji drugi softver, jer bi to ugrozilo sigurnost koju pruža vaš Hardware Wallet, čak i ako je Wallet još uvek prazan.


## Kako izvršiti test oporavka?


U ovom uputstvu, objasniću kako da izvedete test oporavka na Bitcoin Software Wallet, koristeći Sparrow Wallet (za Hot Wallet). Međutim, proces ostaje isti za bilo koji drugi tip uređaja. Još jednom, **ako koristite Hardware Wallet, nemojte izvoditi test oporavka na Sparrow Wallet** (pogledajte prethodni odeljak).


Upravo sam kreirao novi Hot Wallet na Sparrow Wallet. Trenutno još nisam poslao bitkoine na njega. Prazan je.


![RECOVERY TEST](assets/notext/02.webp)


Pažljivo sam zabeležio svoju 12-rečnu Mnemonic frazu na parčetu papira. I pošto želim da poboljšam sigurnost ovog Wallet, takođe sam postavio BIP39 passphrase koji sam sačuvao na drugom parčetu papira:


```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```


```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```


***Očigledno, nikada ne bi trebalo da delite svoju Mnemonic frazu i svoj passphrase na internetu, za razliku od onoga što radim u ovom vodiču. Ovaj primer Wallet neće biti korišćen i biće obrisan na kraju vodiča.***


Sada ću zabeležiti na nacrtu deo informacija svedoka sa mog Wallet. Možete izabrati različite delove informacija, kao što su prvi prijemni Address, xpub, ili otisak prsta glavnog ključa. Lično, preporučujem da izaberete prvi prijemni Address. Ovo vam omogućava da proverite da li ste u mogućnosti da pronađete kompletnu prvu derivacionu putanju koja vodi do ovog Address.


Na Sparrow-u, kliknite na karticu "*Addresses*".


![RECOVERY TEST](assets/notext/03.webp)


Zatim, zapišite na parče papira prvi primljeni Address vašeg Wallet. U mom primeru, Address je:


```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```


Nakon što zabeležite informacije, idite na meni "*File*", zatim izaberite "*Delete Wallet*". Još jednom vas podsećam da vaš Bitcoin Wallet mora biti prazan pre nego što nastavite sa ovom operacijom.


![RECOVERY TEST](assets/notext/04.webp)


Ako je vaš Wallet zaista prazan, potvrdite brisanje vašeg Wallet.


![RECOVERY TEST](assets/notext/05.webp)


Sada treba da ponovite proces kreiranja Wallet, ali koristeći naše papirne rezervne kopije. Kliknite na "*File*" meni, a zatim na "*New Wallet*".


![RECOVERY TEST](assets/notext/06.webp)


Ponovo unesite ime vašeg Wallet.


![RECOVERY TEST](assets/notext/07.webp)


U meniju "*Script Type*" treba da izaberete isti tip skripte kao Wallet koji ste prethodno obrisali.


![RECOVERY TEST](assets/notext/08.webp)


Zatim kliknite na dugme "*New or Imported Software Wallet*".


![RECOVERY TEST](assets/notext/09.webp)


Odaberite tačan broj reči za vaš seed.


![RECOVERY TEST](assets/notext/10.webp)


Unesite svoju Mnemonic frazu u softver. Ako se pojavi poruka "*Invalid Checksum*", to ukazuje da je bekap vaše Mnemonic fraze netačan. Tada ćete morati da započnete kreiranje vaše Wallet ispočetka, jer je vaš test oporavka neuspešan.


![RECOVERY TEST](assets/notext/11.webp)


Ako imate passphrase, kao u mom slučaju, takođe ga unesite.


![RECOVERY TEST](assets/notext/12.webp)


Kliknite na "*Create Keystore*", zatim na "*Import Keystore*".


![RECOVERY TEST](assets/notext/13.webp)


I na kraju, kliknite na dugme "*Apply*".


![RECOVERY TEST](assets/notext/14.webp)


Sada se možete vratiti na karticu "*Addresses*".


![RECOVERY TEST](assets/notext/15.webp)


Konačno, proverite da li prvi primljeni Address odgovara onom koji ste zabeležili kao svedoka na vašem nacrtu.


![RECOVERY TEST](assets/notext/16.webp)


Ako se primajuće adrese podudaraju, vaš test oporavka je uspešan i možete koristiti svoj novi Bitcoin Wallet. Ako se ne podudaraju, to može ukazivati na grešku u izboru tipa skripte, što čini put derivacije netačnim, ili na problem sa rezervnom kopijom vaše Mnemonic fraze ili vašeg passphrase. U oba slučaja, snažno preporučujem da počnete ispočetka i kreirate novi Bitcoin Wallet od početka kako biste izbegli bilo kakav rizik. Ovog puta, pazite da zabeležite Mnemonic frazu bez grešaka.

Čestitamo, sada ste upoznati sa sprovođenjem testa oporavka! Savetujem vam da generalizujete ovaj proces za kreiranje svih vaših Bitcoin novčanika. Ako vam je ovaj vodič bio od pomoći, bio bih zahvalan ako biste mogli ostaviti palac gore ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!