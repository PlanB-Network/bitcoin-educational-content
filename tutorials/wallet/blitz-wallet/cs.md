---
name: Blitz Wallet
description: Nejjednodušší bitcoinová peněženka.
---

![cover](assets/cover.webp)

Uživatelský zážitek je jedním z rozhodujících faktorů při výběru bitcoinové peněženky. V tomto tutoriálu vám představíme Blitz Wallet, peněženku, která staví jednoduchost do středu svého přístupu: díky integraci protokolu **Spark** vám Blitz nabízí jednu z nejjednodušších a nejkompletnějších bitcoinových peněženek na trhu, s okamžitými platbami a bez nutnosti technické správy.

## Co je Blitz Wallet?

Blitz Wallet je **self-custodial** a **open source** bitcoinová peněženka, která vsází na vaši suverenitu a plynulý, intuitivní uživatelský zážitek.

[Blitz Wallet](https://blitz-wallet.com/) je mobilní aplikace dostupná na Androidu (Play Store) i iOS (App Store).

Na rozdíl od tradičních Lightning peněženek, které vyžadují správu platebních kanálů a příchozí likvidity, Blitz Wallet se opírá o **protokol Spark**, čímž tyto technické složitosti odstraňuje. Výsledek: okamžité platby od prvního přijatého satoshi, bez jakéhokoli předchozího nastavení. Cílem Blitzu je učinit platby v bitcoinu stejně jednoduché jako běžná platební aplikace, aniž by kdy ohrozil self-custody vašich prostředků.

Blitz Wallet rovněž podporuje **čitelné adresy** ve formátu `uzivatel@domena.com` (přes LNURL), což umožňuje posílat bitcoiny stejně snadno jako e-mail, bez nutnosti pracovat s dlouhými invoices nebo QR codes při každé transakci.

## Pochopení protokolu Spark

Než přejdeme k praxi, je užitečné pochopit technologii, díky které Blitz Wallet funguje pod kapotou: **protokol Spark**.

### Co je Spark?

Spark je open source protokol druhé vrstvy postavený na Bitcoinu, vyvinutý týmem Lightspark. Umožňuje provádět okamžité transakce s nízkými náklady a zároveň zachovává self-custody vašich bitcoinů.

Na rozdíl od Lightning Network, který je založen na **platebních kanálech** mezi dvěma stranami, Spark používá technologii nazývanou **statechain** (řetězec stavů). Základní princip je následující: místo přesouvání bitcoinů na blockchainu při každé transakci Spark přenáší **právo na utracení** z jednoho uživatele na druhého, bez pohybu on-chain.

### Jak to funguje?

Pro intuitivní pochopení Sparku si představme, že utracení bitcoinu na Sparku vyžaduje složení puzzle ze dvou dílků:
- Jeden dílek drží uživatel (například Alice).
- Druhý dílek drží skupina operátorů nazývaná **Spark Entity (SE)**.

Pouze kombinace obou odpovídajících dílků umožňuje utratit bitcoiny.

Když chce Alice poslat své bitcoiny Bobovi, stane se toto: společně mezi Bobem a SE se vytvoří nový puzzle. Puzzle si zachová stejný tvar, ale dílky, které ho tvoří, se změní. Nyní je to Bobův dílek, který odpovídá dílku SE. Starý dílek Alice se stane nepoužitelným, protože SE zničila svůj odpovídající dílek. Vlastnictví bitcoinů přešlo z rukou do rukou, **bez jediné transakce na blockchainu**.

Bob pak může zopakovat stejný proces a poslat tyto bitcoiny Carol, a tak dále. Každý převod funguje výměnou dílků puzzle, nikoli pohybem prostředků on-chain.

### Proč je to bezpečné?

Nabízí se legitimní otázka: co se stane, pokud SE ve skutečnosti nezničí svůj starý dílek?

Spark Entity není jediná entita: je to skupina nezávislých operátorů. Dílek SE nikdy nedrží jediný operátor. Výměna puzzle vyžaduje spolupráci více operátorů. Stačí, aby **jediný operátor byl poctivý** během převodu, a to zabrání reaktivaci starého puzzle. Žádný izolovaný operátor nemůže tajně uchovat starý aktivní puzzle ani ho později znovu vytvořit.

Navíc Spark zahrnuje mechanismus jednostranného výstupu: své bitcoiny můžete vždy získat zpět on-chain bez spolupráce SE. Tento záložní mechanismus je nedílnou součástí architektury Sparku a zaručuje, že nikdy nejste závislí na síti pro přístup ke svým prostředkům.

### Spark vs Lightning Network

Spark a Lightning si nekonkurují: jsou **komplementární**. Blitz Wallet integruje oba, což vám umožňuje těžit z výhod každého z nich.

|                               | **Spark**                    | **Lightning Network**  |
| ----------------------------- | ---------------------------- | ---------------------- |
| **Technologie**               | Statechains (řetězce stavů)  | Platební kanály        |
| **Správa kanálů**             | Není vyžadována              | Vyžadována             |
| **Příchozí likvidita**        | Není vyžadována              | Vyžadována             |
| **Okamžité transakce**        | Ano                          | Ano                    |
| **Self-custody**              | Ano                          | Ano                    |
| **Kompatibilita s Lightning** | Ano (přes atomic swaps)      | Nativní                |

Lightning Network zůstává vynikajícím protokolem pro okamžité platby, ale přináší technická omezení (správa kanálů, příchozí likvidita, online uzel...), která mohou začátečníky odradit. Spark tato omezení odstraňuje a zároveň zůstává kompatibilní s Lightning.

## Instalace a konfigurace

V tomto tutoriálu vycházíme z verze Blitz Wallet pro Android, ale všechny níže uvedené postupy platí i pro iOS.

![installation](assets/fr/01.webp)

Jelikož je Blitz Wallet peněženka s self-custody, máte na výběr mezi **vytvořením nové peněženky** nebo **importem fráze pro obnovení** (12 nebo 24 slov) z existující peněženky.

Zde začínáme vytvořením nové peněženky. Níže najdete naše doporučení pro zálohování vaší fráze pro obnovení:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **DŮLEŽITÉ**: Těchto 12 nebo 24 slov pro obnovení je **jediný klíč k přístupu k vašim bitcoinům**. Blitz je self-custodial peněženka: ani Blitz, ani Spark nemají přístup k vaší frázi pro obnovení ani k vašim prostředkům. Pokud tato slova ztratíte, navždy přijdete o přístup ke svým bitcoinům. Nesdílejte je s nikým: kdokoli je vlastní, může utratit vaše bitcoiny.

Poté vytvořte **PIN kód** pro zabezpečení přístupu k vaší peněžence.

![setup-wallet](assets/fr/02.webp)

## Začínáme s Blitzem

Provádění transakcí s Blitzem je intuitivnější než u většiny ostatních bitcoinových peněženek. Rozhraní je minimalistické a zaměřené na tři hlavní akce: odeslat, naskenovat a přijmout.

### Přijímání bitcoinů

Pro příjem bitcoinů na vaši peněženku Blitz klikněte na ikonu **"Šipka dolů"** (↓), zadejte částku v satoshi, kterou chcete přijmout, přidejte volitelný popis a peněženka vygeneruje fakturu (invoice), kterou můžete sdílet s odesílatelem.

⚠️ **POZNÁMKA**: Satoshi (nebo "sat") je nejmenší jednotka bitcoinu: **1 bitcoin = 100 000 000 satoshi**.

Jednou ze zvláštností Blitz Wallet je, že podporuje několik sítí a protokolů ekosystému Bitcoin:

- **Lightning Network**: Jedna z nadstavbových vrstev Bitcoinu, která umožňuje provádět mikroplatby okamžitě s velmi nízkými poplatky. Ideální pro malé každodenní částky.

- **Bitcoin (on-chain)**: Hlavní blockchain protokolu Bitcoin, vhodný pro transakce vyšších částek, kde je prioritou maximální bezpečnost a finalita.

- **Liquid Network**: Sidechain (paralelní řetězec) Bitcoinu vyvinutý společností Blockstream, který umožňuje rychlé a důvěrné transakce pomocí Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Ve výchozím nastavení Blitz generuje Lightning fakturu, ale můžete si vybrat síť, na které chcete přijímat satoshi, kliknutím na tlačítko **"Choose format"** (Zvolit formát).

![receive-sats](assets/fr/03.webp)

### Vytváření kontaktů

Blitz Wallet zjednodušuje opakované posílání bitcoinů díky svému systému kontaktů.

V nabídce **Contacts** můžete uložit uživatelská jména Blitz nebo Lightning adresy (LNURL), se kterými často komunikujete.

Díky tomu můžete posílat satoshi na tyto adresy několika kliknutími, aniž byste museli pokaždé skenovat QR code nebo ručně zadávat adresu.

### Odesílání bitcoinů

Kromě klasických metod odesílání bitcoinů (sken QR code, ruční zadání adresy) Blitz nabízí několik praktických možností:

- **Z obrázku** (*From Image*): Importujte QR code z vaší fotogalerie.
- **Ze schránky** (*From Clipboard*): Vložte dříve zkopírovanou adresu nebo fakturu.
- **Ruční zadání** (*Manual Input*): Zadejte přímo bitcoinovou adresu, Lightning fakturu nebo čitelnou adresu (například `uzivatel@walletofsatoshi.com`).
- **Z vašich kontaktů**: Vyberte předem uloženého příjemce a odešlete několika kliknutími.

V nabídce **Wallet** klikněte na tlačítko **"Šipka nahoru"** (↑), zvolte metodu odeslání, zadejte částku k odeslání, přidejte popis a potvrďte transakci.

Minimální částka pro odeslání je aktuálně **1 000 satoshi**.

![send-bitcoin](assets/fr/05.webp)

## Obchod Blitz

Kromě operací s převodem bitcoinů Blitz Wallet integruje obchod, ve kterém můžete utratit své bitcoiny za nákup digitálních služeb přímo z aplikace.

Z hlavní nabídky klikněte na záložku **Store** pro přístup do obchodu. Najdete zde také přístup k platformě **Bitrefill**, která umožňuje nakupovat dárkové karty u tisíců obchodníků po celém světě, přímo za bitcoin.

- **Umělá inteligence**: Získejte přístup k nejnovějším modelům generativní AI (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) a plaťte své kredity přímo v satoshi. K dispozici je několik tarifů podle vašich potřeb (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonymní SMS**: Odesílejte a přijímejte SMS po celém světě bez odhalení vašeho osobního telefonního čísla. Služba je účtována v satoshi za každou odeslanou zprávu.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Chraňte své soukromí online předplacením VPN WireGuard (týdenní, měsíční nebo čtvrtletní), platitelné v bitcoinu přímo z obchodu Blitz. Stačí si stáhnout klientskou aplikaci WireGuard na vaše zařízení.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet v zákulisí: jdeme hlouběji

Za jednoduchostí používání Blitz Wallet se skrývá dobře promyšlená technická architektura, která kombinuje několik vrstev ekosystému Bitcoin.

### Rozdělení vašeho zůstatku

Blitz Wallet spravuje váš zůstatek transparentně tím, že rozděluje vaše prostředky mezi různé protokoly podle potřeby. Pokud je váš zůstatek nižší než 500 000 satoshi, Blitz používá **Liquid Network** a atomické výměny (*atomic swaps*), aby vám nabídl plynulý zážitek a umožnil transakce na Lightning Network i s malými částkami.

Tento přístup zaručuje snadné zahájení pro nové uživatele, aniž by potřebovali rozumět základním mechanismům. Rozdělení vašeho zůstatku mezi různé vrstvy si můžete prohlédnout v nabídce **Nastavení > Balance Info**.

![balance](assets/fr/09.webp)

### Režim Lightning (volitelný)

Ve výchozím nastavení Blitz Wallet používá Liquid Network a protokol Spark, aby vám nabídl plynulý zážitek bez technické konfigurace. Blitz vám však dává možnost aktivovat **režim Lightning**, který automaticky otevře platební kanál, jakmile dosáhnete zůstatku **500 000 satoshi** (0,005 BTC).

Pro aktivaci režimu Lightning přejděte do **Nastavení**, poté v sekci **Technická nastavení** klikněte na možnost **Node Info**.

![enable-lightning](assets/fr/10.webp)

Díky protokolu Spark je tato aktivace **volitelná**: Spark již umožňuje provádět platby kompatibilní s Lightning bez nutnosti otevírat kanál nebo spravovat příchozí likviditu. Nativní režim Lightning zůstává užitečný pro pokročilé uživatele, kteří chtějí mít svůj vlastní Lightning uzel integrovaný v rámci aplikace.

### Prodejní místo (PoS)

Blitz Wallet integruje funkci **prodejního místa**, která umožňuje obchodníkům přijímat platby v bitcoinu přímo z aplikace.

V nabídce **Nastavení > Point-of-sale** můžete konfigurovat:

- Jedinečný identifikátor vašeho obchodu
- Místní fiat měnu, ve které se zobrazují ceny
- Pokyny pro vaše zaměstnance
- Možnost spropitného pro vaše zákazníky

Vaši zákazníci pouze naskenují vygenerovaný QR code a provedou okamžitou platbu v bitcoinu.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Zdroje použité při tvorbě tohoto tutoriálu:
- Blog [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
