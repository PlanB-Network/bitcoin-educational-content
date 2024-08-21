---
term: ATOMIC SWAP
---

Tehnoloogia, mis võimaldab krüptovaluutade otsest vahetust kahe osapoole vahel, ilma usalduse vajaduseta ja ilma vahendaja kaasamiseta. Neid vahetusi nimetatakse "atoomilisteks", kuna need võivad lõppeda ainult kahe tulemusega:
* Kas vahetus on edukas ja mõlemad osapooled on tõhusalt vahetanud oma krüptovaluutasid;
* Või vahetus ebaõnnestub ja mõlemad osapooled lahkuvad oma algsete krüptovaluutadega.

Atomaarseid vahetusi saab teostada kas sama krüptovaluutaga, sel juhul nimetatakse seda ka "*coinswap*iks", või erinevate krüptovaluutade vahel. Ajalooliselt tuginesid need "Hash Time-Locked Contracts" (HTLC) peale, ajalukustuse süsteemile, mis tagab vahetuse lõpuleviimise või täieliku tühistamise, säilitades seeläbi osapoolte vahendite terviklikkuse. See meetod nõudis protokolle, mis suudaksid käsitleda nii skripte kui ka ajalukke. Siiski on viimastel aastatel trend liikunud *Adaptor Signatures* kasutamise suunas. See teine lähenemine on eeliseks, kuna see kõrvaldab vajaduse skriptide järele, vähendades seeläbi operatsioonikulusid. Selle teine suur eelis on see, et see ei nõua tehingu mõlemas osas identse heshimise kasutamist, mis aitab vältida nende vahelise seose paljastamist.