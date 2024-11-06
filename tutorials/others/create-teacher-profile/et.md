---
name: PlanB Professor
description: Kuidas lisada oma professori profiili PlanB võrgustikku?
---
![kaas](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja hostitud GitHubis, mis võimaldab kõigil platvormi rikastamises osaleda. Panused võivad olla erinevad: olemasolevate tekstide parandamine ja toimetamine, koolituskursuste loomine, tõlkimine teistesse keeltesse, informatsiooni uuendamine või meie saidil veel mitte saadaolevate uute õpetuste loomine.

Kui soovite PlanB võrgustikule lisada uue täieliku õpetuse või kursuse, peate looma oma professori profiili. See võimaldab teil saada nõuetekohast tunnustust veebisaidil loodud sisu eest.
![õpetus](assets/1.webp)
Kui olete varem PlanB võrgustikule kaasa aidanud, on teil tõenäoliselt juba kaastöötaja ID. Leiate selle oma professori kaustast, mis on kättesaadav [sellel lehel](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors). Kui see nii on, võite selle õpetuse vahele jätta ja otse kaasa lööma hakata.
![õpetus](assets/2.webp)

Avastame koos, kuidas lisada uus professor selles õpetuses!

## Eeltingimused

**Tarkvara, mida on vaja minu õpetuse järgimiseks:**
- [GitHub Desktop](https://desktop.github.com/)
- Koodiredaktor ([VSC](https://code.visualstudio.com/) või [Sublime Text](https://www.sublimetext.com/))
![õpetus](assets/3.webp)
**Eeltingimused enne õpetuse alustamist:**
- Omama [GitHubi kontot](https://github.com/signup).
- Omama fork'i [PlanB võrgustiku lähterepositooriumist](https://github.com/PlanB-Network/bitcoin-educational-content).

**Kui vajate abi nende eeltingimuste saamiseks, juhendavad teid minu teised õpetused:**
- **[Git'i ja GitHubi mõistmine](https://planb.network/tutorials/others/basics-of-github)**
- **[GitHubi konto loomine](https://planb.network/tutorials/others/create-github-account)**
- **[Töökeskkonna seadistamine](https://planb.network/tutorials/others/github-desktop-work-environment)**

## Kuidas luua uut professori profiili?

- Avage oma brauser ja navigeerige oma PlanB repositooriumi forki lehele. Teie forki URL peaks välja nägema selline: `https://github.com/[kasutajanimi]/bitcoin-educational-content`
![õpetus](assets/4.webp)
- Veenduge, et olete peaharus `dev`, seejärel klõpsake nupul `Sync fork`. Kui teie fork ei ole ajakohane, pakub GitHub teie haru uuendamist. Jätkake selle sünkroniseerimisega.

- Kui teisest küljest on teie haru juba ajakohane, teavitab GitHub teid:
![õpetus](assets/5.webp)- Avage GitHub Desktop ja veenduge, et teie fork on õigesti valitud akna ülemises vasakus nurgas:
![õpetus](assets/6.webp)
- Klõpsake nupul `Fetch origin`.

- Kui teie kohalik repositoorium on juba ajakohane, ei paku GitHub Desktop edasisi toiminguid. Vastasel juhul ilmub valik `Pull origin`. Klõpsake sellel nupul, et uuendada oma kohalikku repositooriumi:
![õpetus](assets/7.webp)
- Veenduge, et olete peaharus `dev`:
![õpetus](assets/8.webp)
- Klõpsake sellel harul, seejärel klõpsake nupul `New Branch`:
![õpetus](assets/9.webp)
- Veenduge, et uus haru põhineb lähterepositooriumil, nimelt `PlanB-Network/bitcoin-educational-content`.
- Nimetage oma haru viisil, mis teeb selle eesmärgi selgeks, kasutades iga sõna eraldamiseks sidekriipse. Kuna see haru on mõeldud professori profiili lisamiseks, võiks näiteks nimi olla: `add-professor-[teie-nimi]`. Pärast nime sisestamist klõpsake `Create branch`, et kinnitada selle loomist:
![õpetus](assets/10.webp)
- Nüüd klõpsake nuppu `Publish branch`, et salvestada oma uus tööharu oma veebiharule GitHubis:
![õpetus](assets/11.webp)
- Sel hetkel, GitHub Desktopis, peaksite olema oma uuel harul. See tähendab, et kõik arvutis kohapeal tehtud muudatused salvestatakse ainult sellel konkreetsel harul. Samuti, niikaua kui see haru on GitHub Desktopis valitud, vastavad teie masinas kohapeal nähtavad failid nende haru failidele (`add-professor-your-name`), mitte põhiharu (`dev`) failidele:
![õpetus](assets/12.webp)
- Oma professori profiili lisamiseks avage oma failihaldur ja navigeerige oma kohalikku repositooriumisse, kaustas `professors`. Leiate selle teekonna alt: `\GitHub\bitcoin-educational-content\professors`.

- Selles kaustas looge uus kaust, mis on nimetatud teie nime või pseudonüümi järgi. Veenduge, et kausta nimes poleks tühikuid. Seega, kui teie nimi on "Loic Pandul" ja ükski teine professor ei oma seda nime, tuleb luua kaust nimega `loic-pandul`:
![õpetus](assets/13.webp)
- Asjade lihtsustamiseks võite juba kopeerida ja kleepida kõik dokumendid teise professori kaustast oma kausta. Seejärel jätkame nende dokumentide muutmist, et neid vastavalt teie profiilile kohandada:
![õpetus](assets/14.webp)
- Alustage navigeerimist kausta `assets`. Kustutage professori profiilipilt, kelle dokumendid te varem kopeerisite, ja asendage see oma profiilipildiga. On hädavajalik, et see pilt oleks `.webp` formaadis ja et see oleks nimetatud `profile`, andes täieliku failinime `profile.webp`. Olge teadlikud, et see pilt avaldatakse Internetis ja on kõigile kättesaadav: ![õpetus](assets/15.webp)
- Järgmisena avage `professor.yml` fail oma koodiredaktoriga (näiteks VSC või Sublime Text). Jõuate faili, mis on kopeeritud olemasolevast professorist:
![õpetus](assets/16.webp)
- Peate seejärel värskendama olemasolevat teavet oma teabega:
	- **name:** kirjutage oma nimi või pseudonüüm;
	- **links:** märkige oma kontod sotsiaalvõrgustikes nagu Twitter ja Nostr, samuti oma isikliku veebisaidi URL (valikuline);
	- **affiliation:** mainige ettevõtte nime, mis teid töötab (valikuline);
	- **tags:** täpsustage oma erialasid järgnevast loendist, teades, et võite lisada oma teemasid. Siiski veenduge, et märksõnade arv oleks piiratud maksimaalselt 4-ga, et tagada hea kasutajaliides:
	    - privacy,
	    - cryptography,
	    - bitcoin,
	    - mining,
	    - lightning-network,
	    - economy,
	    - history,
	    - merchants,
	    - security,
	    - ...
	- **tips:** esitage oma Lightning aadress annetuste jaoks, et teie tulevaste õpetuste lugejad saaksid teile mõned satsid saata (valikuline);
	- **company:** kui teil on oma ettevõte, märkige oma ettevõtte nimi (valikuline). Peate seejärel värskendama olemasolevat teavet oma teabega:
![õpetus](assets/17.webp)- Peate muutma ka `contributor-id`. See identifikaator on mõeldud teie äratundmiseks veebisaidil, kuid see ei ole GitHubist väljaspool avalik. Võite vabalt valida mis tahes kahe sõna kombinatsiooni, viidates [ingliskeelsele 2048 sõna nimekirjale BIP39-st](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Ärge unustage kahe valitud sõna vahele kriipsu lisamast. Näiteks siin valisin ma `crazy-cactus`:
![õpetus](assets/18.webp)
- Kui olete lõpetanud `professor.yml` dokumendi muutmise, klõpsake faili salvestamiseks `File > Save`. Seejärel võite oma koodiredaktorist väljuda:
![õpetus](assets/19.webp)
- Oma professori kaustas võite kustutada dokumendid keeltes, mis teid ei puuduta ja mis algselt kopeeriti teiselt professorilt. Jätke alles ainult teie emakeelega vastav fail. Näiteks minu puhul jätsin alles ainult `fr.yml` faili, kuna minu keel on prantsuse keel: ![õpetus](assets/20.webp)
- Topeltklõpsake sellel failil, et see oma koodiredaktoriga avada.

- Selles failis on teil võimalus kirjutada oma täielik elulugu jaotises `bio` ning kokkuvõte või lühike pealkiri jaotises `short_bio`:
![õpetus](assets/21.webp)
- Pärast oma `fr.yml` dokumendi salvestamist peate looma selle faili koopia järgmistes kaheksas keeles:
    - Saksa (DE);
    - Inglise (EN);
    - Prantsuse (FR);
    - Hispaania (ES);
    - Itaalia (IT);
    - Portugali (PT);
    - Jaapani (JA);
    - Vietnami (VI).

- Jätkake oma algse faili kopeerimist ja kleepimist, seejärel tõlkige iga dokument vastavasse keelde. Kui valdate keelt, võite tõlke teha käsitsi. Vastasel juhul võite kasutada automaatset tõlkevahendit või vestlusrobotit:
![õpetus](assets/22.webp)
- Kui eelistate, võite jätta alles ainult eluloo oma emakeeles; me hoolitseme tõlke eest pärast teie Pull Requesti esitamist.

- Teie professori kaust peaks seega välja nägema selline:
![õpetus](assets/23.webp)
```plaintext
eesnimi-perekonnanimi/
├── fr.yml
├── it.yml
├── es.yml
├── en.yml
├── de.yml
├── pt.yml
├── ja.yml
├── vi.yml
├── professor.yml
└── assets/
    └── profile.webp
```
- Nüüd naaske GitHub Desktopi.
- Akna vasakul küljel peaksite nägema kõiki teie harule tehtud muudatusi. Veenduge, et need muudatused on õiged:
![õpetus](assets/24.webp)
- Kui muudatused tunduvad teile õiged, sisestage oma commiti jaoks pealkiri. Commit on harule tehtud muudatuste salvestus, mida saadab kirjeldav sõnum, mis võimaldab jälgida projekti arengut aja jooksul.
- Pealkirja sisestamisel vajutage sinist nuppu `Commit to [your branch]`, et need muudatused kinnitada:
![õpetus](assets/25.webp)
- Seejärel klõpsake nupul `Push origin`. See saadab teie commiti teie forkile:
![õpetus](assets/26.webp)
- Kui olete selle haru jaoks oma muudatustega lõpetanud, klõpsake nüüd nupul `Preview Pull Request`:
![õpetus](assets/27.webp)
- Viimast korda saate kontrollida, kas teie muudatused on õiged, seejärel klõpsake nupul `Create pull request`: ![õpetus](assets/28.webp) - Teid suunatakse automaatselt teie brauseris GitHubi Pull Request'i ettevalmistamise lehele. Pull Request on taotlus, mille eesmärk on integreerida muudatused teie harust peaharusse PlanB Networki repositooriumis, mis võimaldab muudatuste üle vaadata ja arutada enne nende ühendamist: ![õpetus](assets/29.webp)
- Sellel ettevalmistuslehel märkige pealkiri, mis lühidalt kokku võtab muudatused, mida soovite allikarepositooriumiga ühendada.
- Lisage lühike kommentaar, kirjeldades neid muudatusi.
- Pärast nende sammude lõpetamist klõpsake rohelisel nupul `Create pull request`, et kinnitada ühendamistaotlus: ![õpetus](assets/30.webp)
- Teie PR muutub seejärel nähtavaks PlanB Networki pearepositooriumi `Pull Request` vahelehel. Nüüd peate lihtsalt ootama, kuni administraator võtab teiega ühendust, et kinnitada teie panuse ühendamist või paluda täiendavaid muudatusi: ![õpetus](assets/31.webp)
- Pärast teie PR ühendamist peaharuga on soovitatav kustutada oma tööharu (`add-professor-your-name`), et hoida teie forkis puhas ajalugu. GitHub pakub teile seda võimalust automaatselt teie PR lehel: ![õpetus](assets/32.webp)
- GitHub Desktop tarkvaras saate tagasi lülituda oma forki peaharusse (`dev`): ![õpetus](assets/8.webp)
- Kui soovite pärast oma PR esitamist oma profiilis muudatusi teha, sõltub protseduur teie PR-i praegusest seisundist:
	- Kui teie PR on endiselt avatud ja seda ei ole veel ühendatud, tehke muudatused kohalikult, jäädes samale harule. Kui muudatused on lõpetatud, kasutage nuppu `Push origin`, et lisada oma endiselt avatud PR-ile uus commit;
	- Juhul, kui teie PR on juba peaharuga ühendatud, peate protsessi alustama uuesti, luues uue haru ja esitades uue PR. Enne jätkamist veenduge, et teie kohalik repositoorium oleks PlanB Networki allikarepositooriumiga sünkroniseeritud.
