---
term: HISA
---

Katika muktadha wa vikundi vya Mining, hisa ni kiashirio kinachotumika kukadiria mchango wa mtu binafsi wa Miner ndani ya bwawa. Hatua hii hutumika kama msingi wa kukokotoa zawadi ambayo bwawa hugawanya upya kwa kila Miner. Kila hisa inalingana na Hash ambayo inakidhi lengo la ugumu chini ya ile ya mtandao wa Bitcoin.


Ili kuelezea kwa mlinganisho, fikiria kufa kwa pande 20. Kwenye Bitcoin, tuseme kwamba Proof of Work inahitaji kusongesha nambari chini ya 3 ili kudhibitisha kizuizi (yaani, kufikia matokeo ya 1 au 2). Sasa, fikiria kwamba ndani ya Mining pool, lengo la ugumu kwa hisa limewekwa kwa 10. Kwa hiyo, kwa Miner binafsi katika bwawa, kila roll ya kete ambayo husababisha nambari ya chini kuliko hesabu 10 kama sehemu halali. Hisa hizi kisha hutumwa kwenye bwawa na Miner, ili kudai malipo yao, hata kama hazilingani na matokeo halali ya kizuizi kwenye Bitcoin.


Kwa kila Hash iliyokokotolewa, Miner ya kibinafsi kwenye bwawa inaweza kukumbana na matukio matatu tofauti:


- Ikiwa thamani ya Hash ni kubwa kuliko au sawa na lengo la ugumu lililowekwa la bwawa la kushiriki, basi Hash hii haina matumizi. Miner kisha hubadilisha Nonce yao ili kujaribu Hash mpya: `Hash > shiriki > block`.
- Ikiwa Hash ni ya chini kuliko lengo la ugumu wa hisa, lakini kubwa kuliko au sawa na lengo la ugumu la Bitcoin, basi Hash hii inajumuisha sehemu halali ambayo, hata hivyo, haitoshi kuthibitisha kizuizi. Miner inaweza kutuma Hash hii kwenye kundi lao ili kudai zawadi inayohusishwa na kushiriki: `shiriki > Hash > block`.
- Ikiwa Hash iko chini kuliko lengo la ugumu la mtandao wa Bitcoin, inachukuliwa kuwa sehemu halali na kizuizi halali. Miner husambaza Hash hii kwenye bwawa lao, ambayo huharakisha kuitangaza kwenye mtandao wa Bitcoin. Hash hii pia inahesabiwa kama mgao halali wa Miner: `shiriki > kambi > Hash`.


![](../../dictionnaire/assets/32.webp)


Mfumo huu wa hisa hutumika kukadiria kazi iliyofanywa na kila mtu Miner ndani ya bwawa, bila kulazimika kukokotoa upya heshi zote zinazozalishwa na Miner, ambayo haitakuwa na ufanisi kabisa kwa bwawa.


Makundi ya Mining hurekebisha ugumu wa hisa ili kusawazisha mzigo wa uthibitishaji na kuhakikisha kwamba kila Miner, iwe ndogo au kubwa, inawasilisha hisa takriban kila sekunde chache. Hii inaruhusu hesabu sahihi ya kila Hashrate ya Miner na usambazaji wa zawadi kulingana na mbinu iliyochaguliwa ya hesabu ya fidia (PPS, PPLNS, TIDES...).


> ► *Kwa Kifaransa, "hisa" inaweza kutafsiriwa kama "sehemu".*