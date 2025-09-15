---
name: SDK로 Lightning에서 개발하기
goal: 중급 Rust 및 SDK 교육을 통해 라이트닝 개발 기술을 향상하세요.
objectives: 

  - Rust 언어에 익숙해지기
  - Bitcoin 개발에 Rust을 사용하는 이유 이해하기
  - SDK의 기초 알아보기

---

# LN 개발 기술 향상


SDK와 함께하는 LN 여정에 오신 것을 환영합니다.


이 과정에서는 Rust 책의 기본 사항을 학습한 다음 SDK를 사용하여 LN 프로그래밍을 수행하고 몇 가지 실습으로 마무리합니다. 다양한 배경을 가진 강사진이 실무 기술을 안내하고 오늘날 LN 엔지니어가 자주 직면하는 다양한 문제를 설명합니다.


이 강좌는 2023년 10월에 열린 LN 토스카나 행사에서 풀구르벤처스가 주최한 라이브 세미나를 촬영한 것입니다.


코스를 즐겨보세요!


+++

# 소개

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## 코스 개요

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**소개**


SDK에 대한 고급 프로그래밍 과정에 오신 것을 환영합니다. 이 교육에서는 Rust의 기본 사항을 학습한 다음 BTC 및 Rust에 집중하고 SDK를 사용한 몇 가지 실습으로 마무리합니다.


이 교육은 현재 영어로만 제공되며, 지난 10월 토스카나에서 풀큐어 벤처가 주최한 라이브 세미나의 일부입니다. 라이브 이벤트의 프로그램은 아래에서 확인할 수 있으며, 이번 교육은 첫 주만 집중적으로 다룹니다. 후반부는 RGB을 대상으로 하며 RGB 코스에서 확인할 수 있습니다.


**교사**


이 프로그램에 참여해주신 선생님들께 감사드립니다:



- 알레코스 : "안녕하세요, 저는 이탈리아 출신의 코더이자 해커입니다. 비트코인데브킷, 매지컬비트코인, h4ckbs 등 다양한 프로젝트에 참여했습니다."
- Andrei : "LIPA의 번개 전문가"
- 가브리엘 : "저는 코드를 작성하고 일을 합니다."
- 제시 드 위트 : "Lightning Network 애호가 | 개발자 | 브리즈"


**세미나 일정**


LN 토스카나 이벤트 1주차

![image](assets/1.webp)


이 과정을 마친 후 후속 교육에 관심이 있으시다면 다음 일정의 두 번째 부분을 확인하시기 바랍니다:

![image](assets/2.webp)



이 교육은 Rust 및 다양한 SDK를 사용하여 Lightning Network에서 프로그래밍 기술을 개발할 수 있는 기회를 제공합니다. 이 교육은 탄탄한 프로그래밍 배경 지식을 갖춘 개발자가 Lightning Network 전용 개발에 뛰어들고자 하는 개발자를 위해 설계되었습니다. Rust의 기본 사항과 Bitcoin 개발에 적합한 이유를 학습한 다음, 전문 SDK를 사용하여 실습을 진행합니다.


*섹션 2: Rust으로 코딩하기****

이 섹션에서는 일련의 점진적인 챕터를 통해 Rust의 기본 사항을 살펴봅니다. 7개의 세부 파트에 걸쳐 Rust 코드를 작성하고, 그 특수성을 이해하고, 필수 기능을 마스터하는 방법을 배우게 됩니다. 이 모듈은 Rust이 왜 Bitcoin 개발에 선호되는 언어인지 이해하는 데 필수적입니다.


**섹션 3: Rust 및 Bitcoin**

여기서는 Rust이 Bitcoin 개발에 적합한 이유를 자세히 살펴봅니다. 강력하고 안전한 소프트웨어를 구축하는 데 있어 Elements의 핵심인 오류 모델, UniFFI 도구, 비동기 특성에 대해 알아보세요.


**섹션 4: SDK를 사용한 LNP/BP 개발**

Breez SDK 및 Lipa용 Greenlight와 같은 다양한 SDK를 사용하여 LN 노드를 개발하는 방법을 배우게 됩니다. Bitcoin 및 Lightning 개발을 간소화하도록 설계된 라이브러리를 사용하여 Lightning Network 애플리케이션을 구현하는 방법을 살펴봅니다.


Lightning Network로 Rust 기술을 향상시킬 준비가 되셨나요? 시작하세요!

# Rust 책으로 코딩하는 방법 알아보기

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Rust 소개(1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::


## Rust 소개(2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


## Rust 소개(3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::


## Rust 소개(4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::


## Rust 소개(5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::


## Rust 소개(6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::


## Rust 소개(7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::


# Rust & BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## 왜 Bitcoin당 Rust인가?

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


## 오류 모델

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::


## Unniffit

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::


## 비동기 특성

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>


:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::


# SDK로 LNP/BP 개발하기

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## SDK의 LN 노드

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::


## 리파를 위한 그린라이트

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::


## 리파용 브리즈 SDK

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>


:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::


# 최종 섹션

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>




## 리뷰 및 평가

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## 결론

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>