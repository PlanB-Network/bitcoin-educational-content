---
name: Delving Into Simplicity
goal: Master the design philosophy, type system, and full lifecycle of Simplicity
objectives:
  - Understand the three fundamental composition methods and the nine combinators that form a complete language
  - Build boolean logic, arithmetic, and SHA-256 from Simplicity's minimal type system
  - Grasp how the Failure and Reader side effects enable real blockchain interaction
  - Learn how Simplicity programs become Taproot addresses and are redeemed with witness data
---

# Delving Into Simplicity

A deep dive into the theory and design decisions behind the Simplicity language, based on the complete five-part ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) article series by [Dr. Russell O'Connor](https://r6.ca/), the creator of Simplicity at Blockstream Research. This course explains *why* Simplicity was designed the way it was, not how to write it.

The course follows Dr. O'Connor's articles through the three fundamental ways of combining computations, the minimal type system and its completeness theorem, the construction of practical data types and arithmetic from first principles, the careful introduction of side effects for blockchain interaction, and finally how programs are committed to addresses and redeemed on-chain.

+++

# Introduction

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Course overview

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Welcome to SCR403 — Delving Into Simplicity!

This course is based on the **"Delving Simplicity"** article series written by [Dr. Russell O'Connor](https://r6.ca/), an Infrastructure Tech Developer at [Blockstream](https://blockstream.com/) and the creator of Simplicity. The original articles were published on the [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) forum and form the primary source material for this course. We are grateful for his pioneering work, which made this educational content possible.

### What you will learn

This course explores the design philosophy and mathematical foundations behind Simplicity, the next-generation scripting language activated on the [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) in July 2025. It follows the complete five-part article series and is structured in two main content sections:

1. **Foundations of Simplicity** — Why blockchain computation demands a fundamentally different language, the three ways to combine operations (sequential, parallel, conditional), and the nine core combinators that form a mathematically complete language
2. **From Data Types to Programs** — Building boolean logic, arithmetic, and SHA-256 from first principles; understanding the Failure and Reader side effects that enable blockchain interaction; and learning how programs are committed to Taproot addresses via Commitment Merkle Roots and redeemed with witness data

### Prerequisites

This is an **expert-level** course (approximately 10 hours). You should be comfortable with:
- Basic Bitcoin scripting concepts (what transaction validation does)
- Fundamental programming concepts (types, functions, composition)
- Some familiarity with mathematical notation is helpful but not required. We introduce everything as we go

### Key resources

- **Original articles**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) by Dr. Russell O'Connor on Delving Bitcoin
- **Simplicity repository**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — source code and Rocq formal proofs
- **Official website**: [simplicity-lang.org](https://simplicity-lang.org/) — documentation and SimplicityHL reference
- **Blockstream blog**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — technical overview

Ready to dive into one of the most elegant pieces of Bitcoin engineering? Let's go!

## What is Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

If you're coming to this course without a background in Simplicity, this chapter will orient you before we dive into the deep end.

### Simplicity in a nutshell

Simplicity is a **Bitcoin-native smart contract language**, live on the Liquid Network today. First envisioned by Dr. Russell O'Connor around 2012 and detailed in his 2017 paper *Simplicity: A New Language for Blockchains*, it was activated on the Liquid Network in July 2025 after years of formal verification and development.

Unlike Ethereum's Solidity, which is a Turing-complete, high-level contract language, Simplicity is intentionally minimal. It has:
- **Three type formers** (unit, sum, product)
- **Nine combinators** (basic operations and composition rules)
- **No loops, no recursion, no dynamic memory**

From just these primitives, you can build any computation you need for transaction validation, from boolean logic to full SHA-256 hashing.

### What can you do with Simplicity today?

Simplicity is already powering real applications on the Liquid Network. The most notable is the [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), an oracle-free options marketplace where users trade call options on L-BTC using USDt as collateral (the underlying contract also supports puts). Other live Simplicity projects include [Swaption](https://swaption.io/) by SideSwap (options) and the open-source [Deadcat](https://github.com/Resolvr-io/deadcat) by Resolvr (prediction markets). Beyond DeFi, Simplicity enables advanced spending conditions such as vaults, covenants, and complex multisig schemes that would be impossible or unsafe in Bitcoin Script.

### What this course is — and isn't

This is **not** a hands-on coding tutorial. You won't write Simplicity programs here. If you're looking for that, check out:
- [simplicity-lang.org](https://simplicity-lang.org/) — official documentation and the SimplicityHL high-level language
- The [Simplicity GitHub repository](https://github.com/BlockstreamResearch/simplicity) — reference implementation, examples, and Rocq proofs
- The [Blockstream blog post](https://blog.blockstream.com/en-simplicity-github/) on getting started

What this course **is** about: the **philosophical and technical choices** behind Simplicity's design. Why was this language created this way? Why only nine combinators? Why no recursion? Why does it matter that the type system connects to Gentzen's sequent calculus?

Think of it as understanding **why the engine was built this way** rather than learning to drive the car.

### Who is this for?

This course is ideal for:
- **Protocol developers** who want to understand Simplicity's foundations before writing code
- **Bitcoin researchers** interested in the formal verification and type-theoretic approach
- **Computer scientists** curious about the connection between sequent calculus and blockchain computation
- **Advanced bitcoiners** who want to go beyond surface-level understanding of Liquid's scripting capabilities

If terms like "sum types", "combinators", or "sequent calculus" are entirely new to you, don't worry, we explain everything from scratch. But be prepared for a dense, mathematical journey.

### From articles to course

The original "Delving Simplicity" series by Dr. O'Connor is structured as five technical articles. This course reorganizes and annotates that material into a progressive learning path with quizzes to test your understanding along the way. The ideas, definitions, and proofs are his, and we've adapted the format for structured education.

# Foundations of Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Fundamental Ways of Combining Computations

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Now that Simplicity has been activated on the Liquid Network, I'd like to do an in-depth dive into the philosophy and design of the Simplicity language.

Bitcoin's transaction validation is a significantly different application from regular programming language design. Block space cost is at a premium so programs need to be compact. The programs in Bitcoin transactions are only ever executed on a single input and everyone executes the program on the same input. Also, the agent authorizing the transaction already knows the outcome of the computation in advance: that the transaction is valid.

Typically the authorizing agent will run much more expensive computations to derive witness data attesting to the transaction's validity, whereas programs run on the blockchain need to check the witness data for validity. Checking validity is often much cheaper than proving validity.

We've designed Simplicity with these sorts of unique language design challenges in mind. For example, Simplicity requires unexecuted branches be pruned so they do not appear on the blockchain. Preprocessing steps are carefully designed to exhibit (quasi-)linear time complexity in the size of the Simplicity program. Static analysis is used instead of "gas", which cannot be computed without executing code in a prescribed manner, so that the details of the execution model do not become consensus critical. No dynamic memory allocation during execution. And so on.

Before delving into the design details of Simplicity, I want to begin this series with some programming philosophy about the general ways of combining basic building blocks to create new functionality.

### Composition

Suppose one is designing a language for programmable transactions for a blockchain like Bitcoin. In particular, programs only have access to the transaction data and the UTXO data of the inputs, and execution only determines transaction validity (which lets the result of execution be cached). Let's say one starts with some set of basic operations that can perform various tasks such as basic computations, reading and/or processing data from the transaction, and signature verification. Each operation consumes some type of input (possibly empty) and returns some type of output. What are the ways we can combine these basic operations into more complex operations?

### Sequential Composition

![Sequential Composition](assets/en/001.webp)

The most fundamental composition method is sequential composition. If we have two basic operations, one whose output data type matches the input data type of the other, then we can combine these two operations into a new composite operation. This new operation runs these two basic operations in sequence, taking as input the input of the first operation, passing the output of that first operation into the input of the second operation, and ultimately returning the output of that second operation.

Of course, we don't need to restrict ourselves to just combining basic operations. Now that we have some composite operations, we can combine those using functional composition as well.

In mathematics, this sequential composition is often just called "composition", and one might think that this is the only way of composing things. However, we have other ways of composing operations.

### Parallel Composition

![Parallel Composition](assets/en/002.webp)

Suppose that we have two operations, they could be basic or complex operations, and they both take the same type of input. A second fundamental way of composing these two operations is to execute them both on the same input. This is called parallel composition, and the type of output is the "product" of the types of the outputs of the original operations and contains the pair of the two outputs.

While this is called "parallel" composition, and the two operations could in principle be executed in parallel, parallel execution isn't an operational requirement. We can implement parallel composition "sequentially" by executing one operation first and then the second operation. We don't care about the details of how parallel composition is implemented as long as the output is the same.

### Conditional Composition

![Conditional Composition](assets/en/003.webp)

Conditional composition is the dual of parallel composition. In this case we have two operations that produce the same output, and we compose them by choosing one of them to execute. The input to this composite operation is the "sum" or "tagged union" of the types of the inputs of the original operation. In this instance the tag, "Left" or "Right", is a single bit in the input's data which determines which type of data is being carried, and hence which of the two operations can be executed.

Conditional composition operates in the same way even when the input is the sum of two identical types. The sum type still contains a tag, and the value of that tag determines which of the two operations is to be executed.

### Composition in Bitcoin Script

There are many ways of realizing these three kinds of composition in various programming languages. In Bitcoin Script, sequential composition is realized (approximately) by the concatenation of two routines (this is why Bitcoin Script is called a concatenative programming language) since the output of one routine is left on the stack to be consumed by the subsequent routine. Parallel composition is achieved by use of duplicate and swap operations to manipulate the stack so that two routines can be run on the same input. Things are not entirely straightforward since what we are calling the "product" of types is typically realized by utilizing multiple stack items. Hopefully you can see the general idea.

Conditional composition is, of course, realized by `OP_IF` which branches based on the value on the stack. In this case the top stack item plays the role of a tag, and usually the next item or items on the stack are of different "types" that depend on the value of the tag. For each case the stack item types may only be suitable for processing by one of the branches in the `OP_IF`. However after we reach `OP_ENDIF` the stack items must be of consistent "type" such that the remaining script is capable of proceeding independent of which branch was previously taken.

### Composition in Simplicity

We designed Simplicity with combinators that directly implement these three forms of composition. Along with a few more combinators to support other basic operations related to the product and sum types, the core Simplicity language ends up consisting of nine combinators that are adequate to express any finite computation. We will discuss this in more detail in the next chapter.

### A Fourth Kind of Composition

Before ending we should mention that there is at least one more kind of composition found in Computer Science, which is "recursive composition". In recursive composition one operation is iterated multiple times.

Note that Bitcoin Script does not support recursive composition, and similarly, we have explicitly excluded unbounded recursion from Simplicity's design. Our thesis is that unbounded iterative computation is better implemented using recursive covenants which compute over multiple transactions. This allows users to avoid block space and standardness constraints and better predict transaction costs.

That being said, there are ways of abusing Simplicity's delegation feature to provide something resembling unbounded recursive composition, which we may discuss later in this series.

### Conclusion

We reviewed the three major forms of composition for transforming basic operations into complex operations:

- sequential composition
- parallel composition
- conditional composition

We discussed how these forms of composition are realized in Bitcoin Script, and hinted at how they have influenced the design of the Simplicity language. We noted that the fourth kind of composition, recursive composition, is specifically excluded from both Simplicity and Bitcoin Script.

In the next chapter we will describe the nine combinators that make up the core of the Simplicity language, how they serve to directly realize these three forms of composition, and how this forms a complete language for describing any finite computation.

## Combinator Completeness of Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

In this chapter we introduce the core Simplicity language and show that the language is complete, meaning that any finite computation can be expressed within it.

### Simplicity Types

Simplicity supports three fundamental type constructors. The product type `A × B` represents parallel composition outputs, while the sum type `A + B` (tagged union) handles conditional composition inputs. The third type is the unit type.

### Unit Type

The unit type, denoted `𝟙` or `ONE`, contains exactly one value: the empty tuple `⟨⟩` or `()`. This zero-bit data type carries no information.

### Sum Type

A sum type `A + B` combines two types with tags indicating "left" or "right." Values are written as `σᴸ(a)` or `inl(a)` for left-tagged values and `σᴿ(b)` or `inr(b)` for right-tagged values. The tags remain distinct even when combining identical types.

#### Boolean Type

The type `𝟙 + 𝟙`, denoted `𝟚` or `TWO`, represents a one-bit type with two values. By convention, `σᴸ⟨⟩` represents false/zero, while `σᴿ⟨⟩` represents true/one.

### Product Type

Product types `A × B` contain value pairs written as `⟨a, b⟩` or `(a, b)`. The type `𝟚 × 𝟚` has four values, distinct from the four values in `𝟚 + 𝟚`.

### Core Simplicity Expressions

Operations are denoted as `f : A ⊢ B`, meaning input type `A` and output type `B`. Simplicity is "first-order" — it lacks function types.

### Two Basic Operations

The core language provides two basic operations:

**Identity (`iden`).** The identity operation passes its input through unchanged:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** The unit operation discards its input and returns the empty tuple:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

These form families with one operation per type.

### Three Composition Combinators

Sequential composition uses `comp f g` (written `f ⨾ g` or `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Parallel composition uses `pair f g` (written `f ▵ g` or `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Conditional composition uses `case f g : (A + B) × C ⊢ D`, providing branches access to shared environment `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Why does conditional composition take this shape — a sum paired with a shared environment `C` — rather than a simpler `copair f g : A + B ⊢ C` that merely picks a branch? Because a bare `copair` cannot express **distribution**: the function `dist : (A + B) × C ⊢ A × C + B × C` that pushes a shared input into whichever branch is taken. By building the environment `C` directly into `case`, Simplicity obtains conditional composition *and* distribution from a single combinator — one of the key design decisions that keeps the core language down to nine combinators.

### Four More Combinators

Product consumption uses `take` and `drop`:

**take** extracts the left element:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extracts the right element:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Sum production uses `injl` and `injr`:

**injl** wraps with a left tag:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** wraps with a right tag:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### The Nine Core Combinators

In total, Simplicity has exactly nine core combinators:

| Combinator | Purpose |
|---|---|
| `iden` | Pass input through |
| `unit` | Discard input |
| `comp` | Sequential composition |
| `pair` | Parallel composition |
| `case` | Conditional composition |
| `take` | Extract left from product |
| `drop` | Extract right from product |
| `injl` | Inject into left of sum |
| `injr` | Inject into right of sum |

### Simplicity and the Sequent Calculus

Simplicity's design derives from the conjunctive-disjunctive fragment of Gentzen's sequent calculus. More precisely, it is a variant of the *functional interpretation* of the sequent calculus, which is itself analogous to the Curry-Howard correspondence between natural deduction and the lambda calculus. The combinator rules exhibit "smaller types in premises than conclusions," enabling the Bit Machine — Simplicity's abstract stack machine interpreter — to minimize data copying during execution.

### Values are not Expressions

Simplicity expressions denote operations, not values. The notation `scribe b : A ⊢ B` represents a unique expression always returning value `b`, serving as notational convenience rather than a combinator. This mirrors Bitcoin Script, where operations like `OP_1` push values rather than express them directly.

### Simplicity's Completeness Theorem

With all nine combinators in hand, how do we know we aren't missing something — that these nine really are enough? The Simplicity Completeness theorem answers this: for any function between (finite) Simplicity types, some Simplicity expression denotes it. The proof is constructive — it shows how to build the expression:

1. **Decompose the input**: Using nested `case` expressions, fully decompose any input of any type into its constituent bits
2. **Build a lookup table**: For each possible input, use `scribe` to produce the corresponding output
3. **Assemble**: The nested cases and scribes together form a giant lookup table that implements the function

This theorem is formally verified in the Rocq proof assistant (formerly Coq). The proof is part of the official Simplicity repository and has been machine-checked for correctness.

While the completeness theorem guarantees that Simplicity's nine combinators can express any function between (finite) Simplicity types, resulting expressions from the lookup-table construction are impractically large. A function on 256-bit inputs would require a lookup table with 2²⁵⁶ entries. This is why the next chapters focus on building efficient expressions that exploit the structure of computations, rather than brute-forcing everything through lookup tables.

### Conclusion

Simplicity's core language includes a type system and combinators enabling any finite computation. While the Completeness theorem guarantees expressiveness, resulting expressions from the generic construction are impractically large. Practical Simplicity development involves exploiting computational structure for succinct expressions. The next chapters explore data structures, transaction interactions, and additional combinators.

# From Data Types to Programs

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Building Data Types

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

In the previous chapters, we showed how Simplicity's core set of combinators are enough to implement any finite pure computation. This chapter shows how to build practical data structures and computations from these primitives — the same way computers are built from logic gates.

### Boolean Logic

The Boolean type, denoted `𝟚`, equals `𝟙 + 𝟙` and has two values: `σᴸ⟨⟩` (false) and `σᴿ⟨⟩` (true). Using the core combinators, Boolean logic operators can be constructed.

#### And Operation

The logical `and : 𝟚 × 𝟚 ⊢ 𝟚` operation takes two bits and returns one bit. The implementation branches on the first bit: if false, return false; otherwise, return the second bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testing with `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Testing with `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Other Logic Operations

The `not` operation requires a helper combinator:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

The initial `iden ▵ unit : A ⊢ A × 𝟙` adds an empty "environment" to the input, enabling the `case` combinator to apply. The use of `take` in the two branches drops this empty environment to execute `f` or `g`.

Other Boolean logical operations:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit Adders

A "half-adder" takes two bits and adds them, producing a two-bit output: a carry bit and sum bit.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

A "full-adder" adds three bits, producing two-bit output. The input uses nested tuple `(𝟚 × 𝟚) × 𝟚`.

For nested tuples, compact notation is used:

- `O f` denotes `take f`
- `I f` denotes `drop f`
- `H` denotes `iden`

For example, `I O H` means `drop (take iden) : A × (B × C) ⊢ B`, extracting the middle value. The notation evokes binary digits: when thinking of nested tuples as binary trees, the notation represents reversed binary digits of tree positions. These expressions form De Bruijn indices for Simplicity.

**Note:** The `I`, `O`, and `H` notation only applies to subexpressions consisting solely of `take`, `drop`, and `iden`.

The full-adder composes two half-adders, taking logical `or` of the carry bits:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

In the first line, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` runs the half-adder on the first two bits, saving the last bit.

In the second line, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` saves the first bit (the carry-out of the first half-adder) and runs the half-adder on the last two bits.

In the last line, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` takes the logical OR of the first two bits (carry-outs of both half-adders) and returns the sum-out bit of the second half-adder.

This demonstrates Simplicity programming: using `I`, `O`, and `H` notation to reference data bits, forming suitable "environments" for calling other functions via sequential composition.

Users don't define low-level operations directly. Later this series discusses standard library jets implementing common functions. End users aren't expected to program directly in Simplicity, similar to Bitcoin Script. Instead, higher-level languages like SimplicityHL generate Simplicity code, managing subexpression "environments" and translating named variables into appropriate `take` and `drop` sequences.

### Vectors

Fixed-length vectors are defined by forming iterated products of type `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

These may be written as `A^2`, `A^4`, `A^8`, etc.

Vectors are defined only for lengths that are powers of two. Other powers require choosing bracketing conventions.

Given expression `f : A ⊢ B`, repeated pairing "maps" it over fixed-length vectors:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Given function `f : A × B ⊢ B`, iteration or "folding" over fixed-length vectors:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Many variations exist. Given `f : A × B ⊢ C`, "zip" over paired vectors with `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Given `f : (A × B) × C ⊢ C`, fold over paired vectors with `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Combining `map` and `fold-right` creates accumulating combinators: `f : A × C ⊢ C × B` yields `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Many more variants are possible.

#### Multi-bit Words

A bit vector yields multi-bit integers. For example, `𝟚³²` is a 32-bit word type. `𝟚²⁵⁶` is a 256-bit word type, suitable for hashes and cryptographic operations.

Using the full-adder, a variant of vector operations defines a "ripple carry adder" over multi-bit words:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` takes two n-bit binary numbers and a one-bit carry-input, returning a one-bit carry-out flag and an n-bit sum.

#### SHA-256

By recursively defining arithmetic operations on multi-bit words — subtraction, multiplication, division — and bit-wise logical operations such as logical AND, OR, XOR, and repeatedly combining these, even SHA-256's block compression function can be built:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

The SHA-256 compression is formally defined using Simplicity within the Rocq proof assistant (formerly Coq), with a formal proof that the `sha256-hash-block` implementation is correct.

The compression runs too slowly as raw Simplicity. Jets execute common functions like SHA-256 compression natively. Pure Simplicity implementations serve as formal specifications for jets.

### Option Types

Option types result from taking a sum with the unit type:

```
Option A ≔ 𝟙 + A
```

The type `Option A` may be written as `A?` or `𝕊 A` (where `𝕊` means "successor"). Functions map over option types:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Monadic combinators such as bind can be defined:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Variable Length Buffers

"Buffers" are types for partially filled vectors:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

The type `Xᑉ⁸` expands to `(1 + X⁴) × ((1 + X²) × (1 + X))`. Treating this as a polynomial and expanding yields `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interpreting as a type, it represents the sum of all possible tuples of X up to 7, including the empty tuple. This is exactly the type of lists with length strictly less than 8.

Like vectors, mapping and folding operations can be defined over buffers. Stack operations include `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` and `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` appends an item to the buffer, returning a full vector if overflow occurs. `pop-<n` removes an item, returning the smaller buffer and removed item, optionally returning nothing if the original buffer was empty.

The `push-<n` definition, recursively:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Raw Simplicity becomes difficult to follow beyond certain complexity levels. End users utilize higher-level languages like SimplicityHL generating these idiomatic expressions.

### Conclusion

This chapter showed how to build logical operations from bits. From these, bit-level arithmetic emerged, enabling reasoning about execution. Vector types were developed, demonstrating iteration over multi-bit words for arithmetic definition. Continuing, cryptographic operations like SHA-256 and Schnorr signature validation can be defined using Simplicity combinators alone — all actually defined using Simplicity.

This chapter isn't a comprehensive guide to all possible data types and operations buildable in Simplicity, but illustrates achieving practical functionality within Simplicity's constraints. Despite finitely bounded types, useful vectors, buffer types, and operations iterating over these structures can be defined.

Actual standard library operation specifications differ slightly from definitions here. For instance, the full-adder uses a 3-way XOR and "majority" logic function rather than two half-adders.

In practice, Simplicity programs use jets for arithmetic and cryptographic operations. However, jets only replace expressions. Combinators iterating over buffers and vectors cannot be replaced by jets, appearing in actual Simplicity programs. Though rather than directly using these, end users employ higher-level languages like SimplicityHL generating such expressions.

Recursively defined combinators appear to grow exponentially in expression size. This isn't problematic. During serialization, expressions are encoded as DAGs (directed acyclic graphs) rather than trees. Actual representation grows only linearly.

So far, only pure computations were considered. Interaction with transaction data for tasks like signing transactions requires some way for programs to fail if signatures are invalid. The next chapter discusses side-effects in Simplicity.

## Two Side Effects

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

In the previous chapters, we showed how to build some data structures and computations using Simplicity's core set of combinators. As we noted, the core combinators are enough to implement any finite pure computation. This raises the question: what more can be achieved? We can add additional side effects to our expressions.

There are various kinds of possible side effects for expressions: state update, writing to a log, throwing an exception, reading from an environment, calling a continuation, etc. The side effects available in Simplicity will depend on the application.

For Bitcoin and Liquid applications, we currently have two side effects: the Failure effect, which is an exception effect where the exception has type `𝟙`, and the Reader effect which allows data from the transaction environment to be accessed. Our core combinators are "pure"; they have no side effects. However, jets can introduce new primitives that do have side effects.

### Jets with Effects

We will talk more about jets later in this course, but here we introduce a few example jets to illustrate their side effects.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` is a jet for an expression that takes an x-only pubkey, a 256-bit message, and a Schnorr signature, and returns nothing! According to its type, it ought to behave the same as a `unit`. The difference lies in the jet's side effect: if the signature validation fails, then the entire computation is aborted by throwing an exception (of unit type). This is the Failure effect.

#### Verify

`verify : 𝟚 ⊢ 𝟙` is a barebones jet for expressing the Failure effect. If `verify`'s input is `false`, the entire computation is aborted, by throwing an exception. If the input is `true`, nothing is returned, but the computation can continue.

#### Transaction Hashes

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` appears to be a constant function, since there is only one possible input value: the empty tuple. However, this jet reads from the transaction environment and produces a hash of transaction data that is analogous to the `SIGHASH_ALL` message digest used in Bitcoin Script's signature verification. This is an example of the Reader effect: the value returned depends on the transaction environment that the jet is executed within. There are several other hashing jets that hash various subsets of the transaction environment data to help build custom message digests for signatures.

#### Introspection Jets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` is a function that takes an input index and returns the transaction's sequence number for that input, optionally returning nothing if the index is out of bounds. Again, the output value is not a pure function of the input index, but rather, the operation uses the Reader effect to access the transaction environment in order to determine the output value. There are several other introspection jets that return various fragments of the transaction environment data.

### Classifying Effects

Not all side effects are created equal. Some side effects behave nicer than others. We can classify effects by how amenable they are to program transformations.

#### Commutative Effects

A commutative effect is one where, if you swap the outputs of two expressions, you can safely swap the expressions themselves without changing the expression's effect. Consider `swap = I H ▵ O H : A × B ⊢ B × A`. If `f ▵ g ⨾ swap = g ▵ f` for every expression `f` and `g` with side effects, then the effects are commutative.

Reading transaction data from the environment is a commutative effect because the result of reading from the environment is the same, no matter what order we execute the reading in.

In general, throwing an exception is not a commutative effect. If `f` throws some exception `e₁` and `g` throws some other exception `e₂`, then which exception is thrown from the pair of `f` and `g` depends on the order they are executed in.

However, in the special case of the Failure effect, in which only a unit typed exception can be thrown, the effect is commutative. No matter which of `f` or `g` throws an exception, the resulting exception will be the same, because there is only one possible exception value.

#### Idempotent Effects

An idempotent effect is one where, if you duplicate the output of an expression, you can safely duplicate the expression itself without changing the expression's effect. Consider `dup = iden ▵ iden : A ⊢ A × A`. If `f ⨾ dup = dup ⨾ f ▵ f` for every `f` with side effects, then the effects are idempotent.

Reading transaction data from the environment is an idempotent effect. Throwing an exception is also an idempotent effect. Even though only one of the two duplicated expressions will be executed, any exception thrown by `dup ⨾ f ▵ f` will be the same as the exception thrown by `f ⨾ dup`.

However, writing to a log may not be idempotent, as duplicating the effect would cause the log message to appear twice. However, if the log consists of a _set_ of messages instead of a _list_ of messages, then the effect would be idempotent (and commutative) because set insertion is itself an idempotent operation.

#### Unitary Effects

A unitary effect is one where, if you discard the output of an expression, you can safely discard the expression itself without changing the expression's effects. If it is always the case that `f ⨾ unit = unit` for every `f` with side effects, then your effects are unitary.

Reading data from the environment is one of the few types of unitary effects. If the result of reading transaction data from the environment is discarded, the whole expression performing the read may be discarded.

The failure effect isn't unitary. If `f` throws an exception then so will `f ⨾ unit`; execution will not even make it to the `unit` combinator before the computation is aborted. On the other hand, `unit` obviously would not throw any exception, so the effects of `f ⨾ unit` and `unit` would be different.

To summarize, here is how the effects discussed above fare against these three properties:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (transaction environment) | ✓ | ✓ | ✓ |
| Failure (unit-typed exception) | ✓ | ✓ | ✗ |
| Writer (log as a set) | ✓ | ✓ | ✗ |
| General exceptions (arbitrary type) | ✗ | ✓ | ✗ |

### Effects Allowed in Simplicity

The more well-behaved properties that a type of effect has, the more room a Simplicity optimizer has for transforming programs that use those effects. Ideally we would only allow effects that have all three properties: commutative, idempotent, and unitary. This would allow an optimizer to perform any sort of program transformation it would like. However, reading from an environment is the only effect that satisfies all three properties.

Instead we demand that Simplicity effects are commutative and idempotent. Both the effects we use in Simplicity, the Failure effect and the Reader effect, are commutative and idempotent. This allows a large class of optimizations to be performed on Simplicity code.

However, the "discard" transformation described above, attempting to replace `f ⨾ unit` with `unit`, or any similar transformation is not allowed if `f` may produce a Failure effect. Indeed, imagine if `f` contained a `bip0340-verify` assertion. It would be disastrous to attempt to optimize that check away.

### Why Allow Side Effects At All?

Why does Simplicity even allow side effects at all? Wouldn't it be better if every program took the entire transaction as input and returned a Boolean output that decides if a transaction is valid or not?

#### Batch Verification

One reason we have the Failure effect is to support [batch verification](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) of Schnorr signatures. In batch verification, many individual Schnorr signature checks are pooled together in such a way that if any single signature check fails, then the entire batch fails.

This batching procedure improves efficiency over individually verifying each signature. The downside is that if the batch verification fails, then we do not learn which specific signature check or checks failed.

By using the failure side effect, `bip0340-verify` ensures that if a signature check fails, the whole transaction fails. If `bip0340-verify` were instead to return `𝟚`, a Boolean type, for success or failure, then a failing signature check could still lead to a branch where the script succeeds. In such a case we would need to know if the particular signature is valid or not, and thus we wouldn't be able to take advantage of batch verification.

#### Precomputed Transaction Data

A problem in early Bitcoin Script was that the hashing function used to create message digests for signatures was linear in the size of the transaction. Typically every input creates at least one message digest for signature verification, so overall the amount of hashing was quadratic in the transaction size.

This problem was fixed in Segwit and later iterations of Bitcoin Script by redefining the message digests so that they could be computed in constant time per signature check. This relies on having `PrecomputedTransactionData`, which precomputes hashes of transaction data once and is then shared by each input's sighash computations. Simplicity's transaction hashing jets rely on the same kind of precomputed transaction data in order to ensure the jets run in constant time.

Suppose `sig-all-hash` didn't use the Reader effect. Suppose we somehow managed to build a Simplicity type for the transaction environment. Let's call it `TxEnv`, so that `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` was the jet's type. Such a definition would require the `sig-all-hash` jet to be able to compute the hash of any transaction, not just the transaction it is involved with. Simplicity programs could copy the given `TxEnv` and pass a modified copy of it to `sig-all-hash`. In such a case `sig-all-hash` couldn't rely on `PrecomputedTransactionData`, and we would be back to requiring linear time in whatever transaction data was passed into this version of `sig-all-hash`.

Because `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` uses the Reader effect to access the transaction data, it _only_ gets access to a fixed transaction environment. For that reason, the jet's implementation can safely use `PrecomputedTransactionData` and operate in constant time.

### Cross-Input Signature Aggregation

While neither Liquid nor Bitcoin support [cross-input signature aggregation](https://hrf.org/latest/cisa-research-paper/) at this point in time, we would like to check that Simplicity can be compatible with it when the time comes.

While details haven't been worked out, we imagine half-aggregation being implemented using a Writer effect. That is, a new jet with a type such as `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` would take a public key, message digest, and the `r`-component of a Schnorr signature (a Schnorr signature consists of an `r`-component and an `s`-component) and write it to a transaction log before continuing on with execution. Then, elsewhere in the transaction or with the transaction, an aggregate `s`-component for all half-aggregated Schnorr signatures would be provided. The transaction would only be valid when such an aggregate `s`-component is provided for all the logged keys, messages, and `r`-components.

To meet Simplicity's requirements, this Writer effect needs to be idempotent and commutative. This can be ensured by treating the writer log as a set of key, message, `r`-component tuples. This works because set operations are idempotent and commutative. Treating the log as a set of values would be compatible with the half-aggregation verification algorithm.

### Conclusion

In this chapter we looked at adding side effects to the computations that Simplicity can do. We classified various kinds of effects according to how well-behaved they are with respect to various kinds of program transformation. We decided to restrict Simplicity's effects to those that are commutative and idempotent.

The two effects we use for Bitcoin and Liquid applications are the Reader effect, for accessing the transaction environment, and the Failure effect, for aborting and failing the program. Some jets make use of primitive operations where these sorts of side effects can occur.

The Failure effect determines the output of a Simplicity program: the program either fails, making the transaction invalid, or the program succeeds. The Reader effect provides one sort of input to a Simplicity program: the environment containing transaction data. But we also need to provide other inputs, such as digital signatures, to Simplicity programs.

In the next chapter we will look at what Simplicity programs are, how they are turned into addresses, and how we add other inputs, such as signatures, to Simplicity programs.

## Programs and Addresses

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

In the previous chapter we described two side effects used in Simplicity: the Failure effect, which determines a program's success or failure, and the Reader effect, which provides access to the transaction environment. Now we turn to the practical question: what exactly is a Simplicity program, and how does it become an address on the blockchain?

### Simplicity Programs

A Simplicity program is defined as a Simplicity expression of type `𝟙 ⊢ 𝟙`. This type signature means the program takes no meaningful input (just the unit value) and produces no meaningful output (just the unit value). The Reader effect captures the transaction environment input, while the Failure effect indicates success or failure. These effects handle I/O rather than Simplicity types themselves.

### Commitment Merkle Root

Rather than storing complete programs on-chain, Bitcoin employs commitments — a practice extending from Pay-to-Script-Hash (P2SH). Simplicity uses a Commitment Merkle Root (CMR).

Each combinator receives a SHA-256 tag derived from the pattern: `Simplicity␟Commitment␟[identifier]`, where `␟` represents ASCII code 31 (the unit separator).

Each tag is the SHA-256 hash of the corresponding pre-image string listed below:

| Combinator | Tag pre-image (ASCII string) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

A Simplicity expression is then recursively hashed into a 256-bit CMR by computing a tagged SHA-256 midstate for each combinator together with the CMRs of its arguments (write `#ᶜ(e)` for the CMR of expression `e`, and `∥` for byte concatenation):

| Combinator | CMR rule |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Binary combinators (`comp`, `pair`, `case`) concatenate the CMRs of both children; unary combinators (`take`, `drop`, `injl`, `injr`) concatenate their single child's CMR after 32 bytes of `0x00` padding; and the nullary leaves (`iden`, `unit`) hash their tag alone. Two conventions keep this cheap to compute: SHA-256 midstates are used so that **each expression requires at most one call to the SHA-256 compression function** (assuming the midstate up to the constant tags is precomputed), and the one-argument constructors prefix their argument with 32 bytes of `0x00` padding, which allows for a little extra precomputation for implementations that want it.

For the `unit` combinator — a nullary constructor with no argument sub-expressions — this rule specialises to `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, where `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (the tag is fed in twice). The resulting CMR for the trivial `unit` program is:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Critically, the CMR does not commit to the types of Simplicity expressions, relying instead on type inference during redemption.

### Addresses

Addresses employ BIP-0341's Taproot mechanism with CMRs committed under TapLeaf version `0xbe`. The process involves:

1. Computing a TapLeaf tagged hash combining the version byte, CMR length, and CMR itself
2. Tweaking an internal public key (using a NUMS point when no key-spend path is desired)
3. Converting to bech32m format
4. Adding appropriate checksums

When no key-spend path is desired, the internal public key is set to a **NUMS** ("Nothing-Up-My-Sleeve") point: a curve point deliberately chosen so that nobody knows its discrete logarithm — in other words, a point with no corresponding private key. Because no one can ever produce a signature for it, the key-spend path is provably unusable, and the output can be spent *only* through the committed Simplicity script path. In a real application, this NUMS point should be randomized as recommended by BIP-0341, so that outputs with no key-spend path are indistinguishable from ordinary Taproot outputs (a privacy benefit).

#### From Simplicity to Address

Let's walk through the whole derivation for the simplest program possible: `unit : 𝟙 ⊢ 𝟙`, a no-op that always succeeds.

**1. Combinator tag.** First compute the `unit` tag:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Feed the tag in twice to obtain the program's CMR:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf hash.** Prefix the CMR with Simplicity's TapLeaf version `0xbe` and the CMR length `0x20` (32 bytes), then take the Elements TapLeaf tagged hash (a tagged hash is `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

With only this one leaf there are no TapBranches, so this hash is already the TapTree root.

**4. TapTweak.** Since we want no key-spend path, we use the BIP-0341 NUMS point as the internal key and tweak it with the TapTree root:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Output key.** Tweak the internal key on the curve, `output_pk = lift_x(internal_pk) ⊕ t·G` (the elliptic-curve arithmetic is summarized here), giving the x-only output key `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Bech32m address.** Encode the x-only output key, prefix a `p` (the SegWit v1 witness-version character), add the Liquid-testnet human-readable prefix `tex1`, and append the Bech32m checksum. The final address is:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

That was a lot of work — but much of it is mandated by Taproot itself, not by Simplicity.

### Witness Expressions

A new combinator type addresses the absence of input to Simplicity programs: the witness expression. The `witness` combinator permits signature data and other witness material to be integrated into programs.

```
      w : B
-----------------
witness w : A ⊢ B
```

The witness expression's semantics is straightforward: it ignores its input and simply returns the value `w` (which may be of any Simplicity type), i.e. `⟦witness w⟧(a) = w`. This adds **no new expressiveness** — by the completeness theorem, Simplicity can already build any such constant function (recall the `scribe` macro from the previous chapters). The point of the `witness` combinator lies entirely in its **CMR**: the value `w` is **excluded** from the expression's CMR, so the address can be computed before `w` is known, and `w` is supplied at redemption time.

This design choice supports pruning — unexecuted conditional branches needn't be revealed on-chain, including their associated witness expressions. When a branch is pruned, the verifier only needs the CMR of the pruned subtree, not its actual content.

### Witness Values

It may seem like a limitation that a witness expression can hold only a *value*, and not a more general Simplicity expression. But programs for UTXO-based blockchains are executed only once. There is no need to pass a whole sub-expression into a witness node: the user can simply run that sub-expression themselves, off-chain, and transcribe its output into the witness value to obtain the very same result.

(Later in this course we will meet the `disconnect` combinator, which behaves much like a witness expression that *does* take an entire Simplicity expression as its argument.)

An alternative design would feed all witness data in as an argument to the top-level Simplicity program. Witness expressions are preferred for two reasons. First, **pruning**: unexecuted branches of `case` expressions are never revealed on-chain, and any witness expressions inside those branches are pruned away along with them. Second, **locality**: witness expressions let us place each witness value exactly where it is used, instead of threading it down from the program's top-level input.

### Type Inference

Since CMRs don't commit to types, the type system is reconstructed during redemption. Simplicity's type inference algorithm determines the minimal types for each subexpression based on the combinator structure. More precisely, inference computes the *principal* (most general) type of every subexpression; any type variables that remain free are then instantiated to the unit type `𝟙`, which yields a unique, minimal type for the program.

### Conclusion

In this chapter we established that Simplicity programs are expressions of type `𝟙 ⊢ 𝟙`, explained how Commitment Merkle Roots are constructed from tagged SHA-256 hashes of each combinator, and showed how CMRs are turned into on-chain addresses via BIP-0341 Taproot. We introduced witness expressions as the mechanism for providing signature data and other inputs at spending time without committing to their values at address creation time.

# Final Section

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Reviews & Ratings

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusion

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
