---
name: blog-article
description: Draft a new blog article for Vasco Yasenov's blog "Advanced Topics in Statistical Data Science" (https://vyasenov.github.io/blog). Takes a topic, optional paper references, and optional rough notes, then produces a full .qmd draft in blog/ that follows the site's conventions (Background → Notation → A Closer Look → Bottom Line → Where to Learn More → References), with R/Python code tabs and LaTeX math. Use when the user asks to write, draft, or start a new blog post, blog article, or .qmd post for this blog. After writing, adds today's date to the YAML front matter and runs `quarto render` + `quarto preview`.
---

# Blog Article Drafter

Drafts a new article for the "Advanced Topics in Statistical Data Science" blog, matching the author's voice, structure, and code conventions.

## Inputs to gather from the user

Before writing, make sure you have:

1. **Topic** (required) — the subject of the article.
2. **Topic-specific notes** (optional) — e.g. "flavors of" survey, "skip the code", "focus on asymptotics", "emphasize causal angle", target length, etc.
3. **Paper(s) / references** (optional) — arXiv links, PDFs, or citations the user wants drawn on. Fetch them if given URLs.
4. **Rough notes** (optional) — bullet points, outlines, or ideas the user already has.

If the user's initial prompt doesn't include some of these, ask once in a single short message. Do not pepper them with follow-ups.

## About the author and blog (context for voice)

- Staff Data Scientist at Adobe; postdocs at UC Berkeley and Stanford; PhD in Economics. Work sits at the intersection of causal inference, machine learning, and applied econometrics.
- The blog translates current and past academic research into practical guidance for advanced data scientists. Audience is technically sophisticated — comfortable with math and code — but practitioners, not theorists. Goal: practical relevance without sacrificing rigor.
- Consistent structure and voice across all posts.

## Target audience

Advanced data scientists and applied statisticians who:
- Are comfortable with mathematical notation and statistical theory.
- Want to understand *why* methods work, not just *how* to use them.
- Care about assumptions and where they break down.
- Work in industry or applied research settings.

## Required article structure (follow exactly)

1. **Background** — motivate the topic. Why does it matter? What problem does it solve? Hook the reader with an intuition or a common misconception. 1–3 paragraphs.
2. **Notation** — define the mathematical setup clearly and concisely. LaTeX math (`$Y = X\beta + \varepsilon$`). Introduce all symbols before using them.
3. **A Closer Look** — main body. 3–6 subsections depending on the topic. Cover key ideas, methods, variants. Include formal definitions where appropriate. Explain practical implications of theoretical results. Call out common pitfalls.
4. **Bottom Line** — 3–5 bullet points summarizing takeaways for a practitioner. Concise and opinionated.
5. **Where to Learn More** — 1 short paragraph pointing to 2–4 canonical references (textbooks, seminal papers). Mention by author/title with brief characterization.
6. **References** — full citations in a consistent academic format (Author, Year, Title, Journal/Publisher).

## Writing style

- Clear, precise, confident voice. Use **first-person singular** ("I") for author voice — "I will walk through", "I describe", "In practice, I…". Avoid first-person plural for author voice (do not write "we will show", "we'll explore", "we conclude"). Inclusive/pedagogical "we" is fine where the reader is part of the action ("let's consider", "we can see", "suppose we have a sample"), as is the math convention ("we have", "we obtain") inside derivations.
- Mathematically rigorous but never pedantic. Every equation should serve the narrative.
- Acknowledge limitations, edge cases, and where theoretical guarantees don't translate to practice.
- Do not oversimplify or talk down. Do not pile on caveats or hedging.
- Avoid bullet-heavy prose in the body — use paragraphs. Reserve bullets for the Bottom Line section.
- Direct and grounded tone, not breathless or promotional.

## Code conventions

- Include R and Python code blocks where relevant (especially for "flavors of" surveys and applied methods). Organize them in R/Python tabs using this pattern:

```
::::{.panel-tabset}

### R
​```r
set.seed(1988)
# ...
​```

### Python
​```python
import numpy as np
np.random.seed(1988)
# ...
​```
::::
```

- Always seed with `1988` (`set.seed(1988)` in R, `np.random.seed(1988)` in Python).
- Self-contained, well-commented, runnable code. Realistic variable names.
- Name all libraries explicitly. For niche packages, note what to install.

## Length

Roughly 800–1800 words of prose (not counting code), calibrated to topic complexity. "Flavors of" survey pieces can be longer.

## File conventions

- Write to `blog/<slug>.qmd` (not `_drafts/`) so the user can preview it live. The user will move the file to `_drafts/` themselves if they don't want to publish it.
- Slug: lowercase, hyphenated, short (2–5 words). Check existing `blog/` filenames to avoid collisions and to match naming style (e.g. `bootstrap-limitations.qmd`, `flavors-bootstrap.qmd`, `ci-residualized-reg.qmd`).
- Front matter template (use today's date from the environment — format `YYYY-MM-DD`):

```yaml
---
title: "Title Case Title"
date: "YYYY-MM-DD"
categories: [topic1, topic2, topic3]
---
```

- Categories: 2–4 lowercase tags. Reuse existing categories where possible — check a few existing posts in `blog/` to match.
- Use `## Background`, `## Notation`, `## A Closer Look` (with `###` subsections), `## Bottom Line`, `## Where to Learn More`, `## References` as the top-level headings. Separate major subsections in "A Closer Look" with `---` horizontal rules, matching the site's style.
- For highlighted algorithm boxes, use:

```
::: {.callout-note title="Algorithm:"}
...
:::
```

## Workflow

1. **Gather inputs** — topic, notes, papers, rough notes. Ask once if missing.
2. **Skim a couple existing posts** in `blog/` (e.g. `flavors-bootstrap.qmd`, one non-flavors post) to match voice and formatting exactly. Do this only if you haven't in the current session.
3. **If papers/URLs were provided**, fetch their content (WebFetch) so citations and claims are grounded.
4. **Write the draft** at `blog/<slug>.qmd` with today's date (pull from environment, not a guess).
5. **Render** the site: `quarto render blog/<slug>.qmd` first to catch errors on the new file; if clean, optionally `quarto render` the full site.
6. **Preview**: launch `quarto preview` in the background so the user can see it. Report the URL/port when it's up.
7. **Tell the user** the file path, the word count, and the preview URL.

## What not to do

- Don't write to `_drafts/` — Quarto skips `_`-prefixed directories, so preview won't show the article. The user moves files to `_drafts/` themselves when un-publishing.
- Don't invent citations. If a claim needs a reference and none was provided, either (a) cite a canonical textbook the author has used before (check References sections of existing posts), or (b) rephrase to avoid the unsupported claim.
- Don't add emojis.
- Don't ship placeholder code. If code is included, it must run.
- Don't overwrite an existing `blog/<slug>.qmd` without confirming.
