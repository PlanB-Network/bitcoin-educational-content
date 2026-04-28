---
term: Silent payments
definition: Methode voor het ontvangen van betalingen via een statisch adres zonder adreshergebruik.
---

Methode voor het gebruik van statische Bitcoin adressen om betalingen te ontvangen zonder hergebruik van Address, zonder interactie en zonder een zichtbare On-Chain koppeling tussen de verschillende betalingen en de statische Address. Deze techniek elimineert de noodzaak om generate nieuwe, ongebruikte ontvangstadressen te geven voor elke transactie, en vermijdt zo de gebruikelijke interacties in Bitcoin waarbij de ontvanger een nieuwe Address moet geven aan de betaler.


Bij Stille Betalingen gebruikt de betaler de publieke sleutels van de ontvanger (openbare sleutel uitgeven en openbare sleutel scannen) en de som van hun eigen privésleutels als input voor generate een nieuwe Address voor elke betaling. Alleen de ontvanger kan met zijn privé-sleutels de privé-sleutel berekenen die overeenkomt met deze betaling Address. ECDH (*Elliptic-Curve Diffie-Hellman*), een cryptografisch Exchange sleutelalgoritme, wordt gebruikt om een gedeeld geheim vast te stellen dat vervolgens wordt gebruikt om de ontvangende Address en de privésleutel af te leiden (alleen aan de kant van de ontvanger). Om de Stille Betalingen die voor hen bestemd zijn te identificeren, moeten ontvangers de Blockchain scannen en elke transactie onderzoeken die aan de criteria van het protocol voldoet. In tegenstelling tot BIP47, dat een kennisgevingstransactie gebruikt om het betalingskanaal tot stand te brengen, elimineren Stille Betalingen deze stap en besparen zo een transactie. Het compromis is echter dat de ontvanger alle potentiële transacties moet scannen om, door toepassing van ECDH, te bepalen of ze voor hem bestemd zijn.


Bijvoorbeeld, Bob's statische Address $B$ vertegenwoordigt de aaneenschakeling van zijn openbare sleutel voor scannen en zijn openbare sleutel voor uitgeven:


$$ B = B_{{scan}} \‖ } B_{{uitgaven}} $$


Deze sleutels zijn eenvoudigweg afgeleid van het volgende pad:


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


Deze statische Address wordt uitgegeven door Bob. Alice haalt het op om een Stille Betaling aan Bob te doen. Ze berekent Bob's betaling Address $P_0$ op deze manier:


$$ P_0 = B_{{spend}} + \text{Hash}(\text{inputHash} \cdot a \cdot B_{scan}} \text{ ‖ } 0) \cdot G $$


Waar:


$$ \text{inputHash} = \text{Hash}(\text{outpoint}_L \text{ ‖ } A) $$


Met:


- $B_{{scan}}$: Bob's openbare sleutel voor scannen (statische Address);
- $B_{{spend}}$: Bob's openbare sleutel voor uitgaven (statisch Address);
- $A$: De som van de openbare sleutels in de invoer (tweak);
- $a$: De privésleutel van de tweak, dat wil zeggen de som van alle sleutelparen die gebruikt zijn in de `scriptPubKey` van de UTXO's die als invoer gebruikt zijn in de transactie van Alice;
- tekst{uitgangspunt}_L$: De kleinste UTXO (lexicografisch) die wordt gebruikt als invoer in de transactie van Alice;
- ‖ }$: Aaneenschakelen (de bewerking om operanden eind aan eind samen te voegen);
- $G$: Het generatorpunt van de elliptische kromme `secp256k1`;
- tekst{Hash}$: De SHA256 Hash functie gelabeld met `BIP0352/SharedSecret`;
- $P_0$: De eerste publieke sleutel / uniek Address voor betaling aan Bob;
- $0$: Een geheel getal dat wordt gebruikt om meerdere unieke betalingsadressen generate te maken.


Bob scant de Blockchain om zijn Stille Betaling op deze manier te vinden:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{{scan}} \cdot A \text{ ‖ } 0) \cdot G $$


Met:


- $b_{{scan}}$: Bob's private scansleutel.


Als hij $P_0$ vindt als een Address met een Stille Betaling aan hem geadresseerd, berekent hij $p_0$, de privésleutel waarmee hij het geld kan uitgeven dat Alice naar $P_0$ heeft gestuurd:


$$ p_0 = (b_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{{scan}} \cdot A \text{ ‖ } 0)) \mod n $$


Met:


- $b_{{spend}}$: Bob's private bestedingssleutel;
- $n$: de orde van de elliptische kromme `secp256k1`.


Naast deze basisversie kunnen labels ook gebruikt worden om generate verschillende statische adressen van dezelfde statische basis Address te scheiden, met als doel om meerdere toepassingen te scheiden zonder het werk dat nodig is tijdens het scannen onredelijk te vermenigvuldigen.