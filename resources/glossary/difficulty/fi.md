---
termi: VAIKEUSASTE
---

Säädettävä parametri, joka määrittää louhinnassa vaadittavan työn todistuksen monimutkaisuuden uuden lohkon lisäämiseksi lohkoketjuun ja siihen liittyvän palkkion ansaitsemiseksi. Tämä vaikeusaste ilmenee vaikeusasteen tavoitteena, 256-bittisenä arvona, joka asettaa ylärajan, jonka lohkon otsikon tiivisteen on täytettävä ollakseen kelpaava. Tavoitteena on, että tiiviste, joka saavutetaan suorittamalla SHA256 (SHA256d) kahdesti, on pienempi tai yhtä suuri kuin tämä tavoite. Tämän tiivisteen saavuttamiseksi louhijat manipuloivat `nonce`-arvoa lohkon otsikossa. Vaikeusaste säätyy joka 2016 lohkon jälkeen, eli suunnilleen joka toinen viikko, pitääkseen keskimääräisen lohkon luomisajan noin 10 minuutissa.