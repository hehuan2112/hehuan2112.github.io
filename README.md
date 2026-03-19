# Huan He's Online CV

Personal website at [hehuan2112.github.io](https://hehuan2112.github.io/).

## Tech Stack

- **Bun** — package manager & runtime
- **Vue 3** — UI framework (Composition API)
- **Vite** — build tool
- **marked** — Markdown rendering

All content is stored as JSON files in `content/`. No database, no backend.

## Development

```bash
bun install       # install dependencies
bun run dev       # start dev server (http://localhost:5173)
bun run build     # production build → dist/
bun run preview   # preview the production build
```

## Updating Content

All data lives in `content/`. Edit the relevant JSON file and push — the CI will rebuild automatically.

| File | Content |
|---|---|
| `content/works.json` | Name, email, institution, about bio |
| `content/works.news.json` | News items (supports Markdown) |
| `content/works.publications.json` | Publications |
| `content/works.projects.json` | Projects |
| `content/works.tools.json` | Tools |
| `content/works.patents.json` | Patents |
| `content/works.work_exp.json` | Work experience |
| `content/works.academic_exp.json` | Community services |
| `content/works.awards.json` | Awards |

Paper files and thumbnails go in `content/file/<venue>/`.

**Adding a publication:**
```json
{
    "thumb": "<venue>/<name>-thumb.jpg",
    "title": "",
    "authors": "",
    "date": "Nov, 2025",
    "source": "",
    "type": "journal",
    "links": [
        ["12345678", "https://pubmed.ncbi.nlm.nih.gov/12345678/", "pmid"],
        ["10.xxx/yyy", "https://doi.org/10.xxx/yyy", "doi"]
    ]
}
```

## Deployment

Push to `master` triggers the GitHub Actions workflow (`.github/workflows/deploy.yml`):

1. Bun installs dependencies
2. Vite builds to `dist/`
3. Deployed to GitHub Pages via `actions/deploy-pages`

**Required one-time setup:** In repo **Settings → Pages → Source**, select **"GitHub Actions"** (not "Deploy from a branch").

## Project Structure

```
src/
├── App.vue
├── components/       # one component per section
├── data/index.js     # imports all JSON files
└── utils/markdown.js # md rendering, citation formatting, author highlighting

content/              # all JSON data + paper files/thumbnails
public/
├── file -> ../content/file   (symlink)
└── img  -> ../themes/hh-theme/static/img  (symlink)
```

---

## Archive: Previous Stack (pre-2025)

The site was originally built with [Pelican](https://getpelican.com/) (Python static site generator) using a custom Jinja2 theme (`themes/hh-theme/`). Deployment used `nelsonjchen/gh-pages-pelican-action` to build and push to the `gh-pages` branch. The Pelican setup is preserved in the repository for reference but is no longer active.
