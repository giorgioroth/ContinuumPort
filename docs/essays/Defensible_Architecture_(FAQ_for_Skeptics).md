
## Defensible Architecture (FAQ for Skeptics)

### 1. "Isn't this just a glorified JSON summary?"

**Yes.** And that is its greatest strength. ContinuumPort does not aim for structural complexity, but for **normative restriction**. While a standard "summary" is informal and often contaminated with behavioral instructions or persona drift, CP-Core is a strictly defined transport layer. It standardizes the *data*, not the *formatting*.

### 2. "Why not just use a well-crafted system prompt?"

System prompts are model-dependent, fragile, and constitute a "prompting trick" rather than a robust architecture. ContinuumPort separates the **Semantic State** (the *what*) from the **Regen Engine** (the *how*). By treating task continuity as a data serialization problem, we achieve true multimodel portability. **Prompt construction is explicitly out of scope for the protocol.**

### 3. "Does this really protect privacy if the state is plain text?"

Its primary privacy contribution is the **Prevention of Identity Leakage**. By explicitly forbidding the storage of user style, emotional tone, or personal history, the protocol ensures that even if a container is intercepted, it contains only "work in progress," not a "psychological profile" of the user. We standardize the exclusion of identity.

### 4. "Without the 'Regen Engine', isn't the protocol useless?"

A protocol is a contract, not a product. TCP/IP doesn't send emails; it moves packets. ContinuumPort moves semantic state. By separating the **Transport Layer (CP-Core)** from the **Interpretation Layer (Regen Engine)**, we allow the ecosystem to build diverse, conformant engines that all speak the same semantic language.

### 5. "What prevents vendors from adding their own 'tracking' fields?"

The specification allows for extensions, but they are marked as **Non-Normative**. A Regen Engine is conformant **if and only if** removing all non-normative layers (tracking, embeddings, proprietary metadata) does not change the reconstructed semantic intent. We provide the standard that allows users to detect and strip away vendor lock-in.


