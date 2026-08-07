---
name: Ažuriranje BTCPay Server-a
description: Primenite bezbednosno ažuriranje na svoju BTCPay Server instancu i rotirajte akreditive koji su bitni
---

![cover](assets/cover.webp)

Pokretanje sopstvenog procesora plaćanja znači da ste ujedno i sopstveni bezbednosni tim. Kada održavaoci BTCPay Server-a objave bezbednosno izdanje, niko neće zakrpiti vašu instancu umesto vas: ažuriranje, provera i rotacija akreditiva koja sledi na vama su da ih izvedete.

Ovaj vodič vas vodi kroz celu proceduru, bez obzira na to kako ste postavili BTCPay Server: provera pokrenute verzije, primena ažuriranja na vašem tipu instalacije, provera da je ono zaista primenjeno i rotacija tajni koje je napadač mogao da prisvoji dok je vaša instanca bila ranjiva.

Ako još niste postavili BTCPay Server, počnite sa vodičem za instalaciju:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Kritična ranjivost iz avgusta 2026.

⚠️ **Kritično bezbednosno upozorenje (7. avgust 2026):** kritična ranjivost koja pogađa BTCPay Server se aktivno zloupotrebljava i može dovesti do gubitka sredstava. Odmah ažurirajte svoju instancu na **verziju 2.4.2** putem `Admin Dashboard > Server > Maintenance > Update`, a zatim proverite da li podnožje stranice prikazuje `2.4.2`. Ako ne možete odmah da ažurirate, ugasite svoj BTCPay Server. Nakon ažuriranja, morate takođe u potpunosti osvežiti svoje macaroons i svoj `macaroons.db`, u potpunosti osvežiti autentifikacione stringove svakog drugog Lightning backend-a, a ako ste unutar BTCPay Server-a generisali „vruć" on-chain novčanik, prebacite ta sredstva i ponovo kreirajte novčanik. Integratori bi takođe trebalo da ažuriraju NBXplorer na verziju 2.6.10. Izvor: [Napomene uz izdanje BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Verzija 2.4.2 objavljena je 7. avgusta 2026. U napomenama uz izdanje stoji da ona ispravlja kritičnu ranjivost koja je već bila zloupotrebljavana u praksi, a koju su prijavili `brunoerg` i `benthecarman` u okviru inicijative Bitcoin Red Team. Isto izdanje takođe ispravlja zaobilaženje TOTP dvofaktorske autentifikacije putem Greenfield Basic autentifikacije i podrazumevano onemogućava Greenfield Basic autentifikaciju pet minuta nakon kreiranja naloga.

Iz „aktivno se zloupotrebljava" slede dve posledice:

- **Ažuriranje nije opciono i nije nešto što se zakazuje za sledeću nedelju.** Nezakrpljena instanca koja je dostupna sa interneta mora biti ili ažurirana ili ugašena.
- **Samo ažuriranje nije dovoljno.** Ako je vaša instanca bila kompromitovana pre nego što ste je zakrpili, napadač možda već poseduje kopije vaših Lightning akreditiva i svakog materijala ključeva vrućeg novčanika koji je BTCPay Server generisao za vas. Te tajne ostaju važeće i nakon ažuriranja, sve dok ih ne rotirate. Odeljak o rotaciji u nastavku je deo koji ljudi preskaču, a upravo je to deo koji zaista štiti vaša sredstva.

## Korak 1 — Utvrdite koju verziju koristite

Prijavite se na svoj BTCPay Server i pogledajte **podnožje bilo koje stranice**: tamo je prikazan string sa verzijom. Možete i otvoriti `Admin Dashboard > Server > Maintenance`, gde se vide trenutna verzija i kontrole za ažuriranje.

Ako vaša instanca izlaže Greenfield API, `GET /api/v1/server/info` takođe vraća verziju.

Sve ispod `2.4.2` je ranjivo.

## Korak 2 — Ažurirajte

### Samostalno hostovana Docker instalacija (standardna instalacija)

Ovo se odnosi na zvaničnu Docker instalaciju, onu koju dobijate iz dokumentacije BTCPay Server-a, preko LunaNode pokretača u jednom kliku i kod većine VPS instalacija.

Najjednostavniji put je veb interfejs:

1. Idite na `Admin Dashboard > Server > Maintenance`.
2. Kliknite na **Update**.
3. Sačekajte da se kontejneri preuzmu i ponovo pokrenu. Interfejs će biti nedostupan nekoliko minuta.

Ako je veb interfejs nedostupan ili radije želite da vidite logove, uradite to preko SSH-a:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Pri podrazumevanoj instalaciji `$BTCPAY_BASE_DIRECTORY` je `/root`, pa je direktorijum `/root/btcpayserver-docker`. Skripta preuzima najnovije image-e, ponovo kreira kontejnere i ispisuje dobijene verzije.

Docker instalacija isporučuje NBXplorer zajedno sa BTCPay Server-om, pa standardno ažuriranje dovodi i NBXplorer na preporučenu verziju `2.6.10`. Ako NBXplorer pokrećete odvojeno — što je uobičajeno kod integratora i prilagođenih stekova — ažurirajte ga izričito.

### Umbrel

Otvorite Umbrel kontrolnu tablu, idite na **App Store**, pronađite BTCPay Server i primenite ažuriranje ako je ponuđeno.

⚠️ **Važno:** pakete iz app store-a prepakuje Umbrel tim i oni mogu satima ili danima kasniti za originalnim izdanjem. Nakon ažuriranja proverite verziju u podnožju BTCPay Server-a. Ako je i dalje ispod `2.4.2`, **zaustavite aplikaciju** iz Umbrel kontrolne table i sačekajte prepakovano izdanje umesto da ostavite ranjivu instancu pokrenutu.

