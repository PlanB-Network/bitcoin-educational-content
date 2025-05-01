---
term: MSIMBO WA MALIPO UNAOWEZA KUTUMIA UPYA
---

Katika BIP47, msimbo wa malipo unaoweza kutumika tena ni kitambulishi tuli kilichotolewa kutoka kwa Bitcoin Wallet ambacho kinaruhusu shughuli ya arifa na kupata anwani za kipekee. Hii inaepuka utumiaji upya wa anwani, ambayo husababisha upotezaji wa faragha, bila kulazimika kupata na kusambaza anwani mpya, ambazo hazijatumika kwa kila malipo. Katika BIP47, misimbo ya malipo inayoweza kutumika tena imeundwa kama ifuatavyo:


- Byte 0 inalingana na toleo;
- Byte 1 ni uwanja kidogo wa kuongeza habari katika kesi ya matumizi maalum;
- Byte 2 inaonyesha usawa wa `y` wa ufunguo wa umma;
- Kutoka kwa byte 3 hadi 34, utapata thamani ya `x` ya ufunguo wa umma;
- Kutoka kwa byte 35 hadi 66, kuna msimbo wa mnyororo unaohusishwa na ufunguo wa umma;
- Kutoka kwa byte 67 hadi 79, kuna pedi za sifuri.


Sehemu Inayosomeka na Binadamu (HRP) kwa ujumla huongezwa mwanzoni mwa msimbo wa malipo na cheki mwishoni, kisha inasimbwa katika base58. Kwa hivyo, ujenzi wa nambari ya malipo ni sawa na ule wa ufunguo uliopanuliwa. Hapa kuna nambari yangu ya malipo ya BIP47 katika base58 kwa mfano:


```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```


Katika utekelezaji wa PayNym wa BIP47, misimbo ya malipo inaweza pia kuonyeshwa kwa namna ya vitambulishi vinavyohusishwa na picha ya roboti. Hapa kuna yangu, kwa mfano:


```text
+throbbingpond8B1
```


Matumizi ya misimbo ya malipo pamoja na utekelezaji wa PayNym yanapatikana kwa sasa kwenye Sparrow Wallet kwenye PC na kwenye Samourai Wallet kwenye simu ya mkononi.