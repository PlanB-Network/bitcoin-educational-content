---
term: ADAPTOR SIGNATURE
---

Krüptograafiline meetod, mis võimaldab ühendada tõelise allkirja lisasignatuuriga (mida nimetatakse "adaptor signature"), et paljastada salajane andmepala. See meetod toimib nii, et kahe elemendi – kehtiva allkirja, adaptor signatuuri ja salajase andme – teadmine võimaldab järeldada puuduva kolmanda elemendi. Selle meetodi üks huvitavaid omadusi on see, et kui me teame oma vastaspoole adaptor signatuuri ja spetsiifilist punkti elliptilisel kõveral, mis on seotud salajase andmega, mida kasutati selle adaptor signatuuri arvutamiseks, saame tuletada oma adaptor signatuuri, mis sobib sama salajase andmega, ilma et meil oleks kunagi otsene juurdepääs salajasele andmele. Kahe usaldamatute osapoolte vahelises vahetuses võimaldab see tehnika kahe tundliku andmepala samaaegset avalikustamist osalejate vahel. See protsess kõrvaldab vajaduse usalduse järele hetkelistes tehingutes nagu Coin Swap või Atomic Swap. Võtame näite, et seda paremini mõista. Alice ja Bob soovivad teineteisele saata 1 BTC, kuid nad ei usalda teineteist. Seetõttu kasutavad nad adaptor signatuure, et kõrvaldada vajadus usaldada teist osapoolt selles vahetuses (muutes selle seeläbi "atomiseks" vahetuseks). Nad toimivad järgmiselt:
* Alice algatab selle atomise vahetuse. Ta loob tehingu $m_A$, mis saadab 1 BTC Bobile. Ta loob allkirja $s_A$, mis valideerib selle tehingu kasutades oma privaatvõtit $p_A$ ($P_A = p_A \cdot G$) ja kasutades nonce'i $n_A$ ning salajast $t$ ($N_A = n_A \cdot G$ ja $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice arvutab adaptor signatuuri $s_A'$ salajase $t$ ja oma tõelise allkirja $s_A$ põhjal:  
$$s_A' = s_A - t$$
&nbsp;
* Alice saadab Bobile oma adaptor signatuuri $s_A'$, allkirjastamata tehingu $m_A$, punkti, mis vastab salajasele $T$, ja punkti, mis vastab nonce'ile $N_A$. Neid andmeid nimetame "adaptoriks". Pane tähele, et ainult selle teabega ei ole Bob võimeline Alice'i BTC-d taastama.
* Siiski saab Bob kontrollida, et Alice teda ei petaks. Selleks kontrollib ta, et Alice'i adaptor signatuur $s_A'$ vastab lubatud tehingule $m_A$. Kui järgnev võrrand on õige, siis on ta veendunud, et Alice'i adaptor signatuur on kehtiv: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* See kontroll annab Bobile kindlustunde Alice'ilt, nii et ta saab jätkata atomise vahetuse protsessiga rahulikult. Ta loob oma tehingu $m_B$, saates 1 BTC Alice'ile ja oma adaptor signatuuri $s_B'$, mis on seotud sama salajase $t$-ga, mida praegu ainult Alice teab (Bob ei tea seda väärtust $t$, vaid ainult selle vastavat punkti $T$, mille Alice on talle andnud): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob saadab Alice'ile oma adapteeritud allkirja $s_B'$, oma allkirjastamata tehingu $m_B$, punkti, mis vastab saladusele $T$, ja punkti, mis vastab nontsile $N_B$. Alice saab nüüd ühendada Bobi adapteeritud allkirja $s_B'$ saladusega $t$, mida ainult tema teab, et arvutada kehtiv allkiri $s_B$ tehingule $m_B$, mis saadab talle Bobi BTC-d: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice edastab selle allkirjastatud tehingu $m_B$ Bitcoin'i plokiahelasse, et taastada BTC, mille Bob talle lubas. Bob saab sellest tehingust plokiahelas teada. Seega on ta võimeline ekstraheerima allkirja $s_B = s_B' + t$. Selle teabe põhjal saab Bob eraldada kuulsa saladuse $t$, mida ta vajas:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Siiski oli see saladus $t$ ainus puuduv teave Bobile, et toota kehtiv allkiri $s_A$, Alice'i adapteeritud allkirjast $s_A'$, mis võimaldab tal kinnitada tehingut $m_A$, mis saadab BTC Alice'ilt Bobile. Ta arvutab seejärel $s_A$ ja edastab omakorda tehingu $m_A$: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$