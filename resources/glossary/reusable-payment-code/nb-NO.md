---
term: GJENBRUKBAR BETALINGSKODE

---
I BIP47 er en gjenbrukbar betalingskode en statisk identifikator som genereres fra en Bitcoin-lommebok, og som gjør det mulig å varsle transaksjonen og utlede unike adresser. På denne måten unngår man gjenbruk av adresser, noe som fører til tap av personvern, uten å måtte utlede og overføre nye, ubrukte adresser manuelt for hver betaling. I BIP47 er gjenbrukbare betalingskoder konstruert på følgende måte:


- Byte 0 tilsvarer versjonen;
- Byte 1 er et bitfelt for å legge til informasjon i tilfelle spesifikk bruk;
- Byte 2 angir pariteten til `y` i den offentlige nøkkelen;
- Fra byte 3 til byte 34 finner du `x`-verdien til den offentlige nøkkelen;
- Fra byte 35 til byte 66 er det kjedekoden som er knyttet til den offentlige nøkkelen;
- Fra byte 67 til byte 79 er det null utfylling.

Betalingskoden inneholder vanligvis en Human-Readable Part (HRP) i begynnelsen og en sjekksum på slutten, og deretter kodes den i base58. Oppbyggingen av en betalingskode er dermed ganske lik oppbyggingen av en utvidet nøkkel. Her er for eksempel min egen BIP47-betalingskode i base58:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

I PayNym-implementeringen av BIP47 kan betalingskoder også uttrykkes i form av identifikatorer som er knyttet til bildet av en robot. Her er for eksempel min:

```text
+throbbingpond8B1
```

Bruk av betalingskoder med PayNym-implementeringen er for øyeblikket tilgjengelig i Sparrow Wallet på PC og i Samourai Wallet på mobil.