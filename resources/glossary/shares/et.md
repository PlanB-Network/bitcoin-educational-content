---
term: SHARES
---

Kaevandusbasseinide kontekstis on osak (share) näitaja, mida kasutatakse üksiku kaevurite panuse kvantifitseerimiseks basseinis. See mõõdik on aluseks preemia arvutamisel, mida bassein iga kaevuri vahel ümber jaotab. Iga osak vastab räsi (hash) väärtusele, mis rahuldab raskustaseme sihtmärki, mis on madalam kui Bitcoin'i võrgustikul.

Analoogia abil selgitades kujutage ette 20-tahulist täringut. Bitcoin'il eeldame, et töötõendi (proof of work) valideerimiseks on vaja veeretada numbrit, mis on väiksem kui 3 (st saavutada tulemus 1 või 2). Nüüd kujutage ette, et kaevandusbasseinis on osaku raskustaseme sihtmärk seatud 10 peale. Seega, iga basseini üksiku kaevuri täringuveeretus, mis annab tulemuseks numbri, mis on väiksem kui 10, loetakse kehtivaks osakuks. Need osakud edastab kaevur seejärel basseinile, et nõuda oma preemiat, isegi kui need ei vasta Bitcoin'i plokile kehtivale tulemusele.

Iga arvutatud räsi puhul võib basseini üksik kaevur kohata kolme erinevat stsenaariumi:
* Kui räsi väärtus on suurem või võrdne basseini seatud raskustaseme sihtmärgiga osaku jaoks, siis see räsi pole kasutatav. Kaevur muudab oma nonce'i, et proovida uut räsi: `hash > share > block`.
* Kui räsi on madalam kui osaku raskustaseme sihtmärk, kuid suurem või võrdne Bitcoin'i raskustaseme sihtmärgiga, siis see räsi moodustab kehtiva osaku, mis siiski ei ole piisav ploki valideerimiseks. Kaevur saab selle räsi saata oma basseinile, et nõuda osakuga seotud preemiat: `share > hash > block`.
* Kui räsi on madalam kui Bitcoin'i võrgustiku raskustaseme sihtmärk, peetakse seda nii kehtivaks osakuks kui ka kehtivaks plokiks. Kaevur edastab selle räsi oma basseinile, mis kiirustab seda Bitcoin'i võrgustikus levitama. Seda räsi loetakse ka kaevuri kehtivaks osakuks: `share > block > hash`.

![](../../dictionnaire/assets/32.png)

Seda osakute süsteemi kasutatakse iga üksiku kaevuri poolt basseinis tehtud töö hinnanguliseks määramiseks, ilma et oleks vaja üksikult ümber arvutada kõiki kaevuri poolt genereeritud räsiväärtusi, mis oleks basseini jaoks täiesti ebaefektiivne.

Kaevandusbasseinid kohandavad osakute raskust, et tasakaalustada kontrollikoormust ja tagada, et iga kaevur, olgu ta väike või suur, esitab osakuid umbes iga paari sekundi järel. See võimaldab täpselt arvutada iga kaevuri hashrate'i ja preemiate jaotamist vastavalt valitud kompensatsiooni arvutamise meetodile (PPS, PPLNS, TIDES...).

> ► *Prantsuse keeles võib "shares" tõlkida kui "part".*