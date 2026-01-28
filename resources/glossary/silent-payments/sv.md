---
term: Silent payments
definition: Metod för att ta emot betalningar via en statisk adress utan adressåteranvändning.
---

Metod för att använda statiska Bitcoin-adresser för att ta emot betalningar utan återanvändning av Address, utan interaktion och utan en synlig On-Chain-länk mellan de olika betalningarna och den statiska Address. Denna teknik eliminerar behovet av att generate nya, oanvända mottagningsadresser för varje transaktion, och därmed undviks de vanliga interaktionerna i Bitcoin där mottagaren måste tillhandahålla en ny Address till betalaren.


Med Silent Payments använder betalaren mottagarens publika nycklar (spend public key och scan public key) och summan av sina egna privata nycklar som indata till generate en ny Address för varje betalning. Endast mottagaren, med sina privata nycklar, kan beräkna den privata nyckeln som motsvarar denna betalning Address. ECDH (*Elliptic-Curve Diffie-Hellman*), en kryptografisk nyckel Exchange-algoritm, används för att upprätta en delad hemlighet som sedan används för att härleda den mottagande Address och den privata nyckeln (endast på mottagarens sida). För att identifiera de Tysta betalningar som är avsedda för dem måste mottagarna skanna Blockchain och undersöka varje transaktion som matchar protokollets kriterier. Till skillnad från BIP47, som använder en aviseringstransaktion för att upprätta betalningskanalen, eliminerar Silent Payments detta steg och sparar en transaktion. Kompromissen är dock att mottagaren måste skanna alla potentiella transaktioner för att genom att tillämpa ECDH avgöra om de är adresserade till dem.


Bob:s statiska Address $B$ representerar t.ex. sammankopplingen av hans offentliga nyckel för skanning och hans offentliga nyckel för utgifter:


$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$


Dessa nycklar är helt enkelt härledda från följande väg:


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


Denna statiska Address publiceras av Bob. Alice hämtar den för att göra en tyst betalning till Bob. Hon beräknar Bob:s betalning Address $P_0$ på detta sätt:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$$


Var?


$$ \text{inputHash} = \text{Hash}(\text{outpoint}_L \text{ ‖ } A) $$


Med:


- $B_{\text{scan}}$: Bob:s offentliga nyckel för skanning (statisk Address);
- $B_{\text{spend}}$: Bob:s offentliga nyckel för utgifter (statisk Address);
- $A$: Summan av de publika nycklarna i inmatningen (tweak);
- $a$: Tweakens privata nyckel, dvs. summan av alla nyckelpar som används i `scriptPubKey` för de UTXO:er som förbrukas som insatsvaror i Alice:s transaktion;
- $\text{utpunkt}_L$: Den minsta UTXO (lexikografiskt) som används som input i Alice:s transaktion;
- $\text{ ‖ }$: Konkatenering (sammanfogning av operander från början till slut);
- $G$: Generatorpunkten för den elliptiska kurvan `secp256k1`;
- $\text{Hash}$: SHA256 Hash-funktionen taggad med `BIP0352/SharedSecret`;
- $P_0$: Den första publika nyckeln / unika Address för betalning till Bob;
- $0$: Ett heltal som används för att generate flera unika betalningsadresser.


Bob skannar Blockchain för att hitta sin tysta betalning på detta sätt:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$$


Med:


- $b_{\text{scan}}$: Bob:s privata skanningnyckel.


Om han hittar $P_0$ som en Address innehållande en tyst betalning adresserad till honom, beräknar han $p_0$, den privata nyckeln som gör det möjligt för honom att spendera de medel som skickats av Alice till $P_0$:


$$ p_0 = (b_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$$


Med:


- $b_{\text{spendera}}$: Bob:s privata utgiftsnyckel;
- $n$: ordningen på den elliptiska kurvan `secp256k1`.


Utöver denna grundläggande version kan etiketter också användas för att generate flera olika statiska adresser från samma grundläggande statiska Address, i syfte att separera flera användningsområden utan att orimligt multiplicera det arbete som krävs vid skanning.