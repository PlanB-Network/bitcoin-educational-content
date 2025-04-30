---
term: TRUDNOŚĆ
---

Regulowany parametr, który określa złożoność Proof of Work wymaganą do dodania nowego bloku do Blockchain i uzyskania powiązanej nagrody. Trudność ta jest reprezentowana przez docelową trudność, 256-bitową wartość, która określa górną granicę, jaką musi spełnić Hash nagłówka bloku, aby został uznany za prawidłowy. Celem jest, aby Hash, osiągnięty poprzez podwójne wykonanie SHA256 (SHA256d), był mniejszy lub równy temu celowi. Aby osiągnąć Hash, górnicy manipulują `Nonce` w nagłówku bloku. Trudność dostosowuje się co 2016 bloków, czyli mniej więcej co dwa tygodnie, aby utrzymać średni czas tworzenia bloku na poziomie około 10 minut.