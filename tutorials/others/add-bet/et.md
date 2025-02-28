---
name: Hariduslike Vahendite Lisamine
description: Kuidas lisada uusi õppematerjale PlanB võrgustikku?
---
![sündmus](assets/cover.webp)

PlanB missiooniks on pakkuda juhtivaid haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja majutatud GitHub'is, mis võimaldab kõigil platvormi rikastamises osaleda.

Lisaks õpetustele ja koolitustele pakub PlanB võrgustik ka laia valikut erinevat hariduslikku sisu Bitcoin'i kohta, mis on kõigile kättesaadav [BET (_Bitcoin Educational Toolkit_) sektsioonis](https://planb.network/resources/bet). See andmebaas sisaldab hariduslikke plakateid, meeme, humoorikaid propagandaplakateid, tehnilisi diagramme, logosid ja muid tööriistu kasutajatele. Selle algatuse eesmärk on toetada üksikisikuid ja kogukondi üle maailma Bitcoin'i õpetamisel, pakkudes neile vajalikke visuaalseid ressursse.

Kas soovite osaleda selle andmebaasi rikastamises, kuid ei tea, kuidas? See õpetus on teile!

*On hädavajalik, et kõik saidile integreeritud sisu oleks vaba õigustest või austaks lähtefaili litsentsi. Samuti on kõik PlanB võrgustikus avaldatud visuaalid kättesaadavad [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) litsentsi alusel.*
![sündmus](assets/01.webp)
- Esiteks, teil peab olema konto GitHub'is. Kui te ei tea, kuidas kontot luua, oleme teinud [üksikasjaliku õpetuse, mis juhendab teid](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c).
- Minge [PlanB-le pühendatud GitHubi repositooriumisse andmete jaoks](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) `resources/bet/` sektsioonis:
![sündmus](assets/02.webp)
- Klõpsake paremal üleval nupul `Add file`, seejärel `Create new file`:
![sündmus](assets/03.webp)
- Kui te pole varem PlanB võrgustiku sisule kaasa aidanud, peate looma oma haru (fork) originaalrepositooriumist. Repositooriumi haru loomine tähendab selle repositooriumi koopia loomist oma GitHubi kontole, mis võimaldab teil projekti kallal töötada ilma originaalrepositooriumit mõjutamata. Klõpsake nupul `Fork this repository`:
![sündmus](assets/04.webp)
- Seejärel jõuate GitHubi redigeerimislehele:
![sündmus](assets/05.webp)
- Looge oma sisu jaoks kaust. Selleks kirjutage `Name your file...` kasti oma sisu nimi väiketähtedega ja tühikute asemel sidekriipsudega. Minu näites, kui soovin lisada PDF-visuaali 2048-sõnalise BIP39 nimekirjaga, nimetan oma kausta `bip39-wordlist`: ![sündmus](assets/06.webp)
- Kausta loomise kinnitamiseks lisage lihtsalt nimele samas kastis kaldkriips, näiteks: `bip39-wordlist/`. Kaldkriipsu lisamine loob automaatselt kausta, mitte faili:
![sündmus](assets/07.webp)
- Selles kaustas loote esimese YAML-faili nimega `bet.yml`:
![sündmus](assets/08.webp)
- Täitke see fail oma sisuga seotud teabega, kasutades seda malli:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - et: 
tags:
  - 
  - 
contributors:
  - 
```

Siin on üksikasjad, mida iga välja jaoks täita:
```yaml
builder: Näita oma organisatsiooni identifikaatorit PlanB võrgustikus. Kui teie ettevõttel ei ole veel "builder" identifikaatorit, saate selle luua [selle õpetuse järgi](https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d). Kui teil seda veel ei ole, võite lihtsalt kasutada oma nime, pseudonüümi või ettevõtte nime ilma builder profiili loomata.
type: Valige oma sisu tüüp järgmiste kahe võimaluse hulgast:
	- `Educational Content` haridusliku sisu jaoks.
	- `Visual Content` muud tüüpi mitmekesise sisu jaoks.

