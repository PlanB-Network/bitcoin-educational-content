---
name: Přidání podcastu do sítě PlanB
description: Jak přidat nový podcast do sítě PlanB?
---
![podcast](assets/cover.webp)

Mise PlanB je poskytovat špičkové vzdělávací zdroje o Bitcoinu v co nejvíce jazycích. Veškerý obsah publikovaný na stránkách je open-source a hostovaný na GitHubu, což umožňuje každému podílet se na obohacování platformy.

Chcete přidat Bitcoin podcast na stránky sítě PlanB a zvýšit viditelnost vašeho pořadu, ale nevíte jak? Tento tutoriál je pro vás!
![podcast](assets/01.webp)
- Nejprve potřebujete mít účet na GitHubu. Pokud nevíte, jak jej vytvořit, připravili jsme podrobný tutoriál, který vás provede.

https://planb.network/tutorials/others/create-github-account


- Přejděte na [GitHubový repozitář PlanB věnovaný datům](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) v sekci `resources/podcasts/`:
![podcast](assets/02.webp)
- Klikněte vpravo nahoře na tlačítko `Add file` a poté na `Create new file`:
![podcast](assets/03.webp)
- Pokud jste nikdy předtím nepřispívali na obsah sítě PlanB, budete muset vytvořit svůj fork původního repozitáře. Forknutí repozitáře znamená vytvoření kopie tohoto repozitáře na vašem vlastním účtu na GitHubu, což vám umožní pracovat na projektu bez ovlivnění původního repozitáře. Klikněte na tlačítko `Fork this repository`:
![podcast](assets/04.webp)
- Poté se dostanete na stránku GitHubu pro úpravy:
![podcast](assets/05.webp)
- Vytvořte složku pro váš podcast. Chcete-li to provést, do pole `Name your file...` napište název vašeho podcastu malými písmeny a místo mezer použijte pomlčky. Například, pokud se váš pořad jmenuje "Super Podcast Bitcoin", měli byste napsat `super-podcast-bitcoin`:
![podcast](assets/06.webp)
- Pro potvrzení vytvoření složky jednoduše přidejte lomítko za název vašeho podcastu ve stejném poli, například: `super-podcast-bitcoin/`. Přidání lomítka automaticky vytvoří složku místo souboru:
![podcast](assets/07.webp)
- V této složce vytvoříte první YAML soubor pojmenovaný `podcast.yml`:
![podcast](assets/08.webp)
- Vyplňte tento soubor informacemi o vašem podcastu pomocí této šablony:

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Zde jsou podrobnosti, které je třeba vyplnit pro každé pole:

- **`name`**: Uveďte název vašeho podcastu.
- **`host`**: Uveďte jména nebo pseudonymy mluvčích nebo hostitele podcastu. Každé jméno by mělo být odděleno čárkou.
- **`language`**: Uveďte kód jazyka, ve kterém je váš podcast mluven. Například pro angličtinu uveďte `en`, pro italštinu `it`...

- **`links`**: Poskytněte odkazy na váš obsah. Máte dvě možnosti:
	- `podcast`: odkaz na váš podcast,
	- `twitter`: odkaz na Twitter profil podcastu nebo organizace, která jej produkuje,
	- `website`: odkaz na webové stránky podcastu nebo organizace, která jej produkuje.
