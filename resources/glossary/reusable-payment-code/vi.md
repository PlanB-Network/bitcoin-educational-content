---
term: REUSABLE PAYMENT CODE

---
In BIP47, a reusable payment code is a static identifier generated from a Bitcoin wallet that allows for a notification transaction and the derivation of unique addresses. This avoids the reuse of addresses, which leads to a loss of privacy, without having to manually derive and transmit new, unused addresses for each payment. In BIP47, reusable payment codes are constructed as follows:


- Byte 0 corresponds to the version;
- Byte 1 is a bit field for adding information in case of specific use;
- Byte 2 indicates the parity of the `y` of the public key;
- From byte 3 to byte 34, you will find the `x` value of the public key;
- From byte 35 to byte 66, there is the chain code associated with the public key;
- From byte 67 to byte 79, there is zero padding.

A Human-Readable Part (HRP) is generally added at the beginning of the payment code and a checksum at the end, and then it is encoded in base58. The construction of a payment code is thus quite similar to that of an extended key. Here is my own BIP47 payment code in base58 for example:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

In the PayNym implementation of BIP47, payment codes can also be expressed in the form of identifiers associated with the image of a robot. Here is mine, for example:

```text
+throbbingpond8B1
```

The use of payment codes with the PayNym implementation is currently available on Sparrow Wallet on PC and on Samourai Wallet on mobile.