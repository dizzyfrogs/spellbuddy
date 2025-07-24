import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from spellbuddy.suggester import SpellingSuggester

def load_wordlist(path="data/wordlist.txt"):
    """Load words from a text file, one word per line."""
    try:
        with open(path, encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
            print(f"Loaded {len(words)} words from {path}")
            return words
    except FileNotFoundError:
        print(f"Warning: {path} not found. Using fallback word list.")
        return ["hello", "help", "held", "helmet", "shell", "hero", "hell"]

def main():
    word_list = load_wordlist()
    suggester = SpellingSuggester(word_list)

    print("\nSpellBuddy - Type a word and get spelling suggestions! (type 'quit' or Ctrl+C to exit)\n")

    while True:
        try:
            word = input("Enter a word: ").strip()
            if word.lower() == "quit":
                print("Goodbye!")
                break

            suggestions = suggester.suggest(word, tolerance=2)

            if suggestions:
                print("Did you mean:")
                for w, dist in suggestions:
                    print(f"  - {w} (distance {dist})")
            else:
                print("No suggestions found.")
            print()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
