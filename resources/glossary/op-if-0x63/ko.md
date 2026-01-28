---
term: OP_IF (0X63)
---

스택 맨 위에 있는 값이 0이 아닌 경우(true) 스크립트의 다음 부분을 실행합니다. 값이 0(거짓)이면 이러한 연산을 건너뛰고 `OP_ELSE`가 있는 경우 바로 그 뒤에 있는 연산으로 이동합니다. oP_IF`는 스크립트 내에서 조건부 제어 구조를 실행할 수 있게 해줍니다. 트랜잭션 실행 시점에 제공된 조건에 따라 스크립트에서 제어 흐름을 결정합니다. oP_IF`는 다음과 같은 방식으로 `OP_ELSE` 및 `OP_ENDIF`와 함께 사용됩니다:


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```