```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin je technická ŽIVÁ relace konaná jednou týdně na Twitteru, která se podrobně zabývá protokolem Bitcoin, řešeními druhé vrstvy a vším, co vás ohromí. Naši moderátoři Lounes, Pantamis, Loïc a Sosthene zodpoví vaše otázky a nabídnou nejtechničtější pořad o Bitcoinu na světě.

tags:
  - bitcoin
  - technologie
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Jakmile dokončíte úpravy tohoto souboru, uložte je kliknutím na tlačítko `Commit changes...`:
![podcast](assets/10.webp)
- Přidejte název pro vaše změny, stejně jako krátký popis:
![podcast](assets/11.webp)
- Klikněte na zelené tlačítko `Propose changes`:
![podcast](assets/12.webp)
- Poté se dostanete na stránku, která shrnuje všechny vaše změny:
![podcast](assets/13.webp)
- Klikněte na vaši profilovou fotografii v pravém horním rohu, poté na `Your Repositories`:
![podcast](assets/14.webp)
- Vyberte váš fork repozitáře PlanB Network:
![podcast](assets/15.webp)
- Na vrchu okna byste měli vidět oznámení s vaší novou větví. Pravděpodobně se jmenuje `patch-1`. Klikněte na ni:
![podcast](assets/16.webp)
- Nyní jste ve vaší pracovní větvi:
![podcast](assets/17.webp)
- Vraťte se do složky `resources/podcast/` a vyberte složku podcastu, kterou jste právě vytvořili v předchozím commitu: ![podcast](assets/18.webp)
- Ve vaší složce podcastu klikněte na tlačítko `Add file`, poté na `Create new file`:
![podcast](assets/19.webp)
- Pojmenujte tuto novou složku `assets` a potvrďte její vytvoření přidáním lomítka `/` na konec:
![podcast](assets/20.webp)
- V této složce `assets` vytvořte soubor s názvem `.gitkeep`:
![podcast](assets/21.webp)
- Klikněte na tlačítko `Commit changes...`:
![podcast](assets/22.webp)
- Nechte název commitu jako výchozí a ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`:
![podcast](assets/23.webp)
- Vraťte se do složky `assets`:
![podcast](assets/24.webp)
- Klikněte na tlačítko `Add file`, poté na `Upload files`:
![podcast](assets/25.webp)
- Otevře se nová stránka. Přetáhněte logo vašeho podcastu do dané oblasti. Tento obrázek bude zobrazen na webu PlanB Network: ![podcast](assets/26.webp)
- Buďte opatrní, obrázek musí být čtvercový, aby co nejlépe pasoval na náš web: ![podcast](assets/27.webp)
- Jakmile je obrázek nahrán, ověřte, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`: ![podcast](assets/28.webp)
- Buďte opatrní, váš obrázek musí být pojmenován `logo` a musí být ve formátu `.webp`. Celý název souboru by tedy měl být: `logo.webp`: ![podcast](assets/29.webp)
- Vraťte se do vaší složky `assets` a klikněte na mezi soubor `.gitkeep`: ![podcast](assets/30.webp)
- Jakmile jste na souboru, klikněte na tři malé tečky v pravém horním rohu a poté na `Delete file`: ![podcast](assets/31.webp)
- Ověřte, že jste stále na stejné pracovní větvi, poté klikněte na tlačítko `Commit changes`: ![podcast](assets/32.webp)
- Přidejte název a popis k vašemu commitu, poté klikněte na `Commit changes`: ![podcast](assets/33.webp)
- Vraťte se na kořen vašeho repozitáře: ![podcast](assets/34.webp)
- Měli byste vidět zprávu, která indikuje, že vaše větev prošla změnami. Klikněte na tlačítko `Compare & pull request`: ![podcast](assets/35.webp)
- Přidejte jasný název a popis k vašemu PR: ![podcast](assets/36.webp)
- Klikněte na tlačítko `Create pull request`: ![podcast](assets/37.webp)
Gratulujeme! Vaše PR bylo úspěšně vytvořeno. Administrátor to nyní zkontroluje a pokud je vše v pořádku, sloučí to do hlavního repozitáře PlanB Network. Na webu byste měli vidět svůj podcast několik dní poté.

Ujistěte se, že sledujete průběh vašeho PR. Administrátor vám může zanechat komentář s žádostí o dodatečné informace. Dokud vaše PR není validováno, můžete ho zobrazit na kartě `Pull requests` na GitHub repozitáři PlanB Network: ![podcast](assets/38.webp)
Moc vám děkujeme za vaši cennou příspěvek! :)
