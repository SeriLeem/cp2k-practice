# H₂O Geometry Optimization with CP2K

## Objective

Optimize the geometry of an H₂O molecule using density functional theory (DFT) with CP2K, starting from a manually constructed geometry in Avogadro.

## Starting Geometry

The initial H₂O structure was constructed in Avogadro and its Cartesian coordinates were extracted manually.

The starting coordinates were provided to CP2K in angstroms:

```text
O  -2.3041288853   3.0244705677   0.0000031757
H  -1.3873639895   2.7787770982   0.0409521963
H  -2.7232182837   2.5653969825  -0.7184086120
```

The starting geometry was not optimized beforehand. CP2K was allowed to optimize the structure from this initial configuration.

## Computational Setup

* **Software:** CP2K 2026.2
* **Calculation:** Geometry optimization
* **Electronic structure method:** DFT
* **Exchange-correlation functional:** PBE
* **Basis set:** DZVP-MOLOPT-SR-GTH
* **Pseudopotential:** GTH-PBE
* **SCF guess:** Atomic
* **Geometry optimizer:** BFGS
* **Simulation cell:** 10 × 10 × 10 Å

The complete CP2K input is provided in `h2o.inp`.

## Results

The geometry optimization converged after **6 optimization steps**.

The final optimized structure was written to:

```text
H2O-FINAL-1_6.xyz
```

The optimization trajectory was written to:

```text
H2O-pos-1.xyz
```

The final Cartesian coordinates were:

```text
O  -2.3150585129   3.0559918227   0.0003536779
H  -1.3903232163   2.7635416129   0.0229004841
H  -2.7059245642   2.5497508245  -0.7291991574
```

The changes from the starting geometry are relatively small, demonstrating that the initial Avogadro structure was already reasonably close to the optimized geometry.

## Files

| File                | Description                      |
| ------------------- | -------------------------------- |
| `h2o.inp`           | CP2K input file                  |
| `H2O-FINAL-1_6.xyz` | Final optimized H₂O geometry     |
| `H2O-pos-1.xyz`     | Geometry optimization trajectory |

##

