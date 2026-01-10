---
name: Specter Desktop
description: Upravljajte svojim Bitcoin portfolijima sa više potpisa u potpunom suverenitetu sa svojim čvorom
---

![cover](assets/cover.webp)



Specter Desktop je aplikacija otvorenog koda (MIT licenca) koju razvija Cryptoadvance od 2019. godine i koja olakšava upravljanje Bitcoin novčanicima sa vašim hardverskim novčanicima (Ledger, Trezor, Coldcard, BitBox02, Passport, itd.) i vašom sopstvenom Bitcoin infrastrukturom (Bitcoin Core čvor ili Electrum server). Aplikacija se posebno ističe u konfiguracijama sa više potpisa, omogućavajući vam da osigurate velike sume raspodelom moći potpisivanja između nekoliko nezavisnih hardverskih novčanika.



**U ovom vodiču ćete naučiti kako da:**




- Instalirajte i konfigurišite Specter Desktop na vašem računaru (Windows, macOS ili Linux)
- Povežite Specter sa Electrum serverom (u ovom primeru ćemo koristiti Umbrel)
- Kreiraj jednostavan wallet sa wallet hardverom (Coldcard)
- Primajte i šaljite bitkoine sa potpunim suverenitetom
- Postavljanje 2-na-3 multisignature wallet sa nekoliko hardverskih novčanika
- Instalirajte Specter na Umbrel server (napredni bonus)



Sve vaše transakcije će biti validirane lokalno putem vaše sopstvene infrastrukture, bez prenosa bilo kakvih informacija na eksterne servere, garantujući vašu poverljivost i finansijski suverenitet. Uvek proverite transakcije na vašem wallet hardverskom ekranu pre potpisivanja.



## Preuzimanje i instalacija



Posetite zvaničnu veb stranicu Specter Desktop-a da biste preuzeli aplikaciju.



