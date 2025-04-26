---
term: KONSOLIDERING

---
En spesifikk transaksjon der flere små UTXO-er slås sammen til én input for å danne én enkelt, større UTXO som output. Denne operasjonen er en transaksjon som gjøres til ens egen lommebok. Målet med konsolidering er å dra nytte av perioder der avgiftene i Bitcoin-nettverket er lave for å slå sammen flere små UTXO-er til én som er større i verdi. På den måten foregriper man obligatoriske utgifter i tilfelle gebyrøkninger, noe som gir besparelser på fremtidige transaksjonsgebyrer.

Transaksjoner med mange inndata er tyngre og følgelig dyrere. Utover besparelsene som kan oppnås på transaksjonsgebyrer, er konsolidering også en form for langsiktig planlegging. Hvis lommeboken din inneholder svært små UTXO-er, kan disse bli ubrukelige hvis Bitcoin-nettverket går inn i en lengre periode med høye gebyrer. Hvis du for eksempel trenger å bruke en UTXO på 10 000 sats, men minimumsgebyret for utvinning er på 15 000 sats, vil utgiftene overstige verdien av selve UTXO-en. Disse små UTXO-ene blir da økonomisk irrasjonelle å bruke, og forblir ubrukelige så lenge avgiftene ikke reduseres. Disse UTXO-ene omtales ofte som "støv" Ved å regelmessig konsolidere de små UTXO-ene dine, reduserer du denne risikoen knyttet til gebyrøkninger.

Det er imidlertid viktig å merke seg at konsolideringstransaksjoner er gjenkjennelige under en kjedeanalyse. En slik transaksjon indikerer en Common Input Ownership Heuristic (CIOH), noe som betyr at inndataene i konsolideringstransaksjonen eies av én og samme enhet. Dette kan ha konsekvenser for personvernet til brukeren.

![](../../dictionnaire/assets/7.webp)