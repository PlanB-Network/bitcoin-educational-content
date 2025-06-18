---
term: CPFP (DETE PLAĆA ZA RODITELJA)
---

Transakcioni mehanizam usmeren na ubrzavanje potvrde Bitcoin transakcije, slično onome što Replace-by-fee (RBF) radi, ali sa strane primaoca. Kada transakcija sa previše niskim naknadama u poređenju sa tržištem ostane zaglavljena u mempoolovima čvorova i ne potvrdi se dovoljno brzo, primalac može napraviti novu transakciju, trošeći bitkoine primljene u blokiranoj transakciji, iako još nije potvrđena. Ova druga transakcija nužno zahteva da prva bude rudarska kako bi bila potvrđena. Rudari su tako primorani da uključe obe transakcije zajedno. Druga transakcija će dodeliti mnogo više u naknadama za transakciju nego prva, na takav način da prosečna naknada podstiče rudare da uključe obe transakcije. Dečja transakcija (druga) plaća roditeljsku transakciju koja je zaglavljena (prva). Zbog toga se naziva "CPFP."


Dakle, CPFP omogućava primaocu da brže dobije svoja sredstva uprkos niskim početnim naknadama koje snosi pošiljalac, za razliku od RBF (*Replace-by-fee*), koji omogućava pošiljaocu da preduzme inicijativu da ubrza sopstvenu transakciju povećanjem naknada.