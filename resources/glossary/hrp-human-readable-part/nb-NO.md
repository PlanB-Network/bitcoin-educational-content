---
term: Hrp (human readable part)

definition: Lesbar prefiks for bech32-adresser som gjør det mulig å identifisere typen Bitcoin-adresse.
---
HRP, som står for "Human Readable Part", er en komponent i bech32- og bech32m-mottakeradresser (SegWit v0 og SegWit v1). HRP refererer til den delen av adressen som er spesifikt formatert for å kunne leses og tolkes av mennesker. Ta for eksempel en bech32 Bitcoin-adresse:

```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```

I denne adressen representerer det innledende `bc` HRP. Dette prefikset gjør at man raskt kan identifisere at tegnrekken som presenteres er en Bitcoin-adresse og ikke noe annet.