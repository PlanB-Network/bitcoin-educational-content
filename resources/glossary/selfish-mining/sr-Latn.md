---
term: SEBIČNI Mining
---

Strategija (ili napad) u Mining, gde Miner ili grupa rudara namerno zadržava blokove sa važećim Proof of Work bez trenutnog objavljivanja na mreži. Cilj je da budu ispred drugih rudara u smislu Proof of Work, što im potencijalno omogućava da Miner nekoliko blokova zaredom i objave ih sve odjednom, čime maksimiziraju svoje dobitke. Drugim rečima, napadačka grupa rudara ne rudari na poslednjem bloku koji je validirala cela mreža, već na bloku koji su sami kreirali, a koji se razlikuje od onog koji je validiran od strane mreže.


Ovaj proces generiše neku vrstu tajne grane Blockchain, koja ostaje nepoznata celoj mreži sve dok ovaj alternativni lanac potencijalno ne premaši pošteni Blockchain. Kada tajni lanac napadačkih rudara postane duži (tj. sadrži više akumuliranog rada) od poštenog, javnog lanca, tada se emituje celoj mreži. U tom trenutku, čvorovi u mreži koji prate najduži lanac (sa najviše akumuliranog rada) će se sinhronizovati sa ovim novim lancem. Tako dolazi do reorganizacije.


Mining sebičnost je dosadna za korisnike, jer smanjuje sigurnost sistema trošeći deo računarske snage mreže. Ako je uspešna, takođe dovodi do Blockchain reorganizacija, što utiče na pouzdanost potvrda transakcija za korisnike. Ipak, ova praksa ostaje rizična za napadačku grupu rudara, jer je često isplativije Miner normalno iznad poslednjeg javno poznatog bloka nego alocirati računarsku snagu na tajnu granu koja verovatno nikada neće premašiti pošteni Blockchain. Što je veći broj blokova u reorganizaciji, manja je verovatnoća uspešnog napada.