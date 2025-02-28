---
term: BIP145

---
Päivitetään JSON-RPC-kutsu `getblocktemplate` lisäämällä siihen SegWit-tuki BIP141:n mukaisesti. Tämän päivityksen ansiosta louhijat voivat rakentaa lohkoja ottamalla huomioon SegWitin käyttöön ottaman uuden transaktioiden ja lohkojen "painon" mittauksen sekä muita parametreja, kuten sigops-rajan laskemisen.