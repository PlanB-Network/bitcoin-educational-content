---
name: Sats.mobi

description: Telegram-pristupačan kustodijalni Wallet
---

![cover](assets/cover.webp)


_Ovaj vodič je napisao_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi je Wallet koji radi na Telegramu, sa svim funkcionalnostima Lightning Network (custodial) Wallet, plus niz veoma zabavnih funkcija. Nastao je iz Fork sada već ukinutog LightningTipBot-a, nasleđujući sve njegove funkcije dok je dodao savremenije, čineći ga modernijim. Kao i LNTipBot, Sats.Mobi takođe prihvata filozofiju otvorenog koda. Wallet se može konfigurisati i upravljati nezavisno kloniranjem iz ovog [repozitorijuma](https://github.com/massmux/SatsMobiBot).


Ako više volite da ga koristite jednostavno, započinjanje ćaskanja na Telegramu će otkriti da je to bot.


## Postavke

Iz trake za pretragu na Telegramu potražite "satsmobi" i pojaviće se link ka [botu](@SatsMobiBot).


**Pažnja**: Ako niste sigurni kako da pretražujete putem Telegrama, pristupite botu sigurno koristeći sledeći [link](https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Sve što treba da uradite da biste započeli je da pritisnete _START_


![image](assets/it/02.webp)


Da biste istražili Wallet, možete odabrati _Menu_ u donjem levom uglu.


![image](assets/it/03.webp)


Sada izaberite _/help_ među glavnim komandama.


![image](assets/it/04.webp)


Sats.Mobi nas dočekuje prikazivanjem poruke, navodeći sve glavne funkcionalnosti. Prilikom pokretanja, bot je takođe kreirao LN Address, povezan sa izabranim nalogom na Telegramu (koji je jedinstven po defaultu). Komande za slanje i primanje Sats sa ovim Wallet su vidljive, kao i druge funkcije koje ćemo kasnije videti. Zanimljivo je takođe pogledati _/advanced_ meni.


![image](assets/it/05.webp)


Primetno je da je Sats.Mobi takođe kreirao anonimni LN Address, koji se koristi za postizanje privatnosti. Bot radi sa komandama: samo kliknite na odgovarajuću reč, ili upišite kosu crtu "/" u traku za poruke, praćenu komandom koju želite da izvršite. Čak i ako je Wallet tek kreiran, izaberite na primer _/transactions_


![image](assets/it/06.webp)


Ova komanda prikazuje listu najnovijih transakcija, u ovom konkretnom slučaju jednakih nuli.


![image](assets/it/07.webp)


## Primanje Sats

Komanda za kreiranje Invoice i primanje Sats je _/invoice_. Sats.Mobi posluje isključivo u Satoshi, najmanjoj jedinici Bitcoin; stoga, da biste kreirali Invoice, potrebno je napisati iznos u Sats u traku za poruke i zatim ga poslati u četu sa botom.

![image](assets/it/08.webp)


U sledećem primeru, izbor je napravljen da se primi iznos od 210 Sats.


![cover](assets/it/09.webp)


Nakon nekoliko trenutaka čekanja da se Invoice pripremi, dostupan je kao tekst i kao QR kod. Plaćajući Invoice, Wallet prikazuje stanje. Ako iz nekog razloga ukupni iznos nije ažuriran, napišite _/balance_ i pritisnite taster `enter`.


![image](assets/it/10.webp)


## Slanje Sats


Iako su Sats izuzetno vredna imovina, sa kojom se ne treba olako rastajati, Sats.Mobi čini ovaj deo privlačnim, izvođenje nekih kratkih testova (npr. nekoliko probnih transakcija) neće predstavljati problem.


### Plaćanje Invoice


Najjednostavniji način da platite Invoice je da kopirate niz poruke `lnbc1xxxxx` i zalepite ga u traku za poruke nakon što otkucate komandu _/pay_. **Ispravna sintaksa** zahteva ostavljanje razmaka nakon komande.


![image](assets/it/11.webp)


Wallet šalje poruku tražeći potvrdu. Klikom na _Plati_, Invoice se plaća.


![image](assets/it/12.webp)


Sats.Mobi može se osloniti na efikasan i dobro povezan Lightning čvor, retko kada plaćanja ne uspevaju jer uvek uspeva da pronađe ispravnu rutu.


### Plaćanje udobno sa mobilnog


Pregledajući na Telegramu, Sats.Mobi je takođe dostupan na mobilnim uređajima. Najpogodnija funkcija za plaćanje putem mobilnog je skeniranje QR koda, ali ovaj Wallet ga nema po dizajnu, jer nije samostalna aplikacija već je sadržana u društvenoj mreži. Sats.Mobi je stoga programiran da olakša mobilno iskustvo što je više moguće: zaista može dekodirati sliku, poput fotografije snimljene QR koda Invoice koji želite platiti.


Pretpostavimo, na primer, da želite da platite Invoice od 50 Sats.


![image](assets/it/20.webp)


Kada nam se ovo pokaže, možemo fotografisati odgovarajući QR kod.


![image](assets/it/21.webp)


Zatim otvaramo Telegram na mobilnom i, u ćaskanju sa Sats.Mobi, prilažemo upravo napravljenu fotografiju QR koda.


![cover](assets/it/22.webp)


Jednom kada je odabrano, šaljemo ga botu:


![image](assets/it/23.webp)

Sats.Mobi dekodira fotografiju i **odmah prikazuje zahtev za plaćanje**, sa tačnim opisom. Čet traži potvrdu, da biste nastavili morate pritisnuti _/pay_

![image](assets/it/24.webp)


Molimo sačekajte trenutak da se uplata obradi.


![image](assets/it/25.webp)


Invoice za 50 Sats je plaćen, rezultat postignut bez korišćenja kamere i njene integrisane funkcije skeniranja.


### Sats.Mobi u Telegram grupama


![image](assets/it/27.webp)


Među funkcijama koje su učinile LNTipBot poznatim i koje Sats.Mobi donosi na Telegram, nalazi se ona koja čini iskustvo zabavnim i interaktivnim za članove u grupi.

Vlasnici mogu pozvati bota da se pridruži grupnom četu i zatim imenovati Sats.Mobi kao administratora. Od tog trenutka počinje zabava, jer članovi mogu početi nagrađivati druge korisnike za njihov doprinos grupi.


- _/tip_ dodaje napojnicu odgovaranjem na poruku;
- _/send_ šalje sredstva navodeći LN Address ili Telegram korisničko ime kao primaoca;
- _/faucet_ (u _/advanced_ meniju) omogućava kreiranje serije napojnica koje najbrži članovi grupe mogu prikupiti klikom na _/collect_;
- _/tipjar_ (u _/advanced_ meniju) kreira drugu vrstu distribucije koja može biti poslata korisnicima u grupi.


Svaka od ovih komandi ima svoju sintaksu, koja je objašnjena u glavnom meniju komandi.


A ako mi nismo vlasnik grupe? Nema problema: samo zamolite osnivača da pozove Sats.Mobi, dodajte ga kao administratora grupe i sve je spremno!


## Point of Sale (POS)


Kada se Sats.Mobi pokrene prvi put, bot takođe kreira još jednu funkciju za korisnika: **POS**. "Uređaj" se aktivira od strane korisnika komandom _/pos_ ili klikom na odgovarajuće dugme iz konzole u donjem desnom uglu. U stvari, POS je veb aplikacija, koja se otvara kao iskačući prozor u Telegram četu.


![image](assets/it/14.webp)


Interface prikazuje lični Telegram nalog korisnika u gornjem levom uglu i koristi se jednostavno kao i svi POS uređaji: unosom iznosa na tastaturi. Pretpostavimo sada da želimo da naplatimo 21 euro cent za uslugu. Znajući da Sats.Mobi samo nativno upravlja Sats, nije lako izvršiti konverziju u glavi. Naprotiv, POS prikazuje euro kao obračunsku jedinicu, istovremeno prikazujući ekvivalent u Satoshi.


![image](assets/it/15.webp)

Klikom na _/OK_ prikazuje se Invoice koji se može pokazati kupcu putem QR koda, ili se može poslati kao string putem instant poruka, kako bi se mogao platiti.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Prirodno, POS je takođe dostupan na mobilnim telefonima, pristupa mu se na isti način kao što je prethodno prikazano.


![image](assets/it/18.webp)


Takođe je dobro prikazano na ekranu mobilnog telefona:


![image](assets/it/19.webp)


## Dodatne funkcije


Postoje i druge funkcije koje dopunjuju ponudu Sats.Mobi Wallet, koje, kao što smo videli, proširuju koncept Wallet izvan operacija primanja i slanja uplata:


- _/nostr_: da povežete Wallet sa svojim Nostr korisnikom kako biste primali zaps;
- _/cashback_: prikazuje kod koji se može predstaviti trgovcu za ostvarivanje povrata novca pri kupovini;
- _/buy_: pokreće vođenu proceduru unutar bota, koja omogućava kupovinu Sats za evre;
- _/activatecard_: da zatražite aktivaciju NFC debitne kartice, koja se može dopuniti putem Sats.Mobi Wallet i za koju se mogu aktivirati obaveštenja;
- _/link_: kreira link za vaš sopstveni Zeus ili Blue Wallet, koji se može koristiti kao daljinski upravljač za ovaj Wallet.


## Zaključak

Sats.Mobi je prijatan i zabavan Wallet za korišćenje, koji vraća iskustva stečena sa LNTipBot koristeći naprednije funkcije LNBits. Međutim, važno je zapamtiti da **je to kustodijalna usluga**. Stoga, treba ga koristiti za držanje vrlo malo Sats, nije glavni Wallet za vaša Lightning Network sredstva. Takođe postoji intrinzično ograničenje kapaciteta, jednako 500,000 Sats, ograničenje koje se savetuje da se ne prekorači.


Ako tražite ne-kustodijalne Lightning Network novčanike, svakako je preporučljivo da pogledate druge proizvode.


---
### Dokumentacija


- [Github](https://github.com/massmux/SatsMobiBot)
- Plejlista [video snimaka](https://www.youtube.com/results?search_query=Sats.mobi) demo