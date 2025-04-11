---
term: P2PKH

---
P2PKH je zkratka pro *Pay to Public Key Hash*. Jedná se o standardní model skriptu, který se používá pro stanovení podmínek výdajů na UTXO. Umožňuje uzamknout bitcoiny na hash veřejného klíče, tedy na přijímací adresu. Tento skript je spojen se standardem Legacy a byl zaveden v raných verzích Bitcoinu Satoshi Nakamotem.

Na rozdíl od P2PK, kde je veřejný klíč explicitně obsažen ve skriptu, P2PKH používá kryptografický otisk veřejného klíče. Tento skript obsahuje hash `RIPEMD160` veřejného klíče `SHA256` a stanoví, že pro přístup k prostředkům musí příjemce poskytnout veřejný klíč, který odpovídá tomuto hashi, a také platný digitální podpis vygenerovaný z přidruženého soukromého klíče. Adresy P2PKH jsou kódovány pomocí formátu `Base58Check`, který jim díky použití kontrolního součtu zajišťuje odolnost proti překlepům. Tyto adresy vždy začínají číslem `1`.