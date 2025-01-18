---
name: COLDCARD Q - Pokročilé
description: Použití pokročilých možností karty COLDCARD Q
---
![cover](assets/cover.webp)

V předchozím tutoriálu jsme se zabývali počáteční konfigurací karty COLDCARD Q a jejími základními funkcemi pro začátečníky. Pokud jste právě obdrželi kartu COLDCARD Q a ještě jste ji nenastavili, doporučuji vám začít tímto návodem, než budete pokračovat zde:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
Tento nový návod je věnován pokročilým možnostem karty COLDCARD Q, které jsou určeny pro pokročilé a paranoidní uživatele. Karty COLDCARD se totiž od ostatních hardwarových peněženek liší mnoha pokročilými bezpečnostními funkcemi. Všechny tyto možnosti samozřejmě nemusíte používat. Stačí si vybrat ty, které vyhovují vaší bezpečnostní strategii.

**Upozornění**: nesprávné použití některých z těchto pokročilých možností může vést ke ztrátě bitcoinů nebo zničení hardwarové peněženky. Proto důrazně doporučuji, abyste si pečlivě přečetli rady a vysvětlení k jednotlivým možnostem.

Než začnete, ujistěte se, že máte přístup k fyzické záloze své 12- nebo 24slovné mnemotechnické fráze, a zkontrolujte její platnost prostřednictvím následující nabídky: `Pokročilé/Nástroje > Nebezpečná zóna > Funkce zadávání > Zobrazit zadaná slova`.

![CCQ](assets/fr/01.webp)

## Heslo BIP39

Pokud nevíte, co je to přístupová fráze BIP39, nebo pokud vám není zcela jasné, jak funguje, důrazně doporučuji, abyste se předem podívali na tento výukový program, který obsahuje teoretické základy potřebné k pochopení rizik spojených s používáním přístupové fráze :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Mějte na paměti, že po nastavení přístupové fráze v peněžence vám samotná mnemotechnická pomůcka nebude stačit k získání přístupu k bitcoinům. Budete potřebovat jak mnemotechnickou, tak přístupovou frázi. Navíc budete muset zadat přístupovou frázi pokaždé, když odemknete kartu COLDCARD Q. Tím se zvyšuje bezpečnost, protože bez přístupové fráze je fyzický přístup ke kartě COLDCARD a znalost kódu PIN nedostatečná.

Na kartách COLDCARD máte dvě možnosti správy přístupové fráze:

1. **Klasické zadávání:** Při každém použití hardwarové peněženky zadáte přístupovou frázi ručně, stejně jako u jiných hardwarových peněženek. Karta COLDCARD Q tento úkol zjednodušuje díky své plnohodnotné klávesnici.

2. **Můžete si zvolit šifrování přístupové fráze a uložit ji na kartu microSD. V takovém případě budete muset kartu microSD vložit do zařízení COLDCARD Q při každém použití. Upozorňujeme, že tato karta microSD bude fungovat pouze na kartě COLDCARD Q a není záložní. Je proto velmi důležité, abyste si kopii své přístupové fráze uchovávali také na fyzickém médiu, například na papíře nebo kovu.

Chcete-li nastavit přístupovou frázi BIP39, otevřete nabídku "*Passphrase*".

![CCQ](assets/fr/02.webp)

Zadejte přístupovou frázi pomocí klávesnice. Nezapomeňte zvolit silnou přístupovou frázi (dlouhou a náhodnou) a vytvořte si fyzickou zálohu.

![CCQ](assets/fr/03.webp)

Po nastavení přístupové fráze vám karta COLDCARD Q zobrazí otisk hlavního klíče nové peněženky přiřazené k této frázi. Nezapomeňte si tento otisk uložit. Až budete v budoucnu při používání zařízení znovu zadávat svou přístupovou frázi, budete moci zkontrolovat, zda se zobrazený otisk prstu shoduje s tím, který jste uložili. Tato kontrola zajistí, že jste se při zadávání přístupové fráze nespletli.

![CCQ](assets/fr/04.webp)

