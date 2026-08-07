---
name: Actualizarea BTCPay Server
description: Aplică o actualizare de securitate pentru instanța ta BTCPay Server și rotește credențialele importante
---

![cover](assets/cover.webp)

A-ți administra propriul procesator de plăți înseamnă că ești și propria ta echipă de securitate. Când mentenanții BTCPay Server publică o versiune de securitate, nimeni nu îți va actualiza instanța în locul tău: actualizarea, verificarea și rotația credențialelor care urmează sunt responsabilitatea ta.

Acest tutorial parcurge întreaga procedură, indiferent de modul în care ai instalat BTCPay Server: verifică versiunea rulată, aplică actualizarea în funcție de tipul instalării, verifică dacă aceasta a avut efect și rotește secretele pe care un atacator le-ar fi putut obține în timp ce instanța ta era vulnerabilă.

Dacă nu ai instalat încă BTCPay Server, începe cu ghidul de instalare:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Vulnerabilitatea critică din august 2026

⚠️ **Alertă critică de securitate (7 august 2026):** o vulnerabilitate critică ce afectează BTCPay Server este exploatată activ și poate duce la pierderea fondurilor. Actualizează-ți instanța imediat la **versiunea 2.4.2** din `Admin Dashboard > Server > Maintenance > Update`, apoi verifică dacă subsolul afișează `2.4.2`. Dacă nu poți actualiza imediat, oprește-ți instanța BTCPay Server. După actualizare, trebuie de asemenea să reînnoiești complet macaroon-urile și fișierul `macaroons.db`, să reînnoiești complet șirurile de autentificare pentru orice alt backend Lightning și, dacă ai generat un portofel on-chain hot în interiorul BTCPay Server, să muți acele fonduri și să recreezi portofelul. Integratorii ar trebui de asemenea să actualizeze NBXplorer la versiunea 2.6.10. Sursă: [notele de lansare BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Versiunea 2.4.2 a fost publicată pe 7 august 2026. Notele de lansare precizează că aceasta remediază o vulnerabilitate critică deja exploatată în mediul real, raportată de `brunoerg` și `benthecarman` prin efortul Bitcoin Red Team. Aceeași versiune remediază de asemenea o eludare a autentificării cu doi factori TOTP prin autentificarea Greenfield Basic și dezactivează implicit autentificarea Greenfield Basic la cinci minute după crearea contului.

Din „exploatată activ” decurg două consecințe:

- **Actualizarea nu este opțională și nu este ceva ce poate fi programat pentru săptămâna viitoare.** O instanță neactualizată și accesibilă din internet trebuie fie actualizată, fie oprită.
- **Actualizarea nu este suficientă de una singură.** Dacă instanța ta a fost compromisă înainte să aplici remedierea, atacatorul ar putea deja deține copii ale credențialelor tale Lightning și ale oricărui material de cheie pentru portofelul hot pe care BTCPay Server l-a generat pentru tine. Aceste secrete rămân valide după actualizare până când le rotești. Secțiunea de rotație de mai jos este partea pe care oamenii o sar, și este partea care îți protejează efectiv fondurile.

## Pasul 1 — Află ce versiune rulezi

Autentifică-te în BTCPay Server și uită-te în **subsolul oricărei pagini**: șirul versiunii este afișat acolo. Poți deschide și `Admin Dashboard > Server > Maintenance`, care arată versiunea curentă și comenzile de actualizare.

Dacă instanța ta expune API-ul Greenfield, `GET /api/v1/server/info` returnează de asemenea versiunea.

Orice versiune sub `2.4.2` este vulnerabilă.

## Pasul 2 — Actualizează

### Instalare Docker auto-găzduită (instalarea standard)

Aceasta acoperă instalarea Docker oficială, care este ceea ce obții din documentația BTCPay Server, din lansatorul one-click LunaNode și din majoritatea instalărilor pe VPS.

Calea cea mai simplă este interfața web:

1. Mergi la `Admin Dashboard > Server > Maintenance`.
2. Apasă **Update**.
3. Așteaptă ca containerele să fie preluate și repornite. Interfața va fi indisponibilă câteva minute.

Dacă interfața web este inaccesibilă, sau preferi să vezi jurnalele, fă asta prin SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

La o instalare implicită, `$BTCPAY_BASE_DIRECTORY` este `/root`, deci directorul este `/root/btcpayserver-docker`. Scriptul preia cele mai recente imagini, recreează containerele și afișează versiunile rezultate.

Instalarea Docker livrează NBXplorer împreună cu BTCPay Server, deci o actualizare standard aduce și NBXplorer la versiunea recomandată `2.6.10`. Dacă rulezi NBXplorer separat — tipic pentru integratori și pentru stive personalizate — actualizează-l explicit.

### Umbrel

Deschide dashboard-ul Umbrel, mergi la **App Store**, găsește BTCPay Server și aplică actualizarea dacă este oferită una.

⚠️ **Important:** pachetele din app store sunt reambalate de echipa Umbrel și pot rămâne în urmă față de upstream cu ore sau zile. Verifică versiunea din subsolul BTCPay Server după actualizare. Dacă este încă sub `2.4.2`, **oprește aplicația** din dashboard-ul Umbrel și așteaptă versiunea ambalată, în loc să lași o instanță vulnerabilă rulând.

Ghidul Umbrel dedicat acoperă aplicația în sine:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Aceeași logică: actualizează BTCPay Server din marketplace-ul StartOS, apoi verifică versiunea din subsol. Dacă versiunea ambalată nu este încă `2.4.2`, oprește serviciul până când este.

### Găzduire administrată și de la terți

Dacă altcineva îți operează instanța (un furnizor de găzduire, o asociație, serverul unui prieten), tot ai nevoie de confirmare. Cere operatorului șirul versiunii afișat în subsol și întreabă explicit dacă rotația credențialelor de după actualizare, descrisă mai jos, a fost efectuată. „Am actualizat” nu este același răspuns cu „ți-am rotit macaroon-urile”.

## Pasul 3 — Verifică dacă actualizarea a avut efect

Reîncarcă interfața BTCPay Server și citește versiunea din subsol. Trebuie să arate `2.4.2` sau o versiune mai nouă.

Nu te baza pe faptul că derularea comenzii de actualizare s-a încheiat fără eroare: pe mașini cu resurse limitate, preluarea unei imagini poate eșua silențios și poate lăsa containerul anterior rulând. Citește versiunea, de fiecare dată.

## Pasul 4 — Rotește-ți credențialele

Acesta este pasul care transformă „actualizat” în „sigur”. Deoarece vulnerabilitatea era exploatată înainte ca remedierea să fie lansată, tratează fiecare secret deținut de instanța ta ca fiind potențial cunoscut de un atacator.

### Lightning: LND

Regenerează atât macaroon-urile, **cât și** fișierul `macaroons.db`. Ștergerea doar a fișierelor macaroon nu este suficientă — LND derivă macaroon-urile din cheia rădăcină stocată în `macaroons.db`, deci un atacator care deține o copie a unui macaroon vechi păstrează acces până când acea bază de date este recreată.

Procedura este: oprește LND, elimină `macaroons.db` și fișierele `*.macaroon` din directorul rețelei (pentru mainnet, `data/chain/bitcoin/mainnet/` în interiorul directorului de date LND), apoi repornește și deblochează LND, ceea ce le recreează. Fă mai întâi o copie de rezervă a directorului și re-asociază fiecare aplicație care folosea macaroon-urile vechi — BTCPay Server însuși, Zeus, Thunderhub, RTL, Alby și orice script pe care l-ai scris.

Dacă expui de asemenea LND pe internet, revizuiește-i în același timp certificatul TLS și orice credențiale din `lnd.conf`.

### Lightning: alte backend-uri

Orice se autentifică la nodul tău printr-un șir trebuie să primească un șir nou:

- **Core Lightning**: regenerează rune-ul sau credențialele de acces folosite de conexiune.
- **Phoenixd**: rotește parola HTTP.
- **LNbits și similare**: revocă și reemite cheile de administrator și de factură.
- **Șirurile de conexiune ale nodurilor la distanță** stocate în setările magazinului din BTCPay Server: rescrie-le cu noile secrete.

### Portofel on-chain hot generat în interiorul BTCPay Server

Dacă ai lăsat BTCPay Server să genereze un portofel on-chain pentru tine — spre deosebire de conectarea unui portofel hardware sau de importarea unui xpub ale cărui chei nu au atins niciodată serverul — acea sămânță a trăit pe mașină.

Consider-o compromisă:

1. Creează un portofel nou, ideal cu un portofel hardware, astfel încât cheile să nu mai stea niciodată pe server.
2. Transferă fondurile din portofelul vechi în cel nou.
3. Înlocuiește schema de derivare din setările magazinului cu noul portofel.
4. Nu reutiliza niciodată sămânța veche.

Configurările watch-only (xpub sau portofel hardware) nu necesită acest lucru: cheile private nu au fost niciodată pe server. Exact de aceea ghidul de instalare le recomandă.

### Conturile BTCPay Server și cheile API

Cât timp ești la asta:

- Schimbă parolele fiecărui cont de utilizator de pe instanță.
- Revocă și reemite toate **cheile API** Greenfield.
- Re-înscrie autentificarea cu doi factori, având în vedere că 2.4.2 remediază o eludare a 2FA.
- Deschide `Admin Dashboard > Server > Users` și verifică dacă nu există niciun cont neașteptat.
- Revizuiește recentele **plăți**, **pull payments** și **rambursări** pentru intrări pe care nu le-ai creat tu.
- Revizuiește webhook-urile tale și secretele lor.

## Pasul 5 — Rămâi informat pentru data viitoare

Versiunile de securitate îi ajută doar pe operatorii care aud despre ele:

- Urmărește [lansările BTCPay Server pe GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub te poate anunța prin e-mail la fiecare lansare nouă a unui depozit.
- Urmărește canalele oficiale de anunțuri ale proiectului și [blogul oficial](https://blog.btcpayserver.org/).
- Menține-ți instanța la o versiune pe care o poți actualiza rapid: cu cât rămâi mai în urmă, cu atât o actualizare de urgență devine mai dureroasă.

Auto-găzduirea îți oferă suveranitate asupra plăților tale. Costul acestei suveranități este exact acesta: să citești notele de lansare și să fii cel care aplică remedierile.
</content>
