---
name: COLDCARD Mk

description: Kreiranje, pravljenje rezervne kopije i korišćenje Bitcoin privatnog ključa sa Coldcard uređajem i Bitcoin Core
---

![cover](assets/cover.webp)


_Kreiranje, bekapovanje i korišćenje Bitcoin privatnog ključa sa Coldcard uređajem i Bitcoin Core_


## Potpuni vodič za generisanje privatnog ključa koristeći Coldcard i korišćenje istog kroz Interface vašeg Bitcoin Core čvora!


U srži korišćenja mreže Bitcoin leži koncept asimetrične kriptografije: par ključeva - jedan privatni i jedan javni - koji šifruju i dešifruju podatke, koncept koji osigurava poverljivost komunikacije.


U slučaju Bitcoin, generisanjem takvog para privatnih i javnih ključeva, možemo čuvati bitkoine (UTXO ili Neutrošeni Izlaz Transakcije) i potpisivati transakcije kako bismo ih potrošili.


Danas postoji više alata dostupnih za olakšavanje nasumičnog generisanja privatnog ključa i njegovog bekapa u tekstualnom obliku koristeći BIP 39 - standard koji određuje kako novčanici povezuju Mnemonic frazu (seed frazu) sa enkripcijskim ključevima. Češće nego ne, Mnemonic fraza se sastoji od 12 ili 24 reči, koje moraju biti sigurno bekapovane kako bi se mogao povratiti Wallet i njegovi bitkoini.


U ovom članku ćemo naučiti kako da generate privatni ključ koristeći Coldcard Mk4, jedan od najčešće korišćenih i najsigurnijih uređaja u svetu Bitcoin, koristeći metodu bacanja kockica kako bismo osigurali maksimalnu entropiju, i kako da ga koristimo sa Bitcoin Core na način bez povezivanja na mrežu!


**Napomena:🧰** Nabavite sledeće alate da biste koristili vodič:



- Coldcard uređaj (Mk3 ili Mk4)
- MicroSD kartica (4GB je dovoljno)
- Magnetni USB kabl samo za napajanje (mini-usb za Mk3, usb-c za Mk4)
- Jedna ili više kvalitetnih kockica za igru


## Generisanje nove Mnemonic fraze pomoću Coldcard-a


Počećemo proces kreiranja privatnog ključa od nule, pod pretpostavkom da je Coldcard tek raspakovan i da je na njemu već postavljen PIN (pratite korake na Coldcard-u tokom inicijalizacije uređaja).


**Napomena🚨:** Da biste resetovali privatni ključ već konfigurisanog Coldcard-a, pratite ove korake:

_Advanced/Tools > Danger Zone > seed Functions > Uništi seed > ✓_


**Pažnja:** vaš Coldcard će zaboraviti privatni ključ nakon ovih koraka. Uverite se da ste pravilno napravili rezervnu kopiju vaše Mnemonic fraze ako želite da je kasnije možete povratiti.


## Koraci koje treba pratiti:


Poveži se sa Coldcard pomoću PIN-a > Novi seed Reči > 24 Reči Bacanje Kockica


Izvršite 100 bacanja kockica, zapisujući rezultat dobijen od 1 do 6 na Coldcard nakon svakog bacanja. Praktikovanjem ove metode, kreirate 256 bajtova entropije, čime se favorizuje kreiranje potpuno nasumičnog privatnog ključa. Coinkite takođe pruža potrebnu dokumentaciju za nezavisnu verifikaciju njihovog sistema generisanja entropije.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


Kada se završi 100 bacanja kockica, pritisnite ✓ i zatim zapišite 24 dobijene reči redosledom. Proverite dvaput i pritisnite ✓. Na kraju, ostaje samo da završite test verifikacije 24 reči na Coldcard-u, i voila, vaš novi privatni ključ je kreiran!


Zatim, odlučite da li želite da aktivirate NFC (Mk4) i USB funkcije prateći prikazane korake. Kada ste u glavnom meniju, vreme je da ažurirate firmware uređaja. Idite na Advanced/Tools > Upgrade Firmware > Show Version, i proverite zvaničnu web stranicu da biste potvrdili i preuzeli najnoviju dostupnu verziju. Preporučljivo je ažurirati Coldcard kako biste iskoristili maksimalnu sigurnost.


