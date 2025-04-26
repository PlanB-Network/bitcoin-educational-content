---
term: SETTINGS.JSON

---
Fil som brukes i Bitcoin Core til å lagre innstillingene for det grafiske brukergrensesnittet (GUI). Den lagrer informasjon om brukerkonfigurasjoner, som for eksempel åpne lommebøker. Når Bitcoin Core startes på nytt, muliggjør denne filen automatisk gjenåpning av lommebøker som var aktive før applikasjonen ble lukket. Hvis en lommebok lukkes via det grafiske brukergrensesnittet, fjernes den også fra denne filen, og den vil derfor ikke åpnes automatisk ved neste start.