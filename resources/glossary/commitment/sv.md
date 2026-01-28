---
term: Åtagande
definition: Kryptografiskt objekt som gör det möjligt att bevisa existensen av data utan att avslöja dem.
---

En Commitment (i kryptografisk mening) är ett matematiskt objekt, betecknat $C$, som härleds deterministiskt från en operation på strukturerade data $m$ (meddelandet) och ett slumpmässigt värde $r$. Vi skriver :


$$
C = \text{commit}(m, r)
$$


Denna mekanism består av två huvudsakliga operationer:




- Commit: vi använder en kryptografisk funktion på ett meddelande $m$ och en slumpmässig $r$ för att producera $C$ ;
- Verify: vi använder $C$, $m$-meddelandet och $r$-värdet för att kontrollera att denna Commitment är korrekt. Funktionen returnerar `True` eller `False`.


En Commitment måste respektera två egenskaper:




- Binding: det måste vara omöjligt att hitta två olika meddelanden som ger samma $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Som till exempel :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Dölja: kunskap om $C$ får inte avslöja innehållet i $m$.


I fallet med RGB-protokollet ingår en Commitment i en Bitcoin-transaktion för att bevisa att en viss information finns vid en viss tidpunkt, utan att avslöja själva informationen.