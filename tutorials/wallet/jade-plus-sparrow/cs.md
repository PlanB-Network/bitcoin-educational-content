---
name: Jade Plus - Vrabec
description: Pokročilá konfigurace Jade Plus s peněženkou Sparrow Wallet
---
![cover](assets/cover.webp)

Jade Plus je hardwarová peněženka určená pouze pro bitcoiny, kterou navrhla společnost Blockstream. Je to nástupce klasické peněženky Jade s vylepšeným softwarem, více možnostmi a přepracovanou ergonomií pro intuitivnější používání. Tato nová verze se může pochlubit nádherným 1,9palcovým LCD displejem s širším barevným gamutem než její předchůdce. Optimalizována byla také tlačítka a navigace v nabídkách.

Jade Plus lze používat několika způsoby: přes kabelové připojení USB-C, v režimu "*Air-Gap*" s kartou micro SD (nutný adaptér), přes Bluetooth nebo dokonce výměnou QR kódů díky integrované kameře. Tato hardwarová peněženka je napájena z baterie.

V základní černé verzi je k dispozici od 149,99 USD, cena se může zvýšit až o 20 USD za verze "*Genesis Grey*" nebo "*Lunar Silver*". Jade Plus je tedy zajímavou volbou s pokročilými funkcemi srovnatelnými s funkcemi špičkových hardwarových peněženek, jako jsou Coldcard Q nebo Passport V2, ale za poměrně nízkou cenu, blízkou modelům střední třídy.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

Jade Plus je kompatibilní s většinou softwaru pro správu portfolia. Zde je přehled kompatibility v době psaní článku (leden 2025):

| Stolní počítače | Mobilní zařízení | USB | Bluetooth | QR | JadeLink | Software pro správu

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 | 🔴

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

| Vrabec | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 |

| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

| Keeper | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

V tomto návodu nastavíme pokročilou konfiguraci zařízení Jade Plus s desktopovým softwarem Sparrow Wallet v režimu QR kódů. Tato konfigurace je ideální pro středně pokročilé nebo zkušené uživatele. Pokud hledáte jednodušší přístup pro začátečníky, doporučuji podívat se na tento návod, kde používáme Jade Plus se zelenou peněženkou přes připojení Bluetooth:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
## Bezpečnostní model Jade Plus

Jade Plus používá bezpečnostní model založený na "virtuálním bezpečném prvku", který je zhmotněn "slepým orákulem". Konkrétně tento mechanismus kombinuje PIN zvolený uživatelem, tajemství umístěné v systému Jade a tajemství držené orákulem (serverem spravovaným společností Blockstream) a vytváří klíč AES-256 distribuovaný mezi dvěma entitami. Během iniciace se výměnou ECDH zabezpečí komunikace s orákulem a zašifruje se fráze pro obnovení v hardwarové peněžence. V praxi to znamená, že když chcete získat přístup k seedu pro podepisování transakcí, potřebujete přístup k :


- Samotné zařízení Jade Plus;
- Kód PIN pro odemknutí zařízení ;
- A k tajemství věštírny.

Hlavní výhodou tohoto přístupu je absence jediného bodu selhání na úrovni hardwaru, protože pokud útočník někdy získá přístup k vašemu Jade, extrakce klíčů vyžaduje současné ohrožení Jade a orákula. Tento model také znamená, že Jade Plus je zcela open-source, čímž se vyhýbá omezením spojeným s používáním skutečně fyzicky zabezpečených prvků, jaké se používají například u Ledgeru.

Nevýhodou tohoto systému je, že použití systému Jade Plus závisí na věštírně, kterou spravuje společnost Blockstream. Pokud se toto orákulum stane nedostupným, není již možné používat hardwarovou peněženku přímo s PIN kódem. To však neznamená, že vaše bitcoiny jsou ztraceny, protože je stále můžete získat zpět pomocí obnovovací fráze, kterou můžete zadat v systému Jade Plus v režimu "*stateless*". Chcete-li tuto závislost obejít, můžete si také nakonfigurovat a spravovat vlastní oracle server.

