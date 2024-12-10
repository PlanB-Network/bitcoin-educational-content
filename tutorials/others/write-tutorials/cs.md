---
name: Příspěvek - Tutoriály
description: Jak navrhnout nový tutoriál na PlanB Network?
---
![obálka](assets/cover.webp)

Mise PlanB spočívá v poskytování špičkových vzdělávacích zdrojů o Bitcoinu v co nejvíce jazycích. Veškerý obsah publikovaný na webu je open-source a hostovaný na GitHubu, což nabízí příležitost pro každého zapojit se do obohacování platformy. Příspěvky mohou mít různé formy: opravy a korektury stávajících textů, překlady do jiných jazyků, aktualizace informací nebo vytváření nových tutoriálů, které ještě nejsou na našem webu dostupné.

V tomto tutoriálu vám vysvětlím, jak upravit sekci "Tutoriály" na PlanB Network. Pokud si přejete přidat nový tutoriál nebo vylepšit stávající, tento článek je pro vás! Podrobně se podíváme na to, jak přispívat do PlanB Network prostřednictvím GitHubu, přičemž využijeme Obsidian, nástroj pro psaní.

## Předpoklady

Pro přispívání do PlanB Network máte 3 možnosti v závislosti na vaší úrovni zkušeností s GitHubem:
1. **Zkušení uživatelé**: Pokračujte svými obvyklými metodami a prostudujte tento tutoriál, abyste se seznámili se strukturou repozitáře PlanB, specifickými požadavky a pracovním postupem.
2. **Začátečníci připraveni se učit**: Doporučuji si nastavit vlastní pracovní prostředí. Sledujte tento tutoriál stejně jako naše další články uvedené níže, které vás provedou krok za krokem.
3. **Začátečníci pro menší příspěvky**: Pro úkoly, které vyžadují méně úprav, jako je korektura nebo opravy, použijte přímo webové rozhraní GitHubu bez nastavení kompletního lokálního prostředí.

