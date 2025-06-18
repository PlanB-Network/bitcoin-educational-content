---
name: BitcoinVoucherBot
description: Telegram bot za kupovinu Bitcoin u poverljivosti
---
![image](assets/cover.webp)


_Ovaj vodič je napisao_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


# Uvod


BitcoinVoucherBot je alat pomoću kojeg se Bitcoini mogu kupiti u Exchange za evre.


### KYC Light


Radnja zamene evra za Bitcoin je prvi i najosnovniji korak za početak proučavanja ove teme, ali je očigledno i najteži i najsloženiji. Može biti mnogo opcija: ponuda Bitcoin preko centralizovanih berzi, Bitcoin tematski susreti, prijatelji, poznanici i još mnogo toga. Pridružujemo se Bitcoiner zajednici i **apsolutno preporučujemo korišćenje centralizovanih berzi** kako bismo obezbedili veću pažnju prema nečijoj privatnosti.


Iako ovaj izbor može biti manje praktičan, važno je razumeti da berze sprovode regulativu "Upoznaj svog kupca" (KYC), čime dodeljuju identitet, kao i fizičku lokaciju, svakom Satoshi kupljenom od njih. "Praktičnost" ima neke upečatljive nuspojave.


### Kako to uraditi?


Evo dolazi [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot) usluga, Telegram bot koji deluje kao posrednik između naših SEPA transfera i Sats kupovina.


### Pre-requisites


Da biste počeli koristiti BitcoinVoucherBot, nije potrebno otkrivati osetljive lične informacije osoblju Bota. **Nije potrebna autorizacija**.


Sve što je potrebno je već aktivan Telegram nalog i bankovni račun. **Napomena**: Nalog otvoren kod Poste Italiane (za italijanske korisnike) ili, općenitije, koji se odnosi na dopunjivu karticu nije pogodan.


U Telegram četu pripremamo narudžbu, bankovnim transferom je plaćamo, i na kraju preko bota dobijamo vaučer izdat od strane treće kompanije koja ne zna predmet kupovine.


### Aktivacija bota i meni


Aktivacija je jednostavna jednokratna operacija. Na Telegramu, potražite _@BitcoinVoucherBot_ i čim dođete do četa sa Botom, veliki taster _Start/Start_ se ističe na dnu. Operacija uzrokuje da Bot odgovori, što prikazuje meni sa glavnim komandama koje su mu dostupne. Pojavljuju se i prve poruke dobrodošlice, za koje preporučujemo pažljivo čitanje.


