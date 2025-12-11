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

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Bitcoin実施のための数学

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## 楕円曲線暗号

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin 取引の内幕

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin トランザクションの解析とECDSA署名

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin スクリプトとトランザクションの検証

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## トランザクションの構築とペイ・ツー・スクリプト Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin ネットワークの内部構造

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## BitcoinブロックとProof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## ネットワーク・コミュニケーションとメルクル・ツリー

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## 高度なノード通信と分離ウィットネス

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# 最終節


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## レビュー＆評価


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## 結論


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
