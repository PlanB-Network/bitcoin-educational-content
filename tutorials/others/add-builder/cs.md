---
name: Přidání tvůrce
description: Jak navrhnout přidání nového tvůrce na síť PlanB Network?
---
![builder](assets/cover.webp)

Mise PlanB je poskytovat špičkové vzdělávací zdroje o Bitcoinu v co nejvíce jazycích. Veškerý obsah publikovaný na webu je open-source a hostován na GitHubu, což umožňuje každému podílet se na obohacování platformy.

Chcete-li přidat nového Bitcoin "tvůrce" na web síti PlanB Network a zvýšit viditelnost vaší společnosti nebo softwaru, ale nevíte jak? Tento tutoriál je pro vás!
![builder](assets/01.webp)
- Nejprve potřebujete mít účet na GitHubu. Pokud nevíte, jak vytvořit účet, připravili jsme podrobný tutoriál, který vás provede.

https://planb.network/tutorials/others/create-github-account


- Přejděte na [GitHub repozitář PlanB věnovaný datům](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) v sekci `resources/builder/`:
![builder](assets/02.webp)
- Klikněte vpravo nahoře na tlačítko `Add file` a poté na `Create new file`:
![builder](assets/03.webp)
- Pokud jste předtím nikdy nepřispívali k obsahu síti PlanB Network, budete muset vytvořit svůj fork původního repozitáře. Forknutí repozitáře znamená vytvoření kopie tohoto repozitáře na vašem vlastním účtu na GitHubu, což vám umožní pracovat na projektu bez ovlivnění původního repozitáře. Klikněte na tlačítko `Fork this repository`:
![builder](assets/04.webp)
- Poté se dostanete na stránku GitHubu pro úpravy:
![builder](assets/05.webp)
- Vytvořte složku pro vaši společnost. Chcete-li to provést, do pole `Name your file...` napište název vaší společnosti malými písmeny s pomlčkami místo mezer. Například, pokud se vaše společnost jmenuje "Bitcoin Baguette", měli byste napsat `bitcoin-baguette`:
![builder](assets/06.webp)
- Pro potvrzení vytvoření složky jednoduše přidejte lomítko za název ve stejném poli, například: `bitcoin-baguette/`. Přidání lomítka automaticky vytvoří složku místo souboru:
![builder](assets/07.webp)
- V této složce vytvoříte první YAML soubor pojmenovaný `builder.yml`:
![builder](assets/08.webp)
- Vyplňte tento soubor informacemi o vaší společnosti podle této šablony:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Co vyplnit pro každý klíč:
- `name`: Název vaší společnosti (povinné);
- `address` : Umístění vaší firmy (volitelné);
- `language` : Země, ve kterých vaše firma působí, nebo podporované jazyky (volitelné);
- `links` : Různé oficiální odkazy vaší firmy (volitelné);
- `tags` : 2 termíny, které kvalifikují vaši firmu (povinné);
- `category` : Kategorie, která nejlépe popisuje oblast, ve které vaše firma působí, z následujících možností:
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.
Například váš soubor YAML by mohl vypadat takto:
```yaml
name: Bitcoin Baguette

address_line_1: Paříž, Francie
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - vzdělávání

category: vzdělávání
```

