---
term: Hrp (human readable part)
definition: Bitcoin 주소 유형을 식별할 수 있는 bech32 주소의 읽기 가능한 접두사입니다.
---

HRP는 "사람이 읽을 수 있는 부분"의 약자로, bech32 및 bech32m(SegWit v0 및 SegWit v1) 수신 주소의 구성 요소입니다. HRP는 Address에서 사람이 쉽게 읽고 해석할 수 있도록 특별히 포맷된 부분을 말합니다. 예를 들어 bech32 Bitcoin Address을 생각해 보세요:


```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```


이 Address에서 이니셜 `bc`는 HRP를 나타냅니다. 이 접두사를 사용하면 제시된 문자열이 다른 것이 아니라 Bitcoin Address임을 빠르게 식별할 수 있습니다.