---
term: LIBSECP256K1
---

Hoogperformante, hoog-veilige C bibliotheek voor digitale handtekeningen en andere cryptografische primitieven op de `secp256k1` elliptische curve. Aangezien deze curve nooit veel gebruikt is buiten Bitcoin (in tegenstelling tot de vaak geprefereerde `secp256r1` curve), heeft deze bibliotheek als doel de meest uitgebreide referentie te zijn voor het gebruik ervan. De ontwikkeling van libsecp256k1 was primair gericht op de behoeften van Bitcoin, en functies bedoeld voor andere toepassingen zijn mogelijk minder getest of geverifieerd. Passend gebruik van deze bibliotheek vereist zorgvuldige aandacht, om er zeker van te zijn dat het geschikt is voor de specifieke doeleinden van andere toepassingen dan Bitcoin.


De libsecp256k1 bibliotheek biedt een verscheidenheid aan mogelijkheden, waaronder:




- ECDSA-secp256k1-handtekening en -verificatie en genereren van cryptografische sleutels ;
- Additieve en multiplicatieve bewerkingen op geheime en openbare sleutels ;
- Serialisatie en analyse van geheime sleutels, openbare sleutels en handtekeningen ;
- Ondertekening en generatie van openbare sleutels in constante tijd met constante geheugentoegang;
- En een heleboel andere cryptografische primitieven.