---
name: BitcoinVoucherBot P2P
description: Kako kupiti i prodati Bitcoin P2P sa BitcoinVoucherBot
---

![image](assets/cover.webp)



Još uvek čujemo o BitcoinVoucherBot-u, Telegram botu kreiranom za kupovinu Bitcoin bez [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) putem SEPA bankovnog transfera. Nažalost, od novembra 2025. godine, BitcoinVoucherBot u svom centralizovanom obliku više nije dostupan kao usluga bez KYC-a.



U ovom vodiču ćemo pogledati kako funkcioniše nova implementacija koja omogućava korisnicima da kupuju i prodaju Bitcoin direktno na novoj P2P (Peer-To-Peer) pijaci, bez KYC-a. Da bi se suprotstavili novim ograničenjima koja sve više ugrožavaju digitalnu slobodu i privatnost, programeri su kreirali ovo proširenje, dajući korisnicima mogućnost da kupuju i prodaju Bitcoin sa visokim stepenom anonimnosti putem P2P (Peer-To-Peer). Hajde da zajedno vidimo kako funkcioniše ovaj novi metod razmene.



Da biste koristili uslugu, moraćete da izvršite transfere putem Lightning Network. Zato se uverite da imate wallet koji podržava ovaj protokol i omogućava vam korišćenje "LNURL" ili "Lightning Address" za primanje i slanje sredstava.



