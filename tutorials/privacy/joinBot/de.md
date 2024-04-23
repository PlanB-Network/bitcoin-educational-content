---
name: JoinBot
description: Verstehen und Verwenden des JoinBots
---

![DALL·E – Samurai-Roboter in einem roten Wald, 3D-Rendering](assets/cover.webp)

JoinBot ist ein neues Tool, das mit dem neuesten Update 0.99.98f der beliebten Bitcoin-Wallet-Software Samourai Wallet eingeführt wurde. Es ermöglicht Ihnen, einfach eine gemeinsame Transaktion durchzuführen, um Ihre Privatsphäre zu optimieren, ohne einen Partner finden zu müssen.

**Vielen Dank an den ausgezeichneten Fanis Michalakis für die Idee, DALL-E für das Miniaturbild zu verwenden!**

## Was ist eine gemeinsame Transaktion bei Bitcoin?

Bitcoin basiert auf einem verteilten und transparenten Kontenbuch. Jeder kann die Transaktionen der Benutzer dieses elektronischen Bargeldsystems verfolgen. Um eine gewisse Vertraulichkeit zu gewährleisten, kann der Bitcoin-Benutzer Transaktionen mit einer spezifischen Struktur durchführen, um eine plausible Abstreitbarkeit bei der Interpretation dieser Transaktionen hinzuzufügen.

Das Ziel ist nicht, die Informationen direkt zu verbergen, sondern sie unter anderen zu verwirren. Dieses Ziel wird insbesondere bei Coinjoins verwendet, bei denen Transaktionen verwendet werden, um die Historie einer Bitcoin-Münze zu unterbrechen und ihre Rückverfolgung zu erschweren. Um dieses Ziel zu erreichen, müssen mehrere Inputs und Outputs mit dem gleichen Betrag in der Transaktion erstellt werden.

Die Inputs sind die Eingänge einer Bitcoin-Transaktion und die Outputs sind die Ausgänge. Die Transaktion verwendet ihre Eingänge, um neue Ausgänge zu erstellen und die Ausgabenbedingungen für eine Münze zu ändern. Dieser Mechanismus ermöglicht es, Bitcoins zwischen den Benutzern zu verschieben.
Ich erkläre Ihnen das im Detail in diesem Artikel: Mechanismus einer Bitcoin-Transaktion: UTXO, Inputs und Outputs.

Eine Möglichkeit, die Spuren in einer Bitcoin-Transaktion zu verwischen, besteht darin, eine gemeinsame Transaktion durchzuführen. Wie der Name schon sagt, handelt es sich dabei um eine Vereinbarung zwischen mehreren Benutzern, die jeweils einen Betrag an Bitcoins als Input in eine gemeinsame Transaktion einzahlen und einen Betrag als Output erhalten.

Wie bereits erwähnt, ist die bekannteste Struktur für gemeinsame Transaktionen der Coinjoin. Zum Beispiel werden bei Coinjoin Whirlpool 5 Teilnehmer mit dem gleichen Betrag an Bitcoins als Eingabe und Ausgabe in den Transaktionen verwendet.

![Schema einer Coinjoin-Transaktion auf Whirlpool](assets/1.webp)

Ein externer Beobachter dieser Transaktion wird nicht in der Lage sein zu wissen, welcher Output zu welchem Benutzer als Eingabe gehört. Wenn wir das Beispiel des Benutzers Nr. 4 (violett) nehmen, können wir seine UTXO als Eingabe erkennen, aber wir werden nicht wissen, welcher der 5 Outputs wirklich seiner ist. Die ursprüngliche Information wird nicht versteckt, sondern in einer Gruppe verwirrt.
Der Benutzer kann den Besitz eines bestimmten UTXO in der Ausgabe leugnen. Dieses Phänomen wird als "plausible Abstreitbarkeit" bezeichnet und ermöglicht es, Vertraulichkeit in einer transparenten Bitcoin-Transaktion zu erreichen.

Um mehr über Coinjoin zu erfahren, erkläre ich ALLES in diesem ausführlichen Artikel: Verstehen und Verwenden von CoinJoin auf Bitcoin.

