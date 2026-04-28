---
term: OP_IF (0X63)

definition: Opcode ikora igice ca script mu gihe ibintu biri k’inyuma ku mupfundikizo ari ukuri.
---

Ikora igice gikurikira c'inyandiko iyo agaciro kari hejuru y'ikirundo atari zero (ukuri). Iyo agaciro ari zero (ikinyoma), ivyo bikorwa birasimburwa, bikaja ku bikurikira `OP_ELSE`, iyo biriho. `OP_IF` ishoboza gutanguza uburyo bwo kugenzura bushingiye ku bintu mu nyandiko. Igena urugendo rw’ubugenzuzi mu nyandiko ishingiye ku ngingo yatanzwe igihe igikorwa co gucuruza gikorwa. `OP_IF` ikoreshwa na `OP_ELSE` na `OP_ENDIF` mu buryo bukurikira:


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```