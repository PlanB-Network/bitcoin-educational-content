---
term: LOMMEBOKENS FOTAVTRYKK

---
Et sett med karakteristiske kjennetegn som kan observeres i transaksjoner utført av den samme Bitcoin-lommeboken. Disse kjennetegnene kan inkludere likheter i bruken av skripttyper, gjenbruk av adresser, rekkefølgen på UTXO-er, plasseringen av endringsutganger, signaleringen av RBF (*Replace-by-Fee*), versjonsnummeret, `nSequence`-feltet og `nLockTime`-feltet.

Lommebokfotavtrykk brukes av analytikere til å spore aktivitetene til en bestemt enhet i blokkjeden ved å identifisere tilbakevendende mønstre i transaksjonene. En bruker som systematisk sender vekslepenger til P2TR-adresser (`bc1p...`), oppretter for eksempel et karakteristisk fotavtrykk som kan brukes til å spore fremtidige transaksjoner.

Som LaurentMT forklarer i Space Kek #19 (en fransktalende podcast), øker nytten av lommebokfotavtrykk i kjedeanalyse betydelig over tid. Det økende antallet skripttyper og den stadig mer gradvise implementeringen av disse nye funksjonene i lommebokprogramvaren forsterker forskjellene. Det er til og med mulig å identifisere programvaren som brukes av den sporede enheten. Derfor er det viktig å forstå at det å studere en lommebøkenes fotavtrykk er spesielt relevant for nyere transaksjoner, mer enn for de som ble initiert tidlig på 2010-tallet.