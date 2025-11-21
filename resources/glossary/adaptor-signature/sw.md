---
term: SAINI YA ADAPTER
---

Mbinu ya kriptografia inayoruhusu kuchanganya sahihi na sahihi ya ziada (inayoitwa "saini ya adapta") ili kufichua kipande cha data cha siri. Njia hii inafanya kazi kwa njia ambayo kujua Elements mbili kati ya saini halali, saini ya adapta, na siri inaruhusu kupunguza kipengele cha tatu kilichokosekana. Mojawapo ya sifa za kuvutia za njia hii ni kwamba ikiwa tunajua saini ya adapta ya mwenzetu na sehemu maalum kwenye curve ya duara iliyounganishwa na siri iliyotumiwa kukokotoa sahihi ya adapta hii, basi tunaweza kupata sahihi yetu ya adapta ambayo italingana na siri sawa, bila kupata ufikiaji wa moja kwa moja kwa siri yenyewe. Katika Exchange kati ya washikadau wawili ambao hawaaminiani, mbinu hii inaruhusu kufichuliwa kwa wakati mmoja wa vipande viwili nyeti vya habari kati ya washiriki. Mchakato huu huondoa hitaji la uaminifu katika miamala ya papo hapo kama vile Kubadilishana Sarafu au Kubadilishana kwa Atomiki. Hebu tuchukue mfano ili kuelewa vizuri zaidi. Alice na Bob wanataka kutuma kila mmoja BTC 1, lakini hawaaminiani. Kwa hivyo watatumia saini za adapta kukanusha hitaji la kuamini mhusika mwingine katika Exchange hii (na hivyo kuifanya kuwa "atomiki" Exchange). Wanaendelea kama ifuatavyo:


- Alice anaanzisha Exchange hii ya atomiki. Anatengeneza muamala $m_A$ ambao hutuma BTC 1 kwa Bob. Anaunda sahihi $s_A$ ambayo inaidhinisha muamala huu kwa kutumia ufunguo wake wa faragha $p_A$ ($P_A = p_A \cdot G$), na kwa kutumia Nonce $n_A$ na $t$ ya siri ($N_A = n_A \cdot G$ na $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \sambamba P_A \sambamba m_A) \cdot p_A$$



- Alice anakokotoa saini ya adapta $s_A'$ kutoka kwa siri $t$ na sahihi yake halisi $s_A$:

$$s_A' = s_A - t$$



- Alice anatuma kwa Bob saini ya adapta yake $s_A'$, muamala wake ambao haujatiwa saini $m_A$, nukta inayolingana na $T$ ya siri, na uhakika unaolingana na Nonce $N_A$. Tunaita vipande hivi vya habari "adapta". Kumbuka kuwa kwa habari hii tu, Bob hana uwezo wa kupata BTC ya Alice.
- Hata hivyo, Bob anaweza kuthibitisha kwamba Alice hamdanganyi. Ili kufanya hivyo, anakagua kama saini ya adapta ya Alice $s_A'$ inalingana na shughuli iliyoahidiwa $m_A$. Ikiwa equation ifuatayo ni sahihi, basi ana hakika kuwa saini ya adapta ya Alice ni halali:

$$s_A' \cdot G = N_A + H(N_A + T \sambamba P_A \sambamba m_A) \cdot P_A$$



- Uthibitishaji huu unampa Bob uhakikisho kutoka kwa Alice, ili aweze kuendelea na mchakato wa kubadilishana atomiki kwa amani ya akili. Kisha ataunda muamala wake mwenyewe $m_B$ kutuma BTC 1 kwa Alice na saini yake ya adapta $s_B'$, ambayo itaunganishwa na siri ile ile $t$ ambayo Alice pekee anajua kwa sasa (Bob hajui thamani hii $t$, lakini tu pointi yake sambamba $T$ ambayo Alice amempa): $$s_B' = n_B +B + H (Nparalle P_ m_B) \cdot p_B$$



- Bob anatuma kwa Alice saini ya adapta yake $s_B'$, muamala wake ambao haujatiwa saini $m_B$, nukta inayolingana na $T$ ya siri, na uhakika unaolingana na Nonce $N_B$. Sasa Alice anaweza kuchanganya sahihi ya adapta ya Bob $s_B'$ na siri $t$, ambayo yeye pekee ndiye anajua, ili kukokotoa sahihi sahihi $s_B$ kwa shughuli $m_B$ ambayo humtumia Bob's BTC:

$$s_B = s_B' + t$$


$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \sambamba P_B \sambamba m_B) \cdot P_B$$



- Alice anatangaza muamala huu uliotiwa saini $m_B$ kwenye Bitcoin Blockchain ili kurejesha BTC ambayo Bob alimwahidi. Bob anajifunza kuhusu muamala huu kwenye Blockchain. Kwa hivyo ana uwezo wa kutoa sahihi $s_B = s_B' + t$. Kutoka kwa habari hii, Bob anaweza kutenga siri maarufu $t$ aliyohitaji:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$



- Hata hivyo, siri hii $t$ ilikuwa ni taarifa pekee ambayo haikukosekana kwa Bob kutoa saini halali $s_A$, kutoka sahihi ya adapta ya Alice $s_A'$, ambayo itamruhusu kuhalalisha shughuli $m_A$ kutuma BTC kutoka Alice hadi Bob. Kisha anakokotoa $s_A$ na kutangaza muamala $m_A$ kwa zamu: $$s_A = s_A' + t$$


$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \sambamba P_A \sambamba m_A) \cdot P_A$$