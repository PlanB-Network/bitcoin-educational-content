---
term: Proof of Work
---

針對 Sybil 攻擊的保護機制，Sybil 攻擊的特點是創造多個虛假身份，目的是獲得非法優勢。因此，Proof of Work 在 Bitcoin 上建立了不可忽略的票數倍增邊際成本。Proof of Work 是中本共識機制的基礎，而中本共識機制是用來在網路的不同節點之間就分散式 Ledger 的單一版本達成協議的原則。具體來說，Proof of Work 涉及到尋找一個數值，當該數值通過隨機數學函數時，得到的結果會低於一個目標值。Proof of Work 的這個目標值每隔 2016 個區塊就會由節點調整一次。這稱為難度調整。降低目標值可增加 Mining 的難度，或提高目標值可降低 Mining 的難度，這取決於前一時期礦工部署的計算能力的演變。


![](../../dictionnaire/assets/34.webp)


每找到一個有效的區塊，礦工所做的這些工作就會得到獎勵。勝出的 Miner 會獲得金錢獎勵，包括區塊補貼 (無中生有的新比特幣)，以及交易費用。如今，Proof of Work 對 Bitcoin 的難度已經到了 Mining 需要大量計算能力才能成功贏得區塊的地步。因此，通常需要有專門的電子晶片來執行 `SHA256d`，稱為 ASIC，並參與 Mining 池。


> ► *在英文中，它被稱為 "Proof-of-Work「，有時簡稱為 」PoW"。