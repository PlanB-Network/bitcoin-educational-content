---
term: COINSWAP
---

Protokoll for hemmelig overføring av Ownership mellom brukere. Denne metoden tar sikte på å overføre besittelse av bitcoins fra en person til en annen, og omvendt, uten at denne Exchange er eksplisitt synlig på Blockchain. Coinwap bruker smartkontrakter for å foreta overføringen uten behov for tillit mellom partene.


La oss tenke oss et naivt eksempel (som ikke fungerer) med Alice og Bob. Alice har 1 BTC sikret med den private nøkkelen $A$, og Bob har også 1 BTC sikret med den private nøkkelen $B$. Teoretisk sett kan de Exchange sine private nøkler via en ekstern kommunikasjonskanal for å gjennomføre en hemmelig overføring. Denne naive metoden innebærer imidlertid en høy risiko når det gjelder tillit. Ingenting hindrer Alice i å beholde en kopi av den private nøkkelen $A$ etter Exchange og bruke den senere til å stjele bitcoins, når nøkkelen er i hendene på Bob. I tillegg er det ingen garanti for at Alice ikke vil motta Bobs private nøkkel $B$ og aldri videreformidle sin private nøkkel $A$ i Exchange. Denne Exchange er derfor avhengig av overdreven tillit mellom partene, og er ineffektiv når det gjelder å sikre en sikker, hemmelig overføring av Ownership.


For å løse disse problemene og muliggjøre myntbytte mellom parter som ikke stoler på hverandre, kommer vi til å bruke Smart contract-systemer som gjør Exchange "atomisk". Disse kan være HTLC (*Hash Time-Locked Contracts*) eller PTLC (*Point Time-Locked Contracts*). Disse to protokollene fungerer på samme måte, ved hjelp av et tidslåsingssystem som sikrer at Exchange enten fullføres eller kanselleres fullstendig, og dermed beskytter integriteten til begge parters midler. Hovedforskjellen mellom HTLC og PTLC er at HTLC bruker hashkoder og forhåndsbilder for å sikre transaksjonen, mens PTLC bruker Adaptor Signatures.


I et myntbyttescenario med en HTLC eller PTLC mellom Alice og Bob foregår Exchange på en sikker måte: enten lykkes det, og begge mottar den andres BTC, eller så mislykkes det, og begge beholder sin egen BTC. Dette gjør det umulig for noen av partene å jukse eller stjele den andres BTC.


Bruken av Adaptor Signatures er spesielt interessant i denne sammenhengen, ettersom den gjør det mulig å unngå tradisjonelle skript (en mekanisme som noen ganger omtales som "_skriptløse skript"). Dette reduserer kostnadene forbundet med Exchange. En annen stor fordel med Adaptor Signatures er at de ikke krever bruk av en felles Hash for begge parter i transaksjonen, slik at man unngår behovet for å avsløre en direkte kobling mellom dem i visse typer Exchange.