---
term: ECDSA
definition: Elliptic Curve Digital Signature Algorithm gebruikt op Bitcoin om transacties te ondertekenen.
---

Acroniem voor "Elliptic Curve Digital Signature Algorithm" Het is een algoritme voor digitale handtekeningen gebaseerd op cryptografie met elliptische kromme (ECC). Het is een variant van DSA (Digital Signature Algorithm). ECDSA maakt gebruik van de eigenschappen van elliptische krommen om beveiligingsniveaus te bieden die vergelijkbaar zijn met die van traditionele openbare sleutelalgoritmen, zoals RSA, terwijl de sleutel aanzienlijk kleiner is. Met ECDSA kunnen sleutelparen (publieke en private sleutels) worden gegenereerd en digitale handtekeningen worden aangemaakt en geverifieerd.


In de context van Bitcoin wordt ECDSA gebruikt om publieke sleutels af te leiden van private sleutels. Het wordt ook gebruikt om transacties te ondertekenen, om te voldoen aan een script om bitcoins te ontgrendelen en uit te geven. De elliptische curve die gebruikt wordt in Bitcoin's ECDSA is `secp256k1`, gedefinieerd door de vergelijking $y^2 = x^3 + 7$. Dit algoritme is gebruikt sinds de start van Bitcoin in 2009. Tegenwoordig deelt het zijn plaats met het Schnorr protocol, een ander algoritme voor digitale handtekeningen dat in 2021 met Taproot werd geïntroduceerd.