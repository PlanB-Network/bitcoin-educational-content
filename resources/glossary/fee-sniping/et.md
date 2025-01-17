---
term: FEE SNIPING

---
Ründestsenaarium, mille puhul kaevandajad püüavad ümber kirjutada hiljuti kinnitatud ploki, et nõuda selles sisalduvad tehingutasud, lisades samal ajal mempoolis vahepeal saabunud kõrgete tasudega tehinguid. Selle rünnaku lõppeesmärk on kaevandajate jaoks nende kasumlikkuse suurendamine. Tasude kärpimine võib muutuda üha kasumlikumaks, kui plokkide tasu väheneb ja tehingutasud moodustavad suurema osa kaevurite tuludest. See võib olla kasulik ka siis, kui eelmises plokis sisalduvad tasud on märkimisväärselt kõrgemad kui järgmises parimas kandidaadiplokis. Lihtsustatult öeldes seisab kaevandaja selle valiku ees stiimulite osas:


- Kaevandage normaalselt pärast viimast plokki, suure tõenäosusega võite võita väikese tasu;
- Püüa kaevandada eelmine plokk (tasu sniping), madala tõenäosusega võita kõrge tasu.

See rünnak kujutab endast ohtu Bitcoini süsteemile, sest mida rohkem kaevandajaid võtab selle kasutusele, seda rohkem on teisi, algselt ausaid kaevandajaid motiveeritud sama tegema. Tõepoolest, iga kord, kui uus kaevandaja liitub tasu snaipimist üritavate kaevandajatega, suureneb tõenäosus, et üks ründavatest kaevandajatest õnnestub, ja tõenäosus, et üks ausatest kaevandajatest pikendab ahelat, väheneb vastutasuks. Kui selline rünnak toimub massiliselt ja kestvalt, ei ole plokkide kinnitused enam usaldusväärne näitaja Bitcoini tehingu muutumatuse kohta. See võib muuta süsteemi potentsiaalselt kasutuskõlbmatuks.

Selle riski vastu võitlemiseks täidab enamik rahakoti tarkvara automaatselt välja `nLocktime`, et see seaks tehingu valideerimise tingimuseks järgmise ploki kõrgusesse lisamise. Seega muutub võimatuks tehingu lisamine eelmise ploki ümberkirjutamisel. Kui Bitcoini kasutajad võtavad `nLocktime` laialdaselt kasutusele, vähendab see oluliselt stiimuleid tasude snipeldamiseks. Tõepoolest, see soodustab pigem plokiahela edenemist kui selle ümberkirjutamist, vähendades sellest saadavat potentsiaalset kasu. BIP326 teeb ettepaneku kasutada Taproot-tehingute puhul sarnaselt välja `nSequence`, et saavutada samaväärne mõju kui väljal `nLocktime` muud tüüpi tehingute puhul. Selline kasutamine lööks kaks kärbest ühe hoobiga, parandades ka sama välja kasutavate teise tasandi protokollide privaatsust.