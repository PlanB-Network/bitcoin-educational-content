---
term: BIP0386
definition: 디스크립터에서 Taproot 출력을 설명하기 위한 tr() 함수.
---

Taproot용 Descriptor 함수를 소개합니다. 여기서는 Taproot 출력을 찾기 위한 함수 `tr(KEY)`와 `tr(KEY, TREE)`를 정의하며, 여기서 `KEY`는 내부 키이고 `TREE`는 선택적 스크립트 경로 트리입니다. BIP386은 Bitcoin core 버전 22.0에서 구현되었습니다.