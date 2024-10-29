---
name: Panus - Õpetused
description: Kuidas pakkuda välja uut õpetust PlanB võrgustikus?
---
![kaas](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja hostitud GitHub'is, mis pakub võimalust kõigile platvormi rikastamises osaleda. Panused võivad võtta erinevaid vorme: olemasolevate tekstide parandamine ja toimetamine, tõlkimine teistesse keeltesse, informatsiooni uuendamine või meie saidil veel mitteolevate uute õpetuste loomine.

Selles õpetuses selgitan, kuidas muuta PlanB võrgustiku "Õpetuste" jaotist. Kui soovite lisada uue õpetuse või parandada olemasolevat, on see artikkel teile! Vaatame üksikasjalikult, kuidas panustada PlanB võrgustikku GitHub'i kaudu, kasutades kirjutamisvahendit Obsidian.

## Eeltingimused

PlanB võrgustikku panustamiseks on teil 3 võimalust, sõltuvalt teie kogemuse tasemest GitHub'iga:
1. **Kogenud kasutajad**: Jätkake oma tavaliste meetoditega ja tutvuge selle õpetusega, et harjuda PlanB repositooriumi struktuuri, spetsiifiliste nõuetega ja töövooga.
2. **Algajad, kes on valmis õppima**: Soovitan seadistada oma töökeskkonna. Järgige seda õpetust ja meie teisi allpool loetletud artikleid, mis juhendavad teid samm-sammult.
3. **Algajad väiksemate panuste jaoks**: Ülesannete jaoks, mis nõuavad vähem muudatusi, nagu toimetamine või parandused, kasutage otse GitHub'i veebiliidest, ilma et seadistaksite täielikku kohalikku keskkonda.

**Tarkvara, mida on vaja minu õpetuse järgimiseks:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Koodiredaktor ([VSC](https://code.visualstudio.com/) või [Sublime Text](https://www.sublimetext.com/))
![õpetus](assets/1.webp)
**Eeltingimused enne õpetuse alustamist:**
- Omada [GitHub'i kontot](https://github.com/signup).
- Omada [PlanB võrgustiku lähterepositooriumi](https://github.com/PlanB-Network/bitcoin-educational-content) kahvelversiooni.
- Omada [professori profiili PlanB võrgustikus](https://planb.network/professors) (ainult juhul, kui pakute täielikku õpetust).

**Kui vajate abi nende eeltingimuste saamiseks, juhendavad teid minu teised õpetused:**
- **[Git'i ja GitHub'i mõistmine](https://planb.network/tutorials/others/basics-of-github)**
- **[GitHub'i konto loomine](https://planb.network/tutorials/others/create-github-account)**
- **[Töökeskkonna seadistamine](https://planb.network/tutorials/others/github-desktop-work-environment)**
- **[Professori profiili loomine](https://planb.network/tutorials/others/create-teacher-profile)**
## Millist tüüpi sisu kirjutada PlanB võrgustikus?
Otsime peamiselt õpetusi tööriistade kohta, mis on seotud Bitcoin'i või selle ökosüsteemiga. Need sisud võivad olla korraldatud kuue peamise kategooria ümber:
- Rahakott;
- Nood;
- Kaevandamine;
- Kaupmees;
- Vahetus;
- Privaatsus.
![õpetus](assets/2.webp)
Lisaks nendele Bitcoin'iga otseselt seotud teemadele otsib PlanB ka panuseid teemadel, mis rõhutavad individuaalset suveräänsust, nagu:
- Avatud lähtekoodiga tööriistad;
- Arvutustehnika;
- Krüptograafia;
- Energia;
- Matemaatika;
- Majandus;
- Tee-ise-projektid;
- Eluhäkkimine...
Näiteks on meil praegu õpetused Tails'i, Nostr'i või GrapheneOS'i kohta. Need tööriistad ei ole otseselt seotud Bitcoiniga, kuid need on süsteemid, mis võivad meid huvitada digitaalse maailma suveräänsuse protsessis. Neid sisusid saab integreerida "Teised" jaotise alamkategooriasse.
Teil on võimalus kujundada õpetus nullist või võtta varem teie veebisaidil avaldatud õpetus (eeldusel, et teil on autoriõigus), et jagada seda ka PlanB võrgustikus, lisades lingi algartiklile.

Olenemata teie valikust, pidage meeles, et kõik PlanB võrgustikus avaldatud sisu on vaba litsentsi [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) all. See litsents võimaldab kellelgi teie sisu kopeerida ja potentsiaalselt muuta, eeldusel, et algallikas on nõuetekohaselt ära märgitud.

## Kuidas pakkuda õpetust PlanB võrgustikus?

Kui kõik on paigas ja teie kohalik keskkond on oma PlanB võrgustiku kahvliga hästi seadistatud, võite alustada õpetuse lisamist.

### Loo uus haru

- Avage oma brauser ja minge oma PlanB hoidla kahvli lehele. See on kahvel, mille olete GitHubis loonud. Teie kahvli URL peaks välja nägema selline: `https://github.com/[teie-kasutajanimi]/bitcoin-educational-content`:
![õpetus](assets/3.webp)
- Veenduge, et olete peaharus `dev`, seejärel klõpsake nupul `Sync fork`. Kui teie kahvel ei ole ajakohane, pakub GitHub teie haru värskendamist. Jätkake selle värskendusega. Kui teie haru on vastupidi juba ajakohane, teavitab GitHub teid:
![õpetus](assets/4.webp)
- Avage GitHub Desktopi tarkvara ja veenduge, et teie kahvel on akna ülaosas korrektselt valitud:
![õpetus](assets/5.webp)
- Klõpsake nupul `Fetch origin`. Kui teie kohalik hoidla on juba ajakohane, ei paku GitHub Desktop edasisi toiminguid. Vastasel juhul ilmub valik `Pull origin`. Klõpsake sellel nupul, et värskendada oma kohalikku hoidlat: ![õpetus](assets/6.webp)
- Veenduge, et olete peaharus `dev`:
![õpetus](assets/7.webp)
- Klõpsake sellel harul, seejärel klõpsake nupul `New Branch`:
![õpetus](assets/8.webp)
- Veenduge, et uus haru põhineb allikahoidlal, nimelt `PlanB-Network/bitcoin-educational-content`.
- Nimetage oma haru nii, et pealkiri oleks selle eesmärgi suhtes selge, kasutades iga sõna eraldamiseks sidekriipse. Näiteks, kui meie eesmärk on kirjutada õpetus Sparrow Wallet tarkvara kasutamise kohta, võiks sellele pühendatud tööharu nimeks olla: `tuto-sparrow-wallet-loic`. Kui sobiv nimi on sisestatud, klõpsake haru loomise kinnitamiseks nupul `Create branch`:
![õpetus](assets/9.webp)
- Nüüd klõpsake nupul `Publish branch`, et salvestada oma uus tööharu oma veebikahvlile GitHubis:
![õpetus](assets/10.webp)
Nüüd peaks GitHub Desktopis olema teie uus haru. See tähendab, et kõik teie arvutis kohapeal tehtud muudatused salvestatakse ainult sellele konkreetsele harule. Samuti, niikaua kui see haru on GitHub Desktopis valitud, vastavad teie masinas kohapeal nähtavad failid selle haru (`tuto-sparrow-wallet-loic`) failidele, mitte peaharu (`dev`) failidele.
![õpetus](assets/11.webp)
Iga uue artikli avaldamiseks, mida soovite avaldada, peate looma uue haru `dev`-ist. Haru Git'is on projekti paralleelne versioon, mis võimaldab teil teha muudatusi ilma peaharu mõjutamata, kuni töö on valmis ühendamiseks.
### Juhendi lisamine

Nüüd, kui tööharu on loodud, on aeg integreerida teie uus juhend.
- Avage oma failihaldur ja navigeerige kausta `bitcoin-educational-content`, mis esindab teie repositooriumi kohalikku kloonimist. Tavaliselt peaksite selle leidma kaustast `Documents\GitHub\bitcoin-educational-content`. Selles kataloogis on vajalik leida sobiv alamkaust oma juhendi paigutamiseks. Kaustade organisatsioon peegeldab PlanB Network veebisaidi erinevaid sektsioone. Meie näites, kuna soovime lisada juhendi Sparrow Wallet'i kohta, on asjakohane minna järgmisele teele: `bitcoin-educational-content\tutorials\wallet`, mis vastab veebisaidi `WALLET` sektsioonile: ![juhend](assets/12.webp)
- `wallet` kaustas peate looma uue kataloogi, mis on spetsiaalselt pühendatud teie juhendile. Selle kausta nimi peab evokatsioonima tarkvara, mida juhendis käsitletakse, tagades sõnade ühendamise sidekriipsudega. Minu näites saab kausta pealkirjaks `sparrow-wallet`:
![juhend](assets/13.webp)
- Selles uues alamkaustas, mis on pühendatud teie juhendile, tuleb lisada mitu elementi:
	- Looge `assets` kaust, mis on mõeldud kõigi teie juhendi jaoks vajalike illustratsioonide vastuvõtmiseks;
    - Selles `assets` kaustas peate looma 8 alamkausta, mille nimed on `fr`, `de`, `en`, `it`, `es`, `ja`, `vi` ja `pt`, et klassifitseerida visuaalid vastavalt vastavatele keeltele. Samuti peate lisama `notext` alamkausta visuaalide jaoks, mis ei vaja tõlkimist, nagu näiteks ekraanipildid;
	- Tuleb luua `tutorial.yml` fail, et salvestada teie juhendiga seotud üksikasjad;
	- Markdown formaadis fail tuleb luua, et kirjutada teie juhendi tegelik sisu. See fail peab olema nimetatud vastavalt kirjutamise keelekoodile. Näiteks prantsuse keeles kirjutatud juhendi puhul peaks fail olema nimetatud `fr.md`.
![juhend](assets/14.webp)
- Kokkuvõtteks, siin on loodavate failide hierarhia:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (muudetud õige kategooria järgi)
        └── sparrow-wallet/ (muudetud juhendi nime järgi)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (muudetud vastavalt sobivale keelekoodile)
```

- Alustuseks avage oma `tutorial.yml` fail kasutades oma koodiredaktorit.
- Täitke iga väli allpool toodud teabega:
- **builder**: Sisestage ettevõtte nimi, mis toodab tarkvara, mille jaoks loote juhendi;
- **tags**: Määrake rida märksõnu, mis on tihedalt seotud teie artikli teemaga, et hõlbustada selle otsimist ja indekseerimist;
- **kategooria**: Valige PlanB saidil saadaolevate alamkategooriate hulgast sobiv, lähtudes teie õpetuse sisust. Näiteks `WALLET` sektsiooni õpetuse puhul on saadaolevad valikud `Desktop`, `Hardware` ja `Mobile`;
- **tase**: Määrake oma õpetuse raskusaste, valides ühe järgmistest neljast kategooriast:
    - Algaja (`beginner`),
    - Kesktase (`intermediary`),
    - Edasijõudnud (`advanced`),
    - Ekspert (`expert`).
- **professor**: Esitage oma kaastöötaja ID, nagu see ilmub teie professori profiilil. Lisateabe saamiseks vaadake [vastavat õpetust](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (valikuline): Kui soovite oma arendatava õpetuse jaoks krediteerida allikaveebisaiti, nagu teie isiklik sait, siis siin saate lisada vastava lingi.
![õpetus](assets/15.webp)
- Kui olete oma `tutorial.yml` faili muutmise lõpetanud, salvestage oma dokument, klõpsates `File > Save`:
![õpetus](assets/16.webp)
- Nüüd võite oma koodiredaktori sulgeda.
- `assets` kaustas peate lisama faili nimega `logo.webp`, mis toimib teie artikli pisipildina. See pilt peab olema `.webp` formaadis ja peab austama ruudukujulist mõõtmet, et harmoneeruda kasutajaliidesega. Teil on vabadus valida õpetuses käsitletava tarkvara logo või mõni muu asjakohane pilt, eeldusel, et see on vaba õigustest. Lisaks lisage samasse asukohta pilt pealkirjaga `cover.webp`. See pilt kuvatakse teie õpetuse ülaosas. Veenduge, et see pilt, nagu logo, austab kasutusõigusi ja sobib teie õpetuse konteksti:
![õpetus](assets/17.webp)
- Nüüd saate avada oma faili, mis võõrustab teie õpetust, nimetades selle teie keele koodiga, nagu `et.md`. Minge Obsidianis, akna vasakul küljel, kerige kaustapuud oma õpetuse kausta ja otsitava failini:
![õpetus](assets/18.webp)
- Klõpsake failil, et see avada:
![õpetus](assets/19.webp)
- Alustame `Properties` sektsiooni täitmisega dokumendi ülaosas. Kui see sektsioon puudub teie failist (kui dokument on täiesti tühi), saate selle reprodutseerida, kopeerides selle teisest olemasolevast õpetusest: ![õpetus](assets/20.webp)
- Samuti võite selle käsitsi lisada järgmisel viisil, kasutades oma koodiredaktorit:
```markdown
---
name: [Pealkiri]
description: [Kirjeldus]
---
```
![õpetus](assets/21.webp)
- Täitke oma õpetuse nimi ja lühidescription:
![õpetus](assets/22.webp)
- Seejärel lisage oma õpetuse algusesse kaanepilt. Selleks tippige:
```markdown
![kaanepilt-sparrow](assets/cover.webp)
```
- See süntaks on kasulik iga kord, kui on vajalik oma õpetusse pilt lisada. Hüüumärk näitab, et tegemist on pildiga, alternatiivtekst (alt) on märgitud nurksulgude vahele. Pildi tee on märgitud ümarsulgude vahele:
![õpetus](assets/23.webp)
- Jätkake oma õpetuse kirjutamist, lisades oma sisu. Kui soovite integreerida alapealkirja, rakendage sobivat markdowni vormindust, lisades teksti ette `##`:
![õpetus](assets/24.webp)

### Kuidas lisada õpetusse diagramme?
`assets` kaustas asuvad keelealakaustad on mõeldud diagrammide ja visuaalide organiseerimiseks, mis saadavad teie õpetust. Kui teie piltidel on tekst, veenduge, et tõlkite need kõikide asjaomaste keelte jaoks, et muuta teie sisu rahvusvahelisele publikule kättesaadavaks. Diagrammide puhul, millel pole tõlkida teksti või ekraanipiltide puhul, paigutage need otse `notext` alamkausta.
![õpetus](assets/25.webp)
Oma piltide nimetamiseks lihtsalt pange numbrid ilmumise järjekorras õpetuses. Näiteks nimetage oma esimene pilt `1.webp`, teine `2.webp` ja nii edasi.

Kui sama diagrammi on tõlgitud mitmesse keelde, hoidke erinevates keelealakaustades sama failinime, näiteks `en/1.webp`, `fr/1.webp`, `pt/1.webp` jne.

Teil on võimalus kasutada erinevaid pildiformaate nagu `jpeg`, `png` või `webp`. Soovitatav on valida `webp` formaat, et pildid oleksid vähem mahukad.
![õpetus](assets/26.webp)
Diagrammi oma dokumendisse lisamiseks kasutage Markdownis järgmist käsku, veendudes, et määrate sobiva alternatiivteksti ja pildi õige tee:
```markdown
![varblane](assets/notext/1.webp)
```
Hüüumärk alguses näitab, et tegemist on pildiga. Alternatiivtekst, mis aitab kaasa ligipääsetavusele ja SEO-le, asetatakse nurksulgude vahele. Lõpuks näidatakse pildi tee sulgudes: ![õpetus](assets/27.webp)
Kui soovite luua oma diagramme, veenduge, et järgite PlanB Networki graafilist hartat, et tagada visuaalne järjepidevus:
- **Font**: Kasutage [Rubik](https://fonts.google.com/specimen/Rubik);
- **Värvid**:
	- Oranž: #FF5C00
	- Must: #000000
	- Valge: #FFFFFF

**On hädavajalik, et kõik teie õpetustesse integreeritud visuaalid oleksid autoriõigustega vabad või vastaksid allikfaili litsentsile**. Lisaks tehakse kõik PlanB Networkis avaldatud diagrammid kättesaadavaks CC-BY-SA litsentsi alusel, samamoodi nagu tekst.

**-> Nipp:** Avalike failide, nagu pildid, jagamisel on oluline eemaldada kõik üleliigsed metaandmed. Need võivad sisaldada tundlikku teavet, nagu asukoha andmed, loomiskuupäevad või autori üksikasjad. Oma privaatsuse kaitsmiseks on soovitatav see metaandmed eemaldada. Selle toimingu lihtsustamiseks võite kasutada spetsialiseeritud tööriistu nagu [Exif Cleaner](https://exifcleaner.com/), mis pakub võimalust dokumendi metaandmeid lihtsa lohistamisega puhastada.

### Kuidas salvestada ja pushida õpetust?

Kui olete oma õpetuse valitud keeles kirjutamise lõpetanud, on järgmine samm esitada **Pull Request**. Administraator lisab seejärel teie õpetusele puuduvad tõlked, kasutades meie automatiseeritud tõlkemeetodit.

- Pull Requesti protsessiga jätkamiseks avage GitHub Desktop tarkvara.
- Tarkvara peaks automaatselt tuvastama teie poolt kohalikult tehtud muudatused võrreldes algse hoidlaga. Enne jätkamist kontrollige hoolikalt liidese vasakul küljel, et need muudatused vastaksid täpselt sellele, mida ootasite: ![õpetus](assets/28.webp)
- Lisage oma commit'ile pealkiri, seejärel klõpsake sinisel `Commit to [your branch]` nupul, et need muudatused kinnitada: ![õpetus](assets/29.webp)
Commit on tehtud muudatuste salvestus harule, millele on lisatud kirjeldav sõnum, võimaldades jälgida projekti arengut aja jooksul. Seega on see omamoodi vahepunkt.
- Seejärel klõpsake nupul `Push origin`. See saadab teie muudatuse teie fork'i: ![õpetus](assets/30.webp)- Kui te pole oma õpetusega lõpetanud, saate hiljem tagasi tulla ja teha uusi muudatusi.
- Kui olete selle haru jaoks oma muudatused lõpetanud, klõpsake nüüd nupul `Preview Pull Request`: ![õpetus](assets/31.webp)
- Kontrollige viimast korda, et teie muudatused on korrektsed, seejärel klõpsake nupul `Create pull request`:
![õpetus](assets/32.webp)
Pull Request on taotlus integreerida muudatused teie harust PlanB Networki peaharu, mis võimaldab muudatuste üle vaadata ja arutada enne nende ühendamist.

- Teid suunatakse automaatselt oma brauseris GitHubi oma Pull Requesti ettevalmistamise lehele:
![õpetus](assets/33.webp)
- Sisestage pealkiri, mis lühidalt kokku võtab muudatused, mida soovite allikarepositooriumiga ühendada.
- Lisage lühike kommentaar, kirjeldades neid muudatusi.
- Klõpsake rohelisel nupul `Create pull request`, et kinnitada ühendamistaotlus:
![õpetus](assets/34.webp)
Teie PR muutub seejärel nähtavaks PlanB Networki pearepositooriumi `Pull Request` vahelehel. Nüüd peate lihtsalt ootama, kuni administraator võtab teiega ühendust, et kinnitada teie panuse ühendamist või paluda täiendavaid muudatusi.
![õpetus](assets/35.webp)
Pärast teie PR ühendamist peaharuga on soovitatav kustutada oma tööharu (`tuto-sparrow-wallet`), et hoida teie fork'is puhas ajalugu. GitHub pakub teile seda võimalust automaatselt teie PR lehel:
![õpetus](assets/36.webp)
GitHub Desktop tarkvaras saate tagasi lülituda oma fork'i peaharu (`dev`).
![õpetus](assets/7.webp)
Kui soovite pärast oma PR esitamist oma panusele teha muudatusi, sõltub järgitav protseduur teie PR-i praegusest seisundist:
- Kui teie PR on endiselt avatud ja seda ei ole veel ühendatud, tehke muudatused kohapeal, jäädes samale harule. Kui muudatused on lõpetatud, kasutage uue commit'i lisamiseks oma endiselt avatud PR-ile nuppu `Push origin`;
- Juhul, kui teie PR on juba peaharuga ühendatud, peate protsessi algusest peale uuesti tegema, luues uue haru ja esitades uue PR. Enne jätkamist veenduge, et teie kohalik repositoorium on sünkroniseeritud PlanB Networki allikarepositooriumiga.