Obwohl Coinjoin sehr effektiv ist, um die Rückverfolgung eines UTXO zu unterbrechen, ist es nicht für direkte Ausgaben geeignet. Tatsächlich erfordert seine Struktur die Verwendung von Inputs mit vordefinierten Beträgen und Outputs mit dem gleichen Wert (abzüglich der Mining-Gebühren). Die Ausgabetransaktion bei Bitcoin ist jedoch ein kritischer Moment für die Vertraulichkeit, da sie oft eine physische Verbindung zwischen dem Benutzer und seiner On-Chain-Aktivität herstellt. Es scheint daher unerlässlich, Vertraulichkeitstools für Ausgaben zu verwenden. Es gibt auch andere kollaborative Transaktionsstrukturen, die speziell für effektive Zahlungstransaktionen entwickelt wurden.

## Die StonewallX2-Transaktion

Unter den vielen Ausgabetools, die in der Samourai Wallet angeboten werden, gibt es die kollaborative Transaktion StonewallX2. Es handelt sich um einen Mini-Coinjoin zwischen zwei Benutzern, der für Zahlungen gedacht ist. Von außen betrachtet kann diese Transaktion zu mehreren möglichen Interpretationen führen. Es gibt also plausible Abstreitbarkeit und folglich Vertraulichkeit für den Benutzer.

Diese kollaborative StonewallX2-Transaktion ist in der Samourai Wallet und in der Sparrow Wallet verfügbar. Dieses Tool ist interoperabel zwischen den beiden Softwareprogrammen.

Der Mechanismus ist ziemlich einfach zu verstehen. Hier ist seine praktische Funktionsweise:

> - Ein Benutzer möchte eine Zahlung in Bitcoins leisten (zum Beispiel bei einem Händler).
> - Er erhält die Empfangsadresse des tatsächlichen Zahlungsempfängers (des Händlers).
> - Er erstellt eine spezifische Transaktion mit mehreren Inputs: mindestens einen, der ihm gehört, und einen, der einem externen Mitarbeiter gehört.
> - Die Transaktion hat 4 Outputs, darunter 2 mit dem gleichen Betrag: einer zur Adresse des Händlers, um ihn zu bezahlen, einer als Wechselgeld, das zum Benutzer zurückkehrt, ein Output mit dem gleichen Wert wie die Zahlung, der zum Mitarbeiter geht, und ein weiterer Output, der ebenfalls zum Mitarbeiter zurückkehrt.

Hier ist zum Beispiel eine klassische StonewallX2-Transaktion, bei der ich eine Zahlung von 50.125 Sats geleistet habe. Der erste Input von 102.588 Sats stammt aus meiner Samourai Wallet. Der zweite Input von 104.255 Sats stammt aus dem Wallet meines Mitarbeiters:

![Schema einer StonewallX2-Transaktion](assets/2.webp)

Es gibt 4 Outputs, von denen 2 den gleichen Betrag haben, um die Spuren zu verwischen:

> - 50.125 Sats, die an den tatsächlichen Empfänger meiner Zahlung gehen.
> - 52.306 Sats, die mein Wechselgeld repräsentieren und daher zu einer Adresse meiner Wallet zurückkehren.
> - 50.125 Sats, die zu meinem Mitarbeiter zurückkehren.
> - 53.973 Sats, die zu meinem Mitarbeiter zurückkehren.
>   Am Ende der Transaktion hat der Mitarbeiter sein ursprüngliches Guthaben wieder (abzüglich der Mining-Gebühren) und der Benutzer hat dem Händler bezahlt. Dadurch wird der Transaktion eine große Menge an Entropie hinzugefügt und die eindeutigen Verbindungen zwischen Absender und Zahlungsempfänger werden aufgebrochen.

Die Stärke der StonewallX2-Transaktion besteht darin, dass sie eine der empirischen Regeln der Chain-Analysten vollständig konterkariert: die gemeinsame Eigentümerschaft der Inputs in einer Multi-Input-Transaktion. Mit anderen Worten, in den meisten Fällen kann man davon ausgehen, dass alle Inputs einer Bitcoin-Transaktion einer einzigen Person gehören. Satoshi Nakamoto hatte dieses Problem der Benutzeranonymität bereits in seinem White Paper erkannt:

