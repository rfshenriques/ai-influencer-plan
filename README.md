# Persona Plan

An installable web app (PWA) for reviewing the AI influencer plan: 128 personas across 7 niches and 11 languages, plus the full playbook (hooks, selling, platform descriptions, rules, launch waves).

- Browse by persona, niche or language; every persona has Overview, Look and voice, Content, Sell, Rules, Prompts and a Checklist.
- Mark personas Approved / Skipped, tick checklists and write notes. These are saved on the device only.
- Works offline after the first load.

## Deploy on Netlify

Import this repo. No build command is needed; the publish directory is the repo root (set in `netlify.toml`).

## Rebuild after editing

Sources live in `src/`. From a working copy:

```
cd src && python3 gen.py && python3 build.py
```

`build.py` writes `index.html` to the repo root (edit the `OUT` path at the top for your machine). On iPhone: open the site in Safari, Share, Add to Home Screen.

## Notes

Rules and platform policies in the plan were checked on 5 Nov 2026 from web sources. They are not legal advice; verify before launch.
