---
term: SegWit
---

SegWit, akronim za "Segregated Witness," je ažuriranje Bitcoin protokola uvedeno u avgustu 2017. godine. Cilj mu je rešavanje nekoliko tehničkih problema, uključujući problem kapaciteta transakcija mreže, problem promenljivosti transakcija i olakšavanje budućih izmena protokola.


Ovaj Soft Fork modifikuje strukturu transakcije premještanjem podataka o potpisu u poseban direktorijum. Konkretno, sa SegWit, potpisi se uklanjaju iz glavnog bloka i ubacuju u posebnu strukturu podataka na kraju bloka, poznatu kao svjedoci. Ovo razdvajanje omogućava povećanje kapaciteta svakog bloka bez promjene maksimalne veličine bloka, koja je 1 MB na Bitcoin. Ova promjena takođe rješava problem promjenljivosti transakcija. Prije SegWit, potpisi su mogli biti izmijenjeni prije nego što je transakcija potvrđena, što je mijenjalo identifikator transakcije. Ovo je otežavalo konstrukciju složenih transakcija, jer je nepotvrđena transakcija mogla imati promijenjen identifikator. Razdvajanjem potpisa, SegWit čini transakcije nepromjenljivim, jer svaka promjena u potpisima sada utiče samo na identifikator svjedoka (WTXID), a ne na identifikator transakcije (txid). Rješavanjem problema promjenljivosti, SegWit je otvorio put za dalji razvoj na vrhu Bitcoin sistema, posebno Lightning Network, koji omogućava brze i niskotarifne transakcije.