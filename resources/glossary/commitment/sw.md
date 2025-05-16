---
term: Commitment
---

Commitment (katika maana ya kriptografia) ni kitu cha hisabati, kinachoashiria $C$, kinachotokana na operesheni kwenye data iliyopangwa $m$ (ujumbe) na thamani ya nasibu $r$. Tunaandika:


$$
C = \text{commit}(m, r)
$$


Utaratibu huu unajumuisha shughuli kuu mbili:




- Ahadi: tunatumia kitendakazi cha kriptografia kwa ujumbe $m$ na $r$ nasibu ili kutoa $C$ ;
- Thibitisha: tunatumia $C$, ujumbe wa $m$ na thamani ya $r$ ili kuangalia kama Commitment hii ni sahihi. Chaguo za kukokotoa hurejesha `Kweli` au `Sivyo`.


Commitment lazima iheshimu sifa mbili:




- Kufunga: lazima isiwezekane kupata jumbe mbili tofauti zinazozalisha sawa $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Kama vile:


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Inaficha: ujuzi wa $C$ lazima ufichue maudhui ya $m$.


Katika kesi ya itifaki ya RGB, Commitment imejumuishwa katika shughuli ya Bitcoin ili kuthibitisha kuwepo kwa kipande fulani cha habari kwa wakati fulani, bila kufichua habari yenyewe.