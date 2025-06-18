---
term: UFUNGUO ULIOpanuliwa
---

Msururu wa herufi unaochanganya ufunguo (wa umma au wa faragha), msimbo wake wa mnyororo unaohusishwa, na mfululizo wa metadata. Ufunguo uliopanuliwa hujumuisha Elements zote zinazohitajika ili kupata funguo za watoto kuwa kitambulisho kimoja. Zinatumika katika pochi za kuamua na za viwango na zinaweza kuwa za aina mbili: ufunguo wa umma uliopanuliwa (hutumika kupata funguo za umma za watoto) au ufunguo wa faragha uliopanuliwa (hutumika kupata funguo za kibinafsi na za umma). Ufunguo uliopanuliwa kwa hivyo unajumuisha vipande kadhaa tofauti vya data, vilivyoelezewa katika BIP32, kwa mpangilio:


- Kiambishi awali: `prv` na `pub` ni HRP (Sehemu Inayosomeka kwa Binadamu) kikionyesha ikiwa ni ufunguo wa faragha uliopanuliwa (`prv`) au ufunguo uliopanuliwa wa umma (`pub`). Herufi ya kwanza ya kiambishi awali huteua toleo la ufunguo uliopanuliwa: `x` kwa Legacy au SegWit V1 kwenye Bitcoin, `t` kwa Legacy au SegWit V1 kwenye Bitcoin Testnet, `y` kwa Nested SegWit kwenye Bitcoin, `u` kwa Nested SegWit kwenye SegWit GW kwa GW kwa `GW` kwa `GW`, `y` kwa SegWit Testnet, `y`. SegWit V0 kwenye Bitcoin Testnet.
- Ya kina, ambayo inaonyesha idadi ya derivations kutoka kwa ufunguo mkuu kufikia ufunguo uliopanuliwa;
- Alama ya vidole ya mzazi. Hii inawakilisha baiti 4 za kwanza za `HASH160` ya ufunguo kuu wa umma;
- Kielezo. Hii ni idadi ya jozi kati ya ndugu zake ambao ufunguo uliopanuliwa hutolewa;
- Nambari ya mnyororo;
- Baiti ya pedi ikiwa ni ufunguo wa faragha `0x00`;
- Ufunguo wa kibinafsi au wa umma;
- Cheki. Inawakilisha baiti 4 za kwanza za `HASH256` ya ufunguo mwingine uliopanuliwa.


Kiutendaji, ufunguo uliopanuliwa wa umma hutumiwa kwa generate kupokea anwani na kuangalia shughuli za akaunti bila kufichua funguo za faragha zinazohusiana. Hii inaweza kuruhusu, kwa mfano, kuundwa kwa kile kinachoitwa "kuangalia-pekee" Wallet. Hata hivyo, ni muhimu kutambua kwamba ufunguo uliopanuliwa wa umma ni taarifa nyeti kwa faragha ya mtumiaji, kwa kuwa ufumbuzi wake unaweza kuruhusu washirika wengine kufuatilia miamala na kuona salio la akaunti husika.