Pre nego što nastavite, preporučuje se da zabeležite Otisak Prsta Glavnog Ključa (XFP) povezan sa privatnim ključem. Ovi podaci omogućavaju brzu validaciju da li ste u ispravnom Wallet u slučaju oporavka, na primer. Idite na Advanced/Tools > View Identity > Master Key Fingerprint (XFP) i zapišite niz od osam alfanumeričkih karaktera koji ste dobili. XFP se može zabeležiti na istom mestu kao i Mnemonic fraza, to nisu osetljivi podaci.


**Napomena:💡** preporučuje se testiranje vaše Mnemonic fraze za bekap u drugom softveru. Da biste to uradili bezbedno, konsultujte naš članak Verifikujte bekap Bitcoin Wallet sa Tails za manje od 5 minuta.


## Sigurnosni bonus: "Tajna fraza" (opcionalno)


passphrase (tajna fraza) je odličan element za dodavanje Wallet konfiguraciji kako bi se dodao Layer sigurnosti za zaštitu vaših bitkoina. passphrase deluje kao neka vrsta 25. reči za Mnemonic frazu. Kada se doda, kreira se potpuno novi Wallet zajedno sa privatnim ključem i pripadajućom Mnemonic frazom. Nije neophodno zapisivati novu Mnemonic frazu, jer se ovom Wallet može pristupiti kombinovanjem početne Mnemonic fraze sa odabranim passphrase.


Cilj je da se passphrase zabeleži odvojeno od fraze Mnemonic jer napadač koji ima pristup oba elementa imaće pristup sredstvima. S druge strane, napadač koji ima pristup samo jednom od ovih elemenata neće imati pristup sredstvima, i upravo ta specifična prednost optimizuje nivo sigurnosti konfiguracije Wallet.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## Koraci za dodavanje passphrase sa Coldcard:


passphrase > Dodaj Reči (preporučeno) > Primeni. Uređaj će prikazati XFP novog generisanog Wallet sa passphrase, što treba zabeležiti uz passphrase iz istih razloga pomenutih ranije.


**Saveti💡** Ovde se nalaze dodatni resursi vezani za passphrase:



