---
term: BETRI
---

Katika muktadha wa lugha ya uandishi inayotumika kubandika masharti ya matumizi kwa Bitcoin UTXOs, rafu hiyo ni muundo wa data wa LIFO (*Last In, First Out*) unaotumiwa kuhifadhi Elements ya muda wakati wa utekelezaji wa hati. Kila utendakazi kwenye hati hubadilisha rafu hizi, ambapo Elements inaweza kuongezwa (*sukuma*) au kuondolewa (*pop*). Hati hutumia mrundikano kutathmini vielezi, kuhifadhi vibadilisho vya muda na kudhibiti hali.


Wakati wa kutekeleza hati ya Bitcoin, rafu 2 zinaweza kutumika: rafu kuu na safu mbadala (mbadala). Rafu kuu hutumiwa kwa shughuli nyingi za hati. Ni kwenye rafu hii ambapo shughuli za hati huongeza, kuondoa au kuendesha data. Rafu mbadala, kwa upande mwingine, inatumika kuhifadhi data kwa muda wakati wa utekelezaji wa hati. Misimbo mahususi, kama vile `OP_TOALTSTACK` na `OP_FROMALTSTACK`, inakuruhusu kuhamisha Elements kutoka kwa rafu kuu hadi kwenye rafu mbadala na kinyume chake.


Kwa mfano, muamala unapoidhinishwa, saini na vitufe vya umma vinasukumwa kwenye rafu kuu na kuchakatwa na opcodes zinazofuatana ili kuthibitisha kwamba sahihi zinalingana na vitufe vya muamala na data.