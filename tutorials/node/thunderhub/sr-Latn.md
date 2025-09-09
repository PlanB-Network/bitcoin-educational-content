---
name: ThunderHub
description: Interfejs za upravljanje LND Lightning node-om
---
![cover](assets/cover.webp)



## Uvod



ThunderHub je **menadžer otvorenog koda za Lightning čvorove (LND)**, koji nudi intuitivni interfejs dostupan sa bilo kog uređaja ili pretraživača.



**Glavne karakteristike:**




- **Nadzor**: Globalni pregled stanja, kanala, transakcija, statistike usmeravanja
- **Menadžment**: Otvaranje/zatvaranje kanala, dolazna/odlazna plaćanja, balansiranje kanala
- **Integracije**: LNURL podrška, swaps putem Boltz-a, Amboss rezervna kopija
- **Responzivni interfejs**: Kompatibilan sa mobilnim, tablet i desktop uređajima sa tamnim/svetlim režimom rada



ThunderHub se lako integriše sa **Umbrel**, **Voltage**, **RaspiBlitz** i **MyNode**, pojednostavljujući svakodnevno upravljanje vašim čvorom.



**ThunderHub je posebno pogodan za operatere koji traže ergonomski interfejs za upravljanje svojim kanalima, kontrolu likvidnosti (rebalansiranje), praćenje transakcija i integraciju usluga trećih strana kao što je Amboss. Sigurnost je osigurana putem lokalne ili Tor veze.**



Ako još uvek nemate Lightning čvor, preporučujemo da pratite naš LND Umbrel vodič:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalacija



ThunderHub se može instalirati na više različitih načina, u zavisnosti od vašeg okruženja za hosting Lightning čvora. Bilo da koristite turnkey rešenje, tj. rešenje koje je već spremno za upotrebu (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, itd.) ili ručnu instalaciju, ThunderHub je često dostupan bez većih napora. U nastavku opisujemo dva uobičajena pristupa: putem Umbrel App Store-a i putem ručne instalacije (primenljivo na server ili samostalno hostovanu distribuciju).



### Instalacija putem Umbrel-a



Umbrel integriše ThunderHub u svoj **App Store**, čineći instalaciju izuzetno jednostavnom. Nema potrebe za komandnom linijom ili ručnom konfiguracijom: sve se obavlja putem Umbrel korisničkog interfejsa. Samo pratite ove korake:





- **Otvorite Umbrel kontrolnu tablu**: Povežite se sa web interfejsom vašeg Umbrel čvora (npr. `http://umbrel.local` na vašoj lokalnoj mreži, ili putem njegove `.onion` adrese ako koristite Tor).
- **Pristupite App Store-u**: U glavnom meniju Umbrel-a, kliknite na "App Store" (ili "App"). Potražite **ThunderHub** na listi dostupnih aplikacija.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Instaliraj ThunderHub**: Klikni na aplikaciju ThunderHub, zatim na dugme za instalaciju. Potvrdi ako je potrebno. Umbrel će automatski preuzeti i implementirati ThunderHub na tvoj čvor.





- **Pokrenite aplikaciju**: Kada je instalacija završena (nekoliko desetina sekundi), ThunderHub se pojavljuje na vašoj početnoj stranici. Kliknite na ikonu da je otvorite. ThunderHub se pokreće u vašem pregledaču.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Važno:** Kada se ThunderHub prvi put otvori, automatski prikazuje **podrazumevana lozinka** potrebnu za prijavu. Opcija "Ne prikazuj ovo ponovo" (na engleskom Don't show this again) omogućava vam da sakrijete ovaj prikaz za buduće konekcije. **Snažno vam savetujemo da:**




- **Odmah sačuvate ovu lozinku** u svom menadžeru lozinki
- **Kopirate** za upotrebu u sledećem koraku
- Označite "Ne prikazuj ovo ponovo" kada je lozinka sačuvana



![Page de connexion de ThunderHub](assets/fr/03.webp)



Bićete preusmereni na stranicu za prijavu, gde morate uneti lozinku koju ste kopirali u prethodnom koraku da biste otključali interfejs.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel se brine o pružanju LND informacija o vezi (TLS sertifikat, administrativni macaroon, itd.) ThunderHub-u u pozadini, tako da ne morate da radite nikakvu dodatnu konfiguraciju. U samo nekoliko klikova, imaćete ThunderHub pokrenut na vašem Umbrel čvoru.



### Ručno instaliranje (samostalno hostovano, isključujući Umbrel)



Za korisnike van Umbrel-a (npr. na ličnom serveru, Raspberry Pi sa RaspiBlitz-om ili *samostalna* instalacija), instalacija ThunderHub-a zahteva nekoliko dodatnih koraka. U nastavku opisujemo instalaciju iz izvornog koda i konfiguraciju, prema [zvaničnoj ThunderHub dokumentaciji](https://docs.thunderhub.io).



#### Instalacija



**Preduslovi:** Uverite se da vaš sistem ispunjava minimalne zahteve prema [dokumentaciji za postavljanje](https://docs.thunderhub.io/setup):




- **Node.js** verzija 18 ili viša
- **npm** instaliran
- Pristup LND autentifikacionim fajlovima :
  - LND TLS sertifikat (`tls.cert`)
  - LND administracija macaroon (`admin.macaroon`)
  - LND gRPC servis adresa (hostname:port) (podrazumevano `127.0.0.1:10009` lokalno)



**1. Preuzmite ThunderHub kod:** Klonirajte GitHub repozitorijum projekta kao što je opisano u [dokumentaciji za instalaciju](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. instalirajte zavisnosti i izgradite aplikaciju:**



```bash
npm install
npm run build
```



Ove komande instaliraju sve potrebne module, a zatim kompajliraju aplikaciju (ThunderHub je napisan u TypeScript/React).



**3. Ažuriraj kasnije:** ThunderHub nudi nekoliko metoda za buduća ažuriranja:



```bash
# Brzi način
npm run update

# Ručna metoda
git pull
npm install
npm run build
```



#### Konfiguracija (Setup)



**1. Glavna konfiguraciona datoteka:** Kreirajte `.env.local` datoteku u korenskom direktorijumu ThunderHub foldera da biste prilagodili konfiguraciju (ovo će sprečiti da vaša podešavanja budu prepisana tokom ažuriranja). Glavne promenljive prema [dokumentaciji za podešavanje](https://docs.thunderhub.io/setup):



```bash
# -----------
# Konfiguracija servera
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Konfiguracija interfejsa
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Konfiguracija za privatnost
# -----------
FETCH_PRICES=true # Preuzimanje BTC/fiat cena sa sajta Blockchain.com
FETCH_FEES=true # Preuzimanje on-chain naknada sa sajta Earn.com
DISABLE_LINKS=false # Linkovi ka sajtovima 1ml.com i Blockchain.com
NO_VERSION_CHECK=false # Provera verzije sa GitHub-a

# -----------
# TOR (opciono)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Za prosleđivanje saobraćaja preko TOR-a

# -----------
# Konfiguracija naloga
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Datoteka sa nalozima
```



**2. Konfiguracija naloga servera:** Kreirajte YAML datoteku navedenu u `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'vaša_glavna_lozinka'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'lozinka_za_određeni_nalog'
# Opcionalno: nalog sa macaroon-om u heksadecimalnom obliku
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon u HEX ili Base64 formatu
certificate: '0202045c7365...' # Sertifikat u HEX ili Base64 formatu
```



**3. Daljinski pristup:** Da biste se povezali sa udaljenim LND čvorom, dodajte u `LND.conf` :



```bash
# Option 1 : pristup preko IP adrese
tlsextraip=<pristupacna_spoljna_ip>
rpclisten=0.0.0.0:10009

# Option 2 : pristup preko domena
tlsextradomain=<pristupacan_spoljni_domen>
rpclisten=0.0.0.0:10009
```



**4. Sigurnost:** Pri prvom pokretanju, ThunderHub **automatski** skriva `masterPassword` i sve lozinke naloga u YAML fajlu, kako bi se izbeglo čuvanje lozinki u čistom tekstu na serveru.



**5. Pokreni ThunderHub:**



```bash
npm start
```



Podrazumevano, server sluša na portu 3000. Pristupite `http://localhost:3000` (ili `http://ip-serveur:3000` sa lokalne mreže).



**6. Docker alternativa:** ThunderHub nudi zvanične Docker slike:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Slika sa osnovnom putanjom /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Pojavljuje se stranica za prijavu u ThunderHub. Izaberite podešeni nalog i unesite lozinku da biste pristupili kontrolnoj tabli.



**Instalacija na drugim distribucijama:** Unapred pripremljene distribucije čvorova (RaspiBlitz, MyNode, Start9 i dr.) uglavnom nude ugrađenu podršku za ThunderHub preko svojih odgovarajućih administrativnih interfejsa.



**Za više informacija:** Pogledajte kompletnu zvaničnu dokumentaciju :




- **Instalacija:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Konfiguracija:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Ovi resursi detaljno opisuju napredne opcije kao što su SSO nalozi, šifrovani makaruni, TOR konfiguracija i još mnogo toga.



Kada je ThunderHub instaliran i dostupan, spremni ste da iskoristite sve njegove funkcije. U sledećem odeljku, pogledaćemo ThunderHub interfejs i njegove različite kartice, kako bismo vas vodili kroz njegovo korišćenje.



## Predstavljanje interfejsa



ThunderHub interfejs je strukturiran oko glavnog menija (obično prikazan u koloni sa leve strane) koji se sastoji od nekoliko ključnih sekcija. Svaka od njih odgovara određenom aspektu upravljanja vašim Lightning čvorom. Hajde da ih prođemo jednu po jednu:





- **Home** - Kartica Početna sa opštom komandnom tablom (pregled vašeg čvora i brze radnje).
- **Dashboard** - Prilagodljiva kontrolna tabla sa vidžetima i naprednim metrima.
- **Peers** - Upravljanje povezanim čvorovima u Lightning mreži (povezivanje sa drugim čvorovima).
- **Channels** - Detaljno upravljanje Lightning kanalima.
- **Rebalance** - Alat za balansiranje kanala (kružna plaćanja).
- **Transactions** - Istorija Lightning plaćanja (LN transakcije).
- **Forwards** - Statistika rutiranja (uplate prosleđene preko vašeg čvora).
- **Chain** - Node's On-Chain portfolio (On-Chain BTC: UTXO-i, transakcije).
- **Amboss** - Integracija sa Amboss-om (praćenje čvorova, bekapovi, itd.).
- **Alati** - Razni alati (bekapi, potpisane poruke, makaruni, izveštaji, itd.).
- **Swap** - On-Chain/Lightning swap funkcije putem Boltz-a.
- **Stats** - Napredna statistika i metrički podaci o performansama čvorova.



*(Napomena: U zavisnosti od verzije ThunderHub-a, neki delovi mogu imati malo drugačije naslove ili dodatne funkcije, ali opšti principi ostaju isti)*



### Početna (Opšta kontrolna tabla)



ThunderHub-ova kartica **Home** je početna stranica koja se pojavljuje nakon što se prijavite. Sadrži **General Dashboard**, koji nudi **globalni pregled** statusa vašeg Lightning čvora i predlaže **brze akcije** za rutinske operacije. Evo šta ćete obično pronaći:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Stanja i kapaciteti:** Na vrhu stranice, ThunderHub prikazuje vaše dostupne bilanse. Ovde ćete obično videti [on-chain](https://planb.network/resources/glossary/onchain) bilans (Bitcoin on-Chain u čvoru novčanika, simbolizovan sa sidrom ⚓) i Lightning bilans (kapaciteti vaših kanala, simbolizovani sa Bolt munjom ⚡). Ovo vam daje trenutni uvid u sredstva koja imate u On-Chain-u i Lightning-u. Ako imate nekoliko naloga ili kanala, proverite da li ste na pravom (npr. Mainnet vs Testnet).





- **Ključne statistike:** Kontrolna tabla može prikazati neke globalne metrike za vaš čvor - na primer, broj otvorenih kanala, broj povezanih partnera, zarađene naknade za usmeravanje (ako je primenljivo), itd. To je rezime nedavne aktivnosti i zdravlja čvora.





- **Brze radnje:** Kontrolna tabla sadrži dugmad za brzo izvršavanje najčešćih zadataka, bez potrebe za navigacijom kroz menije. Ove brze radnje uključuju :





  - **Ghost**: Postavi prilagođenu Lightning adresu putem Ambossa.
  - **Donate**: Doniraj putem Lightning-a.
  - **Login/Go To**: Povežite se sa svojim Amboss nalogom (Quick Connect) i idite direktno na Amboss.space da biste videli informacije o svom čvoru.
  - **Address** : Unesite Lightning adresu da izvršite plaćanje.
  - **Open**: Otvorite novi Lightning kanal. Klikom se otvara obrazac za unos URI-ja udaljenog čvora s kojim želite otvoriti kanal, iznos i, ako je primenljivo, maksimalnu On-Chain naknadu koja će se koristiti.
  - **Decode**: Dekodiraj Lightning fakturu ili LNURL da bi ste videli detalje pre plaćanja.
  - **LNURL**: Procesuiraj LNURL-ove za Lightning uplate ili isplate.
  - **LnMarkets Login**: Prijavite se na LnMarkets za trgovanje.



Ove brze radnje omogućavaju vam da izvršite najčešće operacije direktno sa početne stranice, bez potrebe da se krećete kroz različite kartice grafičkog interfejsa.



Ukratko, ThunderHub kontrolna tabla vam daje **brz pregled** vašeg čvora i omogućava vam da izvršite najčešće operacije (slanje/primanje, otvaranje kanala) jednim klikom. To je idealna početna tačka za svakodnevnu administraciju.



### Kontrolna tabla



Deo **Dashboard** je odvojen od "Home" kartice i nudi napredniju, prilagodljivu kontrolnu tablu. Ovaj deo vam omogućava da kreirate prilagođeni prikaz sa specifičnim widget-ima prema vašim potrebama kao operatera čvora.





- **Prilagodljivi widgeti:** Za razliku od početne stranice, koja ima fiksni raspored, kontrolna tabla vam omogućava da tačno izaberete koji elemente želite prikazati i kako da ih organizujete.



![Dashboard sans widgets activés](assets/fr/06.webp)



Ako nijedan widget nije omogućen, videćete poruku "No Widgets Enabled!" sa dugmetom "Settings" za pristup parametrima prilagođavanja.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



U podešavanjima možete birati iz širokog spektra widgeta organizovanih u kategorije: "Lightning - Info", "Lightning - Table", "Lightning - Graph", i tako dalje. Svaki widget može biti pojedinačno aktiviran ili deaktiviran pomoću dugmadi "Show/Hide", u prevodu "Prikaži/Sakrij".



![Bas de la page des paramètres](assets/fr/08.webp)



Na dnu postavki, pronaći ćete dugme "To Dashboard" za povratak na kontrolnu tablu i dugme "Reset Widgets" za resetovanje podrazumevanog prikaza.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Jednom kada je konfigurisan, vaš kontrolni panel može prikazivati različite grafikone i metrike: grafikone plaćanja putem Lightning-a, broj izdatih faktura, statistiku prosleđivanja, detaljne bilanse, itd.





- **Napredne metrike:** Pristupite detaljnijim statistikama o performansama vašeg čvora, sa grafikonima i podacima u realnom vremenu.





- **Prilagodljiv pregled:** Prilagodite prikaz prema tome da li ste povremeni korisnik ili profesionalni operater koji upravlja višestrukim rutiranim kanalima.





- **Modularni interfej:** Dodajte ili uklonite widgete po potrebi: grafikoni prosljeđivanja, metrički podaci o likvidnosti, upozorenja o zdravlju čvorova, itd.



Ovaj odeljak je posebno koristan za napredne korisnike koji žele da prate specifične metrike ili dobiju tehnički pregled svog Lightning čvora. Dopunjuje početni odeljak nudeći veću fleksibilnost i kontrolu nad načinom prikaza informacija.



### Vršnjaci



Deo **Peers** navodi sve Lightning čvorove koji su trenutno povezani sa vašim kao vršnjaci. **Peer** je direktna veza između dva čvora na Lightning mreži. Vaš čvor može biti povezan sa vršnjacima čak i bez otvorenog kanala (npr. samo za razmenu informacija na mreži), ili naravno svaki otvoreni kanal automatski podrazumeva povezanog vršnjaka.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Na kartici Peers, videćete :





- **Informacione kolone:** Interfejs prikazuje korisne detalje kao što su status sinhronizacije, tip konekcije (clearnet ili Tor), ping, primljeni/poslati satoshiji i obim razmenjenih podataka.
- **Add peer, u prevodu Dodaj vršnjaka:** ThunderHub vam omogućava ručno povezivanje sa novim vršnjakom putem dugmeta **"Add "** u gornjem desnom uglu. Trebaće vam URI čvora (format `<public_key>@<socket>`). Kada se validira, ThunderHub šalje odgovarajuću `lncli connect` komandu. Ako je čvor online i dostupan, biće dodat na vašu listu vršnjaka.



### Kanali



Kartica **Channels** je srce upravljanja Lightning kanalima. Verovatno je to deo koji ćete najčešće konsultovati. Prikazuje **sve vaše Lightning kanale** sa njihovim detaljima i omogućava vam da izvršavate upravljačke akcije na tim kanalima.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Evo šta ćete pronaći na stranici Channels:





- **Prikaz liste kanala:** Svaki otvoreni (ili otvarajući/zatvarajući) kanal je naveden, obično sa alijasom udaljenog čvora, ukupnim kapacitetom kanala i obojenom trakom koja ilustruje raspodelu lokalne naspram udaljene likvidnosti. ThunderHub koristi kodiranje bojama (često plava/zelena) ili procenat za označavanje balansa kanala: na primer, plava za vaš lokalni udeo, zelena za udaljeni udeo. Ako je kanal savršeno balansiran (50/50), traka će biti polovina svake boje. Ovo vam omogućava da na prvi pogled identifikujete koji kanali su neuravnoteženi (sve plavo = skoro sve lokalno, sve zeleno = skoro sve udaljeno).





- **Informacione kolone:** Interfejs prikazuje detaljne kolone uključujući Status, Dostupne akcije, Informacije o partneru, ID kanala, Kapacitet, Aktivnost, Naknade i Stanje sa grafičkim prikazom likvidnosti.





- **Prikaz konfiguracije:** Zupčanik u gornjem desnom uglu omogućava vam da prilagodite prikaz kanala prema vašim željama.





- **Status:** Videćete i indikatore statusa - npr. `Active` (kanal je otvoren i operativan), `Offline` (peer je isključen, tako da je kanal trenutno neupotrebljiv), `Pending` (za otvaranja ili zatvaranja koja čekaju On-Chain potvrdu).





- **Akcije na kanalu:** Za svaki kanal, ThunderHub pruža dugmad za akcije (često u obliku ikonica):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





  - **Naknade za uređivanje:** Interfejs "Update Channel Policy" vam omogućava da prilagodite sve parametre kanala: Osnovna naknada, Stopa naknade (u ppm), CLTV Delta, Maksimalni HTLC i Minimalni HTLC. Ovo vam omogućava da prilagodite svoje politike naknada pojedinačno po kanalu, sa ciljem privlačenja (ili odvraćanja) saobraćaja rutiranja. *(Napomena: ThunderHub nije zamena za automatski alat za upravljanje naknadama, ali za ručno podešavanje je veoma efikasan)*
  - **Zatvori Kanal (*Close*)**: Interfejs "Zatvori Kanal" vam daje izbor između **kooperativnog zatvaranja** (podrazumevano) ili **prisilnog zatvaranja** (*Force Close*) definišući naknade (u Sats/vByte). **Važno:** uvek preferirajte kooperativno zatvaranje kada je moguće, kako biste izbegli kašnjenja u On-Chain poravnanju i veće naknade. ThunderHub će vam reći da li je peer online (kooperativno moguće) ili ne. U slučaju prisilnog zatvaranja, budite sigurni da potvrdite jer je ovo nepovratno i pokrenuće transakciju sa vremenskim zaključavanjem (obično 144 bloka ili ~1 dan na Bitcoin Mainnet-u).
  - **Otvorite novi kanal:** Da biste otvorili novi kanal, kliknite na ikonicu zupčanika u gornjem desnom uglu stranice Channels, a zatim odaberite "Open". Zatim možete pokrenuti kanal ka novom ili postojećem partneru. Prednost korišćenja ove stranice je što imate listu vaših postojećih kanala ispred sebe, što vam može pomoći da odlučite gde da otvorite novi kanal.



Ukratko, odeljak Channels vam daje **preciznu kontrolu nad svakim kanalom**. Ovde upravljate alokacijom likvidnosti, odlučujete koje kanale da zadržite ili zatvorite i postavljate parametre rutiranja po kanalu. ThunderHub nudi jasan interfejs za ove ključne operacije upravljanja čvorovima.



### Rebalansiraj



Kartica **Rebalance** je posvećena **balansiranju kanala**. Balansiranje (ili *rebalansiranje*) podrazumeva ponovno podešavanje raspodele sredstava između vaših odlaznih i dolaznih kanala, pravljenjem **kružnog plaćanja** sa jednog od vaših kanala na drugi vaš kanal, preko Lightning mreže. Ovo vam omogućava, bez unošenja novih sredstava, da prebacite likvidnost iz kanala koji je prepun u kanal koji je previše prazan, čineći vaše kanale korisnijim (izbalansiran kanal može i slati i primati uplate).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub uveliko olakšava ovu operaciju, koja bi inače bila zamorna na komandnoj liniji. Evo kako koristiti odeljak za Rebalansiranje:





- **Početni prikaz kanala:** Prilikom ulaska u Rebalance, ThunderHub prikazuje listu vaših kanala, sa indikatorom balansa za svaki (slično kao na stranici Channels). Odmah možete videti koji kanali su van balansa. ThunderHub može sortirati kanale po rastućem balansu, tako da najnebalansiraniji kanali budu na vrhu liste (0.0 znači potpuno lokalni ili udaljeni).





- **Izbor partnera:** Interfejs olakšava izbor odlaznih i dolaznih partnera za ponovno balansiranje.





- **Postavke parametara:** Možete postaviti :
  - Maksimalna naknada (u Sats i ppm) koju ste spremni platiti
  - Iznos za ponovno balansiranje sa opcijom "Fiksno" ili "Ciljano"
  - **Čvorovi koje treba izbegavati** prilikom rutiranja
  - **Maksimalno vreme probe** za pronalaženje rute





- Odaberite **source**** kanal: Prvo odaberite **outgoing (source)** kanal, tj. kanal iz kojeg imate previše lokalne likvidnosti za premeštanje. U praksi, to je kanal gde je vaš lokalni udeo visok (> 50%). Zamislimo kanal A sa 1,000,000 Sats-a, od kojih je 900,000 lokalno - dobar kandidat za slanje Sats-a na drugo mesto. Klikom na ovaj kanal A kao "outgoing", ThunderHub ga označava kao izvor.





- Izaberite **ciljni kanal****: Zatim izaberite **dolazni (ciljni)** kanal koji treba da primi likvidnost. Obično će to biti kanal gde je situacija obrnuta - većina sredstava je na udaljenoj strani (npr. samo 100,000 lokalnih Sats-a od 1,000,000). ThunderHub, kada je izvorni kanal izabran, će sortirati ostale kanale u obrnutom redosledu (opadajući saldo) kako bi pomogao u identifikaciji najkomplementarnijih kanala. Izaberite B kanal koji ima prostora na lokalnoj strani. ThunderHub će tada jasno prikazati koja dva kanala su izabrana (izvor A i cilj B).





- **Postavite iznos naknade i toleranciju:** Obrazac vam omogućava unos:





  - Količina **za ponovno balansiranje** (u Sats). Često biramo količinu koja bi izbalansirala oba kanala na \~50/50. ThunderHub može unapred popuniti polovinu viška kapaciteta izvornog kanala, na primer.
  - **Maksimalna naknada** koju ste spremni da platite za ovu operaciju (opciono). Ova naknada je izražena u Sats (ukupni trošak kružnog rutiranja). Ako ostavite prazno, ThunderHub će tražiti put bez obzira na trošak, što generalno nije preporučljivo (bolje je postaviti limit, npr. 10 Sats za malo balansiranje, ili maksimalni ppm).





- **Pronađi rutu:** Kliknite na dugme da pronađete rutu. ThunderHub pita LND da izračuna rutu od vašeg izvornog kanala kroz mrežu do vašeg ciljanog kanala. Ako pronađe moguću rutu koja zadovoljava vaše kriterijume naknade, prikazuje je sa detaljima o skokovima i troškovima naknade. Na primer, može naznačiti da je pronašao putanju sa 3 skoka sa ukupno 2 Sats u troškovima.





- **Pokreni ponovno balansiranje:** Ako ste zadovoljni predloženom rutom, kliknite na **Balance Channel**. ThunderHub će tada pokrenuti kružno plaćanje putem LND. Ako plaćanje bude uspešno, videćete obaveštenje o uspehu, a balans kanala A i B će biti izmenjen u realnom vremenu. ThunderHub će ažurirati indikator balansa za ove kanale (idealno bi bilo da budu zeleniji nego pre, što ukazuje na bolji balans).





- **Prilagođavanja i iteracije:** Ako ruta nije pronađena pri prvom pokušaju (ili ako je preskupa), možete prilagoditi parametre :





  - Pokušajte sa manjim iznosom (ponekad delimično rebalansiranje prođe dok veliki iznos ne uspe).
  - Postepeno povećavajte maksimalnu naknadu, ali pazite da ne platite više u naknadama nego što vredi.
  - Koristite dugme **Get Another Route**, ako je dostupno, da pokušate alternativu.
  - Pokušajte sa drugim parom kanala ako stvari postanu zaista teške.



ThunderHub čini proces veoma **intuitivnim i vizuelnim**. U samo 4 koraka (izaberite izlazni kanal, izaberite ulazni kanal, iznos, validirajte), možete uraditi ono što je ranije zahtevalo složene manuelne komande. Alat je neprocenjiv za održavanje dobro balansiranog čvora, poboljšavajući vaše performanse rutiranja i iskustvo (lakše slanje i primanje uplata preko svih vaših kanala).



Konačno, imajte na umu da ponovno balansiranje podrazumeva troškove usmeravanja (plaćene posredničkim čvorovima), tako da je to **investicija** za učiniti vaš čvor fluidnijim. Koristite je mudro, na primer za podršku kanalu ka usluzi koju često koristite (dolazna likvidnost) ili za balansiranje velikog kanala za usmeravanje. ThunderHub vam omogućava da to uradite **jednostavno i efikasno**.



### Transakcije



Sekcija **Transactions** u ThunderHub-u odgovara istoriji **Lightning** transakcija vašeg čvora, tj. uplate i fakture plaćene ili primljene putem kanala. To je neka vrsta izveštaja o stanju računa za vaše LN operacije.



![Historique des transactions Lightning](assets/fr/14.webp)



U ovoj kartici ćete pronaći :





- **Grafikon faktura:** U gornjem desnom uglu, grafikon prikazuje evoluciju primljenih faktura tokom vremena, omogućavajući vam da vizualizujete aktivnost vašeg čvora.





- Hronološka lista svih Lightning transakcija napravljenih *od* ili *do* vašeg čvora. Svaki unos može prikazati:





  - Tip operacije: **poslata uplata** (odlazna uplata) ili **primljena uplata** (dolazna, putem uplaćene fakture).
  - Iznos u Sats.
  - Datum/vreme.
  - ID plaćanja (Hash ili RHash pre-image) ili komentar (ako ste dodali belešku uz fakturu).
  - Status: **završeno**, ili moguće **u toku**/*neuspešno* (npr. uplata koja čeka rešavanje, ali generalno LND ovo brzo obrađuje, tako da ovde ima malo "na čekanju" u poređenju sa On-Chain transakcijama).



Ukratko, odeljak Transakcije služi kao vaš **LN dnevnik aktivnosti**. Veoma je koristan za proveru da li je uplata prošla, koliko je koštala naknada ili za praćenje istorije vaših Lightning razmena. U kombinaciji sa odeljkom Forwards (opisan sledeće), imaćete potpun pregled novca koji je prošao kroz vaš čvor.



### Forwards



Kartica **Forwards** posvećena je aktivnosti **rutiranja** vašeg čvora, tj. plaćanjima koja **prolaze** kroz vaše kanale (kada delujete kao posrednički čvor na Lightning mreži). Ako upravljate svojim čvorom kao ruting čvorom, ovo je važan deo za praćenje vašeg učinka.



![Statistiques de routage Lightning](assets/fr/15.webp)



U sekciji Forwards, ThunderHub predstavlja:





- **Filteri i opcije prikaza:** U gornjem desnom uglu, filteri vam omogućavaju da sortirate podatke po danu/nedelji/mesecu/godini, i da birate između grafičkog ili tabelarnog prikaza.





- **Poruka aktivnosti:** Ako nije izvršeno rutiranje tokom izabranog perioda, interfejs prikazuje poruku "Nema prosleđivanja za ovaj period", na engleskom "No forwards for this period", kao što je prikazano u ovom primeru.





- **Tabela nedavnih prosleđivanja:** svaki unos odgovara uplati koja je prosleđena kroz vaš čvor. Za svako prosleđivanje, obično vidimo:





  - Vremensku oznaku,
  - iznos koji je rutiran (u satoshijima),
  - naknada zarađena na ovom prosleđivanju (u Sats, ovo je razlika između onoga što ste primili na dolaznom kanalu i poslali na odlaznom),
  - korišćeni dolazni i odlazni kanali (često identifikovani po aliasu partnera ili ID-u kanala).
  - status (uobičajeno završen ("completed") ili neuspeh ("failure") ako prosleđivanje nije uspelo tokom rute).





- **Prikupljene statistike**: ThunderHub izračunava i prikazuje na vrhu stranice ukupne vrednosti i statistike za dati period (npr. poslednjih 24 sata, ili 7 dana, itd., ponekad podesivo).



Ukratko, odeljak Forwards (u prevodu prosleđivanje) nudi **pregled u realnom vremenu aktivnosti rutiranja vašeg Lightning čvora**. U kombinaciji sa odeljcima Kanali i Rebalansiranje, ovo čini kompletan paket za optimizaciju vašeg čvora: Kanali/Rebalans za likvidnost, Prosleđivanje za posmatranje rezultata (tokova i profita).



### Lanac (eng. Chain)



Sekcija **Chain** odgovara upravljanju portfoliom on-chain bitcoina vašeg LND čvora. Ovaj interfejs vam omogućava da pregledate i upravljate Bitcoin fondovima, koji se koriste za otvaranje kanala ili primanje sredstava iz zatvorenih kanala.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



U Chainu, naći ćete :





- **On-Chain stanje:** Prikazuje ukupno BTC stanje dostupno u LND novčaniku.





- **Lista UTXO-a:** Pogledaj sve nepotrošene izlaze (UTXO) sa iznosom, potvrde, adrese i format za svaki izlaz.





- **Istorija transakcija:** Detaljna tabela svih Bitcoin transakcija sa tipom (ulaz/izlaz), datumom, iznosom, naknadama, potvrdama, blokom uključivanja, adresama i txid.



### Amboss



ThunderHub se integriše sa platformom **Amboss** (amboss.space), koja nudi detaljne informacije o Lightning čvorovima, tržištu likvidnosti i korisne funkcije kao što su šifrovana rezervna kopija kanala i praćenje dostupnosti.



![Intégration Amboss avec ses options](assets/fr/17.webp)



U ThunderHub-u, odeljak Amboss omogućava vam da **povežete** vaš čvor sa vašim Amboss nalogom:





- **Ghost adresa:** Postavite **personalizovanu Lightning adresu** za vaš čvor, čime se olakšava primanje uplata.





- **Automatske rezervne kopije kanala:** Vodeća funkcija za **šifrovane rezervne kopije kanala** (SCB datoteke) na Amboss-u. Aktivirajte **Amboss Auto Backup = Yes** u podešavanjima da automatski šaljete ažuriranja šifrovanih rezervnih kopija svaki put kada promenite kanale. U slučaju kvara, moći ćete da povratite svoja sredstva zahvaljujući ovoj eksternoj rezervnoj kopiji.





- **Provere zdravlja:** Aktiviraj **Amboss Healthcheck = Da** kako bi tvoj čvor slao redovne pingove Amboss-u. Dobijaćeš obaveštenja ako tvoj čvor izgleda kao da je van mreže.





- **Ostale funkcije:** Automatsko slanje stanja, **Magma/Hydro** integracija (tržište likvidnosti), i pristup detaljnim statističkim podacima o performansama.



Amboss integracija dodaje esencijalni **nivo zaštite** sa automatskim eksternim backup-om i praćenjem dostupnosti, dostupno direktno iz ThunderHub-a.



### Alati



Sekcija **Alati** okuplja razne napredne alate za upravljanje vašim čvorom. Evo glavnih elemenata:



![Interface des outils disponibles](assets/fr/18.webp)





- **Backups (rezervne kopije):** Ručno upravljajte rezervnim kopijama vaših kanala (SCB). ThunderHub vam omogućava da **preuzmete kompletnu rezervnu kopiju** vaših kanala (opcija "Backup all channels -> Download"). Čuvajte ovu datoteku `channel-all.bak` na sigurnom mestu - ona je ključna za povrat vaših sredstava u slučaju pada sistema. Takođe možete **uvesti** rezervnu kopiju prilikom ponovnog postavljanja čvora.





- **Računovodstvo:** Alat za izvoz finansijskih izveštaja uključujući zarađene/plaćene naknade i obime usmerene tokom datog perioda.
- **Potpisane poruke:** **Potpišite ili verifikujte poruke** sa svojim čvorom kako biste dokazali Ownership vašeg Lightning čvora putem kriptografske potpise.
- **Makroni (Pekara sekcija):** Upravljajte LND** makronima kako biste kreirali prilagođeni pristup. Interface "Pekara" vam omogućava da precizno odaberete svaku dozvolu: "Dodaj ili ukloni Peers", "Kreiraj Lančane Adrese", "Kreiraj Fakture", "Kreiraj Makrone", "Izvedi Ključeve", "Dobij Pristupne Ključeve", "Dobij Lančane Transakcije", "Dobij Fakture", "Dobij Wallet Info", "Dobij Uplate", "Dobij Peers", "Plati Fakture", "Poništi Pristupne Id-ove", "Pošalji na Lančane Adrese", "Potpiši bajtove", "Potpiši Poruke", "Zaustavi daemon", "Verifikuj potpis bajtova", "Verifikuj poruke", i tako dalje. Svaka dozvola može biti aktivirana pojedinačno sa "Da/Ne" dugmadima kako bi se kreirao makron po meri.
- **Informacije o sistemu:** Prikaz verzije novčanika i aktiviranih RPC-ova.



Ukratko, odeljak Alati objedinjuje napredne administrativne funkcije - bekapove, računovodstvo, bezbednost i upravljanje pristupom - u jedinstvenom interfejsu.



### Swap (zamena)



ThunderHub-ova kartica **Swap** omogućava vam zamenu Lightning satoshija za on-chain bitcoine putem Boltz servisa. Ova funkcija je korisna za „prebacivanje” viška Lightning likvidnosti u kanal bez njegovog zatvaranja.


![Interface de swap via Boltz](assets/fr/19.webp)



Proces je jednostavan:





- **Iznos**: Definišite iznos za razmenu
- **Adresa** : Unesite Bitcoin prijemnu adresu
- **Izvršenje**: ThunderHub komunicira sa Boltz-om kako bi automatski izvršila razmena



**Prednosti:**




- Bez posredničkog držanja sredstava 
- Sačuvajte svoje postojeće kanale
- Jednostavan integrisani interfejs za korišćenje



Boltz naplaćuje malu proviziju, ali plaćate i standardnu Bitcoin naknadu za transakciju. ThunderHub prikazuje sve troškove pre potvrde.



### Statistika



ThunderHubova sekcija **Statistika** nudi **napredne statistike** o vašem Lightning čvoru za analizu performansi i optimizaciju rutiranja.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Ovaj odeljak je ključan za optimizaciju vaših troškova, identifikaciju uspešnih kanala i planiranje širenja vašeg čvora.



## Zaključak



**ThunderHub** se etablirao kao neophodan alat za jednostavnu administraciju Lightning čvora **LND**. Ovaj moderni interfejs nudi sve osnovne funkcije: upravljanje kanalima, plaćanja, nadgledanje, sa naprednim funkcijama kao što su automatsko balansiranje i integracija sa Amboss-om.



**Ključne prednosti:**




- Elegantan i intuitivan interfejs
- Snažni alati (ponovno balansiranje, Boltz swaps, automatske sigurnosne kopije)
- Kompatibilan sa Umbrel-om, Voltage-om, RaspiBlitz-om i drugim distribucijama



ThunderHub demokratizuje napredno upravljanje Lightning čvorovima, čineći dostupnim ono što je ranije zahtevalo složene tehničke komande. Bilo da ste početnik ili iskusni operater, ThunderHub vam omogućava efikasno upravljanje vašim Lightning čvorom putem modernog, sveobuhvatnog korisničkog interfejsa.



## Resursi



**Zvanični linkovi:**




- Zvanična veb stranica:** [thunderhub.io](https://thunderhub.io)
- Dokumentacija:** [docs.thunderhub.io](https://docs.thunderhub.io)
- Izvorni kod na GitHub-u:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)
