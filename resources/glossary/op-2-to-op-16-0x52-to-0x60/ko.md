---
term: OP_2 TO OP_16(0x52~0X60)

---

OP_2`부터 `OP_16`까지의 옵코드는 2~16의 각 숫자 값을 스택에 밀어 넣습니다. 작은 숫자 값을 삽입할 수 있도록 하여 스크립트를 단순화하는 데 사용됩니다. 이 유형의 옵코드는 특히 다중 서명 스크립트에서 많이 사용됩니다. 다음은 2/3 다중 서명을 위한 `scriptPubKey`의 예시입니다:


```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```


> ► *이 모든 옵코드는 OP_PUSHNUM_N.*이라고도 합니다