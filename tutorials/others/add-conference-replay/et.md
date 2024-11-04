---
name: Konverentsi Korduse Lisamine
description: Kuidas lisada konverentsi kordust PlanB võrgustikus?
---
![konverents](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja hostitud GitHub'is, võimaldades kellel tahes panustada platvormi rikastamisse.

Kas soovite lisada oma Bitcoin'i konverentsi korduse PlanB võrgustiku saidile ja anda sellele üritusele nähtavust, kuid ei tea, kuidas? See õpetus on teile!

Kui aga soovite lisada tulevikus toimuva konverentsi, soovitan teil [lugeda seda teist õpetust](https://planb.network/tutorials/others/add-event), milles selgitame, kuidas saidile uut üritust lisada.
![konverents](assets/01.webp)
- Esiteks peate omama kontot GitHub'is. Kui te ei tea, kuidas kontot luua, oleme teinud [üksikasjaliku õpetuse, mis juhendab teid](https://planb.network/tutorials/others/create-github-account).
- Minge [PlanB-le pühendatud GitHub'i andmerepositooriumisse](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) jaotisesse `resources/conference/`:
![konverents](assets/02.webp)
- Klõpsake paremal üleval nupul `Add file`, seejärel `Create new file`:
![konverents](assets/03.webp)
- Kui te pole varem PlanB võrgustiku sisule kaasa aidanud, peate looma oma haru (fork) algsest repositooriumist. Repositooriumi haru loomine tähendab selle repositooriumi koopia loomist oma GitHub'i kontole, mis võimaldab teil projekti kallal töötada, mõjutamata algset repositooriumi. Klõpsake nupul `Fork this repository`:
![konverents](assets/04.webp)
- Seejärel jõuate GitHub'i redigeerimislehele:
![konverents](assets/05.webp)
- Looge oma konverentsi jaoks kaust. Selleks kirjutage kasti `Name your file...` oma konverentsi nimi väiketähtedega ja tühikute asemel sidekriipsudega. Näiteks, kui teie konverentsi nimi on "Paris Bitcoin Conference", peaksite märkima `paris-bitcoin-conference`. Lisage ka oma konverentsi aasta, näiteks: `paris-bitcoin-conference-2024`:
![konverents](assets/06.webp)
- Kausta loomise kinnitamiseks lihtsalt märkige sama kasti järel oma nime järel kaldkriips, näiteks: `paris-bitcoin-conference-2024/`. Kaldkriipsu lisamine loob automaatselt kausta, mitte faili:
![konverents](assets/07.webp)
- Selles kaustas loote esimese YAML-faili nimega `conference.yml`:
![konverents](assets/08.webp)
Täitke see fail oma konverentsi kohta käiva teabega, kasutades seda malli:
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

Näiteks võiks teie YAML-fail välja näha selline:

```yaml
year: 2024-08
name: Pariisi Bitcoin Konverents 2024
builder: Pariisi Bitcoin Konverents
location: Pariis, Prantsusmaa
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - Rahvusvaheline
  - Kõik Publikud
```

![konverents](assets/09.webp)
Kui teie organisatsioonil ei ole veel "*builder*" identifikaatorit, saate selle lisada [järgides seda teist õpetust](https://planb.network/tutorials/others/add-builder).
- Kui olete selle faili muutmisega lõpetanud, salvestage muudatused, klõpsates nupul `Commit changes...`:
![konverents](assets/10.webp)
- Lisage oma muudatustele pealkiri, samuti lühike description:
![konverents](assets/11.webp)
- Klõpsake rohelisel nupul `Propose changes`:
![konverents](assets/12.webp)
- Seejärel jõuate lehele, mis võtab kokku kõik teie muudatused:
![konverents](assets/13.webp)
- Klõpsake üleval paremal oma GitHubi profiilipildil, seejärel valige `Your Repositories`:
![konverents](assets/14.webp)
- Valige oma PlanB Networki repositooriumi fork:
![konverents](assets/15.webp)
- Peaksite akna ülaosas nägema teavitust oma uue haru kohta. See on tõenäoliselt nimetatud `patch-1`. Klõpsake sellel:
![konverents](assets/16.webp)
- Nüüd olete oma tööharul:
![konverents](assets/17.webp)
- Minge tagasi kausta `resources/conference/` ja valige konverentsi kaust, mille just eelmises commit'is lõite:
![konverents](assets/18.webp)
- Oma konverentsi kaustas klõpsake nupul `Add file`, seejärel valige `Create new file`:
![konverents](assets/19.webp)
- Nimetage see uus kaust `assets` ja kinnitage selle loomine, lisades lõppu kaldkriipsu `/`:
![konverents](assets/20.webp)
- Selles `assets` kaustas looge fail nimega `.gitkeep`:
![konverents](assets/21.webp)
- Klõpsake nupul `Commit changes...`:
![konverents](assets/22.webp)
- Jätke commit'i pealkiri vaikimisi ja veenduge, et ruut `Commit directly to the patch-1 branch` oleks märgitud, seejärel klõpsake `Commit changes`:
![konverents](assets/23.webp)
- Minge tagasi `assets` kausta:
![konverents](assets/24.webp)
- Klõpsake nupul `Add file`, seejärel valige `Upload files`:
![konverents](assets/25.webp)
- Avaneb uus leht. Lohistage ja kukutage pilt, mis esindab teie konverentsi ja mida kuvatakse PlanB Networki saidil: ![konverents](assets/26.webp)
- See võib olla logo, pisipilt või isegi poster:
![konverents](assets/27.webp)
- Kui pilt on üles laaditud, kontrollige, et ruut `Commit directly to the patch-1 branch` oleks märgitud, seejärel klõpsake `Commit changes`:
![konverents](assets/28.webp)
- Olge ettevaatlik, teie pilt peab olema nimetatud `thumbnail` ja peab olema `.webp` formaadis. Täielik failinimi peaks seega olema: `thumbnail.webp`:
![konverents](assets/29.webp)
- Minge tagasi oma `assets` kausta ja klõpsake vahendajafailil `.gitkeep`:
![konverents](assets/30.webp)
- Faili juures olles klõpsake paremas ülanurgas kolmel väikesel punktil ja seejärel valige `Delete file`:
![konverents](assets/31.webp)
- Veenduge, et olete endiselt samal tööharul, seejärel klõpsake nupul `Commit changes`:
![konverents](assets/32.webp)
- Lisage oma commit'ile pealkiri ja kirjeldus, seejärel klõpsake `Commit changes`:
![konverents](assets/33.webp)
- Minge tagasi oma konverentsi kausta: ![konverents](assets/34.webp)
- Klõpsake nuppu `Add file`, seejärel `Create new file`:
![konverents](assets/35.webp)
- Looge uus markdown (.md) fail, nimetades selle oma emakeele tähisega. Seda faili kasutatakse teie konverentsi korduste jaoks. Näiteks, kui tahan kirjutada konverentside kirjeldusi inglise keeles, nimetan selle faili en.md:
![konverents](assets/36.webp)
- Täitke see markdown fail kasutades järgnevat malli, mida saate kohandada vastavalt oma konverentsi seadistusele:

```markdown
---
name: Pariisi Bitcoin Konverents 2024
description: Suurim Bitcoin konverents Prantsusmaal, kus igal aastal osaleb üle 8,000 osaleja!
--- 

# Pealava

## Reede hommik

![video](https://youtu.be/XXXXXXXXXXXX)

## Reede pärastlõuna

![video](https://youtu.be/XXXXXXXXXXXX)

## Laupäev hommik

![video](https://youtu.be/XXXXXXXXXXXX)

## Laupäev pärastlõuna

![video](https://youtu.be/XXXXXXXXXXXX)

# Töötuba

## Bitcoini kaevandamise tulevik: Väljakutsed ja uuendused

![video](https://youtu.be/XXXXXXXXXXXX)

Esineja: Satoshi Nakamoto, Satoshi Nakamoto

## Kas privaatsus on Bitcoinil veel võimalik?

![video](https://youtu.be/XXXXXXXXXXXX)

Esineja: Satoshi Nakamoto

## Bitcoin Core: Süvitsi läbi koodibaasi

![video](https://youtu.be/XXXXXXXXXXXX)

Esineja: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Bitcoini rahakottide ehitamine ja turvamine Miniscriptiga

![video](https://youtu.be/XXXXXXXXXXXX)

Esineja: Satoshi Nakamoto
```

![konverents](assets/37.webp)
- Dokumendi alguses, "front matter" osas, täitke `name:` väli teie konverentsi nime ja korduste aastaga. `description:` väljal kirjutage oma sündmuse lühikirjeldus faili keeles. Näiteks faili `en.md` puhul peaks kirjeldus olema inglise keeles. PlanB Network meeskond hoolitseb teie kirjelduse tõlkimise eest kasutades nende mudelit.
- Esimese taseme pealkirjad, mida tähistatakse `#`-ga, kasutatakse konverentsi stseenide kaupa korraldamiseks. Näiteks `# Pealava` pealava jaoks ja `# Töötuba` töötubadele pühendatud lava jaoks.

- Teise taseme pealkirjad, mida tähistatakse kahekordse `##`-ga, kasutatakse erinevate kordusvideote eraldamiseks. Kui konverentse filmiti pidevalt pool päeva, näidake näiteks `## Reede hommik`. Kui konverentse filmiti ja edastati individuaalselt, nimetage konverents otse teise taseme pealkirjaga.

- Iga teise taseme pealkirja alla sisestage vastava kordusvideo link. Süntaks peaks olema: `![video](https://youtu.be/XXXXXXXXXXXX)`, asendades `XXXXXXXXXXXX` tegeliku video lingiga.

- Kui formaat seda võimaldab (individuaalsed konverentsid), võite lisada esinejate nimed. Selleks lisage video lingi alla `Speaker:` väli, millele järgneb esineja nimi või pseudonüüm. Mitme esineja puhul eraldage iga nimi komaga, näiteks nii: `Esineja: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Kui olete selle faili muudatustega valmis, salvestage need klõpsates nupul `Commit changes...`:
![konverents](assets/38.webp)
- Lisage oma muudatustele pealkiri, samuti lühidescription:
![konverents](assets/39.webp)
- Klõpsake nupul `Commit changes`: ![konverents](assets/40.webp)
- Teie konverentsi kaust peaks nüüd välja nägema selline:
![konverents](assets/41.webp)
- Kui kõik on teie rahuloluks, naaske oma kahvli juurkausta:
![konverents](assets/42.webp)
- Peaksite nägema sõnumit, mis näitab, et teie haru on läbinud muudatusi. Klõpsake nupul `Compare & pull request`:
![konverents](assets/43.webp)
- Lisage oma PR-ile selge pealkiri ja description:
![konverents](assets/44.webp)
- Klõpsake nupul `Create pull request`:
![konverents](assets/45.webp)
Palju õnne! Teie PR on edukalt loodud. Administraator vaatab selle nüüd üle ja, kui kõik on korras, ühendab selle PlanB Networki peamisse repositooriumisse. Mõne päeva pärast peaksid teie konverentsi kordused ilmuma veebisaidile.

Palun jälgige oma PR-i edenemist. On võimalik, et administraator võib jätta kommentaari, paludes lisateavet. Niikaua kui teie PR ei ole kinnitatud, saate seda vaadata PlanB Networki GitHubi repositooriumi vahekaardil `Pull requests`:
![konverents](assets/46.webp)

Suur tänu teie väärtusliku panuse eest! :)
