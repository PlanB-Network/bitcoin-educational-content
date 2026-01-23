---
term: BIP0111
definition: 노드가 블룸 필터(BIP37) 지원을 신호할 수 있게 하는 NODE_BLOOM 서비스 비트 추가.
---

노드가 BIP37에 설명된 대로 블룸 필터에 대한 지원을 명시적으로 알릴 수 있도록 `NODE_BLOOM`이라는 서비스 비트의 추가를 제안합니다. 노드 운영자는 `NODE_BLOOM`의 도입으로 이 서비스를 비활성화하여 DoS의 위험을 줄일 수 있습니다. BIP37 옵션은 Bitcoin core에서 기본적으로 비활성화되어 있습니다. 활성화하려면 설정 파일에 `peerbloomfilters=1` 파라미터를 입력해야 합니다.