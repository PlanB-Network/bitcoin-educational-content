---
name: Session
description: Šalji šifrovane poruke, ne metapodatke
---
![cover](assets/cover.webp)



Session je aplikacija za šifrovano dopisivanje kreirana 2020. godine, dizajnirana da ponudi viši nivo poverljivosti od tradicionalnog dopisivanja. Prvo ju je razvila *Oxen Privacy Tech Foundation*, a zatim *Session Technology Foundation*.



Session se može pohvaliti nekim zanimljivim tehničkim karakteristikama: end-to-end enkripcija poruka, decentralizovana mreža organizovana da garantuje dostupnost i redundanciju (otpornost na otkaz), i Tor-inspirisano onion rutiranje. Takođe, za razliku od WhatsApp-a ili Signala, koji zahtevaju telefonski broj za registraciju, Session ne traži nikakve lične informacije (nema broja, nema email-a, samo par kriptografskih ključeva).



Session vam omogućava slanje poruka, datoteka, glasovnih poruka, audio poziva, kao i grupu do 100 članova (i zajednicu izvan toga), uz minimiziranje curenja metapodataka.



![Image](assets/fr/01.webp)



Session je namenjena pre svega korisnicima koji poverljivost stavljaju u srž svojih prioriteta. Ova usluga za razmenu poruka predstavlja ozbiljnu alternativu WhatsApp-u, sa arhitekturom dizajniranom da izdrži moderne modele nadzora.



| Aplikacija          | E2EE 1:1       | E2EE grupe   | Anonimna prijava | Licenca klienta otvorenog koda | Licenca servera otvorenog koda | Decentralizovni server | Godina kreiranja |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opciono) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (opciono) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (federacija)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (putem mejla)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (federacija)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(nema imenika)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Šifrovanje od kraja do kraja*



## Instalirajte Session aplikaciju



Session je dostupna na svim platformama. Možete preuzeti aplikaciju direktno iz prodavnice aplikacija na vašem telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



