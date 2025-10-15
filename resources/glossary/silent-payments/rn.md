---
term: IVYISHURA BICECERE
---

Uburyo bwo gukoresha aderesi za Bitcoin zidahinduka kugira ngo umuntu aronke amahera ata Address isubira gukoresha, ata gukorana, kandi ata n’ihuriro riboneka rya On-Chain hagati y’amahera atandukanye na Address idahinduka. Ubwo buryo burakuraho ivy’ugutanga amaderesi mashasha, atakoreshwa yo kwakira generate ku bijanye n’ugucuruza kwose, gutyo hakaba umuntu yirinda imigenderanire isanzwe muri Bitcoin aho uwuronka ategerezwa gutanga Address nshasha ku wuyitanga.


Mu kwishura mu gacerere, uwuriha akoresha imfunguruzo za bose z’uwuronka (akoresha urufunguzo rwa bose no gucapura urufunguzo rwa bose) n’umubare w’imfunguruzo zabo bwite nk’inyungu kuri generate Address nshasha ku kwishura kwose. Uwuronka, n'imfunguruzo ziwe z'ibanga, ni we wenyene ashobora guharura urufunguzo rw'ibanga rujanye n'iyi nyishu Address. ECDH (*Elliptic-Curve Diffie-Hellman*), urufunguzo rw’ubuhinga bwa none Exchange, rukoreshwa mu gushinga ibanga ry’abantu bose rikoreshwa mu gukuraho Address yakira n’urufunguzo rw’ibanga (ku ruhande rw’uwuronka gusa). Kugira ngo bamenye Ivyishyurwa vy’Iceceka vyagenewe, ababironka bategerezwa gucapura Blockchain maze bagasuzuma igikorwa cose gihuye n’ingingo ngenderwako z’itegeko. Udakunze BIP47, ikoresha igikorwa co kumenyesha kugira ngo ishingeho umurongo wo kwishura, Silent Payments irakuraho iyo ntambwe, ikazigama igikorwa. Ariko rero, ikintu co gusenyera ku mugozi umwe ni uko uwuronka ategerezwa gucapura amafaranga yose ashobora gukoreshwa kugira ngo amenye, mu gukoresha ECDH, nimba ari we yarungikiwe.


Nk'akarorero, Bob's static Address $B$ igereranya uguhuza urufunguzo rwiwe rwa bose rwo gucapura n'urufunguzo rwiwe rwa bose rwo gukoresha:


$$ B = B_{\umwandiko{gupima}} \umwandiko{‖ } B_{\umwandiko{gukoresha}} $$


Izo mfunguruzo zikomoka gusa ku nzira ikurikira:


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


Iyi Address idahinduka isohowe na Bob. Alice irayigarura kugira ngo yishure Bob mu gacerere. Aharura amahera Bob yishuye Address $P_0$ muri ubu buryo:


$$ P_0 = B_{\umwandiko{gukoresha}} + \umwandiko{Hash}(\umwandiko{injizaHash} \cdot a \cdot B_{\umwandiko{gupima}} \cdot{ ‖ } 0) \cdot G $$


Hehe:


$$ \umwandiko{injizaHash} = \umwandiko{Hash}(\umwandiko{isohoka}_L \umwandiko{‖ } A) $$


Hamwe:


- $B_{\umwandiko{gupima}}$: Urufunguzo rwa bose rwo gupima rwa Bob (Address idahinduka);
- $B_{\umwandiko{gukoresha}}$: Urufunguzo rwa bose rwa Bob (Address idahinduka);

**$A$**: Umubare w'imfunguruzo za bose mu kwinjiza (tweak);


- $a$: Urufunguzo rwihariye rwa tweak, ni ukuvuga umubare w'urufunguzo rwose rwakoreshejwe muri `scriptPubKey` rw'ama UTXO yakoreshejwe nk'inyungu mu gucuruza kwa Alice;
- $\text{outpoint}_L$: UTXO ntoyi cane (mu rurimi rw'inkoranyabumenyi) ikoreshwa nk'inyungu mu gucuruza kwa Alice;

**‖**: Gufatanya (igikorwa co gufatanya ibikorwa kuva ku mpera kugeza ku mpera);


- $G$: Igiharuro c'umuyagankuba c'umurongo w'uruzitiro `secp256k1`;
- $\umwandiko{Hash}$: Umurimo wa SHA256 Hash washizweko ikimenyetso `BIP0352/Ibanga Risangiwe`;
- $P_0$: Urufunguzo rwa mbere rwa bose / Address yihariye yo kwishura Bob;

**$0$**: Umubare wose ukoreshwa kuri generate amaderesi menshi yihariye yo kwishura.


Bob aca scanner Blockchain kugira aronke Ukwishyura kwiwe kw’Iceceka muri ubu buryo:


$$ P_0 = B_{\umwandiko{gukoresha}} + \umwandiko{Hash}(\umwandiko{injizaHash} \cdot b_{\umwandiko{gupima}} \cdot A \umwandiko{ ‖ } 0) \cdot G $$


Hamwe:


- $b_{\umwandiko{gupima}}$: Urufunguzo rwo gupima rw'ibanga rwa Bob.


Iyo asanze $P_0$ ari Address irimwo Silent Payment imugenewe, abara $p_0$, urufunguzo rw’ibanga rumufasha gukoresha amahera yoherejwe na Alice kuri $P_0$:


$$ p_0 = (b_{\umwandiko{gukoresha}} + \umwandiko{Hash}(\umwandiko{injizaHash} \cdot b_{\umwandiko{gupima}} \cdot A \umwandiko{ ‖ } 0)) \mod n $$


Hamwe:


- $b_{\igisomwa{gukoresha}}$: Urufunguzo rw'ugukoresha rw'ibanga rwa Bob;
- $n$: urutonde rw'umurongo w'umurongo `secp256k1`.


Uretse iyo verisiyo y’ishimikiro, amabara arashobora kandi gukoreshwa kuri generate amaderesi menshi atandukanye avuye kuri Address imwe y’ishimikiro, n’intumbero yo gutandukanya ikoreshwa ryinshi ata kugwiza mu buryo budasanzwe igikorwa gikenewe mu gihe co gupima.