Nyní můžete stisknutím tlačítka "*ENTER*" použít tuto přístupovou frázi k mnemotechnické frázi a aktivovat novou peněženku. Pokud dáváte přednost uložení této přístupové fráze na kartu microSD, vložte kartu do příslušného slotu a stiskněte "*1*".

![CCQ](assets/fr/05.webp)

Vaše přístupová fráze je nyní použita. Otisk klíče se zobrazí na domovské obrazovce a v horní části obrazovky.

![CCQ](assets/fr/06.webp)

Při každém odemknutí karty COLDCARD Q musíte vstoupit do nabídky "*Passphrase*" a zadat svou přístupovou frázi stejným způsobem jako výše, abyste ji použili na mnemotechnické heslo uložené v zařízení a získali přístup ke správné peněžence Bitcoin.

![CCQ](assets/fr/07.webp)

Pokud jste uložili přístupovou frázi na kartu microSD, vložte ji při každém použití do karty COLDCARD a otevřete nabídku "*Passphrase*". Karta COLDCARD načte přístupovou frázi přímo z karty microSD, takže ji nebudete muset zadávat ručně. Klikněte na "*Obnovit uložené*".

![CCQ](assets/fr/08.webp)

Zkontrolujte, zda je délka a první písmeno načtené přístupové fráze správné.

![CCQ](assets/fr/09.webp)

Zkontrolujte, zda se zobrazený otisk prstu shoduje s otiskem vaší peněženky, a klikněte na "*Obnovit*".

![CCQ](assets/fr/10.webp)

Mějte na paměti, že použití přístupové fráze znamená, že budete muset do softwaru pro správu peněženky (například Sparrow Wallet) importovat novou sadu klíčů odvozenou z kombinace mnemotechnické fráze a přístupové fráze. Chcete-li to provést, postupujte podle kroku "*Konfigurace nové peněženky ve Sparrow*" v tomto dalším návodu :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
## Možnosti odemknutí

Karty COLDCARD také využívají řadu možností pro odblokování zařízení. Pojďme se o těchto pokročilých možnostech dozvědět více.

### Záludné kódy PIN

Trick PIN je sekundární kód PIN odlišný od kódu definovaného při počáteční konfiguraci zařízení. Tento kód se používá ke spuštění specifických předem nakonfigurovaných akcí, jakmile je zadán při zapnutí karty COLDCARD. Můžete nakonfigurovat několik kódů Trick PIN, z nichž každý je spojen s jinou akcí. Tyto funkce umožňují přizpůsobit kartu COLDCARD vaší osobní bezpečnostní strategii. Jsou obzvláště užitečné v případech fyzického nátlaku, například při loupeži (v komunitě bitcoinů běžně označované jako "útok *5$ klíčem*").

Chcete-li aktivovat trikový kód PIN a přiřadit jej k akci, přejděte do nabídky `Nastavení > Nastavení přihlášení > Trikové kódy PIN`.

![CCQ](assets/fr/11.webp)

Vyberte možnost "*Přidat nový trik*".

![CCQ](assets/fr/12.webp)

Nastavte kód PIN, který má být spojen s akcí, a nezapomeňte jej uložit.

![CCQ](assets/fr/13.webp)

Poté zvolte akci, která se má automaticky provést při každém zadání tohoto kódu Trick PIN. Zde je seznam akcí dostupných pro kód PIN:


- "*Brick Self*: Tato akce zničí oba čipy COLDCARD Q, pokud je zadán Trick PIN, čímž se zařízení stane zcela nepoužitelným. Pak jej nebude možné znovu prodat, použít nebo dokonce vrátit společnosti Coinkite. Zařízení se stane nenávratně zastaralým. Tuto funkci lze využít v případě loupeže a přesvědčit útočníka, že se k vašim bitcoinům nikdy nedostane. **Upozornění**: Bez fyzické zálohy mnemotechnické fráze a případné přístupové fráze budou vaše bitcoiny nenávratně ztraceny.

![CCQ](assets/fr/14.webp)


