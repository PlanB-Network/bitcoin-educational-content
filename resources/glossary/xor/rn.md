---
term: XOR
definition: Uburyo bwo gukora mu buhinga bwa orudinatere butanga ukuri igihe gusa ivyakozwe bitandukanye.
---

Inyuguti y'igikorwa "Idasanzwe canke," mu gifaransa "Ou exclusif." Ni igikorwa nyamukuru c’ubuhinga bwa Boolean. Iyi nzira ifata ibikorwa bibiri vya Boolean, kimwe cose kikaba ari $ukuri$ canke $ikinyoma$, kandi kigatanga igisubizo c'ukuri$ iyo gusa ivyo bikorwa bibiri bitandukanye. Mu yandi majambo, igisohoka c'igikorwa ca XOR ni $ukuri$ nimba kimwe (ariko si vyose) mu bikorwa ari $ukuri$. Nk'akarorero, igikorwa ca XOR kiri hagati ya $1$ na $0$ kizovamwo $1$. Turabona:


$$
1 \oplus 0 = 1
$$


Na vyo nyene, igikorwa ca XOR gishobora gukorwa ku rutonde rurerure rw’ibice. Nk'akarorero:


$$
10110 \oplus 01110 = 11000
$$


Buri biti biri mu rukurikirane bigereranywa n’ibindi, hanyuma igikorwa ca XOR kigakoreshwa. Aha niho hari imbonerahamwe y'ukuri y'igikorwa ca XOR:


<div guhuza="hagati">


| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>


Igikorwa kijanye na XOR gikoreshwa mu bice vyinshi vy'ubuhinga bwa mudasobwa, cane cane mu vy'ubuhinga bwa mudasobwa, kubera ibiranga bishimishije nka:


- Uguhindura kwayo: urutonde rw’ibikorwa ntirugira ico rukoze ku ciyumviro. Ku bihinduka bibiri vyatanzwe $D$ na $E$: $D \ugushiramwo E = E \ugushiramwo D$;

**Ubufatanye bwayo:** ugushira mu mirwi ibikorwa ntibigira ico bikoze ku ciyumviro. Ku bihinduka bitatu vyatanzwe $A$, $B$, na $C$: $(A \ivyongera B) \ivyongera C = A \ivyongera (B \ivyongeyeko C)$;


- Ifise ikintu kitagira aho kigarukira $0$: igikorwa xored na $0$ kizokwama kingana n'igikorwa. Ku mpinduka yatanzwe $A$: $A \oplus 0 = A$;
- Ikintu cose ni inverse yaco bwite. Ku muhinduzi watanzwe $A$: $A \wongereyeko A = 0$.


Mu bijanye na Bitcoin, biragaragara ko igikorwa ca XOR gikoreshwa ahantu henshi. Nk’akarorero, XOR ikoreshwa cane mu gikorwa ca SHA256, gikoreshwa cane mu nzira ya Bitcoin. Hariho ama protocoles nka *SeedXOR* ya Coldcard nayo akoresha iyo primitive ku bindi bikorwa. Iboneka kandi muri BIP47 kugira ngo ipfuke kode y’ukwishura ishobora gusubirwamwo mu gihe iriko irarungikwa.

Mu bijanye n'ubuhinga bwo gupfuka amakuru, XOR ishobora gukoreshwa nk'uko iri nk'ubuhinga bwo gupfuka amakuru buhuye. Iryo koraniro ryitwa "One-Time Pad" canke "Vernam Cipher", ryitwa izina ry'uwarihinguye. Naho bidashoboka kubera uburebure bw’urufunguzo, iyo nzira ni imwe mu nzira zonyene zo gupfuka amakuru zizwi ko zitekanye ataco zisaba.