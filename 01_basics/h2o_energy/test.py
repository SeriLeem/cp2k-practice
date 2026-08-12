import glob
import subprocess

with open("H2O_POTENTIAL.inp", "r") as file:
    content = file.read()

original_content = content

n = 1.2

while n > 0.5:

    lines = original_content.splitlines()

    for i in range(len(lines)):
        parts = lines[i].split()

        if len(parts) > 0 and parts[0] == "H":
            parts[1] = f"{n:.1f}"
            lines[i] = " ".join(parts)
            content = "\n".join(lines)
            break

    with open("H2O_POTENTIAL" + f"{n:.1f}"  + ".inp", "w") as file:
        file.write(content)

    n -= 0.1


files = glob.glob("H2O_POTENTIAL*.inp")
print(files)

for file in files:
    outfile = file.replace(".inp", ".out")
    subprocess.run([
        "cp2k.psmp",
        "-i",
        file,
        "-o",
        outfile
    ])

energy = []

n = 1.2

while n > 0.5:

    filename = "H2O_POTENTIAL" + f"{n:.1f}" + ".out"

    with open(filename, "r") as file:
        content = file.read()

    for l in content.splitlines():
        if "ENERGY| Total FORCE_EVAL" in l:
            a = l.split("]")
            energy.append(float(a[1].strip()))
            break

    n -= 0.1

n=1.2
k=0
f=[]
plot=[]
while k<7:
    f=[n,energy[k]]
    plot.append([round(n, 1), energy[k]])    
    k+=1
    n-=0.1

import matplotlib.pyplot as plt

x = [p[0] for p in plot]
y = [p[1] for p in plot]

plt.plot(x, y, marker="o")
plt.xlabel("O-H distance (Å)")
plt.ylabel("Energy (Hartree)")
plt.title("H2O Potential Energy Curve")
plt.show()
