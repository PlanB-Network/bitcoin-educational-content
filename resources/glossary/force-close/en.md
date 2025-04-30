---
term: FORCE CLOSE
---

Non-cooperative Lightning channel closing mechanism. When two users open a channel with a Multisig 2/2, each can unilaterally close the channel by broadcasting the last commitment transaction that has already been signed, in order to recover their onchain bitcoins. This is known as "force close".

This method is generally used if one of the participants no longer responds, or if cooperative closing of the channel is impossible. If force close can be avoided, it's best, as it takes longer to recover onchain funds and can be much more expensive in terms of fees.

In a force close, one of the two users broadcasts the commitment transaction, which reflects the last known state of the Lightning channel. There is then a timelock before the bitcoins can be retrieved onchain, giving the other party time to verify that the transaction corresponds to the latest channel state. If a user tries to cheat by publishing an out-of-date commitment transaction, the other party can use the revocation secret to punish the cheater and recover all the funds in the channel.