**Upozorenje**: postoji nekoliko prevaranata koji se predstavljaju kao originalni VoucherBot. Ako niste sigurni u pretragu putem Telegrama, molimo vas da pristupite BitcoinVoucherBot linku sa [zvanične web stranice](https://www.bitcoinvoucherbot.com/)


![image](assets/it/01.webp)


Opcije se pojavljuju klikom na dugme _Menu_ u donjem levom uglu: možete kliknuti na reč koja odgovara komandi, ili upisati u polje za poruke kosu crtu `/` praćenu otkucanom komandom.


![image](assets/it/02.webp)


Glavne operacije uključuju:




- _/purchase_: je stvarna procedura kupovine. Kada je transakcija završena, QR kod automatski generiše bot i spreman je za iskorišćavanje.
- _/refill_: dostupno u trenutku pisanja ovog tutorijala, ali nećemo ga pokrivati jer-iz tehničkih razloga-ova opcija može biti uklonjena kasnije.
- _/swap_: otvara proceduru zamene, dostupnu ili putem praktičnog Telegram bota ili preko veba.
- _/ap_: plan akumulacije, koji vam omogućava da postavite **Plan Konstantne Akumulacije (CAP)**.
- _/lnaddress_: sa kojom se traži da povežemo sopstveni LN Address, za određenu proceduru koju ćemo videti kasnije.
- _/krediti_: da proverite koliko je kredita ostalo na generate vaučerima.
- _/myorders_: prikazuje narudžbine izvršene putem bota (**Upozorenje** sistem prati samo poslednjih 10 narudžbina, a ne celu istoriju).
- _/fees_: komanda za proveru mrežnih naknada. Da biste ih procenili, uvek je najbolje osloniti se na Mempool.space.
- _/support_: u slučaju potrebe, pojavljuju se kontakti za prijavu problema timu za podršku.


# Bitcoin procedura nabavke


## Priprema narudžbine


Kliknite _/purchase_ u komandnom meniju


![image](assets/it/03.webp)


Pojavljuje se niz prilika, ali mi biramo _BTC Vouchers_


![image](assets/it/04.webp)


BitcoinVoucherBot vam omogućava kupovinu Bitcoin onchain, Lightning i Liquid.


U ovoj fazi izaberite _Onchain & Lightning 🔗⚡️_


![image](assets/it/05.webp)


Ekran se brzo menja i VoucherBot predlaže apoene za kupovinu. Počinju od minimuma od €100.00 do €900.00.


U slučaju prve kupovine, nude se samo apoeni od 100,00 €, Onchain i Lightning. Da biste povećali poverljivost, predlažemo da izaberete _Lightning ⚡️_


![image](assets/it/06.webp)


VoucherBot nas obaveštava da je prvi izbor napravljen i da, kako bismo ga potvrdili, treba da izaberemo _Proceed_


![image](assets/it/07.webp)


Sada je stvar izbora načina plaćanja. Transfer se vrši bankovnim transferom **(prihvaćen samo SEPA)**. VoucherBot predlaže kao primaoca kompaniju koja nudi dva bankovna računa, jedan u U.K i drugi u Švajcarskoj. Švajcarska banka je izabrana za sprovođenje ovog tutorijala.


![image](assets/it/08.webp)


U ovom trenutku se od nas traži da unesemo naš IBAN, onaj sa kojeg će početi transfer ka odabranoj banci. Ove informacije čine slagalicu koja će omogućiti botu, tj. mašini, da sastavi neke informacije kako bi proces kupovine tekao bez potrebe za ljudskom intervencijom.


IBAN mora biti napisan u traci za poruke, proveren i poslat botu.


![image](assets/it/09.webp)


Kontrolna poruka se sada pojavljuje u ćaskanju sa VoucherBot-om.


Ako je sve ispravno, nastavite klikom na _Proceed_.


![image](assets/it/10.webp)


## Plaćanje


Nakon nekoliko trenutaka, potrebnih za obradu podataka, VoucherBot odgovara porukom koja sadrži sve detalje potrebne za završetak narudžbe. U zavisnosti od zahteva vaše banke, relevantne informacije su:




- `IBAN`, koji je neophodan za depozit, kao i primalac`ov Address;
- `iznos odabran` prethodno kroz cutoff, koji mora biti ispunjen da bi VoucherBot prepoznao narudžbinu kada uplata bude primljena;
- `Razlog plaćanja`, što je razlog plaćanja. **Mora biti kopirano i nalepeno bez uklanjanja ili dodavanja bilo čega u odgovarajuće polje vaše transakcije. Bilo koja "." ili "-" prisutna u razlogu plaćanja, može biti zamenjena `belim prostorom'**.
- jedinstveni `OrderID` za referencu prilikom traženja bilo kakve pomoći.


Zatim možete nastaviti sa plaćanjem, putem vaše aplikacije ili banke. Kada banka prihvati plaćanje, važno je zapamtiti da pritisnete _Notify payment_ u ćaskanju sa VoucherBot-om. Ova jednostavna operacija vas obaveštava da je uplata na putu.


![image](assets/it/11.webp)


VoucherBot odgovara porukom koja sadrži veoma važno upozorenje: **ne brišite razgovor**, barem dok ne primite vaučer, jer je to jedini način za rekonstrukciju narudžbine i njeno održavanje.


![image](assets/it/12.webp)


---
Molim vas, zabeležite:




- prihvataju se samo SEPA bankovni transferi;
- vremena čekanja su isključivo povezana s tim kako banke (koje ne rade 24/7/365 kao Bitcoin) obrađuju vaučer. Može potrajati od nekoliko sati do 3 radna dana da primite vaučer;
- za sve potrebe, Bitcoin VoucherBot ima odličnu [podršku](https://t.me/BitcoinVoucherGroup) na Telegramu.


---
## Iskupljenje


Čim uplata bude uspešna, Bitcoin VoucherBot šalje vaučer direktno u čet. Vaučer za brzu transakciju je u obliku QR koda, odštampan na narandžastoj pozadini.


![image](assets/it/31.webp)


Tu su svi podaci potrebni za unovčavanje:




- iznos u Sats, ekvivalentan onom poslatom putem bankovnog transfera, isključujući naknade za uslugu i mrežne naknade;
- referentni ID vaučera;
- datum do kojeg vaučer mora biti iskorišćen ili će sredstva biti izgubljena, tj. 25 dana nakon izdavanja.


Možete unovčiti vaučer tako što ćete uokviriti QR kod funkcijom skeniranja kompatibilnog Wallet Lightning Network, ili putem LNURL, koji je takođe prikazan ispod QR koda.


Za ovaj vodič koristili smo Wallet Od Satoshi, koristeći funkciju skeniranja aktiviranu pomoću _Send_ tastera.


![image](assets/it/32.webp)


Sa aktiviranom kamerom mobilnog telefona, uokvirite QR kod u ćaskanju, otvarajući Telegram sa računara.


![image](assets/it/34.webp)


Pre nego što nastavite, Wallet Od Satoshi sa ekrana za verifikaciju koji uključuje iznos, koji tačno odgovara iznosu navedenom na vaučeru i, kao opis, BitcoinVoucherBot. Da biste unovčili vaučer, jednostavno kliknite na _Receive_


![image](assets/it/35.webp)


Wallet Od Satoshi procesa za nekoliko trenutaka


![image](assets/it/36.webp)


i konačno kolekcija je prijavljena i odmah dostupna u Wallet bilansu.


**Wallet od Satoshi je skrbnički app: odmah nakon unovčavanja vaučera, preporučljivo je premestiti Sats na Wallet ne-skrbnički.**


![image](assets/it/37.webp)


### Kako unovčiti onchain vaučer


Kao što smo videli u pripremi narudžbine, VoucherBot omogućava da se Sats kupi direktno na lancu, uz izbor istoimenog vaučera.


**Napomena**: Priprema narudžbine i plaćanje se ne menjaju, uvek su isti. Ono što se menja je način na koji se onchain vaučer unovčava.


Nakon završetka narudžbine, izvršenja plaćanja, pritiskanja _Obavesti o uplati_ i čekanja tehničkog vremena banaka za prenos transfera, VoucherBot će odgovoriti slanjem vaučera direktno u čet.


Ovaj vaučer je takođe u obliku QR koda, ali glavna boja je kanarinac žuta i - što je najvažnije - u opisu je dobro objašnjeno da je to onchain vaučer, koji unovčavate direktno na vašem Wallet onchain i, da biste započeli proceduru unovčavanja, morate kliknuti na _Redeem on Telegram_. Onchain vaučer takođe sadrži informacije koje su već viđene za lightning vaučer:




- iznos u Sats, ekvivalentan onom poslatom putem bankovnog transfera, isključujući naknade za uslugu i mrežne naknade;
- kod vaučera;
- referentni ID vaučera;
- datum do kojeg vaučer mora biti iskorišćen ili će sredstva biti izgubljena, tj. 25 dana nakon izdavanja.


![image](assets/it/22.webp)


**UPOZORENJE ⚠️:** kliknuto kako je objašnjeno, otvara se iskačući prozor drugog bota: **Voucher RedeemBot.**


Voucher RedeemBot je alat napravljen za ovu svrhu. Bilo da je ovo prva upotreba ili postoje prethodne narudžbine, svaki put kada se izvrši novo iskorišćavanje, uvek je potrebno kliknuti na _START_.


![image](assets/it/23.webp)


U ovom trenutku RedeemBot učitava onchain vaučer, lako prepoznatljiv po kodu vaučera i referentnom ID-u. Takođe otključava traku za pisanje poruka i započinjanje ćaskanja sa botom, koji nas zapravo poziva da mu kažemo onchain Address našeg Wallet.


**Napomena**: Ovaj Address mora biti tipa SegWit.


![image](assets/it/24.webp)


Otvaramo naš Wallet u ovom trenutku i generate a SegWit Address


![image](assets/it/25.webp)


kopiramo to


![image](assets/it/26.webp)


i nalepite ga u ćaskanje sa RedeemBot


![image](assets/it/27.webp)


Sada imamo ekran za proveru, da potvrdimo da je kod vaučera tačan, kao i Address koji smo preneli RedeemBot-u. Hajde da ga dobro proverimo jer, klikom na _Proceed_, transakcija počinje i neće biti načina da je ponovo pronađemo ako smo, na primer, preneli pogrešan Address.


![image](assets/it/28.webp)


Transakcija je započeta i Redeem procedura onchain vaučera se time završava.


![image](assets/it/29.webp)


dok se iznos može videti u istoriji našeg Wallet.


![image](assets/it/30.webp)