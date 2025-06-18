---
term: ENTROPY
---

Entropia, w kontekście kryptografii i informacji, jest ilościową miarą niepewności lub nieprzewidywalności związanej ze źródłem danych lub procesem losowym. Entropia odgrywa kluczową rolę w bezpieczeństwie systemów kryptograficznych, zwłaszcza w generowaniu kluczy i liczb losowych. Wysoka entropia zapewnia, że wygenerowane klucze są wystarczająco nieprzewidywalne i odporne na ataki siłowe, w których atakujący próbuje wszystkich możliwych kombinacji, aby odgadnąć klucz.


W kontekście Bitcoin entropia jest używana do kluczy prywatnych lub nasion generate. Podczas tworzenia deterministycznego i hierarchicznego Wallet, konstrukcja frazy Mnemonic jest wykonywana z liczby losowej, która sama pochodzi ze źródła entropii. Fraza ta jest następnie wykorzystywana do generate wielu kluczy prywatnych, w sposób deterministyczny i hierarchiczny, w celu stworzenia warunków wydatków na UTXO.


Aby zapewnić bezpieczeństwo systemów kryptograficznych, niezbędne jest posiadanie wysokiej jakości źródła entropii. Źródłem entropii mogą być procesy fizyczne, takie jak szum elektroniczny lub zmiany termiczne, lub procesy programowe, takie jak generatory liczb pseudolosowych.