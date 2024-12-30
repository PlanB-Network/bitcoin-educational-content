---
name: GitHubi alused
description: Git'i ja GitHubi aluste mõistmine
---

![cover](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta, mis oleksid saadaval võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja hostitud GitHubis, pakkudes kõigile võimalust panustada platvormi rikastamisse. Panused võivad võtta erinevaid vorme: olemasolevate tekstide parandamine ja toimetamine, tõlkimine teistesse keeltesse, informatsiooni uuendamine või meie saidil veel mitteolevate õpetuste loomine.

Kui soovite panustada PlanB võrgustikku, peate kasutama Git'i ja GitHubi. Kui need tööriistad on teile tundmatud või nende toimimine tundub arusaamatu, ärge paanitsege, see artikkel on teile! Vaatame koos üle Git'i ja GitHubi alused, samuti nendega seotud tehnilise žargooni, et võimaldada teil neid tööriistu hiljem tõhusalt kasutada.

## Mis on Git?

Git on versioonihaldussüsteem, mis on spetsiaalselt loodud tarkvaraprojektide haldamiseks. Linus Torvaldsi poolt 2005. aastal loodud Git on kiiresti saanud tarkvaraarendustööstuse standardiks versioonihalduses. Aga mida see täpselt tähendab?
![git](assets/1.webp)
Oma olemuselt võimaldab Git arendajatel jälgida projekti lähtekoodis aja jooksul tehtud muudatusi. See tähendab, et iga koodis tehtud muudatusega salvestab Git projekti uue versiooni. Kui ilmneb viga või kui katsetuslik funktsioon ei tööta oodatult, on võimalik naasta koodi varasema seisundi juurde, nagu omamoodi ajamasin failide jaoks.

Üks Git'i võtmefunktsioone on harude haldamine. Haru on omamoodi paralleeljoon, kus arendajad saavad töötada sõltumatult ülejäänud projektist. See hõlbustab suuresti uute funktsioonide lisamist või vigade parandamist ilma peamist koodi segamata. Kui muudatused on testitud ja valideeritud, saab need peaharuga ühendada.

Üks Git'i eripärasid on selle võime toimida detsentraliseeritult. Igal arendajal on oma arvuti kõvakettal projekti täielik koopia, mis võimaldab neil töötada võrguühenduseta ja ühendada muudatused hiljem, kui Interneti-ühendus on saadaval. See vähendab konfliktide riski ja võimaldab mitmel arendajal samaaegselt töötada samal projektil ilma üksteisele jalgu jäämata.
Algselt oli Git peamiselt mõeldud tarkvaraarendusprojektide jaoks. Siiski saab seda kasutada ka sisukirjutamisprojektide haldamiseks. Koostööd tehakse koodi asemel teksti kallal. Ja just seda meetodit on PlanB võrgustik oma sisu haldamiseks kasutanud! Git hõlbustab õppematerjalide ja õpetuste kirjutamisel koostööd, kuna see võimaldab muudatuste täpset jälgimist, tõhusat versioonihaldust ning samuti sisu teiste kaastöötajate poolt ülevaatamist ja täiustamist.
## Mis on GitHub?

GitHub on Git versioonihaldussüsteemil põhinev lähtekoodi haldamise ja hostimise platvorm, millest me just rääkisime. 2008. aastal käivitatud GitHub on kiiresti populaarsust kogunud ja saanud arendajatele üle maailma hädavajalikuks viitepunktiks. Kuidas aga GitHub erineb Git'ist ja miks on see meie sisutootmismeetodis nii oluline?
![github](assets/2.webp)
Esmalt on oluline mõista, et GitHub on ehitatud Git'i peale (millest me eelmises jaotises rääkisime). Kui Git on tööriist, mis jälgib koodimuudatusi, siis GitHub on veebiteenus, mis hostib, jagab ja haldab seda koodi.

Kujutage Git'i ette omamoodi logiraamatuna, mida iga arendaja kasutab oma arvutis kõigi oma projekti muudatuste salvestamiseks. GitHub seevastu on nagu avalik raamatukogu, kus kõiki neid logiraamatuid saab jagada, võrrelda ja ühendada.
Git'i ja GitHub'i põhimõtteline erinevus seisneb nende funktsioonis: Git on tööriist, mida iga arendaja kasutab kohalikult oma koodiversioonide haldamiseks, samas kui GitHub on veebiplatvorm, mis majutab neid versioone ja hõlbustab koostööd.
GitHub on palju enamat kui lihtsalt koodi majutamise teenus. See on koostööplatvorm, mis võimaldab arendajatel tõhusalt koos töötada. Ja tõepoolest, PlanB Network kasutab seda platvormi mitte ainult kogu veebisaidi jõustava koodi, vaid ka, ja see on meie jaoks huvipakkuv, kogu sisu (õpetused, koolitused, ressursid...) majutamiseks.

## Mõned Tehnilised Terminid

Git'i ja GitHub'i kasutades kohtate käsklusi ja funktsioone, mille nimed võivad tunduda keerulised. Selles viimases osas pakun lihtsaid definitsioone, et mõista tehnilisi termineid, millega võite Git'i ja GitHub'i kasutamisel kokku puutuda:

- **Fetch origin:** Käsk, mis toob kohalikku repositooriumisse viimased teabe ja muudatuste andmed kaugrepositooriumist ilma neid kohaliku tööga ühendamata. See uuendab teie kohalikku repositooriumit uute harude ja muudatustega, mis on kaugrepositooriumis olemas.

- **Pull origin:** Käsk, mis toob uuendused kaugrepositooriumist ja integreerib need kohe teie kohalikku harusse, et see sünkroniseerida. See ühendab fetchi ja merge'i sammud üheks käsuks.
- **Sync Fork:** Funktsioon GitHub'is, mis võimaldab teil uuendada oma projekti kahvelversiooni viimaste muudatustega allikarepositooriumist. See tagab, et teie projekti koopia püsib peamise arendusega ajakohane.
- **Push origin:** Käsk, mida kasutatakse teie kohalike muudatuste saatmiseks kaugrepositooriumisse.

- **Pull Request:** Taotlus, mille esitab kaastöötaja, et näidata, et nad on lükanud muudatused kaugrepositooriumi harusse ja soovivad, et neid muudatusi vaadataks üle ja võimalusel ühendataks repositooriumi peaharuga.

- **Commit:** Oma muudatuste salvestamine. Commit on nagu hetktõmmis teie tööst antud hetkel, mis võimaldab hoida muudatuste ajalugu. Iga commit sisaldab kirjeldavat sõnumit, mis selgitab, mis on muudetud.

- **Branch:** Repositooriumi paralleelversioon, mis võimaldab teil muudatustega töötada ilma peaharu (tihti nimetatud "main" või "master") mõjutamata. Harud hõlbustavad uute funktsioonide arendamist ja vigade parandamist ilma stabiilse koodi häirimise riskita.

- **Merge:** Ühendamine seisneb muudatuste integreerimises ühest harusse teise. Seda kasutatakse näiteks tööharu muudatuste lisamiseks peaharusse, mis võimaldab erinevate panuste lisamist.

- **Fork:** Repositooriumi kahveldamine tähendab selle repositooriumi koopia loomist oma GitHub'i kontole, mis võimaldab teil projekti kallal töötada ilma algset repositooriumit mõjutamata. Kahvel võib minna oma teed ja saada algsest projektist erinevaks või see võib regulaarselt sünkroniseerida algse projektiga, et sellele kaasa aidata.

- **Clone:** Repositooriumi kloonimine tähendab selle kohaliku koopia tegemist oma arvutisse, mis annab teile juurdepääsu kõigile failidele ja ajaloole. See võimaldab teil projekti otse kohapeal töötada.

- **Repository:** Projekti hoiuruum GitHub'is. Repositoorium sisaldab kõiki projekti faile ning kõigi nendele tehtud muudatuste ajalugu. See on GitHub'is hoiustamise ja koostöö alus.

- **Issue:** Tööriist ülesannete ja vigade jälgimiseks GitHub'is. Issued võimaldavad probleemidest teatada, ettepanekuid teha või uutest funktsioonidest arutada. Iga issue saab määrata, märgistada ja kommenteerida.

See nimekiri ei ole kaugeltki ammendav. On palju muid tehnilisi termineid, mis on spetsiifilised Git'ile ja GitHub'ile. Siiski mainitud siin on peamised, millega te sageli kokku puutute.
Pärast selle artikli lugemist võib olla, et mõned aspektid Git'ist ja GitHub'ist on teile endiselt ebaselged. Julgustan teid neid tööriistu ise kasutama hakkama. Praktika on tihti parim viis mõista, kuidas masin töötab! Alustamiseks võite avastada need 2 teist õpetust:
- **[Loo oma GitHubi konto](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
- **[Seadista oma kohalik keskkond, et panustada PlanB võrgustikku](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**