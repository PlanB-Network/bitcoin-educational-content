---
name: Delving Into Simplicity
goal: Understand Simplicity's design philosophy, type system, and combinator-based approach to blockchain computation.
objectives:
  - Understand why blockchain computation requires a fundamentally different language design
  - Master the three composition methods; sequential, parallel, and conditional
  - Learn Simplicity's type system including unit, sum, product, and boolean types
  - Understand the nine core combinators and the completeness theorem
  - Build practical data structures and computations from Simplicity primitives
---

A deep dive into Simplicity, the next-generation Bitcoin scripting language activated on the Liquid Network. This course explores its type system, its nine core combinators, and how complex computations — from boolean logic to SHA-256 — are built from minimal primitives. Based on the ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) article series by [Dr. Russell O'Connor](https://r6.ca/) (Blockstream Research).

+++

# Introduction

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Course overview

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Welcome to SCR401 — Delving Into Simplicity!

This course is based on the **"Delving Simplicity"** article series written by [Dr. Russell O'Connor](https://r6.ca/), an Infrastructure Tech Developer at [Blockstream](https://blockstream.com/) and the creator of Simplicity. The original articles were published on the [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) forum and form the primary source material for this course. We are grateful for his pioneering work, which made this educational content possible.

### What you will learn

This course explores the design philosophy and mathematical foundations behind Simplicity, the next-generation scripting language activated on the [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) in July 2025. It is structured in four main parts:

1. **A Blockchain Perspective on Computation** — Why blockchain computation demands a fundamentally different language, and the three ways to combine operations
2. **Core Simplicity and Its Type System** — The minimal type system, the nine core combinators, and the completeness theorem
3. **Building Data Types and Computations** — From boolean logic to SHA-256, constructing real programs from first principles
4. **The Road Ahead** — Future developments, side effects, and the broader vision

### Prerequisites

This is an **expert-level** course (approximately 8 hours). You should be comfortable with:
- Basic Bitcoin scripting concepts (what transaction validation does)
- Fundamental programming concepts (types, functions, composition)
- Some familiarity with mathematical notation is helpful but not required — we introduce everything as we go

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

Simplicity is a **smart contract language for Bitcoin** (and the Liquid sidechain). It was designed from scratch by Dr. Russell O'Connor starting in 2017 and activated on the Liquid Network in July 2025, after years of formal verification and development.

Unlike Ethereum's Solidity — which is a general-purpose, high-level language — Simplicity is intentionally minimal. It has:
- **Three type formers** (unit, sum, product)
- **Nine combinators** (basic operations and composition rules)
- **No loops, no recursion, no dynamic memory**

From just these primitives, you can build any computation you need for transaction validation — from boolean logic to full SHA-256 hashing.

### What can you do with Simplicity today?

Simplicity is already powering real applications on the Liquid Network. The most notable example is the [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/) — a structured options marketplace where users can create and trade call and put options on L-BTC using USDt as collateral, with no price oracle required. The open-source [Deadcat](https://github.com/Resolvr-io/deadcat) protocol implements this, and the [Swaption](https://swaption.io/) app provides a user-facing interface. You can watch a [demo of the DEX in action](https://www.youtube.com/watch?v=4c8bvD6oomw). Beyond DeFi, Simplicity enables any advanced spending condition — vaults, covenants, complex multisig schemes — that would be impossible or unsafe in Bitcoin Script.

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

If terms like "sum types", "combinators", or "sequent calculus" are entirely new to you, don't worry — we explain everything from scratch. But be prepared for a dense, mathematical journey.

### From articles to course

The original "Delving Simplicity" series by Dr. O'Connor is structured as technical blog posts. This course reorganizes and annotates that material into a progressive learning path with quizzes to test your understanding along the way. The ideas, definitions, and proofs are his — we've adapted the format for structured education.

# A Blockchain Perspective on Computation

<partId>7a7690a5-ea70-4d3d-a9c5-299115661db5</partId>

## Why Simplicity Exists

<chapterId>ab030a7a-053d-407f-932b-d71f699f2d0d</chapterId>

Bitcoin's transaction validation is a significantly different application from regular programming language design. It operates under a unique set of constraints that no general-purpose language was built to handle. Understanding these constraints is essential to understanding why Simplicity was created.

### The Unique Constraints of Blockchain Computation

When a Bitcoin transaction is validated, the computation happens under strict resource limitations. Block space is expensive, execution must be deterministic, and every node on the network must arrive at exactly the same result. This creates several design principles that shape everything about how Simplicity works:

**Pruning unexecuted branches.** In a blockchain context, you don't want to store code that never runs. If a transaction script has multiple execution paths, only the taken path should consume block space. Simplicity's design ensures that unexecuted branches can be pruned from the blockchain entirely.

**Quasi-linear preprocessing.** Before a Simplicity program executes, the network needs to validate it. This preprocessing step — which includes type checking and resource estimation — must run in quasi-linear time. There's no room for exponential blowups during validation.

**Static analysis over dynamic metering.** Unlike Ethereum's gas model, which meters execution dynamically, Simplicity allows static analysis to determine resource bounds before execution begins. You know ahead of time exactly how much computation a program requires.

**No dynamic memory allocation.** During execution, Simplicity programs don't allocate memory dynamically. Everything is determined by the types at compile time. This eliminates entire classes of bugs and attack vectors.

### What Simplicity Is Not

Simplicity is not a general-purpose programming language. You wouldn't write a web server or a game in it. It's designed for one purpose: expressing the conditions under which Bitcoin (or Liquid) transactions are valid. This narrow focus allows for a radically minimal design.

The fundamental question that Simplicity answers is this: given a set of basic blockchain operations — checking signatures, hashing data, inspecting transaction fields — what are the methods for combining these operations into more complex ones?

The answer, as we'll see in this course, is that there are exactly three fundamental ways to combine computations.

## Sequential Composition

<chapterId>c45df1f0-9cef-4d66-bdc3-f75eb158f7a3</chapterId>

The most fundamental way to combine two operations is to link them sequentially: the output of one operation becomes the input of the next.

### The Pipeline Model

Imagine you have two operations:
- Operation **f** takes an input of type A and produces an output of type B
- Operation **g** takes an input of type B and produces an output of type C

Sequential composition chains them together: the output of **f** flows directly into **g**, creating a new composite operation that takes an A and produces a C.

```
 [f] → B → [g] → C
```

This is the most intuitive form of composition. It's what happens when you pipe commands in a Unix shell, or when you chain function calls in any programming language.

### Key Properties

Sequential composition has several important properties:

1. **Associativity**: Chaining (f then g) then h is the same as chaining f then (g then h)
2. **Recursiveness**: The composite operation (f then g) is itself an operation, so it can be composed further
3. **Type safety**: The output type of the first operation must match the input type of the second

### In Bitcoin Script

In Bitcoin Script, sequential composition is achieved simply by concatenating scripts. When you write `OP_DUP OP_HASH160`, the DUP operation produces a value that HASH160 immediately consumes. The stack serves as the implicit connector between operations.

### In Simplicity

In Simplicity, sequential composition is made explicit through the `comp` combinator (also written as `⨾` or `>>>`). If `f : A ⊢ B` and `g : B ⊢ C`, then:

```
comp f g : A ⊢ C
```

The semantics are straightforward: `⟦comp f g⟧(a) = ⟦g⟧(⟦f⟧(a))` — apply f first, then apply g to the result.

## Parallel Composition

<chapterId>8ede59a8-10b0-43ad-a3c0-87695e5e5ef4</chapterId>

The second fundamental way to combine operations is to run them in parallel on the same input.

### Running Operations Side by Side

Given two operations that both accept the same input type:
- Operation **f** takes input A and produces output B
- Operation **g** takes input A and produces output C

Parallel composition gives both operations the same input and collects both results into a pair:

```
 [f] → B ─┐
 (B, C)
 [g] → C ─┘
```

The result is a **product type** — a pair containing both outputs. Whether the two operations physically execute simultaneously or one after the other doesn't matter; what matters is that they both receive the same unmodified input.

### Product Types

The product type `B × C` contains pairs of values `⟨b, c⟩`. These are like tuples or structs in other languages. In Simplicity, product types are the fundamental way to bundle multiple pieces of data together.

### In Bitcoin Script

Bitcoin Script achieves parallel composition through stack manipulation. You can duplicate the top of the stack with `OP_DUP`, then apply different operations to the copies. It's less elegant but functionally equivalent.

### In Simplicity

Parallel composition uses the `pair` combinator (also written as `▵` or `&&&`):

```
pair f g : A ⊢ B × C
```

Semantics: `⟦pair f g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩` — apply both f and g to the same input, pair the results.

## Conditional Composition

<chapterId>7f38ccc5-bd5b-4404-aef0-1928ecb97c90</chapterId>

The third and final fundamental composition method introduces choice: given two alternative operations, which one executes depends on the input.

### Sum Types and Tagged Unions

Before we can define conditional composition, we need the concept of a **sum type**. A sum type `A + B` is a tagged union — a value that is either a left-tagged value of type A, or a right-tagged value of type B. The tag (a single bit) tells you which alternative the value represents.

We write left-tagged values as `σᴸ(a)` and right-tagged values as `σᴿ(b)`.

### Branching on the Tag

Given two operations:
- Operation **f** handles the "left" case (input of type A)
- Operation **g** handles the "right" case (input of type B)

Conditional composition inspects the tag and routes execution accordingly:

```
 [f] → D
 [g] → D
```

Both branches must produce the same output type. This ensures that no matter which path is taken, the rest of the program can proceed without knowing which branch executed.

### In Bitcoin Script

Bitcoin Script uses `OP_IF ... OP_ELSE ... OP_ENDIF` for conditional execution. A value on the stack determines which branch runs. This is Bitcoin's original mechanism for expressing choice.

### In Simplicity

Simplicity uses the `case` combinator, which provides conditional composition along with a shared environment:

```
case f g : (A + B) × C ⊢ D
```

The extra type C acts as a shared environment that both branches can access. This is more powerful than a simple `if-then-else` because both branches receive context alongside their specific data.

### Why Only Three Methods?

These three composition methods — sequential, parallel, and conditional — are not arbitrary choices. They arise from fundamental mathematical structures. Sequential composition corresponds to function composition. Parallel composition corresponds to the product construction. Conditional composition corresponds to the coproduct (sum) construction. Together, they form a complete basis for expressing any computation over finite types, as we'll prove in Part 2 of this course.

### No Recursion

Notably absent from this list is recursion. Simplicity deliberately excludes unbounded recursion. In a blockchain context, you need guaranteed termination and predictable resource usage. Recursive covenants that compute across multiple transactions better serve iterative needs without blowing up block space within a single transaction.

# Core Simplicity and Its Type System

<partId>dabbd97b-4fad-4c16-a189-6d768c97c82d</partId>

## Simplicity Types

<chapterId>4067acaa-8b28-4741-9a0a-66013897e28b</chapterId>

Simplicity's type system is remarkably minimal. There are exactly three ways to form types, and from these three, all the data structures you need can be built.

### The Unit Type (𝟙)

The unit type, written `𝟙` or `ONE`, contains exactly one value: the empty tuple `⟨⟩`. Think of it as a zero-bit data type — it carries no information. While this seems useless, it plays a crucial role as a building block. It's the starting point from which all other types are constructed.

### Sum Types (A + B)

A sum type `A + B` represents a tagged union of two types. A value of type `A + B` is either:
- `σᴸ(a)` — a left-tagged value where `a` has type A, or
- `σᴿ(b)` — a right-tagged value where `b` has type B

The tag is a single bit that distinguishes which variant you have. Even when A and B are the same type, left-tagged and right-tagged values are distinct: `σᴸ(a)` ≠ `σᴿ(a)`.

### The Boolean Type (𝟚)

The simplest useful sum type is `𝟙 + 𝟙`, written `𝟚` or `TWO`. This is a one-bit data type with exactly two values:
- `σᴸ⟨⟩` — conventionally represents **false** or **0**
- `σᴿ⟨⟩` — conventionally represents **true** or **1**

This is how Simplicity represents single bits. Everything from cryptographic hashes to transaction signatures is ultimately built from this type.

### Product Types (A × B)

A product type `A × B` contains pairs of values `⟨a, b⟩`. This is how you bundle two pieces of data together — like a struct with exactly two fields.

### Counting Values

You can think of types arithmetically:
- `𝟙` has 1 value
- `𝟚` = `𝟙 + 𝟙` has 1 + 1 = 2 values
- `𝟚 × 𝟚` has 2 × 2 = 4 values
- `𝟚 + 𝟚` has 2 + 2 = 4 values (but structured differently!)

This arithmetic interpretation is not just a mnemonic — it precisely captures the number of distinct values each type can hold.

### No Function Types

Critically, Simplicity's types do not include function types. Simplicity is a **first-order** language. Functions exist as combinators that transform data, but data itself never contains functions. This restriction is essential for the static analysis properties that blockchains require.

## Basic Operations and Composition Combinators

<chapterId>dc247e58-a753-4a46-9e4b-62fbb7e8f1b7</chapterId>

Simplicity expressions denote operations with typed inputs and outputs. We write `f : A ⊢ B` to mean "f is an operation that takes input of type A and produces output of type B."

### The Two Basic Operations

Simplicity starts with just two primitive operations:

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

Both are families of operations — there's one `iden` and one `unit` for every Simplicity type.

### The Three Composition Combinators

We already met these in Part 1, but now we can state them precisely with types:

**Sequential Composition (`comp`):**
```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦comp f g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

**Parallel Composition (`pair`):**
```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦pair f g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

**Conditional Composition (`case`):**
```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

The `case` combinator is slightly more powerful than a simple conditional because it distributes a shared environment (type C) to both branches.

### Values vs. Expressions

An important distinction: Simplicity expressions are operations (functions), not values. The notation `scribe b : A ⊢ B` represents the unique expression that always returns the value `b`, regardless of input. For example:

```
scribe ⟨σᴸ⟨⟩, σᴿ⟨⟩⟩ = pair (injl unit) (injr unit) : A ⊢ 𝟚 × 𝟚
```

This is analogous to Bitcoin Script's `OP_1`, which is not the value 1 — it's the operation that pushes 1 onto the stack.

## Extractors, Injectors, and the Sequent Calculus

<chapterId>19e0aa6a-f1e1-4307-8646-2c676d3ea937</chapterId>

Beyond the two basic operations and three composition combinators, Simplicity has four more combinators that complete its core. These handle the mechanics of accessing data within product and sum types.

### Extractors: take and drop

These combinators reach into product types to access their components:

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

Think of `take` and `drop` as projection operators. `take iden` gives you the left element of a pair. `drop iden` gives you the right element.

### Injectors: injl and injr

These combinators wrap values with tags to create sum type values:

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

### The Nine Core Rules

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

### Connection to the Sequent Calculus

These nine rules closely resemble the conjunctive-disjunctive fragment of Gentzen's sequent calculus — a foundational system in mathematical logic. Just as the Curry-Howard correspondence links lambda calculus to natural deduction, Simplicity represents a tweaked variant of the functional interpretation of Gentzen's sequent calculus.

This connection isn't just theoretical elegance. The sequent calculus formulation ensures that types in the premises are always smaller than in the conclusions. The **Bit Machine** — Simplicity's abstract stack machine interpreter — exploits this property to minimize data copying during execution.

## Completeness of Simplicity

<chapterId>7770b8e6-4a4f-40d0-87cc-11d378a6f5ad</chapterId>

The most remarkable property of Simplicity is its completeness theorem: **for any function between two Simplicity types, there exists some Simplicity expression that denotes it.**

### What Completeness Means

Despite having only nine combinators, Simplicity can express every possible function from any type A to any type B. If you can describe the function's behavior on all possible inputs, you can build a Simplicity expression that implements it.

### How the Proof Works

The proof is constructive — it actually shows you how to build the expression. The method is conceptually simple:

1. **Decompose the input**: Using nested `case` expressions, fully decompose any input of any type into its constituent bits
2. **Build a lookup table**: For each possible input, use `scribe` to produce the corresponding output
3. **Assemble**: The nested cases and scribes together form a giant lookup table that implements the function

For example, to implement a function on `𝟚 × 𝟚` (which has 4 possible inputs), you'd build a tree of case expressions that tests each bit and maps to the correct output.

### Practical Implications

The completeness theorem guarantees that Simplicity's nine combinators are a sufficient foundation for any blockchain computation. You never need to add new primitives to express a function — the language is already capable of expressing it.

However, the lookup-table construction produces expressions of astronomical size for large types. A function on 256-bit inputs would require a lookup table with 2²⁵⁶ entries — clearly impractical. This is why Part 3 of this course focuses on building efficient expressions that exploit the structure of computations, rather than brute-forcing everything through lookup tables.

### Formal Verification

The completeness theorem has been formally verified in the Rocq proof assistant (formerly Coq). The proof is part of the official Simplicity repository and has been machine-checked for correctness.

# Building Data Types and Computations

<partId>7cbc15b8-739e-4452-99de-3fa9b3feb119</partId>

## Boolean Logic in Simplicity

<chapterId>e6a198ac-1ac7-4ce7-9292-9d56b49613b7</chapterId>

With only three type formers and nine combinators, Simplicity may seem too minimal for practical use. This part demonstrates how abstractions are built up from these basics — the same way computers are built from logic gates.

### The Boolean Type Revisited

Recall that the boolean type `𝟚 = 𝟙 + 𝟙` has two values:
- `σᴸ⟨⟩` = false (0)
- `σᴿ⟨⟩` = true (1)

Boolean operations take one or two bits as input and produce a bit as output. Let's build them from scratch.

### Logical AND

The AND function is defined as:

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

How does this work? The input is `⟨bit₁, bit₂⟩`. The `case` combinator branches on the first bit:
 `injl unit` produces `σᴸ⟨⟩`
 `drop iden` extracts bit₂

This matches the truth table for AND: false AND anything = false; true AND x = x.

### Logical OR

```
or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚
```

 `drop iden`
 `injr unit`

### Logical NOT

```
not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚
```

This uses a helper combinator `copair`, defined as:
```
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

The `copair` adds a trivial environment to enable the case combinator to work on pure sum types.

For NOT: if input is false, return true; if true, return false.

### Logical XOR

```
xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚
```

- If bit₁ is false: return bit₂ unchanged
- If bit₁ is true: return NOT bit₂

These four operations form a complete basis for boolean logic. Every other boolean function can be built from them.

## Bit Adders and Arithmetic

<chapterId>f5bd93d1-3e64-49ce-8876-41a8bfcc22eb</chapterId>

With boolean logic in hand, we can build arithmetic circuits. The approach mirrors how hardware engineers construct adders from logic gates.

### The Half-Adder

A half-adder takes two single bits and produces:
- A **carry** bit (the AND of the inputs)
- A **sum** bit (the XOR of the inputs)

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

This uses parallel composition to compute both outputs simultaneously. For inputs `⟨a, b⟩`, the output is `⟨a AND b, a XOR b⟩`.

### Access Notation

To manage deeply nested pairs, Simplicity uses a shorthand notation:
- `O f` abbreviates `take f` (take the left/first element)
- `I f` abbreviates `drop f` (take the right/second element)
- `H` abbreviates `iden` (the whole thing)

With this notation, navigating nested tuples becomes like navigating a binary tree:
- `O H` = first element of a pair
- `I H` = second element
- `O O H` = first element of the first element
- `I O H` = first element of the second element

This resembles De Bruijn indices, with O and I acting as binary digits representing positions in a tree structure.

### The Full-Adder

A full-adder takes three inputs — two bits and a carry-in — and produces a carry-out and a sum. The input type is `(𝟚 × 𝟚) × 𝟚`:

```
full-adder ≔ take half-adder ▵ I H ⨾
  O O H ▵ (O I H ▵ I H ⨾ half-adder) ⨾
  (O H ▵ I O H ⨾ or) ▵ I I H
  : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

The logic works in three stages:
1. Apply half-adder to the first two bits, preserving the carry-in
2. Apply half-adder to the first sum and the carry-in
3. OR the two carry outputs together, return the final sum

### Multi-bit Words

Bit vectors represent integers. Simplicity uses nested product types for power-of-two lengths:
- `𝟚²` = `𝟚 × 𝟚` (2-bit)
- `𝟚⁴` = `𝟚² × 𝟚²` (4-bit)
- `𝟚³²` (32-bit words)
- `𝟚²⁵⁶` (256-bit — used for hashes and keys)

A ripple carry adder chains full-adders across all bits:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

From addition, subtraction, multiplication, division, and all bitwise operations follow by recursive composition.

## Vectors, Buffers, and Data Structures

<chapterId>8dc8748f-6e52-42a3-9404-77da22d2d2cb</chapterId>

Simplicity's type system, despite its minimalism, supports surprisingly rich data structures.

### Fixed-Length Vectors

Vectors are built from iterated products with power-of-two lengths:
- `A² = A × A`
- `A⁴ = A² × A²`
- `A⁸ = A⁴ × A⁴`

### Mapping Over Vectors

For any operation `f : A ⊢ B`, we can map it over a vector using parallel composition:
- `f² ≔ f ▵ f : A² ⊢ B²` (apply f to both elements)
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

### Folding Over Vectors

For a function `f : A × B ⊢ B` that combines an element with an accumulator:

```
fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B
fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B
```

This recursively folds over vector elements from right to left.

### Option Types

The option type wraps a value with a presence/absence tag:

```
Option A ≔ 𝟙 + A
```

A value of type `Option A` is either `σᴸ⟨⟩` (nothing/none) or `σᴿ(a)` (some value a).

For mapping: `f? ≔ copair (injl unit) (injr f) : Option A ⊢ Option B`

For monadic bind: `bind f ≔ copair (injl unit) f : Option A ⊢ Option B`

### Variable-Length Buffers

Buffers represent partially filled vectors using option types:
- `Aᑉ² ≔ Option A` (0 or 1 elements)
- `Aᑉ⁴ ≔ Option A² × Aᑉ²` (0 to 3 elements)
- `Aᑉ⁸ ≔ Option A⁴ × Aᑉ⁴` (0 to 7 elements)

The type `Xᑉ⁸` expands to `(1 + X⁴) × ((1 + X²) × (1 + X))`, which as a polynomial yields `1 + X + X² + ... + X⁷` — representing collections of 0 to 7 elements.

Stack operations like push and pop are definable:
- `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` — appends an item, returning a full vector on overflow
- `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?` — removes an item, returning nothing if empty

## From SHA-256 to Practical Programs

<chapterId>e3541a33-f57c-4efb-b59b-c6c887061475</chapterId>

The constructions from the previous chapters aren't just theoretical exercises — they lead to real cryptographic implementations.

### SHA-256 in Simplicity

The SHA-256 block compression function can be fully expressed in Simplicity:

```
sha256-hash-block : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

This takes a 256-bit hash state and a 512-bit message block, and produces a new 256-bit hash state. The implementation uses all the building blocks we've covered: boolean logic, multi-bit arithmetic, and vector operations.

The SHA-256 implementation is formally verified in the Rocq proof assistant (formerly Coq), with a machine-checked proof that it correctly implements the standard.

### The Role of Jets

Raw Simplicity execution of SHA-256 would be impractically slow — the expression tree is enormous. This is where **jets** come in.

A jet is a native implementation of a Simplicity expression. The network agrees that when a particular Simplicity expression appears (identified by its Merkle root), it can be replaced with an optimized native implementation. The Simplicity expression serves as a formal specification — it defines exactly what the jet must compute — while the jet provides practical performance.

Common jets include:
- Arithmetic operations (add, subtract, multiply)
- Cryptographic primitives (SHA-256, SHA-512, secp256k1)
- Signature verification
- Bitwise operations

### DAG Serialization

You might worry that Simplicity expressions grow exponentially as they get more complex. In practice, they don't. Simplicity expressions are serialized as **directed acyclic graphs (DAGs)**, not trees. When a sub-expression appears multiple times, it's stored once and referenced multiple times. This keeps expression sizes growing linearly, not exponentially.

### Higher-Level Languages

Nobody writes raw Simplicity by hand for production use. The language **SimplicityHL** provides a higher-level syntax that compiles down to Simplicity expressions. SimplicityHL handles:
- Variable naming and scope
- Automatic environment management
- Library imports
- Familiar control flow syntax

The low-level Simplicity expressions we've studied in this course are the compilation target — the "assembly language" that SimplicityHL generates.

## The Road Ahead

<chapterId>c29188f6-dd5b-40b3-afbc-4cbd9a6a30d9</chapterId>

This course has covered the pure computational core of Simplicity. But a blockchain scripting language needs more than pure computation — it needs to interact with transactions.

### Side Effects

Future installments of the "Delving Simplicity" series will introduce:

**Assertions (fail).** A mechanism for computations to fail, which is essential for transaction validation. If a condition isn't met (e.g., an invalid signature), the computation must be able to reject the transaction.

**Witness data.** A way to provide input data (like signatures) that isn't part of the program itself but is provided at spending time.

**Transaction introspection.** Combinators that read fields from the transaction being validated — amounts, script hashes, lock times, and more.

### Programs and Addresses

Part V of the series will cover how Simplicity programs are structured for deployment:
- How programs are committed to the blockchain
- The Merkle tree structure of Simplicity programs
- Address generation and spending conditions

### The Broader Vision

Simplicity represents a fundamentally different approach to blockchain scripting. Instead of adding features incrementally (as Bitcoin Script does with new opcodes), Simplicity provides a minimal, mathematically complete foundation. New functionality comes from composition, not from expanding the language.

With its activation on the Liquid Network, Simplicity has moved from theory to practice. The concepts you've learned in this course — composition, types, combinators, and data construction — are now powering real transactions on a production blockchain.

### Further Resources

- **Delving Simplicity series**: The [original article series](https://delvingbitcoin.org/u/roconnor-blockstream/summary) by Dr. Russell O'Connor on the Delving Bitcoin forum — the primary source for this course
- **Simplicity GitHub repository**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — source code and Rocq formal proofs
- **Simplicity language website**: [simplicity-lang.org](https://simplicity-lang.org/) — official documentation and SimplicityHL reference
- **Blockstream announcement**: [Simplicity activation on Liquid](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) (July 2025)

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
