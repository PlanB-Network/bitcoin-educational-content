---
name: JoinBot
description: Porozumění a používání JoinBotu
---

![DALL·E – samurajský robot v červeném lese, 3D render](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů Samourai Wallet a zabavení jejich serverů 24. dubna **služba JoinBot již není dostupná**. Od této chvíle již není možné toto nástroje používat. Nicméně, stále můžete provádět Stonewall X2, ale musíte najít spolupracovníka a ručně vyměňovat PSBTs. Tato služba může být v nadcházejících měsících znovu spuštěna v závislosti na vývoji případu.*

_Sledujeme vývoj tohoto případu stejně jako vývoj souvisejících nástrojů. Ujistěte se, že tento tutoriál aktualizujeme, jakmile budou k dispozici nové informace._

_Tento tutoriál je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

JoinBot je nový nástroj, který byl přidán do sady Samourai Wallet s poslední aktualizací 0.99.98f slavného softwaru pro Bitcoin peněženku. Umožňuje vám snadno provést spolupracující transakci za účelem optimalizace vašeho soukromí, aniž byste museli hledat partnera.

*Díky vynikajícímu Fanisovi Michalakisovi za nápad použít DALL-E pro miniaturu!*

## Co je spolupracující transakce na Bitcoinu?

Bitcoin je založen na distribuovaném a transparentním účetním knize. Každý je schopen sledovat transakce uživatelů tohoto elektronického platebního systému. Aby bylo zajištěno určité úroveň soukromí, mohou uživatelé Bitcoinu provádět transakce se specifickou strukturou, aby přidali věrohodné popření ve své interpretaci.

Nápad není přímo skrýt informace, ale zamíchat je mezi ostatní. Tento cíl se používá v Coinjoins, transakcích, které přerušují historii mince na Bitcoinu a činí její sledování složitým. Pro dosažení tohoto výsledku musí být ve transakci vytvořeny více vstupů a výstupů stejné částky.

Vstupy jsou vstupy Bitcoinové transakce a výstupy představují výstupy. Transakce spotřebuje své vstupy k vytvoření nových výstupů změnou podmínek utrácení mince. Tento mechanismus umožňuje přesun bitcoinů mezi uživateli.
Toto podrobně rozebírám v tomto článku: Mechanismus Bitcoinové transakce: UTXO, Vstupy a Výstupy.

Jedním ze způsobů, jak zamaskovat stopy v Bitcoinové transakci, je provést spolupracující transakci. Jak název napovídá, zahrnuje dohodu mezi více uživateli, z nichž každý vloží sumu bitcoinů jako vstup do stejné transakce a obdrží sumu jako výstup.

Jak bylo zmíněno dříve, nejznámější struktura spolupracující transakce je Coinjoin. Například v protokolu Coinjoin Whirlpool zahrnují transakce 5 účastníků jako vstupy a výstupy, každý se stejným množstvím bitcoinů.

![Diagram transakce Coinjoin na Whirlpool](assets/1.webp)

Externí pozorovatel této transakce nebude schopen vědět, který výstup patří kterému uživateli jako vstup. Pokud vezmeme příklad uživatele č. 4 (fialový), můžeme rozpoznat jejich vstupní UTXO, ale nebudeme vědět, který z 5 výstupů je ve skutečnosti jejich. Původní informace nejsou skryty, ale spíše zamíchány v rámci skupiny.
Uživatel je schopen popřít vlastnictví určitého UTXO jako výstup. Tento jev se nazývá "věrohodné popření" a umožňuje důvěrnost v transparentní Bitcoinové transakci.

Chcete-li se dozvědět více o Coinjoin, vše vysvětluji v tomto dlouhém článku: Porozumění a používání CoinJoin na Bitcoinu.
Ačkoliv je Coinjoin velmi účinný při přerušování sledování UTXO, není vhodný pro přímé výdaje. Jeho struktura totiž vyžaduje použití vstupů předem definovaného množství a výstupů stejné hodnoty (modulo těžební poplatky). Avšak transakce výdajů na Bitcoinu je kritickým okamžikem pro soukromí, protože často vytváří fyzické spojení mezi uživatelem a jeho aktivitou na řetězci. Zdá se tedy nezbytné používat nástroje pro ochranu soukromí při výdajích. Existují i další kolaborativní transakční struktury speciálně navržené pro skutečné platební transakce.
## Transakce StonewallX2

Mezi množstvím nástrojů pro výdaje nabízených v peněžence Samourai Wallet se nachází kolaborativní transakce StonewallX2. Jedná se o mini Coinjoin mezi dvěma uživateli určený pro platbu. Zvenčí může tato transakce vést k několika možným interpretacím. Poskytuje tedy věrohodné popření a následně důvěrnost pro uživatele.

Nastavení kolaborativní transakce StonewallX2 je dostupné v peněženkách Samourai Wallet a Sparrow Wallet. Tento nástroj je interoperabilní mezi oběma softwary.

Jeho mechanismus je poměrně jednoduchý na pochopení. Zde je, jak funguje v praxi:

> - Uživatel chce provést platbu v bitcoinech (například obchodníkovi).
> - Získají přijímací adresu skutečného příjemce platby (obchodníka).
> - Sestaví specifickou transakci s několika vstupy: alespoň jeden patřící jim a jeden patřící externímu spolupracovníkovi.
> - Transakce bude mít 4 výstupy, včetně 2 stejných částek: jedna na adresu obchodníka pro platbu, jedna jako vrácení peněz uživateli, jeden výstup stejné hodnoty jako platba, který jde spolupracovníkovi, a další výstup, který se také vrací spolupracovníkovi.

Například zde je typická transakce StonewallX2, při které jsem provedl platbu 50,125 sats. První vstup 102,588 sats pochází z mé peněženky Samourai. Druhý vstup 104,255 sats pochází z peněženky mého spolupracovníka:

![Diagram transakce StonewallX2](assets/2.webp)

Můžeme pozorovat 4 výstupy, včetně 2 stejných částek, aby se zaměnily stopy:

> - 50,125 sats, které jdou skutečnému příjemci mé platby.
> - 52,306 sats, které představují moji změnu a tedy se vracejí na adresu v mé peněžence.
> - 50,125 sats, které se vracejí mému spolupracovníkovi.
> - 53,973 sats, které se vracejí mému spolupracovníkovi.
>   Na konci operace bude mít spolupracovník obnovený svůj počáteční zůstatek (minus těžební poplatky) a uživatel zaplatil obchodníkovi. Toto přidává transakci značné množství entropie a přerušuje nezpochybnitelné vazby mezi odesílatelem a příjemcem platby.

Síla transakce StonewallX2 spočívá v tom, že úplně odráží jedno z empirických pravidel používaných analytiky řetězců: společné vlastnictví vstupů v transakci s více vstupy. Jinými slovy, ve většině případů, pokud pozorujeme Bitcoinovou transakci s několika vstupy, můžeme předpokládat, že všechny tyto vstupy patří téže osobě. Satoshi Nakamoto již tento problém pro soukromí uživatele ve svém Bílém papíře identifikoval:

> "Jako další ochranná bariéra by pro každou transakci mohl být použit nový pár klíčů, aby nebyly spojeny se společným majitelem. Avšak spojení je nevyhnutelné u transakcí s více vstupy, které nutně odhalují, že jejich vstupy patřily stejnému majiteli."

To je jedno z mnoha empirických pravidel používaných v analýze na řetězci pro konstrukci klastrů adres. Chcete-li se dozvědět více o těchto heuristikách, doporučuji číst tuto sérii čtyř článků od Samourai, která téma úžasně představuje.
Síla transakce StonewallX2 spočívá v tom, že vnější pozorovatel si bude myslet, že různé vstupy transakce patří jednomu majiteli. Ve skutečnosti jsou to dva různí uživatelé, kteří spolupracují. Analýza platby je tedy vedena k návnadě a soukromí uživatele je zachováno.
Zvenčí nelze transakci StonewallX2 odlišit od transakce Stonewall. Jediným skutečným rozdílem mezi nimi je, že Stonewall není kolaborativní. Používá pouze UTXO jednoho uživatele. Nicméně ve svých strukturách na účetní knize jsou Stonewall a StonewallX2 naprosto identické. To umožňuje ještě více možných interpretací této struktury transakce, protože vnější pozorovatel nebude schopen rozpoznat, zda vstupy pocházejí od stejné osoby nebo od dvou spolupracovníků.

Navíc výhoda StonewallX2 oproti typu PayJoin Stowaway spočívá v tom, že ji lze použít v jakékoli situaci. Skutečný příjemce platby nepřispívá žádnými vstupy do transakce. Tím pádem lze StonewallX2 použít k platbě u jakéhokoli obchodníka přijímajícího Bitcoin, i když obchodník nepoužívá Samourai nebo Sparrow.
Na druhou stranu hlavní nevýhodou této struktury transakce je, že vyžaduje spolupracovníka, který je ochoten použít své bitcoiny k účasti na vaší platbě. Pokud máte přátele s bitcoiny, kteří jsou ochotni vám pomoci v jakékoli situaci, není to problém. Pokud však neznáte žádné další uživatele peněženky Samourai, nebo pokud není k dispozici nikdo, kdo by spolupracoval, pak jste uvízli.

Tento problém nedávno vyřešil tým Samourai přidáním nové funkce do jejich aplikace: JoinBot.

# Co je JoinBot?

Princip JoinBotu je jednoduchý. Pokud nemůžete najít nikoho, kdo by s vámi spolupracoval na transakci StonewallX2, můžete spolupracovat s JoinBotem. V praxi budete ve skutečnosti provádět kolaborativní transakci přímo s peněženkou Samourai.

Tato služba je velmi pohodlná, zejména pro začínající uživatele, protože je k dispozici 24/7. Pokud potřebujete provést naléhavou platbu a chcete provést StonewallX2, již nemusíte kontaktovat přítele nebo hledat online spolupracovníka. JoinBot vám pomůže.

Další výhodou JoinBotu je, že UTXO, které poskytuje jako vstup, pocházejí výhradně z postmix Whirlpool, což zlepšuje soukromí vaší platby. Navíc, protože JoinBot je vždy online, měli byste spolupracovat s UTXO, které mají velké potenciální Anonsety.

Samozřejmě, JoinBot má některé kompromisy, které je třeba poznamenat:

> Stejně jako u klasického StonewallX2, váš spolupracovník nutně ví o použitých UTXO a jejich cíli. V případě JoinBotu Samourai zná podrobnosti této transakce. To nutně není špatná věc, ale mělo by se na to pamatovat.
> Aby se zabránilo spamu, účtuje Samourai poplatek za službu ve výši 3,5 % z částky skutečné transakce, s maximálním limitem 0,01 BTC. Například, pokud pošlu skutečnou platbu 100 kilosatů s JoinBotem, částka poplatku za službu bude 3 500 satů.
> Pro použití JoinBotu musíte mít ve své peněžence alespoň dva nesouvisející a dostupné UTXO.
> U klasického StonewallX2 jsou těžební poplatky rozděleny rovným dílem mezi oba spolupracovníky. S JoinBotem budete samozřejmě muset zaplatit celé těžební poplatky.
Aby transakce JoinBot byla přesně stejná jako klasická transakce StonewallX2 nebo Stonewall, platba servisních poplatků se provádí v zcela samostatné transakci. Vrácení poloviny těžebních poplatků, které původně zaplatil Samourai, bude provedeno během této druhé transakce. Aby bylo dosaženo optimálního soukromí až do konce, vyrovnání poplatků se provádí pomocí strukturované transakce Stowaway (PayJoin).

## Jak používat JoinBot?

Pro provedení transakce JoinBot musíte mít peněženku Samourai. Můžete si ji stáhnout zde nebo z Google Playstore.

Na rozdíl od většiny nástrojů vyvinutých společností Samourai, Sparrow Wallet dosud neoznámil implementaci JoinBot. Tento nástroj je tedy dostupný pouze na Samourai.

Objevte krok za krokem, jak provést transakci StonewallX2 s JoinBot v tomto videu:

![Jak používat Joinbot](https://youtu.be/80MoMz2Ne5g)

Zde je diagram transakce, kterou jsme právě provedli ve videu:

![Diagram mé transakce StonewallX2 s JoinBot.](assets/3.webp)

Vidíme 5 vstupů:

> - 3 vstupy po 100 kilosatech pocházející od Samourai (JoinBot).
> - 2 vstupy z mé osobní peněženky, 3,524 sats a 1.8 megasat.

Čtyři výstupy transakce jsou následující:

> - 1 ve výši 212,452 sats skutečnému příjemci mé platby.
> - Další ve stejné výši, který se vrací na adresu Samourai.
> - 1 změna, která se také vrací Samourai ve výši 87,302 sats. To představuje rozdíl mezi celkovým počtem jejich vstupů (300,000 sats) a výstupem pro zamaskování (212,452 sats) mínus těžební poplatky.
> - 1 změna, která se vrací na další adresu v mé peněžence. Představuje rozdíl mezi celkovým počtem mých vstupů a skutečnou platbou, mínus těžební poplatky.

Připomínáme, že těžební poplatky nepředstavují výstupy transakce. Jednoduše představují rozdíl mezi celkovými vstupy a celkovými výstupy.

## Závěr

JoinBot je další nástroj, který přidává více možností a svobody pro uživatele Samourai. Umožňuje spolupracovat na transakci StonewallX2 přímo se Samourai jako spolupracovníkem. Tento typ transakce pomáhá zlepšit soukromí uživatele.

Pokud můžete provést klasickou transakci StonewallX2 s přítelem, stále doporučuji použít tento nástroj. Pokud však jste v situaci, kdy nemůžete najít žádné spolupracovníky pro provedení platby, víte, že JoinBot bude k dispozici 24/7, aby s vámi spolupracoval.

**Externí zdroje:**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin