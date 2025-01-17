---
term: COVENANT

---
Ein Mechanismus, der die Auferlegung spezifischer Bedingungen dafür ermöglicht, wie ein bestimmtes Währungsstück ausgegeben werden kann, auch in zukünftigen Transaktionen. Über die Bedingungen hinaus, die die Skriptsprache eines UTXO normalerweise zulässt, erzwingt der Covenant zusätzliche Beschränkungen, wie dieser Bitcoin in nachfolgenden Transaktionen ausgegeben werden kann. Technisch gesehen entsteht eine Vereinbarung, wenn der "ScriptPubKey" eines UTXO Einschränkungen für den "ScriptPubKey" der Ausgaben einer Transaktion definiert, die den UTXO ausgibt. Durch die Erweiterung des Anwendungsbereichs des Skripts würden Covenants zahlreiche Entwicklungen auf Bitcoin ermöglichen, wie die bilaterale Verankerung von Drivechains, die Implementierung von Tresoren oder die Verbesserung von Overlay-Systemen wie Lightning. Die Covenant-Vorschläge werden anhand von drei Kriterien unterschieden:


- Ihr Anwendungsbereich;
- Ihre Umsetzung;
- Ihre Rekursivität.

Es gibt viele Vorschläge, die die Verwendung von Covenants für Bitcoin ermöglichen würden. Die in der Umsetzung am weitesten fortgeschrittenen sind: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO), und `OP_VAULT`. Zu den anderen Vorschlägen gehören: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, usw.

Um das Konzept einer Vereinbarung besser zu verstehen, stellen Sie sich folgende Analogie vor: Stellen Sie sich einen Tresor vor, der 500 € in kleinen Scheinen enthält. Wenn es Ihnen gelingt, diesen Tresor mit dem richtigen Schlüssel zu öffnen, dann können Sie dieses Geld nach Belieben verwenden. Das ist die normale Situation bei Bitcoin. Stellen Sie sich nun vor, dass derselbe Tresor keine 500€ in Banknoten enthält, sondern Essensgutscheine im gleichen Wert. Wenn es Ihnen gelingt, diesen Tresor zu öffnen, können Sie diese Summe verwenden. Allerdings ist Ihre Ausgabefreiheit eingeschränkt, da Sie mit diesen Gutscheinen nur in bestimmten Restaurants bezahlen können. Es gibt also eine erste Bedingung, um dieses Geld auszugeben, nämlich den Tresor mit dem entsprechenden Schlüssel zu öffnen. Es gibt aber auch eine zusätzliche Bedingung für die künftige Verwendung dieser Summe: Sie darf nur in Partnerrestaurants ausgegeben werden und nicht frei. Dieses System von Beschränkungen für künftige Transaktionen wird als Vertrag bezeichnet.

> im Französischen gibt es keinen Begriff, der die Bedeutung des Wortes "covenant" genau wiedergibt. Man könnte von einer "Klausel", einem "Pakt" oder einer "Verpflichtung" sprechen, die aber nicht genau dem Begriff "Covenant" entsprechen würden. Dieser Begriff ist der juristischen Terminologie entlehnt, die es ermöglicht, eine Vertragsklausel zu beschreiben, die einer Immobilie dauerhafte Verpflichtungen auferlegt.*