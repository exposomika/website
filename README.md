# exposomika.io

Reproducible Quarto source and rendered static website for exposomika.

## Edit and preview

The main source is `index.qmd`. Styling lives in `styles.css`, the HTML shell in `template.html`, and the accessible exposure tabs in `site.js`. Original and official artwork lives in `assets/`.

Install [Quarto](https://quarto.org/docs/get-started/) (this site is verified with **1.6.43**). No Node, Python packages, R, or Jupyter kernel are needed to render.

```sh
quarto render
python3 scripts/check_site.py
python3 -m http.server 8765 --directory docs
```

Open <http://localhost:8765>. Rendered HTML and all public assets are in `docs/`; the directory can also be served by any static web host. Always edit the source files, then render again. The hero photograph and official logos are saved locally; the build never needs to download or regenerate them.

## Publish on GitHub Pages

1. Add these files to [`exposomika/website`](https://github.com/exposomika/website), using the `main` branch.
2. Under **Settings → Pages → Build and deployment**, select **GitHub Actions**.
3. Set the custom domain to **exposomika.io** in Pages settings. The repository's `CNAME` file also records it for branch-based publishing.
4. Configure the domain at your DNS provider using [GitHub’s current custom-domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Use the GitHub username or organisation that owns the selected repository; do not use a repository path in the DNS target.
5. Once GitHub validates the DNS and issues a certificate, enable **Enforce HTTPS**.
6. Push to `main`, or run **Build and deploy exposomika** under Actions. The workflow renders with a pinned Quarto version, validates local assets and links, then deploys the `docs/` artifact. Pull requests build and validate without deploying.

Alternatively, the checked-in `docs/` output supports Pages **Deploy from a branch → main → /docs**. Choose one publishing method. For branch deployment, disable the Actions publishing workflow and remember to render and commit `docs/` after edits.

No live deployment or DNS change is implied by these files. A destination repository and access to the domain's DNS are required to connect the site.

Official deployment references: [GitHub custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), [Quarto and GitHub Pages](https://quarto.org/docs/publishing/github-pages.html).

## Content and behaviour

- Contact links open the visitor’s email application at **hello@exposomika.io**. The website does not provision that mailbox.
- Team names, affiliations and the Cyber Valley Batch #9 participation are based on the supplied brief. Research profile links lead to the institutions’ public pages.
- The mortality statement cites the **2016 WHO report**, based on **2012 mortality estimates**, rather than presenting it as a new estimate.
- Exposure descriptions are illustrative educational context. The three-part approach describes the intended direction; it does not claim a deployed or clinically validated product.
- The page uses local assets and system fonts, with no analytics, third-party trackers, form backend or cookies added by this code. The hosting provider handles its own request logs.
- The exposure selector supports mouse, touch, Left/Right, Home/End and screen readers. Without JavaScript, all four descriptions remain visible. Reduced-motion preferences are respected.

See `ASSETS.md` for asset provenance and licences.

## Research experience

The team’s doctoral-research start years were supplied by the founders: **2012** for Manuel and **2019** for Salma. `index.qmd` declares an explicit reference year of **2026**. The bundled-Pandoc Lua filter `filters/research-experience.lua` calculates **14**, **7**, and **21 combined** at render time. These are calendar-year differences, not precise anniversary calculations; no start months were supplied. The reference year is visible on the page. Advance `research-as-of` deliberately when updating the site, then re-render, so historical renders remain reproducible.

The expertise wording describes study design, exposure measurement, and analysis of physiological and behavioural data. It is grounded in the founders’ stated research experience and the [group’s public research programme](https://www.kyb.tuebingen.mpg.de/tscn), with the measurement focus supported by [wearable light-logger field validation](https://arxiv.org/abs/2606.20719). It does not claim clinical validation of an exposomika product.
