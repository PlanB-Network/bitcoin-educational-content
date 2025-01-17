---
name: Aqua
description: Bitcoin, Lightning a Liquid v jedné peněžence
---
![cover](assets/cover.webp)

Aqua je mobilní aplikace, která umožňuje snadno vytvořit hot wallet pro Bitcoin a Liquid a díky integrovaným swapům nabízí také možnost používat Lightning bez složité správy uzlu. Umožňuje také správu stablecoinů USDT v různých sítích.

Aplikace Aqua, kterou vyvinula společnost JAN3 pod vedením Samsona Mowa, byla původně navržena speciálně pro potřeby uživatelů v Latinské Americe, i když je vhodná pro všechny uživatele na celém světě. Zajímavá je zejména pro začátečníky a pro ty, kteří používají Bitcoin ke svým platbám denně.

V tomto návodu se dozvíte, jak používat mnoho funkcí systému Aqua. Ještě předtím si ale na chvíli uvědomíme, co je to sidechain v Bitcoinu a jak funguje Liquid, abychom plně pochopili hodnotu Aqua.

![AQUA](assets/fr/01.webp)

## Co je to postranní řetězec?

Protokol bitcoinu má záměrná technická omezení, která pomáhají udržet decentralizaci sítě a zajišťují, že bezpečnost je rozdělena mezi všechny uživatele. Tato omezení však mohou někdy uživatele frustrovat, zejména v době přetížení sítě v důsledku velkého množství souběžných transakcí. Debata o škálovatelnosti Bitcoinu dlouho rozdělovala komunitu, zejména během války o velikost bloků. Od této epizody je v komunitě bitcoinů všeobecně uznáváno, že škálovatelnost musí být zajištěna řešeními mimo řetězec, v systémech druhé vrstvy. Mezi tato řešení patří sidechainy, které jsou ve srovnání s jinými systémy, jako je Lightning Network, stále relativně neznámé a málo používané.

Sidechain je nezávislý blockchain, který funguje paralelně s hlavním blockchainem Bitcoinu. Používá bitcoin jako zúčtovací jednotku díky mechanismu zvanému "*two-way peg*". Tento systém umožňuje uzamknout bitcoiny v hlavním řetězci, aby bylo možné reprodukovat jejich hodnotu v sidechainu, kde obíhají ve formě tokenů krytých původními bitcoiny. Tyto tokeny si obvykle zachovávají paritu hodnoty s bitcoiny uzamčenými na hlavním řetězci a tento proces lze zvrátit a získat zpět prostředky na Bitcoinu.

Cílem sidechainů je nabídnout další funkce nebo technická vylepšení, jako jsou rychlejší transakce, nižší poplatky nebo podpora chytrých smluv. Tyto inovace nelze vždy implementovat přímo do bitcoinového blockchainu, aniž by byla ohrožena jeho decentralizace nebo bezpečnost. Sidechainy proto umožňují testovat a zkoumat nová řešení při zachování integrity Bitcoinu. Tyto protokoly však často vyžadují kompromisy, zejména pokud jde o decentralizaci a bezpečnost, v závislosti na zvoleném modelu správy a konsensuálním mechanismu.

## Co je to tekutina?

Liquid je federativní překryvný sidechain pro Bitcoin, který vyvinula společnost Blockstream s cílem zvýšit rychlost, důvěrnost a funkčnost transakcí. Využívá dvoustranný mechanismus ukotvení vytvořený na federaci k uzamčení bitcoinů na hlavním řetězci a na oplátku vytváří Liquid-bitcoiny (L-BTC), tokeny obíhající na Liquidu, přičemž zůstávají kryté původními bitcoiny.

![AQUA](assets/fr/02.webp)

Síť Liquid se opírá o federaci účastníků, kterou tvoří uznávané subjekty z ekosystému bitcoinu, které ověřují bloky a spravují dvoustranné peggingy. Kromě L-BTC umožňuje Liquid také vydávání dalších digitálních aktiv, jako je stablecoin USDT a další kryptoměny.

![AQUA](assets/fr/03.webp)

## Instalace aplikace Aqua

Prvním krokem je samozřejmě stažení aplikace Aqua. Přejděte do svého obchodu s aplikacemi:

- [Pro Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Pro Apple](https://apps.apple.com/us/app/aqua-wallet/id6468594241).
![AQUA](assets/fr/04.webp)

Uživatelé systému Android mají také možnost nainstalovat aplikaci prostřednictvím souboru `.apk` [dostupného na jejich GitHubu](https://github.com/AquaWallet/aqua-wallet/releases).

![AQUA](assets/fr/05.webp)

Spusťte aplikaci a zaškrtněte políčko "*Seznámil jsem se s podmínkami služby a zásadami ochrany osobních údajů* a souhlasím s nimi".

![AQUA](assets/fr/06.webp)

## Vytvořte si portfolio na Aqua

Klikněte na tlačítko "*Vytvořit peněženku*".

![AQUA](assets/fr/07.webp)

A voilà, vaše portfolio je již vytvořeno!

![AQUA](assets/fr/08.webp)

Především je však nutné, vzhledem k tomu, že se jedná o peněženku pro vlastní úschovu, vytvořit si fyzickou zálohu mnemotechnické pomůcky. **Tato mnemotechnická peněženka vám dává plný, neomezený přístup ke všem vašim bitcoinům**. Kdokoli, kdo má tuto mnemotechniku, může vaše prostředky ukrást, a to i bez fyzického přístupu k vašemu telefonu.

Umožňuje obnovit přístup k bitcoinům v případě ztráty, krádeže nebo rozbití telefonu. Je proto velmi důležité pečlivě je uložit na fyzické médium (nikoli digitální) a uložit je na bezpečném místě. Můžete si ji zapsat na kus papíru, nebo pro větší bezpečnost, pokud se jedná o velkou peněženku, bych doporučoval vyrýt ji na nerezový nosič, který ji ochrání před rizikem požáru, povodně nebo zřícení (u horké peněženky určené k zabezpečení malého množství bitcoinů pravděpodobně postačí jednoduchá papírová záloha).

Za tímto účelem klikněte na nabídku Nastavení.

![AQUA](assets/fr/09.webp)

Poté klikněte na "*Zobrazit klíčovou frázi*". Vytvořte fyzickou zálohu této 12slovné fráze.

![AQUA](assets/fr/10.webp)

Ve stejné nabídce nastavení můžete také změnit jazyk aplikace a použitou fiat měnu.

![AQUA](assets/fr/11.webp)

Než obdržíte své první bitcoiny do peněženky, **důrazně doporučuji provést test obnovy prázdné peněženky**. Zaznamenejte si některé referenční údaje, jako je vaše xpub nebo první přijímací adresa, a poté peněženku v aplikaci Aqua vymažte, dokud je ještě prázdná. Poté zkuste peněženku v aplikaci Aqua obnovit pomocí papírových záloh. Zkontrolujte, zda informace o souboru cookie vygenerované po obnovení odpovídají těm, které jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé. Další informace o tom, jak provést zkušební obnovu, naleznete v tomto dalším návodu:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

On to na mém displeji nevidíte, protože používám emulátor, ale v nastavení najdete také možnost zamknout aplikaci pomocí biometrického ověřování. Důrazně doporučuji tuto funkci aktivovat, protože bez ní může kdokoliv, kdo získá přístup k vašemu odemčenému telefonu, ukrást vaše bitcoiny. Na iOS můžete použít Face ID, na Androidu otisk prstu. Pokud by tyto metody při ověřování selhaly, stále byste mohli získat přístup k aplikaci prostřednictvím PIN kódu vašeho telefonu.


## Přijímání bitcoinů na platformě Aqua

Nyní, když je vaše peněženka nastavena, jste připraveni přijímat první saty! Jednoduše klikněte na tlačítko "*Přijmout*" v nabídce "*Peněženka*".

![AQUA](assets/fr/12.webp)

Můžete si vybrat, zda chcete přijímat bitcoiny v řetězci, v systému Liquid nebo prostřednictvím blesku.

![AQUA](assets/fr/13.webp)

Pro transakce v řetězci Aqua vygeneruje konkrétní přijímací adresu, na které můžete přijímat saty.

![AQUA](assets/fr/14.webp)

Podobně vám společnost Aqua poskytne adresu Liquid, pokud zvolíte Liquid.

![AQUA](assets/fr/15.webp)

Pokud dáváte přednost přijímání prostředků prostřednictvím blesku, musíte nejprve zadat požadovanou částku.

![AQUA](assets/fr/16.webp)

Poté klikněte na "*Generovat fakturu*".

![AQUA](assets/fr/17.webp)

Aqua vytvoří fakturu pro příjem prostředků z peněženky Lightning. Upozorňujeme, že na rozdíl od možností onchain a Liquid budou prostředky přijaté prostřednictvím Lightningu automaticky převedeny na L-BTC na Liquidu pomocí nástroje Boltz, protože Aqua není uzlem Lightningu. Tento proces vám umožňuje přijímat a odesílat prostředky prostřednictvím Lightning, ale bez toho, abyste své bitcoiny kdy ukládali na Lightning.

![AQUA](assets/fr/18.webp)

Osobně začnu tím, že budu posílat bitcoiny přes Lightning do Aqua. Po dokončení transakce s poskytnutou fakturou obdržíme potvrzení.

![AQUA](assets/fr/19.webp)

Chcete-li sledovat průběh výměny, vraťte se na domovskou stránku své peněženky a klikněte na účet "*L2 Bitcoin*", kde jsou uvedeny transakce Lightning (prostřednictvím výměny) a Liquid.

![AQUA](assets/fr/20.webp)

Zde si můžete prohlédnout své transakce a zůstatek L-BTC.

![AQUA](assets/fr/21.webp)

## Výměna bitcoinů se společností Aqua

Když máte aktiva v peněžence Aqua, můžete je přímo z aplikace vyměnit, a to buď do hlavního blockchainu bitcoinů, nebo do Liquidu. Své bitcoiny můžete také převést na stablecoin USDT (nebo jiné). Chcete-li tak učinit, přejděte do nabídky "*Marketplace*".

![AQUA](assets/fr/22.webp)

Klikněte na "*Swaps*".

![AQUA](assets/fr/23.webp)

V poli "*Převod z*" vyberte aktivum, se kterým chcete obchodovat. V současné době vlastním pouze L-BTC, takže vybírám toto aktivum.

![AQUA](assets/fr/24.webp)

V poli "*Převést na*" vyberte cílové aktivum pro výměnu. Já jsem si vybral USDT v síti Liquid.

![AQUA](assets/fr/25.webp)

Zadejte částku, kterou chcete převést.

![AQUA](assets/fr/26.webp)

Potvrďte kliknutím na "*Pokračovat*".

![AQUA](assets/fr/27.webp)

Ujistěte se, že jste s nastavením výměny spokojeni, a potvrďte jej přetažením tlačítka "*Výměna*" v dolní části obrazovky.

![AQUA](assets/fr/28.webp)

Vaše výměna je nyní potvrzena.

![AQUA](assets/fr/29.webp)

Když se podíváme zpět na naše portfolio, vidíme, že nyní máme USDT na Liquidu.

![AQUA](assets/fr/30.webp)

## Odesílání bitcoinů pomocí aplikace Aqua

Když už máte bitcoiny v peněžence Aqua, můžete je poslat. Klikněte na tlačítko "*Odeslat*".

![AQUA](assets/fr/31.webp)

Vyberte aktivum, které chcete odeslat, nebo síť, ve které chcete transakci provést. Já budu posílat bitcoiny přes Lightning.

![AQUA](assets/fr/32.webp)

Dále zadejte informace potřebné k odeslání platby: v případě onchainu nebo Liquid bitcoins je třeba zadat přijímací adresu, v případě Lightningu je vyžadována faktura. Tyto informace můžete vložit přímo do určeného pole nebo pomocí ikony QR kódu otevřít fotoaparát a naskenovat adresu nebo fakturu. Poté klikněte na tlačítko "*Pokračovat*".

![AQUA](assets/fr/33.webp)

Pokud se všechny informace zdají být správné, klikněte znovu na tlačítko "*Pokračovat*".

![AQUA](assets/fr/34.webp)

Aqua vám poté zobrazí shrnutí transakce. Zkontrolujte, zda jsou všechny informace správné, včetně cílové adresy, poplatků a částky. Transakci potvrdíte posunutím tlačítka "*Posunout k odeslání*" ve spodní části obrazovky.

![AQUA](assets/fr/35.webp)

Poté obdržíte potvrzení o odeslání zásilky.

![AQUA](assets/fr/36.webp)

Nyní tedy víte, jak pomocí aplikace Aqua přijímat a utrácet peníze v Bitcoinech, Lightningu a Liquidu, a to vše z jediného rozhraní.

Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Moc vám děkuji!

Doporučuji vám také podívat se na tento další komplexní návod na mobilní aplikaci Blockstream Green, která je dalším zajímavým řešením pro nastavení peněženky Liquid :

https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a