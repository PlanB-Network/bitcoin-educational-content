---
term: BIP0044
---

Pendekezo la uboreshaji ambalo linatanguliza muundo wa kiwango cha juu cha hali ya juu kwa pochi za HD. BIP44 hujengwa juu ya kanuni zilizowekwa na BIP32 kwa utokezi wa ufunguo na kwenye BIP43 kwa matumizi ya sehemu ya "madhumuni". Inatanguliza muundo wa kiwango cha tano: `m / kusudi' / coin_type' / akaunti' / change / address_index`. Hapa kuna maelezo ya kila kina:


- `m /` inaonyesha ufunguo mkuu wa faragha. Ni ya kipekee kwa Wallet na haiwezi kuwa na ndugu kwa kina sawa. Ufunguo mkuu unatokana moja kwa moja kutoka kwa Wallet ya seed;
- `m / madhumuni' /` huonyesha madhumuni ya uasili ambayo husaidia kutambua kiwango kinachofuatwa. Sehemu hii imeelezewa katika BIP43. Kwa mfano, ikiwa Wallet inafuata kiwango cha BIP84 (SegWit V0), faharasa itakuwa `84'`;
- `m / kusudi' / aina ya sarafu' /` inaonyesha aina ya sarafu-fiche. Hii inaruhusu utofauti wa wazi kati ya matawi yaliyowekwa kwa cryptocurrency moja na yale yaliyowekwa kwa cryptocurrency nyingine katika Wallet ya sarafu nyingi. Faharasa iliyowekwa kwa Bitcoin ni `0'`;
- `m / kusudi' / aina ya sarafu' / akaunti' /` inaonyesha nambari ya akaunti. Kina hiki kinaruhusu utofautishaji rahisi na upangaji wa Wallet katika akaunti tofauti. Akaunti hizi zimepewa nambari kuanzia `0'`. Vifunguo vilivyopanuliwa (`xpub`, `xprv`...) vinapatikana kwa kina hiki;
- `m / kusudi' / aina ya sarafu' / akaunti' / mabadiliko /` inaonyesha mnyororo. Kila akaunti kama inavyofafanuliwa kwa kina 3 ina minyororo miwili katika kina cha 4: mnyororo wa nje na mnyororo wa ndani (pia huitwa "mabadiliko"). Msururu wa nje hupata anwani zinazokusudiwa kuwasilishwa kwa umma, yaani, anwani zinazotolewa kwetu tunapobofya "kupokea" katika programu yetu ya Wallet. Msururu wa ndani hupata anwani zisizokusudiwa kubadilishwa hadharani, yaani, kubadilisha anwani. Msururu wa nje unatambulishwa kwa faharasa `0` na mnyororo wa ndani unatambulishwa kwa faharasa `1`. Utaona kwamba kutoka kwa kina hiki, hatufanyi tena derivation ngumu, lakini derivation ya kawaida (hakuna apostrophe). Ni kutokana na utaratibu huu kwamba tunaweza kupata funguo zote za umma za watoto kutoka kwa `xpub` yao;
- `m / kusudi' / aina ya sarafu' / akaunti' / change / Address-index` inaonyesha tu nambari ya Address inayopokea na jozi ya funguo zake, ili kuitofautisha na ndugu zake kwa kina sawa kwenye tawi moja. Kwa mfano, Address inayotokana na kwanza ina faharasa `0`, ya pili Address ina faharasa `1`, na kadhalika...

Kwa mfano, ikiwa upokeaji wangu wa Address una njia ya derivation `m / 86' / 0' / 0' / 0 / 5`, tunaweza kubainisha taarifa ifuatayo:


- `86'` inaonyesha kuwa tunafuata kiwango cha uasiliaji cha BIP86 (Taproot au SegWitV1);
- `0'` inaonyesha kuwa ni Bitcoin Address;
- `0'` inaonyesha kwamba tuko kwenye akaunti ya kwanza ya Wallet;
- `0` inaonyesha kuwa ni Address ya nje;
- `5` inaonyesha kuwa ni Address ya sita ya nje ya akaunti hii.