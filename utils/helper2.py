import re


with open("input.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Step 1: Remove leading/trailing spaces for each line
lines = [line.strip() for line in raw_text.splitlines()]

# Step 2: Remove empty lines
lines = [line for line in lines if line]

# Step 3: Add group="5" before "/>" if not already there
lines = [re.sub(r'\s*/>', ' group="5"/>', line) for line in lines]

# Step 4: Join with a blank line between each entry
cleaned_text = "\n\n".join(lines)

# Save to output file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Done! Cleaned file saved to output.txt")