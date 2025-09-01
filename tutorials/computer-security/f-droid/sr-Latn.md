---
name: F-Cold
description: Katalog besplatnih i open-source aplikacija.
---

![cover](assets/cover.webp)



U digitalnom dobu, velike korporacije i institucije rade na tome da Internet učine centralizovanijim, stavljajući njegovu kontrolu u svoje ruke, čime ometaju privatnost i slobodu svih korisnika. Ovo nije utopija, već se već dešava. Kao bitkoiner, decentralizacija, poštovanje privatnosti i individualne slobode su principi koje cenite, posebno u alatima koje koristite svakodnevno. Android, za razliku od iOS-a, već godinama omogućava postojanje više prodavnica aplikacija unutar svog ekosistema, dajući vam slobodu da pronađete i instalirate aplikacije iz svojih omiljenih izvora.



U ovom vodiču ćemo pogledati F-droid, direktorijum aplikacija koji predstavlja alternativu prodavnicama aplikacija kao što su Google Play Store i Microsoft Store.



## Početak sa F-Droid



F-Droid je prodavnica aplikacija i alatki koja vam omogućava da instalirate besplatne, open-source aplikacije na Android platformi. F-Droid je sam po sebi open source projekat koji je započeo 2010. godine od strane Ciaran Gultnieks-a i nekoliko drugih saradnika. Glavni cilj projekta je da učini open source aplikacije dostupnim i da omogući pokretačima open source projekata da pronađu platformu na kojoj mogu objaviti svoje alatke bez potrebe da se oslanjaju na Google Play Store.



Nažalost, F-Droid nije aplikacija dostupna na iOS-u i sadrži mnoge alate dizajnirane za Android sisteme.



Možete preuzeti F-droid sa [zvanične veb stranice](https://f-droid.org/) u APK formatu i ručno ga instalirati na vaš Android telefon.



![download](assets/fr/02.webp)



Na Androidu, uverite se da ste dali dozvole za instalaciju za pregledač iz kojeg ste preuzeli F-Droid.



Kada je instalacija završena, F-Droid će pokrenuti ažuriranje direktorijuma aplikacija otvorenog koda kako bi obogatio aplikacije u prodavnici.



![repositories](assets/fr/03.webp)



Sada možete instalirati aplikacije na svoj telefon bez korišćenja Google Play Store-a.



## Knjizara F-Droid



U Prodavnici aplikacija, pronaći ćete nekoliko kategorija aplikacija koje odgovaraju vašim potrebama. Na kartici **Kategorije**, pronaći ćete preko 20 tipova aplikacija, od pregledača do besplatnih uređivača teksta, i sve zahtevaju najmanje informacija sa vaše strane.



Da li želite da instalirate određenu aplikaciju? Kliknite na dugme **Pretraga**, zatim unesite ime aplikacije koju tražite.



![search](assets/fr/04.webp)



F-Droid pruža sveobuhvatne informacije o svakoj aplikaciji koju želite instalirati.



Klikom na aplikaciju, između ostalog, pronaći ćete:




- Funkcije i promene dodate u najnovijoj dostupnoj verziji
- Detaljan opis aplikacije, njenih funkcija, razloga za korišćenje i Open Source zajednice koja stoji iza projekta.



![features](assets/fr/05.webp)





- Licenca koju koristi projekat, linkovi ka izvornom kodu i ka problemima na koje se nailazi prilikom korišćenja aplikacije
- Dozvole koje zahteva aplikacija



![permissions](assets/fr/06.webp)



Saznajte više u našem vodiču za Thunderbird:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid vam daje sve informacije koje su vam potrebne da odlučite da li korišćenje aplikacije štiti vaše podatke i poboljšava vašu privatnost. Skenirajte sve aplikacije koje želite da koristite, zatim kliknite na dugme **Install** da preuzmete i instalirate vašu aplikaciju.


Omogućite prava za instalaciju F-Droid aplikacije uključivanjem opcije u vašim podešavanjima.



![settings](assets/fr/07.webp)



## Exchange vaše aplikacije



F-Droid podstiče praksu otvorenog koda i doprinos zajednice, posebno putem svoje opcije **Near By** Exchange. Povežite se sa korisnicima oko vas putem:




- Otkrivanje Bluetooth-a;
- Ista Wi-Fi mreža;
- QR kod ili IP:PORT Address za unos u vaš pretraživač.



Sa ovom opcijom, možete deliti i primati aplikacije instalirane na vašem Android telefonu sa prijateljima i porodicom u samo nekoliko koraka.



![swap](assets/fr/08.webp)



## Ažuriranja



Na kartici **Update**, pogledajte listu dostupnih ažuriranja i obavezno pročitajte informacije o novim verzijama svake aplikacije kako biste saznali o svim većim promenama u verziji koju koristite.



![updates](assets/fr/09.webp)



Takođe možete ažurirati listu dostupnih aplikacija osvežavanjem stranice (skrolujte nadole).



## Dodajte svoje aplikacije



F-Droid je projekat otvorenog koda koji podstiče doprinose aplikacijama koje daju prioritet privatnosti korisnika. Možete dodati svoju Android mobilnu aplikaciju u prodavnicu putem doprinosa F-Droid GitLab izvornom kodu.



Vaša aplikacija mora biti otvorenog koda, sa izvornim kodom javno dostupnim na GitHub-u ili GitLab-u, na primer.


Morate zatim pripremiti YAML datoteku (metapodatke) koja opisuje vašu aplikaciju, uključujući sve informacije i dozvole potrebne za njeno korišćenje, prateći [šablon metapodataka](https://f-droid.org/docs/Build_Metadata_Reference/) koji predlaže F-Droid.



U odeljku **Developers** [dokumentacije](https://f-droid.org/en/docs/), pronaći ćete sve resurse potrebne za objavljivanje i održavanje vaših aplikacija na F-Droidu.



### Integritet i bezbednost



Stavljanje aplikacije u open source često je sinonim za povećanu sigurnost, ali i za značajan rizik. Kako možete osigurati da nema zlonamernih izmena u izvornom kodu aplikacije dostupne na F-Droidu?



F-Droid kompajlira aplikacije na sopstvenim serverima, na osnovu zvaničnog izvornog koda i uputstava za kompajliranje. Svaka objavljena aplikacija se ponovo gradi i verifikuje kako bi se osiguralo da nije kompromitovana. Ovo osigurava da je ponuđeni APK veran izvornom kodu koji su objavili programeri. Štaviše, svaka aplikacija instalirana putem F-Droid-a je digitalno potpisana, a zatim se otisak prsta potpisa upoređuje sa onim koji su objavili programeri aplikacije na zvaničnom sajtu ili na Git repozitorijumu.



Ako vam se dopao ovaj vodič, saznajte više o našem kursu IT bezbednosti i upravljanja podacima:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1