- "*Utírejte semena*": Tato nabídka nabízí několik akcí pro vymazání osiva, tj. resetování karty COLDCARD bez jejího zničení. Na rozdíl od možnosti "*Brick Self*" bude možné znovu nakonfigurovat zařízení pomocí zálohy vaší mnemotechnické fráze. Bez této zálohy však budou vaše bitcoiny ztraceny. Zde jsou dostupné možnosti:
 - "*Vymazat a restartovat* : Odstraní osivo a restartuje kartu COLDCARD bez zobrazení jakýchkoli informací na obrazovce.
 - "*Tiché utírání*": Tiché vymazání osiva a odemknutí karty COLDCARD v náhodné falešné peněžence, jako by se nic nestalo.
 - "*Vymazat -> Peněženka*": Odstraní diskrétně osivo a odemkne kartu COLDCARD v předem nakonfigurované sekundární peněžence, která je určena jako návnada. Tato peněženka může obsahovat malou část vašich úspor v bitcoinech, aby útočníka uspokojila.
 - "*Řekni Wiped, Stop*": Na obrazovce se zobrazí zpráva `Seed is wiped, Stop`.

![CCQ](assets/fr/15.webp)


- "*Peněženka z donucení*": Při této akci odemkne kód Trick PIN peněženku odvozenou ze semínka pomocí BIP85. Tuto sekundární peněženku lze použít jako návnadu k uspokojení útočníka. Karta COLDCARD se chová, jako by to byla skutečná peněženka, ale bez hlavního kódu PIN (odlišného od kódu Trick PIN) se útočník do skutečné peněženky nikdy nedostane. Tato strategie je navržena tak, aby lidé uvěřili, že peněženka spojená s Trick PIN je jediná existující.

![CCQ](assets/fr/16.webp)


- "*Odpočítávání přihlášení*": Tato nabídka seskupuje akce s odpočtem před jejich provedením. **Upozornění**, některé z nich mohou zničit vaše zařízení nebo vést ke ztrátě bitcoinů. Zde jsou uvedeny dostupné dílčí akce:
 - "*Vymazání a odpočítávání* : Vymaže osivo z paměti karty COLDCARD a poté spustí hodinové odpočítávání. Bez uložení mnemotechnické nebo přístupové fráze budou vaše bitcoiny ztraceny. Tato možnost je navržena tak, aby útočníka oklamala, že se zařízení po skončení odpočítávání odemkne, zatímco ve skutečnosti bude obnoveno do továrního nastavení.
 - "*Odpočet a cihla*": Na konci tohoto času karta COLDCARD zničí své dva zabezpečené čipy, čímž se stane trvale nepoužitelnou. Bez zálohy budou vaše bitcoiny ztraceny. Tato akce je navržena tak, aby oklamala útočníka, který si myslí, že čeká na odemčení, zatímco ve skutečnosti dojde k sebedestrukci zařízení.
 - "*Jen odpočítávání* : Spustí jednoduché hodinové odpočítávání, po kterém se karta COLDCARD znovu spustí bez další akce. Sada se nevymaže a zařízení zůstane nedotčeno. Dávejte pozor, abyste tuto akci nezaměnili s možností "*Login Countdown*", o které pojednávají následující kapitoly a která přidává odpočet k hlavnímu PINu a zároveň umožňuje přístup ke skutečné peněžence.

![CCQ](assets/fr/17.webp)


- "*Pohled prázdný*": Tato akce způsobí, že se karta COLDCARD bude jevit jako prázdná, což vyvolá dojem, že osivo bylo smazáno. Ve skutečnosti se nic nestane a osivo zůstane nedotčené. Tím se simuluje nepoužitá nebo vynulovaná karta COLDCARD.

![CCQ](assets/fr/18.webp)


- "*Prostě restartujte* : Při použití kódu PIN Trick se karta COLDCARD jednoduše restartuje. Žádná další akce se neprovádí.

![CCQ](assets/fr/19.webp)


