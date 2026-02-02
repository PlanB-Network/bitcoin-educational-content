---
term: 정책 (Miniscript)
definition: Miniscript에서 UTXO 소비 조건을 지정하기 위한 고수준 언어.
---

미니스크립트의 프레임워크 내에서 UTXO을 잠금 해제할 수 있는 조건을 간단하게 지정할 수 있는 높은 수준의 사용자 지향 언어입니다. 이 정책은 지출 규칙에 대한 추상적인 설명입니다. 그런 다음 Bitcoin의 기본 스크립트 언어의 연산과 일대일로 동등한 미니스크립트로 컴파일할 수 있습니다.





정책 언어는 미니스크립트 언어와 약간 다릅니다. 예를 들어 기본 경로가 키 A이고 복구 경로가 키 B이지만 타임록이 1년(약 52,560블록)인 보안 시스템을 상상해 보세요. 정책적으로는 이렇게 될 것입니다:


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


미니 스크립트로 컴파일되면 이렇게 됩니다:


```plaintext
andor(pk(B),older(52560),pk(A))
```


그리고 네이티브 스크립트로 변환되면 그렇게 될 것입니다:


```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```