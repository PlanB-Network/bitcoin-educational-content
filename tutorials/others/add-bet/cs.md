---
name: Přidání vzdělávacích nástrojů
description: Jak přidat nové vzdělávací materiály na PlanB Network?
---
![event](assets/cover.webp)

Mise PlanB je poskytovat přední vzdělávací zdroje o Bitcoinu v co nejvíce jazycích. Veškerý obsah publikovaný na webu je open-source a hostovaný na GitHubu, což umožňuje každému podílet se na obohacování platformy.

Kromě tutoriálů a školení nabízí PlanB Network také rozsáhlou knihovnu různorodého vzdělávacího obsahu o Bitcoinu, přístupného všem, [v sekci "BET" (_Bitcoin Educational Toolkit_) ](https://planb.network/resources/bet). Tato databáze zahrnuje vzdělávací plakáty, memy, humorné propagační plakáty, technické diagramy, loga a další nástroje pro uživatele. Cílem této iniciativy je podporovat jednotlivce a komunity vyučující o Bitcoinu po celém světě tím, že jim poskytne potřebné vizuální zdroje.

Chcete se podílet na obohacování této databáze, ale nevíte jak? Tento tutoriál je pro vás!

*Je nezbytné, aby veškerý obsah začleněný na web byl bez autorských práv nebo respektoval licenci zdrojového souboru. Také všechny vizuály publikované na PlanB Network jsou k dispozici pod licencí [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*
![event](assets/01.webp)
- Nejprve potřebujete mít účet na GitHubu. Pokud nevíte, jak vytvořit účet, připravili jsme podrobný tutoriál, který vás provede.

https://planb.network/tutorials/others/create-github-account


- Přejděte na [GitHubový repozitář PlanB věnovaný datům](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) v sekci `resources/bet/`:
![event](assets/02.webp)
- Klikněte vpravo nahoře na tlačítko `Add file`, poté na `Create new file`:
![event](assets/03.webp)
- Pokud jste předtím nikdy nepřispívali k obsahu PlanB Network, budete muset vytvořit svůj fork původního repozitáře. Forknutí repozitáře znamená vytvoření kopie tohoto repozitáře na vašem vlastním účtu GitHub, což vám umožní pracovat na projektu bez ovlivnění původního repozitáře. Klikněte na tlačítko `Fork this repository`:
![event](assets/04.webp)
- Poté se dostanete na stránku GitHubu pro úpravy:
![event](assets/05.webp)
- Vytvořte složku pro váš obsah. Chcete-li to provést, do pole `Name your file...` napište název vašeho obsahu malými písmeny s pomlčkami místo mezer. V mém příkladu, řekněme, že chci přidat PDF vizuál seznamu 2048 slov BIP39. Takže pojmenuji mou složku `bip39-wordlist`: ![event](assets/06.webp)
- Pro potvrzení vytvoření složky jednoduše přidejte lomítko za název ve stejném poli, například: `bip39-wordlist/`. Přidání lomítka automaticky vytvoří složku místo souboru:
![event](assets/07.webp)
- V této složce vytvoříte první YAML soubor pojmenovaný `bet.yml`:
![event](assets/08.webp)
- Vyplňte tento soubor informacemi týkajícími se vašeho obsahu pomocí této šablony:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```
- **`builder`**: Uveďte identifikátor vaší organizace na síti PlanB Network. Pokud ještě nemáte pro vaši společnost identifikátor "builder", můžete si jej vytvořit podle tohoto návodu.

https://planb.network/tutorials/others/add-builder

 Pokud žádný nemáte, můžete jednoduše použít své jméno, pseudonym nebo název vaší společnosti, aniž byste vytvořili profil builder.
- **`type`**: Vyberte povahu vašeho obsahu z následujících dvou možností:
	- `Educational Content` pro vzdělávací obsahy.
	- `Visual Content` pro ostatní typy různorodého obsahu.

- **`links`**: Poskytněte odkazy na své obsahy. Máte dvě možnosti:
	- Pokud se rozhodnete hostovat svůj obsah přímo na GitHubu PlanB, budete muset přidat odkazy na tento soubor v následujících krocích.
	- Pokud jsou vaše obsahy hostovány jinde, například na vašem osobním webu, uveďte zde příslušné odkazy:
	    - `download`: Odkaz ke stažení vašeho obsahu.
	    - `view`: Odkaz pro zobrazení vašeho obsahu (může být stejný jako odkaz ke stažení). Pokud je váš obsah dostupný v několika jazycích, přidejte odkaz pro každý jazyk.

- **`tags`**: Přidejte dva tagy spojené s vaším obsahem. Příklady:
	- bitcoin
	- technologie
	- ekonomie
	- vzdělávání
	- meme...

- **`contributors`**: Uveďte svůj identifikátor přispěvatele, pokud jeden máte.

Například váš YAML soubor by mohl vypadat takto:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- V mém příkladu nechám odkazy zatím prázdné, protože svůj PDF soubor přidám přímo na GitHub:
![event](assets/09.webp)
- Jakmile dokončíte úpravy tohoto souboru, uložte je kliknutím na tlačítko `Commit changes...`:
![event](assets/10.webp)
- Přidejte název pro vaše úpravy, stejně jako krátký popis:
![event](assets/11.webp)
- Klikněte na zelené tlačítko `Propose changes`:
![event](assets/12.webp)
- Poté se dostanete na stránku, která shrnuje všechny vaše změny:
![event](assets/13.webp)
- Klikněte na obrázek vašeho profilu GitHub v pravém horním rohu, poté na `Your Repositories`:
![event](assets/14.webp)
- Vyberte váš fork repozitáře PlanB Network:
![event](assets/15.webp)
- Na vrchu okna byste měli vidět oznámení s vaší novou větví. Pravděpodobně se jmenuje `patch-1`. Klikněte na ni:
![event](assets/16.webp)
- Nyní jste ve vaší pracovní větvi (**ujistěte se, že jste ve stejné větvi jako vaše předchozí úpravy, to je důležité!**):
![event](assets/17.webp)
- Vraťte se do složky `resources/bet/` a vyberte složku vašeho obsahu, kterou jste právě vytvořili v předchozím commitu:
![event](assets/18.webp)
- Ve složce vašeho obsahu klikněte na tlačítko `Add file`, poté na `Create new file`:
![event](assets/19.webp)
- Tuto novou složku pojmenujte `assets` a potvrďte její vytvoření umístěním lomítka `/` na konci:
![event](assets/20.webp)
- V této složce `assets` vytvořte soubor pojmenovaný `.gitkeep`: ![event](assets/21.webp)
- Klikněte na tlačítko `Commit changes...`: ![event](assets/22.webp)- Ponechte název commitu ve výchozím nastavení a ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`: ![event](assets/23.webp)
- Vraťte se do složky `assets`: ![event](assets/24.webp)
- Klikněte na tlačítko `Add file`, poté na `Upload files`: ![event](assets/25.webp)
- Otevře se nová stránka. Přetáhněte miniaturu, která reprezentuje váš obsah, do oblasti. Tento obrázek bude zobrazen na webu PlanB Network: ![event](assets/26.webp)
- Může to být náhled, logo nebo ikona: ![event](assets/27.webp)
- Jakmile je obrázek nahrán, ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`: ![event](assets/28.webp)
- Buďte opatrní, váš obrázek musí být pojmenován `logo` a musí být ve formátu `.webp`. Celý název souboru by tedy měl být: `logo.webp`: ![event](assets/29.webp)
- Vraťte se do vaší složky `assets` a klikněte na mezi soubor `.gitkeep`: ![event](assets/30.webp)
- Jakmile jste na souboru, klikněte na tři malé tečky v pravém horním rohu a poté na `Delete file`: ![event](assets/31.webp)
- Ujistěte se, že jste stále na stejné pracovní větvi, poté klikněte na tlačítko `Commit changes`: ![event](assets/32.webp)
- Přidejte název a popis k vašemu commitu, poté klikněte na `Commit changes`: ![event](assets/33.webp)
- Vraťte se do složky vašeho obsahu: ![event](assets/34.webp)
- Klikněte na tlačítko `Add file`, poté na `Create new file`: ![event](assets/35.webp)
- Vytvořte nový YAML soubor pojmenováním ho indikátorem vašeho mateřského jazyka. Tento soubor bude použit pro popis obsahu. Například, pokud chci napsat můj popis v angličtině, pojmenuji tento soubor `en.yml`: ![event](assets/36.webp)
- Vyplňte tento YAML soubor použitím této šablony:

```yaml
name: 
description: |
  
```

- Pro klíč `name` můžete přidat název vašeho obsahu;
- Pro klíč `description` stačí přidat krátký odstavec, který popisuje váš obsah. Popis musí být ve stejném jazyce jako název souboru. Není nutné překládat tento popis do všech podporovaných jazyků na webu, jelikož to udělají týmy PlanB pomocí jejich modelu.
Například, zde je, jak by váš soubor mohl vypadat:

```yaml
name: BIP39 WORDLIST
description: |
  Kompletní a číslovaný seznam 2048 anglických slov z BIP39 slovníku používaného pro kódování mnemonických frází. Dokument lze vytisknout na jedné stránce.
```

![event](assets/37.webp)
- Klikněte na tlačítko `Commit changes...`:
![event](assets/38.webp)
- Ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, přidejte název, poté klikněte na `Commit changes`:
![event](assets/39.webp)
- Složka vašeho obsahu by nyní měla vypadat takto:
![event](assets/40.webp)
*Pokud nechcete přidávat obsah na GitHub a již jste si v předchozích krocích zaznamenali odkazy v souboru `bet.yml`, můžete tuto sekci přeskočit a přejít přímo na část týkající se vytvoření Pull Requestu.*
- Vraťte se do složky `/assets`:
![událost](assets/41.webp)
- Klikněte na tlačítko `Add file` a poté na `Upload files`:
![událost](assets/42.webp)
- Otevře se nová stránka. Přetáhněte do oblasti obsah, který chcete sdílet:
![událost](assets/43.webp)
- Například jsem přidal PDF soubor seznamu BIP39:
![událost](assets/44.webp)
- Jakmile je obsah nahrán, ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, a poté klikněte na `Commit changes`:
![událost](assets/45.webp)
- Vraťte se do vaší složky `/assets` a klikněte na soubor, který jste právě nahráli:
![událost](assets/46.webp)
- Získejte mezičlánek URL vašeho souboru. Například v mém případě je URL:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Ponechte pouze poslední část URL od `/resources` dále:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- K základu URL přidejte následující informace, abyste měli správný odkaz:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

To, co zde děláme, je předvídání budoucího odkazu na váš soubor, jakmile bude váš návrh sloučen do zdrojového repozitáře sítě PlanB.
- Vraťte se do vašeho souboru `bet.yml` a klikněte na ikonu tužky: ![událost](assets/47.webp)
- Tam přidejte váš odkaz:
![událost](assets/48.webp)
- Jakmile jsou vaše změny dokončeny, klikněte na tlačítko `Commit changes...`:
![událost](assets/49.webp)
- Přidejte název pro vaše změny, stejně jako krátký popis:
![událost](assets/50.webp)
- Klikněte na zelené tlačítko `Commit changes`:
![událost](assets/51.webp)

---

- Pokud je pro vás vše v pořádku, vraťte se do kořenové složky vašeho forku:
![událost](assets/52.webp)
- Měli byste vidět zprávu, která oznamuje, že vaše větev byla upravena. Klikněte na tlačítko `Compare & pull request`:
![událost](assets/53.webp)
- Přidejte jasný název a popis pro váš PR:
![událost](assets/54.webp)
- Klikněte na tlačítko `Create pull request`:
![událost](assets/55.webp)
Gratulujeme! Váš PR byl úspěšně vytvořen. Administrátor jej nyní zkontroluje a pokud je vše v pořádku, sloučí ho do hlavního repozitáře sítě PlanB. Váš BET by se na webu měl objevit o několik dní později.

Nezapomeňte sledovat průběh vašeho PR. Administrátor vám může zanechat komentář s žádostí o dodatečné informace. Dokud váš PR není validován, můžete ho konzultovat na kartě Pull requests v GitHub repozitáři sítě PlanB:
![událost](assets/56.webp)
Moc vám děkujeme za váš cenný příspěvek! :)
