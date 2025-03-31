---
name: Mnemonická fráze - Hod kostkami
description: Jak vygenerovat vlastní obnovovací frázi pomocí hodu kostkami?
---

![cover](assets/cover.webp)

V tomto tutoriálu se naučíte, jak ručně sestavit obnovovací frázi pro Bitcoin peněženku pomocí hodu kostkami.

**VAROVÁNÍ:** Generování mnemonické fráze bezpečným způsobem vyžaduje, aby při jejím vytváření nezůstala žádná digitální stopa, což je téměř nemožné. V opačném případě by peněženka představovala příliš velkou útočnou plochu, což by výrazně zvýšilo riziko krádeže vašich bitcoinů. **Proto se důrazně doporučuje nepřevádět prostředky do peněženky, která závisí na obnovovací frázi, kterou jste vygenerovali sami.** I když budete tento tutoriál dodržovat do písmene, existuje riziko, že obnovovací fráze může být ohrožena. **Tento tutoriál by tedy neměl být použit pro vytvoření skutečné peněženky.** Použití hardwarové peněženky pro tento úkol je mnohem méně riskantní, protože generuje frázi offline a skuteční kryptografové zvážili použití kvalitativních zdrojů entropie.

Tento tutoriál lze sledovat pouze pro experimentální účely pro vytvoření fiktivní peněženky, bez záměru používat ji s skutečnými bitcoiny. Zkušenost však nabízí dva přínosy:

- Zaprvé, umožňuje vám lépe pochopit mechanismy na základě vaší Bitcoin peněženky;
- Zadruhé, umožňuje vám vědět, jak na to. Neříkám, že to jednoho dne bude užitečné, ale může!

## Co je mnemonická fráze?

Obnovovací fráze, někdy také nazývaná "mnemonika", "seed fráze" nebo "tajná fráze", je sekvence obvykle složená z 12 nebo 24 slov, která je generována pseudo-náhodným způsobem ze zdroje entropie. Pseudo-náhodná sekvence je vždy doplněna kontrolním součtem.

Mnemonická fráze spolu s volitelnou heslovou frází slouží k deterministickému odvození všech klíčů spojených s HD (Hierarchická Deterministická) peněženkou. To znamená, že z této fráze je možné deterministicky generovat a znovu vytvořit všechny soukromé a veřejné klíče Bitcoin peněženky a tím pádem přistupovat k prostředkům s ní spojeným.
![mnemonic](assets/notext/1.webp)
Účelem této věty je poskytnout snadno použitelný prostředek pro zálohování a obnovu bitcoinů. Je nezbytné uchovávat mnemonickou frázi na bezpečném a zabezpečeném místě, protože kdokoli, kdo tuto frázi vlastní, by měl přístup k prostředkům odpovídající peněženky. Pokud je použita v kontextu tradiční peněženky a bez volitelné heslové fráze, často představuje SPOF (Single Point Of Failure).
Obvykle vám tato fráze je přímo dána při vytváření vaší peněženky, softwarem nebo hardwarovou peněženkou, kterou používáte. Je však také možné tuto frázi vygenerovat sami a poté ji zadat na vybraném nosiči k odvození klíčů peněženky. To se naučíme v tomto tutoriálu.

## Příprava potřebných materiálů

Pro ruční vytvoření vaší obnovovací fráze budete potřebovat:

- List papíru;
- Pero nebo tužku, ideálně různých barev pro usnadnění organizace;
- Několik kostek, aby se minimalizovala rizika zkreslení spojená s nevyváženou kostkou;
- [Seznam 2048 BIP39 slov](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) vytištěný.

