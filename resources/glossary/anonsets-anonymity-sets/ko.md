---
term: Anonsets (anonymity sets)
definition: UTXO의 개인 정보 보호 정도를 세트에서 구별 불가능한 UTXO의 수를 세어서 측정하는 지표로, 일반적으로 coinjoin 후입니다.
---
Anonset은 특정 UTXO의 프라이버시 수준을 평가하기 위한 지표로 사용된다. 보다 구체적으로는, 분석 대상 코인을 포함하는 집합 내에서 구별할 수 없는 UTXO의 수를 측정한다. 동일한 UTXO들의 집합이 필요하기 때문에, anonset은 일반적으로 coinjoin 주기 내에서 계산된다. 이를 통해 필요한 경우 coinjoin의 품질을 평가할 수 있다. anonset의 크기가 클수록 익명성 수준이 높아지며, 집합 내에서 특정 UTXO를 구별하기가 어려워진다.

Anonset에는 두 가지 유형이 존재한다. forward anonset (forward-looking metrics)과 backward anonset (backward-looking metrics)이다. anonset을 지칭하기 위해 "*score*"라는 용어가 사용되기도 한다.

첫 번째는 입력 UTXO가 알려진 상태에서, 분석 대상인 출력 UTXO가 숨어 있는 그룹의 크기를 나타낸다. 이 지표는 과거에서 현재로의 분석(입력에서 출력)에 대한 코인의 프라이버시 저항성을 측정할 수 있게 한다. 두 번째는 출력 UTXO가 알려진 상태에서, 특정 코인에 대해 가능한 출처의 수를 나타낸다. 이 지표는 현재에서 과거로의 분석(출력에서 입력)에 대한 코인의 프라이버시 저항성을 측정할 수 있게 한다.
