links: Esitage oma sisu lingid. Teil on kaks võimalust:
	- Kui otsustate oma sisu otse PlanB GitHub'is majutada, peate järgnevate sammude käigus lisama lingid sellesse faili.
	- Kui teie sisu on majutatud mujal, nagu teie isiklikul veebilehel, märkige vastavad lingid siin:
	    - `download`: Link oma sisu allalaadimiseks.
	    - `view`: Link oma sisu vaatamiseks (võib olla sama mis allalaadimislink). Kui teie sisu on saadaval mitmes keeles, lisage iga keele jaoks link.

tags: Lisage oma sisuga seotud kaks märksõna. Näited:
	- bitcoin
	- tehnoloogia
	- majandus
	- haridus
	- meme...

contributors: Mainige oma kaastöötaja identifikaatorit, kui teil on üks.

Näiteks võiks teie YAML fail välja näha selline:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- Minu näites jätan lingid esialgu tühjaks, kuna lisan oma PDF-i otse GitHub'ile:
![event](assets/09.webp)
- Kui olete selle faili muudatustega valmis, salvestage need, klõpsates nupul `Commit changes...`:
![event](assets/10.webp)
- Lisage oma muudatustele pealkiri ja lühike description:
![event](assets/11.webp)
- Klõpsake rohelisel nupul `Propose changes`:
![event](assets/12.webp)
- Seejärel jõuate lehele, mis võtab kokku kõik teie muudatused:
![event](assets/13.webp)
- Klõpsake üleval paremal oma GitHubi profiilipildil, seejärel `Your Repositories`:
![event](assets/14.webp)
- Valige oma PlanB Networki repositooriumi fork:
![event](assets/15.webp)
- Peaksite akna ülaosas nägema teavitust oma uue haruga. See on tõenäoliselt nimetatud `patch-1`. Klõpsake sellel:
![event](assets/16.webp)
- Nüüd olete oma tööharul (**veenduge, et olete samal harul kui teie eelmised muudatused, see on oluline!**):
![event](assets/17.webp)
- Minge tagasi kausta `resources/bet/` ja valige kaust, mille oma eelmise kohustusega just lõite:
![event](assets/18.webp)
- Oma sisu kaustas klõpsake nupul `Add file`, seejärel `Create new file`:
![event](assets/19.webp)
- Nimetage see uus kaust `assets` ja kinnitage selle loomine, pannes lõppu kaldkriipsu `/`:
![event](assets/20.webp)
- Selles `assets` kaustas looge fail nimega `.gitkeep`: ![event](assets/21.webp)
```
- Klõpsake nupul `Commit changes...`: ![event](assets/22.webp)- Jätke commit'i pealkiri vaikimisi seadistusele ja veenduge, et `Commit directly to the patch-1 branch` kast on märgitud, seejärel klõpsake `Commit changes`: ![event](assets/23.webp)
- Pöörduge tagasi `assets` kausta: ![event](assets/24.webp)
- Klõpsake nupul `Add file`, seejärel `Upload files`: ![event](assets/25.webp)
- Avaneb uus leht. Lohistage sisu esindav pisipilt alasse. See pilt kuvatakse PlanB Network saidil: ![event](assets/26.webp)
- See võib olla eelvaade, logo või ikoon: ![event](assets/27.webp)
- Kui pilt on üles laaditud, veenduge, et `Commit directly to the patch-1 branch` kast on märgitud, seejärel klõpsake `Commit changes`: ![event](assets/28.webp)
- Olge ettevaatlik, teie pilt peab olema nimetatud `logo` ja peab olema `.webp` formaadis. Täielik failinimi peaks seega olema: `logo.webp`: ![event](assets/29.webp)
- Pöörduge tagasi oma `assets` kausta ja klõpsake vahendajafailil `.gitkeep`: ![event](assets/30.webp)
- Faili avamisel klõpsake paremas ülanurgas asuvatel kolmel väikesel punktil ja seejärel `Delete file`: ![event](assets/31.webp)
- Veenduge, et olete endiselt samal tööharul, seejärel klõpsake nupul `Commit changes`: ![event](assets/32.webp)
- Lisage oma commit'ile pealkiri ja kirjeldus, seejärel klõpsake `Commit changes`: ![event](assets/33.webp)
- Pöörduge tagasi oma sisu kausta: ![event](assets/34.webp)
- Klõpsake nupul `Add file`, seejärel `Create new file`: ![event](assets/35.webp)
- Looge uus YAML fail, nimetades selle oma emakeele indikaatoriga. Seda faili kasutatakse sisu kirjelduse jaoks. Näiteks, kui tahan kirjeldust kirjutada inglise keeles, nimetan selle faili `en.yml`: ![event](assets/36.webp)
- Täitke see YAML fail kasutades järgnevat malli:

```yaml
name: 
description: |
  
