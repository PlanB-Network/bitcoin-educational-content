---
name: BitcoinVoucherBot
description: Bot Telegramu pro nákup Bitcoin v důvěrnosti
---
![image](assets/cover.webp)

_Tento návod napsal_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Úvod

BitcoinVoucherBot je nástroj, s jehož pomocí lze nakupovat bitcoiny v Exchange za eura.

### KYC Light

Akce změny eura pro Bitcoin je prvním a nejzákladnějším krokem k zahájení studia tohoto tématu, ale zřejmě také nejobtížnějším a nejsložitějším. Možností může být mnoho: nabídka Bitcoin prostřednictvím centralizovaných burz, setkání s tématikou Bitcoin, přátelé, známí a další. Připojujeme se ke komunitě Bitcoinerů a **naprosto doporučujeme používat centralizované burzy**, aby byla zajištěna větší pozornost k vlastnímu soukromí.

Ačkoli tato volba může být méně pohodlná, je důležité si uvědomit, že burzy prosazují nařízení Know Your Cutomer (KYC), a proto ke každému Satoshi, který si u nich zakoupíte, přiřadíte identitu i fyzické umístění. "Pohodlnost" má některé zarážející vedlejší účinky.

### Jak na to?

Přichází služba [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot), bot Telegramu, který funguje jako prostředník mezi našimi převody SEPA a nákupy Sats.

### Předpoklady

Chcete-li začít používat službu BitcoinVoucherBot, není třeba sdělovat pracovníkům Bota žádné citlivé osobní údaje. **Není potřeba žádná autorizace**.

Stačí mít aktivní účet Telegram a bankovní účet. **Poznámka**: Vhodný není účet zřízený u Poste Italiane (pro italské zákazníky) nebo obecněji odkaz na dobíjecí kartu.

V chatu Telegramu připravíme objednávku, bankovním převodem ji zaplatíme a nakonec prostřednictvím bota dostaneme poukaz vystavený společností třetí strany, která nezná předmět nákupu.

### Aktivace bota a menu

Aktivace je jednoduchá jednorázová operace. Na Telegramu vyhledejte _@BitcoinVoucherBot_ a jakmile se dostanete do chatu Bota, vynikne dole velké tlačítko _Start/Start_. Operace vyvolá reakci Bota, který představí nabídku hlavních příkazů, které má k dispozici. Objeví se také první uvítací zprávy, u kterých doporučujeme pečlivé čtení.

