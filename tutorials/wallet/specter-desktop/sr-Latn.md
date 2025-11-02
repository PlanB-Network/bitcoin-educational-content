---
name: Specter Desktop
description: Upravljajte svojim Bitcoin portfolijima sa više potpisa u potpunom suverenitetu sa svojim čvorom
---

![cover](assets/cover.webp)



Specter Desktop je aplikacija otvorenog koda (MIT licenca) koju razvija Cryptoadvance od 2019. godine i koja olakšava upravljanje Bitcoin novčanicima sa vašim hardverskim novčanicima (Ledger, Trezor, Coldcard, BitBox02, Passport, itd.) i vašom sopstvenom Bitcoin infrastrukturom (Bitcoin core čvor ili Electrum Server). Aplikacija se posebno ističe u konfiguracijama sa više potpisa, omogućavajući vam da osigurate velike sume raspodelom moći potpisivanja između nekoliko nezavisnih hardverskih novčanika.



**U ovom vodiču ćete naučiti kako da:**




- Instalirajte i konfigurišite Specter Desktop na vašem računaru (Windows, macOS ili Linux)
- Povežite Specter sa Electrum Server (koristićemo Umbrel u ovom primeru)
- Kreiranje jednostavnog Wallet sa Hardware Wallet (Coldcard)
- Primajte i šaljite bitkoine sa potpunim suverenitetom
- Postavljanje 2-od-3 multisignature Wallet sa nekoliko hardverskih novčanika
- Instalirajte Specter na Umbrel server (napredni bonus)



Sve vaše transakcije će biti validirane lokalno putem vaše sopstvene infrastrukture, bez prenosa bilo kakvih informacija na eksterne servere, garantujući vašu poverljivost i finansijski suverenitet. Uvek proverite transakcije na vašem Hardware Wallet ekranu pre potpisivanja.



## Preuzimanje i instalacija



Posetite zvaničnu veb stranicu Specter Desktop-a da biste preuzeli aplikaciju.



