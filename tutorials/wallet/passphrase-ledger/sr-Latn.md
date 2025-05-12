---
name: passphrase BIP39 Ledger
description: Kako dodati passphrase vašem Ledger Wallet?
---
![cover](assets/cover.webp)


BIP39 passphrase je opcionalna lozinka koja, kada se kombinuje sa vašom Mnemonic frazom, pruža dodatni Layer sigurnosti za determinističke i hijerarhijske Bitcoin novčanike. U ovom uputstvu, zajedno ćemo pregledati kako postaviti passphrase na vaš siguran Bitcoin Wallet na Ledger (bez obzira na model).


Pre nego što započnete ovaj tutorijal, ako niste upoznati sa konceptom passphrase, kako funkcioniše i njegovim implikacijama za vaš Bitcoin Wallet, toplo preporučujem da pogledate ovaj drugi teorijski članak gde sve objašnjavam:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Kako passphrase funkcioniše na Ledger?


Sa uređajima Ledger, imate dve različite opcije za konfigurisanje passphrase na vašem Wallet: opciju "*PIN-vezano*" i opciju "*privremeno*".


Sa opcijom "*PIN-tied*", povezujete passphrase sa drugim PIN-om na vašem Ledger. To znači da ćete imati 2 PIN-a: jedan za pristup vašem regularnom Wallet bez passphrase, i drugi za pristup vašem drugom Wallet zaštićenom passphrase.


![PASSPHRASE BIP39](assets/notext/03.webp)


U suštini, čak i sa ovom opcijom passphrase vezanom za drugi PIN, vaš passphrase ostaje vaš passphrase. To znači da ako izgubite svoj Ledger i želite da povratite svoje bitkoine na drugom uređaju ili softveru, apsolutno će vam biti potrebna vaša fraza od 24 reči i vaš **kompletan passphrase**. PIN povezan sa passphrase se koristi samo za pristup na vašem trenutnom Ledger, ali ne funkcioniše na drugim Ledgerima ili drugom softveru. Stoga je važno potpuno napraviti rezervnu kopiju vašeg passphrase na fizičkom mediju. **Poznavanje samo sekundarnog PIN-a nije dovoljno za ponovno dobijanje pristupa vašem Wallet**; to je jednostavno funkcija pogodnosti na vašem Ledger.


Ova druga opcija PIN-a je posebno zanimljiva za suočavanje sa fizičkim napadima. Na primer, ako vas napadač prisili da otključate svoj uređaj kako bi ukrao vaša sredstva, možete koristiti prvi PIN za pristup lažnom Wallet koji sadrži malu količinu bitkoina, dok vaša glavna sredstva ostaju sigurna iza drugog PIN-a.


Štaviše, ova opcija nudi sve sigurnosne prednosti BIP39 passphrase bez ograničenja da ga morate unositi ručno svaki put kada koristite svoj uređaj za potpisivanje. Ovo vam omogućava da koristite dug i nasumičan passphrase, čime se jača zaštita protiv napada grubom silom, dok se izbegava poteškoća ručnog unosa svaki put na malim dugmićima uređaja.

Opcija "privremeni passphrase" ne čuva passphrase na uređaju. Svaki put kada želite pristupiti vašem zaštićenom Wallet, moraćete ručno uneti passphrase na Ledger. Ovo čini korišćenje nezgodnijim, ali takođe blago povećava sigurnost jer ne ostavlja trag passphrase na uređaju. Čim isključite uređaj, on se vraća u svoje podrazumevano stanje i zahteva novi unos kompletnog passphrase za pristup skrivenim nalozima. Ova opcija "privremeni passphrase" je stoga slična radu drugih hardverskih novčanika.

U ovom uputstvu, koristiću Ledger Flex kao primer. Međutim, ako koristite drugi model Ledger, proces ostaje isti. Za Ledger Stax, Interface je isti kao kod Ledger Flex. Što se tiče modela Nano S, Nano S Plus i Nano X, iako je Interface drugačiji, proces i nazivi menija ostaju isti.


**Pažnja:** Ako ste već primili bitkoine na vaš Ledger pre aktiviranja passphrase, biće potrebno da ih prenesete putem Bitcoin transakcije. passphrase generiše set novih ključeva, čime se kreira Wallet koji je potpuno nezavisan od vašeg početnog Wallet. Kada dodate passphrase, imaćete novi Wallet koji će biti prazan. Međutim, ovo ne briše vaš prvi Wallet bez passphrase. I dalje možete pristupiti njemu, bilo direktno putem vašeg Ledger bez unosa passphrase ili preko drugog softvera koristeći vašu frazu od 24 reči.


