---
term: Knapsack solver
definition: Bitcoin Core'daki eski madeni para seçme yöntemi, yerini Branch-and-Bound yöntemine bırakmıştır.
---

Sürüm 0.17'den önce Bitcoin core Wallet'de coin seçmek için kullanılan eski bir yöntem. Knapsack Solver, ücretleri ve işlemin boyutunu en aza indirmek amacıyla UTXO'ları yinelemeli ve rastgele seçerek ve bunları alt kümelere ekleyerek Coin seçim problemini çözmeye çalışır. Bu yöntem o zamandan beri *Branch-and-Bound* ile değiştirilmiştir.