---
name: Setting Up a BitAxe
Description: Hvordan sette opp en BitAxe?
---

### Introduksjon

BitAxe er et åpen kildekode-prosjekt skapt av Skot og [tilgjengelig på GitHub](https://github.com/skot/bitaxe) som tillater kostnadseffektiv eksperimentering med mining.

Det har reversert ingeniørkunsten bak den berømte Antminer S19 fra Bitmain, markedslederen innen ASICs, de spesialiserte maskinene for bitcoin-mining. Nå er det mulig å bruke disse kraftige brikkene i nye åpen kildekode-prosjekter. I motsetning til Nerdminer, har BitAxe tilstrekkelig databehandlingskraft til å kobles til en miningpool, som vil tillate deg å jevnlig tjene noen satoshis. Nerdminer, på den andre siden, kan kun kobles til det som kalles en solopool, som fungerer som et lodd: du har en liten sjanse for å vinne hele blokkbelønningen.

Det finnes flere versjoner av BitAxe, med forskjellige brikker og ytelse:

| Bitaxe Modellserie       | ASIC-brikke | Brukt På                    | Forventet Hash Rate         | Ideell For                                                                                                 |
| ------------------------ | ----------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Serie 100)   | 1 x BM1397  | Antminer Serie 17           | 400 GH/s (opp til 450 GH/s) | Bitcoin-mining nybegynnere, tilbyr en solid hash rate med moderat strømforbruk.                            |
| Bitaxe Ultra (Serie 200) | 1 x BM1366  | Antminer S19 XP og S19k Pro | 500 GH/s (opp til 550 GH/s) | Seriøse minere som sikter på å balansere effektivitet og høyere hash rate.                                 |
| Bitaxe Hex (Serie 300)   | 6 x BM1366  | Antminer S19k Pro og S19 XP | 3.0 TH/s (opp til 3.3 TH/s) | Minere som søker skalérbarhet og høy ytelse uten å ofre effektivitet.                                      |
| Bitaxe Supra (Serie 400) | 1 x BM1368  | Antminer S21                | 600 GH/s (opp til 700 GH/s) | Seriøse entusiaster som søker de høyeste hash ratene og effektiviteten.                                    |

I denne veiledningen vil vi bruke en BitAxe Ultra 204 utstyrt med en BM1366-brikke, brukt for Antminer S19XP. Denne er allerede montert og flashet av forhandleren.

### [Listen over forhandlere er tilgjengelig på denne siden](https://bitaxe.org/legit.html)

![signup](assets/2.webp)

Vanligvis selges strømforsyningen med den. Hvis ikke, må du kjøpe en strømforsyning med en 5V jack-kabel og minst 4A.

![signup](assets/1.webp)

### Konfigurasjon
Når du først kobler til BitAxe, vil den forsøke å koble seg til et Wi-Fi-nettverk som standard. Etter fem forsøk, vil den vise navnet på sitt eget Wi-Fi-nettverk slik at du kan koble til det og konfigurere det.
For å gjøre dette, kan du bruke hvilken som helst datamaskin eller smarttelefon. Gå til Wi-Fi-innstillingene dine, søk etter nye nettverk, og du vil se et Wi-Fi kalt Bitaxe_XXXX. Her er det `Bitaxe_A859`. Koble til dette Wi-Fi-nettverket, og et vindu vil automatisk åpne seg.

![signup](assets/3.webp)

I dette vinduet, klikk på de tre små horisontale linjene øverst til venstre, deretter på `Settings`.

![signup](assets/4.webp)

Du må manuelt angi informasjonen til Wi-Fi-nettverket ditt, ettersom det ikke finnes noe automatisk oppdagelsessystem.
![signup](assets/5.webp)
Derfor, angi SSID-en til Wi-Fi, det vil si navnet på nettverket ditt, passordet, samt informasjonen om miningpoolen du har valgt. Vær forsiktig, her presenteres ikke URL-en til poolen på samme måte. For eksempel, for Braiins, er pool-URL-en som oppgis: `stratum+tcp://eu.stratum.braiins.com:3333`.

![signup](assets/6.webp)

Som du kan se på skjermen, må du fjerne `stratum+tcp://` og `:3333` delene, og bare la `eu.stratum.braiins.com` stå igjen. Deretter, i `Port` feltet, skriv inn de 4 sifrene på slutten av URL-en gitt av poolen, men uten `:`. Her er det altså `3333`.