Pre nego što započnete ovaj vodič, uverite se da ste već inicijalizovali svoj Ledger i generisali svoju Mnemonic frazu. Ako to nije slučaj i vaš Ledger je nov, pratite specifičan vodič za vaš model dostupan na PlanB Network. Kada završite ovaj korak, možete se vratiti na ovaj vodič.


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Kako postaviti privremeni passphrase sa Ledger?


Na početnoj stranici vašeg Ledger, kliknite na ikonu zupčanika za podešavanja.


![PASSPHRASE BIP39](assets/notext/04.webp)


Odaberite meni "Advanced", zatim "Set passphrase".


![PASSPHRASE BIP39](assets/notext/05.webp)


Ovo je korak gde možete birati između opcije "povezano sa PIN-om" ili opcije "privremeno" o kojoj smo govorili u prethodnom delu. Ovde ću objasniti kako postaviti privremeni passphrase, pa kliknite na "Postavi privremeni passphrase".


![PASSPHRASE BIP39](assets/notext/06.webp)

Zatim se od vas traži da unesete svoj passphrase. Izaberite jak passphrase i odmah nastavite sa fizičkom rezervnom kopijom, na medijumu kao što je papir ili metal. U ovom primeru, izabrao sam passphrase: `fH3&kL@9mP#2sD5qR!82`. Nakon unosa vašeg passphrase, kliknite na dugme "*Continue*".

![PASSPHRASE BIP39](assets/notext/07.webp)


Proverite da vaš passphrase odgovara onome što ste zabeležili na vašoj fizičkoj rezervnoj kopiji, zatim kliknite na dugme "*Da, tačno je*" da potvrdite.


![PASSPHRASE BIP39](assets/notext/08.webp)


Da biste završili kreiranje vašeg passphrase, unesite PIN kod vašeg Ledger. Od sada, kad god želite pristupiti vašem Wallet sa passphrase na Ledger, moraćete da pratite tačno iste korake kao što je ovde opisano.


![PASSPHRASE BIP39](assets/notext/09.webp)


Sada možete uvesti svoj set javnih ključeva na Sparrow Wallet da biste upravljali svojim Wallet. Na Sparrow-u, ovo će odgovarati drugačijem Wallet od vašeg početnog Wallet bez passphrase.


Otvorite Sparrow Wallet. Uverite se da je softver povezan sa čvorom, zatim kliknite na karticu "*File*" i izaberite "*New Wallet*".


![PASSPHRASE BIP39](assets/notext/10.webp)


Izaberite ime za vaš Wallet zaštićen passphrase. Za ovaj primer, odlučio sam se za ime koje eksplicitno uključuje termin "*passphrase*". Međutim, ako želite da zadržite diskreciju ovog Wallet na vašem računaru, možete izabrati manje evokativno ime.


![PASSPHRASE BIP39](assets/notext/11.webp)


Izaberite tip skripte za vaš Wallet. Savetujem vam da izaberete "*Taproot*" ili alternativno "*Native SegWit*".


![PASSPHRASE BIP39](assets/notext/12.webp)


Povežite svoj Ledger sa računarom, zatim kliknite na "*Connected Hardware Wallet*". Uverite se da ste već uneli svoj passphrase na vaš Ledger. Ako niste, molimo vas da se vratite na prethodne korake kako biste uneli svoj passphrase. Pre nego što nastavite sa skeniranjem, takođe se setite da otvorite aplikaciju "*Bitcoin*" na vašem Ledger.


![PASSPHRASE BIP39](assets/notext/13.webp)


Kliknite na dugme "*Skeniraj...*".


![PASSPHRASE BIP39](assets/notext/14.webp)


Kliknite na "*Import Keystore*" pored vašeg Ledger.


![PASSPHRASE BIP39](assets/notext/15.webp)


Vaš Wallet zaštićen od strane passphrase je sada kreiran na Sparrow. Da biste potvrdili, kliknite na dugme "*Apply*".


![PASSPHRASE BIP39](assets/notext/16.webp)

