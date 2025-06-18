---
term: PSBT
---

Kifupi cha "Partially Signed Bitcoin Transaction". Ni vipimo vilivyoletwa na BIP174 ili kusawazisha njia ambayo shughuli ambazo hazijakamilika zinaundwa katika programu zinazohusiana na Bitcoin, kama vile programu ya Wallet. PSBT inajumlisha shughuli ambayo pembejeo huenda zisiwe na saini kamili. Inajumuisha maelezo yote muhimu kwa mshiriki kutia sahihi muamala bila kuhitaji data ya ziada. Kwa hivyo, PSBT inaweza kuchukua aina 3 tofauti:


- Muamala uliojengwa kikamilifu, lakini bado haujatiwa saini;
- Muamala uliotiwa saini kwa sehemu, ambapo baadhi ya pembejeo hutiwa saini huku zingine bado hazijatiwa saini;
- Au muamala wa Bitcoin uliotiwa saini kikamilifu, ambao unaweza kubadilishwa kuwa tayari kutangazwa kwenye mtandao.


Umbizo la PSBT huwezesha mwingiliano kati ya programu tofauti za Wallet na vifaa vyenye saini (Hardware Wallet). Kwa sasa, toleo la 0 la PSBT linatumika, kama lilivyofafanuliwa katika BIP174, lakini toleo la 2 linapendekezwa kupitia BIP370.


> ► *Toleo la 1 la PSBT halipo. Kwa kuwa toleo la 0 lilikuwa toleo la kwanza, toleo la pili liliitwa kwa njia isiyo rasmi toleo la 2. Ava Chow, ambaye aliandika BIP370, aliamua kugawa nambari 2 kwa toleo hili jipya ili kuepuka mkanganyiko wowote.*