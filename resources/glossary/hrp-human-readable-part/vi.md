---
term: HRP (HUMAN READABLE PART)

---
The HRP, standing for "Human Readable Part," is a component of bech32 and bech32m (SegWit v0 and SegWit v1) receiving addresses. The HRP refers to the part of the address that is specifically formatted to be easily read and interpreted by humans. Take, for example, a bech32 Bitcoin address:

```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```

In this address, the initial `bc` represents the HRP. This prefix allows one to quickly identify that the string of characters presented is a Bitcoin address and not something else.