Izaberite jaku lozinku za zaštitu pristupa Sparrow Wallet. Ova lozinka će osigurati sigurnost pristupa vašim Wallet podacima na Sparrow-u, što pomaže u zaštiti vaših javnih ključeva, adresa, oznaka i istorije transakcija od bilo kakvog neovlašćenog pristupa.

Savetujem vam da sačuvate ovu lozinku u menadžeru lozinki kako je ne biste zaboravili.


![PASSPHRASE BIP39](assets/notext/17.webp)


I eto ga, vaš Wallet je sada kreiran! U meniju "*Settings*", Sparrow će vam pružiti vaš "*Master fingerprint*". Ovo predstavlja otisak vašeg glavnog ključa, koji se koristi kao osnova za izvođenje vašeg Wallet. Preporučujem da sačuvate kopiju ovog otiska. U mom primeru, on odgovara: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/18.webp)


Setite se šta smo pomenuli u prethodnim delovima: greška, čak i manja, pri unosu vašeg passphrase će generate potpuno novi Wallet sa različitim ključevima. Svaki put kada treba da se uverite da pristupate pravom Wallet sa ispravnim passphrase, proverite da li se otisak vašeg glavnog ključa poklapa sa onim koji ste zabeležili. Ova informacija, sama po sebi, ne predstavlja rizik za sigurnost vaših sredstava ili vašu privatnost.


Pre nego što koristite svoj Wallet sa passphrase, toplo vam savetujem da izvedete test oporavka na suvo. Zapišite referentni podatak kao što je vaš xpub ili otisak vašeg glavnog ključa, zatim resetujte svoj Ledger dok je Wallet još uvek prazan. Zatim pokušajte da obnovite svoj Wallet na Ledger koristeći svoje papirne rezervne kopije 24-reči fraze i passphrase. Proverite da li se informacije generisane nakon obnove podudaraju sa onim što ste prvobitno zabeležili. Ako je to slučaj, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.


## Kako postaviti passphrase povezan sa PIN-om sa Ledger?


Na početnoj stranici vašeg Ledger, kliknite na ikonu zupčanika za podešavanja.


![PASSPHRASE BIP39](assets/notext/19.webp)


Odaberite meni "*Advanced*", zatim "*Set passphrase*".


![PASSPHRASE BIP39](assets/notext/20.webp)


Ovo je korak gde možete birati između opcije "*povezano sa PIN-om*" ili "*privremeno*" o kojoj smo govorili u prethodnom delu. Ovde ću objasniti kako da postavite passphrase povezan sa PIN-om, pa kliknite na "*Postavi passphrase i poveži ga sa novim PIN-om*".


![PASSPHRASE BIP39](assets/notext/21.webp)

Morate zatim izabrati PIN kod koji će biti povezan sa vašim passphrase. Kao i sa glavnim PIN kodom, preporučuje se da izaberete 8-cifreni PIN kod, što je moguće nasumičniji. Takođe, obavezno sačuvajte ovaj kod na drugom mestu od onog gde je vaš Ledger Flex uskladišten.

U mom slučaju, glavni PIN kod je `58293647`, a izabrao sam `71425839` kao sekundarni PIN kod povezan sa passphrase.


![PASSPHRASE BIP39](assets/notext/22.webp)


Zatim se od vas traži da unesete svoj passphrase. Izaberite jak passphrase i odmah nastavite sa fizičkom rezervnom kopijom, na mediju kao što je papir ili metal. U ovom primeru, izabrao sam passphrase: `fH3&kL@9mP#2sD5qR!82`. Nakon unosa vašeg passphrase, kliknite na dugme "*Continue*".


![PASSPHRASE BIP39](assets/notext/23.webp)


Proverite da vaš passphrase odgovara onome što ste zabeležili na vašoj fizičkoj rezervnoj kopiji, zatim kliknite na dugme "*Da, tačno je*" da potvrdite.


![PASSPHRASE BIP39](assets/notext/24.webp)


Da biste finalizirali kreiranje vašeg passphrase, unesite glavni PIN kod vašeg Ledger (ne onaj koji je povezan sa passphrase).


![PASSPHRASE BIP39](assets/notext/25.webp)


Od sada, kad god želite da pristupite svom Wallet sa passphrase na Ledger, moraćete da unesete ne glavni PIN kod, već sekundarni PIN kod:


- Glavni PIN kod (`58293647`) > Wallet bez passphrase.
- Sekundarni PIN kod (`71425839`) > Wallet sa passphrase.