- "*Režim Delta*": Tato složitá akce, vyhrazená pro zkušené uživatele, je určena proti vysoce sofistikovaným nátlakovým útokům, ať už ze strany státu nebo příbuzného s privilegovanými informacemi. Při aktivaci režimu Delta poskytuje karta COLDCARD přístup ke skutečné peněžence, což útočníkovi umožňuje procházet a ověřovat, zda se jedná o správnou peněženku. Podpisy transakcí jsou však zablokovány, čímž je zabráněno jakémukoli převodu bitcoinů. Kromě toho je zakázán přístup k mnemotechnické frázi a jakýkoli pokus o její načtení vede k jejímu vymazání. Pro zvýšení důvěryhodnosti musí mít trikový PIN použitý s režimem Delta stejnou předponu jako skutečný PIN (aby se zobrazovala stejná slova proti phishingu), ale přípona musí být jiná.

![CCQ](assets/fr/20.webp)

Po výběru akce potvrďte svůj výběr.

![CCQ](assets/fr/21.webp)

Všechny nakonfigurované trikové kódy PIN pak můžete zobrazit ve vyhrazeném menu.

![CCQ](assets/fr/22.webp)

Výběrem existujícího kódu PIN triku můžete zkontrolovat přidruženou akci. Můžete ji také skrýt pomocí příkazu "*Skrýt trik*", čímž se v nabídce trikových PINů stane neviditelnou. Můžete jej odstranit kliknutím na "*Delete Trick*" (Odstranit trik*) nebo změnit kód PIN při zachování přidružené akce pomocí "*Change PIN*" (Změnit kód PIN*).

![CCQ](assets/fr/23.webp)

Možnost "*Přidat při chybě*", která je k dispozici v nabídce "*Trick PIN*", umožňuje nakonfigurovat konkrétní akci, která se automaticky spustí po určitém počtu chybných pokusů o zadání hlavního kódu PIN. Počet povolených pokusů lze nastavit během konfigurace.

### Scramble Keys

Volba Scramble Keys umožňuje zakódovat číslice zobrazené na tlačítkách klávesnice při zadávání kódu PIN. Tato funkce chrání důvěrnost kódu PIN i v případě sledování osobami nebo kamerami.

Chcete-li tuto možnost aktivovat, přejděte do nabídky `Nastavení > Nastavení přihlášení > Kódovací klávesy`.

![CCQ](assets/fr/24.webp)

Vyberte možnost "*Scramble Keys*".

![CCQ](assets/fr/25.webp)

Od nynějška se při odemykání karty COLDCARD Q budou tlačítkům na klávesnici při každém použití náhodně přiřazovat nová čísla.

![CCQ](assets/fr/26.webp)

### Odpočítávání přihlášení

Tato možnost umožňuje nastavit systematické odpočítávání při každém pokusu o odemknutí karty COLDCARD. Lze ji začlenit do bezpečnostní strategie odložením přístupu k zařízení v případě krádeže nebo zavedením odkladu před podpisem transakce, například pro ochranu v případě přepadení. Toto odpočítávání se však vztahuje na všechna vaše použití, včetně případů, kdy kartu COLDCARD používáte oprávněně, což vás rovněž zavazuje k trpělivosti. Dávejte pozor, abyste si tuto možnost nezaměnili s akcí "*Jen odpočítávání*", která se aktivuje pouze při použití konkrétního kódu PIN Trick.

Chcete-li tuto možnost nakonfigurovat, přejděte do nabídky `Nastavení > Nastavení přihlášení > Odpočítávání přihlášení`.

![CCQ](assets/fr/27.webp)

Vyberte čas odpočítávání. Pokud například vyberete možnost 1 hodina, budete muset při každém pokusu o odemknutí karty COLDCARD Q čekat 1 hodinu.

![CCQ](assets/fr/28.webp)

Při každém odemknutí budete vyzváni k zadání kódu PIN.

![CCQ](assets/fr/29.webp)

Poté počkejte na čas nastavený odpočítáváním.

![CCQ](assets/fr/30.webp)

Po skončení odpočítávání budete muset pro přístup k zařízení znovu zadat kód PIN.

![CCQ](assets/fr/31.webp)

### Přihlášení ke kalkulačce

Tato možnost umožňuje při odemykání maskovat kartu COLDCARD jako kalkulačku. Chcete-li tuto funkci aktivovat, vstupte do nabídky `Nastavení > Nastavení přihlášení > Přihlášení kalkulačky`.

