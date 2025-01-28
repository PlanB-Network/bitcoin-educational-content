---
term: TRANSAKSJONSVITNE

---
Refererer til en komponent i Bitcointransaksjoner som ble flyttet med SegWit soft fork for å løse problemet med transaksjonsfeilbarhet. Vitnet inneholder signaturene og de offentlige nøklene som er nødvendige for å låse opp bitcoinsene som brukes i en transaksjon. I Legacy-transaksjoner representerte vitnet summen av `scriptSig` fra alle inndataene. I SegWit-transaksjoner representerer vitnet summen av `scriptWitness` for hver inngang, og denne delen av transaksjonen er nå flyttet inn i et eget Merkle-tre i blokken.

Før SegWit kunne signaturer endres litt uten å bli ugyldiggjort før en transaksjon ble bekreftet, noe som endret transaksjonsidentifikatoren. Dette gjorde det vanskelig å bygge ulike protokoller, ettersom en ubekreftet transaksjon kunne få endret sin identifikator. Ved å skille vitnene fra hverandre gjør SegWit transaksjonene ikke-feilbarlige, ettersom enhver endring i signaturene ikke lenger påvirker transaksjonsidentifikatoren (TXID), men bare vitneidentifikatoren (WTXID). I tillegg til å løse problemet med manipulerbarhet, gjør denne separasjonen det mulig å øke kapasiteten til hver blokk.

> på engelsk oversettes "témoin" med "vitne"