---
term: ADAPTERI ALLKIRI

---
Krüptograafiline meetod, mis võimaldab kombineerida ehtsat allkirja täiendava allkirjaga (nn "adapterallkiri"), et paljastada salajane andmestik. See meetod töötab nii, et kahe elemendi teadmine kehtiva allkirja, adapterallkirja ja salajase allkirja hulgast võimaldab tuletada puuduva kolmanda elemendi. Üks selle meetodi huvitavaid omadusi on see, et kui me teame oma vastaspoole adaptori allkirja ja selle adaptori allkirja arvutamiseks kasutatud salaga seotud elliptilise kõvera konkreetset punkti, siis saame tuletada oma adaptori allkirja, mis vastab samale saladusele, ilma et meil oleks otsene juurdepääs saladusele endale. Kahe üksteist mitte usaldava sidusrühma vahelises teabevahetuses võimaldab see tehnika kahe tundliku teabe üheaegset paljastamist osalejate vahel. See protsess välistab vajaduse usalduse järele hetkeliste tehingute puhul, nagu näiteks mündivahetuse või aatomivahetuse puhul. Võtame selle paremaks mõistmiseks näite. Alice ja Bob soovivad saata üksteisele 1 BTC, kuid nad ei usalda teineteist. Seetõttu kasutavad nad adaptori allkirju, et eirata vajadust usalduse järele teise osapoole suhtes selles vahetuses (seega on tegemist "aatomilise" vahetusega). Nad toimivad järgmiselt:


- Alice algatab selle aatomivahetuse. Ta loob tehingu $m_A$, mis saadab Bobile 1 BTC. Ta loob allkirja $s_A$, mis kinnitab selle tehingu, kasutades oma isiklikku võtit $p_A$ ($P_A = p_A \cdot G$) ning kasutades nonce $n_A$ ja salajust $t$ ($N_A = n_A \cdot G$ ja $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \paralleel P_A \paralleel m_A) \cdot p_A$$$

&nbsp;


- Alice arvutab adapteri allkirja $s_A'$ salajase $t$ ja oma tegeliku allkirja $s_A$ põhjal:

$$s_A' = s_A - t$$$

&nbsp;


- Alice saadab Bobile oma adapteri allkirja $s_A'$, oma allkirjastamata tehingu $m_A$, punkti, mis vastab saladusele $T$, ja punkti, mis vastab nonce'ile $N_A$. Nimetame neid teabetükke "adaptoriks". Pange tähele, et ainult selle teabega ei ole Bob võimeline Alice'i BTC-d tagasi saama.
- Bob saab siiski kontrollida, et Alice ei peta teda. Selleks kontrollib ta, kas Alice'i adapteri allkiri $s_A'$ vastab lubatud tehingule $m_A$. Kui järgmine võrrand on õige, siis on ta veendunud, et Alice'i adapteri allkiri on kehtiv:

$$s_A' \cdot G = N_A + H(N_A + T \paralleel P_A \paralleel m_A) \cdot P_A$$$

&nbsp;


- See kontrollimine annab Bobile Alice'i kinnituse, nii et ta saab rahulikult jätkata aatomivahetuse protsessi. Seejärel loob ta oma tehingu $m_B$, millega saadab Alice'ile 1 BTC ja oma adapteri allkirja $s_B'$, mis on seotud sama saladusega $t$, mida esialgu teab ainult Alice (Bob ei tea seda väärtust $t$, vaid ainult selle vastavat punkti $T$, mille Alice on talle andnud): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$$

&nbsp;


- Bob saadab Alice'ile oma adapteri allkirja $s_B'$, oma allkirjastamata tehingu $m_B$, punkti, mis vastab saladusele $T$, ja punkti, mis vastab nonce'ile $N_B$. Alice saab nüüd kombineerida Bobi adapteri allkirja $s_B'$ ja saladuse $t$, mida teab ainult tema, et arvutada kehtiv allkiri $s_B$ tehingu $m_B$ jaoks, mis saadab talle Bobi BTC:

$$s_B = s_B' + t$$$

&nbsp;

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \paralleel P_B \paralleel m_B) \cdot P_B$$$

&nbsp;


- Alice edastab selle allkirjastatud tehingu $m_B$ Bitcoini plokiahelas, et saada tagasi BTC, mida Bob talle lubas. Bob saab sellest tehingust teada plokiahelas. Seega saab ta välja võtta allkirja $s_B = s_B' + t$. Selle teabe põhjal saab Bob eraldada kuulsa saladuse $t$, mida ta vajas:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$$

&nbsp;


- See saladus $t$ oli aga ainus puuduv teave, mille abil Bob sai Alice'i adapteri allkirja $s_A'$ põhjal esitada kehtiva allkirja $s_A$, mis võimaldab tal valideerida tehingu $m_A$, millega Alice'ilt BTC saadetakse Bobile. Seejärel arvutab ta $s_A$ ja edastab omakorda tehingu $m_A$: $$s_A = s_A' + t$$$

&nbsp;

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \paralleel P_A \paralleel m_A) \cdot P_A$$