Namenski vodič za Umbrel pokriva samu aplikaciju:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Ista logika: ažurirajte BTCPay Server sa StartOS marketplace-a, a zatim proverite verziju u podnožju. Ako prepakovana verzija još nije `2.4.2`, zaustavite servis dok ne bude.

### Upravljani hosting i hosting kod trećih strana

Ako vašom instancom upravlja neko drugi (hosting provajder, udruženje, prijateljev server), i dalje vam je potrebna potvrda. Zatražite od operatora string sa verzijom prikazan u podnožju i izričito pitajte da li je izvršena rotacija akreditiva nakon ažuriranja, opisana u nastavku. „Ažurirali smo" nije isti odgovor kao „rotirali smo vaše macaroons".

## Korak 3 — Proverite da je ažuriranje zaista primenjeno

Ponovo učitajte interfejs BTCPay Server-a i pročitajte verziju u podnožju. Mora prikazivati `2.4.2` ili noviju.

Nemojte se oslanjati na to što se komanda za ažuriranje završila bez greške: na mašinama sa ograničenim resursima preuzimanje image-a može tiho da ne uspe i ostavi prethodni kontejner pokrenut. Pročitajte verziju, svaki put.

## Korak 4 — Rotirajte svoje akreditive

Ovo je korak koji „zakrpljeno" pretvara u „bezbedno". Pošto je ranjivost bila zloupotrebljavana i pre nego što je ispravka objavljena, tretirajte svaku tajnu koju je vaša instanca čuvala kao potencijalno poznatu napadaču.

### Lightning: LND

Ponovo generišite macaroons **i** datoteku `macaroons.db`. Brisanje samo macaroon datoteka nije dovoljno — LND izvodi macaroons iz korenog ključa smeštenog u `macaroons.db`, pa napadač koji poseduje kopiju starog macaroon-a zadržava pristup sve dok se ta baza podataka ponovo ne kreira.

Procedura je sledeća: zaustavite LND, uklonite `macaroons.db` i `*.macaroon` datoteke iz direktorijuma mreže (za mainnet, `data/chain/bitcoin/mainnet/` unutar LND direktorijuma sa podacima), zatim ponovo pokrenite i otključajte LND, koji ih iznova kreira. Prvo napravite rezervnu kopiju direktorijuma i ponovo uparite svaku aplikaciju koja je koristila stare macaroons — sam BTCPay Server, Zeus, Thunderhub, RTL, Alby i svaku skriptu koju ste napisali.

Ako LND izlažete i na internet, istovremeno preispitajte njegov TLS sertifikat i sve akreditive u `lnd.conf`.

### Lightning: ostali backend-ovi

Sve što se vašem čvoru autentifikuje pomoću stringa mora dobiti novi string:

- **Core Lightning**: ponovo generišite rune ili akreditive za pristup koje veza koristi.
- **Phoenixd**: rotirajte HTTP lozinku.
- **LNbits i slični**: opozovite i ponovo izdajte admin i invoice ključeve.
- **Stringovi za povezivanje sa udaljenim čvorom** sačuvani u podešavanjima prodavnice u BTCPay Server-u: prepišite ih novim tajnama.

### Vrući on-chain novčanik generisan unutar BTCPay Server-a

Ako ste dozvolili BTCPay Server-u da za vas generiše on-chain novčanik — za razliku od povezivanja hardverskog novčanika ili uvoza xpub-a čiji ključevi nikada nisu dodirnuli server — taj seed je živeo na toj mašini.

Smatrajte ga kompromitovanim:

1. Kreirajte novi novčanik, po mogućstvu sa hardverskim novčanikom, kako se ključevi više nikada ne bi nalazili na serveru.
2. Prebacite sredstva sa starog novčanika na novi.
3. Zamenite šemu izvođenja u podešavanjima prodavnice novim novčanikom.
4. Nikada ponovo ne koristite stari seed.

Watch-only konfiguracije (xpub ili hardverski novčanik) ovo ne zahtevaju: privatni ključevi nikada nisu bili na serveru. Upravo zato ih vodič za instalaciju i preporučuje.

### BTCPay Server nalozi i API ključevi

Kada ste već kod toga:

- Promenite lozinke svakog korisničkog naloga na instanci.
- Opozovite i ponovo izdajte sve Greenfield **API ključeve**.
- Ponovo podesite dvofaktorsku autentifikaciju, s obzirom na to da 2.4.2 ispravlja zaobilaženje 2FA.
- Otvorite `Admin Dashboard > Server > Users` i proverite da ne postoji nijedan neočekivani nalog.
- Pregledajte nedavne **isplate**, **pull payments** i **povraćaje sredstava** i potražite stavke koje niste vi kreirali.
- Preispitajte svoje webhook-ove i njihove tajne.

## Korak 5 — Ostanite obavešteni za sledeći put

Bezbednosna izdanja pomažu samo onim operatorima koji za njih saznaju:

- Pratite [BTCPay Server izdanja na GitHub-u](https://github.com/btcpayserver/btcpayserver/releases) — GitHub vam može poslati e-poštu pri svakom novom izdanju repozitorijuma.
- Pratite kanale za najave projekta i [zvanični blog](https://blog.btcpayserver.org/).
- Držite svoju instancu na verziji koju možete brzo ažurirati: što više zaostajete, to hitno ažuriranje postaje bolnije.

Samostalno hostovanje vam daje suverenitet nad vašim plaćanjima. Cena tog suvereniteta je upravo ovo: čitanje napomena uz izdanja i to da ste vi taj ko primenjuje zakrpe.