Následně se stane nutné použití počítače s terminálem pro výpočet kontrolního součtu. Právě z tohoto důvodu doporučuji proti ruční generaci mnemonické fráze. Podle mého názoru zásah počítače, i při dodržení opatření uvedených v tomto tutoriálu, výrazně zvyšuje zranitelnost peněženky.
Pro experimentální přístup týkající se "fiktivní peněženky" je možné použít váš běžný počítač a jeho terminál. Nicméně pro rigoróznější přístup zaměřený na omezení rizik kompromitace vaší fráze by bylo ideální použít PC odpojené od internetu (nejlépe bez wifi komponenty nebo kabelového RJ45 připojení), vybavené minimem periferií (všechny by měly být připojeny kabelem, aby se vyhnulo Bluetooth) a především běžící na amnestické distribuci Linuxu, jako je [Tails](https://tails.boum.org/index.fr.html), spuštěné z odnímatelného média.
![mnemonic](assets/notext/2.webp)

V reálném kontextu by bylo klíčové zajistit důvěrnost vašeho pracovního prostoru výběrem místa mimo dosah zvědavých očí, bez pohybu lidí a bez kamer (webkamery, telefony...).
Doporučuje se použít velké množství kostek, aby se zmírnil dopad potenciálně nevyvážené kostky na entropii. Před jejich použitím se doporučuje kostky zkontrolovat: to lze provést testováním v misce s nasycenou solnou vodou, což umožní kostkám plavat. Poté proveďte asi dvacet hodů každou kostkou v solné vodě, pozorujte výsledky. Pokud se jedna nebo dvě strany objevují nepřiměřeně ve srovnání s ostatními, prodlužte test více hody. Rovnoměrně rozložené výsledky naznačují, že kostka je spolehlivá. Nicméně, pokud jedna nebo dvě strany pravidelně dominují, tyto kostky by měly být odloženy, protože by mohly ohrozit entropii vaší mnemonické fráze a tím pádem bezpečnost vaší peněženky.
V reálných podmínkách byste po provedení těchto kontrol byli připraveni generovat potřebnou entropii. Pro experimentální fiktivní peněženku vytvořenou jako součást tohoto tutoriálu byste tyto přípravy mohli samozřejmě vynechat.

## Několik připomenutí ohledně obnovovací fráze

Začneme přehledem základů vytváření mnemonické fráze podle BIP39. Jak bylo dříve vysvětleno, fráze je odvozena z pseudo-náhodných informací určité velikosti, ke kterým je přidán kontrolní součet, aby se zajistila jejich integrita.

Velikost této počáteční informace, často označované jako "entropie", je určena počtem slov, které chcete získat v obnovovací frázi. Nejběžnější formáty jsou fráze o 12 a 24 slovech, odvozené respektive z entropie 128 bitů a 256 bitů. Zde je tabulka ukazující různé velikosti entropie podle BIP39:

| Fráze (slova) | Entropie (bity) | Kontrolní součet (bity) | Entropie + Kontrolní součet (bity) |
| ------------- | --------------- | ----------------------- | ---------------------------------- |
| 12            | 128             | 4                       | 132                                |
| 15            | 160             | 5                       | 165                                |
| 18            | 192             | 6                       | 198                                |
| 21            | 224             | 7                       | 231                                |
| 24            | 256             | 8                       | 264                                |

Entropie je tedy náhodné číslo mezi 128 a 256 bity. V tomto tutoriálu si vezmeme příklad fráze o 12 slovech, ve které je entropie 128 bitů, což znamená, že vygenerujeme náhodnou sekvenci 128 `0` nebo `1`. To představuje číslo složené z 128 číslic v základu 2 (binárně).
Na základě této entropie bude vygenerován kontrolní součet. Kontrolní součet je hodnota vypočítaná ze sady dat, používaná k ověření integrity a platnosti těchto dat během jejich přenosu nebo ukládání. Algoritmy kontrolního součtu jsou navrženy tak, aby detekovaly náhodné chyby nebo změny v datech.
V případě naší mnemonické fráze má kontrolní součet za úkol odhalit jakékoli chyby při zadávání fráze do softwaru peněženky. Neplatný kontrolní součet signalizuje přítomnost chyby ve frázi. Naopak platný kontrolní součet naznačuje, že je fráze nejpravděpodobněji správná.
Pro získání tohoto kontrolního součtu je entropie převedena prostřednictvím hashovací funkce SHA256. Tato operace produkuje jako výstup 256bitovou sekvenci, z níž budou ponechány pouze první `N` bitů, přičemž `N` závisí na požadované délce obnovovací fráze (viz tabulka výše). Takže pro 12slovní frázi budou ponechány první 4 bity hashe.
![mnemonic](assets/en/3.webp)
Tyto první 4 bity, tvořící kontrolní součet, budou poté přidány k původní entropii. V této fázi je obnovovací fráze prakticky vytvořena, ale je stále ve formě binární sekvence. Abychom tuto binární sekvenci převedli na slova v souladu se standardem BIP39, nejprve rozdělíme sekvenci na 11bitové segmenty.
![mnemonic](assets/notext/4.webp)
Každý z těchto balíčků reprezentuje číslo v binární formě, které bude poté převedeno na desítkové číslo (základ 10). K každému číslu přičteme `1`, protože v informatice se počítá od `0`, ale seznam BIP39 je číslován od `1`.

![mnemonic](assets/notext/5.webp)

Nakonec nám číslo v desítkové soustavě řekne pozici odpovídajícího slova v [seznamu 2048 slov BIP39](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf). Zbývá už jen vybrat tato slova, aby se složila obnovovací fráze pro naši peněženku.

![mnemonic](assets/notext/6.webp)

Nyní přejděme k praxi! Vygenerujeme 12slovní obnovovací frázi. Tato operace zůstává stejná i v případě 24slovní fráze, s výjimkou toho, že by vyžadovala 256 bitů entropie a 8bitový kontrolní součet, jak je uvedeno v ekvivalenční tabulce na začátku této sekce.

## Krok 1: Generování entropie

Připravte si list papíru, pero a kostky. Začneme tím, že náhodně vygenerujeme 128 bitů, tj. sekvenci 128 `0` a `1` za sebou. K tomu použijeme kostky.
![mnemonic](assets/notext/7.webp)

Kostky mají 6 stran, všechny s identickou pravděpodobností, že padnou. Naším cílem je však produkovat binární výsledek, tedy dvě možné výsledky. Proto přiřadíme hodnotu `0` každému hodu, který padne na sudé číslo, a `1` pro každé liché číslo. V důsledku toho provedeme 128 hodů, abychom vytvořili naši 128bitovou entropii. Pokud kostka ukáže `2`, `4`, nebo `6`, zapíšeme `0`; pro `1`, `3`, nebo `5` to bude `1`. Každý výsledek bude zaznamenán sekvenčně, zleva doprava a shora dolů.

Abychom usnadnili následující kroky, seskupíme bity do balíčků po čtyřech a třech, jak je znázorněno na obrázku níže. Každý řádek musí mít 11 bitů: 2 balíčky po 4 bitech a jeden balíček po 3 bitech.

![mnemonic](assets/notext/8.webp)
Jak vidíte v mém příkladu, dvanácté slovo je v současnosti tvořeno pouze 7 bity. Ty budou doplněny o 4 bity kontrolního součtu v dalším kroku, aby vytvořily 11 bitů.
![mnemonic](assets/notext/9.webp)

## Krok 2: Výpočet kontrolního součtu

Tento krok je nejkritičtější při ruční generaci mnemonické fráze, protože vyžaduje použití počítače. Jak bylo zmíněno dříve, kontrolní součet odpovídá začátku hash SHA256 generovaného z entropie. Ačkoliv je teoreticky možné vypočítat SHA256 ručně pro vstup 128 nebo 256 bitů, tento úkol by mohl trvat celý týden. Navíc jakákoli chyba v ručních výpočtech by byla identifikována až na konci procesu, což by vás nutilo začít znovu od začátku. Proto je nepředstavitelné provést tento krok pouze s listem papíru a perem. Počítač je téměř nezbytný. Pokud stále chcete vědět, jak provést SHA256 ručně, vysvětlujeme, jak na to v kurzu [CRYPTO301](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f).

Z tohoto důvodu důrazně doporučuji nevytvářet ručně frázi pro skutečnou peněženku. Podle mého názoru použití počítače v této fázi, i se všemi nezbytnými opatřeními, neúměrně zvyšuje útočnou plochu peněženky.
Pro výpočet kontrolního součtu při zanechání co nejmenších stop použijeme amnestickou distribuci Linuxu na odnímatelném disku pojmenovanou **Tails**. Tento operační systém se spouští z USB klíčenky a funguje zcela v RAM počítače, aniž by interagoval s pevným diskem. Teoreticky tedy po vypnutí počítače nezanechává žádné stopy. Vezměte prosím na vědomí, že Tails je kompatibilní pouze s procesory typu x86_64, nikoli s procesory typu ARM.
Začněte tím, že ze svého obvyklého počítače [stáhnete obraz Tails z jeho oficiálního webu](https://tails.net/install/index.fr.html). Ověřte pravost vašeho stažení pomocí podpisu vývojáře nebo nástroje pro ověření nabízeného na webu.
![mnemonic](assets/notext/10.webp)
Nejprve proveďte formátování vašeho USB klíčenky, poté nainstalujte Tails pomocí nástroje jako je [Balena Etcher](https://etcher.balena.io/).
![mnemonic](assets/notext/11.webp)
Po potvrzení úspěšného zápisu vypněte počítač. Poté postupně odpojte napájecí zdroj a vyjměte pevný disk z desky vašeho PC. V případě, že je přítomna WiFi karta, měla by být odpojena. Podobně odstraňte jakýkoliv kabel RJ45 Ethernet. Pro minimalizaci rizika úniku dat se doporučuje odpojit vaši internetovou box a vypnout mobilní telefon. Navíc se doporučuje odpojit od počítače jakékoli nadbytečné periferie, jako je mikrofon, webkamera, reproduktory nebo headset, a zkontrolovat, že ostatní periferie jsou připojeny pouze kabelem. Všechny tyto kroky přípravy PC nejsou nezbytné, ale jednoduše pomáhají co nejvíce snížit útočnou plochu v reálném kontextu.

Zkontrolujte, zda je váš BIOS nakonfigurován tak, aby umožňoval bootování z externího zařízení. Pokud ne, změňte toto nastavení, poté restartujte stroj. Jakmile jste zabezpečili počítačové prostředí, restartujte počítač z USB klíčenky s Tails OS.

Na uvítací obrazovce Tails vyberte jazyk dle vašeho výběru, poté spusťte systém kliknutím na `Start Tails`.

![mnemonic](assets/notext/12.webp)

Na ploše klikněte na záložku `Applications`.

![mnemonic](assets/notext/13.webp)

Přejděte do menu `Utilities`.
A nakonec klikněte na aplikaci `Terminal`.

![mnemonic](assets/notext/15.webp)

Dostanete se na nový prázdný příkazový terminál.

![mnemonic](assets/notext/16.webp)
Napište příkaz `echo`, následovaný vaším dříve vygenerovaným entropií, přičemž se ujistěte, že mezi `echo` a vaší sekvencí binárních číslic vložíte mezeru.
![mnemonic](assets/notext/17.webp)

Přidejte další mezeru, poté zadejte následující příkaz, použijte _pipe_ (`|`):

```plaintext
| shasum -a 256 -0
```

![mnemonic](assets/notext/18.webp)

V příkladu s mou entropií je celý příkaz následující:

```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```

V tomto příkazu:

- `echo` se používá k odeslání bitové sekvence;
- `|`, _pipe_, se používá k přesměrování výstupu příkazu `echo` na vstup dalšího příkazu;
- `shasum` spouští hashovací funkci patřící do rodiny SHA (_Secure Hash Algorithm_);
- `-a` specifikuje výběr konkrétního hashovacího algoritmu;
- `256` udává, že se používá algoritmus SHA256;
- `-0` umožňuje interpretovat vstup jako binární číslo.

Po pečlivém ověření, že vaše binární sekvence neobsahuje žádné chyby při psaní, stiskněte klávesu `Enter` k provedení příkazu. Terminál poté zobrazí SHA256 hash vaší entropie.

![mnemonic](assets/notext/19.webp)

Zatím je hash vyjádřen ve formátu hexadecimální (základ 16). Například můj je:

```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```

Pro dokončení naší mnemonické fráze potřebujeme pouze první 4 bity hash, které tvoří kontrolní součet. Ve formátu hexadecimálním každý znak reprezentuje 4 bity. Takže si ponecháme pouze první znak hash. Pro frázi o 24 slovech by bylo nutné vzít v úvahu první dva znaky. V mém příkladu to odpovídá písmenu: `a`. Pečlivě si tento znak někde zapište, poté vypněte počítač.

Dalším krokem je převod tohoto hexadecimálního znaku (základ 16) na binární hodnotu (základ 2), jelikož naše fráze je konstruována v tomto formátu. K tomu můžete použít následující převodní tabulku:

| Desítkový (základ 10) | Hexadecimální (základ 16) | Binární (základ 2) |
| --------------------- | ------------------------- | ------------------ |
| 0                     | 0                         | 0000               |
| 1                     | 1                         | 0001               |
| 2                     | 2                         | 0010               |
| 3                     | 3                         | 0011               |
| 4                     | 4                         | 0100               |
| 5                     | 5                         | 0101               |
| 6                     | 6                         | 0110               |
| 7                     | 7                         | 0111               |
| 8                     | 8                         | 1000               |
| 9                     | 9                         | 1001               |
| 10                    | a                         | 1010               |
| 11                    | b                         | 1011               |
| 12                    | c                         | 1100               |
| 13                    | d                         | 1101               |
| 14                    | e                         | 1110               |
| 15                    | f                         | 1111               |

V mém příkladu písmeno `a` odpovídá binárnímu číslu `1010`. Tyto 4 bity tvoří kontrolní součet naší obnovovací fráze. Nyní je můžete přidat k již na papíře poznamenané entropii, umístěte je na konec posledního slova.

![mnemonic](assets/notext/20.webp)

Vaše mnemonická fráze je nyní kompletní, ale je ve formátu binárních čísel. Dalším krokem bude její převedení do desítkové soustavy, abyste poté mohli každé číslo spojit s odpovídajícím slovem ze seznamu BIP39.

## Krok 3: Převod slov do desítkové soustavy

Pro převod každého řádku binárních čísel na desítkové číslo použijeme metodu, která usnadňuje ruční výpočet. Aktuálně máte na papíře dvanáct řádků, každý složený z 11 binárních číslic `0` nebo `1`. Pro převod do desítkové soustavy přiřaďte každé první číslici hodnotu `1024`, pokud je `1`, jinak `0`. Pro druhou číslici bude přiřazena hodnota `512`, pokud je `1`, jinak `0`, a tak dále až po jedenáctou číslici. Odpovídající hodnoty jsou následující:

- 1. bit: `1024`;
- 2. bit: `512`;
- 3. bit: `256`;
- 4. bit: `128`;
- 5. bit: `64`;
- 6. bit: `32`;
- 7. bit: `16`;
- 8. bit: `8`;
- 9. bit: `4`;
- 10. bit: `2`;
- 11. bit: `1`.

Pro každý řádek sečteme hodnoty odpovídající číslicím `1`, abychom získali desítkové číslo ekvivalentní binárnímu číslu. Vezměme si příklad binárního řádku rovného:

```plaintext
1010 1101 101
```

Převod by proběhl takto:
![mnemonic](assets/notext/21.webp)
Výsledek by poté byl:

```plaintext
1389
```

Pro každý bit rovný `1` zaznamenejte níže přidružené číslo. Pro každý bit rovný `0` nezaznamenávejte nic.

![mnemonic](assets/notext/22.webp)
Poté jednoduše sečtěte všechna čísla potvrzená `1`, abyste získali desítkové číslo reprezentující každý binární řádek. Například, tady je to, jak to vypadá pro můj list:
![mnemonic](assets/notext/23.webp)

## Krok 4: Hledání slov mnemonické fráze

S získanými desítkovými čísly nyní můžeme lokalizovat odpovídající slova ze seznamu a složit mnemonickou frázi. Číslování 2048 slov v seznamu BIP39 však sahá od `1` do `2048`. Naše vypočítaná binární výsledky však sahají od `0` do `2047`. Proto je třeba opravit posun o jednu jednotku. Pro opravu tohoto posunu jednoduše přičtěte `1` k dvanácti dříve vypočítaným desítkovým číslům.

![mnemonic](assets/notext/24.webp)
Po tomto nastavení máte hodnost každého slova v seznamu. Zbývá už jen každé slovo identifikovat podle jeho čísla. Samozřejmě, stejně jako u všech ostatních kroků, nesmíte použít počítač k provedení této konverze. Proto se ujistěte, že máte seznam vytisknutý předem.
[**-> Vytiskněte seznam BIP39 ve formátu A4.**](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)

Například, pokud číslo odvozené z prvního řádku je 1721, odpovídající slovo bude 1721. na seznamu:

```plaintext
1721. strike
```

![mnemonic](assets/notext/25.webp)
Tímto způsobem postupujeme postupně se 12 slovy k sestavení naší mnemonické fráze.

![mnemonic](assets/notext/26.webp)

## Krok 5: Vytvoření Bitcoin peněženky

V tomto bodě zbývá už jen importovat naši mnemonickou frázi do softwaru Bitcoin peněženky. Podle našich preferencí to lze provést na desktopovém softwaru pro získání hot peněženky, nebo na hardwarové peněžence pro cold peněženku.

![mnemonic](assets/notext/27.webp)

Ověření platnosti vašeho kontrolního součtu je možné pouze během importace. Pokud software zobrazí zprávu jako `Invalid Checksum`, znamená to, že do vašeho procesu tvorby se vloudila chyba. Obvykle tato chyba pramení buď z chybného výpočtu během manuálních konverzí a sčítání, nebo z překlepu při zadávání vaší entropie do terminálu na Tails. Bude nutné proces začít od začátku, aby se tyto chyby opravily.

![mnemonic](assets/notext/28.webp)
Po vytvoření vaší peněženky nezapomeňte zálohovat vaši obnovovací frázi na fyzickém médiu, jako je papír nebo kov, a zničit tabulku použitou během její generace, aby nedošlo k úniku informací.

## Specifický případ možnosti Dice Roll na Coldcards

Hardwarové peněženky z rodiny Coldcard nabízejí [funkci pojmenovanou _Dice Roll_](https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7), která umožňuje generovat obnovovací frázi vaší peněženky pomocí kostek. Tato metoda je vynikající, protože vám dává přímou kontrolu nad tvorbou entropie, aniž byste potřebovali použít externí zařízení pro výpočet kontrolního součtu, jak je uvedeno v našem návodu.

Nicméně, nedávno byly hlášeny případy krádeže bitcoinů kvůli nesprávnému použití této funkce. Skutečně, příliš omezený počet hodů kostkami může vést k nedostatečné entropii, což teoreticky umožňuje hrubou sílu mnemonické fráze a krádež přidružených bitcoinů. Aby se tomuto riziku předešlo, doporučuje se provést alespoň 99 hodů kostkami na Coldcard, což zajišťuje dostatečnou entropii.

Metoda interpretace výsledků navržená Coldcardem se liší od té, kterou jsme prezentovali v tomto návodu. Zatímco my doporučujeme 128 hodů pro dosažení 128 bitů bezpečnosti v návodu, Coldcard navrhuje 99 hodů pro dosažení 256 bitů bezpečnosti. Skutečně, v našem přístupu jsou možné pouze dva výsledky pro každý hod kostkou: sudý (`0`) nebo lichý (`1`). Proto entropie generovaná každým hodem je rovna `log2(2)`. V případě Coldcardu, který bere v úvahu šest možných stran kostky (od `1` do `6`), je entropie na hod rovna `log2(6)`. To je důvod, proč v našem návodu potřebujeme provést více hodů, abychom dosáhli stejné úrovně entropie.

```plaintext
Entropie = počet hodů * log2(počet možných výsledků na kostce)
Coldcard:

Entropie = 99 * log2(6)
Entropie = 255.91

Náš tutoriál:

Entropie = 128 * log2(2)
Entropie = 128
```
