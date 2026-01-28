---
term: UMUSINIRO W'UMUGAMBI
---

Uburyo bw'ibanga bushobora gufatanya umukono nyawo n'uwundi mukono w'inyongera (witwa "adaptateur signature") kugira ngo umuntu amenye amakuru y'ibanga. Ubwo buryo burakora ku buryo kumenya Elements zibiri hagati y’umukono ubereye, umukono w’adapteur, n’ibanga bituma umuntu ashobora gukuraho ikintu ca gatatu kibuze. Ikintu kimwe gishimishije c'ubu buryo ni uko nitwamenya umukono w'adapteri w'urunganwe rwacu n'akarongo kadasanzwe ku nzira y'umurongo w'uruzitiro bijanye n'ibanga ryakoreshejwe mu kubara uwo mukono w'adapteri, dushobora rero kuronka umukono wacu bwite w'adapteri uhuye n'iryo banga nyene, vyose tutarigeze turonka uburenganzira bwo gushika ku banga ubwaryo. Mu Exchange hagati y’abantu babiri batizigirana, ubu buryo buratuma amakuru abiri y’agaciro atangazwa icarimwe hagati y’abaje mu nama. Ivyo bikuraho ivy’ukwizigira mu bikorwa vy’ubudandaji bica bihinduka nk’uguhindura amafaranga canke uguhindura amafaranga y’atome. Reka turabe akarorero kugira ngo tuvyiyumvire neza. Alice na Bob umwe wese ashaka kohereza uwundi BTC 1, ariko ntibizigirana. Bazokoresha rero imikono y'aba adapter kugira ngo bakuremwo ivy'ukwizigirana mu gihe ca Exchange (gutyo bibe Exchange "atome"). Bagenda gutya:

*Alice ni yo itangura iyi Exchange y'atome. Akora igikorwa $m_A$ cohereza BTC 1 kuri Bob. Akora umukono $s_A$ kugira ngo yemeze iyo nzira akoresheje urufunguzo rwiwe bwite $p_A$ ($P_A = p_A \cdot G$), Nonce $n_A$, n'ibanga $t$ ($N_A = n_A \cdot G$ na $T = t \cdot G$):*

$$s_A = n_A + t + H(N_A + T \ibihuye P_A \ibihuye m_A) \cdot p_A$$


**Alice ibara umukono w'adapteur $s_A'$ ikoresheje ibanga $t$ n'umukono wiwe nyawo $s_A$:**

$$s_A' = s_A - t$$



- Alice yohereza kuri Bob umukono wiwe w'adapteri $s_A'$, igikorwa ciwe kitashizweko umukono $m_A$, akarongo kahuye n'ibanga $T$, n'akarongo kahuye na Nonce $N_A$. Ivyo bice vy'amakuru vyitwa "adapteur". Zirikana ko n’aya makuru gusa, Bob idashobora gusaba BTC ya Alice.

**Ariko rero, Bob arashobora kugenzura ko Alice atariko aramuhenda.** Kugira ngo abikore, asuzuma nimba umukono wa adapteur wa Alice $s_A'$ uhuye n'ivyo yasezeranye $m_A$. Nimba iyi nsiguro ikurikira ari yo, rero arashobora kwizigira ko umukono w’adapteur wa Alice ari wo:

$$s_A' \cdot G = N_A + H(N_A + T \ibihuye P_A \ibihuye m_A) \cdot P_A$$


**Iryo genzura riha Bob icizigiro kinaka kivuye kuri Alice, bikamufasha gukomeza ata nkomanzi igikorwa co guhindura atome.** Hanyuma akora igikorwa ciwe bwite $m_B$ yohereza BTC 1 kuri Alice maze akabara umukono wiwe bwite w’adapteri $s_B'$, iri banga rihuye na $t at-4 gusa. ingingo, Bob izi gusa ingingo yayo ihuye $T$, iyo Alice yatanze): $$s_B' = n_B + H(N_B + T \ihuye P_B \ihuye m_B) \cdot p_B$$



- Bob yohereza kuri Alice umukono wiwe w'adapteri $s_B'$, igikorwa ciwe kitashizweko umukono $m_B$, akarongo kahuye n'ibanga $T$, n'akarongo kahuye na Nonce $N_B$. Alice ubu arashobora gufatanya umukono wa adapter wa Bob $s_B'$ n'ibanga $t$, ari we wenyene azi, kugira ngo aharure umukono ubereye $s_B$ ku bijanye n'ugucuruza $m_B$ kwohereza BTC yiwe ya Bob:

$$s_B = s_B' + t$$


$$(s_B' + t) \cakadomo G = N_B + T + H(N_B + T \ibihuye P_B \ibihuye m_B) \cakadomo P_B$$


*Alice ica itangaza iyo nzira yasinywe $m_B$ kuri Bitcoin Blockchain kugira ngo isaba BTC Bob yasezeranye. Iyo iyo nzira imaze gusohoka, Bob irashobora kuyibona kuri Blockchain. Arashobora rero gukuraho umukono $s_B = s_B' + t$. Muri ayo makuru, Bob arashobora kwitandukanya n'ibanga rizwi cane $t$ yari akeneye:*

$$t = (s_B' + t) - s_B' = s_B - s_B'$$


*Iri banga $t$ ni ryo ryonyene ryari ribuze Bob yari akeneye kugira ngo abare umukono w'ukuri $s_A$, uhereye ku mukono w'adapteur wa Alice $s_A'$. Nayo, ubu arashobora kwemeza igikorwa $m_A$ cohereza BTC 1 kuva kuri Alice gushika kuri Bob. Araheza abara $s_A$ agaca atangaza ivy'ugucuruza $m_A$:* $$s_A = s_A' + t$$


$$(s_A' + t) \cakadomo G = N_A + T + H(N_A + T \ibihuye P_A \ibihuye m_A) \cakadomo P_A$$