---
term: TEMPO AJUSTADO À REDE (NAT)

---
Estimativa do tempo universal estabelecida nos relógios dos nós da rede. Cada nó calcula o seu NAT tomando a mediana das diferenças horárias entre o seu relógio local (UTC) e os dos nós a que está ligado, acrescentando depois o seu relógio local à mediana dessas diferenças, até um máximo de 70 minutos. O tempo ajustado à rede é, portanto, uma mediana dos tempos dos nós calculados localmente por cada nó. Este quadro de referência é então utilizado para verificar a validade das marcas de tempo dos blocos. Com efeito, para que um bloco seja aceite por um nó, a sua hora deve situar-se entre o MTP (hora mediana dos últimos 11 blocos minerados) e o NAT mais 2 horas:

```text
MTP < Valid Timestamp < (NAT + 2h)
```