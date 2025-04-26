---
term: LABEL (SILENT PAYMENTS)

---
Within the Silent Payments protocol, labels are integers used to modify the initial static address in order to create many other static addresses. The use of these labels allows for the segregation of payments sent via Silent Payments, by employing different static addresses for each use, without excessively increasing the operational burden for detecting these payments (scanning). Bob uses a static address $B$, composed of two public keys: $B_{\text{scan}}$ for scanning and $B_{\text{spend}}$ for spending. The hash of $b_{\text{scan}}$ and an integer $m$, scalar-multiplied by the generator point $G$, is added to the spending public key $B_{\text{spend}}$ to create a sort of new spending public key $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

For example, the first key $B_1$ is obtained in this manner:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

The static address published by Bob will now be composed of $B_{\text{scan}}$ and $B_m$. For example, the first static address with the label $1$ will be:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

We only start from label $1$, because label $0$ is reserved for change. Alice, who wishes to send bitcoins to the labeled static address provided by Bob, will derive the unique payment address $P_0$ using the new $B_1$ instead of $B_{\text{spend}}$:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

In reality, Alice may not even know that Bob has a labeled address, as she simply uses the second part of the static address he provided, which in this case is the value $B_1$ rather than $B_{\text{spend}}$. To scan for payments, Bob will always use the value of his initial static address with $B_{\text{spend}}$ in this manner:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Then, he will simply subtract the value he finds for $P_0$ from each output one by one. He then checks if one of the results of these subtractions matches the value of one of the labels he uses on his wallet. If it matches, for example, for output #4 with the label $1$, this means that this output is a Silent Payment associated with his static address labeled $B_1$:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

This works because:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Thanks to this method, Bob can use a multitude of static addresses (with $B_1$, $B_2$, $B_3$...), all derived from his base static address ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), in order to properly separate uses.

However, this separation of static addresses is only valid from a personal wallet management perspective, but does not allow for the separation of identities. Since they all have the same $B_{\text{scan}}$, it is very easy to associate all the static addresses together and deduce that they belong to a single entity.