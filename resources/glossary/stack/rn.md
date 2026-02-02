---
term: Pile
definition: Uburyo bwa LIFO bwo kubika amakuru bukoreshwa muri Bitcoin Script mu kubika no gukoresha ibintu vy'agateganyo mu gihe bishirwa mu ngiro.
---

Mu bijanye n’ururimi rw’inyandiko rukoreshwa mu gushiramwo ivyangombwa vyo gukoresha amahera kuri Bitcoin UTXOs, ikirundo ni LIFO (*Last In, First Out*) imiterere y’amakuru ikoreshwa mu kubika Elements y’igihe gito mu gihe c’ugushirwa mu ngiro kw’inyandiko. Igikorwa kimwe cose kiri mu nyandiko gikoresha ivyo birundo, aho Elements ishobora kwongerwako (*push*) canke igakurwaho (*pop*). Ivyanditswe bikoresha ibirundo vyo gusuzuma imvugo, kubika ibihinduka vy'igihe gito no gucunga ivyangombwa.


Igihe ukora inyandiko ya Bitcoin, ibirundo 2 birashobora gukoreshwa: ibirundo nyamukuru n'ibirundo vya alt (ibindi). Igitero nyamukuru gikoreshwa ku bikorwa vyinshi vy'inyandiko. Ni kuri iki kirundo aho ibikorwa vy'inyandiko vyongera, bikuraho canke bikoresha amakuru. Ku rundi ruhande, ikirundo c'ibindi gikoreshwa mu kubika amakuru mu gihe c'ugushirwa mu ngiro kw'inyandiko. Amakode yihariye, nka `OP_TOALTSTACK` na `OP_FROMALTSTACK`, aguha uburenganzira bwo kwimurira Elements kuva ku kirundo nyamukuru uja ku kirundo gisubirira n'ibihushanye n'ivyo.


Nk’akarorero, iyo igikorwa cemejwe, imikono n’imfunguruzo za bose birasunikwa ku kirundo nyamukuru maze bikatunganirizwa n’ama opcode akurikirana kugira ngo hasuzumwe ko iyo mikono ihuye n’imfunguruzo n’amakuru y’igicuruzwa.