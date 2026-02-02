---
term: Nonce
definition: Nummer som används endast en gång, modifierat av miners för att hitta en giltig blockhash.
---

I datorsammanhang avser termen "Nonce" ett tal som bara används en gång och sedan ersätts. Det är ofta slumpmässigt eller pseudoslumpmässigt. Nonces används i olika kryptografiska protokoll för att garantera säkerheten i processen. ECDSA-signaturerna som används i Bitcoin-protokollet inkluderar till exempel användningen av en Nonce. Detta innebär att detta nummer måste vara nytt för varje signatur. Om så inte är fallet är det möjligt att beräkna den privata nyckel som används genom att jämföra två signaturer som använder samma Nonce.


Nonces används också i Bitcoin Mining-processen. Miners inkrementerar dessa modifierbara värden i sina kandidatblock. De modifierar Nonce-värdet för att hitta en kryptografisk Hash som är lägre än eller lika med svårighetsmålet. Denna process kräver betydande beräkningskraft, eftersom den innebär en uttömmande sökning bland ett stort antal möjliga nonces. När en Miner hittar en Nonce som, när den inkluderas i deras block, ger en sammanställning som uppfyller svårighetskriterierna, sänds blocket till nätverket och Miner vinner belöningen.


> ► * 2010 upptäckte forskare att Sonys PlayStation 3 använde samma Nonce vid signering av olika kodpaket. Denna återanvändning av Nonce gjorde det möjligt för angripare att beräkna den privata nyckel som användes för att signera programvaran. Med den privata nyckeln i handen kunde angriparna skapa giltiga signaturer för vilken kod som helst, vilket gjorde det möjligt för dem att köra obehörig programvara, inklusive piratkopierade spel eller anpassade operativsystem, direkt på PS3.*

> ► *Det finns en vanlig missuppfattning om ursprunget till termen "Nonce". Vissa hävdar att det är en förkortning av "nummer som bara används en gång". I själva verket går ordets ursprung tillbaka till 1700-talet och kommer från den semantiska utvecklingen av det fornengelska uttrycket "then anes", som betydde "för tillfället".*