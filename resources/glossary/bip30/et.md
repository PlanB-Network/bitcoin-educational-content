---
term: BIP30

---
Parandusettepanek, mis hõlmab 15. märtsil 2012 rakendatud soft forki, et lahendada topelt tehingu identifikaatorite probleem. Enne BIP30 oli tehniliselt võimalik, et plokiahelas oli kaks erinevat tehingut ühe ja sama tehingu identifikaatoriga (TXID). Seda juhtus eelkõige kaks korda coinbase'i tehingute puhul: plokis 91,880 on sama TXID kui ploki 91,722 coinbase'i tehingul ja plokis 91,842 on sama TXID kui ploki 91,812 coinbase'i tehingul. BIP30 lahendas selle vea, kehtestades uue lihtsa reegli: ühelgi uuel tehingul ei saa olla sama TXID kui varem salvestatud tehingul, välja arvatud juhul, kui esialgne tehing on täielikult ära kasutatud (st kõik selle väljundid on kasutatud). See soft fork aktiveeriti lipupäeva meetodi abil. Seega on see üks esimesi UASFi.