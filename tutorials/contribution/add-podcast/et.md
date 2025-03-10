---
name: Podcasti lisamine PlanB võrku
description: Kuidas lisada uut podcasti PlanB võrku?
---
![podcast](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja hostitud GitHubis, võimaldades kõigil platvormi rikastamises osaleda.

Kas soovite lisada oma Bitcoin podcasti PlanB võrgu saidile ja suurendada oma saate nähtavust, kuid ei tea, kuidas? See õpetus on teile!
![podcast](assets/01.webp)
- Esiteks peate omama GitHubi kontot. Kui te ei tea, kuidas seda luua, oleme koostanud [üksikasjaliku juhendi, mis aitab teid](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c).
- Minge [PlanB andmetele pühendatud GitHubi repositooriumisse](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) jaotisesse `resources/podcasts/`:
![podcast](assets/02.webp)
- Klõpsake paremal üleval nupul `Add file`, seejärel `Create new file`:
![podcast](assets/03.webp)
- Kui te pole varem PlanB võrgu sisusse panustanud, peate looma oma kahvli (fork) originaalrepositooriumist. Repositooriumi kahveldamine tähendab selle repositooriumi koopia loomist oma GitHubi kontole, mis võimaldab teil projekti kallal töötada ilma originaalrepositooriumit mõjutamata. Klõpsake nupul `Fork this repository`:
![podcast](assets/04.webp)
- Seejärel jõuate GitHubi redigeerimislehele:
![podcast](assets/05.webp)
- Looge oma podcasti jaoks kaust. Selleks kirjutage kasti `Name your file...` oma podcasti nimi väiketähtedega ja tühikute asemel sidekriipsudega. Näiteks, kui teie saade on nimetatud "Super Podcast Bitcoin", peaksite kirjutama `super-podcast-bitcoin`:
![podcast](assets/06.webp)
- Kausta loomise kinnitamiseks lisage lihtsalt oma podcasti nimele samas kastis pärast kaldkriipsu, näiteks: `super-podcast-bitcoin/`. Kaldkriipsu lisamine loob automaatselt kausta, mitte faili:
![podcast](assets/07.webp)
- Selles kaustas loote esimese YAML-faili nimega `podcast.yml`:
![podcast](assets/08.webp)
- Täitke see fail oma podcasti kohta käiva teabega, kasutades seda malli:

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

Siin on üksikasjad, mida iga välja jaoks täita:

- **`name`**: Määrake oma podcasti nimi.
- **`host`**: Loetlege saatejuhtide või podcasti juhtide nimed või pseudonüümid. Iga nimi tuleks eraldada komaga.
- **`language`**: Määrake oma podcastis räägitava keele kood. Näiteks inglise keele puhul märkige `en`, itaalia keele puhul `it`...

- **`links`**: Esitage oma sisu lingid. Teil on kaks võimalust:
	- `podcast`: link teie podcastile,
	- `twitter`: link podcasti või selle tootva organisatsiooni Twitteri profiilile,
	- `website`: link podcasti või selle tootva organisatsiooni veebisaidile.
```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin on tehniline OTSEÜLEKANNE, mis toimub kord nädalas Twitteris, et süveneda Bitcoin'i protokolli, teise kihi lahendustesse ja kõigesse, mis paneb pea ringi käima. Meie saatejuhid Lounes, Pantamis, Loïc ja Sosthene vastavad teie küsimustele ja pakuvad maailma kõige tehnilisemat saadet Bitcoin'i teemal.

tags:
  - bitcoin
  - tehnoloogia
contributors:
  - rabbit-hole
```

- Kui olete selle faili muudatustega lõpetanud, salvestage need, klõpsates nupul `Commit changes...`:
![podcast](assets/10.webp)
- Lisage oma muudatustele pealkiri, samuti lühidescription:
![podcast](assets/11.webp)
- Klõpsake rohelisel nupul `Propose changes`:
![podcast](assets/12.webp)
- Seejärel jõuate lehele, mis võtab kokku kõik teie muudatused:
![podcast](assets/13.webp)
- Klõpsake üleval paremal oma GitHubi profiilipildil, seejärel `Your Repositories`:
![podcast](assets/14.webp)
- Valige oma PlanB Network repositori forkk:
![podcast](assets/15.webp)
- Akna ülaosas peaksite nägema teadet oma uue haruga. See on tõenäoliselt nimetatud `patch-1`. Klõpsake sellel:
![podcast](assets/16.webp)
- Nüüd olete oma tööharus:
![podcast](assets/17.webp)
- Minge tagasi kausta `resources/podcast/` ja valige podcasti kaust, mille just eelmises kohustuses lõite: ![podcast](assets/18.webp)
- Oma podcasti kaustas klõpsake nupul `Add file`, seejärel `Create new file`:
![podcast](assets/19.webp)
- Nimetage see uus kaust `assets` ja kinnitage selle loomine, lisades lõppu kaldkriipsu `/`:
![podcast](assets/20.webp)
- Selles `assets` kaustas looge fail nimega `.gitkeep`:
![podcast](assets/21.webp)
- Klõpsake nupul `Commit changes...`:
![podcast](assets/22.webp)
- Jätke commit'i pealkiri vaikimisi, veenduge, et ruut `Commit directly to the patch-1 branch` oleks märgitud, seejärel klõpsake `Commit changes`:
![podcast](assets/23.webp)
- Tagasi `assets` kausta juurde:
![podcast](assets/24.webp)
- Klõpsake nupul `Add file`, seejärel `Upload files`:
![podcast](assets/25.webp)
- Avaneb uus leht. Lohista ja aseta oma podcasti logo alale. See pilt kuvatakse PlanB Networki saidil: ![podcast](assets/26.webp)
- Olge ettevaatlik, pilt peab olema ruudukujuline, et see sobiks meie veebisaidiga kõige paremini: ![podcast](assets/27.webp)
- Kui pilt on üles laaditud, kontrollige, et märkeruut `Commit directly to the patch-1 branch` oleks valitud, seejärel klõpsake nupul `Commit changes`: ![podcast](assets/28.webp)
- Olge ettevaatlik, teie pilt peab olema nimetatud `logo` ja peab olema `.webp` formaadis. Täielik failinimi peaks seega olema: `logo.webp`: ![podcast](assets/29.webp)
- Minge tagasi oma `assets` kausta ja klõpsake vahendusfailil `.gitkeep`: ![podcast](assets/30.webp)
- Faili juures olles klõpsake paremas ülanurgas kolmel väikesel punktil ja seejärel `Delete file`: ![podcast](assets/31.webp)
- Kontrollige, et olete endiselt samal tööharul, seejärel klõpsake nupul `Commit changes`: ![podcast](assets/32.webp)
- Lisage oma commit'ile pealkiri ja kirjeldus, seejärel klõpsake nupul `Commit changes`: ![podcast](assets/33.webp)
- Minge tagasi oma repositooriumi juurkausta: ![podcast](assets/34.webp)
- Peaksite nägema teadet, mis näitab, et teie haru on muudetud. Klõpsake nupul `Compare & pull request`: ![podcast](assets/35.webp)
- Lisage oma PR-ile selge pealkiri ja description: ![podcast](assets/36.webp)
- Klõpsake nupul `Create pull request`: ![podcast](assets/37.webp)
Palju õnne! Teie PR on edukalt loodud. Administraator vaatab selle nüüd üle ja kui kõik on korras, ühendab selle PlanB Networki peamisse repositooriumisse. Teie podcast peaks mõne päeva pärast veebisaidil ilmuma.

Palun jälgige oma PR-i edenemist. Administraator võib jätta kommentaari, paludes lisateavet. Niikaua kui teie PR ei ole kinnitatud, saate seda vaadata PlanB Networki GitHubi repositooriumi vahekaardil `Pull requests`: ![podcast](assets/38.webp)
Suur tänu teie väärtusliku panuse eest! :)
