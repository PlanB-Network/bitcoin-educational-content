---
term: SECP256K1
---

Ime dato specifičnoj eliptičnoj krivi korišćenoj u Bitcoin protokolu za implementaciju ECDSA (*Elliptic Curve Digital Signature Algorithm*) i Schnorr algoritama digitalnog potpisa. Kriva `secp256k1` je izabrana od strane pronalazača Bitcoin, Satoshi Nakamoto. Ima neke zanimljive osobine, posebno prednosti u performansama.


Korišćenje `secp256k1` u Bitcoin znači da je svaki privatni ključ (slučajni 256-bitni broj) mapiran na odgovarajući javni ključ kroz sabiranje i udvostručavanje tačke privatnog ključa pomoću generatora tačke krive `secp256k1`. Ova operacija je laka za izvođenje u jednom pravcu, ali praktično nemoguća za obrnuti, što čini osnovu sigurnosti digitalnih potpisa na Bitcoin.


Kriva `secp256k1` je specificirana jednačinom eliptične krive $y^2 = x^3 + 7$, što znači da ima koeficijente $a$ jednako $0$ i $b$ jednako $7$ u opštem obliku jednačine eliptične krive $y^2 = x^3 + ax + b$. `secp256k1` je definisana nad konačnim poljem čiji je red veoma veliki prost broj, konkretno $p = 2^{256} - 2^{32} - 977$. Kriva takođe ima red grupe, što je broj različitih tačaka na krivi, unapred definisanu generator tačku (ili tačku $G$), koja se koristi u kriptografskim operacijama za generate parove ključeva, i kofaktor jednak $1$.


> ► *“SEC” označava “Standards for Efficient Cryptography”. “P256” ukazuje da je kriva definisana nad poljem $\mathbb{Z}_p$ gde je $p$ 256-bitni prost broj. “K” se odnosi na ime njenog pronalazača, Neal Koblitz. Na kraju, “1” označava da je ovo prva verzija ove krive.*