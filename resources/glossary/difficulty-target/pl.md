---
term: DOCELOWY POZIOM TRUDNOŚCI
---

Współczynnik trudności, znany również jako cel trudności, jest parametrem wykorzystywanym w mechanizmie konsensusu przez Proof of Work (Proof of Work, PoW) na Bitcoin. Wartość docelowa reprezentuje wartość liczbową, która określa trudność dla górników w rozwiązaniu określonego problemu kryptograficznego, zwanego Proof of Work, podczas tworzenia nowego bloku na Blockchain.


Docelowa trudność to regulowana 256-bitowa (64 bajty) liczba określająca limit akceptowalności dla haszowania nagłówków bloków. Innymi słowy, aby blok był ważny, Hash jego nagłówka z `SHA256d` (podwójne `SHA256`) musi być numerycznie niższe lub równe docelowej trudności. Proof of Work polega na modyfikacji pola `Nonce` nagłówka bloku lub Coinbase Transaction, aż wynikowy Hash będzie niższy niż wartość docelowa.


Cel ten jest dostosowywany co 2016 bloków (mniej więcej co dwa tygodnie) podczas wydarzenia zwanego "dostosowaniem" Współczynnik trudności jest ponownie obliczany na podstawie czasu potrzebnego do wydobycia poprzednich 2016 bloków. Jeśli łączny czas jest krótszy niż dwa tygodnie, poziom trudności wzrasta poprzez obniżenie wartości docelowej. Jeśli całkowity czas jest dłuższy niż dwa tygodnie, trudność zmniejsza się poprzez dostosowanie celu w górę. Celem jest utrzymanie średniego czasu Mining na poziomie 10 minut na blok. Ten czas między każdym blokiem pomaga zapobiegać podziałom sieci Bitcoin, co skutkuje marnowaniem mocy obliczeniowej. Docelowy poziom trudności znajduje się w nagłówku każdego bloku, w polu `nBits`. Ponieważ pole to jest zredukowane do 32 bitów, a cel ma w rzeczywistości 256 bitów, cel jest skompresowany do mniej precyzyjnego formatu naukowego.


![](../../dictionnaire/assets/34.webp)


> cel trudności jest czasami nazywany "współczynnikiem trudności" W związku z tym może być określany w nagłówkach bloków jako "nBits"