Další možností, jak spravovat osivo, je jednoduše ho v systému Jade Plus neregistrovat. V tomto případě se Jade stane pouze podpisovým zařízením. Během inicializace uložíte kromě obvyklého uložení obnovovací fráze ve formě slov také jako ručně generovaný QR kód. Tímto způsobem můžete při každém použití peněženky importovat semínko pomocí fotoaparátu Jade. Pro pokročilé uživatele to může být zajímavá možnost, záleží na vaší bezpečnostní strategii, ale musíte být opatrní jak při ukládání seedu, tak při jeho ochraně, protože i jako QR kód by umožnil komukoli ukrást vaše prostředky. Na tuto možnost se podíváme v tomto návodu, ale není povinná.

## Rozbalení modelu Jade Plus

Po obdržení produktu Jade Plus zkontrolujte, zda jsou krabice a pečeť v dobrém stavu, abyste se ujistili, že váš balíček nebyl otevřen.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

V krabici najdete :


- Le Jade Plus;
- Kabel USB-C;
- Karty pro záznam mnemotechnické fráze jako slova nebo jako "*CompactSeedQR*";
- Některé pokyny k použití ;
- Šňůra;
- Některé nálepky.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

Zařízení má 4 navigační tlačítka:


- Tlačítko vpravo dole zapne nefrit;
- Velké tlačítko na přední straně přístroje slouží k výběru položky;
- Dvě malá tlačítka v horní části umožňují navigaci doleva a doprava;
- Položku můžete vybrat také současným kliknutím na dvě tlačítka v horní části zařízení.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Nastavení nové peněženky Bitcoin

Klikněte na tlačítko Start.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Klikněte na "*Nastavení Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Vyberte možnost "Advanced Setup*".

![Image](assets/fr/07.webp)

Poté klikněte na "*Vytvořit novou peněženku*" a vygenerujte nový seed. Můžete si vybrat mezi mnemotechnickou frází o 12 nebo 24 slovech. Zabezpečení peněženky zůstává u obou možností rovnocenné, proto může být pro uložení výhodnější zvolit nejjednodušší možnost, tj. 12 slov.

![Image](assets/fr/08.webp)

Kliknutím na tlačítko "*Pokračovat*" zobrazíte novou frázi pro obnovení.

![Image](assets/fr/09.webp)

Jade Plus zobrazí vaši 12slovnou mnemotechnickou frázi. **Tato mnemotechnická fráze vám dává plný, neomezený přístup ke všem vašim bitcoinům. Kdokoli, kdo tuto frázi zná, může vaše prostředky ukrást, a to i bez fyzického přístupu k vašemu Jade Plus. Dvanáctislovná fráze obnoví přístup k vašim bitcoinům v případě ztráty, krádeže nebo rozbití vašeho Jade. Je proto velmi důležité ji pečlivě uložit a uchovávat na bezpečném místě.

Můžete jej napsat na karton dodávaný v krabici, nebo pro větší bezpečnost doporučuji vyrýt jej na podstavec z nerezové oceli, který jej ochrání před požárem, povodní nebo zřícením.

![Image](assets/fr/10.webp)

Pro více informací o správném způsobu ukládání a správy mnemotechnických frází vřele doporučuji sledovat tento další návod, zejména pokud jste začátečníci:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
samozřejmě nesmíte tato slova nikdy sdílet na internetu, jako to dělám já v tomto návodu. Toto ukázkové portfolio bude použito pouze na Testnetu a na konci tutoriálu bude smazáno.**_

Kliknutím na šipku v pravé části obrazovky zobrazíte následující slova.

![Image](assets/fr/11.webp)

Po uložení fráze vás aplikace Jade Plus vyzve k jejímu potvrzení. Pomocí tlačítek v horní části zařízení vyberte správné slovo podle pořadí a kliknutím na prostřední tlačítko přejděte na další slovo.

![Image](assets/fr/12.webp)

Pak máte dvě možnosti. Jak bylo vysvětleno v úvodu, můžete si vybrat, zda chcete svůj seed uložit přímo do zařízení a pro přístup k peněžence použít ochranný systém Blockstream "*Virtual Secure Element*" (možnost 1), nebo zda chcete svůj seed uložit jako QR kód a naskenovat jej při každém použití (možnost 2).

Pro možnost 1 vyberte možnost "*No*" a pro možnost 2 vyberte možnost "*Yes*".

![Image](assets/fr/13.webp)

### Možnost 1: Odemknutí pomocí QR PIN

Pokud jste zvolili možnost 1 (CompactSeedQR: "*No*"), přejdete přímo k výběru metody připojení. V tomto návodu chceme přístroj používat v režimu Air-Gap prostřednictvím výměny QR kódů, proto vyberte možnost "*QR*".

