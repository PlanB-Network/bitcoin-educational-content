---
name: Tiankii
description: Lightning suite alata za trgovce i potrošače
---

![cover](assets/cover.webp)



U ekosistemu Bitcoin, prihvatanje plaćanja u realnom vremenu ostaje veliki izazov za preduzeća i pojedince. Tradicionalna rešenja često zahtevaju napredno tehničko znanje, složenu infrastrukturu za održavanje ili zahtevaju da sredstva budu zadržana kod posrednika. Ova situacija koči masovno usvajanje Bitcoin kao svakodnevne valute, uprkos obećanju tehnoloških napredaka Lightning Network.



Tiankii, salvadorska kompanija osnovana 2021. godine, odgovara na ovaj problem nudeći pristupačnu, modularnu Bitcoin infrastrukturu. Umesto da forsira usvajanje zatvorenog ekosistema, Tiankii nudi paket međusobno povezanih alata koji omogućavaju svakome da integriše Bitcoin Lightning u svoje poslovanje bez žrtvovanja kontrole nad svojim sredstvima.



## Šta je Tiankii?



### Poreklo i filozofija



Tiankii - nahuatl termin koji znači "pijaca na otvorenom dostupna svima" - je prvi 100% Bitcoin startap u El Salvadoru. Osnovao ga je Darvin Otero nakon usvajanja Bitcoin kao zakonskog sredstva plaćanja u zemlji, a cilj kompanije je transformisati Bitcoin iz sredstva čuvanja vrednosti u valutu za svakodnevne transakcije. Za razliku od kustodijalnih platformi, Tiankii usvaja nekustodijalni pristup gde korisnici zadržavaju kontrolu nad svojim sredstvima, dok infrastruktura služi samo kao tehnički posrednik.



### Tehnička arhitektura



Tiankii je pozicioniran kao pružalac Bitcoin-kao-usluga infrastrukture zasnovane na Lightning Network. Ova tehnologija drugog sloja omogućava gotovo trenutne transakcije sa zanemarljivim troškovima, čineći mikrouplate i svakodnevne kupovine mogućim.



Arhitektura se zasniva na tri stuba:



**Lightning-first**: Sistematski favorizujte Lightning mrežu zbog njene brzine i nižih troškova, uz zadržavanje podrške za on-chain transakcije za velike iznose.



**Otvoreni standardi**: Korišćenje LNURL za automatizaciju zahteva za plaćanje, Lightning Address za čitljive email ID-ove, i Bolt Kartica za interoperabilna NFC plaćanja.



**wallet-agnostic modularity**: Mogućnost povezivanja različitih Lightning portfolija (LNbits, Blink, BlueWallet) ili sopstvenog čvora, nudeći maksimalnu fleksibilnost u zavisnosti od nivoa stručnosti i autonomije koji su potrebni.



## Tiankii ekosystem alati



### Bitcoin POS - Terminal za plaćanje u prodavnici



Aplikacija pretvara pametni telefon ili tablet u Lightning terminal. Trgovac unosi iznos u lokalnoj valuti, a aplikacija generiše Lightning QR kod ili prihvata Bolt karticu. Transakcije se odmah pripisuju bez provizije, sa automatskim konverzijama u preko 150 valuta, upravljanjem napojnicama i istorijom prodaje.



### Merchant Dashboard - Ujedinjeno upravljanje prodajom



Interface web centralizovan za povezivanje sa svojim wallet Lightning, praćenje transakcija u realnom vremenu, izdavanje faktura i generate računovodstvenih izveštaja. Platforma agregira sve kanale: plaćanja u prodavnici (POS), online prodaju (e-commerce plug-ins), ili API integracije. Plaćanja se konvergiraju na odabrani wallet.



### Bitcoin Beskontaktna Kartica (Bolt Kartica)



NFC Bolt kartica predstavlja glavnu inovaciju Tiankii-ja u demokratizaciji Bitcoin za širu javnost. Funkcioniše kao beskontaktna bankovna kartica, omogućavajući vam da plaćate Bitcoin Lightning kupovine jednostavnim prislanjanjem na kompatibilni terminal.



Za razliku od tradicionalnih kustodijalnih rešenja, ova kartica prati otvoreni standard koji garantuje interoperabilnost. Korisnici je mogu povezati sa svojim wallet putem IBI aplikacije, čime zadržavaju svoje privatne ključeve i potpunu kontrolu nad povezanim sredstvima. Plaćanje traje samo sekundu, bez potrebe da vadite svoj pametni telefon ili imate aktivnu internet konekciju u trenutku plaćanja.



