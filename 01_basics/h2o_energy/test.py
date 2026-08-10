with open("H2O_POTENTIAL.inp", "r") as file:
    content = file.read()
    lines = content.splitlines()

for i in range(len(lines)):
    parts = lines[i].split()

    if len(parts) > 0 and parts[0] == "H":
        x = float(parts[1])

        if x == 1.2:
            x -= 0.1
            parts[1] = f"{x:.1f}"
            lines[i] = " ".join(parts)
            content = "\n".join(lines)
            print(content)
            break

with open("H2O_POTENTIAL.inp", "w") as file:
    file.write(content)
