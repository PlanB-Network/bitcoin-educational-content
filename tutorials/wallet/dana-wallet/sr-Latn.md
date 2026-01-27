---
name: Dana Wallet
description: Minimalistički portfolio za Tiha Plaćanja (BIP-352)
---

![cover](assets/cover.webp)



Ponovna upotreba Bitcoin adresa je jedna od najdirektnijih pretnji korisničkoj poverljivosti. Kada primalac deli jednu adresu za primanje više uplata, bilo koji posmatrač može pratiti sve povezane transakcije i rekonstruisati njihovu finansijsku istoriju. Ovaj problem posebno pogađa kreatore sadržaja, dobrotvorne organizacije ili aktiviste koji žele javno prikazati adresu za donacije bez ugrožavanja svoje privatnosti ili privatnosti svojih donatora.



Dana Wallet odgovara na ovaj problem elegantnim rešenjem: Silent Payments. Ovaj minimalistički, open-source wallet, lansiran 2024. godine, generiše ponovo upotrebljivu statičku adresu, dok garantuje da svaka primljena uplata završi na zasebnoj adresi na blockchain-u. Pošiljalac ne treba prethodnu interakciju sa primaocem, a nijedan spoljašnji posmatrač ne može povezati pojedinačne transakcije. Na blockchain-u, ove uplate izgledaju kao potpuno obične Taproot transakcije.



Dana Wallet je dostupna na Mainnet i Signet, ali programeri je i dalje smatraju eksperimentalnom i preporučuju da ne deponujete sredstva koja niste spremni da izgubite. U ovom vodiču ćemo koristiti Signet verziju da otkrijemo Silent Payments bez rizikovanja stvarnih sredstava.



## Šta je Dana Wallet?



### Filozofija i ciljevi



Dana Wallet usvaja pristup "SP-prvo": wallet generiše isključivo adrese za Tihe Uplate i prihvata samo ovu vrstu plaćanja. Nećete biti u mogućnosti da kreirate klasičnu Bitcoin adresu (legacy, SegWit ili Taproot standard) sa ovom aplikacijom. Ovo namerno ograničenje omogućava vam da se u potpunosti fokusirate na učenje BIP-352 protokola bez ometanja drugim funkcijama. Nepregledan interfejs namerno favorizuje jednostavnost korišćenja u odnosu na obilje opcija, čineći alat pristupačnim čak i korisnicima koji su novi u on-chain konceptima poverljivosti.



Projekat je potpuno otvorenog koda, razvijen sa Flutter-om za mobilni interfejs i Rust za internu kriptografsku logiku. Ova arhitektura kombinuje fluidno korisničko iskustvo sa optimalnim performansama za intenzivne operacije skeniranja.



### Kako funkcionišu Silent Payments?



Silent Payments (BIP-352) zasnovani su na sofisticiranom kriptografskom mehanizmu koristeći Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Primalac generiše statičku adresu (počinje sa `sp1...` na mainnet ili `tsp1...` na Signet) koja se sastoji od dva različita javna ključa: skenirajući ključ ($B_{scan}$) za detekciju dolaznih uplata, i ključ za trošenje ($B_{spend}$) za trošenje primljenih sredstava. Ovo razdvajanje omogućava da se ključ za trošenje čuva na wallet hardveru dok se skenirajući ključ koristi na povezanom uređaju.



Kada pošiljalac želi da izvrši uplatu, njegov wallet kombinuje zbir privatnih ključeva njegovih ulaza sa javnim ključem za skeniranje primaoca kako bi izračunao zajedničku ECDH tajnu. Ova tajna generiše kriptografski "tweak" koji, dodan na ključ za trošenje primaoca, stvara jedinstvenu Taproot adresu za tu transakciju.



Primalac može reprodukovati ovaj proračun koristeći svoj privatni ključ skeniranja i javne ključeve vidljive u transakciji (matematička osobina Diffie-Hellman-a). Ovo mu omogućava da detektuje i potroši sredstva bez ikakve prethodne interakcije sa pošiljaocem.



Ovaj pristup nudi nekoliko prednosti:




- Poverljivost primaoca**: svaka uplata završava na različitoj adresi
- Poverljivost pošiljaoca**: nema trajnog identifikatora koji povezuje uplate
- Nema servera treće strane**: protokol radi autonomno
- Nedistinguive transakcije**: Tihi Plaćanja izgledaju kao obične Taproot transakcije



Glavni nedostatak je cena skeniranja: primalac mora analizirati svaku novu Taproot transakciju kako bi otkrio one namenjene njemu.



Ako želite da saznate više o tehničkom funkcionisanju Silent Payments, preporučujemo kurs BTC204 o poverljivosti u Bitcoin, koji uključuje poglavlje posvećeno Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Podržane platforme



Dana Wallet je dostupna kao Android aplikacija. APK se može preuzeti putem posvećenog F-Droid repozitorijuma koji obezbeđuju programeri, putem Obtainium-a, ili direktno sa GitHub-a. Za korisnike Linux-a, tehnički je moguće kompajlirati Flutter aplikaciju za desktop.



Aplikacija nije dostupna na iOS-u ili putem zvaničnih prodavnica (Google Play, App Store), što odražava njen eksperimentalni status i fokus na tehničku publiku.



## Instalacija



### Osnovni preduslovi



Da biste instalirali Dana Wallet na Android, potreban vam je Android uređaj sa omogućenim opcijama "Nepoznati izvori" u sigurnosnim postavkama. Nije potreban nalog ili registracija.



### Dodaj F-Cold depozit



Preporučeni metod je da dodate posvećeno F-Droid spremište za Dana Wallet. Idite na `fdroid.silentpayments.dev` gde ćete pronaći link do spremišta i QR kod za skeniranje. Spremište trenutno nudi 3 aplikacije: verziju Mainnet, Development i Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Instalacija putem F-Droid



Otvorite F-Droid aplikaciju na svom Android uređaju, zatim pristupite Podešavanjima putem ikone u donjem desnom uglu. Izaberite "Repozitorijumi" da biste upravljali izvorima aplikacija. Pritisnite dugme "+" da dodate novi repozitorijum, zatim skenirajte QR kod ili nalepite link `https://fdroid.silentpayments.dev/fdroid/repo`. Kada je repozitorijum dodat, videćete tri verzije Dana Wallet dostupne. Izaberite "Dana Wallet - Bookmark" i pritisnite "Instaliraj".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Početna konfiguracija



### Kreiranje portfolija



Prilikom prvog pokretanja, Dana Wallet prikazuje ekran dobrodošlice koji predstavlja njenu misiju: "Šaljite i primajte donacije bez posrednika". Pritisnite "Početak" za nastavak. Sledeći ekran prikazuje tri ključne prednosti aplikacije:




- Lako doniranje**: počnite primati donacije za nekoliko sekundi
- Privatnost po defaultu**: nema potrebe za serverima ili složenom infrastrukturom
- Iskustvo slično e-pošti**: šaljite i primajte bitkoine jednostavno kao e-poštu



Možete izabrati između "Restore" za vraćanje postojećeg portfolija ili "Create new wallet" za kreiranje novog. Pritisnite "Create new wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Aplikacija zatim generiše frazu za oporavak, koju treba pažljivo zabeležiti na fizičkom mediju. Čak i za testna sredstva bez stvarne vrednosti, usvojite dobre prakse pravljenja rezervnih kopija.



### Interface i parametri



Kada je portfolio kreiran, bićete prebačeni na glavni interfejs, podeljen u dva taba: "Transact" i "Settings".



Kartica **Transact** prikazuje stanje vašeg bitcoina (i njegovu konverziju u dolare), listu nedavnih transakcija i dva dugmeta za akciju: "Plati" za slanje sredstava i dugme za primanje (ikona preuzimanja).



Kartica **Settings** nudi četiri opcije:




- Prikaži seed frazu**: prikazuje vašu frazu za oporavak radi čuvanja
- Promeni fiat valutu**: promeni prikaz valute (USD po podrazumevano)
- Postavite URL pozadinskog sistema**: konfigurišite URL servera Blindbit (pogledajte sledeći odeljak)
- Obriši wallet**: potpuno briše wallet sa uređaja



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Blindbit server