Ovo rešenje je posebno inkluzivno za ljude koji nisu upoznati sa pametnim telefonima, nudeći pristupačan ulaz u Bitcoin ekonomiju.



### IBI App - Interface individualni Bitcoin



IBI aplikacija (Individual Bitcoin Interface) je dizajnirana za pojedince koji žele koristiti Bitcoin Lightning na dnevnoj bazi. Njena glavna prednost leži u generisanju personalizovanog Address Lightning-a, identifikatora plaćanja čitljivog u formatu email-a (primer: alice@ibi.me).



Ovaj identifikator drastično pojednostavljuje primanje uplata: nema potrebe za generate novim računom za svaku transakciju, pošiljalac može jednostavno uneti Lightning adresu. Interfejs vam takođe omogućava upravljanje vašom Bolt karticom (aktivacija, deaktivacija, limiti potrošnje), povezivanje različitih Lightning novčanika i vršenje uplata skeniranjem QR kodova.



### E-commerce dodaci



Integracije spremne za korišćenje za WooCommerce, Shopify i Cloudbeds. Instalira se za nekoliko minuta kako bi se dodao Bitcoin Lightning na naplatu. Prednosti: nulta provizija (naspram 2-3% kreditnih kartica), trenutno poravnanje, pristup širom sveta, eliminacija povraćaja sredstava. Uplate stižu direktno na wallet povezan sa trgovcem.



### Bitcoin API i alati za programere



Tiankii SDK omogućava integraciju Bitcoin Lightning u postojeće aplikacije bez održavanja sopstvenog čvora. API upravlja kreiranjem faktura, verifikacijom plaćanja i masovnim slanjem putem robusne infrastrukture hostovane na Google Cloud-u. Command Center upotpunjuje ponudu za organizacije sa Address Lightning na prilagođenim domenima, masovnim plaćanjima i centralizovanim upravljanjem NFC terminalima i karticama.



## Instalacija i prvi koraci



### Osnovni preduslovi



Korišćenje Tiankii ne zahteva složene tehničke preduslove. Aplikacije funkcionišu putem veb pregledača na pametnom telefonu, tabletu ili računaru. Nije potrebna instalacija izvorne aplikacije: sve što vam treba je pristup internetu i noviji pregledač za pristup IBI ili Merchant Dashboard-u.



**For private users (IBI App)**: Nije potreban prethodni wallet Lightning. Kada kreirate svoj nalog, Tiankii automatski konfiguriše radni Address Lightning putem [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), implementacije bez čvorova koja koristi Liquid mrežu u pozadini. Možete odmah primati i slati uplate bez ikakve tehničke konfiguracije. Ovo rešenje drastično pojednostavljuje pristup za početnike, dok ostaje samostalno čuvanje.



**Za trgovce (Kontrolna tabla trgovca)** : Povezivanje postojećeg wallet Lightning je obavezno za korišćenje terminala za prodajna mesta i primanje uplata. Tiankii podržava mnoga rešenja: mobilne novčanike (Blink, Strike), samostalno hostovana rešenja (LNbits, LND/CLN čvor), ili veb novčanike (Alby). Detaljni vodiči za povezivanje su dostupni u odeljku Resursi ovog tutorijala.



### Za privatne korisnike: IBI Aplikacija



**Kreiranje naloga



Idite na accounts.ibi.me da kreirate svoj nalog. Na ovoj stranici možete izabrati između dve vrste naloga: "Personal Use" za ličnu upotrebu, ili "Business Use" za komercijalnu upotrebu. Izaberite "Personal Use" da biste pristupili alatima za primanje i slanje uplata u Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Nakon što odaberete "Personal Use", automatski ćete biti preusmereni na go.ibi.me da dovršite registraciju. Ovo se može uraditi putem email-a, broja telefona, ili korišćenjem vašeg Google, Microsoft ili Twitter naloga. Kada kreirate nalog, možete odmah pristupiti vašem IBI interfejsu, sa vašim Lightning Address koji je već operativan.



![Création du compte](assets/fr/02.webp)



**Interface glavni**



IBI interfejs prikazuje vaš saldo u satoshijima i lokalnoj valuti (USD). Tri dugmeta omogućavaju interakciju: "Primite" za primanje uplata, "Skenirajte" za skeniranje QR koda i "Pošaljite" za slanje satoshija.



![Interface IBI](assets/fr/03.webp)



**Primite uplatu**



Da biste primili satoshije, pritisnite "Receive". Aplikacija automatski generiše QR kod i prikazuje vašu personalizovanu Address Lightning (nom@ibi.me format). Podelite ovu adresu ili QR kod sa pošiljaocem: sredstva stižu trenutno na vaš IBI račun.



