---
name: Zeus Swap
description: Nekustodijalna Exchange usluga između On-Chain i Lightning Network bitkoina
---

![cover](assets/cover.webp)



Bitcoin ekosistem predstavlja dualnost: glavna mreža (On-Chain) nudi maksimalnu sigurnost, dok Lightning Network omogućava trenutne transakcije. Ova dvoslojna Layer arhitektura stvara praktičan izazov: kako sredstva mogu biti efikasno preneta između ova dva sloja bez centralizovanih posrednika?



Problem je konkretan: primate Lightning uplatu, ali želite da je zadržite u Cold skladištu, ili obrnuto, imate On-Chain bitkoine, ali vam je potrebna Lightning likvidnost. Tradicionalna rešenja uključuju ručno otvaranje/zatvaranje Lightning kanala (skupo i tehnički zahtevno) ili centralizovane platforme koje zahtevaju KYC.



Zeus Swap rešava ovaj problem automatizovanom, nekustodijalnom Exchange uslugom. Razvijen od strane Zeus LSP, omogućava vam da konvertujete On-Chain bitkoine u Lightning satoshije dvosmerno, bez poveravanja vaših sredstava posredniku. Proces koristi atomske ugovore (HTLC) koji garantuju da će se Exchange ili završiti ili otkazati.



Inovacija leži u njenoj jednostavnosti: samo nekoliko klikova za Exchange koji čuva vaš finansijski suverenitet, bez registracije ili KYC-a.



## Šta je Zeus Swap?



Zeus Swap je usluga likvidnosti Exchange koju je razvio Zeus LSP i omogućava atomske zamene između glavne Bitcoin mreže i Lightning Network. To je tehnička infrastruktura koja koristi podmorske zamene i obrnute zamene kako bi olakšala dvosmernu konverziju između On-Chain BTC i Lightning satoshija, uz očuvanje ne-kustodijalne prirode operacije.



### Tehnička arhitektura



Zeus Swap koristi Boltzovu open-source Bitcoin/Lightning tehnologiju za atomske zamene. Protokol koristi Hash vremenski zaključane ugovore (HTLC): ugovore koji zaključavaju sredstva sa dva uslova za oslobađanje (otkrivanje kriptografskog tajnog ključa ili isteka vremena).



Za zamenu podmornice (On-Chain → Lightning), korisnik šalje bitkoine na Address koji uključuje Hash Lightning Invoice. Zeus LSP otključava ova sredstva samo plaćanjem odgovarajućeg Invoice, otkrivajući pre-image koji automatski otključava bitkoine. Ovaj mehanizam garantuje atomarnost.



Za reverzni swap (Lightning → On-Chain), korisnik plaća Lightning Invoice od Zeus LSP, otkrivajući pre-image koji omogućava oslobađanje pripremljene Bitcoin transakcije do odredišta Address.



Za više detalja o tome kako Lightning Network funkcioniše, pogledajte naš posvećeni kurs :



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Poslovni model



Zeus LSP deluje kao market maker, održavajući On-Chain i Lightning likvidnost kako bi ispoštovao zamene. Za zamene, Zeus primenjuje varijabilnu naknadu (obično od 0.1% do 0.5% u zavisnosti od smera i uslova) plus Bitcoin-ovu Mining naknadu, transparentno prikazanu pre validacije.



Kao provajder Lightning usluga, Zeus optimizuje troškove zahvaljujući svom stručnom znanju u otvaranju kanala na zahtev, efikasnom rutiranju i prilagođenim rešenjima za likvidnost.



### Integracija



Zeus Wallet nativno integriše uslugu, omogućavajući zamene bez napuštanja Interface Bitcoin/Lightning. Ovo eliminiše trenje kopiranja i lepljenja između aplikacija.



Nezavisni Interface web ostaje dostupan svim novčanicima, garantujući maksimalnu fleksibilnost korišćenja.



## Glavne karakteristike



### Dvosmerne zamene



Zeus Swap nudi dve vrste Exchange:



**Zamene podmornica (On-Chain → Lightning)**: ubrizgajte Lightning likvidnost iz vaših Bitcoin rezervi, korisno za napajanje mobilnog Wallet ili Lightning čvora bez ručnog otvaranja kanala.



**Obrnuti swapovi (Lightning → On-Chain)**: konvertujte Lightning satoshije u On-Chain bitkoine za dugoročno skladištenje, izbegavajući skupe zatvaranja kanala.



### Korisnički interfejsi



**Interface web** (swaps.zeuslsp.com): pojednostavljeno iskustvo bez registracije, vođeni proces sa prikazom naknada i statusa u realnom vremenu.



**Zeus Wallet integracija**: direktne zamene iz aplikacije, automatsko upravljanje fakturama i adresama, eliminisanje grešaka u rukovanju.



### Sigurnost i oporavak



Svaka zamena generiše jedinstveni Contract sa nepromenljivim parametrima: Hash Lightning, timeout, refund Address. U slučaju neuspeha, automatski oporavak putem obezbeđenog Address, nezavisno od Zeus LSP.