![Page d'accueil Specter](assets/fr/01.webp)



Na stranici za preuzimanje, izaberite verziju koja odgovara vašem operativnom sistemu: macOS, Windows ili Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Kada se preuzme, instalirajte aplikaciju prema uobičajenim uputstvima vašeg operativnog sistema. Za macOS, prevucite ikonu u Applications. Za Windows, pokrenite instalacioni program. Za Linux, pratite uputstva za paket.



## Početna konfiguracija



Prilikom prvog pokretanja, Specter Desktop vas pita da izaberete tip konekcije. Možete se povezati na Electrum server ili na sopstveni Bitcoin Core čvor.



![Choix du type de connexion](assets/fr/03.webp)



U ovom primeru, koristićemo konekciju na Electrum server koji radi na Umbrel-u.



Za više informacija, pogledajte naš Umbrel vodič:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Ova opcija nudi bržu sinhronizaciju od Bitcoin Core. Ako želite, možete odabrati "Bitcoin Core" i konfigurisati vezu sa vašim lokalnim čvorom. Sledeći koraci ostaju isti bez obzira na vaš izbor.



Odaberite "Electrum Connection" zatim izaberite "Enter my own" da biste konfigurisali svoj sopstveni Electrum server.



![Configuration Electrum](assets/fr/04.webp)



Unesite adresu vašeg Electrum servera. U našem slučaju sa Umbrel-om, adresa će biti `umbrel.local` sa portom `50001`. Kliknite na "Connect" da uspostavite vezu.



Kada se povežete, pojavljuje se početni ekran sa kontrolnom listom za početak. Sada treba da dodate svoje hardverske novčanike.



![Écran d'accueil](assets/fr/05.webp)



## Dodavanje wallet hardvera



U levom meniju kliknite na "Add device" da dodate vaš wallet hardver.



Specter Desktop podržava brojne hardverske novčanike: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault i mnoge druge.



Ako želite da saznate više, pogledajte naše tutorijale za hardver wallet.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Izaberite svoj wallet hardver. U ovom primeru, koristimo Coldcard MK4.



Ispod ćete pronaći naš vodič za ovaj wallet hardver:



https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Za Coldcard, potrebno je da izvezete javne ključeve sa wallet hardvera ili putem USB veze ili microSD kartice.



![Import des clés du Coldcard](assets/fr/07.webp)



Pratite instrukcije prikazane za izvoz ključeva sa vašeg Coldcard-a. Dajte svom wallet hardveru ime (ovde "MK4 Tuto"). Kada ključevi budu uvezeni, možete kreirati wallet sa jednim ključem, ili dodati druge hardverske novčanike za multi-potpisni wallet.



![Dispositif ajouté](assets/fr/08.webp)



## Kreiranje portfolija



Nakon dodavanja vašeg wallet hardvera, kliknite na "Create single key wallet" da biste kreirali wallet sa jednim potpisom.



Dajte svom portfoliju ime (npr. "Wallet za tuto") i izaberite tip adrese. Izaberite "Segwit" da koristite native bech32 adrese koje optimizuju troškove transakcija.



![Configuration du portefeuille](assets/fr/09.webp)



Kada vaš portfelj bude kreiran, Specter nudi da sačuva rezervnu PDF datoteku koja sadrži sve javne informacije potrebne za obnovu vašeg portfelja (deskriptore, proširene javne ključeve). Ova datoteka ne sadrži vaše privatne ključeve.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Primite bitkoine



Da biste primili bitkoine, izaberite svoj wallet u meniju sa leve strane, zatim kliknite na karticu "Receive".



Specter automatski generiše novu adresu za prijem sa QR kodom.



![Génération d'une adresse de réception](assets/fr/11.webp)



Možete kopirati adresu ili skenirati QR kod. Uvek proverite adresu na vašem wallet hardverskom ekranu pre nego što je prosledite bilo kome.



## Prikaži istoriju i adrese



Kada primite bitkoine, možete pregledati svoje transakcije u kartici "Transakcije".



![Historique des transactions](assets/fr/12.webp)



Kartica "Adrese" omogućava vam da pregledate sve adrese generisane vašim portfoliom, sa njihovim statusom korišćenja i povezanim iznosima.



![Liste des adresses](assets/fr/13.webp)



## Pošalji bitkoine



Da biste poslali bitkoine, kliknite na karticu "Send". Unesite adresu primaoca, iznos koji želite poslati i proverite napredne opcije ako želite ručno da izaberete UTXO-ove (kontrola novčića).



![Création d'une transaction](assets/fr/14.webp)



Kliknite na "Create Unsigned Transaction" da biste napravili transakciju. Specter će zatim tražiti da potpišete transakciju sa vašim wallet hardverom.



![Signature de la transaction](assets/fr/15.webp)



Ako koristite Coldcard, imaćete izbor potpisivanja putem USB-a ili korišćenjem microSD kartice (air-gapped). Potvrdite transakciju na vašem wallet hardverskom ekranu, pažljivo proveravajući adresu odredišta i iznos.



Kada je transakcija potpisana, možete je emitovati na Bitcoin mreži.



![Options de diffusion](assets/fr/16.webp)



Kliknite na "Send transaction" da pošaljete transakciju. Specter će potvrditi da je vaša transakcija poslata, a njen status možete pratiti u kartici Transakcije.



![Diffusion de la transaction](assets/fr/17.webp)



## Kreiranje i korišćenje portfolija sa više potpisa



Jedna od glavnih prednosti Specter Desktop-a je njegova sposobnost da pojednostavi upravljanje portfeljima sa više potpisa. Multisig wallet zahteva nekoliko potpisa za autorizaciju transakcije, čime se eliminiše jedinstvena tačka kvara. Na primer, konfiguracija 2-na-3 zahteva dva potpisa sa tri odvojena hardverska novčanika da bi se potvrdio bilo koji trošak.



Da biste kreirali multisig wallet, počnite dodavanjem svih hardverskih novčanika za potpisivanje putem opcije "Dodaj uređaj". U ovom primeru, koristićemo tri različita hardverska novčanika: Coldcard MK4 (već ranije dodat), Passport i Ledger. Ova diverzifikacija proizvođača jača sigurnost izbegavanjem zavisnosti od jednog lanca snabdevanja ili firmvera.



Evo linkova ka Ledger i Passport uputstvima:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Dodajte Passport tako što ćete imenovati wallet hardver (npr. "Passport multi") i uvesti njegove ključeve putem microSD kartice ili QR koda. Zatim kliknite na "Nastavi" da nastavite.



![Ajout du Passport](assets/fr/23.webp)



Zatim dodajte Ledger povezivanjem putem USB-a i otvaranjem aplikacije Bitcoin na hardveru wallet. Imenujte ga (npr. "ledger multi") i kliknite na "Get via USB" zatim "Continue" da biste uvezli njegove javne ključeve.



![Ajout du Ledger](assets/fr/24.webp)



Kada registrujete svoja tri hardverska novčanika u Specter-u, kliknite na "Add wallet" i izaberite opciju "Multiple Signature" da biste kreirali multi-signature wallet.



![Choix du type de wallet](assets/fr/25.webp)



Odaberite tri hardverska novčanika koja želite uključiti u svoj multisignature kvorum: MK4 Tuto, Passport multi i ledger multi. Kliknite na "Nastavi" da biste prešli na sledeći korak.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Izaberite vašu konfiguraciju sa više potpisa. Izaberite "Segwit" kao tip adrese da biste imali koristi od optimizovanih naknada. Parametar "Potrebni potpisi za autorizaciju transakcija (m od 3)" vam omogućava da definišete prag: za konfiguraciju 2-od-3, potrebna su 2 potpisa. Svaki wallet hardver prikazuje svoj odgovarajući multisig ključ. Kliknite na "Kreiraj wallet" da završite kreiranje.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Vaš "Multi tuto" portfelj sa višestrukim potpisom je sada kreiran. Specter odmah preporučuje da sačuvate rezervnu PDF datoteku koja sadrži opis portfelja. Kliknite na "Sačuvaj rezervni PDF" da preuzmete ovu kritičnu datoteku.



![Wallet multisig créé](assets/fr/28.webp)



Specter takođe omogućava izvoz wallet informacija na svaki od vaših hardverskih novčanika putem QR koda ili fajla. Ovo omogućava određenim hardverskim novčanicima (kao što su Coldcard ili Passport) da direktno u svojoj memoriji čuvaju multisig konfiguraciju.



Za pasoš, otključajte svoj uređaj, zatim idite na "Upravljanje nalogom" > "Poveži Wallet" > "Specter" > "Multisig" > "QR kod", zatim skenirajte QR kod generisan od strane Specter-a. Vaš pasoš će zatim tražiti da skenirate adresu za primanje sa vašeg wallet kako biste potvrdili multisig konfiguraciju.



Za MK4, priključite ga na svoj PC i otključajte. Zatim kliknite na "Save MK4 Tuto file" i sačuvajte datoteku na vaš MK4. Sledeći put kada potpišete svoj wallet hardver, MK4 će koristiti ovu datoteku za završetak konfiguracije multisig-a.



![Export vers les hardware wallets](assets/fr/29.webp)



Za vašu informaciju, možete pristupiti rezervnim kopijama u bilo kom trenutku iz kartice "Postavke" vašeg portfolija, zatim "Izvoz":



![Accès au backup PDF](assets/fr/30.webp)



Svakodnevna upotreba ostaje slična jednostavnom wallet: vi generate primate adrese kao i obično. Da biste poslali bitkoine, idite na karticu "Pošalji", unesite adresu primaoca i iznos, a zatim kliknite na "Kreiraj nepotpisanu transakciju".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter gradi PSBT (Partially Signed Bitcoin Transaction) i prikazuje "Acquired 0 of 2 signatures". Sada morate potpisati sa najmanje dva od vaša tri hardverska novčanika. Kliknite na prvi wallet hardver (npr. "MK4 Tuto") da potpišete sa vašim Coldcard, zatim na drugi (npr. "Passport multi") da dobijete drugi potrebni potpis.



![Signature de la transaction](assets/fr/32.webp)



Kada dobijete 2 potrebna potpisa (interfejs prikazuje "Acquired 2 of 2 signatures" i "Transaction is ready to send"), kliknite na "Send Transaction" da emitujete transakciju na Bitcoin mreži.



![Transaction prête à être diffusée](assets/fr/33.webp)



Ovaj pristup sa više potpisa posebno je pogodan za kompanije (nekoliko menadžera treba da odobri troškove), porodice (zaštita višegeneracijskog nasleđa) ili pojedince koji upravljaju velikim sumama (geografska distribucija hardverskih novčanika za otpornost na lokalizovane katastrofe).



### Kritična važnost rezervnih kopija sa višestrukim potpisom



**Imajte na umu**: pravljenje rezervne kopije multisig portfolija je suštinski različito od pravljenja rezervne kopije pojedinačnog portfolija. Vaše fraze za oporavak (seed fraze) same po sebi nisu dovoljne za vraćanje multisig portfolija. Morate takođe napraviti rezervnu kopiju **output descriptor** (output descriptor), koja sadrži informacije o konfiguraciji vašeg multisig portfolija.



output descriptor uključuje osnovne podatke: proširene javne ključeve (xpubs) svakog potpisnika, prag potpisa (2-od-3 u našem primeru), tip skripte koja se koristi (native, nested ili legacy Segwit), i zaobilazne putanje za svaki wallet hardver. Bez ovog deskriptora, čak i ako imate dve od tri fraze za oporavak, nećete moći da obnovite svoj wallet ili pristupite svojim bitcoinima. Deskriptor omogućava vašem softveru da zna kako da kombinuje javne ključeve za generate Bitcoin adrese koje odgovaraju vašim sredstvima.



Specter Desktop automatski generiše rezervnu PDF datoteku kada kreirate svoj multisig portfelj. Ovaj PDF sadrži kompletan deskriptor, otiske prstiju svakog wallet hardvera i sve javne informacije potrebne za obnovu. **Ova datoteka ne sadrži vaše privatne ključeve** i stoga sama po sebi ne omogućava trošenje vaših bitkoina, ali omogućava svakome ko joj pristupi da vidi vašu kompletnu istoriju transakcija i stanje.



Da biste pravilno napravili rezervnu kopiju vaše multisignature konfiguracije, pratite ovu proceduru: nakon kreiranja vašeg portfolija, kliknite na karticu "Settings", zatim "Export" i odaberite "Save Backup PDF". Napravite nekoliko kopija ovog PDF-a: odštampajte najmanje dve kopije na papiru, a takođe sačuvajte i šifrovanu digitalnu kopiju. Čuvajte jednu kopiju PDF-a sa svakom od vaših fraza za oporavak, na geografski odvojenim lokacijama.



Ugravirajte svoje fraze za oporavak na vatrootporne i vodootporne metalne ploče kako biste osigurali njihovu dugovečnost. Nikada ne potcenjujte važnost ovih rezervnih kopija: ako izgubite fasciklu `~/.specter` na vašem računaru I izgubite jedan od vaših hardverskih novčanika bez rezervne kopije deskriptora, sva vaša sredstva će biti nepovratno izgubljena, čak i sa konfiguracijom 2-od-3. Redundancija sa više potpisa štiti od gubitka wallet hardvera, ali samo ako ste ispravno napravili rezervnu kopiju deskriptora vašeg wallet.



## Prednosti i ograničenja Specter Desktop



**Prednosti**: Optimalna poverljivost sa potpunom lokalnom validacijom bez servera trećih strana. Fleksibilnost višestrukog potpisa za napredne konfiguracije (korporativne, porodične, individualne). Opsežna podrška za hardver wallet sa potpunom interoperabilnošću (USB i bez mrežnog povezivanja).



**Ograničenja**: Značajna kriva učenja na naprednim Bitcoin konceptima (UTXO-i, deskriptori, putanje derivacije).



## Najbolje prakse



Uvek proverite adrese i iznose na vašem wallet hardverskom ekranu pre validacije, kako biste se zaštitili od malvera.



Čuvajte PDF rezervne kopije odvojeno od vaših semena. Ovi javni opisi mogu se čuvati u sefu banke ili šifrovanom oblaku, olakšavajući oporavak bez izlaganja vaših privatnih ključeva.



Testirajte oporavak na token iznosima pre korišćenja vaših portfolija sa velikim fondovima. Kreirajte, testirajte, obrišite i vratite da biste potvrdili vaše procedure.



Ažurirajte Specter i vaš firmware redovno. Rasporedite vaše multi-signature ko-potpisnike geografski (kuća/kancelarija/blizina) kako biste izdržali lokalizovane katastrofe. Koristite opisne oznake kako biste olakšali računovodstvo i poreske prijave.



## Bonus: Instalacija na Bitcoin server (Umbrel, RaspiBlitz, Start9)



Ako već posedujete Bitcoin server kao što su Umbrel, RaspiBlitz, MyNode ili Start9, možete instalirati Specter Desktop direktno iz njihove prodavnice aplikacija. Ovaj pristup nudi nekoliko značajnih prednosti: aplikacija se automatski konfiguriše sa vašim lokalnim Bitcoin Core čvorom, ostaje dostupna 24/7 putem web interfejsa sa bilo kog uređaja na vašoj mreži, a možete joj čak pristupiti sigurno na daljinu putem Tor-a. Cela vaša Bitcoin infrastruktura je centralizovana na jednom posvećenom serveru, što pojednostavljuje upravljanje i jača vašu suverenost.



### Instalacija iz Umbrel prodavnice aplikacija



Sa vašeg Umbrel interfejsa, idite u App Store i potražite Specter Desktop. Kliknite na "Install" da pokrenete instalaciju.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Kada je instalacija završena, otvorite Specter Desktop na vašem Umbrelu. Ekran dobrodošlice će vas zamoliti da izaberete tip konekcije. Ako koristite Specter na vašem Umbrelu, kliknite na "Update settings" da konfigurišete konekciju.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Odaberite "Remote Specter USB connection" da omogućite korišćenje USB hardverskih novčanika povezanih na vaš lokalni računar dok koristite Specter na udaljenom Umbrel serveru.



![Configuration Remote Specter USB](assets/fr/20.webp)



Pratite prikazana uputstva za konfigurisanje HWI Bridge-a. Potrebno je da pristupite podešavanjima uređaja bridge i dodate domen `http://umbrel.local:25441` na belu listu. Kliknite na "Update" da sačuvate konfiguraciju.



![HWI Bridge Settings](assets/fr/21.webp)



Ako biste takođe želeli da koristite svoje USB hardverske novčanike sa lokalnog računara, preuzmite Specter Desktop aplikaciju na svoj uređaj i postavite je na "Da, pokrećem Specter daljinski". Kliknite na "Sačuvaj" da završite konfiguraciju.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Zaključak



Specter Desktop demokratizuje napredne Bitcoin konfiguracije, čineći multisignature pristupačnim bez žrtvovanja vaše suverenosti ili poverljivosti. Za korisnike koji upravljaju značajnim količinama novca, pretvara institucionalne prakse u rešenja koja mogu primeniti privatni pojedinci.



Iako aplikacija zahteva početno ulaganje u infrastrukturu i učenje, nudi potpunu suverenost: kontrolu nad infrastrukturom za validaciju, fizičko vlasništvo nad ključevima i transakcije bez nadzora trećih strana. Bilo da ste pojedinac koji osigurava svoju ušteđevinu, porodica koja stvara sef za više generacija ili kompanija koja upravlja novčanim tokom, Specter Desktop je referentni alat za usklađivanje maksimalne sigurnosti i apsolutne suverenosti.



## Resursi



### Zvanična dokumentacija




- [Specter Desktop zvanična veb stranica](https://specter.solutions/desktop/)
- [GitHub izvorni kod](https://github.com/cryptoadvance/specter-desktop)
- [Complete documentation](https://docs.specter.solutions/)



### Zajednica i podrška




- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Reddit discussion forum](https://reddit.com/r/specterdesktop/)
- [GitHub bug reports](https://github.com/cryptoadvance/specter-desktop/issues)