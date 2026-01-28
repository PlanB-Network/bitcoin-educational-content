---
term: Discrete logarithm
definition: Ikibazo ca kime kigoye gutorera inyishu kigize ishingiro ry'umutekano wa cryptography kuri Bitcoin.
---

Logarithme itandukanye ni ikibazo c'imibare gikoreshwa mu mirongo imwe imwe y'urufunguzo rwa bose. Mu mugwi w’ingendo w’urutonde $q$, ufise umuyagankuba $g$, iyo umuntu afise ingano y’uburyo $g^x = h$, rero $x$ yitwa logarithme itandukanye ya $h$ ku bijanye n’ishimikiro $g$, modulo $q$. Mu majambo yoroshe, birimwo kumenya igiharuro $x$ igihe $g$, $h$, na $q$ bizwi. Logarithme itandukanye rero ni inverse y'igiharuro mu mugwi w'inzinguzingu zifise impera. Ariko rero, ku gaciro kanini ka $q$, gutorera umuti ingorane y’ubuhinga bwa logarithme butandukanye bifatwa nk’ibigoye mu buryo bw’ubuhinga. Iyi nzira ikoreshwa kugira ngo haboneke umutekano w'amasezerano menshi y'ubuhinga bwo gukingira amakuru, nk'amasezerano ya Diffie-Hellman y'urufunguzo Exchange.


Iryo logarithme ry’ibintu bitandukanye rikoreshwa kandi mu gukora amakuru y’ibara ry’uruzitiro (ECC), harimwo no muri ECDSA (*Ibara ry’umukono ry’uruzitiro rw’uruzitiro*). Mu bijanye n’imirongo y’imirongo, ingorane ya logarithme itandukanye irashika no ku kurondera igiharuro $k$ ku buryo $k \cdot G = K$, aho $G$ na $K$ ari uturongo turi ku mirongo, kandi $\cdot$ igereranya igikorwa co gukubita uturongo. Mu bijanye na Bitcoin, inyandiko zishobora gukoresha ECDSA canke umurongo wa Schnorr kugira ngo zifunge UTXOs. Ivyo vyose bishingiye ku kudashoboka ko kubara logarithme itandukanye.