```

- `name` võtme jaoks võite lisada oma sisu nime;
- `description` võtme jaoks peate lihtsalt lisama lühikese lõigu, mis kirjeldab teie sisu. Kirjeldus peab olema sama keeles, mis faili nimi. Te ei pea seda kirjeldust tõlkima kõikidesse saidi toetatud keeltesse, kuna PlanB meeskonnad teevad seda oma mudeli abil.
Näiteks, siin on, kuidas teie fail võib välja näha:

```yaml
name: BIP39 WORDLIST
description: |
  Täielik ja nummerdatud nimekiri 2048 inglise sõnast BIP39 sõnastikust, mida kasutatakse mnemooniliste fraaside kodeerimiseks. Dokumenti saab printida ühele lehele.
```

![event](assets/37.webp)
- Klõpsake nupul `Commit changes...`:
![event](assets/38.webp)
- Veenduge, et `Commit directly to the patch-1 branch` kast on märgitud, lisage pealkiri, seejärel klõpsake `Commit changes`:
![event](assets/39.webp)
- Teie sisu kaust peaks nüüd välja nägema selline:
![event](assets/40.webp)
*Kui eelistate mitte lisada sisu GitHub'ile ja olete juba eelmistes etappides `bet.yml` failis lingid märkinud, võite selle osa vahele jätta ja otse Pull Request'i loomise osa juurde minna.*
- Naaske `/assets` kausta:
![event](assets/41.webp)
- Klõpsake nupul `Add file`, seejärel `Upload files`:
![event](assets/42.webp)
- Avaneb uus leht. Lohistage soovitud sisu alale:
![event](assets/43.webp)
- Näiteks lisasin BIP39 nimekirja PDF-faili:
![event](assets/44.webp)
- Kui sisu on üles laaditud, veenduge, et ruut `Commit directly to the patch-1 branch` oleks märgitud, seejärel klõpsake `Commit changes`:
![event](assets/45.webp)
- Naaske oma `/assets` kausta ja klõpsake just üles laaditud failil:
![event](assets/46.webp)
- Hankige oma faili vaheline URL. Näiteks minu puhul on URL:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Jätke URL-ist alles ainult viimane osa alates `/resources`:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Lisage URL-i alusele järgmine teave, et saada õige link:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Mida me siin teeme, on tulevase lingi etteaimamine teie failile, kui teie ettepanek on PlanB Networki allikarepositooriumiga ühendatud.
- Minge tagasi oma `bet.yml` faili ja klõpsake pliiatsi ikoonil: ![event](assets/47.webp)
- Lisage oma link sinna:
![event](assets/48.webp)
- Kui olete muudatustega valmis, klõpsake nupul `Commit changes...`:
![event](assets/49.webp)
- Lisage oma muudatustele pealkiri ja lühidescription:
![event](assets/50.webp)
- Klõpsake rohelisel nupul `Commit changes`:
![event](assets/51.webp)

---

- Kui kõik tundub teile hea, naaske oma fork'i juurkausta:
![event](assets/52.webp)
- Peaksite nägema teadet, et teie haru on muudetud. Klõpsake nupul `Compare & pull request`:
![event](assets/53.webp)
- Lisage oma PR-ile selge pealkiri ja description:
![event](assets/54.webp)
- Klõpsake nupul `Create pull request`:
![event](assets/55.webp)
Palju õnne! Teie PR on edukalt loodud. Administraator vaatab selle nüüd üle ja kui kõik on korras, ühendab selle PlanB Networki pearepositooriumiga. Teie BET ilmub veebisaidile mõne päeva pärast.

Jälgige kindlasti oma PR-i edenemist. Administraator võib jätta kommentaari, paludes lisateavet. Niikaua kui teie PR ei ole kinnitatud, saate seda vaadata PlanB Networki GitHubi repositooriumi Pull requests vahekaardil:
![event](assets/56.webp)
Suur tänu teie väärtusliku panuse eest! :)
