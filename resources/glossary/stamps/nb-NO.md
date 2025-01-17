---
term: STAMPS

---
En protokoll som gjør det mulig å integrere formaterte bildedata direkte i Bitcoin-blokkjeden gjennom rå multisignaturtransaksjoner (P2MS). Stamps koder det binære innholdet i et bilde i base 64 og legger det til nøklene i en 1/3 P2MS. Én nøkkel er ekte og brukes til å bruke pengene, mens de to andre er dummy-nøkler (den tilhørende private nøkkelen er ukjent) som lagrer dataene. Ved å kode dataene direkte som offentlige nøkler i stedet for å bruke `OP_RETURN`-utganger, er bilder som lagres med Stamps-protokollen, spesielt arbeidskrevende for nodene. Denne metoden skaper flere UTXO-er, noe som øker størrelsen på UTXO-settet og skaper problemer for fulle noder.