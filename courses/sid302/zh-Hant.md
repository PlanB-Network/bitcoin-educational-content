---
name: Liquid Bootcamp Essentials
goal: 全面了解 Liquid Network 和 Elements 專案，並學習如何在 Confidential Transactions、代用幣化和分散式網路架構中實作進階解決方案。
objectives: 

  - 瞭解 Liquid 架構的基本原理及其與 Bitcoin 的關係。
  - 學習使用 Elements 軟體設定和操作 Liquid 節點。
  - 探索使用 Confidential Transactions 和在 Liquid Network 上發行資產。
  - 掌握 Liquid 在資本市場應用的商業和技術層面。

---
# 介紹給 Liquid Network

踏上旨在深入瞭解 Liquid Network 和 Elements 專案的教育之旅。本開發營結合理論與實務，教您實作與運用 Liquid 功能所需的技術、架構與商業基礎。從 Confidential Transactions 到生態系統設計，本課程非常適合想要擴展 Bitcoin 生態系統內進階工具知識的人。

透過業界專家的演講，課程涵蓋的主題包括 Liquid 架構、標記化應用、Elements 的技術概念，以及 Breeze SDK 等創新使用案例。本課程的設計適合初學者和中級使用者，同時也為想要掌握 Liquid 作為優化專案平台的資深開發人員提供價值。

+++
# 簡介

<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>

## Liquid Bootcamp 簡介

<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>

歡迎參加 Liquid Bootcamp，這是一個全面的訓練，旨在讓您掌握有效利用 Liquid Network 和 Elements 專案的知識和技能。本課程深入介紹 Liquid 的獨特功能，例如 Confidential Transactions、資產發行及其聯盟網路結構，同時也涵蓋 Elements 的基礎概念，Elements 是為 Liquid 提供動力的軟體。

在整個訓練營中，您將探討 Liquid Network 的實際應用，從設置和操作節點到瞭解其在 Bitcoin 的資本市場和代用幣化中的使用。透過業界專家的演講，您還將深入瞭解 HTLC、Breeze SDK 和 Blockstream AMP 專案等進階主題。

這個訓練營原本是以現場活動的形式進行，遵循專為現場課程設計的結構化時間表（如圖所示）。然而，在此課程改編中，內容經過重新組織，以更適合線上形式，並方便學生理解。新的順序確保了從基礎概念到更多技術和進階主題的邏輯進程，最大化了學習體驗。

此旅程的結構設計可滿足不同專業程度的參加者，提供理論知識與實作經驗的融合。在本訓練營結束時，您將對 Liquid 的架構、其與 Bitcoin 的整合，以及如何使用其創新功能來建立和最佳化財務解決方案有堅實的了解。

# 基礎

<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>

## Liquid 架構

<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>

![Video](https://youtu.be/QCyWXVWkcAM)

Pablo 介紹 Liquid Network 的架構，強調其作為 Sidechain 至 Bitcoin 聯盟的角色。其中涵蓋了 Confidential Transactions、聯盟模式等主要功能，以及其作為創新沙盒的功能。與會者將深入瞭解 Liquid 如何透過提供更快速、更隱密的交易來補足 Bitcoin。

## Elements 的基本原理

<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>

![Video](https://youtu.be/9Yu0dPAJSek)

James 介紹 Elements 軟體及其與 Liquid Network 的整合。本環節包括運行 Liquid 節點、本機配置 Elements 以及使用 CLI 和 RPC 指令管理交易的實用指南。

## 連接 Bitcoin 層

<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>

![Video](https://youtu.be/zFvv0bn4ZWY)

Michael 討論了多重 Layer 技術（包括 Liquid、Lightning 和 Bitcoin）如何提高交易效率和可靠性。關鍵主題包括用於安全跨 Layer 交易的 HTLC，以及優化 Bitcoin 生態系統的進階腳本功能。

## Liquid Network 概觀

<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>

![Video](https://youtu.be/6wNeHQBlhA4)

Bozza 涵蓋 Liquid Network 的聯盟結構及其技術元件。主題包括在 Liquid 上測試過的創新技術，例如 Schnorr 簽章和 Simplicity scripting，以及使用 Layer Two 解決方案所涉及的權衡。

## 生態系統與資本市場

<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>

![Video](https://youtu.be/IAdOxZyx7-Y)

Chase 重點介紹了 Liquid 的生態系統及其在資本市場的應用。他討論了代幣化、社群資源，以及用於資產管理的 Sid Swap 和 Stokr 等工具，以及 Liquid 在商業環境中日益普及的應用。

## Blockstream AMP

<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>

![Video](https://youtu.be/AnMiD9amSUg)

Nardo 概述了 Blockstream AMP，這是一個在 Liquid 上管理數位資產的平台。他探討了 AMP 的架構、控制資產轉移的能力，以及對開發人員的實際應用。他也強調了 AMP 所面臨的挑戰和未來的改進。

# 技術

<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>

## Breeze SDK - Nodeless

<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>

![Video](https://youtu.be/ucc3a-udbgo)

Antonio 介紹 Breeze，這是專為 Liquid Network 上分散式交易設計的開放原始碼 SDK。他介紹了 Breeze 的功能，包括支援多語言綁定和安全交易流程，同時強調其目標是為開發人員簡化金融技術。

# 總結

<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>

## 評論與評分

<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>

<isCourseReview>true</isCourseReview>
## 總結

<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

恭喜您完成此課程！

我們很高興您已成功達到學習旅程中的這個里程碑。透過您的付出和參與，您獲得了寶貴的知識和技能，這些知識和技能將為您的職業發展提供良好的幫助。