**Zeus Swaps Rescue Key**: tokom On-Chain → Lightning zamene, Zeus automatski generiše univerzalni ključ za oporavak koji zamenjuje stare pojedinačne fajlove za povraćaj. Ovaj jedinstveni ključ funkcioniše na bilo kom uređaju i za sve zamene kreirane sa njim. Ključno je preuzeti i sačuvati ovaj ključ na sigurnom mestu kako biste mogli da povratite svoja sredstva u slučaju neuspeha zamene.



### Optimizacija mreže



Zeus Swap automatski prilagođava vremena isteka i Mining naknade u skladu sa uslovima mreže. Korisnici Zeusa imaju koristi od naprednih opcija: izbor LSP-a, prilagođena kašnjenja, kompatibilnost sa drugim uslugama (Boltz).



## Instalacija i korišćenje



### Metode pristupa



**Interface web** (swaps.zeuslsp.com): univerzalno rešenje kompatibilno sa svim novčanicima, nije potrebna instalacija, idealno za povremenu upotrebu.



**Zeus aplikacija** (iOS/Android): integrisano iskustvo koje kombinuje Wallet i zamene, pogodno za redovne korisnike.



Pogledajte naš Zeus vodič da saznate više o ovom kompletnom Wallet :



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Web konfiguracija



**On-Chain → Lightning**: Proces počinje konfigurisanjem zamene na Interface web Zeus Swap. Korisnik može koristiti strelicu između polja On-Chain i Lightning da obrne smer zamene.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: izbor iznosa (Sats 50,000 → Sats 49,648 nakon naknada) sa transparentnim prikazom mrežnih naknada (Sats 302) i Zeus usluge (Sats 50).*



Tokom procesa, Zeus vam nudi da preuzmete univerzalni ključ za oporavak :



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Dijalog za preuzimanje Zeus Swaps Rescue Key - univerzalni ključ koji zamenjuje stare pojedinačne datoteke za nadoknadu*



Ako već imate ključ, Zeus vam omogućava da ga proverite:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface za proveru validnosti postojećeg Zeus Swaps Rescue Key-a*



Jednom kada se konfiguriše, Zeus generiše skladište Bitcoin Address i prikazuje uputstva :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Stranica za završetak zamene: QR kod i Bitcoin Address za slanje 50,000 Sats, sa podsetnikom o isteku roka od 24 sata*



Zamena zatim čeka potvrdu Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Status "Transakcija u Mempool" - čekanje na potvrdu Bitcoin za finalizaciju zamene*



Kada se potvrdi, zamena se automatski završava:



![Swap réussi](assets/fr/06.webp)



*Potvrda uspeha: 49,648 Sats primljeno na Lightning nakon odbitka mrežnih i uslužnih naknada*



### Korišćenje Zeus aplikacije