![Image](assets/fr/27.webp)

Klikněte na "*Pokračovat*".

![Image](assets/fr/28.webp)

Kód PIN slouží k odemknutí zařízení Jade a poskytuje ochranu proti neoprávněnému fyzickému přístupu. Tento kód PIN se nepodílí na odvození kryptografických klíčů vaší peněženky. Takže i bez přístupu k tomuto kódu PIN vám vlastnictví vaší 12slovné mnemotechnické fráze umožní znovu získat přístup k vašim bitcoinům. Doporučujeme zvolit co nejnáhodnější kód PIN. Také se ujistěte, že tento kód máte uložen na jiném místě, než kde je uložen váš Nefrit, například ve správci hesel.

Zvolte šestimístný kód PIN na zařízení Jade a pomocí levého a pravého tlačítka procházejte číslicemi a prostředním tlačítkem každou číslici potvrďte.

![Image](assets/fr/29.webp)

Potvrďte PIN podruhé.

![Image](assets/fr/30.webp)

Jak bylo vysvětleno v úvodu, vaše osivo je v zařízení Jade Plus uloženo šifrovaně. Chcete-li jej dešifrovat, musíte zadat :


- Platný kód PIN (který jsme právě nastavili) ;
- Tajemství věštírny udržované společností Blockstream.

V tomto pokročilém tutoriálu budeme ke správě peněženky Bitcoin používat aplikaci Sparrow Wallet. Na rozdíl od softwaru Green Wallet společnosti Blockstream však Sparrow nemá přístup k orákulu na serverech společnosti Blockstream. Budeme proto používat webové stránky společnosti Blockstream k získání tajemství orákula při každém odemknutí Jade Plus.

Navštivte https://jadefw.blockstream.com/pinqr/index.html

Klikněte na "*Spustit odemykání QR*".

![Image](assets/fr/31.webp)

Klikněte na "*Done*", protože PIN jste si již zvolili v zařízení Jade Plus.

![Image](assets/fr/32.webp)

Pomocí fotoaparátu počítače naskenujte kódy QR zobrazené na obrazovce zařízení Jade.

![Image](assets/fr/33.webp)

Potvrzením na obrazovce Jade přejdete na další obrazovku.

![Image](assets/fr/34.webp)

Naskenujte QR kód, který je nyní viditelný na webových stránkách, a získejte tajemství věštírny.

![Image](assets/fr/35.webp)

Po vytvoření portfolia můžete přejít k dalším krokům a přeskočit pododdíl "*Možnost 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

Při každém spuštění klikněte na "*QR Mode*".

![Image](assets/fr/37.webp)

Vyberte možnost "*QR PIN Unlock*".

![Image](assets/fr/38.webp)

Zadejte kód PIN.

![Image](assets/fr/39.webp)

