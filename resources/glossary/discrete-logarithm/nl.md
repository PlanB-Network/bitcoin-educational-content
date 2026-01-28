---
term: Discrete logaritme
definition: Moeilijk op te lossen wiskundig probleem dat de basis vormt van de cryptografische beveiliging van Bitcoin.
---

De discrete logaritme is een wiskundig probleem dat gebruikt wordt in sommige cryptografische algoritmen met een openbare sleutel. In een cyclische groep van orde $q$, met een generator $g$, als men een vergelijking heeft van de vorm $g^x = h$, dan heet $x$ de discrete logaritme van $h$ met betrekking tot de basis $g$, modulo $q$. Eenvoudig gezegd gaat het erom de exponent $x$ te bepalen als $g$, $h$ en $q$ bekend zijn. De discrete logaritme is dus de inverse van de exponentiaal in een eindige cyclische groep. Voor grote waarden van $q$ wordt het oplossen van het discrete logaritmeprobleem echter als algoritmisch moeilijk beschouwd. Deze eigenschap wordt gebruikt om de veiligheid van veel cryptografische protocollen te garanderen, zoals het Diffie-Hellman-protocol voor Exchange-sleutels.


De discrete logaritme wordt ook gebruikt in elliptische curve cryptografie (ECC), onder andere in de ECDSA (*Elliptic Curve Digital Signature Algorithm*). In de context van elliptische krommen breidt het probleem van de discrete logaritme zich uit tot het vinden van een scalair $k$ zodanig dat $k \cdot G = K$, waarbij $G$ en $K$ punten op de kromme zijn, en $k \cdot$ de puntvermenigvuldigingsoperatie voorstelt. In de context van Bitcoin kunnen scripts ECDSA of het Schnorr protocol gebruiken om UTXO's te vergrendelen. Beide berusten op de onmogelijkheid om de discrete logaritme te berekenen.