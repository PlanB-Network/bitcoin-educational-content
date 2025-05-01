---
term: BIP0156
---

Propozycja, znana jako Dandelion, ma na celu poprawę prywatności routingu transakcji w sieci Bitcoin w celu przeciwdziałania deanonimizacji. W standardowym działaniu Bitcoin transakcje są natychmiast transmitowane do wielu węzłów. Jeśli obserwator jest w stanie zobaczyć każdą transakcję przekazaną przez każdy węzeł w sieci, może założyć, że pierwszy węzeł, który wysyła transakcję, jest również węzłem źródłowym tej transakcji, a zatem pochodzi od operatora węzła. Zjawisko to może potencjalnie umożliwić obserwatorom powiązanie transakcji, zwykle anonimowych, z adresami IP.


Celem BIP156 jest Address tej kwestii. Aby to zrobić, wprowadza dodatkową fazę w transmisji, aby zachować anonimowość przed publiczną propagacją. W ten sposób Dandelion najpierw wykorzystuje fazę "stem", w której transakcja jest wysyłana przez losową ścieżkę węzłów, zanim zostanie rozesłana do całej sieci w fazie "fluff". Łodyga i puch są odniesieniami do zachowania propagacji transakcji w sieci, przypominając kształt mniszka lekarskiego (*a dandelion* w języku angielskim).


Ta metoda routingu zaciemnia ścieżkę prowadzącą z powrotem do węzła źródłowego, utrudniając śledzenie transakcji przez sieć z powrotem do jej źródła. Dandelion poprawia zatem prywatność, ograniczając zdolność przeciwników do deanonimizacji sieci. Metoda ta jest jeszcze bardziej skuteczna, gdy transakcja przechodzi w fazie "macierzystej" przez węzeł szyfrujący swoją komunikację sieciową, taki jak Tor lub *P2P Transport V2*. BIP156 nie został jeszcze dodany do Bitcoin Core.