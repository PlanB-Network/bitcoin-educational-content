---
term: Address ÅTERANVÄNDNING
---

Address-återanvändning avser användandet av samma mottagande Address för att blockera flera UTXO:er, ibland inom flera olika transaktioner. Bitcoins är vanligtvis låsta med hjälp av ett kryptografiskt nyckelpar som motsvarar en unik Address. Eftersom Blockchain är offentlig är det lätt att se vilka adresser som är associerade med hur många bitcoins. Om samma Address återanvänds för flera betalningar är det rimligt att tänka sig att alla tillhörande UTXO:er tillhör samma enhet. Därför utgör återanvändning av Address ett problem för användarens integritet. Det möjliggör deterministiska länkar mellan flera transaktioner och UTXO:er, samt upprätthåller spårning av On-Chain-fonder. Satoshi Nakamoto nämnde redan detta problem i sin vitbok:


> "* Som en extra brandvägg kan ett nytt nyckelpar användas för varje transaktion för att förhindra att de kopplas till en gemensam ägare.*" - Nakamoto, S. (2008). "Bitcoin: Ett elektroniskt peer-to-peer-system för kontanter". Konsulteras på https://Bitcoin.org/Bitcoin.pdf.

För att bevara integriteten så långt som möjligt rekommenderas starkt att varje mottagande Address endast används en gång. För varje ny betalning är det lämpligt att generate en ny Address. För förändringsutgångar bör också en ny Address användas. Tack vare deterministiska och hierarkiska plånböcker har det lyckligtvis blivit mycket enkelt att använda en mängd olika adresser. Alla nyckelpar som är associerade med en Wallet kan enkelt regenereras från seed. Det är också därför som Wallet-programvaran alltid genererar en ny, annorlunda Address när du klickar på "Receive"-knappen.


> ► * På engelska kallas det "Address Reuse".*