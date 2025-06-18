---
term: LOGARYTM DYSKRETNY
---

Logarytm dyskretny to problem matematyczny, który jest wykorzystywany w niektórych algorytmach kryptograficznych klucza publicznego. W grupie cyklicznej rzędu $q$, z generatorem $g$, jeśli mamy równanie postaci $g^x = h$, to $x$ nazywamy logarytmem dyskretnym $h$ względem podstawy $g$, modulo $q$. Mówiąc prościej, polega to na określeniu wykładnika $x$, gdy znane są $g$, $h$ i $q$. Logarytm dyskretny jest więc odwrotnością wykładnika w skończonej grupie cyklicznej. Jednakże, dla dużych wartości $q$, rozwiązanie problemu logarytmu dyskretnego jest uważane za algorytmicznie trudne. Właściwość ta jest wykorzystywana do zapewnienia bezpieczeństwa wielu protokołów kryptograficznych, takich jak protokół Diffiego-Hellmana dla klucza Exchange.


Logarytm dyskretny jest również wykorzystywany w kryptografii krzywych eliptycznych (ECC), w tym w ECDSA (*Elliptic Curve Digital Signature Algorithm*). W kontekście krzywych eliptycznych, problem logarytmu dyskretnego rozciąga się na znalezienie skalara $k$ takiego, że $k \cdot G = K$, gdzie $G$ i $K$ są punktami na krzywej, a $\cdot$ reprezentuje operację mnożenia punktów. W kontekście Bitcoin skrypty mogą używać ECDSA lub protokołu Schnorra do blokowania UTXO. Oba opierają się na niewykonalności obliczania logarytmu dyskretnego.