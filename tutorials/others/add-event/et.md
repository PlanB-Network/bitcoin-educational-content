---
name: Lisa üritus PlanB võrgustikku
description: Kuidas ma saan soovitada uue ürituse lisamist PlanB võrgustikku?
---
![event](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja majutatud GitHubis, pakkudes kõigile võimalust panustada platvormi rikastamisse.

Kui soovite PlanB võrgustiku saidile lisada Bitcoin'i konverentsi, et suurendada oma ürituse nähtavust, kuid ei tea, kuidas? See õpetus on teile!
![event](assets/01.webp)
- Esiteks peate omama kontot GitHubis. Kui te ei tea, kuidas kontot luua, oleme teinud üksikasjaliku õpetuse, mis juhendab teid.

https://planb.network/tutorials/others/create-github-account


- Minge [PlanB-le pühendatud GitHubi andmerepositooriumisse](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) jaotisesse `resources/conference/`:
![event](assets/02.webp)
- Klõpsake paremal üleval nupul `Add file`, seejärel `Create new file`:
![event](assets/03.webp)
- Kui te pole varem PlanB võrgustiku sisule kaasa aidanud, peate looma oma haru (fork) algsest repositooriumist. Repositooriumi haru loomine tähendab selle repositooriumi koopia loomist oma GitHubi kontole, mis võimaldab teil projekti kallal töötada ilma algset repositooriumit mõjutamata. Klõpsake nupul `Fork this repository`:
![event](assets/04.webp)
- Seejärel jõuate GitHubi redigeerimislehele:
![event](assets/05.webp)
- Looge oma konverentsi jaoks kaust. Selleks kirjutage kasti `Name your file...` oma konverentsi nimi väiketähtedega ja tühikute asemel sidekriipsudega. Näiteks, kui teie konverentsi nimi on "Paris Bitcoin Conference", peaksite märkima `paris-bitcoin-conference`. Lisage ka oma konverentsi aasta, näiteks: `paris-bitcoin-conference-2024`:
![event](assets/06.webp)
- Kausta loomise kinnitamiseks lihtsalt märkige sama kasti pärast oma nime kaldkriips, näiteks: `paris-bitcoin-conference-2024/`. Kaldkriipsu lisamine loob automaatselt kausta, mitte faili:
![event](assets/07.webp)
- Selles kaustas loote esimese YAML-faili nimega `events.yml`:
![event](assets/08.webp)
- Täitke see fail oma konverentsi kohta käiva infoga, kasutades seda malli:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

Näiteks võiks teie YAML-fail välja näha selline:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Pariis, Prantsusmaa
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conference 2024
  builder: Paris Bitcoin Conference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
description: Prantsusmaa suurim Bitcoin'i konverents, kus igal aastal osaleb üle 8000 osaleja!
  keel:
    - fr
    - en
    - es
    - it
  lingid:
    veebileht: https://paris.bitcoin.fr/conference
    kordus_url:
    otse_url:
  märksõnad:
    - Bitcoiner
    - Üldine
    - Rahvusvaheline
```
![üritus](assets/09.webp)
Kui teie organisatsioonil ei ole veel "*builder*" identifikaatorit, saate selle lisada, järgides seda teist õpetust.

https://planb.network/tutorials/others/add-builder



- Kui olete selle faili muutmisega lõpetanud, salvestage need, klõpsates nupul `Commit changes...`:
![üritus](assets/10.webp)
- Lisage oma muudatustele pealkiri, samuti lühike description:
![üritus](assets/11.webp)
- Klõpsake rohelisel nupul `Propose changes`:
![üritus](assets/12.webp)
- Seejärel jõuate lehele, mis võtab kokku kõik teie muudatused:
![üritus](assets/13.webp)
- Klõpsake üleval paremal oma GitHubi profiilipildil, seejärel `Your Repositories`:
![üritus](assets/14.webp)
- Valige oma PlanB Networki repositooriumi fork:
![üritus](assets/15.webp)
- Peaksite akna ülaosas nägema teavitust oma uue haruga. See on tõenäoliselt nimetatud `patch-1`. Klõpsake sellel:
![üritus](assets/16.webp)
- Nüüd olete oma tööharul:
![üritus](assets/17.webp)
- Minge tagasi kausta `resources/conference/` ja valige konverentsi kaust, mille just eelmises commitis lõite:
![üritus](assets/18.webp)
- Oma konverentsi kaustas klõpsake nupul `Add file`, seejärel `Create new file`:
![üritus](assets/19.webp)
- Nimetage see uus kaust `assets` ja kinnitage selle loomine, pannes lõppu kaldkriipsu `/`:
![üritus](assets/20.webp)
- Selles `assets` kaustas looge fail nimega `.gitkeep`:
![üritus](assets/21.webp)
- Klõpsake nupul `Commit changes...`:
![üritus](assets/22.webp)
- Jätke commit'i pealkiri vaikimisi ja veenduge, et ruut `Commit directly to the patch-1 branch` oleks märgitud, seejärel klõpsake `Commit changes`:
![üritus](assets/23.webp)
- Pöörduge tagasi `assets` kausta:
![üritus](assets/24.webp)
- Klõpsake nupul `Add file`, seejärel `Upload files`: ![üritus](assets/25.webp)
- Avaneb uus leht. Lohistage ja kukutage pilt, mis esindab teie konverentsi ja kuvatakse PlanB Networki saidil:
![üritus](assets/26.webp)
- See võib olla logo, pisipilt või isegi plakat:
![üritus](assets/27.webp)
- Kui pilt on üles laaditud, kontrollige, et ruut `Commit directly to the patch-1 branch` oleks märgitud, seejärel klõpsake `Commit changes`:
![üritus](assets/28.webp)
- Olge ettevaatlik, teie pilt peab olema nimetatud `thumbnail` ja peab olema `.webp` formaadis. Täielik failinimi peaks seega olema: `thumbnail.webp`:
![üritus](assets/29.webp)
- Pöörduge tagasi oma `assets` kausta ja klõpsake vahefailil `.gitkeep`:
![üritus](assets/30.webp)
- Faili juures olles klõpsake paremas ülanurgas kolmel väikesel punktil ja seejärel valige `Kustuta fail`: ![event](assets/31.webp)
- Kontrollige, et te ikka viibite samal tööharul, seejärel klõpsake nupul `Commit changes` (Sisesta muudatused):
![event](assets/32.webp)
- Lisage oma commit'ile pealkiri ja kirjeldus, seejärel klõpsake nupul `Commit changes` (Sisesta muudatused):
![event](assets/33.webp)
- Minge tagasi oma repositooriumi juurkausta:
![event](assets/34.webp)
- Peaksite nägema teadet, mis näitab, et teie haru on läbinud muudatusi. Klõpsake nupul `Compare & pull request` (Võrdle ja esita tõmbetaotlus):
![event](assets/35.webp)
- Lisage oma PR-ile selge pealkiri ja description:
![event](assets/36.webp)
- Klõpsake nupul `Create pull request` (Loo tõmbetaotlus):
![event](assets/37.webp)
Palju õnne! Teie tõmbetaotlus on edukalt loodud. Administraator vaatab selle nüüd üle ja kui kõik on korras, ühendab ta selle PlanB Networki peamisse repositooriumisse. Teie sündmus peaks mõne päeva pärast veebisaidil ilmuma.

Jälgige kindlasti oma PR-i edenemist. Administraator võib jätta kommentaari, paludes lisateavet. Niikaua kui teie PR ei ole kinnitatud, saate seda vaadata PlanB Networki GitHubi repositooriumi vahekaardil `Pull requests` (Tõmbetaotlused):
![event](assets/38.webp)
Suur tänu teie väärtusliku panuse eest! :)