- [Evo ovde](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) prvi od _Trezor_;
- [Ovde](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) možete pronaći drugi od _Coinkite_;
- I [ovde](https://armantheparman.com/passphrase/) ćete pronaći poslednji od _armantheparman_.


## Izvoz Wallet u Bitcoin Core


Wallet je sada spreman za izvoz u softver kako bi interagovao sa Bitcoin mrežom. U ovom vodiču ćemo koristiti Bitcoin Core (v24.1).


Pogledajte naše vodiče za instalaciju i konfiguraciju za Bitcoin Core:



- **Pokretanje sopstvenog čvora sa Bitcoin Core:** https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- **Konfigurisanje Tor-a za Bitcoin Core čvor:** https://agora256.com/configuration-tor-Bitcoin-core/


Prvo umetnite micro SD karticu u Coldcard, zatim izvezite Wallet za Bitcoin Core prateći ove korake: Advanced/Tools > Export Wallet > Bitcoin Core. Dva fajla će biti napisana na micro SD karticu: Bitcoin-core.sig & Bitcoin-core.txt. Umetnite micro SD karticu u računar gde je instaliran Bitcoin Core i otvorite .txt fajl. Videćete liniju "For Wallet with master key fingerprint." Proverite da li se osmo-karakterni XFP podudara sa onim koji ste zabeležili prilikom kreiranja vašeg privatnog ključa.'

Pre nego što pratite uputstva u datoteci, počnimo sa pripremom Wallet u Bitcoin Core Interface prateći ove korake: idite na karticu File > Create a Wallet. Izaberite ime za vaš Wallet (zamenljiv termin sa "porte-monnaie" u Core) i označite opcije Disable private keys, Create an empty Wallet, i Wallet descriptors kao što je prikazano na slici ispod. Zatim, pritisnite dugme Create.


![create a wallet](assets/guide-agora/3.webp)


Jednom kada je Wallet kreiran u Bitcoin Core, idite na karticu Window > Console i uverite se da izabrani Wallet na vrhu stranice prikazuje ime onog koji ste kreirali.


Sada, u .txt fajlu koji je ranije generisao Coldcard, kopiraj liniju koja počinje sa importdescriptors, zatim je nalepi u Bitcoin Core konzolu. Trebalo bi da bude vraćen odgovor koji uključuje liniju "success": true.


![nodes window](assets/guide-agora/4.webp)


Ako odgovor sadrži "message": "Ranged descriptors should not have a label", izbrišite unos "label": "Coldcard xxxx0000" u kopiranoj liniji iz .txt fajla, zatim nalepite kompletnu liniju nazad u Bitcoin Core konzolu.


Ako je potrebno, možete pronaći pomoć [ovde](https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md) na Coldcard Github-u.


## Validacija uvoza Wallet u Bitcoin Core


Da bi se osiguralo da je operacija bila uspešna, neophodno je potvrditi da je željeni Wallet uvezen u Bitcoin Core. Jednostavna metoda za potvrdu ovoga je da se proveri da li adrese generisane u Coldcard odgovaraju adresama generisanim u Bitcoin Core.


Bitcoin Core: Primi > Kreiraj novi prijemni Address

Coldcard: Address Explorer > Odaberite Address počinjući sa bc1q. Coldcard Address 'bc1q' treba da se poklapa sa Address prikazanim u Bitcoin Core.

Primanje i slanje transakcija u 'air-gapped' režimu


Primanje transakcije je izuzetno jednostavno; samo pritisnite Primi, označite transakciju (opciono, ali preporučljivo), i Kreirajte novi prijemni Address. Zatim, sve što preostaje je da podelite Address sa pošiljaocem.


Sada, ključni element ove Coldcard + Bitcoin Core postavke je slanje transakcija bez povezivanja Coldcard-a i njegovog privatnog ključa na internet, metoda koja se zove air-gapped i koristi TBSP (PSBT - Delimično Potpisane Bitcoin Transakcije) funkciju Bitcoin.

U suštini, koristimo Bitcoin Core Interface za konstruisanje transakcije, koju ćemo zatim izvesti putem micro SD kartice na Coldcard radi potpisivanja, a zatim vratiti potpisanu datoteku transakcije u Bitcoin Core i emitovati transakciju na mrežu. Moramo to uraditi na ovaj način jer Wallet importovan u Bitcoin Core nema privatni ključ, već samo javni ključ (što nam omogućava da generate naše adrese za primanje), tako da je nemoguće da direktno u softveru potpišemo transakciju kako bismo potrošili naše bitkoine.


Pre nego što nastavite, uverite se da su sledeće opcije omogućene u Podešavanja > Wallet:



- Omogući funkcije kontrole novčića
- Potroši nepotvrđene kovanice (Opcionalno)
- Omogući TBPS provere


![option ](assets/guide-agora/5.webp)


### Koraci za slanje u režimu bez mreže:


Pošalji > Unosi > izaberi željeni UTXO, zatim unesi primaočev Address u Plati. Naknada za transakciju: Izaberi... > Prilagođeno > Unesi naknadu za transakciju (Bitcoin Core računa u Sats/kilobajt umesto sat/bajt kao većina alternativnih Wallet rešenja. Dakle, 4000 Sats/kilobajt = 4 Sats/bajt). Kreiraj nepotpisanu transakciju > sačuvaj fajl na svoju mikro SD karticu i ubaci je u Coldcard.


U Coldcard-u, pritisnite Ready to sign, proverite detalje transakcije, zatim pritisnite ✓ i ubacite micro SD karticu nazad u računar kada potpisani fajlovi budu generisani.


Vratite se u Bitcoin Core, idite na karticu File > Load TBSP from file, i unesite potpisanu datoteku transakcije .PSBT. Kutija PSBT Operations će se pojaviti na ekranu, potvrđujući da je transakcija potpuno potpisana i spremna za emitovanje. Sve što preostaje je da pritisnete Broadcast transaction.


![PSBT operations](assets/guide-agora/6.webp)


### Zaključak


Kombinacija Coldcard uređaja sa Bitcoin Core, na kojem pokrećete svoj čvor, je moćna. Dodajte tome privatni ključ generisan sa 100 bacanja kockica i tajnu frazu, i vaša Wallet konfiguracija postaje sofisticirana i robusna tvrđava.


Slobodno nas kontaktirajte da podelite svoje komentare i pitanja! Naš cilj je da delimo znanje i povećavamo naše razumevanje iz dana u dan.