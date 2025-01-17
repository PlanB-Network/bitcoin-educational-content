---
name: Základy GitHubu
description: Porozumění základům Gitu a GitHubu
---

![cover](assets/cover.webp)

Mise PlanB je poskytovat špičkové vzdělávací zdroje o Bitcoinu, dostupné v co nejvíce jazycích. Veškerý obsah publikovaný na webu je open-source a hostovaný na GitHubu, což nabízí každému možnost přispět k obohacení platformy. Příspěvky mohou mít různé formy: oprava a korektura stávajících textů, překlad do jiných jazyků, aktualizace informací nebo vytváření nových tutoriálů, které ještě nejsou na našem webu dostupné.

Pokud si přejete přispět do sítě PlanB, budete potřebovat používat Git a GitHub. Pokud jsou pro vás tyto nástroje neznámé nebo pokud se jejich fungování jeví jako nejasné, nepanikařte, tento článek je pro vás! Společně si projdeme základy Gitu a GitHubu, stejně jako s nimi spojenou technickou terminologii, abyste tyto nástroje mohli následně efektivně používat.

## Co je Git?

Git je systém pro správu verzí, speciálně navržený pro správu softwarových projektů. Vytvořený v roce 2005 Linusem Torvaldsem, Git se rychle stal standardem v průmyslu softwarového vývoje pro správu verzí. Ale co to přesně znamená?
![git](assets/1.webp)
Ve své podstatě Git umožňuje vývojářům sledovat změny provedené v zdrojovém kódu projektu v průběhu času. To znamená, že s každou změnou v kódu Git zaznamená novou verzi projektu. Pokud dojde k chybě nebo pokud experimentální funkce nefunguje podle očekávání, je možné se vrátit k předchozímu stavu kódu, jako kdyby to byl jakýsi stroj času pro soubory.

Jednou z klíčových funkcí Gitu je správa větví. Větev je jakási paralelní linie, kde mohou vývojáři pracovat nezávisle na zbytku projektu. To velmi usnadňuje přidávání nových funkcí nebo opravu chyb bez rušení hlavního kódu. Jakmile jsou úpravy otestovány a ověřeny, mohou být sloučeny s hlavní větví.

Jednou z osobitostí Gitu je jeho schopnost fungovat distribuovaně. Každý vývojář má na svém vlastním pevném disku kompletní kopii projektu, což mu umožňuje pracovat offline a později sloučit změny, když je k dispozici internetové připojení. To snižuje riziko konfliktů a umožňuje více vývojářům současně pracovat na stejném projektu bez vzájemného rušení.
Původně byl Git primárně navržen pro projekty softwarového vývoje. Nicméně, může být také použit pro správu projektů psaní obsahu. Místo spolupráce na kódu spolupracujeme na textu. A právě tuto metodu síť PlanB přijala pro správu svého obsahu! Git usnadňuje spolupráci na psaní kurzů a tutoriálů, protože umožňuje přesné sledování změn, efektivní správu verzí a také umožňuje revizi a zlepšení obsahu ostatními přispěvateli.
## Co je GitHub?

GitHub je platforma pro správu a hostování zdrojového kódu založená na systému správy verzí Git, o kterém jsme právě diskutovali. Spuštěný v roce 2008, GitHub rychle získal popularitu a stal se nezbytnou referencí pro vývojáře po celém světě. Ale jak se GitHub liší od Gitu a proč je tak klíčový v naší metodě produkce obsahu?
![github](assets/2.webp)
Nejprve je důležité pochopit, že GitHub je postaven na Gitu (o kterém jsme diskutovali v předchozí sekci). Zatímco Git je nástroj, který sleduje změny kódu, GitHub je online služba, která tento kód hostuje, sdílí a spravuje.

Představte si Git jako jakýsi deník, který každý vývojář používá na svém vlastním počítači k zaznamenání všech změn ve svém projektu. GitHub na druhou stranu je jako veřejná knihovna, kde všechny tyto deníky mohou být sdíleny, porovnávány a kombinovány.
Základní rozdíl mezi Git a GitHub spočívá ve jejich funkci: Git je nástroj používaný lokálně každým vývojářem pro správu verzí jejich kódu, zatímco GitHub je online platforma, která tyto verze hostuje a usnadňuje spolupráci.
GitHub je mnohem více než jen služba pro hostování kódu. Je to platforma pro spolupráci, která umožňuje vývojářům efektivně spolupracovat. A skutečně, PlanB Network používá tuto platformu nejen pro hostování veškerého kódu, který pohání webovou stránku, ale také, a to nás zajímá, veškerého obsahu (tutoriály, školení, zdroje...).

