---
term: Härledning
definition: Process för att generera barnnycklar från ett föräldra-nyckelpar i en HD-plånbok.
---

Avser processen att generera underordnade nyckelpar från ett överordnat nyckelpar (privat nyckel och publik nyckel) och en chain code inom en deterministisk och hierarkisk (HD) Wallet. Denna process gör det möjligt att segmentera grenar och organisera en Wallet i olika nivåer med många underordnade nyckelpar, som alla kan återställas genom att endast känna till den grundläggande återställningsinformationen (Mnemonic-frasen och alla potentiella passphrase). För att härleda en underordnad nyckel används funktionen `HMAC-SHA512` med den överordnade chain code och sammankopplingen av den överordnade nyckeln och ett 32-bitars index. Det finns två typer av härledningar:


- Normal härledning, där den överordnade offentliga nyckeln används som grund för funktionen `HMAC-SHA512`;
- Härdad härledning, som använder den överordnade privata nyckeln som grund för funktionen `HMAC-SHA512`;


Resultatet av HMAC-SHA512 delas upp i två: de första 256 bitarna blir barnets nyckel (privat eller offentlig efter bearbetning genom ECDSA), och de återstående 256 bitarna blir barnets chain code.