> "Als zusätzliche Firewall könnte für jede Transaktion ein neues Schlüsselpaar verwendet werden, um sie nicht mit einem gemeinsamen Eigentümer zu verknüpfen. Bei Multi-Input-Transaktionen ist jedoch eine Verknüpfung unvermeidlich, da sie zwangsläufig zeigen, dass ihre Inputs von einem gemeinsamen Eigentümer gehalten wurden."

Dies ist eine der vielen empirischen Regeln, die in der On-Chain-Analyse verwendet werden, um Adresscluster zu erstellen. Um mehr über diese Heuristiken zu erfahren, empfehle ich Ihnen, diese Serie von 4 Artikeln von Samourai zu lesen, die das Thema wunderbar einführen.

Die Stärke der StonewallX2-Transaktion liegt darin, dass ein externer Beobachter denken wird, dass die verschiedenen Inputs der Transaktion einem gemeinsamen Eigentümer gehören. In Wirklichkeit handelt es sich jedoch um zwei verschiedene Benutzer, die zusammenarbeiten. Die Analyse der Zahlung wird also in die Irre geführt und die Benutzeranonymität bleibt gewahrt.

Von außen betrachtet kann eine StonewallX2-Transaktion nicht von einer Stonewall-Transaktion unterschieden werden. Der einzige Unterschied besteht darin, dass Stonewall nicht kollaborativ ist. Es verwendet nur die UTXOs eines einzigen Benutzers. Aber in ihrer Struktur im Kontenbuch sind Stonewall und StonewallX2 völlig identisch. Dadurch können noch mehr mögliche Interpretationen dieser Transaktionsstruktur hinzugefügt werden, da ein externer Beobachter nicht wissen kann, ob die Inputs von einer einzigen Person oder von zwei Mitarbeitern stammen.

Darüber hinaus hat StonewallX2 den Vorteil gegenüber einem PayJoin vom Typ Stowaway, dass es in allen Situationen verwendet werden kann. Der tatsächliche Zahlungsempfänger gibt keine Inputs in die Transaktion ein. Daher kann man StonewallX2 verwenden, um bei jedem Bitcoin-Händler zu bezahlen, auch wenn dieser nicht Samourai oder Sparrow verwendet.
En revanche, l’inconvénient principal de cette structure de transaction est qu’elle nécessite un collaborateur qui veuille bien utiliser ses bitcoins pour participer à votre paiement. Si vous avez des amis bitcoiners prêts à vous aider en toute circonstance, cela n’est pas un problème. En revanche, si vous ne connaissez pas d’autres utilisateurs de Samourai Wallet, ou bien si personne n’est disponible pour collaborer, alors vous êtes bloqué.

Il existe toutefois un groupe Telegram où vous pouvez trouver d’autres utilisateurs de Samourai qui voudront bien collaborer avec vous. Vous pouvez le retrouver en cliquant ici.

Pour résoudre cette problématique, les équipes de Samourai ont récemment ajouté une nouvelle fonctionnalité à leur application : JoinBot.

# C’est quoi JoinBot ?

Le principe de JoinBot est simple. Si vous ne trouvez personne avec qui collaborer pour une transaction StonewallX2, vous pouvez collaborer avec lui. Concrètement, vous allez en fait réaliser une transaction collaborative directement avec Samourai Wallet.

Ce service est très commode, notamment pour les utilisateurs novices, puisqu’il est disponible 24h/24 et 7j/7. Si vous devez effectuer un paiement urgent et que vous souhaitez faire un StonewallX2, vous n’aurez plus besoin de contacter un ami, ou bien de chercher un collaborateur en ligne. JoinBot se chargera de vous assister.

Un autre avantage de JoinBot est que les UTXO qu’il fournit en input sont issus exclusivement de postmix Whirlpool, ce qui vient améliorer la confidentialité de votre paiement. De plus, puisque JoinBot est tout le temps en ligne, vous devriez collaborer avec des UTXO qui disposent de larges Anonset prospectifs.

Évidemment, JoinBot dispose de certains compromis qu’il convient de signaler :

