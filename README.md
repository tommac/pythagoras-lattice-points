# Pythagoras' theorem by counting lattice points

**Tom Maciejewski** · Preprint, 2026 · [Read the paper (PDF)](paper.pdf)

## Abstract

For a right triangle with integer legs $a,b$, Pick's theorem measures the square on the hypotenuse by counting the lattice points in it, and the count comes to $a^2+b^2$. The idea is classroom folklore. We write the argument out in full, extend it to all right triangles by a limit, and say what it really is: the oldest dissection proof of the theorem, expressed in lattice points. We also locate the geometry. The counts cannot see lengths at all; the Euclidean content lies entirely in the fact that a square has the same area in every position.

## Contents

| File | What it is |
|---|---|
| [`paper.pdf`](paper.pdf) | The paper (5 pages) |
| [`paper.tex`](paper.tex) | Its LaTeX source |
| [`anc/verify.py`](anc/verify.py) | Exact check of the lattice-point counts for all legs up to 30. Python standard library only; a few seconds. |
| [`anc/verification-output.txt`](anc/verification-output.txt) | What the scripts printed when this version was built |

## Checking the computations

```bash
python3 anc/verify.py
```

## Citing this paper

```bibtex
@misc{maciejewski2026pick,
  author = {Maciejewski, Tom},
  title  = {Pythagoras' theorem by counting lattice points},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/tommac/pythagoras-lattice-points},
}
```

## Status

This is a preprint and has not been peer reviewed. If you find an error, please open an issue.

## License

The paper is licensed under [CC BY 4.0](LICENSE). The code in `anc/` is under the [MIT License](LICENSE-CODE).