Među podržanim novčanicima možemo pronaći:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet Od Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Skrbnički sa zamjenom na Neskrbnički)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Ili bilo koji wallet koji ima "Lightning Address" i generiše Bolt11 fakturu. novčanici koji generate Bolt12 fakturu trenutno nisu podržani. Za više informacija pogledajte definiciju [Bolt](https://planb.academy/resources/glossary/bolt).



Za ovaj vodič, s obzirom na lakoću trenutne upotrebe, koristićemo Wallet of Satoshi.



**Caution**: Wallet of Satoshi, while popular among beginners, is custodial, with limited control over funds; use it only transiently, transferring immediately to a non-custodial for full sovereignty. As of October 2025, it includes a stable self-custodial mode worldwide on iOS/Android (update the app), with autonomous private keys, switch between modes, custom Lightning addresses, and seed 12-word backup. However, it remains an interim solution until consolidation, preferring wallet non-custodial mature for long-term management.



Vrlo dobro! Sada možemo započeti naše putovanje, koje će vas voditi korak po korak u kreiranju vašeg naloga, upravljanju kupovinama i prodajama, i korišćenju vaše ograničene oblasti.



## Wallet i Upisivanje



Prvo, ako već nije instaliran na vašem pametnom telefonu, preuzmite Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Ako nikada niste koristili Wallet of Satoshi i želite da razumete kako funkcioniše, predlažem da pratite ovaj vodič kako biste ga pravilno aktivirali i bezbedno napravili rezervnu kopiju.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Sada kada je vaš wallet spreman, možete početi slati malu količinu sats. Imajte na umu da ćete, kako biste završili prijavu na vašu P2P (Peer-To-Peer) platformu, morati poslati 1000 sats kao kontrolnu meru: ovo je kako bi se stvorila barijera protiv bilo kakvih napada tipa phantom match (prevara), sprečavajući bilo koga da se prijavi bez ikakvog filtera za spam.



![image](assets/it/02.webp)



Sada možemo otvoriti P2P (Peer-To-Peer) platformu za nastavak upisa. Možete se prijaviti sa desktop računara ili pretraživača na pametnim telefonima, putem Telegram BitcoinVoucherBot-a ili putem .onion linkova kako biste obezbedili još veći nivo privatnosti.



ako odlučiš da koristiš Tor .onion link takođe preporučujem "Tor Browser". Ako ga još ne znaš, možeš saznati više o tome na ovom linku:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Sada izaberite kako želite da pristupite platformi.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Bićete preusmereni na glavnu stranicu.



pritisnite "Get Starter" da biste odmah započeli



![image](assets/it/03.webp)



Na sledećem ekranu morate izabrati lozinku i uneti je (polje A), a zatim je ponoviti (polje B). Preporučujem da odmah sačuvate ovu lozinku na rezervnom mediju, koji može biti na sigurnom digitalnom uređaju kao što je "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

ili sačuvajte svoju lozinku na papirnom medijumu (**upozorenje**: ovo nije dobro rešenje, ali je u redu ako je namenjeno kao privremeno rešenje).



Označite polje za verifikaciju gde izjavljujete da niste robot (polje C). Imajte na umu Nemojte omogućavati RSA enkripciju osim ako tačno znate šta je to i kako funkcioniše. Ne morate ništa da radite u ovoj fazi. Kliknite na "Generate Avatar" ("Generate Avatar") (polje D).



![image](assets/it/04.webp)



Sada morate platiti 1000 sats da biste završili upis.



1. Počevši od vrha, prvo pogledajte svoj nasumično generisani i izuzetno važan "Avatar ID." Sačuvajte ga pažljivo, baš kao što sam vam savetovao da uradite sa lozinkom.


2. Zatim morate uneti svoj "Lightning Address" u polje ispod. Ovo će vam omogućiti da primate uplate ako kupite Bitcoin, ili dobijete povraćaj novca. Ako koristite Wallet ili Satoshi moći ćete da kopirate svoj Address klikom na primanje.


3. Označite polje za verifikaciju gde izjavljujete da niste robot.


4. Napravite uplatu od 1000 sats da biste dobili pristup vašem ograničenom području. Ako ne možete da ga označite, kliknite na njega mišem (na PC-u) ili ga dodirnite prstom (na pretraživaču/Telegram pametnim telefonima) da kopirate adresu koju treba da nalepite u Wallet of Satoshi i završite plaćanje fakture.



![image](assets/it/05.webp)



Ovo je vaš LNURL Address.



![image](assets/it/06.webp)



Čestitamo!!! Trajno ste kreirali svoj Avatar i možete pogledati rezime ovde. Još jednom, preporučujem da pažljivo sačuvate i svoj Avatar i lozinku, kao što sam već predložio.



Kliknite `Sačuvao sam svoje kredencijale, nastavi`



![image](assets/it/07.webp)



Sada ste u srcu platforme, gde možete videti sve trgovinske podudarnosti sa njihovim detaljima. Za jasniji prikaz, ispod ćete videti slike svojstvene vebsajtu sa desktop računara.





- "Type" ("Type") definiše da li je u pitanju "Sell" ("sell") prodaja ili "buy" kupovina
- "Amount" ("Amount"): označava koliko sats korisnik prodaje ako je meč tipa "Sell", ili koliko Bitcoin korisnik želi da kupi ako je meč tipa "Buy".
- "Cena BTC sa Maržom" ("BTC Price with Margin"): prikazuje cenu uzimajući u obzir maržu primenjenu iznad označene vrednosti.
- "Margin" ("Margin") je procenat koji se primenjuje na tržišnu cenu, Sa minus znakom (-) dobijate popust na tržišnu cenu, Sa plus znakom (+) primenjuje se premija na tržišnu cenu.
- "Method" ("Method") označava kojim metodom korisnik preferira da bude plaćen.
- "Kreator" je jedinstveni avatar koji korisnik koristi na platformi.
- "Rep" (Reputacija) Nivo reputacije korisnika kreće se od -5 nepouzdan do +5 izuzetno pouzdan.
- "Status" ("Status"): označava status meča. U primeru snimka ekrana, svi mečevi izgledaju kao "Open" ("Open").
- "Isticanje" ("Isticanje"): pokazuje koliko je vremena preostalo pre nego što meč istekne i bude otkazan ako ga niko ne izabere.



![image](assets/it/08.webp)



U gornjem desnom uglu kliknite na svoj Avatar da biste pristupili svom profilu.



![image](assets/it/09.webp)



Ovde možete videti ime vašeg Avatara, Korisnički ID, datum kreiranja i reputaciju, što će se pozitivno ili negativno odraziti na vaše ponašanje u pregovorima.



![image](assets/it/10.webp)



U odeljku Podešavanja možete videti vaš "Lightning Address," unet tokom registracije, i promeniti ga ako je potrebno. Takođe imate opciju kreiranja Javnog Ključa, koji, kao što je pomenuto, treba postaviti samo ako imate odgovarajuće veštine. Koristi se za šifrovanje poruka koje ćete razmenjivati sa vašim sagovornikom direktno sa vašeg računara.



Funkcija obaveštenja Telegram se toplo preporučuje. Aktiviranjem će se pojaviti QR kod koji možete uokviriti pomoću aplikacije Telegram: na ovaj način ćete primati obaveštenja u realnom vremenu o svim akcijama vezanim za vaše mečeve, direktno u bot četu na Telegram.



![image](assets/it/11.webp)



Konačno, pronalazite svoj odeljak za preporuke, sa zaradom koju su generisali korisnici koje ste pozvali. Odavde možete koristiti dugme za deljenje vašeg linka ili QR koda i, malo niže, pregledati listu mečeva kako biste pratili svoju reputaciju zajedno sa odgovarajućim rezultatom.



![image](assets/it/12.webp)



## Kreiraj narudžbinu za kupovinu Bitcoin



Uđite na Marketplace: iz glavne navigacione trake, kliknite na simbol korpe "Marketplace"("Marketplace") da otvorite knjigu narudžbi. zatim započnite novu narudžbu: pritisnite dugme "New Order" ("New Order") da započnete proces.



![image](assets/it/13.webp)





- Postavite detalje narudžbine:
- Odaberite opciju "Buy Bitcoin"("Buy Bitcoin").
- Unesite količinu sats koju želite.
- Definišite cenovni margini (između -20% i +20% od tržišne vrednosti).
- Izaberite način plaćanja (Instant SEPA, itd.).
- Ukazuje preferiranu valutu.
- Potvrdite narudžbu: kliknite na "Kreiraj narudžbu"("Potvrdi narudžbu") da biste prešli na fazu podnošenja.



![image](assets/it/14.webp)



Depozit potreban: potreban je depozit jednak 10% od ukupnog iznosa, plus naknada za uslugu, kako bi se aktivirala narudžbina.




- Uplata depozita: kada se narudžbina kreira, sistem automatski generiše Lightning fakturu. Depozit je samo privremen i vraća se kada je narudžbina završena.
- Glavne karakteristike:
- Sigurnosni depozit: 10% od vrednosti porudžbine.
- Naknada za uslugu: trošak za korišćenje platforme.
- Vremensko ograničenje: Imate 5 minuta da izvršite uplatu, inače transakcija ističe.



![image](assets/it/15.webp)



Nakon uspešne uplate, narudžbina će se pojaviti u knjizi i biti vidljiva svim korisnicima, koji je mogu izabrati i prihvatiti. Da biste kreirali nalog za prodaju, sve što treba da uradite je da kliknete na "Sell Bitcoin" ("Sell Bitcoin"), unesete količinu satoshi koju želite da prodate, postavite maržu, izaberete način plaćanja i valutu, a zatim nastavite sa uplatom depozita od 10% kao sigurnosni depozit. Kada završite, vaš meč će biti vidljiv na listi.



![image](assets/it/16.webp)



## Kako prihvatiti narudžbinu



1. Prodavci mogu videti listu svih dostupnih narudžbina u knjizi.


2. Proverite detalje: svaka narudžbina prikazuje informacije kao što su:




  - Količina Bitcoin,
  - Marža na cenu,
  - Metod plaćanja,
  - Reputacija korisnika.



![image](assets/it/17.webp)



3. Kliknite na narudžbinu da otvorite ceo list sa svim informacijama.


4. Pritisnite "Sell Bitcoin"("Sell Bitcoin") da prihvatite predlog.



![image](assets/it/18.webp)



## Depozit koji zahteva prodavac



Kada je narudžbina prihvaćena, sistem generiše fakturu za plaćanje. Depozit uključuje:



- Ukupan iznos narudžbine,



- komisija za usluge.



Uplata depozita mora biti izvršena u okviru navedenog vremenskog ograničenja, inače transakcija neće biti potvrđena.



![image](assets/it/19.webp)



## Slanje uputstava za plaćanje



Nakon što je depozit izvršen, transakcija će se pojaviti na ličnom kontrolnom panelu prodavca, koji mora obezbediti detalje kupcu kako bi završio plaćanje u fiat valuti.



1. Prodavac prikazuje aktivnu transakciju u svom panelu.


2. Kliknite na "Submit Payment Instructions."


3. Unesite sve potrebne informacije za fiat uplatu (IBAN, primalac, adresa, svrha uplate, itd.).


4. Kliknite na "Send Message"("Send Message") da biste poslali podatke kupcu.



![image](assets/it/20.webp)



## Postupak plaćanja



Kupac prima, unutar platformskog četa, poruku sa svim potrebnim podacima za izvršenje plaćanja u fiat valuti:




- Podaci o banci: IBAN sa imenom i adresom vlasnika računa prodavca.
- Tačan iznos: tačan iznos fiat valute koji treba preneti.
- Uzrok/opis: tekst koji treba uključiti u transakciju.
- Rok plaćanja: krajnji rok do kojeg treba izvršiti uplatu.



Transfer se odvija izvan sistema P2P i mora se izvršiti putem bankarske institucije.



⚠️ **Važna napomena:** potvrda na platformi treba da se izvrši tek nakon što ste zaista organizovali transfer ili fiat uplatu putem vaše banke.



![image](assets/it/21.webp)



## Potvrda plaćanja fiat



Ovaj korak je ključan za kupca i treba ga obaviti tek nakon što se potvrdi da je uplata zaista poslana.



1. Primanje podataka: kupac je primio uputstva za plaćanje od prodavca.


2. Izvršenje plaćanja: fiat transfer se organizuje sa nečijeg bankovnog računa.


3. Verifikacija: proverite da li je operacija ispravno obrađena.


4. Potvrdite na platformi: kliknite na "Confirm fiat payment"("Confirm fiat payment") na stranici za trgovinu.


Dugme "Potvrdi uplatu fiat" pojavljuje se u odeljku za transakcije i treba ga koristiti samo nakon što se potvrdi da je uplata zaista poslata.



![image](assets/it/22.webp)



Poslednji korak u procesu je da prodavac potvrdi prijem fiat uplate, nakon čega se satoshi puštaju kupcu.



![image](assets/it/23.webp)



## Zaključak



U nadi da će vam ovaj vodič pomoći da koristite novu metodu za trgovinu Bitcoinima ili čak samo da ih kupite, bilo za sopstvenu vrednost ili da počnete sa svakodnevnim plaćanjima. Ipak, ostaje kao vrata za istraživanje kako bi se nosili sa onim što će se desiti u našem digitalnom svetu.



Omča koju vode tela koja nas kontrolišu se steže, kako bi se rodio sve kontrolisaniji Internet. Kupovinom P2P, vaše kupovine će ostati potpuno anonimne, ne ostavljajući tragove i bez posledica od strane trećih lica.