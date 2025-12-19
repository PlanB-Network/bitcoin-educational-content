---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---

Bituma ubucuruzi butagira akamaro kiretse ivyo vyose bishitse:


- Ico kirundo ntikigira ubusa;
- Agaciro kari hejuru y'ikirundo ni kanini canke kangana na `0`;
- Ubwoko bw'igihe ni kimwe hagati y'umwanya `nLockTime` n'agaciro kari hejuru y'ikirundo (igihe nyaco canke umubare w'ibarabara);
- `nSequence` umurima w'inyungu ntungana na `0xffffffff`;
- Agaciro kari hejuru y'ikirundo ni kanini canke kangana n'agaciro k'umwanya `nLockTime` w'ibikorwa.


Iyo kimwe muri ivyo bitegekanijwe kitarangutse, inyandiko irimwo `OP_CHECKLOCKTIMEVERIFY` ntishobora gushitswako. Niba ivyo vyose bifise akamaro, rero `OP_CHECKLOCKTIMEVERIFY` ikora nka `OP_NOP`, bisobanura ko ata gikorwa na kimwe ikora ku nyandiko. Ni nk’aho vyozimangana. `OP_CHECKLOCKTIMEVERIFY` rero ishiraho umwanya wo gukoresha UTXO icungiwe n’inyandiko irimwo. Ivyo bishobora gukora mu buryo bw'itariki y'igihe ca Unix canke nk'umubare w'ibarabara. Kugira ngo ubikore, bigabanya agaciro gashoboka k'umwanya wa `nLockTime` w'isoko rikoresha, kandi uwo mwanya wa `nLockTime` ubwawo ugabanya igihe isohoka rishobora gushirwa mu gice.


> ► *Iyi opcode ni iyo gusubirira `OP_NOP`. Yashizwe kuri `OP_NOP2`. Akenshi yitwa n'ijambo ryayo ry'inyongera "CLTV". Iciyumviro, `OP_CLTV` ntikwiye gutera urujijo n'umwanya wa `nLockTime` w'ibikorwa. Aba mbere bakoresha aba nyuma, ariko kamere zabo n’ibikorwa vyabo biratandukanye.*