---
term: BIP0034

definition: Soft fork vyžadující zahrnutí výšky bloku do coinbase transakce, což zaručuje jedinečnost každého bloku.
---
Soft fork byl použit v březnu 2013, počínaje blokem 227 930, který zavedl verzi 2 pro bloky Bitcoinu. Tato nová verze vyžaduje, aby každý blok obsahoval v `scriptSig` transakce coinbase výšku vytvářeného bloku. Tato změna slouží k vyjasnění způsobu, jakým se síť dohodne na úpravě struktury bloků a pravidel konsensu. Navíc prosazuje jedinečnost každého bloku a každé transakce coinbase.