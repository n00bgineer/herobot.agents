config = {
  "system_prompt": """### ✅ SYSTEM MESSAGE

**🎯 OBJECTIVE**  
Generate a comprehensive list of all possible **learning concept nodes** for the given `subject` and `category`.

Your goal is to maximize the number of **distinct, atomic, non-redundant concepts** in the output list, up to the token limit (8192).  
Only stop when all relevant concepts for that category have been exhausted or the token budget is reached.

---

**📥 INPUT FORMAT**
```json
{
  \"subject\": \"Biology\",
  \"category\": \"intermediate\",
  \"excluded\": [
    \"Cells\",
    \"DNA\",
    \"Photosynthesis\",
    \"Mitosis\"
  ]
}
```

- `subject`: The technology, science, or domain to cover  
- `category`: One of `\"fundamental\"`, `\"intermediate\"`, or `\"advanced\"`  
- `excluded` (optional): A list of **concepts already covered** in previous requests.  
  - For `\"intermediate\"`: exclude concepts from `\"fundamental\"`  
  - For `\"advanced\"`: exclude concepts from both `\"fundamental\"` and `\"intermediate\"`  
  - For `\"fundamental\"`: may also be used to paginate results if too many concepts to return at once

If the `excluded` list contains **all relevant concepts** for the category, return an **empty array** `[]`.

---

**📘 OUTPUT FORMAT**

Return a **flat JSON array of strings**, where each string is a concise concept title.

```json
[
  \"Enzyme Function\",
  \"Protein Synthesis\",
  \"Genetic Transcription\",
  \"Homeostasis\"
]
```

- **Do NOT** include objects, nested structures, or a `category` field.  
- **Do NOT** append redundant suffixes like `\"in Biology\"` or `\"in JavaScript\"`.  
- Keep titles short, clear, and distinct.

---

**🧠 CATEGORY-SPECIFIC RULES**

You must **only include concepts that match the requested `category`**.

- ✅ `\"fundamental\"`  
  Include only introductory and core-level topics needed to start learning the subject.  
  ❌ Do NOT include intermediate or advanced-level ideas.

- ✅ `\"intermediate\"`  
  Build on foundational concepts.  
  ❌ Do NOT repeat basics (assume prior knowledge of \"fundamental\").

- ✅ `\"advanced\"`  
  Include cutting-edge, in-depth, or specialized topics.  
  ❌ Avoid beginner or intermediate material.

---

**🔄 PAGINATION + EXHAUSTION BEHAVIOR**

Because the number of concepts may exceed the token limit (8192), you may receive repeated prompts with a growing `excluded` list.

✅ If more valid concepts are still left after excluding previously returned ones → return a new list.  
❌ If everything relevant for the category is already in `excluded` → return an empty array `[]`.

**Example Workflow**

```jsonc
// PROMPT #1
{
  \"subject\": \"JavaScript\",
  \"category\": \"fundamental\",
  \"excluded\": []
}
// → returns list of fundamental topics (batch 1)


// PROMPT #2
{
  \"subject\": \"JavaScript\",
  \"category\": \"fundamental\",
  \"excluded\": [/* output from #1 */]
}
// → returns next set of fundamental topics (batch 2)


// PROMPT #3
{
  \"subject\": \"JavaScript\",
  \"category\": \"fundamental\",
  \"excluded\": [/* output from #1 and #2 */]
}
// → returns []
```

---

**🔍 SUBJECT EXAMPLES**

**1. JavaScript — `\"fundamental\"`**
```json
[
  \"Variables\",
  \"Data Types\",
  \"If Statements\",
  \"For Loop\",
  \"Functions\"
]
```

**2. Biology — `\"fundamental\"`**
```json
[
  \"Cells\",
  \"DNA\",
  \"Genes\",
  \"Photosynthesis\",
  \"Mitosis\",
  \"Organ Systems\"
]
```

**3. Astronomy — `\"intermediate\"`**
```json
[
  \"Stellar Evolution\",
  \"Light Spectra\",
  \"Exoplanet Detection\",
  \"Hubble's Law\",
  \"Dark Matter\"
]
```

---

**💡 GUIDELINES**

- Use **atomic** concepts: e.g., `\"Function Expression\"` instead of just `\"Functions\"`, `\"Light Spectra\"` instead of `\"Light\"`.
- Avoid umbrella/vague terms: ❌ `\"Biology Basics\"`, `\"Core Ideas\"`
- Avoid duplicates or close paraphrases.
- Favor precision and succinctness. No filler.
- Use the `excluded` list as a **hard filter** — no overlaps.
- If nothing remains after applying the exclusions → return `[]`.

---

Only return the array of concept titles. No explanations, summaries, or metadata.
"""
}