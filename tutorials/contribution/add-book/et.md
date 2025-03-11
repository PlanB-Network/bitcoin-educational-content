---
name: Raamatu lisamine PlanB võrgustikku
description: Kuidas lisada uut raamatut PlanB võrgustikku?
---
![raamat](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja majutatud GitHub'is, võimaldades kõigil platvormi rikastamisele kaasa aidata.

**Kas soovite lisada PlanB võrgustiku saidile Bitcoin'iga seotud raamatu ja suurendada oma töö nähtavust, kuid ei tea, kuidas? See õpetus on teile!**
![raamat](assets/01.webp)
- Esiteks peate omama GitHub'i kontot. Kui te ei tea, kuidas kontot luua, oleme koostanud [üksikasjaliku õpetuse, mis juhendab teid](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c).
- Minge [PlanB-le pühendatud GitHub'i andmerepositooriumisse](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) jaotisesse `resources/books/`:
![raamat](assets/02.webp)
- Klõpsake paremal üleval nupul `Add file`, seejärel `Create new file`:
![raamat](assets/03.webp)
- Kui te pole varem PlanB võrgustiku sisule kaasa aidanud, peate looma oma haru (fork) algsest repositooriumist. Repositooriumi haru loomine tähendab selle repositooriumi koopia loomist oma GitHub'i kontole, võimaldades teil projekti kallal töötada ilma algset repositooriumit mõjutamata. Klõpsake nupul `Fork this repository`:
![raamat](assets/04.webp)
- Seejärel jõuate GitHub'i redigeerimislehele:
![raamat](assets/05.webp)
- Looge oma raamatu jaoks kaust. Selleks kirjutage kasti `Name your file...` oma raamatu nimi väiketähtedega ja tühikute asemel sidekriipsudega. Näiteks, kui teie raamatu nimi on "*Minu Bitcoin Raamat*", peaksite märkima `minu-bitcoin-raamat`:
![raamat](assets/06.webp)
- Kausta loomise kinnitamiseks lisage lihtsalt oma raamatu nimele samas kastis kaldkriips, näiteks: `minu-bitcoin-raamat/`. Kaldkriipsu lisamine loob automaatselt kausta, mitte faili:
![raamat](assets/07.webp)
- Selles kaustas loote esimese YAML-faili nimega `book.yml`:
![raamat](assets/08.webp)
- Täitke see fail oma raamatu kohta käiva teabega, kasutades seda malli:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Siin on väljade täitmiseks üksikasjad:
- **`author`**: Märgi raamatu autori nimi.
- **`level`**: Märgi nõutav tase, et raamatut hästi lugeda ja mõista. Vali tase järgmiste hulgast:
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: Lisa kaks või kolm raamatuga seotud märksõna. Näiteks:
    - `bitcoin`
    - `ajalugu`
    - `tehnoloogia`
    - `majandus`
    - `haridus`...

Näiteks võiks teie YAML-fail välja näha selline:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![raamat](assets/09.webp)
- Kui olete selle faili muudatustega lõpetanud, salvestage need klõpsates nupul `Commit changes...`:
![raamat](assets/10.webp)
- Lisa oma muudatustele pealkiri ja lühidescription: ![raamat](assets/11.webp)
- Klõpsa rohelisel nupul `Esita muudatused`: ![raamat](assets/12.webp)
- Seejärel jõuad lehele, mis kokkuvõtlikult kuvab kõik sinu muudatused: ![raamat](assets/13.webp)
- Klõpsa üleval paremal oma GitHubi profiilipildil, seejärel vali `Sinu Repositooriumid`: ![raamat](assets/14.webp)
- Vali oma PlanB Network repositoriooni fork: ![raamat](assets/15.webp)
- Akna ülaosas peaksid nägema teadet oma uue haru kohta. See on tõenäoliselt nimetatud `patch-1`. Klõpsa sellel: ![raamat](assets/16.webp)
- Nüüd oled oma tööharul: ![raamat](assets/17.webp)
- Mine tagasi kausta `resources/books/` ja vali kaust oma raamatuga, mille just eelmises kohustuses lõid: ![raamat](assets/18.webp)
- Oma raamatu kaustas klõpsa nupul `Lisa fail`, seejärel vali `Loo uus fail`: ![raamat](assets/19.webp)
- Nimeta see uus kaust `assets` ja kinnita selle loomine, lisades lõppu kaldkriipsu `/`: ![raamat](assets/20.webp)
- Selles `assets` kaustas loo fail nimega `.gitkeep`: ![raamat](assets/21.webp)
- Klõpsa nupul `Esita muudatused...`: ![raamat](assets/22.webp)
- Jäta kohustuse pealkiri vaikimisi ja veendu, et ruut `Esita otse patch-1 harusse` on märgitud, seejärel klõpsa `Esita muudatused`: ![raamat](assets/23.webp)
- Mine tagasi `assets` kausta: ![raamat](assets/24.webp)
- Klõpsa nupul `Lisa fail`, seejärel `Laadi üles failid`: ![raamat](assets/25.webp)
- Avaneb uus leht. Lohista ja kukuta oma raamatu kaanepilt alasse. See pilt kuvatakse PlanB Network saidil: ![raamat](assets/26.webp)
- Ole ettevaatlik, pilt peab olema raamatu formaadis, et see sobiks meie veebisaidile kõige paremini, näiteks: ![raamat](assets/27.webp)
- Kui pilt on üles laaditud, veendu, et ruut `Esita otse patch-1 harusse` on märgitud, seejärel klõpsa `Esita muudatused`: ![raamat](assets/28.webp)- Pane tähele, et sinu pilt peab olema nimetatud `cover_en`, kui kaas on inglise keeles ja peab olema `.webp` formaadis. Seega peaks täielik failinimi olema `cover_en.webp`, `cover_fr.webp`, `cover_it.webp` jne. Kui soovid kasutada iga keele jaoks erinevat kaanepilti, näiteks raamatu tõlke puhul, võid need paigutada samasse kohta `assets` kaustas: ![raamat](assets/29.webp)
- Mine tagasi oma `assets` kausta ja klõpsa vahendajafailil `.gitkeep`: ![raamat](assets/30.webp)
- Faili juures olles klõpsa üleval paremal kolmel väikesel täpil ja seejärel `Kustuta fail`: ![raamat](assets/31.webp)
- Veendu, et oled endiselt samal tööharul, seejärel klõpsa nupul `Esita muudatused...`: ![raamat](assets/32.webp)
- Lisa oma kohustusele pealkiri ja kirjeldus, seejärel klõpsa `Esita muudatused`: ![raamat](assets/33.webp)
- Naaske oma raamatu kausta: ![book](assets/34.webp)
- Klõpsake nupul `Add file`, seejärel valige `Create new file`:
![book](assets/35.webp)
- Looge uus YAML-fail, nimetades selle raamatu keeleindikaatori järgi. Seda faili kasutatakse raamatu kirjelduse jaoks. Näiteks, kui tahan oma kirjeldust kirjutada inglise keeles, nimetan selle faili `en.yml`:
![book](assets/36.webp)
- Täitke see YAML-fail järgneva malli abil:
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Siin on väljade täitmiseks vajalikud detailid:
- **`title`**: Määrake raamatu nimi jutumärkides.
- **`publication_year`**: Määrake raamatu avaldamise aasta.
- **`cover`**: Määrake faili nimi, mis vastab kaanepildile, vastavalt YAML-faili keelele, mida te praegu muudate. Näiteks, kui muudate `en.yml` faili ja olete varem lisanud ingliskeelse kaanepildi pealkirjaga `cover_en.webp`, lihtsalt märkige see väljal `cover_en.webp`.
- **`description`**: Lisage lühike lõik, mis kirjeldab raamatut. Kirjeldus peab olema samas keeles, mis on märgitud YAML-faili pealkirjas.
- **`contributors`**: Lisage oma kaastöötaja ID, kui teil on üks.

Näiteks võib teie YAML-fail välja näha selline:

```yaml
title: "Minu Bitcoin Raamat"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Avastage Bitcoin'i murranguline maailm selle kõikehõlmava juhendiga algajatele. Minu Bitcoin Raamat dešifreerib Bitcoin'i keerukused, pakkudes selget ja lühikest sissejuhatust, kuidas protokoll töötab. Alates selle revolutsioonilisest tehnoloogiast kuni selle potentsiaalse mõjuni maailmamajandusele, pakub see raamat hindamatuid teadmisi ja praktilisi teadmisi. Ideaalne neile, kes on Bitcoin'iga uued, katab see alused, turvanõuanded ja digitaalse finantseerimise tuleviku. Sukelduge raha tulevikku ja varustage end teadmistega, et enesekindlalt navigeerida digiajastul.

contributors:
  - pretty-private

![book](assets/37.webp)
- Klõpsake nupul `Commit changes...`:
![book](assets/38.webp)
- Veenduge, et ruut `Commit directly to the patch-1 branch` oleks märgitud, lisage pealkiri, seejärel klõpsake nupul `Commit changes`:
![book](assets/39.webp)
- Raamatu kaust peaks nüüd välja nägema selline:
![book](assets/40.webp)
- Kui kõik tundub teile korras, naaske oma kahvli juurkausta:
![book](assets/41.webp)
- Peaksite nägema sõnumit, mis näitab, et teie haru on muudetud. Klõpsake nupul `Compare & pull request`:
![book](assets/42.webp)
- Lisage selge pealkiri ja kirjeldus oma PR-ile:
![book](assets/43.webp)
- Klõpsake nupul `Create pull request`:
![book](assets/44.webp)
Palju õnne! Teie PR on edukalt loodud. Administraator vaatab selle nüüd üle ja kui kõik on korras, ühendab selle PlanB Network'i peamisse repositooriumisse. Teie raamat peaks veebisaidil ilmuma mõne päeva pärast.

Jälgige kindlasti oma PR-i edenemist. Administraator võib jätta kommentaari, paludes lisateavet. Niikaua kui teie PR pole kinnitatud, saate seda vaadata PlanB Network'i GitHubi repositooriumi `Pull requests` vahekaardil.
![book](assets/45.webp) Suur tänu teie väärtusliku panuse eest! :)