**Upozornění**: existuje několik podvodníků, kteří se vydávají za původní VoucherBot. Pokud si nejste jisti vyhledáváním přes Telegram, přistupte prosím na odkaz BitcoinVoucherBot z [oficiální webové stránky](https://www.bitcoinvoucherbot.com/)

![image](assets/it/01.webp)

Možnosti se zobrazí po kliknutí na tlačítko _Menu_ v levém dolním rohu: můžete kliknout na slovo odpovídající příkazu nebo do pole pro zprávy napsat lomítko `/` následované zadaným příkazem.

![image](assets/it/02.webp)

Mezi hlavní operace patří:


- _/purchase_: je vlastní postup nákupu. Po dokončení transakce bot automaticky vygeneruje QR kód, který je připraven k proplacení.
- _/refill_: v době psaní tohoto návodu byla k dispozici, ale nebudeme se jí zabývat, protože z technických důvodů může být tato možnost později odstraněna.
- _/swap_: otevře proceduru výměny, která je dostupná buď pomocí pohodlného bota Telegramu, nebo přes web.
- _/ap_: akumulační plán, který vám umožní nastavit **konstantní akumulační plán (CAP)**.
- _/lnaddress_: se kterým máme propojit vlastní LN Address, pro konkrétní postup, který uvidíme později.
- _/credits_: zkontroluje, kolik kreditu zbývá na poukázky generate.
- _/myorders_: zobrazuje objednávky zadané pomocí bota (**Upozornění** systém sleduje pouze posledních 10 zadaných objednávek, nikoli celou historii).
- _/fees_: příkaz pro kontrolu síťových poplatků. Pro jejich vyhodnocení je vždy nejlepší spoléhat se na Mempool.space.
- _/support_: v případě potřeby zobrazí kontakty pro nahlášení problémů týmu podpory.

# Postup nákupu Bitcoin

## Příprava objednávky

V příkazovém menu klikněte na _/purchase_

![image](assets/it/03.webp)

Objevuje se řada příležitostí, ale my si vybíráme _BTC Vouchery_

![image](assets/it/04.webp)

BitcoinVoucherBot umožňuje nákup Bitcoin onchain, Lightning a Liquid.

V této fázi vyberte _Onchain & Lightning 🔗⚡️_

![image](assets/it/05.webp)

Obrazovka se rychle změní a VoucherBot navrhne hodnoty nákupu. Ty začínají od minimálních 100,00 € až po 900,00 €.

V případě prvního nákupu jsou nabízeny pouze nominální hodnoty 100,00 €, Onchain a Lightning. Pro zvýšení důvěrnosti doporučujeme zvolit _Lightning ⚡️_

![image](assets/it/06.webp)

VoucherBot nás upozorní, že byla provedena první volba a že pro její potvrzení musíme zvolit _Pokračovat_

![image](assets/it/07.webp)

Nyní je třeba zvolit způsob platby. Převod se provádí bankovním převodem **(přijímá se pouze SEPA)**. VoucherBot navrhuje jako příjemce společnost, která poskytuje dva bankovní účty, jeden ve Velké Británii a druhý ve Švýcarsku. Švýcarská banka byla vybrána k provedení tohoto návodu

![image](assets/it/08.webp)

V tomto okamžiku jsme vyzváni k zadání našeho IBAN, od kterého se začne provádět převod do vybrané banky. Tyto informace jdou do skládačky, která umožní botovi, tj. stroji, poskládat některé informace tak, aby nákupní proces proběhl bez nutnosti lidského zásahu.

IBAN musí být zapsán do panelu zpráv, zkontrolován a odeslán botovi.

![image](assets/it/09.webp)

V chatu s VoucherBotem se nyní zobrazí kontrolní zpráva.

Pokud je vše v pořádku, pokračujte kliknutím na tlačítko _Pokračovat_.

![image](assets/it/10.webp)

## Platba

Po několika okamžicích, které jsou nutné ke zpracování údajů, VoucherBot odpoví zprávou obsahující všechny údaje potřebné k dokončení objednávky. V závislosti na tom, co vaše banka vyžaduje, jsou příslušné informace následující:


- `IBAN`, který je nezbytný pro vklad, stejně jako Address příjemce;
- `zvolená částka` dříve přes mezní hodnotu, která musí být splněna, aby VoucherBot mohl rozpoznat objednávku po přijetí platby;
- `Důvod platby`, což je důvod platby. **Musí být zkopírován a vložen bez odstranění nebo přidání čehokoli do příslušného pole převodu. Jakékoli "." nebo "-", které se v důvodu platby vyskytují, mohou být nahrazeny `bílou mezerou` **.
- jedinečné `OrderID`, na které se odkazuje při žádosti o pomoc.

Poté můžete provést platbu prostřednictvím aplikace nebo banky. Jakmile banka platbu přijme, je důležité nezapomenout v chatu s VoucherBotem stisknout tlačítko _oznámit platbu_. Tato jednoduchá operace vás upozorní, že platba je na cestě.

![image](assets/it/11.webp)

VoucherBot odpoví zprávou, která obsahuje velmi důležité varování: **nevymazávejte chat**, alespoň dokud neobdržíte voucher, protože je to jediný způsob, jak objednávku rekonstruovat a udržet ji v chodu.

![image](assets/it/12.webp)

---
Upozornění:


- přijímáme pouze bankovní převody SEPA;
- čekací doba souvisí výhradně s tím, jak banky (které nepracují 24 hodin denně, 7 dní v týdnu a 365 dní v týdnu jako Bitcoin) poukaz zpracovávají. Obdržení poukazu může trvat od několika hodin až po 3 pracovní dny;
- pro všechny potřeby, Bitcoin VoucherBot má vynikající [podpora](https://t.me/BitcoinVoucherGroup) služby na Telegramu.

---
## Vykoupení

Jakmile je platba úspěšná, odešle Bitcoin VoucherBot poukaz přímo do chatu. Bleskový voucher má podobu QR kódu vytištěného na oranžovém pozadí.

![image](assets/it/31.webp)

K dispozici jsou všechna data potřebná k jeho zpeněžení:


- částku v Sats, která odpovídá částce zaslané bankovním převodem, bez poplatků za služby a síťových poplatků;
- referenční ID voucheru;
- datum, do kterého musí být poukázka uplatněna, jinak finanční prostředky propadnou, tj. 25 dní po vystavení.

Voucher můžete uplatnit zarámováním QR kódu pomocí skenovací funkce kompatibilního zařízení Wallet Lightning Network nebo prostřednictvím služby LNURL, která je rovněž uvedena pod QR kódem.

Pro tento návod jsme použili Wallet Z Satoshi, pomocí funkce skenování aktivované klávesou _Odeslat_

![image](assets/it/32.webp)

Při aktivovaném fotoaparátu mobilního telefonu zarámujte kód QR v chatu a otevřete Telegram z počítače

![image](assets/it/34.webp)

Před pokračováním, Wallet Z Satoshi z ověřovací obrazovky, která obsahuje částku, která přesně odpovídá částce vyjádřené na poukazu a jako popis, BitcoinVoucherBot. Chcete-li poukázku proplatit, stačí kliknout na _Přijmout_

![image](assets/it/35.webp)

Wallet Z Satoshi zpracovává několik okamžiků

![image](assets/it/36.webp)

a nakonec je sbírka vykázána a okamžitě k dispozici v zůstatku Wallet.

**Wallet z Satoshi je opatrovnická aplikace: ihned po proplacení poukázky je vhodné přesunout Sats na Wallet, která není opatrovnická.**

![image](assets/it/37.webp)

### Jak uplatnit voucher onchain

Jak jsme viděli při přípravě objednávky, VoucherBot umožňuje zakoupit Sats přímo v řetězci s výběrem stejnojmenného voucheru.

**Poznámka**: Příprava objednávky a platba se nemění, jsou vždy stejné. Co se mění, je způsob proplácení onchain poukázky.

Po dokončení objednávky, provedení platby, stisknutí tlačítka _oznámit platbu_ a vyčkání na technický čas banky pro převod, VoucherBot zareaguje odesláním voucheru přímo do chatu.

Tento poukaz má také podobu QR kódu, ale jeho hlavní barva je kanárkově žlutá a - což je nejdůležitější - v popisu je dobře vysvětleno, že se jedná o onchain poukaz, který proplatíte přímo na svém onchainu Wallet a pro zahájení proplácení musíte kliknout na _Redeem on Telegram_. Onchainový poukaz obsahuje také informace, které jsme již viděli u bleskového poukazu:


- částku v Sats, která odpovídá částce zaslané bankovním převodem, bez poplatků za služby a síťových poplatků;
- kód voucheru;
- referenční ID voucheru;
- datum, do kterého musí být poukázka uplatněna, jinak finanční prostředky propadnou, tj. 25 dní po vystavení.

![image](assets/it/22.webp)

**Pozornění ⚠️:** klikněte podle vysvětlení, otevře se vyskakovací okno dalšího bota: **Voucher RedeemBot.**

K tomuto účelu je k dispozici nástroj Voucher RedeemBot. Ať už se jedná o první použití, nebo o předchozí objednávky, při každém novém uplatnění je vždy nutné kliknout na tlačítko _START_.

![image](assets/it/23.webp)

V tomto okamžiku RedeemBot načte onchain poukaz, který lze snadno rozpoznat podle kódu poukazu a referenčního ID. Odemkne také lištu pro psaní zpráv a zahájení chatu s botem, který nás vlastně vyzývá, abychom mu sdělili onchain Address našeho Wallet.

**Poznámka**: Address musí být typu SegWit.

![image](assets/it/24.webp)

V tomto okamžiku otevíráme Wallet a generate a SegWit Address

![image](assets/it/25.webp)

kopírujeme ji

![image](assets/it/26.webp)

a vložte ji do chatu s RedeemBotem

![image](assets/it/27.webp)

Nyní máme k dispozici kontrolní obrazovku, která ověřuje správnost kódu voucheru, stejně jako kód Address, který jsme sdělili RedeemBotu. Zkontrolujme je dobře, protože kliknutím na tlačítko _Pokračovat_ se transakce spustí a nebude možné ji znovu zjistit, pokud jsme například sdělili špatný Address.

![image](assets/it/28.webp)

Transakce byla zahájena a postup Redeem pro onchain voucher tím končí.

![image](assets/it/29.webp)

zatímco v historii naší společnosti Wallet je vidět, že částka přichází.

![image](assets/it/30.webp)