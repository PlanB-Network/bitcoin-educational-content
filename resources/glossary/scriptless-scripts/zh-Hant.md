---
term: 無碼腳本
---

這個概念最初是由 Andrew Poelstra 所開發，允許在 Bitcoin Blockchain 上執行智慧型契約，而不需明確揭露 Contract 的邏輯。正如「無指令碼指令碼」這個名稱所暗示的，這個構想是基於執行指令碼（或契約）而無需明確使用指令碼。這些契約利用 Schnorr 簽署的特性，可以使用 *Adaptor Signatures*，特別是在進行 *Atomic Swaps* 時。Contract 條件由參與各方應用和執行 off-chain，只有他們知道這些條款。與傳統智慧型契約不同，*Scriptless Scripts* 可將其對 Blockchain 的影響降至最低，從而降低運作成本。這些合約也比傳統智慧合約更隱密，因為傳統智慧合約會在 Blockchain 上留下痕跡。因此，它們類似於普通交易，這增加了它們的匿名集。