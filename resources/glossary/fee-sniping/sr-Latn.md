---
term: FEE SNIPING
---

Scenarij napada u kojem rudari pokušavaju da prepišu nedavno potvrđeni blok kako bi preuzeli naknade za transakcije koje sadrži, dok dodaju transakcije sa visokim naknadama koje su u međuvremenu stigle u Mempool. Krajnji cilj ovog napada za Miner je povećanje njihove profitabilnosti. Fee sniping može postati sve isplativiji kako se Block reward smanjuje, a naknade za transakcije predstavljaju veći deo prihoda rudara. Takođe može biti korisno kada su naknade sadržane u prethodnom bloku značajno veće od onih u sledećem najboljem kandidatskom bloku. Da pojednostavimo, Miner se suočava sa ovim izborom u smislu podsticaja:


- Rudari na normalan način prateći poslednji blok, sa velikom verovatnoćom osvajanja niske nagrade;
- Pokušaj rudarenja prethodnog bloka (fee sniping), sa malom verovatnoćom osvajanja visoke nagrade.


Ovaj napad predstavlja rizik za Bitcoin sistem, jer što ga više rudara usvoji, to su više drugi rudari, koji su u početku pošteni, motivisani da urade isto. Zaista, svaki put kada se novi Miner pridruži onima koji pokušavaju fee sniping, verovatnoća da jedan od napadačkih rudara uspe raste, a verovatnoća da jedan od poštenih rudara produži lanac opada zauzvrat. Ako se ovaj napad masovno sprovede i održi tokom vremena, potvrde blokova više ne bi bile pouzdan pokazatelj nepromenljivosti Bitcoin transakcije. To bi potencijalno moglo učiniti sistem neupotrebljivim.


Da bi se suprotstavili ovom riziku, većina Wallet softvera automatski popunjava polje `nLocktime` tako da uslovljava validaciju transakcije uključivanjem u sledeću visinu bloka. Tako postaje nemoguće uključiti transakciju u prepravku prethodnog bloka. Ako široka upotreba `nLocktime` bude usvojena od strane Bitcoin korisnika, to značajno smanjuje podsticaje za fee sniping. Zaista, to podstiče napredovanje Blockchain umesto njegovog prepravljanja smanjenjem potencijalnih profita od toga. Za Taproot transakcije, BIP326 predlaže korišćenje polja `nSequence` na sličan način kako bi se postigao ekvivalentan efekat polja `nLocktime` za druge tipove transakcija. Ova upotreba bi ubila dve muve jednim udarcem takođe poboljšavajući privatnost second-Layer protokola koji koriste isto polje.