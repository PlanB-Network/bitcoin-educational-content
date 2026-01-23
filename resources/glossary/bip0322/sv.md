---
term: BIP0322
definition: Ny standard för meddelandesignering kompatibel med alla skripttyper, som ersätter BIP137.
---

Föreslår en ny standard för att ersätta BIP137 för att signera meddelanden med Bitcoin privata nycklar och deras tillhörande adresser, för att bevisa Ownership för en Address. Dessa signaturer är användbara för olika applikationer såsom bevis på medel, revision och andra användningar som kräver autentisering av en Address via dess privata nyckel. Jämfört med BIP137 utökar BIP322 standarden för meddelandesignering bortom traditionella adresser genom att använda ett tillvägagångssätt baserat på skript. Det gör det möjligt för Wallet-programvara att signera ett meddelande för alla skript som de kan låsa upp för att spendera bitcoins. För att göra detta innebär metoden att man signerar en text genom att producera en signatur för en virtuell Bitcoin-transaktion. För traditionella P2PKH-adresser förblir BIP322 kompatibel med det traditionella signaturformatet.