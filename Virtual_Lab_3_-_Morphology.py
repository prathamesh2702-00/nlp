    # Assignment 12: Virtual Lab 3 - Morphology

print("----- Virtual Lab 3 : Morphology -----\n")

# Sample Hindi words for morphological analysis
words = ["लड़का", "लड़के", "लड़कियाँ", "किताब", "किताबें"]

print("Input Hindi Words:\n")
print(words)

print("\nMorphological Analysis using Add-Delete Table:\n")

for word in words:
    print(f"Word: {word}")

    # Simple Add-Delete Table logic
    if word.endswith("का"):
        root = word[:-2]
        suffix = "का"
        category = "Singular Masculine Noun"

    elif word.endswith("के"):
        root = word[:-2]
        suffix = "के"
        category = "Plural Masculine Noun"

    elif word.endswith("याँ"):
        root = word[:-3]
        suffix = "याँ"
        category = "Plural Feminine Noun"

    elif word.endswith("ें"):
        root = word[:-2]
        suffix = "ें"
        category = "Plural Feminine Noun"

    else:
        root = word
        suffix = "None"
        category = "Base Form"

    print(f"Root Word : {root}")
    print(f"Suffix    : {suffix}")
    print(f"Category  : {category}")
    print("----------------------------")