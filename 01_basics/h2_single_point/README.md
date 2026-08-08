# H₂ Single-Point Energy

## Objective

Perform a single-point DFT energy calculation for an H₂ molecule using CP2K.

## Method

- **Software:** CP2K
- **Method:** Quickstep / DFT
- **Exchange-correlation functional:** PBE
- **Basis set:** DZVP-MOLOPT-SR-GTH
- **Pseudopotential:** GTH-PBE
- **SCF initial guess:** ATOMIC
- **H–H distance:** 0.74 Å
- **Simulation cell:** 10 × 10 × 10 Å

## Results

- **Total energy:** −1.161618312391510 Ha
- **SCF convergence:** 8 steps
- **Warnings:** 0
- **Calculation status:** Completed successfully

## Files

- `h2.inp` — CP2K input file
- `h2.out` — CP2K output file

## Notes

This calculation was performed as an introductory CP2K practice exercise to become familiar with CP2K input structure, DFT calculations, and SCF convergence.
