---
name: Aktualizace BTCPay Serveru
description: Nasaďte bezpečnostní aktualizaci na svou instanci BTCPay Serveru a obnovte přihlašovací údaje, na kterých záleží
---

![cover](assets/cover.webp)

Provozovat vlastní platební bránu znamená být zároveň svým vlastním bezpečnostním týmem. Když správci BTCPay Serveru vydají bezpečnostní verzi, nikdo za vás vaši instanci nezáplatuje: aktualizace, její ověření i následná obnova přihlašovacích údajů jsou na vás.

Tento návod provádí celým postupem, ať už jste BTCPay Server nasadili jakkoli: zkontrolovat běžící verzi, provést aktualizaci podle typu nasazení, ověřit, že se skutečně projevila, a obnovit tajné údaje, které mohl útočník získat v době, kdy byla vaše instance zranitelná.

Pokud jste BTCPay Server ještě nenasadili, začněte instalačním návodem:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Kritická zranitelnost ze srpna 2026

⚠️ **Kritické bezpečnostní upozornění (7. srpna 2026):** kritická zranitelnost postihující BTCPay Server je aktivně zneužívána a může vést ke ztrátě prostředků. Okamžitě aktualizujte svou instanci na **verzi 2.4.2** přes `Admin Dashboard > Server > Maintenance > Update` a poté ověřte, že se v patičce zobrazuje `2.4.2`. Pokud nemůžete aktualizovat ihned, svůj BTCPay Server vypněte. Po aktualizaci musíte také kompletně obnovit své macaroons a soubor `macaroons.db`, kompletně obnovit ověřovací řetězce jakéhokoli dalšího Lightning backendu, a pokud jste uvnitř BTCPay Server vygenerovali horkou on-chain peněženku, přesuňte z ní prostředky a peněženku vytvořte znovu. Integrátoři by měli rovněž aktualizovat NBXplorer na verzi 2.6.10. Zdroj: [Poznámky k vydání BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Verze 2.4.2 byla vydána 7. srpna 2026. Poznámky k vydání uvádějí, že opravuje kritickou zranitelnost, která už byla v praxi zneužívána a kterou nahlásili `brunoerg` a `benthecarman` v rámci iniciativy Bitcoin Red Team. Stejné vydání zároveň opravuje obejití dvoufaktorového ověřování TOTP přes Basic autentizaci Greenfield a ve výchozím nastavení Basic autentizaci Greenfield pět minut po vytvoření účtu zakazuje.

Z označení „aktivně zneužívána“ plynou dva důsledky:

- **Aktualizace není volitelná a nedá se naplánovat na příští týden.** Nezáplatovaná instance dostupná z internetu musí být buď aktualizována, nebo vypnuta.
- **Aktualizace sama o sobě nestačí.** Pokud byla vaše instance kompromitována dříve, než jste ji záplatovali, útočník už možná drží kopie vašich Lightning přihlašovacích údajů i klíčového materiálu jakékoli horké peněženky, kterou pro vás BTCPay Server vygeneroval. Tyto tajné údaje zůstávají po aktualizaci platné, dokud je neobnovíte. Sekce o obnově přihlašovacích údajů níže je ta, kterou lidé přeskakují, a přitom právě ona vaše prostředky skutečně chrání.

## Krok 1 — Zjistěte, jakou verzi provozujete

Přihlaste se do svého BTCPay Serveru a podívejte se na **patičku libovolné stránky**: je v ní zobrazen řetězec s verzí. Můžete také otevřít `Admin Dashboard > Server > Maintenance`, kde uvidíte aktuální verzi i ovládací prvky aktualizace.

Pokud vaše instance vystavuje Greenfield API, verzi vrátí i `GET /api/v1/server/info`.

Cokoli nižšího než `2.4.2` je zranitelné.

## Krok 2 — Aktualizujte

### Vlastní nasazení přes Docker (standardní instalace)

Týká se to oficiálního nasazení přes Docker, tedy toho, co dostanete podle dokumentace BTCPay Serveru, z one-click spouštěče LunaNode a z většiny instalací na VPS.

Nejjednodušší cesta vede přes webové rozhraní:

1. Přejděte na `Admin Dashboard > Server > Maintenance`.
2. Klikněte na **Update**.
3. Počkejte, než se kontejnery stáhnou a restartují. Rozhraní bude na několik minut nedostupné.

Pokud je webové rozhraní nedostupné nebo chcete raději vidět logy, proveďte to přes SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Ve výchozí instalaci je `$BTCPAY_BASE_DIRECTORY` nastaven na `/root`, takže jde o adresář `/root/btcpayserver-docker`. Skript stáhne nejnovější image, znovu vytvoří kontejnery a vypíše výsledné verze.

Nasazení přes Docker dodává NBXplorer společně s BTCPay Serverem, takže standardní aktualizace povýší i NBXplorer na doporučenou verzi `2.6.10`. Pokud provozujete NBXplorer samostatně — což je typické pro integrátory a pro vlastní sestavy — aktualizujte jej výslovně.

### Umbrel

Otevřete nástěnku Umbrelu, přejděte do **App Store**, najděte BTCPay Server a nainstalujte aktualizaci, pokud je nabízena.

⚠️ **Důležité:** balíčky z App Store přebaluje tým Umbrelu a mohou se za upstreamem opožďovat o hodiny až dny. Po aktualizaci zkontrolujte verzi v patičce BTCPay Serveru. Pokud je stále nižší než `2.4.2`, **zastavte aplikaci** z nástěnky Umbrelu a počkejte na zabalené vydání, místo abyste nechali běžet zranitelnou instanci.

Samotné aplikaci se věnuje samostatný návod pro Umbrel:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Stejná logika: aktualizujte BTCPay Server z marketplace StartOS a poté ověřte verzi v patičce. Pokud zabalená verze ještě není `2.4.2`, službu do té doby zastavte.

### Spravovaný a cizí hosting

Pokud vaši instanci provozuje někdo jiný (poskytovatel hostingu, spolek, server kamaráda), potvrzení stejně potřebujete. Vyžádejte si od provozovatele řetězec s verzí zobrazený v patičce a výslovně se zeptejte, zda byla provedena i obnova přihlašovacích údajů po aktualizaci popsaná níže. „Aktualizovali jsme“ není totéž jako „obnovili jsme vaše macaroons“.

## Krok 3 — Ověřte, že se aktualizace skutečně projevila

Znovu načtěte rozhraní BTCPay Serveru a přečtěte si verzi v patičce. Musí ukazovat `2.4.2` nebo vyšší.

Nespoléhejte na to, že příkaz aktualizace skončil bez chyby: na strojích s omezenými prostředky může stažení image tiše selhat a nechat běžet předchozí kontejner. Přečtěte si verzi, pokaždé.

## Krok 4 — Obnovte své přihlašovací údaje

Tohle je ten krok, který mění „záplatováno“ na „v bezpečí“. Protože byla zranitelnost zneužívána ještě před vydáním opravy, považujte každý tajný údaj, který vaše instance držela, za potenciálně známý útočníkovi.

### Lightning: LND

Znovu vygenerujte macaroons **i** soubor `macaroons.db`. Smazat pouze soubory s macaroons nestačí — LND odvozuje macaroons z kořenového klíče uloženého v `macaroons.db`, takže útočník, který drží kopii starého macaroonu, si přístup udrží, dokud tuto databázi znovu nevytvoříte.

Postup je následující: zastavte LND, odstraňte z adresáře sítě soubor `macaroons.db` a soubory `*.macaroon` (pro mainnet jde o `data/chain/bitcoin/mainnet/` uvnitř datového adresáře LND), poté LND restartujte a odemkněte, čímž se znovu vytvoří. Nejprve si adresář zazálohujte a znovu spárujte každou aplikaci, která stará macaroons používala — samotný BTCPay Server, Zeus, Thunderhub, RTL, Alby i všechny skripty, které jste napsali.

Pokud navíc vystavujete LND do internetu, projděte si zároveň i jeho TLS certifikát a veškeré přihlašovací údaje v `lnd.conf`.

### Lightning: ostatní backendy

Cokoli, co se vůči vašemu uzlu ověřuje nějakým řetězcem, musí dostat řetězec nový:

- **Core Lightning**: znovu vygenerujte rune nebo přístupové údaje používané daným připojením.
- **Phoenixd**: obnovte HTTP heslo.
- **LNbits a podobné**: odvolejte a znovu vydejte admin a invoice klíče.
- **Připojovací řetězce vzdálených uzlů** uložené v nastavení obchodu v BTCPay Serveru: přepište je novými tajnými údaji.

### Horká on-chain peněženka vygenerovaná uvnitř BTCPay Serveru

Pokud jste nechali BTCPay Server, aby vám vygeneroval on-chain peněženku — na rozdíl od připojení hardwarové peněženky nebo importu xpubu, jehož klíče se serveru nikdy nedotkly — pak byl tento seed na daném stroji.

Považujte jej za spálený:

1. Vytvořte novou peněženku, ideálně hardwarovou, aby už klíče na serveru nikdy neležely.
2. Převeďte prostředky ze staré peněženky do nové.
3. Nahraďte derivační schéma v nastavení obchodu novou peněženkou.
4. Nikdy starý seed znovu nepoužívejte.

Sledovací (watch-only) konfigurace — xpub nebo hardwarová peněženka — to nepotřebují: soukromé klíče na serveru nikdy nebyly. Přesně proto je instalační návod doporučuje.

### Účty a API klíče BTCPay Serveru

Když už u toho jste:

- Změňte hesla všech uživatelských účtů na instanci.
- Odvolejte a znovu vydejte všechny **API klíče** Greenfield.
- Znovu nastavte dvoufaktorové ověřování, protože verze 2.4.2 opravuje obejití 2FA.
- Otevřete `Admin Dashboard > Server > Users` a zkontrolujte, že neexistuje žádný neočekávaný účet.
- Projděte nedávné **výplaty** (payouts), **pull payments** a **vratky** (refunds) a hledejte položky, které jste nevytvořili.
- Zkontrolujte své webhooky a jejich tajné klíče.

## Krok 5 — Zůstaňte informovaní pro příště

Bezpečnostní vydání pomohou jen těm provozovatelům, kteří se o nich dozvědí:

- Sledujte [vydání BTCPay Serveru na GitHubu](https://github.com/btcpayserver/btcpayserver/releases) — GitHub vám může poslat e-mail při každém novém vydání repozitáře.
- Odebírejte oznamovací kanály projektu a [oficiální blog](https://blog.btcpayserver.org/).
- Udržujte svou instanci na verzi, kterou dokážete rychle aktualizovat: čím větší máte skluz, tím bolestivější nouzová aktualizace bude.

Vlastní hosting vám dává suverenitu nad vašimi platbami. Cenou za tuto suverenitu je přesně tohle: číst poznámky k vydání a být tím, kdo záplatuje.
