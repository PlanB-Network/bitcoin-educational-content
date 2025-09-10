---
name: Coin Control
description: Seznamte se s Coin Control, klíčovým nástrojem pro ochranu vašeho soukromí na Bitcoinu
---
![cover](assets/cover.webp)


*Tento tutoriál je převzat z [lekce Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Úvod



Solidnost protokolu Bitcoin je zajištěna jednoduchými klíčovými koncepty. Mezi nimi vyniká transparentnost: všechny bitcoinové transakce jsou veřejné a snadno ověřitelné kýmkoli. Ačkoli je tato vlastnost milníkem protokolu, protože předchází podvodům a zaručuje pravost prostředků, může také představovat výzvu pro důvěrnost. **Zajímalo vás, zda taková transparentnost může ohrozit vaše soukromí?**



Měli byste. Zatímco nashromáždit ne-kyc Satoshi je poměrně snadné, vaše soukromí je nejvíce ohroženo právě ve fázi výdajů.



### Co se stane, když utratíte UTXO



Výdaje Bitcoin nejsou pouhým převodem hodnoty na někoho jiného.



Tím, že spotřebujete některý ze svých UTXO, musíte ve skutečnosti splnit podmínky stanovené pro transparentnost protokolu, protože máte povinnost prokázat, že tyto prostředky vlastníte. Činíte se tedy odpovědnými za :




- vystavit svůj veřejný klíč;
- vytvořit digitální podpis.



Čas výdajů je proto nejkritičtější: **Vydávání Bitcoin je akt, který je třeba provádět vědomě a s co největší kontrolou**.



## Kontrola Coin



V protokolu Bitcoin neexistují položky jako _účet_ nebo _peněžní jednotky_. Koncept UTXO je výborně vysvětlen v následujícím kurzu, který vřele doporučuji:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

S Bitcoin se hromadí a později utrácejí malé nebo velké účetní jednotky měřené v Satoshi, které představují `nevyčerpané transakční výstupy`, **UTXO**, nazývané také `mince`. Když použijete UTXO k vytvoření transakce, jsou zcela zničeny a na jejich místě jsou vytvořeny jiné UTXO.



Softwarové peněženky jsou vyvinuty tak, aby tuto volbu prováděly automaticky, s použitím "náhodně" vybraných mincí, přičemž používají určité algoritmy stanovené protokolem. Jediným kritériem, které tyto algoritmy splňují, je pokrytí částky potřebné k útratě.



V závislosti na algoritmu zvoleném vývojáři mohou míchat dohromady UTXO různého stáří nebo upřednostňovat utrácení nejnovějšího či "nejstaršího". Nejlepší softwarové peněženky, také plánují ponechat uživateli důležitou volbu.



Funkce `Coin Control`, kterou můžete najít také pod názvem `Coin Selection`, je funkce některých softwarových peněženek, která vám umožňuje **ručně vybrat UTXO, které chcete utratit při sestavování transakce**.



Předpokládejme, že máme Wallet se třemi UTXO 21 000, 42 000 a 63 000 Satoshi.



![img](assets/en/01.webp)



Pokud musíte utratit 24 000 Sats a nechat algoritmus provést automatický výběr, dobrý Software Wallet se může rozhodnout zkombinovat UTXO 1 + UTXO 2, aby zaplatil 24k Sats a Miner, čímž vytvoří zbytek, který se vrátí do interního Address počátečního Wallet.



![img](assets/en/02.webp)



Po transakci lze novou situaci v Wallet, která zahrnuje pouze UTXO, shrnout takto.



![img](assets/en/03.webp)



Se správným softwarem a vaší informovaností jste však mohli učinit jinou, v některých ohledech správnější volbu. Například výběrem pouze UTXO2 (od 42 000 Sats).



![img](assets/en/04.webp)



S konečnou situací ve vašem Wallet, na úrovni UTXO, která vypadá jinak než dříve.



![img](assets/en/05.webp)



## Proč ruční coin control?



![img](assets/en/06.webp)



Ve dvou výše uvedených příkladech je zůstatek ve skutečnosti stejný `108 280 Sats`. Po vynaložení 24 000 Sats bychom bez ručního výběru měli v Wallet 2 UTXO; s ručním řízením Coin máme celkem 3.



Otázka, kterou si můžeme položit, je následující: **proč to všechno dělat?** Existují, nebo by mohly existovat, různé důvody, proč jsme nepoužili `UTXO1` **a všechny jsou základem toho, proč je při utrácení jednou z dobrých praktik aktivovat ruční coin control**.



Výběr UTXO umožňuje upřednostnit některé aspekty před jinými. Volba skutečně závisí na cílech, kterých chcete dosáhnout.



### Ochrana osobních údajů



Jednou z hlavních výhod ručního ovládání Coin je **větší soukromí pro plátce**. Vezměme si vždy náš příklad: výdaj 24 000 Satoshi _bez ručního výběru Coin_. Protože Blockchain z Bitcoin je veřejný záznam, může vnější pozorovatel bez stínu pochybností prohlásit, že vstupy `UTXO1 z 21 000 Sats` a `UTXO2 z 42 000 Sats`, stejně jako zbytek, `UTXO5 z 38 280 Sats` **všechny tři patří stejnému uživateli**.



Při ruční volbě `UTXO2` zůstane naopak `UTXO1` zcela rezervován a čeká v sadě UTXO na využití ve vhodnější dobu.



Položka `UTXO1` může pocházet ze zdroje KYC, například z platby přijaté v systému Exchange za zboží a služby, zatímco ostatní položky UTXO nikoli. Míchání UTXO-kyc s jinými, které jsou důvěrnější, ohrožuje soubor anonymity nekyc prostředků.



**Prostředky KYC by nevyhnutelně vedly k odhalení identity plátce. Kdyby to byla tvoje peněženka, chtěl bys, aby mohl externí pozorovatel s tak absolutní jistotou zjistit tvou identitu?**



Zkuste tedy vzít v úvahu, že peněženky, které implementují ruční výběr UTXO, umožňují například **segregaci jednoho nebo více UTXO**, což je funkce, kterou lze v takových situacích použít.



Ačkoli jsem přesvědčen, že prostředky s kyc by měly být vedeny v odděleném Wallet než v Bitcoin zakoupeném bez kyc, pokud je to váš případ, je oddělení některých vašich adres klíčovou pomocí, kterou byste mohli využít tím, že se naučíte ručně vybírat vstupy pro výdaje.



### Úspora poplatků



Výběr správného UTXO pro uskutečnění výdaje **umožňuje optimalizaci poplatků**. Opět vycházíme z našeho původního příkladu, Software Wallet vybral dva UTXO k pokrytí výdaje, který má být uskutečněn. Dva UTXO znamenají dva podpisy, které mají být zobrazeny v síti. Z toho vyplývá, že transakce má větší "váhu" z hlediska vBajtů.



Pomocí ručního ovládání Coin můžete naopak vybrat pouze takovou, která postačuje k pokrytí částky, a ušetřit tak poplatky snížením "váhy" transakce.



V době, kdy jsou poplatky vysoké, ale jste nuceni utratit Bitcoin On-Chain (např. za otevření kanálu Lightning Network), se právě tehdy ukáže, že ovládání Coin je tím správným ekonomickým podnětem, na který se můžete obrátit.



### Sdružování ostatků



Když provedete platbu a použijete Bitcoin On-Chain, možnost obdržení drobných se téměř vždy stává jistotou. Každý zbytek je sám o sobě malou ztrátou soukromí, protože prozrazuje síti (a zejména příjemci platby) váš Address, který může být spojen s vaším zdrojovým vstupem.



Vzhledem k tomu, že nejlepší Wallet HDs generate speciální adresy pro zbytky, můžete je snadno rozpoznat a "oddělit" všechny zbytky různých provedených transakcí; když dosáhnou určité částky, můžete je vybrat ručně a konsolidovat je, nebo přejít na Lightning Network (můj preferovaný způsob) a zpracovat je tak, abyste získali zpět soukromí ztracené při utrácení.



### Výdaje z Cold Wallet



Cold Wallet je nástroj, s nímž lze rozumně získat dobrou míru zabezpečení, uložit libovolné množství finančních prostředků na delší dobu stranou. Mohou však nastat nepředvídané události, a tak vznikne potřeba sáhnout na úspory a pokrýt některé neočekávané výdaje.



Nevím, kolik lidí může sdílet můj přístup, ale moje rada je **nikdy neprovádět výdaje přímo z Cold Wallet, aby nedošlo ke změně mezi adresami stejných**. Naučte se ručně vybrat UTXO potřebné k pokrytí výdaje, přenést je do Wallet Hot a připravit transakci z něj. Případné drobné pak můžete poslat zpět na Cold Wallet Address (pokud je částka adekvátní), použít je na jiné výdaje, nebo je ještě oddělit, jak jsme si právě ukázali.



## Praktická prezentace


Po technickém úvodu o tom, proč, se podívejme, jak využít manuální ovládání Coin v praxi s různým softwarem, stolním i mobilním. Budeme používat vždy stejný Wallet BIP39, importovaný do každého ze zvolených nástrojů, abychom vám ukázali drobné rozdíly mezi nimi.



## Wallet Stolní počítač



### Sparrow



Pokud používáte Sparrow, otevřete Wallet a v nabídce vlevo vyberte možnost _UTXOs_. Zobrazí se seznam všech UTXO přidružených k vašemu Wallet.



Stačí kliknout myší na některou z nich a zvolit možnost _Odeslat vybrané_. Přímo u příkazu Sparrow se po výběru zobrazí také celková částka, kterou lze utratit. Graficky vám Sparrow zobrazí vybraný UTXO jeho zvýrazněním modrou barvou.



![img](assets/en/07.webp)



Můžete jich vybrat i více. Pomozte si klávesou _CTRL_ a vyberte v seznamu nesousedící UTXO.



![img](assets/en/08.webp)



Po ručním výběru UTXO můžete začít sestavovat transakci a Sparrow vám dobře graficky ukáže, jak je sestavena.



![img](assets/en/09.webp)



#### Segregace UTXO



Oddělení finančních prostředků znamená jejich "uzamčení" v rámci systému Wallet, aby nemohly být použity jako vstup pro transakci. Sparrow umožňuje tuto funkci, která je vždy přístupná z nabídky _UTXOs_: umístíte myš nad UTXO, který má být "uzamčen", a kliknete pravým tlačítkem myši. Mezi funkcemi tohoto postupu se objeví _Zamrazení UTXO_. Tímto způsobem budete moci oddělit mince s peněženkami Sparrow.



![img](assets/en/29.webp)



### Electrum



Pokud máte na ploše Wallet Electrum, měli byste vědět, že UTXO můžete ručně vybrat buď z nabídky _Adresy_, nebo z nabídky _Coins_. V obou nabídkách se výběr provádí tak, že najedete myší na požadovaný UTXO a po kliknutí pravým tlačítkem myši zvolíte _Přidat k ovládání Coin_.



![img](assets/en/10.webp)



I pomocí tohoto softwaru můžete vybrat více než jednu jednotku UTXO. Pomůžete si klávesou _CTRL_ na klávesnici, pokud nesousedí vedle sebe.



![img](assets/en/11.webp)



Graficky vám Electrum ukáže výběr zvýrazněním vybraných UTXO v Green, zatímco dole se objeví stejnou barvou zvýrazněný pruh, který ukazuje dostupný zůstatek po kontrole Coin.



![img](assets/en/12.webp)



Po výběru výstupu nebo výstupů můžete sestavit transakci jako obvykle z nabídky _Odeslat_.



#### Segregace UTXO



Electrum tuto funkci nabízí tak, že přejdete do nabídky _Coins_, kde vyberete konkrétní UTXO a poté kliknutím pravým tlačítkem myši zvolíte _Freeze_. Address můžete "zmrazit" i bez prostředků z nabídky _Adresy_ nebo "Coin" neutratit.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk umožňuje ručně vybrat UTXO z hlavní nabídky, jakmile je otevřena. Spusťte aplikaci Nunchuk a klikněte na možnost _Zobrazit mince_.



![img](assets/en/13.webp)



Tím se otevře okno obsahující všechny UTXO v Wallet, kde můžete vybrat jeden nebo více aktivací zaškrtávacího políčka vedle každé částky. Po provedení výběru pokračujte příkazem _Create transaction_ (Vytvořit transakci).



![img](assets/en/14.webp)



Poté můžete zadat cíl Address a nastavit částku a poplatky.



![img](assets/en/15.webp)



#### Segregace UTXO



Pro úplnost dodejme, že Nunchuk mezi svými funkcemi umožňuje také oddělení jednoho (nebo více) UTXO, a to dvěma různými způsoby. Vstupte do nabídky _Zobrazit mince_ a ručně vyberte ze seznamu mincí. Poté klikněte na nabídku _Další_ v pravém dolním rohu: zobrazí se seznam možností, ze kterého můžete vybrat _Zamknout mince_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Kliknutím na místo vyhrazené pro UTXO se také dostanete do okna _Coin details_. Zde se v pravém horním rohu zobrazí příkaz k uzamčení/odemčení daného UTXO.



![img](assets/en/41.webp)



### Aplikace Blockstream



Blockstream App desktop, dříve známý jako Green, umožňuje provést výběr Coin, když jste již začali vytvářet transakci. Otevřete tedy svůj Wallet a klikněte na _Odeslat_.



![img](assets/en/16.webp)



Do příslušného pole vložte cílové číslo Address a poté vyberte možnost _Ruční výběr Coin_.



![img](assets/en/17.webp)



Otevře se okno, ve kterém můžete vybrat jednu nebo více mincí UTXO. V níže uvedeném příkladu jsme vybrali dvě mince. Poté potvrďte svůj výběr kliknutím na tlačítko _Confirm Coin Selection_.



![img](assets/en/18.webp)



Nastavte částku a poplatky a poté normálně pokračujte v transakci.



![img](assets/en/19.webp)



⚠️ N.B. V nabídce _Coins_ v Green jsou položky _Lock_/_Unlock_, které předznamenávají možnost oddělení UTXO. Tato funkce je aktivována pouze u tzv. účtů Multisig; aktivuje se rovněž pouze výběrem UTXO velmi malé částky, blížící se hranici `Dust`.



## Wallet mobilní



Peněženky lze vybírat také z mobilních zařízení, která umožňují ruční výběr UTXO. Jako první příklad uveďme modrou Wallet.



### Modrá Wallet



Jste-li uživatelem této aplikace Wallet, otevřete ji a kliknutím na ni vstupte do ovládacích obrazovek souvisejících s jednou z vašich peněženek. Chcete-li vstoupit do ovládacího manuálu Coin, musíte vstoupit do fáze výdajů a poté kliknout na tlačítko _Odeslat_.



![img](assets/en/21.webp)



Na další obrazovce vyberte nabídky označené třemi tečkami v pravém horním rohu. Otevře se rozbalovací okno s řadou příkazů. Vyberte poslední z nich: _Coin Control_.



![img](assets/en/22.webp)



V tomto okamžiku modrá Wallet zobrazuje všechny vaše UTXO. Kromě částek jsou graficky odlišeny různými barvami.



![img](assets/en/27.webp)



Zvolte UTXO, který chcete vybrat, a poté vyberte možnost _Použít minci_.



![img](assets/en/23.webp)



Modrá Wallet vás vrátí do okna _Odeslat_, kde můžete pokračovat v sestavování transakce. Upravte částku a poplatky a poté zvolte možnost _Další_.



![img](assets/en/24.webp)



V tomto okamžiku můžete transakci ukončit, jak to obvykle děláte.



#### Segregace zařízení UTXO



Modrý Wallet také umožňuje oddělit UTXO, čímž je znepřístupní pro výdaje, což není špatná funkce pro Wallet z mobilního zařízení. K ovládacímu prvku Coin přistupujete právě vysvětleným postupem a po výběru UTXO zvolte místo _Use Coin_ možnost _Freeze_.



![img](assets/en/26.webp)



### Nunchuk



Mobilní verze Nunchuku umožňuje uživateli také ovládání pomocí Coin. Pokud tuto aplikaci používáte z mobilního telefonu, otevřete ji a přejděte do nabídky _Peněženka_. Tam vyberte možnost _Zobrazit mince_.



![img](assets/en/30.webp)



V okně, kde se zobrazí seznam UTXO, klikněte na tlačítko _Vybrat_.



![img](assets/en/38.webp)



Vedle každé položky UTXO se zobrazí funkce výběru. Stejně jako ve verzi pro stolní počítače se ruční výběr na mobilním zařízení Nunchuk provádí zaškrtnutím malého čtverečku vedle částky. Na obrazovce se zobrazí počet vybraných UTXO a celková dostupná částka. Po dokončení klikněte na symbol ₿ v levém dolním rohu, což je příkaz k zahájení sestavení transakce.



![img](assets/en/31.webp)



Nyní můžete transakci dokončit výběrem částky a kliknutím na tlačítko _pokračovat_.



![img](assets/en/32.webp)



Pokračujte jako vždy, vložte cílové místo Address, popis a přizpůsobte nastavení poplatků.



#### Segregace UTXO



UTXO můžete oddělit také pomocí mobilního Nunchuku. Vstupte do okna vyhrazeného seznamu mincí a vyberte šipku vedle UTXO, který chcete segregovat.



![img](assets/en/42.webp)



Zobrazí se prostor vyhrazený pro _Coin details_, kde můžete vybrat možnost _Lock this coin_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper je posledním Wallet, se kterým se v tomto průvodci setkáme. Uvidíme, jak se jeho funkce uplatní při ovládání Coin s jednosignálem Wallet, ačkoli takové použití není účelem právě této aplikace. Po nastavení aplikace Keeper v telefonu ji spusťte a otevřete aplikaci Wallet obsahující nějaké finanční prostředky. Uprostřed hlavní obrazovky klikněte na možnost _Zobrazit všechny mince_.



![img](assets/en/34.webp)



Keeper zobrazuje přehled jednotek UTXO. Na obrazovku výběru se dostanete kliknutím na tlačítko _Vybrat k odeslání_.



![img](assets/en/35.webp)



Mince můžete vybrat tak, že je zaškrtnete kliknutím na příslušný příkaz. Po dokončení klikněte na tlačítko _Odeslat_.



![img](assets/en/36.webp)



Bitcoin Keeper vás přenese přímo do nabídky _Odeslat_, kde můžete sestavit transakci s vybranými UTXO.



![img](assets/en/37.webp)



## Hardware Wallet



Každá ze softwarových peněženek uvedených v této příručce může být pouze hodinkami Interface k jedné z vašich hardwarových peněženek. To znamená, že ovládání Coin pro offline podpisové zařízení se provádí pomocí dosud viděných kroků.



### Obecná doporučení



Kontrola Coin je velmi účinným postupem při výběru vstupů pro transakce. Ruční výběr je ještě efektivnější, pokud jste při nákupu/příjmu finančních prostředků dobře označili zdroj svých Satoshis. Pokud se chcete tuto techniku dobře naučit, doporučuji následující výukový program:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Již dříve jsme hovořili o "segregaci ostatků". Pokud chcete pozůstatky uzamknout pro pozdější zpracování a získat zpět soukromí (výměna na Layer 2), musíte dbát na to, abyste je při každém přijetí `označili`. Z dosud viděných softwarových peněženek pouze Electrum graficky obarvuje zbytky UTXO, aby byly na první pohled viditelné. Ostatní, jako například Sparrow, vám zobrazují řetězec v derivační cestě jednotlivých UTXO (`m/84'/0'/0'/1/11`).



Chcete-li tuto techniku účinně použít, nezapomeňte vždy přidat popis na přijatou směnku: osoba, které jste poslali své prostředky (platbu, výukový program nebo jiné), zná kód Address spojený se směnkou a ví, že patří vám, protože pochází z transakce, kterou jste provedli společně!