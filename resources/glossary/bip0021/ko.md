---
term: BIP0021
---

닐스 슈나이더와 매트 코랄로가 작성한 제안서로, 루크 대쉬르가 작성한 BIP20을 기반으로 하며, 이 문서 역시 닐스 슈나이더가 작성한 다른 문서에서 파생된 것입니다.

BIP21은 결제를 용이하게 하기 위해 수신 주소가 URI(*Uniform Resource Identifier*)로 인코딩되는 방식을 정의합니다. 예를 들어, "Pandul"이라는 레이블로 0.1 BTC를 요청하는 BIP21을 따르는 Bitcoin URI는 다음과 같은 형태입니다:


```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```


이 표준화는 링크를 클릭하거나 QR 코드를 스캔하는 것만으로 결제를 시작할 수 있도록 하여 Bitcoin 거래의 사용자 경험을 개선합니다. 현재 BIP21 표준은 Bitcoin Wallet 소프트웨어에 널리 채택되어 있습니다.