## Některé technické termíny

Na Gitu a GitHubu se setkáte s příkazy a funkcemi, jejichž názvy se mohou zdát složité. V této poslední části poskytuji jednoduché definice pro pochopení technických termínů, se kterými se můžete setkat při používání Gitu a GitHubu:

- **Fetch origin:** Příkaz, který načte nedávné informace a změny z vzdáleného repozitáře bez jejich sloučení s vaší lokální prací. Aktualizuje váš lokální repozitář o nové větve a commity přítomné ve vzdáleném repozitáři.

- **Pull origin:** Příkaz, který načte aktualizace z vzdáleného repozitáře a okamžitě je integruje do vaší lokální větve pro synchronizaci. Kombinuje kroky fetch a merge do jediného příkazu.
- **Sync Fork:** Funkce na GitHubu, která vám umožňuje aktualizovat váš fork projektu s nejnovějšími změnami z původního repozitáře. To zajišťuje, že vaše kopie projektu zůstává aktuální s hlavním vývojem.
- **Push origin:** Příkaz používaný k odeslání vašich lokálních změn do vzdáleného repozitáře.

- **Pull Request:** Žádost poslaná přispěvatelem, která označuje, že do větve ve vzdáleném repozitáři byly odeslány změny a přeje si, aby tyto změny byly posouzeny a potenciálně sloučeny do hlavní větve repozitáře.

- **Commit:** Uložení vašich změn. Commit je jako okamžitý snímek vaší práce v daném okamžiku, který umožňuje uchovat historii změn. Každý commit zahrnuje popisnou zprávu vysvětlující, co bylo změněno.

- **Branch:** Paralelní verze repozitáře, která vám umožňuje pracovat na změnách bez ovlivnění hlavní větve (často nazývané "main" nebo "master"). Větve usnadňují vývoj nových funkcí a opravu chyb bez rizika narušení stabilního kódu.

- **Merge:** Sloučení spočívá v integraci změn z jedné větve do druhé. Používá se například k přidání změn z pracovní větve na hlavní větev, což umožňuje přidávat různé příspěvky.

- **Fork:** Vytvoření forku repozitáře znamená vytvoření kopie tohoto repozitáře na vašem vlastním účtu GitHub, což vám umožňuje pracovat na projektu bez ovlivnění původního repozitáře. Fork může buď jít vlastní cestou a stát se odlišným projektem od původního, nebo se pravidelně synchronizovat s původním projektem, aby přispíval k němu.

- **Clone:** Klonování repozitáře znamená vytvoření lokální kopie na vašem počítači, což vám dává přístup ke všem souborům a historii. To vám umožňuje přímo lokálně pracovat na projektu.

- **Repository:** Úložiště pro projekt na GitHubu. Repozitář obsahuje všechny soubory projektu i historii všech provedených změn. Je základem úložiště a spolupráce na GitHubu.

- **Issue:** Nástroj pro sledování úkolů a chyb na GitHubu. Issues umožňují hlásit problémy, navrhovat vylepšení nebo diskutovat o nových funkcích. Každé issue může být přiřazeno, označeno a komentováno.

Tento seznam samozřejmě není vyčerpávající. Existuje mnoho dalších technických termínů specifických pro Git a GitHub. Nicméně ty zmíněné zde jsou hlavní, se kterými se budete často setkávat.
Po přečtení tohoto článku je možné, že některé aspekty Gitu a GitHubu vám stále nejsou zcela jasné. Doporučuji vám začít tyto nástroje používat sami. Praxe je často nejlepší způsob, jak pochopit, jak stroj funguje! A pro začátek můžete objevit tyto 2 další tutoriály:
**[Vytvořte si účet na GitHubu](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Nastavení vašeho lokálního prostředí pro přispívání do PlanB Network](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**