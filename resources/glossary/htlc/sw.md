---
term: HTLC
---

Inasimama kwa "*Hashed Timelock Contract*". Huu ni utaratibu wa Smart contract unaotumiwa hasa kwenye Umeme. Pia wakati mwingine hupatikana katika ubadilishaji wa atomiki. Kimsingi, HTLC hufanya uhamisho wa fedha kuwa masharti ya ufunuo wa siri, na pia inajumuisha hali ya wakati ili kulinda pesa za mtumaji katika tukio la shughuli iliyoshindwa.


Kwenye Umeme, HTLC hukuruhusu kutuma bitcoins kwenye nodi ambayo huna chaneli moja kwa moja, kwa kupitia njia kadhaa, bila hitaji la uaminifu njiani. Malipo kati ya kila nodi ni masharti ya utoaji wa picha ya awali (siri ambayo, wakati wa haraka, inalingana na thamani iliyokubaliwa). Iwapo mpokeaji wa mwisho atatoa picha hii ya awali, anaweza kudai fedha, na kwa lazima kuwezesha kila nodi ya kati kudai fedha kwa kasi.


Kwa mfano, ikiwa Alice anataka kutuma 1 BTC kwa David, lakini hana chaneli ya moja kwa moja naye, anapaswa kupitia Bob na Carol, ambao wana njia za malipo. Hivi ndivyo muamala unavyofanya kazi:




- David akimkabidhi Alice Umeme wa Invoice. Hii ina Hash $h$ ya $s$ ya siri (picha ya awali) ambayo David pekee ndiye anajua. Kwa hivyo tunayo: $h = \text{Hash}(s)$ ;
- Alice anatengeneza HTLC na Bob, ambaye anajitolea kumtumia BTC 1 kwa sharti kwamba Bob ampe $s$ ya siri (picha ya awali) ambayo inalingana na Hash $h$;
- Bob anaunda HTLC na Carol, ambaye anajitolea kumtumia 1 BTC kwa sharti kwamba atoe siri sawa $s$ ;
- Carol anaunda HTLC na David, ambaye hutoa BTC nyingine 1 ikiwa atafunua picha ya $ s$;
- David anafichua $s$ (ambayo yeye pekee alijua) kwa Carol kupokea 1 BTC. Carol sasa anaweza kutumia $s$ kupata BTC kutoka kwa Bob. Na Bob, ambaye sasa anajua $s$, anafanya vivyo hivyo na Alice.


Hatimaye, Alice alituma 1 BTC kwa David kupitia Bob na Carol (hatua isiyopendelea upande wowote), bila mtu yeyote kuaminiana, kwa kuwa kila kitu kinalindwa kwa kasi na masharti ya HTLCs.


Kwa hivyo HTLC huwezesha kinachojulikana kama ubadilishanaji wa "atomiki": ama uhamishaji umefaulu kabisa, au itashindikana, na pesa zinarejeshwa. Hii inahakikisha usalama wa miamala, hata kati ya washiriki wengi bila hitaji la uaminifu.