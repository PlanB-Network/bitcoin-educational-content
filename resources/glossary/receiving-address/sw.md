---
term: KUPOKEA Address
---

Taarifa zinazotumiwa kupokea bitcoins. Address kwa kawaida huundwa kwa kuharakisha ufunguo wa umma, kwa kutumia `SHA256` na `RIMPEMD160`, na kuongeza metadata kwenye muhtasari huu. Vifunguo vya umma vilivyotumika kutengeneza Address inayopokea ni sehemu ya Wallet ya mtumiaji na kwa hivyo yanatokana na seed yao. Kwa mfano, anwani za SegWit zinajumuisha habari ifuatayo:


- HRP ya kuteua "Bitcoin": `bc`;
- Kitenganishi: `1`;
- Toleo la SegWit lililotumika: `q` au `p`;
- Mzigo wa malipo: muhtasari wa ufunguo wa umma (au moja kwa moja ufunguo wa umma katika kesi ya Taproot);
- Cheki: msimbo wa BCH.


Walakini, Address inayopokea inaweza pia kuwakilisha kitu kingine kulingana na muundo wa hati uliotumiwa. Kwa mfano, anwani za P2SH zinaundwa kwa kutumia hati ya Hash. Anwani za Taproot, kwa upande mwingine, zina ufunguo wa umma uliowekwa moja kwa moja bila kuharakisha.


Address inayopokea inaweza kuwakilishwa kwa njia ya mfuatano wa alphanumeric au kama msimbo wa QR. Kila Address inaweza kutumika mara nyingi, lakini hii ni mazoezi ya kukata tamaa. Hakika, ili kudumisha kiwango fulani cha faragha, inashauriwa kutumia kila Bitcoin Address mara moja tu. Address mpya inapaswa kuzalishwa kwa kila malipo yanayoingia kwa Wallet ya mtu. Address imesimbwa katika `Bech32` kwa anwani za SegWit V0, katika `Bech32m` kwa anwani za SegWit V1, na katika `Base58check` kwa anwani za Urithi. Kwa mtazamo wa kiufundi, kupokea Bitcoin hutafsiri kuwa kuwa na ufunguo wa faragha unaohusishwa na ufunguo wa umma (na hivyo Address). Mtu anapopokea bitcoins, mtumaji husasisha kikwazo kilichopo kwenye matumizi yake ili ni mpokeaji pekee anayeweza kuwa na nguvu hii.


![](../../dictionnaire/assets/23.webp)