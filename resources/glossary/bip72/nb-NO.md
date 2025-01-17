---
term: BIP72

---
Kompletterer BIP70 og BIP71 ved å definere utvidelsen av Bitcoin URI (BIP21) med en ekstra parameter `r`. Denne parameteren gjør det mulig å inkludere en lenke til en sikker betalingsforespørsel signert av forhandlerens SSL-sertifikat. Når en klient klikker på denne utvidede URI-en, kontakter lommeboken deres forhandlerens server for å be om betalingsinformasjon. Disse opplysningene fylles automatisk ut i lommebokens transaksjonsgrensesnitt, og kunden kan bli informert om at de betaler domeneeieren som tilsvarer signeringssertifikatet (for eksempel "pandul.fr"). Siden denne forbedringen følger med BIP70, har den aldri blitt tatt i bruk i stor skala.