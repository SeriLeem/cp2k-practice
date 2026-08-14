import math

filename = "H2O_POTENTIAL-FINAL-1_9.xyz"

with open(filename, "r") as file:
    lines = file.readlines()

O = None
H = []

for line in lines[2:]:
    parts = line.split()

    if len(parts) >= 4:
        element = parts[0]
        coordinates = [
            float(parts[1]),
            float(parts[2]),
            float(parts[3])
        ]

        if element == "O":
            O = coordinates
        elif element == "H":
            H.append(coordinates)


def distance(A, B):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(A, B)))


def angle(A, B, C):
    BA = [a - b for a, b in zip(A, B)]
    BC = [c - b for c, b in zip(C, B)]

    dot_product = sum(a * c for a, c in zip(BA, BC))

    length_BA = math.sqrt(sum(a ** 2 for a in BA))
    length_BC = math.sqrt(sum(c ** 2 for c in BC))

    radians = math.acos(
        dot_product / (length_BA * length_BC)
    )

    return math.degrees(radians)


for i, hydrogen in enumerate(H):
    print(f"O-H{i+1} distance:", distance(O, hydrogen), "Å")

print("H-O-H angle:", angle(H[0], O, H[1]), "degrees")