I denne opplæringen bruker vi Braiins miningpool, men du står fritt til å velge en annen. Du kan finne våre opplæringer om miningpooler [på PlanB Network-nettstedet](https://planb.network/en/tutorials/mining).

Videre, i `User`, skriv inn din identifikator og deretter `Password`, vanligvis er det `"x"` eller `"Anything123"`.

`Core Voltage` innstillingen bør stå på `1200` som standard, og for `Frequency`, la også standardverdien stå i utgangspunktet. Det vil være mulig å justere denne innstillingen senere for å oppnå mer databehandlingskraft. Det er imidlertid viktig å sørge for at chipens temperatur ikke overstiger 65-70°C, da BitAxe ikke har et system for å redusere ytelsen i tilfelle overoppheting. Hvis temperaturen overstiger 65°C for mye, kan det skade din BitAxe.

![signup](assets/7.webp)

Når du har korrekt angitt alle innstillingene, klikk på `Save`-knappen nederst, og deretter restart din BitAxe enkelt ved å koble den fra og koble den til igjen.
Hvis du har angitt informasjonen din korrekt, bør enheten raskt koble seg til Wi-Fi, deretter til miningpoolen, og begynne å vise noe informasjon på sin lille skjerm. Det vil sannsynligvis ta noen minutter før den vises på miningpoolens dashboard.
### Dashboard og Skjerm

Tre forskjellige visninger vil rulle gjennom. På den tredje siden vil du se `IP`-informasjonen, som er IP-adressen som lar deg koble til dashboardet. Her er adressen `192.168.1.19`.

![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)

For å få tilgang til dashboardet, skriv bare inn denne adressen i din internettleser.

På dashboardet vil du finne all informasjonen som vises på den lille skjermen, som vi nå vil se nærmere på.

![signup](assets/11.webp)

| BitAxe Skjerm | Dashboard                                   | Beskrivelse                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | Den nåværende databehandlingskraften, uttrykt i GigaHash/s                                                                                                                                                                |
| W/THs         | Effektivitet                                | Dette er effektiviteten til din BitAxe uttrykt i W/THs. Det er forholdet mellom den elektriske kraften som forbrukes og databehandlingskraften som produseres.                                                            |
| A/R           | Aksjer                                      | Antall `Aksjer` sendt av din BitAxe til poolen, som representerer mengden arbeid som er levert.                                                                                                                           |
| UT            | Driftstid                                   | Tiden siden din BitAxe har vært i drift uten avbrudd (tilgjengelig i venstremenyen under `Logs`).                                                                                                                        |
| BD            | Beste Vanskelighetsgrad                     | Maksimal vanskelighetsgrad nådd siden siste omstart. Til sammenligning er den nåværende nettverksvanskeligheten omtrent 85T.                                                                                               |
| FAN           | FAN i `Varme`-boksen                        | Viftehastighet, uttrykt i rotasjoner per minutt.                                                                                                                                                                           |
| Temp          | ASIC-temperatur i `Varme`-boksen           | Chip-temperatur, som ikke bør overstige 65°C.                                                                                                                                                                             |
| Pwr           | Strøm                                       | Strøm i watt som forbrukes. Denne informasjonen tar imidlertid ikke hensyn til skjermen, viften eller strømforsyningen. For eksempel, når den viser 11.7W, er det totale forbruket faktisk 15.8W.                         |
| mV mA         | Inngangsspenning Inngangsstrøm              | Spenning og strøm forbrukt av maskinen. Strømmen i watt er lik spenningen multiplisert med strømmen.                                                                                                                      |
| FH            | Ledig Heap-minne (venstre meny -> `Logger`) | Tilgjengelig minne.                                                                                                                                                                                                       |
| vCore         | ASIC-spenning (i Ytelsesboksen)             | Spenning målt på ASIC-chipen.                                                                                                                                                                                             |
| IP            | NA                                          | IP-adresse.                                                                                                                                                                                                               |
| V2.1.0        | Versjon (venstre meny -> `Logger`)          | Firmwareversjon.                                                                                                                                                                                                          |
Du kan endre Wi-Fi- eller bassenginnstillingene når som helst uten noe problem.  
Avhengig av ventilasjonen og temperaturen i rommet ditt, kan det hende du må øke eller måtte redusere ytelsen slik at temperaturen ikke overstiger 65°C. Hvis du øker ytelsen, vil du tjene flere satoshis, men din BitAxe vil også forbruke mer elektrisitet!