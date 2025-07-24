# SpellBuddy

SpellBuddy is a lightweight Python package that suggests correct spellings for misspelled words using edit distance and a BK-tree.

## Features

- Spelling suggestions based on edit distance
- Fast approximate matching using BK-tree
- Interactive CLI demo included

## Quick Start

```bash
# Clone the repo
git clone https://github.com/dizzyfrogs/spellbuddy.git
cd spellbuddy

# Run the interactive demo
python examples/demo.py
```

## Example

```python
from spellbuddy import SpellingSuggester

suggester = SpellingSuggester(["hello", "help", "held", "hero"])
print(suggester.suggest("helo", tolerance=1))
# Output: [('hello', 1)]
```
