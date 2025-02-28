---
term: DIFFICULTY

---
Säädettävä parametri, joka määrittää uuden lohkon lisäämiseen lohkoketjuun ja siihen liittyvän palkkion ansaitsemiseen vaadittavan todisteellisen työn monimutkaisuuden. Vaikeutta edustaa vaikeustavoite, 256-bittinen arvo, joka asettaa ylärajan, jonka lohko-otsikon hashin on täytettävä, jotta sitä voidaan pitää kelvollisena. Tavoitteena on, että SHA256:n kaksinkertaisen suorituksen (SHA256d) avulla saatu hash on pienempi tai yhtä suuri kuin tämä tavoite. Saavuttaakseen tämän hash-arvon louhijat manipuloivat lohko-otsikon `nonce`-arvoa. Vaikeusaste säätyy joka 2016 lohko eli noin kahden viikon välein, jotta keskimääräinen lohkojen luomiseen kuluva aika pysyy noin 10 minuutissa.