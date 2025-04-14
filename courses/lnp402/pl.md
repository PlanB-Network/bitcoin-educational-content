---
name: Programowanie w Lightning za pomocą SDK
goal: Rozwijaj swoje umiejętności programowania Lightning dzięki szkoleniom Rust i SDK na poziomie średniozaawansowanym.
objectives: 

  - Przyzwyczaj się do języka Rust
  - Zrozumienie, dlaczego warto używać Rust do rozwijania Bitcoin
  - Uzyskaj podstawę SDK

---

# Rozwój umiejętności deweloperskich w LN


Witamy w podróży LN z SDK.


W tym kursie nauczysz się podstaw książki Rust, a następnie programowania LN przy użyciu SDK i zakończysz praktycznymi ćwiczeniami. Nasi nauczyciele z różnych środowisk poprowadzą Cię w kierunku praktycznych umiejętności i wyjaśnią różne wyzwania, przed którymi często stają dzisiejsi inżynierowie LN.


Ten kurs został sfilmowany podczas seminarium LIVE zorganizowanego przez Fulgur'Ventures podczas wydarzenia LN Tuscany w październiku 2023 roku.


Ciesz się kursem!


+++

# Wprowadzenie

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Przegląd kursu

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Wprowadzenie**


Witamy w tym zaawansowanym kursie programowania na SDK. Podczas tego szkolenia poznasz podstawy Rust, następnie skupisz się na BTC i Rust, a na koniec wykonasz kilka praktycznych ćwiczeń z wykorzystaniem SDK.


To szkolenie będzie na razie dostępne tylko w języku angielskim i było częścią seminarium na żywo zorganizowanego w październiku ubiegłego roku w Toskanii przez Fulgure Venture. Program wydarzenia LIVE można znaleźć poniżej, a niniejsze szkolenie skupi się tylko na pierwszym tygodniu. Druga połowa była skierowana do RGB i można ją znaleźć w kursie RGB.


**Nauczyciele**


Bardzo dziękujemy naszym nauczycielom, którzy byli częścią tego programu:



- Alekos: "Hej, jestem włoskim programistą i hakerem. Pracowałem nad różnymi projektami, takimi jak bitcoindevkit, magicalbitcoin i h4ckbs"
- Andrei: "Ekspert od piorunów w LIPA"
- Gabriel : "Piszę kod i robię różne rzeczy"
- Jesse de wit : "entuzjasta Lightning Network | deweloper | Breez"


**Rozkład jazdy**


Tydzień 1 wydarzenia LN Toskania

![image](assets/1.webp)


Po ukończeniu tego kursu, jeśli jesteś zainteresowany szkoleniem uzupełniającym, oto druga część harmonogramu:

![image](assets/2.webp)



To szkolenie daje możliwość rozwijania umiejętności programowania na Lightning Network przy użyciu Rust i różnych zestawów SDK. Jest przeznaczony dla programistów z solidnym zapleczem programistycznym, którzy chcą zagłębić się w rozwój specyficzny dla Lightning Network. Poznasz podstawy Rust, dowiesz się, dlaczego jest on odpowiedni do rozwoju Bitcoin, a następnie przejdziesz do praktycznej implementacji przy użyciu specjalistycznych zestawów SDK.


**Sekcja 2: Nauka kodowania z Rust**

W tej części odkryjesz podstawy Rust poprzez serię progresywnych rozdziałów. Nauczysz się pisać kod Rust, zrozumiesz jego specyfikę i opanujesz jego podstawowe funkcje w siedmiu szczegółowych częściach. Moduł ten jest niezbędny do zrozumienia, dlaczego Rust jest preferowanym językiem do rozwoju Bitcoin.


**Sekcja 3: Rust i Bitcoin**

Tutaj dogłębnie zbadamy, dlaczego Rust jest odpowiednim wyborem dla rozwoju Bitcoin. Dowiesz się o jego modelu błędów, narzędziu UniFFI i asynchronicznych cechach - wszystkie kluczowe Elements w budowaniu solidnego i bezpiecznego oprogramowania.


**Sekcja 4: Rozwój LNP/BP za pomocą SDK**

Dowiesz się, jak tworzyć węzły LN przy użyciu różnych zestawów SDK, takich jak Breez SDK i Greenlight for Lipa. Zobaczysz, jak zaimplementować aplikacje Lightning Network przy użyciu bibliotek zaprojektowanych w celu uproszczenia rozwoju Bitcoin i Lightning.


Gotowy, aby rozwinąć swoje umiejętności Lightning Network z Rust? Do dzieła!

# Naucz się kodować z książką Rust

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Wprowadzenie do Rust (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::


## Wprowadzenie do Rust (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


## Wprowadzenie do Rust (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::


## Wprowadzenie do Rust (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::


## Wprowadzenie do Rust (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::


## Wprowadzenie do Rust (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::


## Wprowadzenie do Rust (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::


# Rust I BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Dlaczego Rust na Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


## Model błędu

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::


## Unniffit

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::


## Cechy asynchroniczne

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>


:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::


# Rozwijanie LNP/BP za pomocą SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## Węzeł LN na SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::


## Greenlight dla Lipy

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::


## Breez sdk dla lipa

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>


:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::


# Sekcja końcowa

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>




## Recenzje i oceny

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Wnioski

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>