![Réception avec Lightning Address](assets/fr/04.webp)



Kada vaš saldo bude uplaćen, možete koristiti ove satoshije za plaćanja.



**Pošalji uplatu**



Da biste poslali satoshi, pritisnite "Pošalji". Možete ili skenirati Lightning QR kod, ili direktno uneti Lightning Address odredište.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Unesite željeni iznos u satoshijima, proverite ekvivalentni iznos u lokalnoj valuti, zatim potvrdite plaćanje.



![Confirmation du montant](assets/fr/07.webp)



Obaveštenje o uspehu potvrđuje pošiljku sa detaljima: poslata količina, naknada za transakciju i primalac.



![Paiement réussi](assets/fr/08.webp)



**Upravljanje nalogom



U Podešavanjima možete upravljati svojim Bitcoin NFC karticama (Bolt Kartice). Interfejs vam omogućava da aktivirate, deaktivirate ili postavite limite potrošnje za vaše kartice.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Za trgovce: Merchantska kontrolna tabla i POS



**Kreiranje poslovnog naloga



Idite na accounts.ibi.me da kreirate svoj nalog. Izaberite "Poslovna upotreba" da biste pristupili alatima za trgovce. Ovaj tip naloga otključava pristup Merchantskoj kontrolnoj tabli i prodajnim terminalima.



Nakon što odaberete "Business Use", automatski ćete biti preusmereni na Merchant Dashboard (pay.tiankii.com). Ovo vas vodi do interfejsa za upravljanje poslovanjem sa praćenjem prihoda, transakcijama i alatima za plaćanje. Da biste počeli da prihvatate uplate, prvo morate povezati svoj wallet Lightning klikom na link na vrhu stranice (pogledajte strelicu na slici).



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning** konekcija



Ključni korak u aktiviranju vašeg prodajnog mesta: povežite vaš wallet Lightning da biste primali uplate. Interfejs nudi nekoliko opcija povezivanja. Imajte na umu da su neke opcije (Bitcoin Onchain i Lightning Network) još u razvoju i prikazane su sivom bojom na interfejsu.



![Options de connexion wallet](assets/fr/12.webp)



Za ovaj vodič koristimo Lightning Address konekciju, kompatibilnu sa Chivo, Blink Wallet i Strike. Unesite vaš Lightning Address (nom@domaine.com format), na primer od LN Markets, Alby, ili bilo kog drugog kompatibilnog dobavljača.



![Saisie de la Lightning Address](assets/fr/13.webp)



Kada se prijavite, vaš nalog je operativan. Sada možete pristupiti POS-u ili se vratiti na kontrolnu tablu da konfigurišete druga podešavanja.



![Connexion réussie](assets/fr/14.webp)



*payment Links** *Payment Links



Meni "Payment Tools" omogućava pristup "Payment Request", koji vam omogućava kreiranje i upravljanje linkovima za plaćanje. Ova funkcija je korisna za generisanje personalizovanih linkova za plaćanje koji se šalju putem emaila ili poruke: donacije, pojedinačna plaćanja, višestruka plaćanja, ili čak paywalls za zaštitu sadržaja. Možete kreirati različite tipove linkova koji odgovaraju potrebama vašeg poslovanja.



![Liens de paiement](assets/fr/15.webp)



**Konfiguracija prodajnog terminala**



Da biste prihvatili plaćanja u prodavnici, pristupite meniju "Prodajni terminal" iz "Alati za plaćanje". Ovaj odeljak vam omogućava da kreirate i upravljate vašim POS terminalima (broj terminala zavisi od vašeg plana, pogledajte Freemium vs. Poslovni planovi ispod). Kliknite na "Otvori" da biste otvorili POS interfejs u vašem pregledaču.



![Gestion des terminaux](assets/fr/16.webp)




**Generisanje prodaje**



POS terminal prikazuje numeričku tastaturu za unos iznosa prodaje. Unesite iznos u lokalnoj valuti (npr. 500 sats odgovara 630.74 ARS), zatim pritisnite "OK" za potvrdu.



![Saisie du montant](assets/fr/17.webp)



Aplikacija trenutno generiše Lightning QR kod i Lightning Address za plaćanje. Kupci mogu skenirati QR kod sa svojim wallet ili koristiti svoju Bolt karticu na NFC terminalu.



![QR code de paiement](assets/fr/18.webp)



Čim uplata bude primljena, pojavljuje se ekran za potvrdu, prikazujući iznos primljen u lokalnoj valuti i satoshijima. Možete poslati račun putem e-pošte, odštampati tiket ili odmah započeti novu prodaju.



