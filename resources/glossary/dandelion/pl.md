---
term: DANDELION
---

Propozycja mająca na celu poprawę prywatności routingu transakcji w sieci Bitcoin w celu przeciwdziałania deanonimizacji. W standardowym działaniu Bitcoin transakcje są natychmiast rozgłaszane do wielu węzłów. Zjawisko to może potencjalnie umożliwić obserwatorom powiązanie transakcji, zwykle anonimowych, z adresami IP. Celem BIP156 jest wyeliminowanie tego problemu w Address. W tym celu wprowadzono dodatkową fazę w procesie rozgłaszania, aby zachować anonimowość przed publiczną propagacją. W ten sposób Dandelion najpierw wykorzystuje fazę "stem", w której transakcja jest wysyłana przez losową ścieżkę węzłów, zanim zostanie rozesłana do całej sieci w fazie "fluff". Łodyga i puch są odniesieniami do zachowania propagacji transakcji w sieci, przypominając kształt mniszka lekarskiego. Ta metoda routingu zaciemnia ścieżkę prowadzącą z powrotem do węzła źródłowego, utrudniając śledzenie transakcji przez sieć z powrotem do jej źródła.


![](../../dictionnaire/assets/36.webp)