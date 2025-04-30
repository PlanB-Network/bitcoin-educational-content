---
term: LEBO (MALIPO YA KIMYA)
---

Ndani ya itifaki ya Malipo ya Kimya, lebo ni nambari kamili zinazotumiwa kurekebisha Address tuli ya awali ili kuunda anwani nyingi tuli. Matumizi ya lebo hizi huruhusu kutenganishwa kwa malipo yanayotumwa kupitia Malipo ya Kimya, kwa kutumia anwani tofauti tuli kwa kila matumizi, bila kuongeza kupita kiasi mzigo wa uendeshaji wa kugundua malipo haya (kuchanganua). Bob anatumia Address $B$ tuli, inayojumuisha funguo mbili za umma: $B_{\text{scan}}$ kwa kuchanganua na $B_{\text{spend}}$ kwa matumizi. Hash ya $b_{\text{scan}}$ na nambari kamili $m$, iliyozidishwa na sehemu ya jenereta $G$, huongezwa kwenye ufunguo wa matumizi wa umma $B_{\text{spend}}$ ili kuunda aina mpya ya ufunguo wa matumizi ya umma $B_m$:


$$ B_m = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$


Kwa mfano, ufunguo wa kwanza $B_1$ unapatikana kwa njia hii:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Address tuli iliyochapishwa na Bob sasa itaundwa na $B_{\text{scan}}$ na $B_m$. Kwa mfano, Address ya kwanza tuli yenye lebo $1$ itakuwa:


$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$


Tunaanzia kwenye lebo $1$ pekee, kwa sababu lebo $0$ imehifadhiwa kwa mabadiliko. Alice, ambaye angependa kutuma bitcoins kwa Address tuli iliyo na lebo iliyotolewa na Bob, atapata malipo ya kipekee ya Address $P_0$ kwa kutumia $B_1$ mpya badala ya $B_{\text{spend}}$:


$$ P_0 = B_1 + \maandishi{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$


Kwa uhalisia, Alice anaweza hata asijue kuwa Bob ana lebo ya Address, kwa kuwa anatumia tu sehemu ya pili ya Address tuli aliyotoa, ambayo katika hali hii ni thamani ya $B_1$ badala ya $B_{\text{spend}}$. Ili kuchanganua malipo, Bob atatumia kila wakati thamani ya tuli yake ya awali ya Address na $B_{\text{spend}}$ kwa njia hii:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Kisha, atatoa tu thamani atakayopata $P_0$ kutoka kwa kila pato moja baada ya nyingine. Kisha huangalia ikiwa moja ya matokeo ya uondoaji huu yanalingana na thamani ya moja ya lebo anazotumia kwenye Wallet yake. Ikiwa inalingana, kwa mfano, kwa pato #4 na lebo $1$, hii inamaanisha kuwa pato hili ni Malipo ya Kimya yanayohusishwa na Address yake tuli inayoitwa $B_1$:

$$ Out_4 - P_0 = \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Hii inafanya kazi kwa sababu:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Shukrani kwa njia hii, Bob anaweza kutumia wingi wa anwani tuli (zenye $B_1$, $B_2$, $B_3$...), zote zimetokana na tuli yake ya msingi ya Address ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}}$), ili kutenganisha matumizi ipasavyo.


Hata hivyo, mgawanyo huu wa anwani tuli ni halali tu kutoka kwa mtazamo wa usimamizi wa Wallet wa kibinafsi, lakini hairuhusu kutenganishwa kwa vitambulisho. Kwa kuwa zote zina $B_{\text{scan}}}$ sawa, ni rahisi sana kuhusisha anwani tuli zote pamoja na kubaini kuwa ni za huluki moja.