![Page d'accueil Specter](assets/fr/01.webp)



Na stranici za preuzimanje, izaberite verziju koja odgovara vašem operativnom sistemu: macOS, Windows ili Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Kada preuzmete, instalirajte aplikaciju prema uobičajenim uputstvima vašeg operativnog sistema. Za macOS, prevucite ikonu u Applications. Za Windows, pokrenite instalacioni program. Za Linux, pratite uputstva za paket.



## Početna konfiguracija



Prilikom prvog pokretanja, Specter Desktop vas pita da izaberete tip konekcije. Možete se povezati na Electrum Server ili na svoj sopstveni Bitcoin core čvor.



![Choix du type de connexion](assets/fr/03.webp)



U ovom primeru, koristićemo konekciju na Electrum Server koji radi na Umbrel.



Za više informacija, pogledajte naš Umbrel vodič:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Ova opcija nudi bržu sinhronizaciju od Bitcoin core. Ako želite, možete izabrati "Bitcoin core" i konfigurisati vezu sa vašim lokalnim čvorom. Sledeći koraci ostaju isti bez obzira na vaš izbor.



Odaberite "Electrum Connection" zatim izaberite "Enter my own" da biste konfigurisali svoj Electrum Server.



![Configuration Electrum](assets/fr/04.webp)



Unesite Address vašeg Electrum Server. U našem slučaju sa Umbrel, Address će biti `umbrel.local` sa portom `50001`. Kliknite na "Connect" da uspostavite vezu.



Kada se povežete, pojavljuje se početni ekran sa kontrolnom listom za početak. Sada treba da dodate svoje hardverske novčanike.



![Écran d'accueil](assets/fr/05.webp)



## Dodavanje Hardware Wallet



U levom meniju kliknite na "Add device" da dodate vaš Hardware Wallet.



Specter Desktop podržava brojne hardverske novčanike: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault i mnoge druge.



Ako želite da saznate više, pogledajte naše Hardware Wallet tutorijale.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Odaberite svoj Hardware Wallet. U ovom primeru, koristimo Coldcard MK4.



Molimo vas da pronađete naš vodič za ovaj Hardware Wallet :



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Za Coldcard, potrebno je da izvezete javne ključeve sa Hardware Wallet bilo putem USB veze ili microSD kartice.



![Import des clés du Coldcard](assets/fr/07.webp)



Pratite instrukcije prikazane za izvoz ključeva sa vašeg Coldcard-a. Dajte svom Hardware Wallet ime (ovde "MK4 Tuto"). Kada ključevi budu uvezeni, možete kreirati Wallet sa jednim ključem, ili dodati druge hardverske novčanike za multi-potpisni Wallet.



![Dispositif ajouté](assets/fr/08.webp)



## Kreiranje portfolija



Nakon dodavanja vašeg Hardware Wallet, kliknite na "Create single key Wallet" da biste kreirali Wallet sa jednim potpisom.



Dajte svom portfoliju ime (npr. "Wallet za tuto") i izaberite tip Address. Izaberite "SegWit" da koristite native BECH32 adrese, koje optimizuju troškove transakcija.



![Configuration du portefeuille](assets/fr/09.webp)



Kada vaš portfelj bude kreiran, Specter nudi da sačuva rezervnu PDF datoteku koja sadrži sve javne informacije potrebne za obnavljanje vašeg portfelja (deskriptori, prošireni javni ključevi). Ova datoteka ne sadrži vaše privatne ključeve.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Primite bitkoine



Da biste primili bitkoine, izaberite svoj Wallet u meniju sa leve strane, zatim kliknite na karticu "Receive".



Specter automatski generiše novi prijem Address sa QR kodom.



![Génération d'une adresse de réception](assets/fr/11.webp)



Možete kopirati Address ili skenirati QR kod. Uvek proverite Address na vašem Hardware Wallet ekranu pre nego što ga prosledite bilo kome.



## Prikaži istoriju i adrese



Kada primite bitkoine, možete pregledati svoje transakcije u kartici "Transakcije".



![Historique des transactions](assets/fr/12.webp)



Kartica "Adrese" omogućava vam da pregledate sve adrese generisane od strane vašeg portfolija, sa statusom korišćenja i povezanim iznosima.



![Liste des adresses](assets/fr/13.webp)



## Pošalji bitkoine



Da biste poslali bitkoine, kliknite na karticu "Pošalji". Unesite primaočev Address, iznos koji se šalje i proverite napredne opcije ako želite ručno da izaberete UTXO-ove (Coin kontrola).



![Création d'une transaction](assets/fr/14.webp)



Kliknite na "Create Unsigned Transaction" da biste napravili transakciju. Specter će zatim tražiti da potpišete transakciju sa vašim Hardware Wallet.



![Signature de la transaction](assets/fr/15.webp)



Ako koristite Coldcard, imaćete izbor potpisivanja putem USB-a ili korišćenjem microSD kartice (air-gapped). Potvrdite transakciju na vašem Hardware Wallet ekranu, pažljivo proveravajući odredište Address i iznos.



Jednom kada je transakcija potpisana, možete je emitovati na Bitcoin mreži.



![Options de diffusion](assets/fr/16.webp)



Kliknite na "Send transaction" da pošaljete transakciju. Specter će potvrditi da je vaša transakcija poslata, a njen status možete pratiti u kartici Transakcije.



![Diffusion de la transaction](assets/fr/17.webp)



## Kreiranje i korišćenje portfolija sa više potpisa



Jedna od glavnih prednosti Specter Desktop-a je njegova sposobnost da pojednostavi upravljanje portfeljima sa više potpisa. Multisig Wallet zahteva više potpisa za autorizaciju transakcije, eliminišući jedinstvenu tačku kvara. Konfiguracija 2-na-3, na primer, zahteva dva potpisa sa tri odvojena hardverska novčanika da bi se potvrdio bilo koji trošak.



Da biste kreirali Multisig Wallet, počnite dodavanjem svih potpisničkih hardverskih novčanika putem opcije "Dodaj uređaj". U ovom primeru, koristićemo tri različita hardverska novčanika: Coldcard MK4 (već ranije dodat), Passport i Ledger. Ova diverzifikacija proizvođača jača sigurnost izbegavanjem zavisnosti od jednog Supply lanca ili firmvera.



Evo linkova do tutorijala za Ledger i Passport:



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Dodajte Passport tako što ćete imenovati Hardware Wallet (npr. "Passport multi") i uvesti njegove ključeve putem microSD kartice ili QR koda. Zatim kliknite na "Nastavi" da nastavite.



![Ajout du Passport](assets/fr/23.webp)



Zatim dodajte Ledger povezivanjem putem USB-a i otvaranjem aplikacije Bitcoin na Hardware Wallet. Imenujte ga (npr. "Ledger multi") i kliknite na "Get via USB" zatim "Continue" da biste uvezli njegove javne ključeve.



![Ajout du Ledger](assets/fr/24.webp)



Kada registrujete svoja tri hardverska novčanika u Specter-u, kliknite na "Add Wallet" i odaberite opciju "Multiple Signature" da biste kreirali multi-signature Wallet.



![Choix du type de wallet](assets/fr/25.webp)



Odaberite tri hardverska novčanika koja želite uključiti u svoj multisignature kvorum: MK4 Tuto, Passport multi i Ledger multi. Kliknite na "Nastavi" da pređete na sledeći korak.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Izaberite svoju konfiguraciju sa više potpisa. Odaberite "SegWit" kao tip Address da biste iskoristili optimizovane troškove. Parametar "Potrebni potpisi za autorizaciju transakcija (m od 3)" vam omogućava da definišete prag: za konfiguraciju 2-od-3, potrebna su 2 potpisa. Svaki Hardware Wallet prikazuje svoj odgovarajući Multisig ključ. Kliknite na "Kreiraj Wallet" da završite kreiranje.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Vaš "Multi tuto" portfelj sa višestrukim potpisom je sada kreiran. Specter odmah preporučuje da sačuvate rezervnu PDF datoteku koja sadrži portfelj Descriptor. Kliknite na "Sačuvaj rezervni PDF" da preuzmete ovu kritičnu datoteku.



![Wallet multisig créé](assets/fr/28.webp)



Specter takođe omogućava izvoz Wallet informacija na svaki od vaših hardverskih novčanika putem QR koda ili fajla. Ovo omogućava određenim hardverskim novčanicima (kao što su Coldcard ili Passport) da direktno u svojoj memoriji čuvaju Multisig konfiguraciju.



Za pasoš, otključajte svoj uređaj, zatim idite na "Upravljanje nalogom" > "Poveži Wallet" > "Specter" > "Multisig" > "QR kod", zatim skenirajte QR kod generisan od strane Specter-a. Vaš pasoš će zatim tražiti da skenirate prijemni Address sa vašeg Wallet kako biste potvrdili Multisig konfiguraciju.



Za MK4, priključite ga na svoj PC i otključajte. Zatim kliknite na "Save MK4 Tuto file" i sačuvajte datoteku na vaš MK4. Sledeći put kada potpišete vaš Hardware Wallet, MK4 će koristiti ovu datoteku da završi konfiguraciju Multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Za vašu informaciju, možete pristupiti rezervnim kopijama u bilo kom trenutku iz kartice "Podešavanja" vašeg portfolija, zatim "Izvoz":



![Accès au backup PDF](assets/fr/30.webp)



Svakodnevna upotreba ostaje slična jednostavnom Wallet: vi generate primate adrese kao i obično. Da biste poslali bitkoine, idite na karticu "Pošalji", unesite primaočev Address i iznos, a zatim kliknite na "Kreiraj nepotpisanu transakciju".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter gradi PSBT (Partially Signed Bitcoin Transaction) i prikazuje "Acquired 0 of 2 signatures". Sada morate potpisati sa najmanje dva od vaša tri hardverska novčanika. Kliknite na prvi Hardware Wallet (npr. "MK4 Tuto") da potpišete sa vašim Coldcard, zatim na drugi (npr. "Passport multi") da dobijete drugi potrebni potpis.



![Signature de la transaction](assets/fr/32.webp)



Kada dobijete 2 potrebna potpisa (Interface prikazuje "Acquired 2 of 2 signatures" i "Transaction is ready to send"), kliknite na "Send Transaction" da biste emitovali transakciju na Bitcoin mreži.



![Transaction prête à être diffusée](assets/fr/33.webp)



Ovaj pristup sa više potpisa posebno je pogodan za kompanije (nekoliko menadžera treba da odobri troškove), porodice (zaštita višegeneracijskog nasleđa) ili pojedince koji upravljaju velikim sumama (geografska distribucija hardverskih novčanika za otpornost na lokalizovane katastrofe).



### Kritična važnost rezervnih kopija sa višestrukim potpisom



**Imajte na umu**: pravljenje rezervne kopije portfolija sa više potpisa je suštinski drugačije od pravljenja rezervne kopije jednog portfolija. Vaše fraze za oporavak (seed fraze) same po sebi nisu dovoljne za vraćanje Multisig portfolija. Morate takođe napraviti rezervnu kopiju **output descriptor** (output descriptor), koja sadrži informacije o konfiguraciji vašeg portfolija sa više potpisa.



output descriptor uključuje osnovne podatke: proširene javne ključeve (xpubs) svakog od potpisnika, prag potpisa (2-od-3 u našem primeru), tip skripte koja se koristi (SegWit native, nested ili legacy), i putanje derivacije za svaki Hardware Wallet. Bez ovog Descriptor, čak i ako imate dve od tri fraze za oporavak, nećete moći da obnovite svoj Wallet ili pristupite svojim bitcoinima. Descriptor omogućava vašem softveru da zna kako da kombinuje javne ključeve za generate Bitcoin adrese koje odgovaraju vašim sredstvima.



Specter Desktop automatski generiše rezervnu PDF datoteku kada kreirate svoj Multisig portfolio. Ovaj PDF sadrži kompletan Descriptor, otiske prstiju svakog Hardware Wallet i sve javne informacije potrebne za restauraciju. **Ova datoteka ne sadrži vaše privatne ključeve** i stoga sama po sebi ne omogućava trošenje vaših bitkoina, ali omogućava svakome ko joj pristupi da vidi vašu kompletnu istoriju transakcija i stanje.



Da biste pravilno napravili rezervnu kopiju vaše multisignature konfiguracije, pratite ovu proceduru: nakon kreiranja vašeg portfolija, kliknite na karticu "Settings", zatim "Export" i odaberite "Save Backup PDF". Napravite nekoliko kopija ovog PDF-a: odštampajte najmanje dve kopije na papiru, a takođe sačuvajte i šifrovanu digitalnu kopiju. Čuvajte jednu kopiju PDF-a sa svakom od vaših fraza za oporavak, na geografski odvojenim lokacijama.



Spalite svoje fraze za oporavak na vatrootpornim i vodootpornim metalnim pločama kako biste garantovali njihovu dugovečnost. Nikada ne potcenjujte važnost ovih rezervnih kopija: ako izgubite `~/.specter` folder na vašem računaru I izgubite jedan od vaših hardverskih novčanika bez Descriptor rezervne kopije, svi vaši fondovi će biti nepovratno izgubljeni, čak i sa konfiguracijom 2-na-3. Redundantnost sa više potpisa štiti od gubitka Hardware Wallet, ali samo ako ste pravilno napravili rezervnu kopiju Descriptor vašeg Wallet.



## Prednosti i ograničenja Specter Desktop



**Prednosti**: Optimalna poverljivost sa potpunom lokalnom validacijom bez servera trećih strana. Fleksibilnost višestrukog potpisa za napredne konfiguracije (korporativne, porodične, individualne). Opsežna podrška za Hardware Wallet sa potpunom interoperabilnošću (USB i bez mrežnog povezivanja).



**Ograničenja**: Značajna kriva učenja na naprednim Bitcoin konceptima (UTXO-i, deskriptori, putanje derivacije).



## Najbolje prakse



Uvek proverite adrese i iznose na vašem Hardware Wallet ekranu pre validacije, kako biste se zaštitili od malvera.



Čuvajte PDF rezervne kopije odvojeno od vaših semena. Ovi javni opisi mogu biti pohranjeni u bankovnom trezoru ili šifrovanom oblaku, olakšavajući oporavak bez izlaganja vaših privatnih ključeva.



Testirajte oporavak na token iznosima pre korišćenja vaših portfolija sa velikim fondovima. Kreirajte, testirajte, obrišite i obnovite kako biste potvrdili vaše procedure.



Ažurirajte Specter i vaš firmware redovno. Rasporedite vaše multi-signature ko-potpisnike geografski (kuća/kancelarija/blizina) kako biste izdržali lokalizovane katastrofe. Koristite opisne oznake kako biste olakšali računovodstvo i poreske prijave.



## Bonus: Instalacija na Bitcoin serveru (Umbrel, RaspiBlitz, Start9)



Ako već posedujete Bitcoin server kao što su Umbrel, RaspiBlitz, MyNode ili Start9, možete instalirati Specter Desktop direktno iz njihove prodavnice aplikacija. Ovaj pristup nudi nekoliko značajnih prednosti: aplikacija se automatski konfiguriše sa vašim lokalnim Bitcoin core čvorom, ostaje dostupna 24/7 putem Interface veba sa bilo kog uređaja na vašoj mreži, a možete joj čak i sigurno pristupiti na daljinu putem Tor-a. Cela vaša Bitcoin infrastruktura je centralizovana na jednom posvećenom serveru, što pojednostavljuje upravljanje i jača vašu suverenost.



### Instalacija iz Umbrel prodavnice aplikacija



Sa vašeg Umbrel Interface, idite u App Store i potražite Specter Desktop. Kliknite na "Install" da pokrenete instalaciju.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Kada je instalacija završena, otvorite Specter Desktop na vašem Umbrelu. Ekran dobrodošlice će vas zamoliti da izaberete tip konekcije. Ako koristite Specter na vašem Umbrelu, kliknite na "Update settings" da konfigurišete konekciju.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Odaberite "Remote Specter USB connection" da omogućite korišćenje USB hardverskih novčanika povezanih sa vašim lokalnim računarom dok koristite Specter na udaljenom Umbrel serveru.



![Configuration Remote Specter USB](assets/fr/20.webp)



Pratite instrukcije prikazane za konfigurisanje HWI Bridge. Potrebno je da pristupite podešavanjima uređaja bridge i dodate domen `http://umbrel.local:25441` na belu listu. Kliknite na "Update" da sačuvate konfiguraciju.



![HWI Bridge Settings](assets/fr/21.webp)



Ako biste takođe želeli da koristite svoje USB hardverske novčanike sa lokalnog računara, preuzmite Specter Desktop aplikaciju na svoj uređaj i postavite je na "Da, pokrećem Specter daljinski". Kliknite na "Sačuvaj" da završite konfiguraciju.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Zaključak



Specter Desktop demokratizuje napredne Bitcoin konfiguracije, čineći multi-potpis dostupnim bez žrtvovanja suvereniteta ili poverljivosti. Za korisnike koji upravljaju značajnim količinama novca, transformiše institucionalne prakse u rešenja koja mogu primeniti privatna lica.



Iako aplikacija zahteva početno ulaganje u infrastrukturu i učenje, nudi potpunu suverenost: kontrolu nad infrastrukturom za validaciju, fizički Ownership ključeva i transakcije bez nadzora trećih strana. Bilo da ste pojedinac koji osigurava svoju ušteđevinu, porodica koja stvara višegeneracijsku sef kutiju ili kompanija koja upravlja novčanim tokovima, Specter Desktop je referentni alat za usklađivanje maksimalne sigurnosti i apsolutne suverenosti.



## Resursi



### Zvanična dokumentacija




- [Specter Desktop zvanična veb stranica](https://specter.solutions/desktop/)
- [GitHub izvorni kod](https://github.com/cryptoadvance/specter-desktop)
- [Complete documentation](https://docs.specter.solutions/)



### Zajednica i podrška




- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Reddit diskusioni forum](https://reddit.com/r/specterdesktop/)
- [GitHub bug reports](https://github.com/cryptoadvance/specter-desktop/issues)