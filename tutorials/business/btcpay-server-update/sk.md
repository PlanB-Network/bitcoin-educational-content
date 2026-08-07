---
name: Aktualizácia BTCPay Servera
description: Nasaďte bezpečnostnú aktualizáciu na svoju inštanciu BTCPay Servera a obnovte prihlasovacie údaje, na ktorých záleží
---

![cover](assets/cover.webp)

Prevádzkovať vlastnú platobnú bránu znamená byť zároveň svojím vlastným bezpečnostným tímom. Keď správcovia BTCPay Servera vydajú bezpečnostnú verziu, nikto za vás vašu inštanciu nezáplatuje: aktualizácia, jej overenie aj následná obnova prihlasovacích údajov sú na vás.

Tento návod prevádza celým postupom bez ohľadu na to, ako ste BTCPay Server nasadili: skontrolovať bežiacu verziu, vykonať aktualizáciu podľa typu nasadenia, overiť, že sa skutočne prejavila, a obnoviť tajné údaje, ktoré mohol útočník získať v čase, keď bola vaša inštancia zraniteľná.

Ak ste BTCPay Server ešte nenasadili, začnite inštalačným návodom:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Kritická zraniteľnosť z augusta 2026

⚠️ **Kritické bezpečnostné upozornenie (7. augusta 2026):** kritická zraniteľnosť postihujúca BTCPay Server je aktívne zneužívaná a môže viesť k strate prostriedkov. Okamžite aktualizujte svoju inštanciu na **verziu 2.4.2** cez `Admin Dashboard > Server > Maintenance > Update` a potom overte, že sa v pätičke zobrazuje `2.4.2`. Ak nemôžete aktualizovať hneď, svoj BTCPay Server vypnite. Po aktualizácii musíte tiež kompletne obnoviť svoje macaroons a súbor `macaroons.db`, kompletne obnoviť overovacie reťazce akéhokoľvek ďalšieho Lightning backendu, a ak ste vnútri BTCPay Servera vygenerovali horúcu on-chain peňaženku, presuňte z nej prostriedky a peňaženku vytvorte nanovo. Integrátori by mali zároveň aktualizovať NBXplorer na verziu 2.6.10. Zdroj: [Poznámky k vydaniu BTCPay Servera 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Verzia 2.4.2 bola vydaná 7. augusta 2026. Poznámky k vydaniu uvádzajú, že opravuje kritickú zraniteľnosť, ktorá už bola v praxi zneužívaná a ktorú nahlásili `brunoerg` a `benthecarman` v rámci iniciatívy Bitcoin Red Team. To isté vydanie zároveň opravuje obídenie dvojfaktorového overovania TOTP cez Basic autentifikáciu Greenfield a vo východiskovom nastavení Basic autentifikáciu Greenfield päť minút po vytvorení účtu zakazuje.

Z označenia „aktívne zneužívaná“ vyplývajú dva dôsledky:

- **Aktualizácia nie je voliteľná a nedá sa naplánovať na budúci týždeň.** Nezáplatovaná inštancia dostupná z internetu musí byť buď aktualizovaná, alebo vypnutá.
- **Aktualizácia sama o sebe nestačí.** Ak bola vaša inštancia kompromitovaná skôr, než ste ju záplatovali, útočník už možno drží kópie vašich Lightning prihlasovacích údajov aj kľúčového materiálu akejkoľvek horúcej peňaženky, ktorú pre vás BTCPay Server vygeneroval. Tieto tajné údaje zostávajú po aktualizácii platné, kým ich neobnovíte. Sekcia o obnove prihlasovacích údajov nižšie je tá, ktorú ľudia preskakujú, a pritom práve ona vaše prostriedky skutočne chráni.

## Krok 1 — Zistite, akú verziu prevádzkujete

Prihláste sa do svojho BTCPay Servera a pozrite sa na **pätičku ľubovoľnej stránky**: je v nej zobrazený reťazec s verziou. Môžete tiež otvoriť `Admin Dashboard > Server > Maintenance`, kde uvidíte aktuálnu verziu aj ovládacie prvky aktualizácie.

Ak vaša inštancia vystavuje Greenfield API, verziu vráti aj `GET /api/v1/server/info`.

Čokoľvek nižšie než `2.4.2` je zraniteľné.

## Krok 2 — Aktualizujte

### Vlastné nasadenie cez Docker (štandardná inštalácia)

Týka sa to oficiálneho nasadenia cez Docker, teda toho, čo dostanete podľa dokumentácie BTCPay Servera, z one-click spúšťača LunaNode a z väčšiny inštalácií na VPS.

Najjednoduchšia cesta vedie cez webové rozhranie:

1. Prejdite na `Admin Dashboard > Server > Maintenance`.
2. Kliknite na **Update**.
3. Počkajte, kým sa kontajnery stiahnu a reštartujú. Rozhranie bude niekoľko minút nedostupné.

Ak je webové rozhranie nedostupné alebo si radšej chcete pozrieť logy, urobte to cez SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Pri predvolenej inštalácii je `$BTCPAY_BASE_DIRECTORY` rovné `/root`, takže adresár je `/root/btcpayserver-docker`. Skript stiahne najnovšie obrazy, znovu vytvorí kontajnery a vypíše výsledné verzie.

Nasadenie cez Docker prináša NBXplorer spolu s BTCPay Serverom, takže štandardná aktualizácia povýši aj NBXplorer na odporúčanú verziu `2.6.10`. Ak prevádzkujete NBXplorer samostatne — čo je typické pre integrátorov a vlastné zostavy — aktualizujte ho výslovne.

### Umbrel

Otvorte nástenku Umbrelu, prejdite do **App Store**, nájdite BTCPay Server a nasaďte aktualizáciu, ak je ponúkaná.

⚠️ **Dôležité:** balíky z app store prebaľuje tím Umbrelu a môžu za upstreamom zaostávať o hodiny až dni. Po aktualizácii skontrolujte verziu v pätičke BTCPay Servera. Ak je stále nižšia než `2.4.2`, **zastavte aplikáciu** z nástenky Umbrelu a počkajte na zabalené vydanie, namiesto toho, aby ste nechali bežať zraniteľnú inštanciu.

Samotnej aplikácii sa venuje osobitný návod pre Umbrel:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Rovnaká logika: aktualizujte BTCPay Server z marketplace StartOS a potom overte verziu v pätičke. Ak zabalená verzia ešte nie je `2.4.2`, službu zastavte, kým nebude.

### Spravovaný a hosting tretích strán

Ak vašu inštanciu prevádzkuje niekto iný (poskytovateľ hostingu, združenie, server kamaráta), potvrdenie potrebujete aj tak. Vypýtajte si od prevádzkovateľa reťazec s verziou zobrazený v pätičke a výslovne sa opýtajte, či bola vykonaná obnova prihlasovacích údajov po aktualizácii, ktorá je opísaná nižšie. „Aktualizovali sme“ nie je tá istá odpoveď ako „obnovili sme vaše macaroons“.

## Krok 3 — Overte, že sa aktualizácia skutočne prejavila

Znovu načítajte rozhranie BTCPay Servera a prečítajte si verziu v pätičke. Musí ukazovať `2.4.2` alebo vyššiu.

Nespoliehajte sa na to, že príkaz aktualizácie skončil bez chyby: na strojoch s obmedzenými zdrojmi môže sťahovanie obrazu zlyhať potichu a nechať bežať predchádzajúci kontajner. Prečítajte si verziu, zakaždým.

## Krok 4 — Obnovte svoje prihlasovacie údaje

Toto je ten krok, ktorý mení „záplatované“ na „bezpečné“. Keďže zraniteľnosť bola zneužívaná ešte pred vydaním opravy, považujte každý tajný údaj, ktorý vaša inštancia držala, za potenciálne známy útočníkovi.

### Lightning: LND

Znovu vygenerujte macaroons **aj** súbor `macaroons.db`. Zmazať iba súbory s macaroons nestačí — LND odvodzuje macaroons z koreňového kľúča uloženého v `macaroons.db`, takže útočník, ktorý drží kópiu starého macaroonu, si prístup udrží, kým túto databázu znovu nevytvoríte.

Postup je nasledovný: zastavte LND, odstráňte z adresára siete súbor `macaroons.db` a súbory `*.macaroon` (pre mainnet ide o `data/chain/bitcoin/mainnet/` vnútri dátového adresára LND), potom LND reštartujte a odomknite, čím sa znovu vytvoria. Najprv si adresár zazálohujte a znovu spárujte každú aplikáciu, ktorá staré macaroons používala — samotný BTCPay Server, Zeus, Thunderhub, RTL, Alby aj všetky skripty, ktoré ste napísali.

Ak navyše vystavujete LND do internetu, prejdite si zároveň aj jeho TLS certifikát a všetky prihlasovacie údaje v `lnd.conf`.

### Lightning: ostatné backendy

Čokoľvek, čo sa voči vášmu uzlu overuje nejakým reťazcom, musí dostať nový reťazec:

- **Core Lightning**: znovu vygenerujte rune alebo prístupové údaje používané daným pripojením.
- **Phoenixd**: obnovte HTTP heslo.
- **LNbits a podobné**: odvolajte a znovu vydajte admin a invoice kľúče.
- **Pripojovacie reťazce vzdialených uzlov** uložené v nastaveniach obchodu v BTCPay Serveri: prepíšte ich novými tajnými údajmi.

### Horúca on-chain peňaženka vygenerovaná vnútri BTCPay Servera

Ak ste nechali BTCPay Server, aby vám vygeneroval on-chain peňaženku — na rozdiel od pripojenia hardvérovej peňaženky alebo importu xpubu, ktorého kľúče sa servera nikdy nedotkli — potom bol tento seed na danom stroji.

Považujte ho za spálený:

1. Vytvorte novú peňaženku, ideálne hardvérovú, aby už kľúče na serveri nikdy neležali.
2. Preveďte prostriedky zo starej peňaženky do novej.
3. Nahraďte derivačnú schému v nastaveniach obchodu novou peňaženkou.
4. Nikdy starý seed znovu nepoužívajte.

Sledovacie (watch-only) konfigurácie — xpub alebo hardvérová peňaženka — to nepotrebujú: súkromné kľúče na serveri nikdy neboli. Presne preto ich inštalačný návod odporúča.

### Účty a API kľúče BTCPay Servera

Keď už pri tom ste:

- Zmeňte heslá všetkých používateľských účtov na inštancii.
- Odvolajte a znovu vydajte všetky **API kľúče** Greenfield.
- Znovu nastavte dvojfaktorové overovanie, keďže verzia 2.4.2 opravuje obídenie 2FA.
- Otvorte `Admin Dashboard > Server > Users` a skontrolujte, či neexistuje žiadny neočakávaný účet.
- Prejdite si nedávne **výplaty** (payouts), **pull payments** a **vratky** (refunds) a hľadajte položky, ktoré ste nevytvorili.
- Skontrolujte svoje webhooky a ich tajné kľúče.

## Krok 5 — Zostaňte informovaní pre nabudúce

Bezpečnostné vydania pomôžu len tým prevádzkovateľom, ktorí sa o nich dozvedia:

- Sledujte [vydania BTCPay Servera na GitHube](https://github.com/btcpayserver/btcpayserver/releases) — GitHub vám môže poslať e-mail pri každom novom vydaní repozitára.
- Odoberajte oznamovacie kanály projektu a [oficiálny blog](https://blog.btcpayserver.org/).
- Udržujte svoju inštanciu na verzii, ktorú dokážete rýchlo aktualizovať: čím väčší máte sklz, tým bolestivejšia bude núdzová aktualizácia.

Vlastný hosting vám dáva suverenitu nad vašimi platbami. Cenou za túto suverenitu je presne toto: čítať poznámky k vydaniu a byť tým, kto záplatuje.
