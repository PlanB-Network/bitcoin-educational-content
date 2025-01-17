---
term: BIP111

---
Proposes the addition of a service bit named `NODE_BLOOM` to allow nodes to explicitly signal their support for Bloom Filters as described in BIP37. The introduction of `NODE_BLOOM` enables node operators to disable this service in order to reduce the risks of DoS. The BIP37 option is disabled by default in Bitcoin Core. To enable it, the parameter `peerbloomfilters=1` must be entered in the configuration file.