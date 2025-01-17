---
name: Blockstream Green - Liquid
description: Nastavení portfolia v postranním řetězci sítě Liquid Network
---
![cover](assets/cover.webp)

Protokol bitcoinu má záměrná technická omezení, která pomáhají udržet decentralizaci sítě a zajišťují, že bezpečnost je rozdělena mezi všechny uživatele. Tato omezení však mohou někdy uživatele frustrovat, zejména v době přetížení sítě v důsledku velkého množství souběžných transakcí. Debata o škálovatelnosti Bitcoinu dlouho rozdělovala komunitu, zejména během války o velikost bloků. Od této epizody je v komunitě bitcoinů všeobecně uznáváno, že škálovatelnost musí být zajištěna řešeními mimo řetězec, v systémech druhé vrstvy. Mezi tato řešení patří sidechainy, které jsou ve srovnání s jinými systémy, jako je Lightning Network, stále relativně neznámé a málo používané.

Sidechain je nezávislý blockchain, který funguje paralelně s hlavním blockchainem Bitcoinu. Používá bitcoin jako zúčtovací jednotku díky mechanismu zvanému "*two-way peg*". Tento systém umožňuje uzamknout bitcoiny v hlavním řetězci, aby bylo možné reprodukovat jejich hodnotu v sidechainu, kde obíhají ve formě tokenů krytých původními bitcoiny. Tyto tokeny si obvykle zachovávají paritu hodnoty s bitcoiny uzamčenými na hlavním řetězci a tento proces lze zvrátit a získat zpět prostředky na Bitcoinu.

Cílem sidechainů je nabídnout další funkce nebo technická vylepšení, jako jsou rychlejší transakce, nižší poplatky nebo podpora chytrých smluv. Tyto inovace nelze vždy implementovat přímo do bitcoinového blockchainu, aniž by byla ohrožena jeho decentralizace nebo bezpečnost. Sidechainy proto umožňují testovat a zkoumat nová řešení při zachování integrity Bitcoinu. Tyto protokoly však často vyžadují kompromisy, zejména pokud jde o decentralizaci a bezpečnost, v závislosti na zvoleném modelu správy a konsensuálním mechanismu.

Dnes je nejznámějším sidechainem pravděpodobně Liquid. V tomto tutoriálu vám nejprve povím, co je Liquid, a poté vás provedu tím, jak ho začít snadno používat s aplikací Blockstream Green, abyste mohli využívat všechny jeho výhody.

![LIQUID GREEN](assets/fr/01.webp)

## Co je Liquid Network?

Liquid je federativní překryvný sidechain pro Bitcoin, který vyvinula společnost Blockstream s cílem zvýšit rychlost, důvěrnost a funkčnost transakcí. Využívá dvoustranný mechanismus ukotvení vytvořený na federaci k uzamčení bitcoinů na hlavním řetězci a na oplátku vytváří Liquid-bitcoiny (L-BTC), tokeny obíhající na Liquidu, přičemž zůstávají kryté původními bitcoiny.

![LIQUID GREEN](assets/fr/02.webp)

Síť Liquid se opírá o federaci účastníků, kterou tvoří uznávané subjekty z ekosystému bitcoinu, jež ověřují bloky a spravují dvoustranné peggingy. Kromě L-BTC umožňuje Liquid také vydávání dalších digitálních aktiv, jako jsou stablecoiny a jiné kryptoměny.

![LIQUID GREEN](assets/fr/03.webp)

## Představujeme Blockstream Green

Blockstream Green je softwarová peněženka dostupná na mobilních zařízeních a počítačích. Tato peněženka, dříve známá jako *Green Address*, se po akvizici v roce 2016 stala projektem společnosti Blockstream.

Zelená je mimořádně snadno použitelná aplikace, která je zajímavá i pro začátečníky. Nabízí všechny základní funkce dobré bitcoinové peněženky, včetně RBF (*Replace-by-Fee*), možnosti připojení přes Tor, možnosti připojení vlastního uzlu, SPV (*Simple Payment Verification*), označování mincí a kontroly.

Blockstream Green podporuje také síť Liquid a právě to se dozvíme v tomto tutoriálu. Pokud byste chtěli Green používat i pro jiné aplikace, doporučuji vám podívat se i na tyto další návody:

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da
https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb
## Instalace a konfigurace aplikace Blockstream Green

