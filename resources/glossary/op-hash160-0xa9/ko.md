---
term: OP_HASH160 (0XA9)
definition: 최상단 요소를 SHA256으로 해싱한 후 RIPEMD160으로 다시 해싱하는 Opcode.
---

스택에서 최상위 요소를 가져와 `SHA256`과 `RIPEMD160` 함수를 동시에 사용하여 해당 Hash으로 대체합니다. 이 2단계 프로세스는 160비트 지문을 생성합니다.