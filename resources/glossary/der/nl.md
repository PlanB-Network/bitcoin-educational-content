---
term: DER
definition: Standaard binair coderingsformaat gebruikt voor ECDSA-handtekeningen op Bitcoin.
---

Acroniem voor *Distinguished Encoding Rules*. Het is een strikte subset van de ASN.1-coderingsregels die zijn gedefinieerd in de specificatie [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) en wordt gebruikt om elk type gegevens te coderen in een binaire reeks. DER wordt voornamelijk gebruikt op specifieke gebieden, zoals cryptografie, waar gegevens op een standaard, voorspelbare manier moeten worden gecodeerd.


Op Bitcoin worden ECDSA-handtekeningen in DER formaat gecodeerd. Ze bestaan uit twee gecodeerde getallen van 32 bytes (`r`,`s`). Het formaat van de handtekening bestaat uit de volgende Elements (71 bytes):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Met :




- 0x30` (1 byte): identificator van een samengestelde structuur;
- length` (1 byte): lengte van de volgende gegevens ;
- 0x02` (1 byte): gegevensidentificatiesymbool type `INTEGER` (geheel getal) ;
- `r-lengte` (1 byte): lengte van de volgende `r` waarde (32 bytes) ;
- r` (32 bytes): waarde van `r` als een big-endian geheel getal;
- 0x02` (1 byte): gegevensidentificatiesymbool type `INTEGER` (geheel getal) ;
- `s-lengte` (1 byte): lengte van de volgende `s` waarde (32 bytes) ;
- `s` (32 bytes): `s` waarde als een big-endian geheel getal.


In een Bitcoin transactie wordt aan het eind van een DER handtekening een byte toegevoegd om het gebruikte type SigHash aan te geven.