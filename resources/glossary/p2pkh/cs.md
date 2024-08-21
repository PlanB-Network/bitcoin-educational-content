---
term: P2PKH
---

P2PKH znamená *Pay to Public Key Hash* (Platba na hash veřejného klíče). Jedná se o standardní skriptový model používaný k určení podmínek výdaje pro UTXO. Umožňuje uzamknout bitcoiny na hash veřejného klíče, tedy na přijímací adresu. Tento skript je spojen se standardem Legacy a byl zaveden v raných verzích Bitcoinu Satoshi Nakamotem.

Na rozdíl od P2PK, kde je veřejný klíč explicitně zahrnut do skriptu, P2PKH používá kryptografický otisk veřejného klíče. Tento skript obsahuje hash `RIPEMD160` z `SHA256` veřejného klíče a stanoví, že pro přístup k prostředkům musí příjemce poskytnout veřejný klíč, který se shoduje s tímto hashem, stejně jako platný digitální podpis vygenerovaný z přidruženého soukromého klíče. Adresy P2PKH jsou kódovány pomocí formátu `Base58Check`, což jim dává robustnost proti typografickým chybám prostřednictvím použití kontrolního součtu. Tyto adresy vždy začínají číslem `1`.