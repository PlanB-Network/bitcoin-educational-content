---
term: Stamps
definition: Protokoll som gör det möjligt att bädda in bilddata i Bitcoins blockkedja via P2MS-transaktioner.
---

Ett protokoll som gör det möjligt att integrera formaterade bilddata direkt i Bitcoin Blockchain genom råa multisignaturtransaktioner (P2MS). Stamps kodar det binära innehållet i en bild i bas 64 och lägger till det till nycklarna i en 1/3 P2MS. En nyckel är riktig och används för att spendera pengarna, medan de andra två är dummy-nycklar (den tillhörande privata nyckeln är okänd) som lagrar data. Genom att koda data direkt som publika nycklar i stället för att använda `OP_RETURN`-utgångar är bilder som lagras med Stamps-protokollet särskilt arbetsintensiva för noderna. Den här metoden skapar flera UTXO:er, vilket ökar storleken på UTXO-uppsättningen och skapar problem för fulla noder.