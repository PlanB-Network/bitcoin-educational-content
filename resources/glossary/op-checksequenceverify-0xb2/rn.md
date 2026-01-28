---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

definition: Opcode ishiraho igihe ntarengwa kigereranije ku gukoresha UTXO.
---

Bihindura ubucuruzi butagira akamaro iyo kimwe muri ibi bimenyetso kibonetse:

*Ikirundo kiri ubusa;*


- Agaciro kari hejuru y'ikirundo ni munsi ya `0`;
- Ibendera ry'uguhagarika ry'agaciro kari hejuru y'ikirundo ntirisobanuwe kandi; Verisiyo y’ugucuruza iri munsi ya `2` canke; Ibendera ry'uguhagarika ry'umurima wa `nSequence` w'inyungu ryashizweho canke; Ubwoko bw'igihe c'ugufunga si kimwe hagati y'umwanya `nSequence` n'agaciro kari hejuru y'ikirundo (igihe nyaco canke umubare w'amabuye) canke; Agaciro kari hejuru y'ikirundo ni kanini kuruta agaciro k'umurima `nSequence` w'inyungu.


Iyo kimwe canke vyinshi muri ivyo bimenyetso vyerekanwa, inyandiko irimwo `OP_CHECKSEQUENCEVERIFY` ntishobora guhazwa. Niba ivyangombwa vyose bifise akamaro, rero `OP_CHECKSEQUENCEVERIFY` ikora nka `OP_NOP`, bisobanura ko ata gikorwa na kimwe ikora ku nyandiko. Ni nk’aho vyozimangana. `OP_CHECKSEQUENCEVERIFY` rero itera umwanya mutoyi ku bijanye n’ugukoresha UTXO icungiwe n’inyandiko irimwo. Ivyo bishobora kubikora mu buryo bw’igihe nyaco canke nk’umubare w’ibice. Kugira ngo ivyo bishoboke, bigabanya agaciro gashoboka k'umurima wa `nSequence` w'inyungu iwukoresha, kandi uwo mwanya wa `nSequence` ubwawo uragabanya igihe igikorwa kirimwo iyo nkuru gishobora gushirwa mu gice.


> ► *Iyi opcode ni iyo gusubirira `OP_NOP`. Yashizwe kuri `OP_NOP3`. Akenshi yitwa n'ijambo ryayo ry'inyongera "CSV". Iciyumviro, `OP_CSV` ntikwiye kuvyivanga n'umurima wa `nSequence` w'ibikorwa. Aba mbere bakoresha aba nyuma, ariko kamere zabo n’ibikorwa vyabo biratandukanye.*