Prvním krokem je samozřejmě stažení zelené aplikace. Přejděte do svého obchodu s aplikacemi:

- [Pro Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Pro Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![LIQUID GREEN](assets/fr/04.webp)

Uživatelé systému Android mohou aplikaci nainstalovat také prostřednictvím souboru `.apk` [dostupného na GitHubu společnosti Blockstream](https://github.com/Blockstream/green_android/releases).

![LIQUID GREEN](assets/fr/05.webp)

Spusťte aplikaci a zaškrtněte políčko "Souhlasím s podmínkami...*".

![LIQUID GREEN](assets/fr/06.webp)

Při prvním otevření aplikace Green se zobrazí domovská obrazovka bez nakonfigurovaného portfolia. Pokud později vytvoříte nebo importujete portfolia, zobrazí se v tomto rozhraní. Než přejdete k vytváření portfolia, doporučuji upravit nastavení aplikace tak, aby vyhovovalo vašim potřebám. Klepněte na tlačítko "Nastavení aplikace".

![LIQUID GREEN](assets/fr/07.webp)

Možnost "*Zvýšené soukromí*", která je k dispozici pouze v systému Android, zvyšuje soukromí tím, že vypíná snímky obrazovky a skrývá náhledy aplikací. Automaticky také uzamkne přístup k aplikacím, jakmile je telefon uzamčen, čímž ztíží odhalení vašich dat.

![LIQUID GREEN](assets/fr/08.webp)

Pro ty, kteří chtějí zvýšit své soukromí, nabízí aplikace možnost zakořenit svůj provoz prostřednictvím sítě Tor, která šifruje všechna vaše připojení a ztěžuje vysledování vašich aktivit. Ačkoli tato možnost může mírně zpomalit provoz aplikace, pro ochranu vašeho soukromí ji vřele doporučujeme, zejména pokud nepoužíváte vlastní kompletní uzel.

![LIQUID GREEN](assets/fr/09.webp)

Uživatelům, kteří mají vlastní kompletní uzel, nabízí Zelená peněženka možnost připojit se k němu prostřednictvím serveru Electrum, což zaručuje úplnou kontrolu nad informacemi o síti Bitcoin a šířením transakcí. Tato funkce je však určena pro klasické bitcoinové peněženky, takže pokud používáte Liquid, nepotřebujete ji.

![LIQUID GREEN](assets/fr/10.webp)

Další alternativní funkcí je možnost "*SPV Verification*", která umožňuje přímo ověřit určitá data blockchainu a snížit tak potřebu důvěřovat výchozímu uzlu Blockstream, ačkoli tato metoda neposkytuje všechny záruky plnohodnotného uzlu. Opět to ovlivní pouze vaše onchain peněženky Bitcoin, nikoliv Liquid.

![LIQUID GREEN](assets/fr/11.webp)

Po úpravě těchto nastavení podle svých potřeb klikněte na tlačítko "*Uložit*" a restartujte aplikaci.

![LIQUID GREEN](assets/fr/12.webp)

## Vytvoření portfolia Liquid na Blockstream Green

Nyní jste připraveni vytvořit portfolio Liquid. Klikněte na tlačítko "*Začít*".

![LIQUID GREEN](assets/fr/13.webp)

Můžete si vybrat mezi vytvořením místní softwarové peněženky nebo správou chladné peněženky prostřednictvím hardwarové peněženky. V tomto návodu se zaměříme na vytvoření horké peněženky na zařízení Liquid, takže budete muset vybrat možnost "*Na tomto zařízení*". K zabezpečení peněženky Liquid můžete použít také kompatibilní hardwarovou peněženku, například Blockstream Jade.

![LIQUID GREEN](assets/fr/14.webp)

Poté můžete obnovit stávající peněženku Bitcoin nebo vytvořit novou. Pro účely tohoto návodu budeme vytvářet novou peněženku. Pokud však potřebujete obnovit stávající peněženku Liquid z její mnemotechnické fráze, například po ztrátě hardwarové peněženky, budete muset zvolit druhou možnost.

![LIQUID GREEN](assets/fr/15.webp)

Poté si můžete vybrat mezi mnemotechnickou frází o 12 nebo 24 slovech. Tato fráze vám v případě problému s telefonem umožní obnovit přístup k peněžence z jakéhokoli kompatibilního softwaru. V současné době nenabízí volba 24slovné fráze větší zabezpečení než 12slovná fráze. Proto doporučuji zvolit mnemotechnickou frázi o 12 slovech.

Zelená vám pak poskytne mnemotechnickou frázi. Než budete pokračovat, ujistěte se, že vás nikdo nesleduje. Kliknutím na "*Zobrazit frázi pro obnovení*" ji zobrazíte na obrazovce.

![LIQUID GREEN](assets/fr/16.webp)

**Tato mnemotechnická pomůcka vám dává plný a neomezený přístup ke všem vašim bitcoinům ** Kdokoli, kdo má tuto mnemotechnickou pomůcku, může ukrást vaše peníze, a to i bez fyzického přístupu k vašemu telefonu.

Obnovuje přístup k bitcoinům v případě ztráty, krádeže nebo rozbití telefonu. Proto je velmi důležité pečlivě zálohovat **na fyzickém médiu (ne digitálním)** a uchovávat je na bezpečném místě. Můžete si ji zapsat na kus papíru, nebo pro větší bezpečnost, pokud se jedná o velkou peněženku, doporučuji vyrýt ji na nerezový nosič, který ji ochrání před rizikem požáru, povodně nebo zřícení (u horké peněženky určené k zabezpečení malého množství bitcoinů pravděpodobně postačí jednoduchá papírová záloha).

*Tato slova samozřejmě nikdy nesmíte sdílet na internetu, jako to dělám já v tomto návodu. Toto ukázkové portfolio bude použito pouze v síti Liquid Testnet a po skončení výukového kurzu bude smazáno.*

![LIQUID GREEN](assets/fr/17.webp)

Po správném nahrání mnemotechnické fráze na fyzické médium klikněte na "*Pokračovat*". Zelená peněženka vás poté požádá o potvrzení některých slov ve vaší mnemotechnické frázi, abyste se ujistili, že jste je zaznamenali správně. Vyplňte prázdná místa chybějícími slovy.

![LIQUID GREEN](assets/fr/18.webp)

Zvolte PIN kód zařízení, který se použije k odemknutí zelené peněženky. To je vaše ochrana proti neoprávněnému fyzickému přístupu. Tento kód PIN se nepodílí na odvozování kryptografických klíčů vaší peněženky. Takže i bez přístupu k tomuto kódu PIN vám vlastnictví vaší 12- nebo 24slovné mnemotechnické fráze umožní znovu získat přístup k vašim bitcoinům.

Doporučujeme zvolit co nejnáhodnější šestimístný kód PIN. Nezapomeňte si tento kód uložit, abyste ho nezapomněli, jinak budete nuceni peněženku načítat z mnemotechniky. Poté můžete přidat možnost biometrického blokování, abyste nemuseli zadávat kód PIN při každém použití. Obecně platí, že biometrické údaje jsou mnohem méně bezpečné než samotný kód PIN. Ve výchozím nastavení tedy doporučuji tuto možnost odemykání nenastavovat.

![LIQUID GREEN](assets/fr/19.webp)

Zadejte PIN podruhé a potvrďte jej.

![LIQUID GREEN](assets/fr/20.webp)

Počkejte, až se vytvoří vaše portfolio, a klikněte na tlačítko "*Vytvořit účet*".

![LIQUID GREEN](assets/fr/21.webp)

V poli "*Active*" vyberte možnost "*Liquid Bitcoin*". Poté si můžete vybrat mezi standardní peněženkou s jedním podpisem, kterou budeme používat v tomto návodu, nebo peněženkou chráněnou dvoufaktorovým ověřováním (2FA).

![LIQUID GREEN](assets/fr/22.webp)

A je to, vaše peněženka Liquid byla vytvořena pomocí aplikace Green!

![LIQUID GREEN](assets/fr/23.webp)

Než obdržíte své první bitcoiny do peněženky Liquid, **důrazně vám doporučuji provést test obnovy prázdné peněženky**. Zaznamenejte si některé referenční údaje, jako je vaše xpub nebo první přijímací adresa, a poté peněženku v aplikaci Green vymažte, dokud je ještě prázdná. Poté zkuste peněženku obnovit v aplikaci Zelená pomocí papírových záloh. Zkontrolujte, zda informace o souboru cookie vygenerované po obnovení odpovídají těm, které jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé. Další informace o tom, jak provést zkušební obnovu, najdete v tomto dalším návodu:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Nastavení portfolia kapalin

Pokud si chcete portfolio přizpůsobit, klikněte na tři malé tečky v pravém horním rohu.

![LIQUID GREEN](assets/fr/24.webp)

Možnost "*Přejmenovat*" umožňuje přizpůsobit název portfolia, což je užitečné zejména v případě, že v jedné aplikaci spravujete více portfolií.

![LIQUID GREEN](assets/fr/25.webp)

Nabídka "*Unit*" umožňuje změnit základní jednotku peněženky. Můžete například zvolit, že se má zobrazovat v satoších, a ne v bitcoinech.

![LIQUID GREEN](assets/fr/26.webp)

Nabídka "*Nastavení*" poskytuje přístup k různým možnostem vaší peněženky Bitcoin.

![LIQUID GREEN](assets/fr/27.webp)

Zde například najdete svůj *deskriptor*, který se může hodit, pokud plánujete z tohoto portfolia Liquid vytvořit portfolio pouze pro hodinky.

![LIQUID GREEN](assets/fr/28.webp)

Můžete také změnit PIN peněženky a aktivovat biometrické připojení.

![LIQUID GREEN](assets/fr/29.webp)

## Používání portfolia Liquid

Nyní, když je vaše portfolio Liquid nastaveno, jste připraveni přijímat své první L-saty!

Pokud ještě nemáte L-BTC, máte několik možností. První z nich je nechat si je poslat přímo na váš účet. Pokud vám chce někdo zaplatit v bitcoinech na Liquidu, stačí mu dát adresu příjemce. Druhou možností je vyměnit své bitcoiny onchain nebo v síti Lightning za L-BTC. K tomu můžete použít [bridge, například Boltz](https://boltz.exchange/). Jednoduše na webu zadejte svou adresu Liquid a poté proveďte platbu buď prostřednictvím sítě Lightning, nebo onchain.

![LIQUID GREEN](assets/fr/30.webp)

Chcete-li vygenerovat adresu kapaliny, klikněte na tlačítko "*Přijmout*".

![LIQUID GREEN](assets/fr/31.webp)

Zelená barva pak zobrazí první prázdnou přijímací adresu v peněžence. Můžete buď naskenovat přidružený QR kód, nebo adresu přímo zkopírovat a odeslat L-BTC.

![LIQUID GREEN](assets/fr/32.webp)

Jakmile je transakce odvysílána v síti, objeví se ve vaší peněžence.

![LIQUID GREEN](assets/fr/33.webp)

Počkejte, až obdržíte dostatek potvrzení, abyste mohli transakci považovat za definitivní. V systému Liquid by potvrzení měla být rychlá, protože blok je zveřejňován každou minutu.

![LIQUID GREEN](assets/fr/34.webp)

S L-sat ve svém portfoliu Liquid je nyní můžete také odesílat. Klikněte na "*Odeslat*".

![LIQUID GREEN](assets/fr/35.webp)

Na další stránce zadejte adresu příjemce Liquid. Můžete ji zadat ručně nebo naskenovat její QR kód.

![LIQUID GREEN](assets/fr/36.webp)

Zvolte výši platby.

![LIQUID GREEN](assets/fr/37.webp)

Kliknutím na tlačítko "*Další*" přejděte na obrazovku se souhrnem transakcí. Zkontrolujte, zda jsou adresa, částka a poplatky správné.

![LIQUID GREEN](assets/fr/38.webp)

Pokud vše proběhne v pořádku, posunutím zeleného tlačítka v dolní části obrazovky doprava transakci podepíšete a odešlete do sítě Bitcoin.

![LIQUID GREEN](assets/fr/39.webp)

Vaše transakce se nyní objeví na panelu peněženky Bitcoin a čeká na potvrzení.

![LIQUID GREEN](assets/fr/40.webp)

A nyní víte, jak snadno používat Liquid sidechain pomocí aplikace Blockstream Green!

Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Moc vám děkuji!

Doporučuji vám také podívat se na tento další komplexní návod na mobilní aplikaci Blockstream Green pro nastavení onchain bitcoinové peněženky:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143