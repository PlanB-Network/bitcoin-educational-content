---
term: Segwit
definition: Uppdatering från 2017 som separerar signaturer för att öka kapaciteten och lösa malleability.
---

SegWit, en akronym för "Segregated Witness", är en uppdatering av Bitcoin-protokollet som introducerades i augusti 2017. Syftet är att lösa flera tekniska problem, bland annat problemet med nätverkets transaktionskapacitet, problemet med transaktionernas formbarhet och att underlätta framtida protokolländringar.


Denna Soft Fork ändrar transaktionsstrukturen genom att flytta signaturdata till en separat katalog. Med SegWit tas signaturerna bort från huvudblocket och läggs in i en separat datastruktur i slutet av blocket, som kallas vittnen. Denna separation gör det möjligt att öka kapaciteten för varje block utan att ändra den maximala blockstorleken, som är 1 MB på Bitcoin. Den här förändringen löser också problemet med transaktionernas formbarhet. Före SegWit kunde signaturer ändras innan en transaktion bekräftades, vilket ändrade transaktionsidentifieraren. Detta gjorde det svårt att konstruera komplexa transaktioner, eftersom en obekräftad transaktion kunde få sin identifierare ändrad. Genom att separera signaturerna gör SegWit att transaktionerna inte kan manipuleras, eftersom en ändring av signaturerna nu bara påverkar vittnesidentifieraren (WTXID), inte transaktionsidentifieraren (txid). Genom att lösa problemet med manipulerbarhet har SegWit banat väg för ytterligare utveckling utöver Bitcoin-systemet, i synnerhet Lightning Network, som möjliggör snabba och billiga transaktioner.