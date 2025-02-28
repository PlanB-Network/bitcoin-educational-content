---
term: SPEEDY TRIAL

---
Method of activating a soft fork initially conceptualized for Taproot in early 2021 by David A. Harding based on an idea by Russell O'Connor. Its principle is to use the BIP8 method with a `LOT` parameter set to `false`, while reducing the activation period to just 3 months. This shortened voting period allows for a quick verification of miner approval. If the required approval threshold is reached during one of the periods, the soft fork is then locked in. It will be activated several months later, thus giving miners the necessary time to update their software.

The success of this method for Taproot, which enjoyed broad consensus within the Bitcoin community, however, does not guarantee its effectiveness for all updates. Although the Speedy Trial method allows for faster activation, some developers express concerns about its future use. They fear it could lead to too rapid a succession of soft forks, which could potentially threaten the stability and security of the Bitcoin protocol. Compared to BIP8 with the `LOT=true` parameter, the Speedy Trial method is much less threatening to miners. No UASF is planned automatically. This activation method has not yet been formalized within a BIP.

> ► *The term "Speedy Trial" is borrowed from legal terminology indicating an "expedited trial." This invokes the fact that the improvement proposal is quickly brought before the court of miners, to determine their intentions. It is generally accepted to use the English term directly in French.*