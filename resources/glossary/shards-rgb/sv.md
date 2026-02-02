---
term: Shards (rgb)
definition: Separat gren i DAG-grafen som spårar historiken för en RGB-kontraktsövergång.
---

I samband med RGB-protokollet representerar en Shard en distinkt gren inom den acykliska riktade grafen (DAG) som spårar historiken för en Contract:s tillståndsövergångar. Den utgör en sammanhängande delmängd av uppsättningen övergångar, som t.ex. motsvarar den sekvens av åtgärder som krävs för att intyga giltigheten av en viss tillgång sedan Genesis. Denna mekanism gör det möjligt att isolera specifika segment av den övergripande historiken för att underlätta verifiering på klientsidan.