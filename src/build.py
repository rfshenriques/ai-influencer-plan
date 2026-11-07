#!/usr/bin/env python3
import json, shutil, os, re
OUT = '/home/claude/ai-influencer-plan'
data = open('data.json', encoding='utf-8').read().replace('</', '<\\/')
css = open('app.css', encoding='utf-8').read()
js = open('app.js', encoding='utf-8').read()
splash = json.load(open('icons/splash/index.json'))
links = ''.join(
 f'<link rel="apple-touch-startup-image" href="{s["f"]}" media="(device-width:{s["w"]}px) and (device-height:{s["h"]}px) and (-webkit-device-pixel-ratio:{s["r"]}) and (orientation:portrait) and (prefers-color-scheme:{s["mode"]})">\n'
 for s in splash)
html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Persona Plan</title>
<meta name="description" content="AI influencer plan: every persona, niche, language and the full playbook.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Persona Plan">
<meta name="theme-color" content="#F4F1FB" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E0B1D" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
{links}<script>try{{var s=JSON.parse(localStorage.getItem('aiplan.v1')||'{{}}');if(s.theme&&s.theme!=='auto')document.documentElement.setAttribute('data-theme',s.theme)}}catch(e){{}}</script>
<style>{css}</style>
</head>
<body>
<div class="nav-bg"></div>
<header class="top" id="top"></header>
<div id="root"></div>
<nav class="tabbar" id="tabbar" aria-label="Sections"></nav>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<noscript>This app needs JavaScript.</noscript>
<script>window.__DATA__={data};</script>
<script>{js}</script>
</body>
</html>
'''
os.makedirs(OUT, exist_ok=True)
open(f'{OUT}/index.html', 'w', encoding='utf-8').write(html)
files = ['apple-touch-icon.png','icon-192.png','icon-512.png','icon-1024.png','favicon-32.png']
for f in files: shutil.copy(f'icons/{f}', f'{OUT}/{f}')
shutil.rmtree(f'{OUT}/splash', ignore_errors=True)
shutil.copytree('icons/splash', f'{OUT}/splash')
shutil.copy('icons/master.svg', f'{OUT}/icon.svg')
shutil.copy('manifest.webmanifest', f'{OUT}/manifest.webmanifest')
shutil.copy('sw.js', f'{OUT}/sw.js')
shutil.copy('netlify.toml', f'{OUT}/netlify.toml')
os.makedirs(f'{OUT}/src', exist_ok=True)
for f in ['gen.py','bank_common.py','bank_food.py','bank_code.py','bank_design.py','bank_gadget.py','bank_home.py','bank_lang.py','build.py','app.css','app.js','make_icons.js','sw.js','manifest.webmanifest','netlify.toml']:
    shutil.copy(f, f'{OUT}/src/{f}')
shutil.copy('icons/master.svg', f'{OUT}/src/master.svg')
print('built', len(html)//1024, 'KB')
