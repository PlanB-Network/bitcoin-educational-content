---
term: BIP
---

Skrót od "Bitcoin Improvement Proposal" Bitcoin Improvement Proposal (BIP) to formalny proces proponowania i dokumentowania ulepszeń i zmian w protokole Bitcoin i jego standardach. Ponieważ Bitcoin nie ma centralnego podmiotu decydującego o aktualizacjach, BIP pozwalają społeczności sugerować, omawiać i wdrażać ulepszenia w ustrukturyzowany i przejrzysty sposób. Każdy BIP wyszczególnia cele proponowanego ulepszenia, uzasadnienia, potencjalny wpływ na kompatybilność, a także zalety i wady. BIPy mogą być pisane przez każdego członka społeczności, ale muszą zostać zatwierdzone przez innych deweloperów i redaktorów, którzy utrzymują bazę danych Bitcoin Core GitHub: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun i Ruben Somsen. Ważne jest jednak, aby zrozumieć, że rola tych osób w edytowaniu BIP-ów nie oznacza, że kontrolują Bitcoin. Jeśli ktoś zaproponuje ulepszenie, które nie zostanie zaakceptowane w formalnych ramach BIP, nadal może przedstawić je bezpośrednio społeczności Bitcoin lub nawet utworzyć Fork zawierający jego modyfikację. Zaletą procesu BIP jest jego formalność i centralizacja, które ułatwiają debatę w celu uniknięcia podziałów wśród użytkowników Bitcoin, dążąc do wdrażania aktualizacji w sposób zgodny. Ostatecznie to zasada większości ekonomicznej określa dynamikę władzy w protokole.


BIP są podzielone na trzy główne kategorie:


- BIPy ścieżki standardów*: Dotyczą modyfikacji, które bezpośrednio wpływają na implementacje Bitcoin, takie jak reguły walidacji transakcji i bloków;
- BIP o charakterze informacyjnym*: Dostarczają informacji lub zaleceń bez proponowania bezpośrednich zmian w protokole;
- Procesy BIP*: Opis zmian w procedurach dotyczących Bitcoin, takich jak procesy zarządzania.


Ścieżki standardów i informacyjne BIP są również klasyfikowane według "Layer":


- Layer*: BIPy w tym Layer dotyczą zasad konsensusu Bitcoin, takich jak modyfikacje zasad walidacji bloków lub transakcji. Propozycje te mogą być forkami Soft (modyfikacje kompatybilne wstecz) lub Hard (modyfikacje niekompatybilne wstecz). Na przykład BIPy dla SegWit i Taproot należą do tej kategorii;
- Usługi równorzędne*: Ten Layer dotyczy działania sieci węzłów Bitcoin, czyli sposobu, w jaki węzły znajdują i komunikują się ze sobą w Internecie.
- API/RPC*: BIPy tego Layer dotyczą interfejsów programowania aplikacji (API) i zdalnych wywołań procedur (RPC), które umożliwiają oprogramowaniu Bitcoin interakcję z węzłami;
- Aplikacje Layer*: Layer odnosi się do aplikacji opartych na Bitcoin. BIPy w tej kategorii zazwyczaj dotyczą modyfikacji na poziomie standardów Bitcoin Wallet.


Proces zgłaszania BIP rozpoczyna się od konceptualizacji i omówienia pomysłu na liście mailingowej *Bitcoin-dev*. Jeśli pomysł jest obiecujący, autor przygotowuje projekt BIP zgodnie z określonym formatem i przesyła go za pośrednictwem Pull Request w repozytorium Core GitHub. Redaktorzy sprawdzają tę propozycję, aby zweryfikować, czy spełnia ona wszystkie kryteria. BIP musi być technicznie wykonalny, korzystny dla protokołu, zgodny z wymaganym formatowaniem i zgodny z filozofią Bitcoin. Jeśli BIP spełnia te warunki, zostaje oficjalnie zintegrowany z repozytorium BIP w serwisie GitHub. Następnie przypisywany jest mu numer. Numer ten jest zwykle ustalany przez redaktora, często Luke'a Dashjra, i jest przypisywany logicznie: BIP-y dotyczące podobnych tematów często otrzymują kolejne numery.


BIP przechodzą następnie przez różne statusy w trakcie swojego cyklu życia. Bieżący status jest określony w nagłówku każdego BIP:


- Projekt: Wniosek jest nadal w fazie opracowywania i debaty;
- Proponowane: BIP jest uważany za kompletny i gotowy do przeglądu przez społeczność;
- Odroczenie: BIP zostaje odłożony na później przez mistrza lub redaktora;
- Odrzucony: BIP jest klasyfikowany jako odrzucony, jeśli nie wykazuje żadnej aktywności przez 3 lata. Jego autor może zdecydować się na wznowienie go później, co pozwoli mu powrócić do statusu projektu;
- Wycofany: BIP został wycofany przez jego autora;
- Finał: BIP jest akceptowany i powszechnie wdrażany na Bitcoin;
- Aktywny: Status ten jest przypisywany wyłącznie do procesowych BIP po osiągnięciu określonego konsensusu;
- Zastąpiony / nieaktualny: BIP nie ma już zastosowania lub został zastąpiony nowszą propozycją, która czyni go zbędnym.


![](../../dictionnaire/assets/25.webp)


> *BIP jest skrótem od "Bitcoin Improvement Proposal". W języku francuskim można go przetłumaczyć jako "Proposition d'amélioration de Bitcoin". Jednak większość francuskich tekstów bezpośrednio używa akronimu "BIP" jako rzeczownika pospolitego, czasem rodzaju żeńskiego, czasem męskiego