**Software potřebný k následování mého tutoriálu:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Editor kódu ([VSC](https://code.visualstudio.com/) nebo [Sublime Text](https://www.sublimetext.com/))
![tutoriál](assets/1.webp)
**Předpoklady před zahájením tutoriálu:**
- Mít [účet na GitHubu](https://github.com/signup).
- Mít fork [zdrojového repozitáře PlanB Network](https://github.com/PlanB-Network/bitcoin-educational-content).
- Mít [profil profesora na PlanB Network](https://planb.network/professors) (pouze pokud navrhujete kompletní tutoriál).

**Pokud potřebujete pomoc s získáním těchto předpokladů, moje další tutoriály vás provedou:**
**[Porozumění Gitu a GitHubu](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Vytvoření účtu na GitHubu](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Nastavení pracovního prostředí](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
**[Vytvoření profilu profesora](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**
## Jaký typ obsahu psát na PlanB Network?
Hledáme především tutoriály o nástrojích souvisejících s Bitcoinem nebo jeho ekosystémem. Tyto obsahy mohou být organizovány do šesti hlavních kategorií:
- Peněženka;
- Uzel;
- Těžba;
- Obchodník;
- Směnárna;
- Soukromí.
![tutoriál](assets/2.webp)
Kromě těchto témat přímo souvisejících s Bitcoinem, PlanB také hledá příspěvky na témata, která zdůrazňují individuální suverenitu, jako jsou:
- Open source nástroje;
- Výpočetní technika;
- Kryptografie;
- Energie;
- Matematika;
- Ekonomie;
- DIY (Udělej si sám);
- LifeHacking...
Například, v současné době máme tutoriály na Tails, Nostr nebo GrapheneOS. Tyto nástroje nejsou přímo související s Bitcoinem, ale jsou to systémy, které nás mohou zajímat v procesu suverenity v digitálním světě. Tyto obsahy mohou být začleněny do podkategorie sekce "Ostatní".
Máte na výběr mezi navržením tutoriálu od nuly nebo použitím tutoriálu, který byl dříve publikován na vašem webu (za předpokladu, že vlastníte autorská práva), aby byl také sdílen na síti PlanB Network, s přidáním odkazu na původní článek.

Ať už se rozhodnete jakkoliv, mějte na paměti, že veškerý obsah publikovaný na síti PlanB Network je pod svobodnou licencí [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Tato licence umožňuje komukoli kopírovat a potenciálně upravovat váš obsah, za předpokladu, že je řádně uveden původní zdroj.

## Jak navrhnout tutoriál na síti PlanB Network?

Jakmile je vše připraveno a vaše lokální prostředí je správně nastaveno s vaším vlastním forknutím síti PlanB Network, můžete začít přidávat tutoriál.

### Vytvoření nové větve

- Otevřete svůj prohlížeč a přejděte na stránku vašeho forknutí repozitáře PlanB. To je fork, který jste založili na GitHubu. URL vašeho forku by měla vypadat takto: `https://github.com/[vaše-uživatelské-jméno]/bitcoin-educational-content`:
![tutorial](assets/3.webp)
- Ujistěte se, že jste na hlavní větvi `dev`, poté klikněte na tlačítko `Sync fork`. Pokud váš fork není aktuální, GitHub nabídne aktualizaci vaší větve. Proveďte tuto aktualizaci. Pokud je naopak vaše větev již aktuální, GitHub vás informuje:
![tutorial](assets/4.webp)
- Otevřete software GitHub Desktop a ujistěte se, že váš fork je správně vybrán v levém horním rohu okna:
![tutorial](assets/5.webp)
- Klikněte na tlačítko `Fetch origin`. Pokud je vaše lokální repozitář již aktuální, GitHub Desktop nenavrhuje žádnou další akci. V opačném případě se objeví možnost `Pull origin`. Klikněte na toto tlačítko, abyste aktualizovali svůj lokální repozitář: ![tutorial](assets/6.webp)
- Ujistěte se, že jste na hlavní větvi `dev`:
![tutorial](assets/7.webp)
- Klikněte na tuto větev, poté klikněte na tlačítko `New Branch`:
![tutorial](assets/8.webp)
- Ujistěte se, že nová větev je založena na zdrojovém repozitáři, tedy `PlanB-Network/bitcoin-educational-content`.
- Pojmenujte vaši větev tak, aby název jasně vypovídal o jejím účelu, použijte pomlčky k oddělení jednotlivých slov. Například, řekněme, že náš cíl je napsat tutoriál na používání softwaru Sparrow Wallet. V tomto případě by pracovní větev věnovaná psaní tohoto tutoriálu mohla být pojmenována: `tuto-sparrow-wallet-loic`. Jakmile je vhodný název zadán, klikněte na `Create branch` pro potvrzení vytvoření větve:
![tutorial](assets/9.webp)
- Nyní klikněte na tlačítko `Publish branch` pro uložení vaší nové pracovní větve na váš online fork na GitHubu:
![tutorial](assets/10.webp)
Nyní byste na GitHub Desktop měli být na vaší nové větvi. To znamená, že veškeré změny provedené lokálně na vašem počítači budou zaznamenány výhradně na této konkrétní větvi. Také, dokud zůstane tato větev vybraná na GitHub Desktop, soubory lokálně viditelné na vašem stroji odpovídají těmto větvi (`tuto-sparrow-wallet-loic`), a ne těm na hlavní větvi (`dev`).
![tutorial](assets/11.webp)
Pro každý nový článek, který chcete publikovat, budete muset vytvořit novou větev od `dev`. Větev v Gitu je paralelní verze projektu, která vám umožňuje provádět změny bez ovlivnění hlavní větve, dokud práce není připravena k začlenění.
### Přidání tutoriálu

Nyní, když je pracovní větev vytvořena, je čas integrovat váš nový tutoriál.
- Otevřete správce souborů a navigujte do složky `bitcoin-educational-content`, která představuje lokální klon vašeho repozitáře. Obvykle byste ji měli najít pod `Documents\GitHub\bitcoin-educational-content`. V tomto adresáři bude nutné najít vhodnou pod-složku pro umístění vašeho tutoriálu. Organizace složek odráží různé sekce webové stránky PlanB Network. V našem příkladu, protože chceme přidat tutoriál na Sparrow Wallet, je vhodné jít na následující cestu: `bitcoin-educational-content\tutorials\wallet`, která odpovídá sekci `WALLET` na webových stránkách: ![tutorial](assets/12.webp)
- V rámci složky `wallet` potřebujete vytvořit nový adresář specificky věnovaný vašemu tutoriálu. Název této složky musí evokovat software, o kterém je tutoriál, přičemž slova spojíte pomlčkami. V mém příkladu bude složka nazvána `sparrow-wallet`:
![tutorial](assets/13.webp)
- V této nové pod-složce věnované vašemu tutoriálu je třeba přidat několik prvků:
	- Vytvořte složku `assets`, určenou k přijímání všech ilustrací potřebných pro váš tutoriál;
    - V rámci této složky `assets` je třeba vytvořit 8 pod-složek pojmenovaných `fr`, `de`, `en`, `it`, `es`, `ja`, `vi` a `pt`, aby bylo možné klasifikovat vizuály podle odpovídajících jazyků. Musíte také přidat pod-složku `notext` pro vizuály, které nepotřebují překlad, jako jsou například snímky obrazovky;
	- Musí být vytvořen soubor `tutorial.yml` pro zaznamenání detailů souvisejících s vaším tutoriálem;
	- Soubor ve formátu markdown je třeba vytvořit pro psaní samotného obsahu vašeho tutoriálu. Tento soubor musí být pojmenován podle kódu jazyka psaní. Například pro tutoriál psaný ve francouzštině by soubor měl být nazván `fr.md`.
![tutorial](assets/14.webp)
- Shrnutí, zde je hierarchie souborů, které je třeba vytvořit:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (upravit podle správné kategorie)
        └── sparrow-wallet/ (upravit podle názvu tutoriálu)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (upravit podle odpovídajícího jazykového kódu)
```

- Začněte otevřením vašeho souboru `tutorial.yml` v editoru kódu.
- Vyplňte každé pole s informacemi uvedenými níže:
- **builder**: Zadejte název společnosti, která produkuje software, pro který vytváříte tutoriál;
- **tags**: Určete sérii klíčových slov úzce souvisejících s tématem vašeho článku, aby se usnadnilo jeho vyhledávání a indexace;
- **category**: Vyberte vhodnou podkategorii z dostupných na webu PlanB, na základě obsahu vašeho tutoriálu. Například pro tutoriál v sekci `WALLET`, dostupné možnosti jsou `Desktop`, `Hardware` a `Mobile`;
- **level**: Označte úroveň obtížnosti vašeho tutoriálu výběrem jedné ze čtyř následujících kategorií:
    - Začátečník (`beginner`),
    - Mírně pokročilý (`intermediary`),
    - Pokročilý (`advanced`),
    - Expert (`expert`).
- **professor**: Uveďte své ID přispěvatele, jak se objevuje na vašem profilu profesora. Pro více informací se odkazujte na [příslušný tutoriál](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (volitelně): Pokud si přejete uvést zdrojovou webovou stránku pro tutoriál, který vyvíjíte, jako je například vaše osobní stránka, zde můžete přidat příslušný odkaz.
![tutorial](assets/15.webp)
- Jakmile dokončíte úpravy vašeho souboru `tutorial.yml`, uložte váš dokument kliknutím na `Soubor > Uložit`:
![tutorial](assets/16.webp)
- Nyní můžete zavřít váš kódový editor.
- Ve složce `assets` musíte přidat soubor pojmenovaný `logo.webp`, který bude sloužit jako miniatura pro váš článek. Tento obrázek musí být ve formátu `.webp` a musí respektovat čtvercový rozměr, aby ladil s uživatelským rozhraním. Máte svobodu vybrat si logo softwaru, o kterém je tutoriál, nebo jakýkoliv jiný relevantní obrázek, za předpokladu, že je bez autorských práv. Kromě toho přidejte také obrázek s názvem `cover.webp` na stejné místo. Tento obrázek bude zobrazen na začátku vašeho tutoriálu. Ujistěte se, že tento obrázek, stejně jako logo, respektuje práva k použití a je vhodný pro kontext vašeho tutoriálu:
![tutorial](assets/17.webp)
- Nyní můžete otevřít váš soubor, který bude hostit váš tutoriál, pojmenovaný podle kódu vašeho jazyka, například `fr.md`. Přejděte na Obsidian, na levé straně okna, prolistujte strom složek do složky vašeho tutoriálu a k hledanému souboru:
![tutorial](assets/18.webp)
- Klikněte na soubor, aby se otevřel:
![tutorial](assets/19.webp)
- Začneme vyplněním sekce `Properties` na začátku dokumentu. Pokud tato sekce ve vašem souboru chybí (pokud je dokument zcela prázdný), můžete ji reprodukovat kopírováním z jiného existujícího tutoriálu: ![tutorial](assets/20.webp)
- Také ji můžete přidat ručně tímto způsobem pomocí vašeho kódového editoru:
```markdown
---
name: [Název]
description: [Popis]
---
```
![tutorial](assets/21.webp)
- Vyplňte název vašeho tutoriálu a krátký popis:
![tutorial](assets/22.webp)
- Poté přidejte na začátek vašeho tutoriálu obrázek obálky. K tomu napište:
```markdown
![cover-sparrow](assets/cover.webp)
```
- Tato syntaxe bude užitečná pokaždé, když je potřeba do tutoriálu přidat obrázek. Vykřičník označuje, že se jedná o obrázek, s alternativním textem (alt) uvedeným mezi hranatými závorkami. Cesta k obrázku je uvedena mezi závorkami:
![tutorial](assets/23.webp)
- Pokračujte psaním vašeho tutoriálu tím, že budete psát váš obsah. Když chcete integrovat podnadpis, použijte odpovídající formátování markdown předřazením textu `##`:
![tutorial](assets/24.webp)

### Jak přidat diagramy do tutoriálu?
Jazykové podsložky ve složce `assets` jsou určeny k organizaci diagramů a vizuálů, které doprovodí váš tutoriál. Pokud vaše obrázky obsahují text, ujistěte se, že je přeložíte pro každý dotčený jazyk, aby byl váš obsah přístupný mezinárodnímu publiku. Pro diagramy bez textu k překladu nebo snímky obrazovky je umístěte přímo do podsložky `notext`. ![tutorial](assets/25.webp)
Pro pojmenování vašich obrázků jednoduše vložte čísla v pořadí, v jakém se objevují v tutoriálu. Například pojmenujte váš první obrázek `1.webp`, váš druhý `2.webp` a tak dále.

Pokud je stejný diagram přeložen do více jazyků, zachovejte stejný název souboru pro různé překlady v jazykových podsložkách, například `en/1.webp`, `fr/1.webp`, `pt/1.webp` atd.

Máte možnost použít různé formáty obrázků, jako jsou `jpeg`, `png` nebo `webp`. Doporučuje se zvolit formát `webp`, aby byly obrázky méně objemné. ![tutorial](assets/26.webp)
Pro vložení diagramu do vašeho dokumentu použijte následující příkaz v Markdown, přičemž nezapomeňte specifikovat vhodný alternativní text a správnou cestu k obrázku:
```markdown
![vrabec](assets/notext/1.webp)
```
Vykřičník na začátku označuje, že jde o obrázek. Alternativní text, který pomáhá při přístupnosti a SEO, je umístěn mezi hranatými závorkami. Nakonec je cesta k obrázku uvedena mezi závorkami: ![tutorial](assets/27.webp)
Pokud si přejete vytvořit vlastní diagramy, ujistěte se, že dodržujete grafický manuál sítě PlanB, aby byla zajištěna vizuální konzistence:
- **Písmo**: Použijte [Rubik](https://fonts.google.com/specimen/Rubik);
- **Barvy**:
	- Oranžová: #FF5C00
	- Černá: #000000
	- Bílá: #FFFFFF

**Je nezbytné, aby všechny vizuály integrované do vašich tutoriálů byly bez autorských práv nebo v souladu s licencí zdrojového souboru**. Také všechny diagramy publikované na síti PlanB jsou k dispozici pod licencí CC-BY-SA stejně jako text.

**-> Tip:** Při veřejném sdílení souborů, jako jsou obrázky, je důležité odstranit veškerá nadbytečná metadata. Ta mohou obsahovat citlivé informace, jako jsou údaje o poloze, data vytvoření nebo podrobnosti o autorovi. Pro ochranu vašeho soukromí je vhodné tato metadata odstranit. Pro zjednodušení této operace můžete použít specializované nástroje jako [Exif Cleaner](https://exifcleaner.com/), který nabízí možnost vyčistit metadata dokumentu jednoduchým přetažením.

### Jak uložit a odeslat tutoriál?

Jakmile dokončíte psaní svého tutoriálu ve vybraném jazyce, dalším krokem je odeslání **Pull Requestu**. Administrátor poté přidá chybějící překlady vašeho tutoriálu díky naší automatizované metodě překladu.

- Pro provedení Pull Requestu otevřete software GitHub Desktop.
- Software by měl automaticky detekovat změny, které jste provedli lokálně ve srovnání s původním repozitářem. Před pokračováním pečlivě zkontrolujte na levé straně rozhraní, že tyto změny přesně odpovídají tomu, co jste očekávali: ![tutorial](assets/28.webp)
- Přidejte název pro váš commit, poté klikněte na modré tlačítko `Commit to [your branch]` pro potvrzení těchto změn: ![tutorial](assets/29.webp)
Commit je uložení změn provedených na větvi, doprovázené popisnou zprávou, která umožňuje sledovat vývoj projektu v čase. Jedná se tedy o jakýsi mezistupeň.
- Poté klikněte na tlačítko `Push origin`. Tím odešlete váš commit do vašeho forku: ![tutorial](assets/30.webp) - Pokud jste svůj tutoriál nedokončili, můžete se k němu později vrátit a vytvořit nové commity.
- Pokud jste dokončili úpravy pro tuto větev, nyní klikněte na tlačítko `Preview Pull Request`: ![tutorial](assets/31.webp)
- Můžete si naposledy zkontrolovat, že vaše úpravy jsou správné, poté klikněte na tlačítko `Create pull request`:
![tutorial](assets/32.webp)
Pull Request je žádost o začlenění změn z vaší větve do hlavní větve repozitáře PlanB Network, což umožňuje přezkoumání a diskusi o změnách před jejich sloučením.

- Budete automaticky přesměrováni ve vašem prohlížeči na GitHub na přípravnou stránku vašeho Pull Requestu:
![tutorial](assets/33.webp)
- Zadejte název, který stručně shrnuje úpravy, které si přejete sloučit s zdrojovým repozitářem.
- Přidejte stručný komentář popisující tyto změny.
- Klikněte na zelené tlačítko `Create pull request` a potvrďte žádost o sloučení:
![tutorial](assets/34.webp)
Váš PR bude poté viditelný na záložce `Pull Request` hlavního repozitáře PlanB Network. Nyní už jen stačí počkat, až vás administrátor kontaktuje s potvrzením sloučení vašeho příspěvku nebo s žádostí o jakékoli další úpravy.
![tutorial](assets/35.webp)
Po sloučení vašeho PR s hlavní větví se doporučuje smazat vaši pracovní větev (`tuto-sparrow-wallet`), aby se udržela čistá historie na vašem forku. GitHub vám tuto možnost automaticky nabídne na stránce vašeho PR:
![tutorial](assets/36.webp)
V softwaru GitHub Desktop můžete přepnout zpět na hlavní větev vašeho forku (`dev`).
![tutorial](assets/7.webp)
Pokud si přejete provést úpravy vašeho příspěvku po již odeslaném PR, postup závisí na aktuálním stavu vašeho PR:
- Pokud je váš PR stále otevřený a ještě nebyl sloučen, proveďte úpravy lokálně při zůstání na stejné větvi. Jakmile jsou úpravy dokončeny, použijte tlačítko `Push origin` k přidání nového commitu do vašeho stále otevřeného PR;
- V případě, že váš PR byl již sloučen s hlavní větví, budete muset celý proces začít od začátku vytvořením nové větve, a poté odesláním nového PR. Před pokračováním se ujistěte, že váš lokální repozitář je synchronizován se zdrojovým repozitářem PlanB Network.
