# Assignment 11: Virtual Lab 2 - Word Generation

print("----- Virtual Lab 2 : Word Generation -----\n")

# Sample root words and suffix rules
root_words = ["play", "read", "write", "run", "teach"]

# Simple morphological generation using suffixes
suffixes = ["ing", "ed", "er", "s"]

print("Root Words:\n")
print(root_words)

print("\nGenerated Words:\n")

for word in root_words:
    print(f"Base Word: {word}")

    for suffix in suffixes:
        # Basic word generation logic
        if word.endswith("e") and suffix == "ing":
            generated_word = word[:-1] + "ing"
        elif word == "run" and suffix == "ing":
            generated_word = "running"
        else:
            generated_word = word + suffix

        print(f"{word} + {suffix} = {generated_word}")

    print("----------------------------")