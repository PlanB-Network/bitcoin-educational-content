---
term: BIP8

---
Developed following the debates on SegWit, which used BIP9 for its activation, BIP8 is a soft fork activation method that natively incorporates an automatic UASF (*User-Activated Soft Fork*) mechanism. Like BIP9, BIP8 utilizes miner signaling but adds the `LOT` (*Lock-in On Time out*) parameter. If `LOT` is set to `true`, upon the expiration of the signaling period without reaching the required threshold, a UASF is automatically triggered, forcing the activation of the soft fork. This approach compels miners to be cooperative or risk a UASF imposed by users. Moreover, unlike BIP9, BIP8 defines the signaling period based on block height, eliminating potential manipulations through hash rate by miners. BIP8 also allows for setting a variable voting threshold and introduces a parameter for a minimum block height for activation, giving miners time to prepare and signal their agreement in advance without necessarily being ready. When a soft fork is activated via BIP8 with the `LOT=true` parameter, this uses a very aggressive method against miners who are immediately put under the pressure of a potential UASF. Indeed, it leaves them only 2 choices:


- Be cooperative, and thus facilitate the activation process;
- Be uncooperative, in which case users automatically perform a UASF to impose the soft fork.