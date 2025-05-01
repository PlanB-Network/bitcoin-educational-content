---
term: NJIA YA DERIVATION
---

Katika muktadha wa pochi za Hierarkia Deterministic (HD), njia ya uasilia inarejelea mlolongo wa fahirisi zinazotumiwa kupata funguo za watoto kutoka kwa ufunguo mkuu. Imefafanuliwa katika BIP32, njia hii inabainisha muundo wa mti wa kupata funguo za watoto. Njia ya unyambulishaji inawakilishwa na mfululizo wa fahirisi zilizotenganishwa na mikwaju, na kila mara huanza na ufunguo mkuu (unaoashiria `m/`). Kwa mfano, njia ya kawaida inaweza kuwa `m/84'/0'/0'/0/0`. Kila ngazi ya derivation inahusishwa na kina maalum:


- `m /` inaonyesha ufunguo mkuu wa faragha. Ni ya kipekee kwa Wallet na haiwezi kuwa na ndugu kwa kina sawa. Ufunguo mkuu unatokana moja kwa moja kutoka kwa seed;
- `m/madhumuni' /` huonyesha dhumuni la uasilishaji ambalo husaidia kutambua kiwango kinachofuatwa. Sehemu hii imeelezewa katika BIP43. Kwa mfano, ikiwa Wallet itafuata kiwango cha BIP84 (SegWit V0), faharasa itakuwa `84'`;
- `m / kusudi' / aina ya sarafu' /` inaonyesha aina ya sarafu-fiche. Hii inaruhusu utofauti wa wazi kati ya matawi yaliyowekwa kwa cryptocurrency moja na yale yaliyowekwa kwa jingine katika Wallet ya sarafu nyingi. Faharasa iliyowekwa kwa Bitcoin ni `0'`;
- `m / kusudi' / aina ya sarafu' / akaunti' /` inaonyesha nambari ya akaunti. Kina hiki hurahisisha kutofautisha na kupanga Wallet katika akaunti tofauti. Akaunti hizi zimepewa nambari kuanzia `0'`. Vifunguo vilivyopanuliwa (`xpub`, `xprv`...) vinapatikana katika kiwango hiki cha kina;
- `m / kusudi' / aina ya sarafu' / akaunti' / mabadiliko /` inaonyesha njia. Kila akaunti kama inavyofafanuliwa kwa kina 3 ina njia mbili kwa kina cha 4: mnyororo wa nje na mnyororo wa ndani (pia huitwa "mabadiliko"). Msururu wa nje hupata anwani zinazokusudiwa kushirikiwa hadharani, yaani, anwani ambazo hutolewa kwetu tunapobofya "kupokea" katika programu yetu ya Wallet. Msururu wa ndani hupata anwani zisizokusudiwa kubadilishwa hadharani, hasa kubadilisha anwani. Msururu wa nje unatambulishwa kwa faharasa `0` na mnyororo wa ndani unatambulishwa kwa faharasa `1`. Utaona kwamba kutoka kwa kina hiki, hatufanyi tena derivation ngumu, lakini derivation ya kawaida (hakuna apostrophe). Ni kutokana na utaratibu huu kwamba tunaweza kupata funguo zote za umma za watoto kutoka kwa `xpub` yao;



- `m / kusudi' / aina ya sarafu' / akaunti' / change / Address-index` inaonyesha tu nambari ya Address inayopokea na jozi ya funguo zake, ili kuitofautisha na ndugu zake kwa kina sawa kwenye tawi moja. Kwa mfano, Address inayotokana na kwanza ina faharasa `0`, ya pili Address ina faharasa `1`, na kadhalika...


Kwa mfano, ikiwa upokeaji wangu wa Address una njia ya derivation `m / 86' / 0' / 0' / 0 / 5`, tunaweza kubainisha taarifa ifuatayo:


- `86'` inaonyesha kuwa tunafuata kiwango cha uasiliaji cha BIP86 (Taproot / SegWit V1);
- `0'` inaonyesha kuwa ni Bitcoin Address;
- `0'` inaonyesha kwamba tuko kwenye akaunti ya kwanza ya Wallet;
- `0` inaonyesha kuwa ni Address ya nje;
- `5` inaonyesha kuwa ni Address ya sita ya akaunti hii.


![](../../dictionnaire/assets/18.webp)