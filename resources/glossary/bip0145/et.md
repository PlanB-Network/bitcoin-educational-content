---
term: BIP0145

definition: JSON-RPC getblocktemplate väljakutse värskendus SegWiti toe integreerimiseks ja tehingute kaalu arvutamiseks.
---
Uuendab JSON-RPC-kõne "getblocktemplate", et lisada tugi SegWitile vastavalt BIP141-le. See uuendus võimaldab kaevandajatel konstrueerida plokke, võttes arvesse SegWitiga kasutusele võetud tehingute ja plokkide uut "kaalu" mõõtmist ning muid parameetreid, näiteks sigops-limiidi arvutamist.