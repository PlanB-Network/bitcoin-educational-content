---
term: 페이로드
definition: 더 큰 데이터 패킷 내에 실려 전달되는 핵심 데이터.
---

컴퓨팅의 일반적인 맥락에서 페이로드는 더 큰 데이터 패킷에 포함된 필수 데이터입니다. 예를 들어, Bitcoin Address을 통한 SegWit V0에서 페이로드는 다양한 메타데이터(HRP, 구분자, SegWit 버전 및 체크섬)가 없는 공개키의 Hash에 해당합니다. 예를 들어, Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`에는 :




- `bc`: 사람이 읽을 수 있는 부분(HRP) ;
- 1`: 구분 기호 ;
- `q`: SegWit 버전. 이것은 버전 0입니다;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: 페이로드, 이 경우 공개 키의 Hash입니다;
- `ys50gj`: 체크섬.