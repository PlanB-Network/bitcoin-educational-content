---
term: SECP256K1
---

Naam gegeven aan een specifieke elliptische curve gebruikt in het Bitcoin protocol voor de implementatie van de ECDSA (*Elliptic Curve Digital Signature Algorithm*) en Schnorr digitale handtekening algoritmes. De `secp256k1` curve werd gekozen door de uitvinder van Bitcoin, Satoshi Nakamoto. Het heeft een aantal interessante eigenschappen, met name prestatievoordelen.


Het gebruik van `secp256k1` in Bitcoin betekent dat elke private sleutel (een willekeurig 256-bit getal) wordt toegewezen aan een overeenkomstige publieke sleutel door optelling en verdubbeling van het punt van de private sleutel door het generatorpunt van de `secp256k1` curve. Deze operatie is eenvoudig uit te voeren in één richting maar praktisch onmogelijk om te keren, wat de basis vormt van de veiligheid van digitale handtekeningen op Bitcoin.


De `secp256k1` kromme wordt gespecificeerd door de elliptische krommevergelijking $y^2 = x^3 + 7$, wat betekent dat de coëfficiënten $a$ gelijk zijn aan $0$ en $b$ gelijk aan $7$ in de algemene vorm van een elliptische krommevergelijking $y^2 = x^3 + ax + b$. `secp256k1` is gedefinieerd over een eindig veld waarvan de orde een zeer groot priemgetal is, namelijk $p = 2^{256} - 2^{32} - 977$. De kromme heeft ook een groepsvolgorde, dat is het aantal verschillende punten op de kromme, een voorgedefinieerd generator punt (of punt $G$), dat gebruikt wordt in cryptografische operaties om generate sleutelparen, en een cofactor gelijk aan $1$.


> ► *"SEC" staat voor "Standards for Efficient Cryptography". "P256" geeft aan dat de curve gedefinieerd is over een veld $\mathbb{Z}_p$ waar $p$ een 256-bits priemgetal is. "K" verwijst naar de naam van de uitvinder, Neal Koblitz. Tot slot geeft "1" aan dat dit de eerste versie van deze kromme is.*