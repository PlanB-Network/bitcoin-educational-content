---
term: Genesis 블록
---

Genesis 블록은 Bitcoin 시스템의 첫 번째 블록입니다. 이는 Bitcoin의 구체적인 출시를 의미합니다. Genesis 블록은 2009년 1월 3일에 Bitcoin의 익명의 창시자인 Satoshi 나카모토에 의해 만들어졌습니다. Hash는


```text
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```


이 블록에는 Miner(이 경우 Satoshi 나카모토 본인)에 대한 보상으로 50 비트코인을 생성하는 Coinbase Transaction만 포함되어 있습니다. 이 블록에는 Coinbase Transaction에 포함된 메시지가 포함되어 있습니다:


```text
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```


이 인용문은 *The Times* 신문의 기사를 인용한 것입니다. 이 메시지는 전통적인 금융 시스템과 그 과잉에 대한 비판으로 해석되며, 이는 부분적으로 화폐 대안으로 Bitcoin을 만들게 된 동기가 되었습니다.


Bitcoin Blockchain의 첫 번째 블록을 구현하기 때문에, Genesis 블록에는 이전 블록의 Hash를 포함하는 필드가 분명히 없습니다(존재하지 않기 때문입니다). 또한, 이 블록에서 보상으로 생성된 50 비트코인은 프로토콜 수준에서 사용할 수 없습니다.