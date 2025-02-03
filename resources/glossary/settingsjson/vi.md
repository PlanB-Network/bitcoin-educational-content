---
term: SETTINGS.JSON

---
File used in Bitcoin Core to store the settings of the graphical user interface (GUI). It retains information about user configurations, such as open wallets for example. When Bitcoin Core is restarted, this file enables the automatic reopening of wallets that were active before the application was closed. If a wallet is closed via the GUI, it is also removed from this file, and therefore, it will not be reopened automatically on the next start.