![builder](assets/09.webp)
- Jakmile dokončíte úpravy tohoto souboru, uložte je kliknutím na tlačítko `Commit changes...`:
![builder](assets/10.webp)
- Přidejte název pro vaše změny spolu s krátkým popisem:
![builder](assets/11.webp)
- Klikněte na zelené tlačítko `Propose changes`:
![builder](assets/12.webp)
- Poté se dostanete na stránku shrnující všechny vaše změny:
![builder](assets/13.webp)
- Klikněte na obrázek vašeho profilu GitHub v pravém horním rohu, poté na `Your Repositories`:
![builder](assets/14.webp)
- Vyberte váš fork repozitáře PlanB Network:
![builder](assets/15.webp)
- Na vrchu okna byste měli vidět oznámení s vaší novou větví. Pravděpodobně se jmenuje `patch-1`. Klikněte na ni:
![builder](assets/16.webp)
- Nyní jste ve vaší pracovní větvi (**ujistěte se, že jste ve stejné větvi jako vaše předchozí úpravy, to je důležité!**):
![builder](assets/17.webp)
- Vraťte se do složky `resources/builders/` a vyberte složku vašeho podnikání, kterou jste právě vytvořili v předchozím commitu:
![builder](assets/18.webp)
- Ve složce vašeho podnikání klikněte na tlačítko `Add file`, poté na `Create new file`:
![builder](assets/19.webp)
- Pojmenujte tuto novou složku `assets` a potvrďte její vytvoření umístěním lomítka `/` na konci:
![builder](assets/20.webp)
- V této složce `assets` vytvořte soubor s názvem `.gitkeep`:
![builder](assets/21.webp)
- Klikněte na tlačítko `Commit changes...`:
![builder](assets/22.webp)
- Nechte název commitu jako výchozí a ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`: ![builder](assets/23.webp)
- Vraťte se do složky `assets`:
![builder](assets/24.webp)
- Klikněte na tlačítko `Add file`, poté na `Upload files`:
![builder](assets/25.webp)
- Otevře se nová stránka. Přetáhněte obrázek vaší společnosti nebo vašeho softwaru do oblasti. Tento obrázek bude zobrazen na webu PlanB Network:
![builder](assets/26.webp)
- Může to být logo nebo ikona:
![builder](assets/27.webp)
- Jakmile je obrázek nahrán, ověřte, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`:
![builder](assets/28.webp)
- Pozor, váš obrázek musí být čtvercový, musí být pojmenován `logo`, a musí být ve formátu `.webp`. Celý název souboru by tedy měl být: `logo.webp`:
![builder](assets/29.webp)
- Vraťte se do vaší složky `assets` a klikněte na mezi soubor `.gitkeep`:
![builder](assets/30.webp)- Jakmile budete na souboru, klikněte na tři malé tečky v pravém horním rohu a poté na `Delete file` (Smazat soubor):
![builder](assets/31.webp)
- Ověřte, že jste stále na stejné pracovní větvi, poté klikněte na tlačítko `Commit changes` (Potvrdit změny):
![builder](assets/32.webp)
- Přidejte název a popis k vašemu commitu, poté klikněte na `Commit changes` (Potvrdit změny):
![builder](assets/33.webp)
- Vraťte se do složky vaší společnosti:
![builder](assets/34.webp)
- Klikněte na tlačítko `Add file` (Přidat soubor), poté na `Create new file` (Vytvořit nový soubor):
![builder](assets/35.webp)
- Vytvořte nový YAML soubor pojmenováním ho indikátorem vašeho mateřského jazyka. Tento soubor bude použit pro popis builderu. Například, pokud chci napsat můj popis v angličtině, pojmenuji tento soubor `en.yml`:
![builder](assets/36.webp)
- Vyplňte tento YAML soubor použitím této šablony:
```yaml
description: |
 
contributors:
 - 
```

- Pro klíč `contributors` můžete přidat váš identifikátor přispěvatele do PlanB Network, pokud jej máte. Pokud ne, nechte toto pole prázdné.
- Pro klíč `description` stačí přidat krátký odstavec, který popisuje vaši společnost nebo váš software. Popis musí být ve stejném jazyce jako název souboru. Nemusíte překládat tento popis do všech jazyků podporovaných na webu, protože to udělají týmy PlanB pomocí svého modelu. Například, tady je, jak by váš soubor mohl vypadat:
```yaml
description: |
Založená v roce 2017, Bitcoin Baguette je pařížská asociace věnovaná organizování setkání a technických workshopů na téma Bitcoin. Sjednocujeme nadšence, odborníky a zvídavé mysli k prozkoumávání a diskusi o složitostech technologie Bitcoin. Naše akce poskytují platformu pro sdílení znalostí, networking a prohlubování porozumění vnitřním mechanismům Bitcoinu. Přidejte se k nám v Bitcoin Baguette, abyste byli součástí pařížské komunity Bitcoinu a zůstali v obraze nejnovějších pokroků v oblasti.

contributors:
- 
```
![builder](assets/37.webp)
- Klikněte na tlačítko `Commit changes` (Potvrdit změny):
![builder](assets/38.webp)
- Ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch` (Přímo potvrdit do větve patch-1), přidejte název, poté klikněte na `Commit changes` (Potvrdit změny):
![builder](assets/39.webp)
- Složka vaší společnosti by nyní měla vypadat takto:
![builder](assets/40.webp)
- Pokud je vše k vaší spokojenosti, vraťte se do kořenové složky vašeho forku:
![builder](assets/41.webp)
- Měli byste vidět zprávu oznamující, že vaše větev prošla změnami. Klikněte na tlačítko `Compare & pull request` (Porovnat a vytvořit pull request):
![builder](assets/42.webp)
- Přidejte jasný název a popis k vašemu PR:
![builder](assets/43.webp)
- Klikněte na tlačítko `Create pull request` (Vytvořit pull request):
![builder](assets/44.webp)
Gratulujeme! Váš PR byl úspěšně vytvořen. Administrátor jej nyní zkontroluje a pokud je vše v pořádku, začlení jej do hlavního repozitáře PlanB Network. Váš profil builderu by se na webu měl objevit o několik dní později.

Nezapomeňte sledovat průběh vašeho PR. Administrátor může zanechat komentář s žádostí o dodatečné informace. Dokud váš PR není schválen, můžete jej konzultovat na záložce `Pull requests` (Pull requesty) na GitHub repozitáři PlanB Network:
![builder](assets/45.webp)
Moc vám děkujeme za vaši cennou příspěvek! :)
