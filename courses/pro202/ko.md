---
name: Bitcoin 프로그래밍
goal: 처음부터 완전한 Bitcoin 라이브러리를 구축하고 Bitcoin의 암호화 기반을 이해하세요
objectives: 

 - 파이썬에서 유한 필드 산술 및 타원 곡선 연산 구현하기
 - 프로그래밍 방식으로 Bitcoin 트랜잭션 구성 및 구문 분석하기
 - Testnet 주소를 생성하고 네트워크를 통해 트랜잭션을 브로드캐스트합니다
 - Bitcoin의 보안 모델의 기본이 되는 수학적 기초를 마스터하세요

---
# Bitcoin의 스크립트 및 프로그램으로의 여정


지미 송이 진행하는 이 이틀간의 집중 강좌에서는 완벽한 Bitcoin 라이브러리를 처음부터 구축하여 Bitcoin의 기술적 기초를 심도 있게 다룹니다. 유한 필드와 타원 곡선의 필수 수학부터 시작하여 트랜잭션 구문 분석, 스크립트 실행 및 네트워크 통신을 진행하게 됩니다. Jupyter 노트북에서 실습 코딩 연습을 통해 나만의 Testnet Address을 만들고, 트랜잭션을 수동으로 구성하고, 네트워크에 직접 브로드캐스트하면서 Bitcoin과 Trustless을 안전하게 만드는 암호화 원리를 깊이 있게 이해하게 됩니다.


발견을 즐기세요!


+++

# 소개

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## 강좌 개요

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

코스 PRO 202 _**Programming Bitcoin**_에 오신 것을 환영합니다. 유한체 산술에서 시작하여 비트코인 테스트넷에서 실제 거래를 생성하고 전송하는 데 이르는 집중적인 여정입니다.

이 과정에서는 Python으로 비트코인 라이브러리를 점진적으로 구축하면서 비트코인의 보안과 내부 작동을 정확히 이해하는 데 필요한 암호학적, 프로토콜 및 소프트웨어 기반을 습득하게 됩니다. PRO 202 접근 방식은 완전히 실습 중심입니다. 모든 개념이 즉시 Jupyter 노트북에 구현되어 이론과 코드가 서로를 강화하도록 합니다.

### 비트코인을 위한 필수 수학 개념

첫 번째 섹션에서는 필수적인 수학적 토대를 확립합니다. 유한체 연산과 타원곡선 연산(군 법칙, 덧셈, 이중화, 스칼라 곱셈...)을 구현할 것입니다 — ECDSA의 전제 조건입니다. 목표는 두 가지입니다: 암호 서명을 가능하게 하는 대수적 구조를 이해하고 이를 조작할 수 있는 신뢰할 수 있는 Python 도구를 구축하는 것입니다.

그런 다음 ECDSA의 구성 요소를 공식화하게 됩니다: 키 생성, 점 형식 지정, 해싱, 서명 생성 및 검증. 이 섹션은 이론과 실습을 직접 연결하며, 구현 세부 사항과 기본 보안 모델의 견고성을 강조합니다.

### 비트코인 거래의 내부 작동 방식

두 번째 섹션에서는 비트코인 거래의 구조를 분석합니다: UTXO, 입력/출력, 시퀀스, 스크립트, 인코딩 등. 거래를 생성, 서명 및 검증하는 코드를 작성하면서 해시에 의해 무엇이 커밋되는지 그리고 그 이유를 정확히 이해하게 됩니다.

다음으로, 최소한의 _Script_ 실행기를 구현하고 주요 오프코드를 검토하며 지출 경로를 검증합니다. 목표는 거래 동작을 감사하고 검증 실패를 진단하며 지출 정책의 안전성을 평가할 수 있도록 하는 것입니다.

### 비트코인 네트워크의 내부 작동 방식

세 번째 섹션에서는 거래를 더 넓은 시스템 내에 배치합니다: 블록 구조, 헤더, 난이도, 그리고 작업 증명(Proof-of-Work) 메커니즘. 프로토콜 메시지, 블록 헤더 및 머클 트리를 다루게 됩니다.

마지막으로, 피어 투 피어 노드 통신, 메시지 최적화 및 SegWit의 도입을 학습하게 됩니다.

Plan ₿ Academy의 모든 과정과 마찬가지로, 마지막 섹션에는 여러분의 이해를 공고히 하기 위한 평가가 포함되어 있습니다. 비트코인의 내부 작동 방식을 탐구하고 그것을 구동하는 코드를 작성할 준비가 되었나요? 시작해봅시다!

# Bitcoin을 위한 필수 수학 개념

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Bitcoin 구현을 위한 수학

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## 타원 곡선 암호화

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin 트랜잭션 내부 작업

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin 트랜잭션 구문 분석 및 ECDSA 서명

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin 스크립트 및 트랜잭션 유효성 검사

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## 트랜잭션 구성 및 대금 지급 Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin 네트워크 내부 연동

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin 블록 및 Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## 네트워크 통신 및 머클 트리

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## 고급 노드 통신 및 분리된 증인

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# 최종 섹션


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## 리뷰 및 평가


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## 결론


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
