---
term: GAP LIMIT

---
Parameeter, mida kasutatakse Bitcoini rahakoti tarkvaras, et määrata maksimaalne arv järjestikuseid kasutamata aadresse, mida genereerida enne täiendavate tehingute otsimise peatamist. Selle parameetri kohandamine on sageli vajalik rahakoti taastamisel, et tagada kõigi tehingute leidmine. Ebapiisav Gap Limit võib põhjustada mõne tehingu puudumise, kui aadressid jäeti tuletamisetappide ajal vahele. Gap Limit'i suurendamine võimaldab rahakotil otsida aadresside järjestuses edasi, et taastada kõik seotud tehingud.

Üks "xpub" võib teoreetiliselt tuletada rohkem kui 4 miljardit vastuvõtuaadressi (nii sisemised kui ka välised aadressid). Kuid rahakoti tarkvara ei saa neid kõiki tuletada ja nende kasutamist kontrollida, ilma et see tekitaks suuri tegevuskulusid. Seega toimivad nad indeksi järjekorras, sest tavaliselt genereerivad kõik rahakotiprogrammid aadressid just selles järjekorras. Tarkvara registreerib iga kasutatud aadressi enne järgmise juurde liikumist ja lõpetab otsingu, kui ta kohtab mitu järjestikust tühja aadressi. Seda arvu nimetatakse Gap Limit'iks.

Kui näiteks Gap Limit on seatud `20` ja aadress `m/84'/0'/0'/0/15/` on tühi, siis tuletab rahakott aadressid kuni `m/84'/0'/0'/0'/0/34/`. Kui see aadresside vahemik jääb kasutamata, peatub otsing seal. Järelikult ei avastataks antud näites tehingut, mille puhul kasutatakse aadressi `m/84'/0'/0'/0'/0/40/`.