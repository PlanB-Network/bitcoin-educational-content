---
term: STONEWALL X2
---

Specifičan oblik Bitcoin transakcije usmeren na povećanje privatnosti korisnika tokom trošenja, kroz saradnju sa trećom stranom koja nije uključena u trošak. Ova metoda simulira mini-CoinJoin između dva učesnika, dok se vrši plaćanje trećoj strani. Stonewall x2 transakcije su dostupne na obe Samourai Wallet aplikaciji i Sparrow Wallet softveru (oba su interoperabilna).


Njegovo funkcionisanje je relativno jednostavno: koristi UTXO koji posedujemo za izvršenje plaćanja i traži pomoć treće strane koja takođe doprinosi sa UTXO koji poseduju. Transakcija se završava sa četiri izlaza: dva od njih su jednake sume, jedan namenjen za Address primaoca plaćanja, drugi za Address koji pripada saradniku. Treći UTXO se vraća na drugi Address saradnika, omogućavajući im da povrate početni iznos (neutralna akcija za njih, minus Mining naknade), a poslednji UTXO se vraća na Address koji posedujemo, što predstavlja kusur od plaćanja. Tako se definišu tri različite uloge u Stonewall x2 transakcijama:


- Pošiljalac, koji vrši efektivnu uplatu;
- Saradnik, koji obezbeđuje bitkoine kako bi poboljšao ukupnu anonimnost transakcije, dok u potpunosti povrati svoja sredstva na kraju;
- Primalac, koji možda nije svestan specifične prirode transakcije i jednostavno čeka uplatu od pošiljaoca.


![](../../dictionnaire/assets/3.webp)


Stonewall x2 struktura dodaje mnogo entropije transakciji i zamagljuje tragove analize lanca. Sa spoljašnje strane, takva transakcija može biti interpretirana kao mali CoinJoin između dve osobe. Ali u stvarnosti, to je plaćanje. Ova metoda stoga generiše nesigurnosti u analizi lanca, ili čak vodi ka lažnim tragovima. Čak i ako spoljni posmatrač uspe da identifikuje obrazac Stonewall x2 transakcije, neće imati sve informacije. Neće moći da odredi koji od dva UTXO-a jednake vrednosti odgovara plaćanju. Štaviše, neće moći da zna ko je izvršio plaćanje. Na kraju, neće moći da utvrdi da li dva ulazna UTXO-a dolaze od dve različite osobe ili pripadaju jednoj osobi koja ih je spojila. Ova poslednja tačka je zbog činjenice da klasične Stonewall transakcije prate potpuno isti obrazac kao Stonewall x2 transakcije. Sa spoljašnje strane i bez dodatnih informacija o kontekstu, nemoguće je razlikovati Stonewall transakciju od Stonewall x2 transakcije. Međutim, prve nisu kolaborativne transakcije, dok druge jesu. Ovo dodaje još više sumnje u vezi sa troškovima.