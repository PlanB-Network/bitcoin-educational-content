---
term: DIFFICULTY ADJUSTMENT

---
Difficulty adjustment is a periodic process that redefines the difficulty target for the proof of work mechanism (mining) on Bitcoin. This event occurs every 2016 blocks (approximately every two weeks). It serves to increase or decrease the difficulty factor (also called the difficulty target), depending on how quickly the last 2016 blocks were found. The adjustment aims to maintain a stable and predictable block production rate, at a frequency of one block every 10 minutes, despite variations in the computational power deployed by miners. The change in difficulty during the adjustment is limited to a factor of 4. The formula executed by the nodes to calculate the new target is as follows:

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$

&nbsp;

Where:


- $N$: The new target;
- $A$: The old target of the last 2016 blocks;
- $T$: The total actual time of the last 2016 blocks in seconds;
- $1,209,600$: The target time in seconds to produce 2016 blocks with a 10-minute interval between each.

> ► *In French, the term "reciblage" is sometimes also used to refer to adjustment. In English, it is referred to as "Difficulty Adjustment".*