---
term: OVERT ASICBOOST
---

Otwarta i przejrzysta wersja AsicBoost. AsicBoost jest algorytmiczną techniką optymalizacji używaną w Bitcoin Mining. Górnicy korzystający z wersji Overt manipulują polem `nVersion` bloku kandydującego i używają tej modyfikacji jako dodatkowego Nonce. Ta metoda pozostawia rzeczywiste pole `Nonce` bloku niezmienione podczas każdej próby haszowania, zmniejszając w ten sposób obliczenia potrzebne dla każdego SHA256, poprzez utrzymanie niektórych danych takich samych między próbami. Ta wersja jest publicznie wykrywalna i nie ukrywa swoich modyfikacji przed resztą sieci, w przeciwieństwie do ukrytej wersji AsicBoost.