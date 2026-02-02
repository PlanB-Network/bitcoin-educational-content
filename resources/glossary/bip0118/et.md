---
term: BIP0118

definition: ANYPREVOUTi ettepanek, mis toob sisse uued SigHash lipud, võimaldades allkirjade taaskasutamist tehingute vahel, mis on kasulik Eltoo jaoks.
---
Ettepanek Bitcoini täiustamiseks, mille eesmärk on võtta kasutusele kaks uut SigHash Flagi modifikaatorit: `SIGHASH_ANYPREVOUT` ja `SIGHASH_ANYPREVOUTANYSCRIPT`. Need funktsioonid laiendavad Bitcoini tehingute võimalusi, eelkõige seoses nutikate lepingute ja ülekandevõrgustiku (nt Lightning Network) sarnaste lahendustega. BIP118 võimaldaks eelkõige Eltoo kasutamist. `SIGHASH_ANYPREVOUT` peamine eelis on allkirjade taaskasutamise võimaldamine mitme tehingu puhul, mis pakub suuremat paindlikkust. Konkreetselt võimaldavad need SigHashes allkirja, mis ei hõlma ühtegi tehingu sisendit.