---
term: MAST
definition: Merkle-träd som grupperar flera spenderingsvillkor där endast ett måste avslöjas för att spendera.
---

Akronym för "Merkelised Alternative Script Tree" En teknik som använder en Merkle Tree för att sammanfatta ett godtyckligt antal utgiftsvillkor som användaren har valt i en mottagande Address, varav ett måste uppfyllas för att spendera de berörda bitcoins. Merkle Tree låter användaren välja vilket villkor som ska uppfyllas utan att avslöja detaljerna i de andra villkoren på Blockchain. Detta bidrar till att minska avgifterna i samband med dessa skript, skapa mycket mer komplexa villkor och med tiden förbättra användarnas integritet (utöver användningen av Schnorr-signaturer). Detta koncept var föremål för flera förslag men lades slutligen till Bitcoin via Taproot Soft Fork under 2021.


> ► *Inledningsvis stod "MAST" för "Merklized Abstract Syntax Tree" Användningen inom ramen för Taproot relaterar inte längre till ett "Abstract Syntax Tree" Användarna fortsatte dock att använda termen MAST. Anthony Towns föreslog därför att den ursprungliga betydelsen skulle ändras samtidigt som denna allmänt använda akronym skulle behållas som: "Merklized Alternative Script Tree."*