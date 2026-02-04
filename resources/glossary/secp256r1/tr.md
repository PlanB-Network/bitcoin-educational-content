---
term: SECP256R1
definition: secp256k1'i tercih eden Bitcoin tarafından kullanılmayan, NIST standardına ait eliptik eğri.
---

Açık anahtar kriptografisi için NIST standardı tarafından tanımlanan bir eliptik eğriye verilen ad. Bu yöntem 256 bitlik bir asal alan ve $y^2 = x^3 + ax + b$ sabitli bir eliptik eğri denklemi kullanır:


```text
a = -3
```


ve


```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```


Secp256r1` eğrisi birçok protokolde yaygın olarak kullanılmaktadır, ancak Bitcoin'da kullanılmamıştır. Aslında, Satoshi Nakamoto 2009 yılında o zamanlar çok az bilinen `secp256k1` eğrisini tercih etmiştir. Bu seçimin kesin nedeni bilinmemektedir, ancak arka kapı riskini en aza indirmek olabilir. Gerçekten de $k1$ eğrisinin parametreleri $r1$ eğrisininkilerden çok daha basittir, özellikle de $b$ sabiti.


> ► *Bu eğri bazen "P-256" olarak da adlandırılır.*