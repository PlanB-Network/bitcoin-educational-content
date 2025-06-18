---
name: Misty Breez
description: Lightning Wallet bez přídě.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez je samonosný blesk Wallet vyvinutý společností Breez na základě její sady pro vývoj softwaru a sítě **Liquid** vyvinuté společností BlockStream.


Přichází se zcela novým přístupem k provozu bez uzlu Lightning: potenciální **ZMĚNA HRY** v přenosu mezi sítěmi Bitcoin.


V tomto tutoriálu vám popíšeme, jak toto portfolio funguje, a poskytneme vám jeho kompletní přehled.



## Jak Misty Breez funguje?



Misty Breez je implementace bez uzlu Lightning jako backendu. Byla vyvinuta na základě Breez SDK a Liquid.



Síť Liquid je paralelní sítí Layer k síti Bitcoin a nabízí výrazné zlepšení rychlosti a transakčních nákladů. Tento Layer umožňuje společnosti Misty Breez obejít se bez uzlu Lightning a místo toho využívat služby třetích stran Exchange, jako je **Boltz**, k zajištění interoperability mezi Liquid Network a Lightning Network. Nespěchejte, ještě se k tomu vrátíme.



Prozatím začněme naše dobrodružství s modelem Misty Breez Wallet.



## Začínáme s Misty Breez



Mobilní aplikace Misty Breez je k dispozici ke stažení na oficiálních platformách, jako je Google Play Store (pro Android) a Apple Store (pro iOS). Na správnou aplikaci můžete být přesměrováni také z oficiálních webových stránek [Misty Breez](https://breez.technology/misty/).



⚠️ Ujistěte se, že si Misty Breez nepletete s Breez Wallet.



⚠️ **DŮLEŽITÉ**: Pro bezpečnost vašich bitcoinů je nezbytné stáhnout aplikaci z oficiálních platforem, aby byla zajištěna její pravost.



![download-misty-breez](assets/fr/01.webp)



V tomto návodu budeme vycházet ze zařízení se systémem Android. Nicméně všechny kroky a konkrétní funkce popsané v této části platí i pro systém iOS.



Po instalaci vám Misty Breez nabídne možnost vytvořit nový program Wallet nebo obnovit starý program Lightning Wallet, pro který máte slova pro obnovení.


V tomto tutoriálu se rozhodneme vytvořit nové portfolio.



⚠️Misty Breez je v současné době ve fázi vývoje, proto vám doporučujeme začít s přiměřeným množstvím.



![create-wallet](assets/fr/02.webp)


### Uložte si slova pro obnovu :


Jednou z prvních věcí, kterou byste měli při vytváření nového portfolia udělat, je zálohovat 12 slov pro obnovu.


Zde je několik tipů, jak zálohovat záložní frázi.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Chcete-li zálohovat fráze, vyberte nabídku **Předvolby > Zabezpečení** a poté možnost **Zkontrolovat záložní frázi**.



![backup](assets/fr/03.webp)


Pro větší bezpečnost si můžete také **vytvořit kód PIN** pro ověření přístupu ke službě Wallet.




Najděte svou místní měnu v mnoha měnách, které společnost Misty Breez přijímá. Nastavte si měnu v nabídce **Preferences (Nastavení) > Fiat Currencies (Měny)** a poté vyberte požadovanou měnu nebo měny.



![devises](assets/fr/04.webp)



### Provádění prvních transakcí


Pokud již znáte portfolio značky Breez, nebude vás intuitivní Interface od Misty Breez vůbec odrazovat.



V nabídce **Bilance** v Interface klikněte na možnost **Přijmout** a vytvořte faktury pro příjem bitcoinů v Wallet.



⚠️ Misty Breez vás požádá, abyste v nastavení telefonu aktivovali oznámení pro aplikaci, která vás opravňuje k získání blesku Address.



S Misty Breez můžete :




- Přijímejte bitcoiny na Lightning Network od **100 satošů** až do **25 000 000 satošů**.
- Přijímejte bitcoiny v hlavní síti Bitcoin od **25 000 satošů**.



![transactions](assets/fr/05.webp)



Zde začíná kouzlo Misty Breez.


Na rozdíl od produktu Breez Wallet, který vám poskytuje uzel Lightning a požaduje, abyste sami hradili náklady na otevření a uzavření platebních kanálů, Misty Breez po vás nic nechce. Jak již bylo zmíněno, Misty Breez dokonce nefunguje ani na základě uzlu Lightning.



Podívejme se blíže do zákulisí.



Ve skutečnosti vlastníte portfolio Liquid, které je spojeno s vaším portfoliem Misty Breez. Logicky budete nakládat s L-BTC (Liquid Bitcoin) v pevných kurzech spojených s konverzními službami podmořských satelitů třetích stran, které vám umožní spolupracovat s Lightning Network.



Když obdržíte platbu na svůj Misty Breez Wallet, odesílatel vám pošle satoši, které projdou konverzní službou, jako je Boltz (v současné době používanou společností Misty Breez), aby se zaslané satoši převedly na L-BTC, které obdržíte na svůj Misty Breez Wallet (přidružený Liquid Wallet).


Zde je zjednodušené schéma procesu v zákulisí.



![lnswap-in](assets/fr/06.webp)



Klikněte na položku Interface v nabídce **Zůstatek**, klikněte na možnost **Odeslat** a zaplaťte bleskovku Invoice.


Vložte Blesk Invoice, Blesk Address příjemce nebo jednoduše naskenujte QR kód na Blesku Invoice a proveďte platbu.



![send-bitcoins](assets/fr/07.webp)



V zákulisí umožníte Liquid Wallet přidruženému k vašemu Misty Breez Wallet převést ekvivalent L-BTC na satoši prostřednictvím Boltzu a poté tyto satoši převést na Lightning Wallet příjemce (přítomný na Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Tato funkce infrastruktury společnosti Misty Breez umožňuje uživatelům provádět transakce, i když je společnost Misty Breez offline.



Pro zkušenější je k dispozici také nabídka **Předvolby > Vývojáři**, která vám poskytne trochu podrobnější informace o :




- Verze sady pro vývoj softwaru Breez.
- Veřejný klíč vašeho Misty Breez Wallet.
- Dlužník, jedinečný identifikátor odvozený z primárního veřejného klíče.
- Zůstatek vašeho portfolia.
- Tip Liquid pro zasílání malých částek L-BTC.
- Tip Bitcoin pro zasílání malých množství Bitcoin.



Můžete také provádět určité akce, jako je synchronizace se zařízením Liquid Network, zálohování klíčů, sdílení protokolu aktivit a volba opětovného skenování zařízení Liquid Network.



![dev-mode](assets/fr/09.webp)


Gratulujeme! Nyní již dobře rozumíte portfoliu Misty Breez a jeho příspěvku k mezisíťovým transakcím Bitcoin. Pokud pro vás byl tento návod užitečný, dejte nám prosím palec Green. Budeme rádi, když se nám ozvete.



Chcete-li jít dál, doporučuji vám také objevit náš návod na Aqua Wallet, který funguje podobně jako Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125