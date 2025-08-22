---
term: CHECKSUM
---

De checksum is een waarde die wordt berekend uit een set gegevens en die wordt gebruikt om de integriteit en geldigheid van die gegevens te verifiëren tijdens de overdracht of opslag. Controlesomalgoritmen zijn ontworpen om toevallige fouten of onbedoelde wijzigingen in gegevens te detecteren, zoals transmissiefouten of bestandscorruptie. Er bestaan verschillende soorten checksum algoritmen, zoals pariteitscontroles, modulaire checksums, cryptografische Hash functies of BCH (*Bose, Ray-Chaudhuri en Hocquenghem*) codes.


Op Bitcoin worden controlesommen gebruikt op applicatieniveau om de integriteit van ontvangen adressen te waarborgen. Een controlesom wordt berekend uit de payload van de Address van een gebruiker en vervolgens toegevoegd aan die Address om fouten in de invoer te detecteren. Een controlesom is ook aanwezig in herstelzinnen (mnemonics).


> ► *Het is algemeen aanvaard om de Engelse term "checksum" rechtstreeks in het Frans te gebruiken.*