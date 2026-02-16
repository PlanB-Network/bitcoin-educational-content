---
term: 페더슨 커밋먼트
definition: 값을 공개하지 않고 합계를 검증할 수 있는 준동형 암호화 약정.
---

Pedersen commitment은 더하기 연산과 동형성이라는 특성을 가진 암호화 Commitment의 한 유형입니다. 즉, 개별 값을 공개하지 않고도 두 커미트먼트의 합계를 검증할 수 있습니다.


공식적으로는 :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


다음 :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


이 속성은 예를 들어 RGB와 같은 암호화폐 시스템에서 교환된 토큰의 양을 숨기면서도 총액을 확인할 수 있을 때 유용합니다.