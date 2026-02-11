# Sources

Original SEBI-published PDFs that this repository's structured extractions are derived from. Committed to git so the repo is self-contained.

## Structure

```
sources/
├── circulars/             # Original SEBI circulars, unmodified
│   └── 2024-08-20_CSCRF-for-SEBI-REs.pdf
└── refs/                  # Logically extracted segments from circulars
    ├── meta/              # Topic-level reference files
    │   ├── abbreviations.pdf
    │   ├── committee.pdf
    │   ├── compliance.pdf
    │   ├── definitions.pdf
    │   └── exemptions.pdf
    └── framework/         # Function-level guidelines & standards
        ├── governance.guidelines.pdf
        ├── governance.standards.pdf
        ├── identify.guidelines.pdf
        ├── identify.standards.pdf
        ├── protect.guidelines.pdf
        ├── protect.standards.pdf
        ├── detect.guidelines.pdf
        ├── detect.standards.pdf
        ├── respond.guidelines.pdf
        ├── respond.standards.pdf
        ├── recover.guidelines.pdf
        ├── recover.standards.pdf
        ├── evolve.guidelines.pdf
        └── evolve.standards.pdf
```

## Naming Convention

Circulars use dated slugs: `YYYY-MM-DD_short-slug.pdf`

Reference PDFs use descriptive names matching the CSCRF function or topic they cover.

## Adding a New Circular

1. Place the unmodified PDF in `circulars/` using the `YYYY-MM-DD_short-slug.pdf` convention (date = SEBI publication date).
2. If extracting function-level reference segments, add them under `refs/framework/` using the `{function}.guidelines.pdf` and `{function}.standards.pdf` naming convention.
3. Any topic-level reference files (definitions, compliance, etc.) go under `refs/meta/`.
