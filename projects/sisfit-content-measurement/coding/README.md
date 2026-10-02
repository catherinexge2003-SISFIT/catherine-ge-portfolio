# Two-Coder Procedure

## Before coding

Each coder should:

1. read `codebook.md` in full;
2. review the same practice examples;
3. code independently;
4. avoid discussing borderline cases until the reliability file has been saved.

The two coders should not see each other's completed score sheets before reliability is calculated.

## File workflow

Create two files:

- `coding/coder1.csv`
- `coding/coder2.csv`

Use the same columns and content IDs as `coder2_template.csv`.

Run:

```bash
python src/reliability.py --coder1 coding/coder1.csv --coder2 coding/coder2.csv
```

## What counts as a disagreement

A disagreement is any non-identical valid score on the same variable/content pair.

`NA` is excluded pairwise for variables where NA is allowed.

If one coder uses NA and the other uses a score, record that mismatch separately during adjudication because it usually indicates a definition problem.

## Reliability sequence

1. save the raw independent files;
2. calculate reliability;
3. archive the reliability output;
4. identify variables below the project threshold;
5. discuss disagreements;
6. revise codebook wording if needed;
7. if definitions materially change, code a fresh reliability set.

Do not overwrite the original independent coding files after adjudication.