Na Androidu je takođe moguće [instalirati putem APK-a](https://github.com/session-foundation/session-android/releases).



U ovom vodiču ćemo se fokusirati na mobilnu verziju, ali imajte na umu da su [verzije za računare takođe dostupne](https://getsession.org/download) (MacOS, Linux i Windows). Kasnije ćemo pogledati kako da sinhronizujete nalog na više uređaja.



## Kreiraj Session nalog



Prilikom prvog pokretanja, kliknite na "Create account" kako biste kreirali nalog.



![Image](assets/fr/02.webp)



Izaberite ime za prikaz na svom profilu. Ovo može biti pseudonim ili vaše pravo ime.



![Image](assets/fr/03.webp)



Zatim ćete morati da izaberete između dva režima upravljanja obaveštenjima:





- **Brzi režim ("*Firebase Cloud Messaging/Apple Push Notification Service*")**: omogućava vam da primate obaveštenja o porukama u gotovo realnom vremenu, zahvaljujući uslugama obaveštavanja koje pružaju Google ili Apple (u zavisnosti od vašeg sistema). Da bi ovo funkcionisalo, vaš IP Address i jedinstveni ID obaveštenja se prenose Google-u ili Apple-u, a ID sesije naloga se takođe registruje na STF serveru (preko Tor-a). Ovaj režim uključuje (priznato minimalno) izlaganje metapodataka, ali ne ugrožava sadržaj poruka ili kontakte, i ne omogućava praćenje vaše stvarne aktivnosti. Ovaj režim je stoga efikasniji u smislu odziva, ali se oslanja na centralizovanu infrastrukturu i nešto je manje efikasan u pogledu poverljivosti.





- **Spori režim (*background polling*)**: aplikacija Session ostaje aktivna u pozadini, periodično proveravajući mrežu za nove poruke. Ovaj pristup garantuje veću poverljivost od prvog, jer se podaci ne prenose na servere trećih strana; ni Google, ni Apple, ni STF serveri ne primaju nikakve informacije. S druge strane, ovaj režim ima dva nedostatka: obaveštenja mogu biti odložena (do nekoliko minuta), a potrošnja energije je generalno veća zbog aktivnosti aplikacije u pozadini.



![Image](assets/fr/04.webp)



Sada ste povezani sa aplikacijom Session i možete početi razmenjivati poruke.



![Image](assets/fr/05.webp)



## Sačuvaj svoj Session nalog



Prva stvar koju treba da uradite pre nego što počnete da koristite Session je da sačuvate svoj nalog kako biste mogli da ga povratite ako izgubite uređaj. Da biste to uradili, kliknite na dugme "Continue" pored "*Save your recovery password*".



![Image](assets/fr/06.webp)



Session će zatim prikazati mnemonic frazu. Pažljivo je kopirajte i čuvajte na sigurnom mestu. Ova fraza omogućava potpuni pristup vašem Session nalogu, tako da je važno da je ne otkrivate. Biće vam potrebna za pristup vašem nalogu na drugom uređaju, posebno ako vaš trenutni telefon bude izgubljen ili zamenjen.



![Image](assets/fr/07.webp)



Ova fraza funkcioniše na sličan način kao mnemonic fraze korišćene u Bitcoin novčanicima. Stoga preporučujem da pogledate ovaj drugi vodič, u kojem objašnjavam najbolje prakse za čuvanje mnemonic fraze:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Imajte na umu**: Za razliku od mnemonic fraza korišćenih u Bitcoin novčanicima, na Session, **apsolutno morate sačuvati svaku reč u celosti**. Prva 4 slova nisu dovoljna!



## Postavljanje Session aplikacije 



Da biste pristupili postavkama aplikacije, kliknite na svoju profilnu fotografiju u gornjem levom uglu interfesja. Ovde možete dodati profilnu fotografiju.



![Image](assets/fr/08.webp)



U meniju "*Privacy*", možete omogućiti ili onemogućiti različite funkcije (pazite, neke mogu otkriti vašu IP adresu). Takođe preporučujem aktiviranje opcije "*Lock App*", koja zahteva autentifikaciju za pristup aplikaciji.



![Image](assets/fr/09.webp)



U meniju "*Notification*" pronaći ćete izbor između "*Fast Mode*" i "*Slow Mode*" (pogledajte prethodne delove tutorijala). Takođe možete prilagoditi obaveštenja prema svojim preferencijama.



![Image](assets/fr/10.webp)



Na kraju, idite na meni "*Appearance*" da prilagodite interfejs prema svom ukusu. Meni "*Recovery Password*" vam omogućava da povratite vašu mnemonic frazu ako želite da napravite novu rezervnu kopiju.



![Image](assets/fr/11.webp)



## Slanje poruka sa Session-a



Da biste kontaktirali druge osobe, kliknite na dugme "*+*" na početnoj stranici.



![Image](assets/fr/12.webp)



Dostupno je nekoliko opcija. Ako želite da kreirate ili se pridružite grupi, izaberite "*Create Group*" ili "*Join Community*".



![Image](assets/fr/13.webp)



Ako želite da vas neko doda kao kontakt, možete im dati da skeniraju vaš Session ID kao QR kod.



![Image](assets/fr/14.webp)



Da biste poslali svoju prijavu na daljinu, kliknite na "*Invite a Friend*". Zatim možete kopirati svoj ID sesije i poslati ga putem drugog komunikacionog kanala. Ove informacije možete takođe preuzeti klikom na svoju profilnu fotografiju sa početne stranice.



![Image](assets/fr/15.webp)



Ako imate ID sesije druge osobe i želite da ga dodate, kliknite na "*New Message*".



![Image](assets/fr/16.webp)



Zatim možete nalepiti njegov identifikator u tekst, ili ga direktno skenirati ako ga imate kao QR kod.



![Image](assets/fr/17.webp)



Zatim pošaljite početnu poruku ovoj osobi.



![Image](assets/fr/18.webp)



Čim osoba prihvati vaš zahtev, videćete njeno korisničko ime i moći ćete slobodno da ćaskate s njom.



![Image](assets/fr/19.webp)



## Sinhronizuj desktop softver



Da biste sinhronizovali svoj nalog na računaru, potrebno je da instalirate softver. [Preuzmite ga sa zvaničnog sajta](https://getsession.org/download). Savetujem vam da proverite njegovu autentičnost i integritet pre instalacije.



![Image](assets/fr/20.webp)



Prilikom prvog pokretanja, kliknite na "*I have an account*".



![Image](assets/fr/21.webp)



Unesite svoju mnemonic frazu, pazeći da ostavite razmak između svake reči.



![Image](assets/fr/22.webp)



Sada možete pristupiti svojim razgovorima sa svog računara.



![Image](assets/fr/23.webp)



Čestitamo, sada ste savladali korišćenje Session poruka, odlične alternative za WathsApp!



Preporučujem i ovaj drugi vodič, u kojem predstavljam Threema, još jednu zanimljivu alternativu za vašu aplikaciju za razmenu poruka:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74