Poté přejděte na [webovou stránku Blockstream](https://jadefw.blockstream.com/pinqr/qrpin.html) a vyměňte si QR kódy s věštírnou.

![Image](assets/fr/40.webp)

Vaše karta Jade je nyní odemčená.

![Image](assets/fr/41.webp)

### Možnost 2: CompactSeedQR

Pokud jste zvolili možnost 2 (CompactSeedQR: "*Yes*"), klikněte znovu na "*Yes*".

![Image](assets/fr/14.webp)

Klikněte na "*Start*".

![Image](assets/fr/15.webp)

Můžete použít základnu QR kódu, která je součástí balení Jade Plus. Vyberte příslušné políčko podle toho, zda jste se rozhodli pro větu o 12 nebo 24 slovech. Můžete si také [vytisknout šablonu z webových stránek Blockstream](https://help.blockstream.com/hc/article_attachments/41928319071769).

Jade Plus zobrazí každou zónu vašeho QR kódu.

![Image](assets/fr/16.webp)

Pomocí pera vybarvěte čtverečky a reprodukujte semínko jako QR kód. Buďte přesní, aby jej fotoaparát Jade Plus mohl později naskenovat. Pomocí šipky přejděte na další oblast.

![Image](assets/fr/17.webp)

Po dokončení klikněte na tlačítko "*Done*".

![Image](assets/fr/18.webp)

Ručně vyrobený QR kód naskenujte pomocí zařízení Jade Plus a zkontrolujte jeho platnost.

![Image](assets/fr/19.webp)

Pokud je záloha papíru správná, klikněte na tlačítko "*Pokračovat*".

![Image](assets/fr/20.webp)

V tomto návodu budeme používat režim připojení založený výhradně na skenování QR kódů, takže vyberte možnost "*QR*".

![Image](assets/fr/21.webp)

Kromě zálohy CompactSeedQR můžete také přidat kód PIN jako v možnosti 1. To nabízí dva způsoby přístupu k vaší peněžence: buď prostřednictvím PIN a systému "Virtual Secure Element" společnosti Blockstream, nebo prostřednictvím CompactSeedQR.

Pokud se rozhodnete pro možnost dvojitého kódu PIN, vyberte možnost "*PIN*" a podle stejného postupu jako v možnosti 1 nastavte kód PIN.

Pokud chcete pokračovat pouze s aplikací CompactSeedQR, vyberte možnost "*SeedQR*".

![Image](assets/fr/22.webp)

Po vytvoření portfolia můžete přejít k dalším krokům.

![Image](assets/fr/23.webp)

Při každém spuštění klikněte na tlačítko "*QR Mode*" a poté na "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Pomocí fotoaparátu zařízení naskenujte uloženou semínkovou sadu jako kód QR.

![Image](assets/fr/25.webp)

Vaše karta Jade je nyní odemčená.

![Image](assets/fr/26.webp)

## Přidání přístupové fráze BIP39

Přístupová fráze BIP39 je volitelné heslo, které si můžete libovolně zvolit a které se přidává k vaší mnemotechnické frázi, aby posílilo zabezpečení peněženky. Pokud je tato funkce povolena, přístup k vaší peněžence Bitcoin bude vyžadovat jak mnemotechnickou, tak heslovou frázi. Bez obou by bylo nemožné peněženku obnovit.

Před konfigurací této možnosti v systému Jade Plus důrazně doporučujeme přečíst si tento článek, abyste plně porozuměli teoretickému fungování přístupové fráze a vyhnuli se chybám, které by mohly vést ke ztrátě vašich bitcoinů :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Když je zařízení Jade stále zamčené (přístupovou frázi lze zadat pouze tehdy, když zařízení není odemčené), přejděte do nabídky "*Options*".

![Image](assets/fr/42.webp)

Vyberte možnost "*BIP39 Passphrase*".

![Image](assets/fr/43.webp)

V možnosti "*Frekvence*" můžete zvolit, zda vás bude aplikace Jade Plus při každém spuštění žádat o zadání přístupové fráze:


- "*Zakázáno*" zakáže použití přístupové fráze;
- "*Pouze při dalším přihlášení*" bude vyžadovat návrat do této nabídky, abyste při dalším spuštění aktivovali požadavek na vaši přístupovou frázi. Tato volba umožňuje neprozradit její použití;
- "*Vždy se ptát*" způsobí, že se vás Jade při každém spuštění systematicky zeptá na vaši přístupovou frázi, čímž odhalí, že je vaše peněženka chráněna přístupovou frází.

Vyberte možnost podle své strategie zabezpečení. Osobně jsem pro tento příklad vybral možnost "*Vždy se ptát*".

![Image](assets/fr/44.webp)

Poté si můžete vybrat ze dvou způsobů zadání přístupové fráze:


- "*Ruční*: Na virtuální klávesnici můžete zadávat písmena (velká a malá), čísla a symboly, znak po znaku. Jedná se o standardní metodu pro všechny hardwarové peněženky;
- "*Seznam slov*": Specifická metoda navržená společností Blockstream pro Jade, která urychluje zadávání hesla a zvyšuje jeho entropii. Během zadávání systém navrhuje slova ze seznamu BIP39, což usnadňuje odemykání. Tato metoda automaticky generuje větu spojením vybraných slov oddělených mezerami (příklad: `abandon ability able`).

Osobně vám doporučuji použít první metodu, protože je to standard, který najdete na všech ostatních podporách portfolia.

![Image](assets/fr/45.webp)

Poté se můžete vrátit na domovskou obrazovku a odemknout peněženku běžným způsobem, a to buď pomocí kódu PIN, nebo pomocí kódu CompactSeedQR (jak je vidět výše). Poté budete vyzváni k zadání přístupové fráze.

![Image](assets/fr/46.webp)

Zadejte jej na klávesnici Jade a nezapomeňte si vytvořit jednu nebo více záloh na fyzickém médiu (papírovém nebo kovovém). V příkladu používám velmi slabou přístupovou frázi, ale vy musíte zvolit silnou, náhodnou přístupovou frázi, která obsahuje všechny typy znaků a je dostatečně dlouhá (jako silné heslo).

![Image](assets/fr/47.webp)

Pokud je vaše přístupová fráze platná, potvrďte ji.

![Image](assets/fr/48.webp)

Upozorňujeme, že u přístupových hesel BIP39 záleží na velikosti písmen a překlepů. Pokud zadáte heslovou frázi mírně odlišnou od původně nakonfigurované, Jade neohlásí chybu, ale odvodí jinou sadu kryptografických klíčů, které nebudou těmi z vašeho původního portfolia.

Proto je důležité, abyste si při konfiguraci poznamenali otisk hlavního klíče, který najdete v pravém dolním rohu obrazovky. Například s mou přístupovou frází `PBN` je otisk hlavního klíče `3AD1AE65`.

![Image](assets/fr/49.webp)

Při každém odemknutí zařízení Jade pomocí přístupové fráze zkontrolujte, zda je otisk prstu stejný jako ten, který jste zadali při konfiguraci. Pokud ano, je vaše přístupová fráze správná a přistupujete ke správné peněžence Bitcoin. Pokud tomu tak není, jste na špatné peněžence a musíte to zkusit znovu a dávat pozor, abyste neudělali žádnou chybu při zadávání.

Než obdržíte své první bitcoiny do peněženky, **důrazně doporučuji provést test obnovy prázdné peněženky**. Zaznamenejte si některé referenční informace, jako je vaše xpub nebo první přijímací adresa, a poté peněženku na Jade Plus vymažte, dokud je ještě prázdná (`Možnosti -> Zařízení -> Obnovení továrního nastavení`). Poté zkuste peněženku obnovit pomocí papírových záloh mnemotechnické fráze a případné přístupové fráze. Zkontrolujte, zda se informace o souboru cookie vygenerované po obnovení shodují s těmi, které jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé. Chcete-li se dozvědět více o tom, jak provést zkušební obnovu, podívejte se na tento další návod:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Konfigurace peněženky v aplikaci Sparrow Wallet

V tomto tutoriálu představím pokročilé použití aplikace Jade Plus pomocí aplikace Sparrow Wallet. Tato hardwarová peněženka je však kompatibilní s mnoha dalšími programy, například Liana, Nunchuk, Specter, Green a Keeper. Tyto kompatibility se liší z hlediska připojení: USB, Bluetooth nebo QR kód (podrobnosti viz tabulka v úvodu).

Začněte stažením a instalací aplikace Sparrow Wallet [z oficiálních stránek](https://sparrowwallet.com/) do počítače, pokud jste tak ještě neučinili.

![Image](assets/fr/50.webp)

Před instalací nezapomeňte zkontrolovat pravost a neporušenost softwaru. Pokud nevíte, jak to udělat, přečtěte si tento návod:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Po otevření aplikace Sparrow Wallet klikněte na kartu "*File*" a poté na "*New Wallet*".

![Image](assets/fr/51.webp)

Pojmenujte svou peněženku a klikněte na "*Vytvořit peněženku*".

![Image](assets/fr/52.webp)

Vyberte možnost "*Airgapped Hardware Wallet*".

![Image](assets/fr/53.webp)

Klikněte na "*Scan...*" vedle možnosti "*Jade*".

![Image](assets/fr/54.webp)

Odemkněte telefon Jade Plus a pokud jej používáte, zadejte přístupovou frázi. Poté přejděte do nabídky "*Možnosti*", vyberte "*Peněženka*" a klikněte na "*Exportovat Xpub*".

![Image](assets/fr/55.webp)

Váš Jade zobrazí váš Keystore prostřednictvím několika QR kódů. Naskenujte je na svém počítači pomocí Sparrow.

![Image](assets/fr/56.webp)

Nyní byste měli vidět svůj xpub a otisk hlavního klíče, který by se měl shodovat s otiskem na vašem Jade Plus. Klikněte na "*Použít*".

![Image](assets/fr/57.webp)

Nastavte si silné heslo pro zabezpečení přístupu do peněženky Sparrow. Toto heslo ochrání vaše veřejné klíče, adresy, štítky a historii transakcí před neoprávněným přístupem. Toto heslo je dobré uložit do správce hesel, abyste ho nezapomněli.

![Image](assets/fr/58.webp)

Vaše portfolio je nyní ve Sparrow správně nakonfigurováno.

![Image](assets/fr/59.webp)

## Přijímání bitcoinů

Nyní, když je vaše Jade Plus nakonfigurována, jste připraveni přijmout první saty do své nové peněženky Bitcoin. Chcete-li tak učinit, klikněte na Sparrow na nabídku "*Přijmout*".

![Image](assets/fr/60.webp)

Sparrow zobrazí první prázdnou adresu příjmu ve vašem portfoliu.

![Image](assets/fr/61.webp)

Před jeho použitím jej zkontrolujme na obrazovce Jade Plus, abychom se ujistili, že patří do naší peněženky Bitcoin. Na obrazovce Jade klikněte na "*Scan QR*" a poté naskenujte QR kód adresy zobrazené na Sparrow.

![Image](assets/fr/62.webp)

Zkontrolujte, zda adresa zobrazená na obrazovce zařízení Jade odpovídá adrese zobrazené v aplikaci Sparrow Wallet. Pokud ano, pokračujte kliknutím na zaškrtávací políčko.

![Image](assets/fr/63.webp)

Vaše hardwarová peněženka pak potvrdí, že tato adresa je součástí vaší peněženky a že je v ní uložen příslušný soukromý klíč.

![Image](assets/fr/64.webp)

Pokud je adresa ověřena vaším Jade, můžete ji nyní používat k přijímání bitcoinů. Když je transakce vysílána v síti, objeví se na Sparrow. Počkejte, až obdržíte dostatek potvrzení, abyste mohli transakci považovat za definitivní.

![Image](assets/fr/65.webp)

## Odeslat bitcoiny

Teď, když máte v peněžence několik sátů, můžete také nějaké poslat. Chcete-li tak učinit, klikněte na nabídku "*UTXOs*".

![Image](assets/fr/66.webp)

Vyberte UTXO, které chcete použít jako vstupy pro tuto transakci, a klikněte na "*Odeslat vybrané*".

![Image](assets/fr/67.webp)

Zadejte adresu příjemce, štítek, který vám připomene účel transakce, a částku, kterou chcete na tuto adresu poslat.

![Image](assets/fr/68.webp)

Upravte sazbu poplatku podle aktuálních tržních podmínek a klikněte na "*Vytvořit transakci*".

![Image](assets/fr/69.webp)

Zkontrolujte, zda jsou všechny parametry transakce správné, a poté klikněte na tlačítko "*Finalizovat transakci k podpisu*".

![Image](assets/fr/70.webp)

Kliknutím na "*Show QR*" zobrazíte PSBT (*Partially Signed Bitcoin Transaction*). Sparrow transakci sestavil, ale stále mu chybí podpisy k odemčení bitcoinů použitých na vstupu. Tyto podpisy může provést pouze Jade Plus, který hostí váš seed poskytující přístup k soukromým klíčům potřebným k podpisu transakce.

![Image](assets/fr/71.webp)

Na obrazovce Jade Plus klikněte na "*Scan QR*" a naskenujte PSBT zobrazený na Sparrow.

![Image](assets/fr/72.webp)

Zkontrolujte, zda jsou doručovací adresa a odesílaná částka správné, a poté kliknutím na šipku potvrďte.

![Image](assets/fr/73.webp)

Ujistěte se, že výše poplatku odpovídá vámi zvolené částce, a poté kliknutím na ikonu zaškrtnutí v levém horním rohu rozhraní podepište transakci.

![Image](assets/fr/74.webp)

V aplikaci Sparrow Wallet klikněte na "*Scan QR*" a naskenujte QR kód zobrazený na obrazovce Jade.

![Image](assets/fr/75.webp)

Vaše podepsaná transakce je nyní připravena k odvysílání v síti Bitcoin a zařazení do bloku těžařem. Pokud je vše v pořádku, klikněte na "*Broadcast Transaction*".

![Image](assets/fr/76.webp)

Vaše transakce byla odeslána a čeká na potvrzení.

![Image](assets/fr/77.webp)

Gratulujeme, nyní víte, jak nastavit a používat zařízení Jade Plus v režimu QR. Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji za sdílení!

Chcete-li jít dále, doporučuji tento další návod na Jade Plus, kde jej konfigurujeme přes Bluetooth pomocí mobilní aplikace Green:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0