---
nimi: Lisa sündmus PlanB võrgustikku
kirjeldus: Kuidas ma saan ettepaneku teha uue sündmuse lisamiseks PlanB võrgustikku?
---
![sündmus](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja majutatud GitHubis, pakkudes kõigile võimalust panustada platvormi rikastamisse.

Kui soovite PlanB võrgustiku saidile lisada Bitcoin'i konverentsi, et suurendada oma sündmuse nähtavust, kuid ei tea, kuidas? See õpetus on teile!
![sündmus](assets/01.webp)
- Esiteks peate omama kontot GitHubis. Kui te ei tea, kuidas kontot luua, oleme teinud üksikasjaliku õpetuse, mis juhendab teid.

https://planb.network/tutorials/others/create-github-account

- Minge [PlanB-le pühendatud GitHubi repositooriumisse andmete jaoks](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/conference) jaotises `resources/conference/`:
![sündmus](assets/02.webp)
- Klõpsake paremal üleval nupul `Add file`, seejärel `Create new file`:
![sündmus](assets/03.webp)
- Kui te pole varem PlanB võrgustiku sisule kaasa aidanud, peate looma oma haru (fork) algsest repositooriumist. Repositooriumi haru loomine tähendab selle repositooriumi koopia loomist oma GitHubi kontole, mis võimaldab teil projekti kallal töötada ilma algset repositooriumit mõjutamata. Klõpsake nupul `Fork this repository`:
![sündmus](assets/04.webp)
- Seejärel jõuate GitHubi redigeerimislehele:
![sündmus](assets/05.webp)
- Looge oma konverentsi jaoks kaust. Selleks kirjutage kasti `Name your file...` oma konverentsi nimi väiketähtedega ja tühikute asemel sidekriipsudega. Näiteks, kui teie konverentsi nimi on "Paris Bitcoin Conference", peaksite märkima `paris-bitcoin-conference`. Lisage ka oma konverentsi aasta, näiteks: `paris-bitcoin-conference-2024`:
![sündmus](assets/06.webp)
- Kausta loomise kinnitamiseks lihtsalt märkige sama kasti järel kaldkriips, näiteks: `paris-bitcoin-conference-2024/`. Kaldkriipsu lisamine loob automaatselt kausta, mitte faili:
![sündmus](assets/07.webp)
- Selles kaustas loote esimese YAML-faili nimega `events.yml`:
![sündmus](assets/08.webp)
- Täitke see fail oma konverentsi kohta käiva infoga, kasutades seda malli:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  nimi:
  ehitaja:
  tüüp: konverents
  book_online: false
  book_in_person: false
  price_dollars: 0
  kirjeldus:
  keel: 
    - 
  lingid:
    veebileht:
    replay_url:    
    live_url :
  märksõnad: 
    - 
```

Näiteks võiks teie YAML-fail välja näha selline:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Pariis, Prantsusmaa
  address_line_2: 
  address_line_3: 
  nimi: Paris Bitcoin Conference 2024
  ehitaja: Paris Bitcoin Conference
  tüüp: konverents
  book_online: false
  book_in_person: false
  price_dollars: 0
```yaml
kirjeldus: Prantsusmaa suurim Bitcoin'i konverents, kus igal aastal osaleb üle 8000 osaleja!
keel:
    - fr
    - en
    - es
    - it
lingid:
    veebileht: https://paris.bitcoin.fr/conference
    kordus_url:
    otse_url:
sildid:
    - Bitcoiner
    - Üldine
    - Rahvusvaheline
```
![üritus](assets/09.webp)
Kui teie organisatsioonil ei ole veel "*builder*" identifikaatorit, saate selle lisada, järgides seda teist õpetust.

https://planb.network/tutorials/others/add-builder

- Kui olete selle faili muutmisega lõpetanud, salvestage need, klõpsates nupul `Commit changes...`:
![üritus](assets/10.webp)
- Lisage oma muudatustele pealkiri ja lühike kirjeldus:
![üritus](assets/11.webp)
- Klõpsake rohelisel nupul `Propose changes`:
![üritus](assets/12.webp)
- Seejärel jõuate lehele, mis kokkuvõtlikult kuvab kõik teie muudatused:
![üritus](assets/13.webp)
- Klõpsake üleval paremal oma GitHubi profiilipildil, seejärel valige `Your Repositories`:
![üritus](assets/14.webp)
- Valige oma PlanB Networki repositooriumi kahvel:
![üritus](assets/15.webp)
- Peaksite akna ülaosas nägema teavitust oma uue haruga. See on tõenäoliselt nimetatud `patch-1`. Klõpsake sellel:
![üritus](assets/16.webp)
- Nüüd olete oma tööharul:
![üritus](assets/17.webp)
- Minge tagasi kausta `resources/conference/` ja valige konverentsi kaust, mille just eelmises kohustuses lõite:
![üritus](assets/18.webp)
- Oma konverentsi kaustas klõpsake nupul `Add file`, seejärel valige `Create new file`:
![üritus](assets/19.webp)
- Nimetage see uus kaust `assets` ja kinnitage selle loomine, pannes lõppu kaldkriipsu `/`:
![üritus](assets/20.webp)
- Selles `assets` kaustas looge fail nimega `.gitkeep`:
![üritus](assets/21.webp)
- Klõpsake nupul `Commit changes...`:
![üritus](assets/22.webp)
- Jätke kohustuse pealkiri vaikimisi ja veenduge, et ruut `Commit directly to the patch-1 branch` oleks märgitud, seejärel klõpsake `Commit changes`:
![üritus](assets/23.webp)
- Pöörduge tagasi `assets` kausta:
![üritus](assets/24.webp)
- Klõpsake nupul `Add file`, seejärel valige `Upload files`: ![üritus](assets/25.webp)
- Avaneb uus leht. Lohistage ja kukutage pilt, mis esindab teie konverentsi ja kuvatakse PlanB Networki saidil:
![üritus](assets/26.webp)
- See võib olla logo, pisipilt või isegi plakat:
![üritus](assets/27.webp)
- Kui pilt on üles laaditud, kontrollige, et ruut `Commit directly to the patch-1 branch` oleks märgitud, seejärel klõpsake `Commit changes`:
![üritus](assets/28.webp)
- Olge ettevaatlik, teie pilt peab olema nimetatud `thumbnail` ja olema `.webp` formaadis. Täielik failinimi peaks seega olema: `thumbnail.webp`:
![üritus](assets/29.webp)
- Pöörduge tagasi oma `assets` kausta ja klõpsake vahefailil `.gitkeep`:
![üritus](assets/30.webp)
- Faili juures olles klõpsake üleval paremal asuvatel kolmel väikesel punktil ja seejärel valikul `Kustuta fail`: ![event](assets/31.webp)
- Kontrollige, et olete endiselt samal tööharul, seejärel klõpsake nupul `Commit changes` (Kinnita muudatused):
![event](assets/32.webp)
- Lisage oma commit'ile pealkiri ja kirjeldus, seejärel klõpsake nupul `Commit changes` (Kinnita muudatused):
![event](assets/33.webp)
- Minge tagasi oma repositooriumi juurkausta:
![event](assets/34.webp)
- Peaksite nägema teadet, mis näitab, et teie haru on läbinud muudatusi. Klõpsake nupul `Compare & pull request` (Võrdle ja esita tõmbetaotlus):
![event](assets/35.webp)
- Lisage oma PR-ile selge pealkiri ja kirjeldus:
![event](assets/36.webp)
- Klõpsake nupul `Create pull request` (Loo tõmbetaotlus):
![event](assets/37.webp)
Palju õnne! Teie tõmbetaotlus on edukalt loodud. Administraator kontrollib seda nüüd ja kui kõik on korras, ühendab ta selle PlanB Networki peamisse repositooriumisse. Teie sündmus peaks veebisaidil ilmuma mõne päeva pärast.

Jälgige kindlasti oma tõmbetaotluse edenemist. Administraator võib jätta kommentaari, paludes lisateavet. Niikaua kui teie tõmbetaotlus pole kinnitatud, saate seda vaadata PlanB Networki GitHubi repositooriumi vahekaardil `Pull requests` (Tõmbetaotlused):
![event](assets/38.webp)
Suur tänu teie väärtusliku panuse eest! :)