**Lightning → On-Chain**: Zeus aplikacija nudi integrisano iskustvo za obrnute zamene (Lightning u Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Glavni ekran Zeus prikazuje stanje Lightning (69,851 Sats) i On-Chain (38,018 Sats), pristup zamjenama putem bočnog menija*



![Configuration du swap reverse](assets/fr/08.webp)



*Interface obrnuto kreiranje zamene: 50,000 Sats Lightning → 49,220 Sats On-Chain, sa mrežnim troškovima (530 Sats) i uslugom (250 Sats) jasno prikazanim. Korisnici mogu ručno uneti Bitcoin primanje Address, ili generate automatski iz Wallet Zeus putem dugmeta "generate On-Chain Address".*



![Finalisation du swap mobile](assets/fr/09.webp)



*Ekrani finalizacije: Lightning Invoice ekran za plaćanje sa "PLATI OVAJ Invoice", potvrda uspešnog Lightning plaćanja za 9,96 sekundi, i izvod stanja sa 49,162 Sats koji čekaju potvrdu*



### Nadzor i bezbednost



Svaka zamena ima jedinstveni identifikator sa praćenjem u realnom vremenu. Prikaz kompletnog napretka, automatska upozorenja za datume isteka. Automatske preporuke naplate prema uslovima mreže.



## Prednosti i ograničenja



### Pogodnosti





- Jednostavnost**: Zamena u nekoliko klikova naspram ručnog manipulisanja kanalima
- Bez staratelja**: nema KYC, nema naloga, sredstva nikada nisu poverena trećoj strani
- Transparentnost**: naknade su eksplicitno prikazane pre validacije (0,1% do 0,5% + minage u zavisnosti od korisničkih testova - proverite trenutne naknade pri svakoj zameni)
- Mobilna integracija**: izvorno iskustvo u Zeus Wallet



### Ograničenja





- Vremena isteka**: maksimalno 24-48h, neuspeh ako Bitcoin nije potvrđen na vreme
- Ograničenja iznosa**: minimum 25,000 Sats, Zeus LSP likvidnost varijabilna prema uslovima
- Tragovi On-Chain**: HTLC skripte potencijalno prepoznatljive analizom Blockchain
- Potvrda potrebna**: minimum 10 minuta za validaciju Bitcoin



## Najbolje prakse



### Vremenski okvir i troškovi





- Gledajte Mempool.space za vreme niske zagušenosti.
- Preferirajte vikende i sate van špica kako biste smanjili troškove Mining
- Izračunajte profitabilnost: male količine naspram otvaranja direktnog kanala



### Bezbednost





- Proverite adrese Bitcoin pažljivo (preporučuje se kopiranje-lepljenje)
- Napravite rezervnu kopiju Zeus Swaps ključa za spasavanje**: preuzmite i sačuvajte ključ za oporavak na sigurnom mestu
- Dokument: Contract ID, povraćaj Address, datum isteka
- Koristite odgovarajuće Mining naknade za pravovremenu potvrdu.



### Strategija korišćenja





- Uskladite likvidnost On-Chain/Lightning prema vašim potrebama
- Zeus Swap za jednokratna prilagođavanja, direktni kanali za trajne potrebe



## Poređenje sa drugim swap uslugama



### Zeus Swap vs Boltz Exchange



Zeus Swap koristi Boltzovu pozadinsku tehnologiju, ali uvodi neka ključna poboljšanja:



**Prednosti Zeus Swap-a** :




- Interface unified**: native integration in Zeus Wallet vs Interface web technique Boltz
- WebSocket API**: ažuriranja u realnom vremenu vs. ručno anketiranje
- Automatizovano upravljanje**: automatsko fakturisanje i upravljanje Address
- Podrška za mobilne uređaje**: optimizacija za pametne telefone vs. samo za desktop računare
- Swagger dokumentacija**: kompletan REST API za programere



**Boltz ostaje povoljan** za potpunu nezavisnost i upotrebu sa bilo kojom Bitcoin/Lightning konfiguracijom.



Zeus Swap transformiše dokazanu Boltz tehnologiju u iskustvo za glavne korisnike, uporedivo sa razlikom između sirovog protokola i aplikacije prilagođene korisniku.



### Zeus Swap vs Phoenix/Breez (integrisane zamene)



Phoenix i Breez integrišu transparentne funkcionalnosti zamene koje skrivaju tehničku složenost od krajnjeg korisnika. Phoenix koristi automatski sistem zamene gde korisnik eksplicitno ne razlikuje između Bitcoin slojeva: on "šalje na Bitcoin Address" i aplikacija upravlja zamenom u pozadini.



Ovaj ultra-pojednostavljeni pristup savršeno odgovara početnicima, ali ograničava razumevanje i kontrolu operacija. Zeus Swap usvaja više obrazovnu filozofiju: korisnici razumeju da menjaju između dva različita sloja, postepeno razvijajući svoje razumevanje ekosistema dva-Layer Bitcoin.



## Detaljno poređenje naknada i ograničenja (2024)



⚠️ **Upozorenje**: Naknade mogu varirati tokom vremena u zavisnosti od tržišnih uslova i ažuriranja usluga. Uvek proverite naknade prikazane u Interface pre nego što potvrdite zamenu.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap nudi ravnotežu između jednostavnosti korišćenja i tehničke kontrole: pristupačniji je od Boltz-a, fleksibilniji od Phoenix/Breez-a, sa strogim nekustodijalnim pristupom.



## Zaključak



Zeus Swap predstavlja značajnu inovaciju u ekosistemu Bitcoin, elegantno rešavajući izazov interoperabilnosti između glavne mreže i Lightning Network. Kombinovanjem kriptografske robusnosti atomskih zamena sa pristupačnim korisničkim iskustvom, ova usluga demokratizuje upravljanje Bitcoin dual-Layer bez kompromitovanja principa finansijskog suvereniteta.



Nenadmašna arhitektura Zeus Swap-a, nasleđena od dokazane Boltz tehnologije, osigurava da vaša sredstva ostanu pod vašom isključivom kontrolom tokom celog procesa zamene. Ovaj pristup poštuje duh Bitcoin, dok nudi korisničku pogodnost potrebnu za masovno prihvatanje. Transparentnost cena i odsustvo KYC procesa dodatno jačaju ovu jedinstvenu vrednosnu ponudu.



Za modernog korisnika Bitcoin, Zeus Swap je strateški alat za optimizaciju distribucije likvidnosti prema potrebama: On-Chain sigurno skladištenje za dugoročne uštede, Lightning dostupnost za dnevnu potrošnju i mikrotransakcije. Ova fleksibilnost transformiše upravljanje Bitcoin iz tehničkog ograničenja u konkurentsku prednost.



Buduća evolucija Zeus Swap-a, podržana od strane iskusnog Zeus LSP tima i Boltz open-source zajednice, obećava kontinuirana poboljšanja u pogledu troškova, vremena obrade i korisničkog iskustva. Ova usluga je deo šireg trenda ka sazrevanju Bitcoin infrastrukture, gde tehnička sofisticiranost postaje transparentna za krajnjeg korisnika.



## Resursi



### Zvanična dokumentacija




- [Zeus Swap - Web portal](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobilna aplikacija](https://zeusln.app)
- [Blog Zeus - Najave i tutorijali](https://blog.zeusln.com)
- [Zeus tehnička dokumentacija](https://docs.zeusln.app)



### Zajednica i podrška




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)