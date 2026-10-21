import glob
import os
import re

files = [os.path.basename(f)[:-3] for f in glob.glob("*.md")]
print("Existing files count:", len(files))

with open("00 - Índice Ciência de Dados.md", "r", encoding="utf-8") as f:
    idx_content = f.read()

links = re.findall(r"\[\[(.*?)\]\]", idx_content)
missing_in_index = set()
for l in links:
    target = l.split("|")[0].split("#")[0].strip()
    if target and target not in files:
        missing_in_index.add(target)

print("Missing targets from index:")
for m in sorted(missing_in_index):
    print(" -", m)

# Also check across ALL markdown files
all_missing = {}
for md in glob.glob("*.md"):
    with open(md, "r", encoding="utf-8") as f:
        c = f.read()
    file_links = re.findall(r"\[\[(.*?)\]\]", c)
    for l in file_links:
        target = l.split("|")[0].split("#")[0].strip()
        if target and target not in files:
            all_missing.setdefault(target, []).append(os.path.basename(md))

print("\nMissing targets across ALL markdown files:")
for m in sorted(all_missing.keys()):
    print(f" - {m} (referenced in: {', '.join(set(all_missing[m]))})")
