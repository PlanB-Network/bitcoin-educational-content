---
name: BTCPay Serveri uuendamine
description: Rakendage oma BTCPay Serveri instantsile turvauuendus ja vahetage välja olulised juurdepääsuandmed
---

![cover](assets/cover.webp)

Oma makseprotsessori haldamine tähendab, et olete ühtlasi ka iseenda turvameeskond. Kui BTCPay Serveri hooldajad avaldavad turvaväljalaske, ei paika keegi teie instantsi teie eest: uuendamine, kontrollimine ja sellele järgnev juurdepääsuandmete vahetamine on teie ülesanne.

See õpetus juhatab teid läbi kogu protseduuri, olenemata sellest, kuidas te BTCPay Serveri kasutusele võtsite: kontrollige töötavat versiooni, rakendage uuendus vastavalt oma paigaldusviisile, veenduge, et see tõepoolest jõustus, ning vahetage välja saladused, mille ründaja võis kätte saada ajal, mil teie instants oli haavatav.

Kui te ei ole BTCPay Serverit veel kasutusele võtnud, alustage paigaldusjuhendist:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## 2026. aasta augusti kriitiline haavatavus

⚠️ **Kriitiline turvahoiatus (7. august 2026):** BTCPay Server'it mõjutavat kriitilist haavatavust kuritarvitatakse aktiivselt ja see võib kaasa tuua rahaliste vahendite kaotuse. Uuenda oma instants viivitamatult **versioonile 2.4.2** kaudu `Admin Dashboard > Server > Maintenance > Update` ning kontrolli seejärel, et jaluses kuvatakse `2.4.2`. Kui sa ei saa kohe uuendada, lülita oma BTCPay Server välja. Pärast uuendamist pead täielikult uuendama ka oma macaroons'id ja `macaroons.db`, täielikult uuendama kõigi teiste Lightning-taustasüsteemide autentimisstringid ning juhul, kui lõid BTCPay Server'i sees kuuma on-chain rahakoti, tuleb need vahendid mujale liigutada ja rahakott uuesti luua. Integreerijad peaksid uuendama ka NBXplorer'i versioonile 2.6.10. Allikas: [BTCPay Server 2.4.2 väljalaskemärkmed](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Versioon 2.4.2 avaldati 7. augustil 2026. Väljalaskemärkmete kohaselt parandab see kriitilise haavatavuse, mida juba aktiivselt kuritarvitati ja millest teatasid `brunoerg` ja `benthecarman` Bitcoin Red Teami algatuse kaudu. Sama väljalase parandab ka TOTP-põhise kaheastmelise autentimise möödahiilimise Greenfieldi Basic-autentimise kaudu ning keelab Greenfieldi Basic-autentimise vaikimisi viis minutit pärast konto loomist.

Väljendist „aktiivselt kuritarvitatav" tuleneb kaks järeldust:

- **Uuendamine ei ole valikuline ega midagi, mille võiks järgmisse nädalasse planeerida.** Paikamata instants, mis on internetist ligipääsetav, tuleb kas uuendada või välja lülitada.
- **Ainuüksi uuendamisest ei piisa.** Kui teie instants sattus rünnaku alla enne paikamist, võivad ründajal juba olla koopiad teie Lightningi juurdepääsuandmetest ja igasugusest kuuma rahakoti võtmematerjalist, mille BTCPay Server teie jaoks genereeris. Need saladused jäävad ka pärast uuendamist kehtima seni, kuni te need välja vahetate. Allpool olev vahetamise jaotis on see osa, mille inimesed vahele jätavad, ja just see osa kaitseb tegelikult teie raha.

## 1. samm — Tehke kindlaks, millist versiooni te kasutate

Logige oma BTCPay Serverisse sisse ja vaadake **mis tahes lehe jalust**: versioonistring kuvatakse seal. Võite avada ka `Admin Dashboard > Server > Maintenance`, kus on näha praegune versioon ja uuendamise juhtnupud.

Kui teie instants avab Greenfieldi API, tagastab ka `GET /api/v1/server/info` versiooni.

Kõik, mis on vanem kui `2.4.2`, on haavatav.

## 2. samm — Uuendage

### Isehostitav Dockeri paigaldus (standardpaigaldus)

See hõlmab ametlikku Dockeri paigaldust, mille saate BTCPay Serveri dokumentatsioonist, LunaNode'i ühe klikiga käivitajast ja enamikust VPS-paigaldustest.

Kõige lihtsam tee on veebiliides:

1. Minge `Admin Dashboard > Server > Maintenance`.
2. Klõpsake **Update**.
3. Oodake, kuni konteinerid alla laaditakse ja taaskäivitatakse. Liides on mõne minuti jooksul kättesaamatu.

Kui veebiliides ei ole kättesaadav või soovite pigem logisid näha, tehke seda SSH kaudu:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Vaikepaigalduses on `$BTCPAY_BASE_DIRECTORY` väärtuseks `/root`, seega on kataloogiks `/root/btcpayserver-docker`. Skript laadib alla uusimad tõmmised, loob konteinerid uuesti ja väljastab saadud versioonid.

Dockeri paigaldus sisaldab BTCPay Serveri kõrval ka NBXplorerit, seega viib standardne uuendus NBXploreri samuti soovitatud versioonile `2.6.10`. Kui te käitate NBXplorerit eraldi — mis on tavaline integreerijate ja kohandatud lahenduste puhul —, tuleb see eraldi uuendada.

### Umbrel

Avage Umbreli töölaud, minge **App Store'i**, leidke BTCPay Server ja rakendage uuendus, kui see on saadaval.

⚠️ **Tähtis:** App Store'i pakette pakendab ümber Umbreli meeskond ja need võivad algallikast tunde või päevi maha jääda. Kontrollige pärast uuendamist versiooni BTCPay Serveri jaluses. Kui see on endiselt vanem kui `2.4.2`, **peatage rakendus** Umbreli töölaual ja oodake pakendatud väljalaset, selle asemel et jätta haavatav instants tööle.

Umbreli eraldi juhend käsitleb rakendust ennast:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Sama loogika: uuendage BTCPay Serverit StartOS-i turuplatsilt ja kontrollige seejärel versiooni jaluses. Kui pakendatud versioon ei ole veel `2.4.2`, peatage teenus seniks, kuni see on.

### Hallatav ja kolmanda osapoole majutus

Kui teie instantsi haldab keegi teine (majutusteenuse pakkuja, ühendus, sõbra server), vajate ikkagi kinnitust. Küsige haldajalt jaluses kuvatavat versioonistringi ja küsige otsesõnu, kas allpool kirjeldatud uuendusjärgne juurdepääsuandmete vahetamine on tehtud. „Me uuendasime" ei ole sama vastus mis „me vahetasime teie macaroon'id välja".

## 3. samm — Veenduge, et uuendus tõepoolest jõustus

Laadige BTCPay Serveri liides uuesti ja lugege versioon jalusest. See peab näitama `2.4.2` või uuemat.

Ärge lootke sellele, et uuenduskäsk lõpetas töö veata: piiratud ressurssidega masinates võib tõmmise allalaadimine vaikselt ebaõnnestuda ja jätta eelmise konteineri tööle. Lugege versiooni, iga kord.

## 4. samm — Vahetage välja oma juurdepääsuandmed

See on samm, mis muudab „paigatud" olekuks „turvaline". Kuna haavatavust kuritarvitati juba enne paranduse ilmumist, käsitlege iga saladust, mida teie instants hoidis, kui ründajale potentsiaalselt teadaolevat.

### Lightning: LND

Genereerige uuesti nii macaroon'id **kui ka** fail `macaroons.db`. Ainuüksi macaroon-failide kustutamisest ei piisa — LND tuletab macaroon'id `macaroons.db`-s hoitavast juurvõtmest, seega säilitab vana macaroon'i koopiat omav ründaja ligipääsu seni, kuni see andmebaas on uuesti loodud.

Toiming on järgmine: peatage LND, eemaldage võrgukataloogist (mainneti puhul `data/chain/bitcoin/mainnet/` LND andmekataloogi sees) `macaroons.db` ja `*.macaroon` failid, seejärel taaskäivitage ja avage LND lukk, mis loob need uuesti. Tehke kataloogist enne varukoopia ning siduge uuesti kõik rakendused, mis vanu macaroon'e kasutasid — BTCPay Server ise, Zeus, Thunderhub, RTL, Alby ja kõik teie kirjutatud skriptid.

Kui te avate LND ka internetile, vaadake samal ajal üle selle TLS-sertifikaat ja kõik `lnd.conf`-is olevad juurdepääsuandmed.

### Lightning: muud taustasüsteemid

Kõik, mis autendib end teie sõlmes stringi abil, peab saama uue stringi:

- **Core Lightning**: genereerige uuesti rune või ühenduse kasutatavad juurdepääsuandmed.
- **Phoenixd**: vahetage välja HTTP-parool.
- **LNbits ja sarnased**: tühistage ja väljastage uuesti admin- ja arvevõtmed.
- **Kaugsõlme ühendusstringid**, mis on salvestatud BTCPay Serveri poe seadetes: kirjutage need uute saladustega üle.

### BTCPay Serveri sees loodud kuum on-chain rahakott

Kui lasksite BTCPay Serveril endale on-chain rahakoti genereerida — erinevalt riistvaralise rahakoti ühendamisest või sellise xpub'i importimisest, mille võtmed ei puutunud kunagi serverisse —, siis asus see seed masinas.

Lugege see põletatuks:

1. Looge uus rahakott, ideaalis riistvaralise rahakotiga, et võtmed ei asuks enam kunagi serveris.
2. Kandke vahendid vanast rahakotist uude.
3. Asendage poe seadetes tuletusskeem uue rahakotiga.
4. Ärge kasutage vana seed'i enam kunagi.

Vaatamisrežiimis seadistused (xpub või riistvaraline rahakott) seda ei vaja: privaatvõtmed ei olnud kunagi serveris. Just seetõttu paigaldusjuhend neid soovitabki.

### BTCPay Serveri kontod ja API võtmed

Kui te juba sellega tegelete:

- Muutke instantsi iga kasutajakonto paroole.
- Tühistage ja väljastage uuesti kõik Greenfieldi **API võtmed**.
- Registreerige kaheastmeline autentimine uuesti, arvestades, et 2.4.2 parandab 2FA möödahiilimise.
- Avage `Admin Dashboard > Server > Users` ja kontrollige, et ühtegi ootamatut kontot ei oleks.
- Vaadake üle hiljutised **väljamaksed**, **pull payment'id** ja **tagasimaksed**, otsides kirjeid, mida te ise ei loonud.
- Vaadake üle oma webhook'id ja nende saladused.

## 5. samm — Olge järgmiseks korraks kursis

Turvaväljalasked aitavad ainult neid haldajaid, kes neist kuulevad:

- Jälgige [BTCPay Serveri väljalaskeid GitHubis](https://github.com/btcpayserver/btcpayserver/releases) — GitHub saab teile iga hoidla uue väljalaske kohta e-kirja saata.
- Jälgige projekti teavituskanaleid ja [ametlikku blogi](https://blog.btcpayserver.org/).
- Hoidke oma instants versioonil, mida saate kiiresti uuendada: mida rohkem te maha jääte, seda valulisemaks hädauuendus muutub.

Isehostimine annab teile suveräänsuse oma maksete üle. Selle suveräänsuse hind on täpselt see: väljalaskemärkmete lugemine ja see, et paikaja olete teie.
