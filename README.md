# Nova

Nova is an experimental AI assistant and NLP engine developed from scratch in Python.

The goal of the project is not simply to detect keywords or intents, but to progressively transform natural language into structured semantic meaning through multiple processing layers.

Current development focuses on building a transparent and explainable NLP pipeline capable of understanding:

* What the user wants to do
* Which entities are involved
* The grammatical relationships between them
* The semantic roles they play within the sentence
* The final user intent

---

# Current Architecture

```text
User Input
    ↓
Text Parser
    ↓
ParsedText
    ↓
Semantic Role Extraction
    ↓
Role Frame
    ↓
Intent Engine
    ↓
Action Execution
```

---

# Processing Layers

## 1. Linguistic Analysis

Nova uses spaCy for low-level linguistic processing.

Extracted information:

* Tokens
* Lemmas
* Part-of-Speech tags (POS)
* Dependency relations
* Named Entities (NER)

Example:

```text
Send the report to John tomorrow
```

Produces information such as:

```text
send → VERB
report → NOUN
John → PERSON
tomorrow → DATE
```

---

## 2. Grammatical Extraction

The parser identifies the core grammatical structure of the sentence.

Current elements:

* Root verb
* Direct object
* Indirect objects

Example:

```text
Send the report to John
```

Produces:

```text
ROOT_VERB      → send
DIRECT_OBJECT  → report
INDIRECT_OBJ   → John
```

---

## 3. Semantic Role Extraction

Grammatical structures are converted into semantic roles.

Examples:

```text
ACTION     → send
TARGET     → report
RECIPIENT  → John
TIME       → tomorrow
LOCATION   → Madrid
```

This layer is intended to become Nova's semantic understanding engine.

---

## 4. Intent Detection (In Progress)

Semantic roles will be used to infer high-level intents.

Example:

```text
ACTION     → send
TARGET     → file
RECIPIENT  → John
```

↓

```text
INTENT → SEND_FILE
```

The intent engine will use rule-based scoring and semantic matching rather than simple keyword detection.

---

# Current Data Models

## ParsedText

Contains:

* LinguisticAnalysis
* GrammaticalExtraction

---

## LinguisticAnalysis

Contains:

* TokenData[]
* EntityData[]

---

## GrammaticalExtraction

Contains:

* Root verb
* Direct object
* Indirect objects

---

## Planned Models

### RoleFrame

Represents semantic meaning through role assignments.

Example:

```text
ACTION     → send
TARGET     → report
RECIPIENT  → John
```

---

### Intent

Represents the final interpretation of the user's objective.

Example:

```text
SEND_FILE
OPEN_APP
PLAY_MEDIA
CREATE_EVENT
```

---

# Current Challenges

Nova is currently focused on improving contextual understanding and semantic extraction.

Several limitations have already been identified:

## Preposition Handling

Example:

```text
Send the PDF to John via WhatsApp
```

Current extraction may incorrectly treat:

```text
John
WhatsApp
```

as equivalent indirect objects.

Desired behavior:

```text
John      → RECIPIENT
WhatsApp  → TOOL
```

---

## Multi-Token Entities

Example:

```text
June 15th
```

Current extraction may split the date into separate components.

Desired behavior:

```text
TIME → June 15th
```

as a single semantic entity.

---

## Semantic Context Resolution

Example:

```text
Meet John at the airport
```

Desired interpretation:

```text
ACTION    → meet
RECIPIENT → John
LOCATION  → airport
```

instead of relying only on dependency labels.

---

# Roadmap

## Near Term

* Improve preposition-aware role extraction
* Build a Preposition → Role Mapper
* Improve multi-token entity handling
* Implement RoleFrame generation
* Create intent scoring engine

## Mid Term

* Context memory
* Conversation state tracking
* Intent confidence scoring
* Semantic conflict resolution

## Long Term

* Tool execution system
* Agent architecture
* Multi-step planning
* Fully autonomous assistant workflows

---

# Philosophy

Nova is being built as an educational and experimental project focused on understanding how modern NLP systems work internally.

Rather than relying entirely on large language models, the project aims to explore:

* Linguistic parsing
* Semantic analysis
* Intent inference
* Explainable AI pipelines

Every layer should remain transparent, debuggable and extensible.
