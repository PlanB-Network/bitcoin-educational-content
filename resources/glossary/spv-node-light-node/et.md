---
term: SPV-SÕLM (VALGUSSÕLM)

---
SPV-sõlm (*Simple Payment Verification*), mida mõnikord nimetatakse "kergsõlmeks", on Bitcoini sõlme kergekaaluline klient, mis võimaldab kasutajatel tehinguid kinnitada ilma kogu plokiahelat salvestamata. Selle asemel salvestab SPV-sõlm ainult plokkide päised ja saab vajaduse korral teavet konkreetsete tehingute kohta, küsides täielikku sõlme. Selle kontrollimise põhimõtte teeb võimalikuks Bitcoini plokkide tehingute struktuur, mis on korraldatud krüptograafilises akumulaatoris (Merkle Tree).

Selline lähenemisviis on kasulik piiratud ressurssidega seadmete, näiteks mobiiltelefonide puhul. Siiski sõltuvad SPV-sõlmed teabe kättesaadavuse osas täissõlmedest, mis tähendab täiendavat usalduse taset ja sellest tulenevalt väiksemat turvalisust võrreldes täissõlmedega. SPV-sõlmed ei saa iseseisvalt tehinguid kinnitada, kuid nad saavad kontrollida, kas tehing on plokis, konsulteerides Merkle'i tõenditega.