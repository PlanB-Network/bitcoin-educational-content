---
term: ACTIVATION METHOD

---
An activation method is the process by which the user community decides on the implementation of a soft fork on the Bitcoin protocol, aiming to avoid a blockchain split. This process involves soliciting the opinion of miners to approve a soft fork before its activation. If a significant majority accepts the soft fork, the risk of a blockchain split is minimized. This consensus is crucial because if a majority of miners refuse to make the modification, the soft fork could create two distinct chains: one with the modified rules and the other without. There are 2 main categories of activation methods:


- UASF (User-Activated Soft Fork) when it is the nodes that impose the update;
- MASF (Miner-Activated Soft Fork) when it is the miners who trigger the activation.

There are many different activation methods that have been tested as Bitcoin has evolved. In Satoshi's time, the activation process was not formally established. Changes were often arbitrary and sometimes even made without informing the community. Later, the *Flag Day* method was adopted. After Satoshi's departure, other methods were successively used, notably BIP34, BIP9, BIP8, and finally, the *Speedy Trial*.