> Comme pour un StonewallX2 classique, votre collaborateur est forcément au courant des UTXO utilisés et de leur destination. Dans le cas de JoinBot, Samourai connait les détails de cette transaction. Ce n’est pas forcément une mauvaise chose, mais il faut le garder à l’esprit.
> Pour éviter les spams, Samourai prélève 3,5 % de frais de service sur le montant de la transaction effective, avec une limite maximale de 0,01 BTC. Par exemple, si j’envoie un paiement réel de 100 kilosats avec JoinBot, le montant des frais de service sera de 3 500 sats.
> Pour utiliser JoinBot, vous devez obligatoirement disposer d’au moins deux UTXO non liés et disponibles sur votre portefeuille.
> Sur un StonewallX2 classique, les frais de minage sont partagés équitablement entre les deux collaborateurs. Avec JoinBot, vous devrez évidemment payer l’intégralité des frais de minage.
> Afin qu’une transaction JoinBot soit exactement semblable à une transaction StonewallX2 classique ou Stonewall, le paiement des frais de service se fait sur une transaction totalement séparée. Le remboursement de la moitié de frais de minage initialement payés par Samourai se fera lors de cette seconde transaction. Afin d’optimiser votre confidentialité jusqu’au bout, le règlement des frais se fait à l’aide d’une transaction à la structure Stowaway (PayJoin).

## Comment utiliser JoinBot ?

Pour réaliser une transaction JoinBot, vous devez disposer d’un portefeuille Samourai Wallet. Vous pouvez le télécharger ici, ou bien depuis le Google Playstore.

Contrairement à la majorité des outils développés par Samourai, pour le moment, Sparrow Wallet n’a pas encore annoncé implémenter JoinBot. Cet outil est donc uniquement disponible sur Samourai.

Découvrez étape par étape comment réaliser une transaction StonewallX2 avec JoinBot dans cette vidéo :

![Comment utiliser Joinbot](https://youtu.be/80MoMz2Ne5g)

Voici le schéma de la transaction que nous venons de réaliser dans la vidéo :

![Schéma de ma transaction StonewallX2 avec JoinBot.](assets/3.webp)

On peut y découvrir 5 inputs :

> - 3 inputs de 100 kilosats qui viennent de Samourai (JoinBot).
> - 2 inputs qui proviennent de mon portefeuille personnel, de 3 524 sats et de 1,8 mégasat.

Les 4 outputs de la transaction sont les suivants :

> - 1 de 212 452 sats vers le destinataire effectif de mon paiement.
> - 1 autre de même montant qui revient vers une adresse de Samourai.
> - 1 change qui revient également vers Samourai pour 87 302 sats. Cela représente la différence entre le total de leurs inputs (300 000 sats) et l’output d’offuscation (212 452 sats) moins les frais de minage.
> - 1 change qui revient vers une autre adresse de mon portefeuille. Il représente la différence entre le total de mes inputs et le paiement effectif, moins les frais de minage.

Pour rappel, les frais de minage ne représentent pas un output des transactions. Ils représentent simplement la différence entre le total des inputs et le total des outputs.

## Conclusion

JoinBot est un outil supplémentaire qui permet d’ajouter plus de choix et de liberté pour l’utilisateur de Samourai. Il permet de réaliser une transaction collaborative StonewallX2 directement avec Samourai comme collaborateur. Ce type de transaction aide à améliorer la confidentialité des utilisateurs.

Si vous pouvez réaliser un StonewallX2 classique avec un ami, je vous conseille tout de même de préférer cette utilisation de l’outil. En revanche, si vous êtes bloqués et que vous ne trouvez aucun collaborateur pour faire un paiement, vous savez que JoinBot sera disponible 24h/24 et 7j/7 pour collaborer avec vous.

> Ressources externes :
> '
>
> - [Understanding Bitcoin Privacy with OXT - Part 1/4](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
> - [Video: Understanding Bitcoin Privacy with OXT](https://youtu.be/vhUREWiY570)
> - [Privacy Enhanced Transactions](https://docs.samourai.io/wallet/privacy-enhanced-transactions)
> - [Comprendre et utiliser le CoinJoin sur Bitcoin](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin)
