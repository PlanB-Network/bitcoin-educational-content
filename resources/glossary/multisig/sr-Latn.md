---
term: Multisig
---

Novčanici sa višestrukim potpisom, često skraćeni kao "Multisig," dizajnirani su da poboljšaju sigurnost bitkoina zahtevajući više potpisa iz različitih privatnih ključeva za autorizaciju trošenja. Ova metoda raspodeljuje rizik među nekoliko ključeva, što pomaže u smanjenju rizika od gubitka i krađe (u zavisnosti od Multisig konfiguracije). Multisig novčanici funkcionišu na modelu "m-od-n", gde `m` predstavlja minimalan broj potpisa potrebnih za validaciju transakcije, a `n` je ukupan broj uključenih ključeva. Na primer, postavka 2-od-3 zahteva dva od tri moguća potpisa za validaciju transakcije. Ovaj pristup nudi superiornu sigurnost u poređenju sa novčanicima sa jednim ključem, ali takođe uvodi veću složenost u smislu upravljanja i bekapa. Štaviše, transakcije koje koriste starije Multisig standarde su manje privatne i skuplje u naknadama od tradicionalnih transakcija sa jednim potpisom. Međutim, nedavne inovacije kao što su Taproot i upotreba deskriptora očekuje se da minimiziraju, ako ne i eliminišu, ove nedostatke višestrukih potpisa.


> ► *Neki bitkoineri razlikuju pojmove "Multisig" i "Threshold Multisig." Zaista, neki tvrde da je Multisig nužno n-of-n, dok je threshold Multisig m-of-n. Međutim, u svakodnevnom jeziku, prihvaćeno je koristiti "Multisig" čak i za m-of-n.*