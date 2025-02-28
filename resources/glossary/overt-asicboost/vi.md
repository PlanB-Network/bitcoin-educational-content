---
term: OVERT ASICBOOST

---
The open and transparent version of AsicBoost. AsicBoost is an algorithmic optimization technique used in Bitcoin mining. Miners using the Overt version manipulate the `nVersion` field of the candidate block and use this modification as an additional nonce. This method leaves the actual `Nonce` field of the block unchanged during each hashing attempt, thereby reducing the calculations needed for each SHA256, by keeping some data the same between attempts. This version is publicly detectable and does not hide its modifications from the rest of the network, unlike the Covert version of AsicBoost.