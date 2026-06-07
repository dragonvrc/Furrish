# Contributing to Furrish (EN)

We welcome contributions to Furrish! Please read this document carefully before making any contributions.

## Code of Conduct
Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## General Guidelines
- Ensure your contributions align with the mission of Furrish: a cute-feral, accessible language learnable in ~10 minutes, consent-first, and SFW baseline.
- Be respectful and constructive in all interactions.
- Provide clear and concise descriptions for your changes.

## Contribution Process
We use **RFCs** (Request for Comments) for significant changes and a direct pull request process for smaller, more straightforward updates.

### Dictionary Edits
For changes to the dictionary (e.g., adding new words, correcting definitions):
1.  **Fork** the repository.
2.  Edit `/dictionary/core_100.csv` or `/dictionary/core_100.json`. Ensure you maintain the existing schema as defined in `/dictionary/DICTIONARY_SCHEMA.md`.
3.  Open a **Pull Request** with a short, clear rationale for your changes.

### RFC (Grammar / Big Changes)
For significant changes to the grammar, core concepts, or other major aspects of Furrish:
1.  Copy the `/governance/RFC_TEMPLATE.md` to a new file in `/governance/rfcs/RFC-YYYY-NAME.md` (replace YYYY with the current year and NAME with a descriptive title).
2.  Fill out all sections of the RFC template, providing detailed explanations and examples.
3.  Open a **Pull Request** with your RFC. It will undergo a 7-day discussion period and requires a simple majority vote for adoption.

### Adding Examples
- When modifying the Core 100, please add relevant examples (Furrish ↔ EN) to illustrate the usage of the words.

### Stop Word
- The stop word is **painapu**.
