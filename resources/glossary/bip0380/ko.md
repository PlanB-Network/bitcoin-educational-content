---
term: BIP0380
definition: HD 지갑의 출력 스크립트를 설명하기 위한 표준 언어인 Output Script Descriptors.
---

BIP380은 "출력 스크립트 설명자"라고 하는 HD Bitcoin 지갑에서 사용되는 출력 스크립트 모음을 설명하는 표준 언어를 도입합니다

목표는 출력 스크립트가 표현되고 관리되는 방식을 표준화하여 Wallet 백업, 내보내기 및 가져오기를 더 쉽게 만드는 것입니다.

설명자는 복구 구문과 같은 개인 데이터 외에도 HD Wallet에서 사용되는 키 쌍을 검색하는 데 필요한 모든 정보를 제공합니다. BIP380이 설명자에 대한 일반적인 프레임워크를 설명하는 반면, BIP381-BIP386은 개별 Descriptor 표현식 유형을 지정합니다. BIP380은 Bitcoin core 버전 0.17에서 다른 모든 Descriptor 관련 BIPs(BIP386 제외)와 함께 구현되었습니다.