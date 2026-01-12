---
term: Commitment
---

(암호학적 의미에서) Commitment은 구조화된 데이터 $m$(메시지)와 임의의 값 $r$에 대한 연산에서 결정론적으로 파생된 $C$로 표시되는 수학적 객체입니다. 우리는 :


$$
C = \text{commit}(m, r)
$$


이 메커니즘은 두 가지 주요 작업으로 구성됩니다:




- 커밋: 메시지 $m$과 임의의 $r$에 암호화 함수를 적용하여 $C$ 를 생성합니다;
- 확인: $C$, $m$ 메시지 및 $r$ 값을 사용하여 이 Commitment가 올바른지 확인합니다. 이 함수는 `True` 또는 `False`를 반환합니다.


Commitment는 두 가지 속성을 준수해야 합니다:




- 바인딩: 동일한 $C$ 를 생성하는 두 개의 서로 다른 메시지를 찾을 수 없어야 합니다:


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


와 같은 :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- 숨기기: $C$에 대한 지식이 $m$의 내용을 드러내지 않아야 합니다.


RGB 프로토콜의 경우, 정보 자체를 공개하지 않고 특정 시점에 특정 정보의 존재를 증명하기 위해 Commitment를 Bitcoin 트랜잭션에 포함시킵니다.