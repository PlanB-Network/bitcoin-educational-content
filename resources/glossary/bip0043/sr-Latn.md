---
term: BIP0043
---

Predlog za poboljšanje koji uvodi upotrebu nivoa derivacionog puta za opisivanje polja svrhe u strukturi HD novčanika, prethodno uvedenog u BIP32. Prema BIP43, prvi nivo derivacije HD Wallet, odmah nakon master ključa označenog kao `m/`, rezervisan je za broj svrhe koji ukazuje na standard derivacije korišćen za ostatak puta. Ovaj broj se beleži kao očvrsnuti indeks. Na primer, ako Wallet prati SegWit standard (BIP84), početak njegovog derivacionog puta bi bio: `m/84'/`. BIP43 tako omogućava pojašnjenje standarda kojih se pridržava svaki Wallet softver kako bi se postigla bolja interoperabilnost među njima. Standardizacija ostatka derivacionog puta opisana je u BIP44.