Dana Wallet koristi indeksirajući server nazvan **Blindbit** za detekciju vaših Silent Payments. Razumevanje kako funkcioniše je važno za evaluaciju modela poverenja aplikacije.



**Zašto nam je potreban server?



Da bi detektovao Silent Payment, tvoj wallet mora teoretski da skenira sve Taproot transakcije u svakom bloku i izvrši kriptografsku kalkulaciju (ECDH) za svaku od njih. Na mobilnom telefonu, ova operacija bi bila previše zahtevna u smislu računarske snage i propusnog opsega.



Blindbit server rešava ovaj problem prethodnim izračunavanjem međupodataka (nazvanih "tweaks") za sve Taproot transakcije. Vaš wallet zatim preuzima ove tweakse (33 bajta po transakciji) i vrši konačni proračun **lokalno** kako bi proverio da li uplata pripada vama.



**Sačuvana poverljivost**



Za razliku od konvencionalnog Electrum servera gde otkrivate svoje adrese, Blindbit server ne zna koja plaćanja pripadaju vama. On pruža iste podatke svim korisnicima, a vaš telefon obavlja konačnu verifikaciju. Vaša poverljivost je stoga očuvana u odnosu na server.



**Podrazumevani server



Dana Wallet koristi javni server `silentpayments.dev/blindbit/signet` (za Signet) ili `silentpayments.dev/blindbit/mainnet` (za Mainnet). Možete promeniti ovaj URL u podešavanjima ako hostujete sopstveni server.



**Hostujte svoj Blindbit server**



Za korisnike koji žele potpunu suverenost, moguće je hostovati sopstveni Blindbit Oracle server. Ovo zahteva :




- Kompletan Bitcoin Core čvor **non-eagled** (non-pruned)
- Instaliranje Blindbit Oracle (dostupno na GitHub-u: `setavenger/blindbit-oracle`)
- Približno 10 GB dodatnog prostora na disku
- Tehničke veštine (Kompilacija Go, konfiguracija servera)



Još uvek nije dostupna nijedna pakovana aplikacija za Umbrel ili Start9. Instalacija za sada ostaje ručna. Ovo je oblast u aktivnoj evoluciji i pristupačnija rešenja mogu se pojaviti u budućnosti.



## Svakodnevna upotreba



### Primanje sredstava



Da biste primili bitkoine, pritisnite dugme za primanje (ikona preuzimanja) sa glavnog ekrana. Dana Wallet zatim prikazuje vašu kompletnu Silent Payment adresu u formatu `tsp1q...` na Bookmark-u. Interfejs nudi nekoliko opcija:




- Prikaži QR kod**: prikazuje QR kod vaše adrese za lako skeniranje
- Podeli**: podeli adresu putem aplikacija na svom telefonu
- Kopiraj**: kopira adresu u međuspremnik



Kao što je prikazano na ekranu, ovu adresu možete javno deliti na svojim društvenim mrežama bez ugrožavanja vaše privatnosti.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Da biste dobili svoja prva testna sredstva na Signet-u, koristite posvećeni Silent Payments faucet dostupan na `silentpayments.dev/faucet/signet`. Kopirajte vašu adresu `tsp1...`, zalepite je u predviđeno polje na faucetu, zatim potvrdite zahtev. Sačekajte da se blok izrudari (oko 10 minuta na Signet-u).



### Pošalji uplatu



Da biste poslali sredstva, pritisnite dugme "Plati" na glavnom ekranu. Pojaviće se ekran "Izaberite primaoca(e)" sa tri opcije za određivanje primaoca:




- Unesite podatke o plaćanju ručno
- Nalepi iz međumemorije**: nalepi adresu iz međumemorije
- Skeniraj QR kod**: skeniraj QR kod koji sadrži adresu



Kada je adresa primaoca potvrđena, ekran "Unesite iznos" vam omogućava da unesete iznos koji želite poslati u satoshijima. Vaše dostupno stanje je prikazano za referencu. Pritisnite "Nastavite na izbor naknade" da nastavite.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Sledeći ekran prikazuje tri nivoa naplate, u zavisnosti od potrebne hitnosti:




- Brzo** (10-30 minuta): veće naknade za brzu potvrdu
- Normalno** (30-60 minuta): umereni troškovi
- Sporo** (1+ sat): minimalna naknada za nehitne transakcije



Nakon odabira nivoa naknade, ekran za potvrdu "Spremni za slanje?" sumira sve detalje: odredišnu adresu, iznos, procenjeno vreme i naknadu za transakciju. Pažljivo proverite ove informacije, a zatim pritisnite "Pošalji" da biste poslali transakciju.



Jednom poslata, transakcija se pojavljuje u vašoj istoriji sa statusom "Nepotvrđeno" dok ne bude uključena u blok. Vaš saldo se ažurira u skladu s tim.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Prednosti i ograničenja



### Istaknuto





- Pedagoški**: pojednostavljeni interfejs fokusiran na učenje Silent Payments
- Dvosmerni**: podržava i slanje i primanje, za razliku od drugih portfolija
- Otvoreni kod**: potpuno proverljiv kod na GitHub-u
- Posvećen Faucet**: olakšava dobijanje sredstava za testiranje
- Bez naloga**: nije potrebna registracija ili lični podaci



### Ograničenja koja treba razmotriti





- Eksperimentalno**: nesoftverizovano, koristiti sa oprezom na Mainnet
- Ograničena platforma**: uglavnom Android, nema iOS verzije
- Smanjena funkcionalnost**: nema kontrole nad novčićima, nema podračuna, nema Lightning
- Intenzivno skeniranje**: detekcija plaćanja troši značajne resurse



## Najbolje prakse



### seed bezbednost



Čak i za Signet testove sa bezvrednim pozadinama, tretirajte vašu frazu za oporavak ozbiljno. Koristite opciju "Prikaži seed frazu" u podešavanjima da je pažljivo zapišete. Kao dobru praksu, održavajte potpuno odvojene novčanike za Signet i Mainnet: nikada ne koristite seed kreiran za testiranje na wallet namenjen za primanje stvarnih sredstava.



### Upozorenje o eksperimentalnom statusu



Dana Wallet je još uvek u eksperimentalnoj fazi prema rečima njenih tvoraca. Kako jasno navode: "Nemojte koristiti sredstva koja niste spremni da izgubite". Za potrebe učenja, odlučite se za Signet verziju. Ako koristite Mainnet verziju, ograničite se na token iznose.



### Bekap i obnova



Oporavak sredstava putem Silent Payments zahteva wallet kompatibilan sa BIP-352 protokolom. Standardni wallet ne može skenirati blockchain da povrati vaše UTXO Silent Payments. Držite instaliran Dana Wallet ili koristite opciju "Restore" pri prvom pokretanju da povratite postojeći wallet.



## Poređenje sa BIP-47 i PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Tihi Plaćanja eliminišu BIP-47 obaveštenje o transakciji po cenu skupljeg skeniranja. PayJoin rešava drugačiji problem (korelacija ulaza) i može se kombinovati sa Tihim Plaćanjima.



## Zaključak



Dana Wallet je vredan obrazovni alat za učenje o Silent Payments u okruženju bez rizika. Njegov minimalistički pristup omogućava vam da razumete osnovne mehanizme BIP-352 protokola bez ometanja sekundarnim funkcijama. Eksperimentisanjem sa Signet-om, razvijate praktično razumevanje ove obećavajuće tehnologije za poverljivost transakcija Bitcoin.



Silent Payments predstavljaju značajan korak napred u usklađivanju jednostavnosti korišćenja i poštovanja privatnosti. Entuzijazam zajednice i prve integracije u razne novčanike (Cake Wallet, BitBox02, BlueWallet za slanje) ukazuju na budućnost u kojoj objavljivanje adrese za donacije više neće ugrožavati finansijsku privatnost njenog vlasnika.



## Resursi



### Zvanična dokumentacija




- Dana Wallet GitHub repository: https://github.com/cygnet3/danawallet
- F-Cold depozit: https://fdroid.silentpayments.dev
- Silent Payments zajednica: https://silentpayments.xyz
- Specifikacija BIP-352: https://bips.dev/352



### Signet test alati




- Faucet Silent Payments: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit server (self-hosted)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle