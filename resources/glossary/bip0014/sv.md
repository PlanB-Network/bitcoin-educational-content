---
term: BIP0014
definition: Standard som definierar identifikationsformatet för Bitcoin-klienter på nätverket, och skiljer programvaruversioner från protokollversionen.
---

BIP som föreslogs av Patrick Strateman och Amir Taaki 2011 och som syftar till att skilja mellan klientens versionsnummer och protokollversionen. BIP14 specificerar hur Bitcoin-protokollimplementeringar ska presentera sig själva i nätverket. Den föreslår användning av ett user-agent-format för att identifiera versionen och typen av Bitcoin-klient som används. Huvudsyftet med BIP14 är att underlätta hanteringen av ändringar och upptäckten av inkompatibilitet mellan de olika befintliga klienterna. Även om det tidigare var logiskt att betrakta Satoshi:s klient som de facto Bitcoin-protokollet, ledde den stora spridningen av programvara vid denna tidpunkt till att BIP14 tydligt skilde klienterna från själva protokollet.