![Paiement encaissé](assets/fr/19.webp)



**Praćenje i upravljanje**



Sve transakcije su zabeležene na vašoj Merchantskoj Kontrolnoj Tabli. Imate potpunu evidenciju prihoda po periodu, ukupan broj prodaja i detaljnu istoriju za vaše knjigovodstvo.



Interfejs podešavanja nudi nekoliko kartica za konfiguraciju. Kartica "Opšta podešavanja" omogućava vam upravljanje profilom trgovca i obaveštenjima. Kartica "Korisnici" omogućava vam dodavanje i upravljanje pristupom Merchant Dashboard-u za vaš tim (upravljanje više korisnika u skladu sa vašim planom). Kartica "Razvojni prostor" daje pristup API ključevima za napredne integracije, dok "Pretplata" omogućava upravljanje vašom pretplatom.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs Business planovi



Tiankii nudi dva paketa za Merchant Dashboard. **Freemium** plan (besplatan) je pogodan za start-up kompanije sa ograničenjima: jedna prodajna tačka, jedan korisnik, mesečni obim ograničen na 1.000 USD i bez pristupa e-commerce konektorima. **Business** plan (0,5% naknada po transakciji) nudi neograničene terminale, neograničene korisnike, neograničen obim, pristup WooCommerce/Shopify/Cloudbeds pluginovima i ekskluzivne WhatsApp notifikacije.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Prednosti i ograničenja



### Istaknuto



**Samostalno čuvanje**: Vi čuvate svoje privatne ključeve i imate potpunu kontrolu nad svojim sredstvima. Nema rizika od zamrzavanja računa ili bankrota platforme treće strane.



**Jednostavnost**: Lightning Address kao email adresa, NFC plaćanja jednostavnim dodirom, intuitivan interfejs bez potrebe za tehničkim znanjem.



**Kompletan ekosistem**: Alati za sve profile (pojedince, trgovce, programere) sa modularnim integracijama koje odgovaraju vašim potrebama.



**Profesionalna usklađenost**: Sigurno hostovanje u oblaku, PCI-DSS usklađenost, usklađenost sa salvadorskim propisima.



### Ograničenja



**Ograničenja munje**: Zahteva stalnu wallet vezu, upravljanje likvidnošću za velike količine, rizik od neuspeha ako primalac nije na mreži. Tiankii ublažava ove aspekte sa integrisanim LSP-ovima.



**SaaS zavisnost**: Ako Tiankii nije dostupan, generisanje faktura je privremeno nemoguće (vaša sredstva ostaju sigurna).



**Privatnost**: Tiankii može posmatrati metapodatke transakcija (iznosi, datumi). Manje privatno od rešenja koje se samostalno hostuje, kao što je BTCPay Server.



## Zaključak



Tiankii ilustruje kako dobro dizajnirana infrastruktura može ukloniti tehničke prepreke koje sprečavaju masovno usvajanje Bitcoin kao svakodnevne valute. Kombinovanjem snage Lightning Network sa nekustodijalnim pristupom i pristupačnim alatima, ekosistem nudi uravnotežen put između finansijskog suvereniteta i jednostavnosti korišćenja.



Za trgovce, Tiankii predstavlja priliku da drastično smanje troškove transakcija dok pristupaju novoj bazi kupaca. Za potrošače, Lightning Address i NFC kartice transformišu Bitcoin u praktičnu valutu, bez tehničke složenosti.



Iako široko prihvatanje Bitcoin ostaje izazov koji zahteva edukaciju i vreme, infrastrukture kao što je Tiankii pokazuju da tehnički alati već postoje. Misija pojednostavljenja plaćanja putem Bitcoin više nije daleka vizija, već stvarnost dostupna svakome ko je spreman da se upusti u to.



## Resursi



### Zvanična dokumentacija




- [Zvanična veb stranica Tiankii](https://tiankii.com)
- [Tiankii Help Center](https://help.tiankii.com)
- [IBI aplikacija](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Komandni Centar](https://cc.ibi.me)



### Vodiči za povezivanje Wallet




- [Poveži LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Poveži BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Poveži Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Poveži Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Zajednica




- [Lightning Network Plus](https://lightningnetwork.plus) - Edukativni resurs za Lightning
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvadorijanska inicijativa za kružnu ekonomiju Bitcoin



### Povezani alati




- [Blink Wallet](https://blink.sv) - Preporučena kompatibilnost sa Wallet Lightning
- [LNbits](https://lnbits.com) - Samohostovano wallet rešenje
- [Standard Bolt Card](https://github.com/boltcard) - Tehničke specifikacije za NFC kartice