# CLAUDE.md

## Project Overview

Personal website and blog for Vasco Yasenov, built with [Quarto](https://quarto.org/) and hosted via GitHub Pages.

- **Site URL:** https://vyasenov.github.io/
- **Output directory:** `docs/` (rendered HTML served by GitHub Pages)
- **Branch:** `main` (single-branch workflow; pushes to `main` deploy the site)

## Project Structure

- `_quarto.yml` — site-wide Quarto config (navbar, theme, footer, Google Analytics)
- `blog/` — blog posts as `.qmd` files; each post is self-contained
- `blog/_metadata.yml` — shared blog metadata (giscus comments, share buttons, Lua filter)
- `blog/_sharebuttons.md` — ShareThis share buttons inserted before each post
- `_drafts/` — draft posts not included in the rendered site
- `code/` — CSS, JS, and Lua assets (`styles.css`, `open-links-new-tab.js`, `back-to-top.js`, `random-article.js`, `code-insertion.lua`)
- `docs/` — rendered output (do not edit by hand)
- `files/` — static assets (PDFs, images, etc.)
- Top-level `.qmd` pages: `index.qmd`, `about.qmd`, `cv.qmd`, `research.qmd`, `software.qmd`, `mind-map.qmd`, `childrenbook.qmd`

## Common Commands

```bash
# Preview the site locally
quarto preview

# Render the full site (output goes to docs/)
quarto render

# Render a single post
quarto render blog/some-post.qmd
```

## Blog Post Conventions

- Each blog post is a `.qmd` file in `blog/`.
- Posts use YAML front matter for title, date, categories, description, and image.
- The Lua filter `code/code-insertion.lua` handles custom code block insertion.
- Giscus comments are enabled site-wide for blog posts via `blog/_metadata.yml`.
- To draft a post, place it in `_drafts/` instead of `blog/`.

## Themes and Styling

- Light theme: `cosmo` / Dark theme: `cyborg`
- Custom CSS in `code/styles.css`
- Fonts: Fira Code, Source Code Pro (loaded from Google Fonts)

## Key Notes

- The `docs/` directory is committed and serves as the GitHub Pages source. After running `quarto render`, the changes in `docs/` should be committed alongside source changes.
- Do not edit files inside `docs/` directly — always edit the source `.qmd` files and re-render.