Sada možete uvesti svoj skup javnih ključeva na Sparrow Wallet kako biste upravljali svojim Wallet. Na Sparrow-u, ovo će odgovarati drugom Wallet od vašeg početnog Wallet bez passphrase.


Otvorite Sparrow Wallet. Uverite se da je softver povezan sa čvorom, zatim kliknite na karticu "*File*" i izaberite "*New Wallet*".


![PASSPHRASE BIP39](assets/notext/26.webp)


Izaberite ime za vaš Wallet zaštićen passphrase. Za ovaj primer, odlučio sam se za ime koje eksplicitno uključuje termin "*passphrase*". Međutim, ako želite da zadržite diskreciju ovog Wallet na vašem računaru, možete izabrati manje evokativno ime.


![PASSPHRASE BIP39](assets/notext/27.webp)


Izaberite tip skripte za vaš Wallet. Savetujem vam da izaberete "*Taproot*" ili, ako to nije moguće, "*Native SegWit*".


![PASSPHRASE BIP39](assets/notext/28.webp)

Povežite svoj Ledger sa računarom, zatim kliknite na "*Connected Hardware Wallet*". Uverite se da već imate svoj passphrase na svom Ledger tako što ćete ga otključati sekundarnim PIN kodom. Ako ne, restartujte svoj Ledger i unesite PIN kod povezan sa passphrase. Pre nego što nastavite sa skeniranjem, takođe se setite da otvorite aplikaciju "*Bitcoin*" na svom Ledger.


![PASSPHRASE BIP39](assets/notext/29.webp)


Kliknite na dugme "*Skeniraj...*".


![PASSPHRASE BIP39](assets/notext/30.webp)


Kliknite na "*Importuj Keystore*".


![PASSPHRASE BIP39](assets/notext/31.webp)


Vaš Wallet zaštićen passphrase sada je kreiran na Sparrow. Da biste potvrdili, kliknite na dugme "*Apply*".


![PASSPHRASE BIP39](assets/notext/32.webp)


Izaberite jaku lozinku kako biste osigurali pristup Sparrow Wallet. Ova lozinka će osigurati sigurnost pristupa vašim Wallet podacima na Sparrow-u, što pomaže u zaštiti vaših javnih ključeva, adresa, oznaka i istorije transakcija od bilo kakvog neovlašćenog pristupa.


Savetujem vam da sačuvate ovu lozinku u menadžeru lozinki kako je ne biste zaboravili.


![PASSPHRASE BIP39](assets/notext/33.webp)


I tu ga imate, vaš Wallet je sada kreiran! U meniju "*Settings*", Sparrow će vam obezbediti vaš "*Master fingerprint*". Ovo predstavlja otisak vašeg glavnog ključa, korišćenog u osnovi derivacije vašeg Wallet. Toplo preporučujem da sačuvate kopiju ovog otiska. U mom primeru, to odgovara: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/34.webp)


Setite se šta smo pomenuli u prethodnim delovima: greška, čak i manja, pri unosu vašeg passphrase će generate potpuno novi Wallet sa različitim ključevima. Svaki put kada treba da obezbedite pristup ispravnom Wallet sa pravim passphrase, proverite da li se otisak vašeg glavnog ključa poklapa sa onim koji ste zabeležili. Ove informacije, same po sebi, ne predstavljaju rizik za sigurnost vaših sredstava ili vašu privatnost.

Pre nego što koristite svoj Wallet sa passphrase, toplo vam preporučujem da izvedete test oporavka na suvo. Zapišite referentni podatak kao što je vaš xpub ili otisak prsta vašeg glavnog ključa, zatim resetujte svoj Ledger dok je Wallet još uvek prazan. Zatim pokušajte da obnovite svoj Wallet na Ledger koristeći svoje papirne rezervne kopije 24-reči fraze i passphrase. Proverite da li se informacije generisane nakon obnove podudaraju sa onim što ste prvobitno zabeležili. Ako je to slučaj, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.


Čestitamo, vaš Bitcoin Wallet je sada osiguran sa passphrase! Ako ste smatrali da je ovaj vodič koristan, bio bih zahvalan ako biste mogli ostaviti palac gore ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!


Takođe vam preporučujem da pogledate ovaj drugi kompletan vodič o tome kako koristiti vaš Ledger Flex:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a