---
term: P2SH
definition: Script yemerera ibisabwa mu gukoresha bitandukanye biciye muri hash ya redeemScript.
---

P2SH bisobanura *Ishura ku nyandiko Hash*. Ni urugero rw'inyandiko rusanzwe rukoreshwa mu gushinga ivyangombwa vyo gukoresha amahera kuri UTXO. Udakunze inyandiko za P2PK na P2PKH, aho ivyangombwa vyo gukoresha amahera bitegekanijwe imbere y’igihe, P2SH iremeza gushiramwo ivyangombwa vyo gukoresha amahera ataco bimaze n’ibindi bikorwa vy’inyongera mu nyandiko y’ugucuruza.


Mu buryo bw'ubuhinga, mu gucuruza P2SH, `scriptPubKey` irimwo Hash y'ibanga y'i `redeemscript`, aho gutanga ivyangombwa vy'ugukoresha amahera. Iyi Hash iboneka hakoreshejwe Hash `SHA256`. Iyo wohereje ama bitcoins kuri P2SH Address, `redeemscript` iri munsi yayo ntihishurwa. Hash yayo yonyene ni yo iri muri iyo nzira. Aderesi za P2SH zishizwe muri `Base58Check` kandi zitangura n'umubare `3`. Iyo uwuronka amafaranga yipfuza gukoresha amafaranga y’ama bitcoins yaronse, ategerezwa gutanga `redeemscript` ihuye na Hash iri muri `scriptPubKey`, hamwe n’amakuru akenewe kugira ngo yuzuze ivyangombwa vy’iyi `redeemscript`. Nk’akarorero, mu nyandiko y’imikono myinshi ya P2SH, iyo nyandiko yoshobora gusaba imikono iva ku mfunguruzo nyinshi z’ibanga.


Gukoresha P2SH biratuma umuntu ashobora guhindura uko abona ibintu, kuko bituma umuntu ashobora kwubaka inyandiko zidasanzwe ata wuzirungitse azi ido n’ido. P2SH yashizweho mu 2012 na BIP16.