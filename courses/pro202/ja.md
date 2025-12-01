---
name: プログラミング Bitcoin
goal: 完全なBitcoinライブラリをゼロから構築し、Bitcoinの暗号基盤を理解する。
objectives: 

 - Pythonで有限体演算と楕円曲線演算を実装する
 - プログラムでBitcoinトランザクションを構築し、解析する
 - Testnetアドレスを作成し、トランザクションをネットワーク上にブロードキャストする。
 - Bitcoinのセキュリティ・モデルの基礎となる数学的基礎をマスターする。

---
# Bitcoinの脚本とプログラムへの旅


ジミー・ソングが教えるこの2日間の集中コースでは、Bitcoinの技術的基礎に深く入り込み、完全なBitcoinライブラリを一から構築します。有限体や楕円曲線といった基本的な数学から始まり、トランザクションの解析、スクリプトの実行、ネットワーク通信などを通して、Bitcoinの技術的基礎を学びます。Jupyterノートブックでの実践的なコーディング演習を通して、Testnet Addressを作成し、トランザクションを手動で構築し、ネットワークに直接ブロードキャストします。


発見を楽しもう！


+++

# はじめに

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## コースの概要

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

コース PRO 202 _**Programming Bitcoin**_ へようこそ。有限体の算術から始まり、Bitcoinのテストネット上で実際のトランザクションを作成し、ブロードキャストするまでの集中的な旅です。

このコースでは、Pythonでビットコインライブラリを段階的に構築しながら、ビットコインのセキュリティと内部動作を正確に理解するために必要な暗号学、プロトコル、ソフトウェアの基礎を習得します。PRO 202のアプローチは徹底的に実践的であり、すべての概念はすぐにJupyterノートブックに実装され、理論とコードが相互に強化し合うことを保証します。

### ビットコインのための基本的な数学的概念

この最初のセクションでは、不可欠な数学的基礎を確立します。有限体の算術と楕円曲線の演算（群の法則、加算、倍算、スカラー乗算…）を実装します — ECDSA の前提条件です。目的は二重です：暗号署名を可能にする代数的構造を理解すること、そしてそれらを操作するための信頼できる Python ツールを構築することです。

次に、ECDSA の構成要素を体系化します：鍵生成、点のフォーマット、ハッシュ化、署名の作成と検証。このセクションでは、理論と実践を直接結び付け、実装の詳細と基礎となるセキュリティモデルの堅牢性を強調します。

### ビットコイン取引の内部構造

第2章では、ビットコイン取引の構造を詳しく分析します：UTXO、入力/出力、シーケンス、スクリプト、エンコーディングなどです。取引を構築し、署名し、検証するコードを書き、ハッシュによって何がコミットされ、なぜそうなのかを正確に理解します。

次に、最小限の _Script_ 実行エンジンを実装し、主要なオペコードを確認し、支出パスを検証します。目的は、取引の挙動を監査し、検証エラーを診断し、支出ポリシーの安全性について論理的に判断できるようにすることです。

### ビットコインネットワークの内部構造

第3章では、取引をより広いシステム内に位置付けます：ブロック構造、ヘッダー、難易度、およびProof-of-Workメカニズム。プロトコルメッセージ、ブロックヘッダー、そしてマークルツリーを扱います。

最後に、ピアツーピアノード間の通信、メッセージの最適化、そしてSegWitの導入について学びます。

Plan ₿ Academy のすべてのコースと同様に、最後のセクションには理解を深めるための評価が含まれています。ビットコインの内部構造を解き明かし、それを動かすコードを書く準備はできましたか？さあ、始めましょう！

# Bitcoinに必要な数学的概念

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Bitcoin実施のための数学

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## 楕円曲線暗号

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin 取引の内幕

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin トランザクションの解析とECDSA署名

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin スクリプトとトランザクションの検証

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## トランザクションの構築とペイ・ツー・スクリプト Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin ネットワークの内部構造

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## BitcoinブロックとProof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## ネットワーク・コミュニケーションとメルクル・ツリー

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## 高度なノード通信と分離ウィットネス

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# 最終節


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## レビュー＆評価


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## 結論


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