![CCQ](assets/fr/32.webp)

Výběrem možnosti ji aktivujte.

![CCQ](assets/fr/33.webp)

Od této chvíle se při každém zapnutí zařízení zobrazí pracovní kalkulačka se základními příkazy.

![CCQ](assets/fr/34.webp)

Můžete například vypočítat hash SHA256 "*Síť plánu B*".

![CCQ](assets/fr/35.webp)

Chcete-li kartu COLDCARD odemknout z režimu kalkulačky, začněte zadáním předčíslí kódu PIN, za kterým následuje pomlčka. Pokud je například váš kód PIN `00-00` (tento kód je slabý a pouze příkladový, proto zvolte silný kód PIN), zadejte `00-`. Karta COLDCARD poté zobrazí vaše dvě slova proti phishingu.

![CCQ](assets/fr/36.webp)

Poté zadejte celý kód PIN oddělený mezerou nebo pomlčkou, například: `00 00`.

![CCQ](assets/fr/37.webp)

Karta COLDCARD poté ukončí režim kalkulačky a normálně se odemkne.

## Čisté zničení karty COLDCARD

Pokud se chystáte kartu COLDCARD Q zlikvidovat, například proto, že nyní používáte jinou hardwarovou peněženku, je důležité zařízení správně zničit. Tím zajistíte, že třetí strana nebude moci obnovit žádné informace týkající se vaší peněženky.

V závislosti na vašich potřebách existují tři úrovně likvidace informací. Než začnete, ujistěte se, že vaše peněženka byla importována do jiné hardwarové peněženky, že máte přístup ke všem svým prostředkům a především, že máte svou mnemotechnickou frázi a případnou přístupovou frázi, které jsou funkční. Bez zálohy peněženky bude mít zničení karty COLDCARD za následek ztrátu vašich bitcoinů.

První úroveň zničení spočívá ve vymazání pouze semen. Tato možnost vymaže vaši mnemotechnickou frázi z paměti karty COLDCARD, přičemž zařízení zůstane funkční. Je ideální, pokud chcete kartu COLDCARD Q později znovu použít. Chcete-li z paměti vymazat semínko, vstupte do nabídky `Rozšířené/Nástroje > Nebezpečná zóna > Funkce semínka > Zničit semínko`.

![CCQ](assets/fr/38.webp)

Druhá úroveň zničení spočívá v trvalém vyřazení dvou zabezpečených čipů karty COLDCARD prostřednictvím softwaru. Tímto úkonem se zařízení stane zcela nepoužitelným. Nebudete jej moci dále prodat, znovu použít ani vrátit společnosti Coinkite: bude trvale zničeno. Chcete-li pokračovat, postupujte podle kroků popsaných v předchozí části týkající se "*Brick Me*" PIN, a poté tento PIN záměrně zadejte při odemykání karty COLDCARD.

Třetí úroveň zahrnuje fyzické zničení zabezpečených součástí karty COLDCARD Q. Stejně jako předtím se tím zařízení stane nevratně nepoužitelným. K tomu použijte vrtačku a udělejte díru do dvou čipů na pravé horní straně zařízení (po otočení vzhůru nohama), v blízkosti nápisu "*SHOOT HERE*".

**Důležitá bezpečnostní opatření** :


- Abyste předešli riziku úrazu elektrickým proudem, vyjměte ze zařízení baterie a před manipulací jej odpojte od elektrické sítě.
- Po vypnutí přístroje počkejte několik minut, než začnete vrtat.
- Pro zajištění své bezpečnosti používejte izolované rukavice a ochranné brýle.

![CCQ](assets/fr/39.webp)

Po vyražení čipů se nepokoušejte kartu COLDCARD Q znovu připojit.

Blahopřejeme, nyní jste se seznámili s pokročilými možnostmi karty COLDCARD Q!

Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento návod sdílet na svých sociálních sítích. Moc vám děkuji!

Doporučuji také tento další tutoriál, ve kterém probíráme použití přímého konkurenta CCQ, Ledger Flex :

https://planb.network/fr/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a