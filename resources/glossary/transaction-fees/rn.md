---
term: Amafaranga y'urungano
definition: Amafaranga arihwa abaminer kugira ngo bashyire itunshwa ry'amafaranga mu gitabo, akaba ari ikinyuranyo hagati y'ayinjira n'ayasohoka.
---

Amafaranga y’ugucuruza agereranya amahera afise intumbero yo gusubiza abacukuzi b’amabuye y’agaciro kubera uruhara rwabo mu buryo bwa Proof of Work. Ivyo bihembo biremesha abacukuzi gushiramwo amafaranga mu bice barema. Biva ku ntandukaniro iri hagati y’umubare wose w’ibintu vyinjizwa n’umubare wose w’ibintu bisohoka mu gucuruza:


```text
fees = inputs - outputs
```


Bigaragazwa muri `Sats/vBytes`, bisobanura ko amafaranga atavana n’ingero y’ama bitcoins yoherejwe, ahubwo ava ku buremere bw’ivyo ugurisha. Bitoranywa mu mwidegemvyo n’uwurungitse igicuruzwa kandi bikagena umuvuduko wo kwinjira mu gice c’ibintu biciye ku buryo bwo gucapura. Nk’akarorero, reka tuvuge ko nkora igikorwa nkoresheje inyungu ya `100.000 Sats`, inyungu ya `40.000 Sats`, n’iyindi nkuru ya `58.500 Sats`. Ivyo bikoresho vyose hamwe ni `98.500 Sats`. Amafaranga agenewe iyo nzira ni `1.500 Sats`. Miner irimwo ivy’ugucuruza vyanje ishobora kurema `1.500 Sats` muri Coinbase Transaction yabo muri Exchange ku `1.500 Sats` ntasubiye mu bisohoka vyanje.


Ibikorwa vy’ubudandaji bifise amafaranga menshi, ugereranije n’ubunini bwavyo, bifatwa nk’ivy’imbere n’abacukuzi, ivyo bikaba bishobora kwihutisha igikorwa co kwemeza. Ku rundi ruhande, amafaranga y’ubudandaji afise amahera make yoshobora guteba mu bihe vy’ugucumbagira cane. Birabereye kumenya ko amafaranga y’ugucuruza Bitcoin atandukanye n’infashanyo y’amabuye, ari yo nkunga y’inyongera ku bacukuzi. Block reward igizwe n’ama bitcoins mashasha yaremwe n’ibarabara ryose ry’amabuye y’agaciro (infashanyo y’ibarabara), hamwe n’amahera y’ugucuruza yashizwe hamwe. Naho infashanyo y’amabuye igabanuka uko igihe kigenda kirarenga kubera umupaka wose wa Supply w’ama bitcoins, amafaranga y’ugucuruza azobandanya kugira uruhara runini mu guhimiriza abacukuzi kugira uruharamwo.


Ku rugero rwa protocole, ntaco kibuza abakoresha gushiramwo amafaranga ata mahera n’amwe mu gice. Mu vy’ukuri, ubwo bwoko bw’ugucuruza ataco umuntu atanga ni ubudasanzwe. Ku mburabuzi, ama node ya Bitcoin ntatanga amakuru afise amafaranga ari munsi ya `1 sat/vBytes`. Nimba hari amafaranga ataco akora yaciye, ni kubera ko yashizwemwo ataco akora na Miner yatsinze, ataco ajabuka uruzitiro rw’ibihimba. Nk’akarorero, ugucuruza gukurikira nta mahera arimwo:


```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```


Muri aka karorero, ni ugucuruza kwatangujwe n'umuyobozi wa F2Pool Mining pool. Nk'umukoresha asanzwe, igipimo co hasi c'ubu rero ni `1 sat/vBytes`.

Ni ngombwa kandi ko turimbura imipaka y’ugusukura. Mu bihe vy’ugucumbagira cane, ama mempools y’ibihimba arasukura amafaranga yabo ategerejwe munsi y’urugero runaka, kugira ngo yubahirize umupaka wa RAM yahawe. Ico kigero gitorwa n’uwukoresha, ariko benshi basiga agaciro ka Bitcoin core kuri 300 MB. Ishobora guhindurwa muri dosiye `Bitcoin.conf` n'umurongo `maxmempool`.

