#!/usr/bin/env python3
"""Generates data.json: markets, niches, personas, plan pages."""
import json
import research as RS
import bank_glam, bank_food, bank_shred, bank_code, bank_design, bank_gadget, bank_home, bank_lang

# ---------------------------------------------------------------- markets
M = [
 dict(id='us', name='English (US)', short='EN-US', lang='English', city='Chicago', cur='$', rate=1, climate='cold',
  accent='general American accent', speech='General American, casual',
  watch='British spellings, units and slang; use miles, Fahrenheit, dollars',
  fillers='"okay so", "honestly", "literally", "kind of"',
  local=['Corner coffee shops and bagel places', 'Subway (the L) and street parking', 'Big-box and drugstore chains'],
  dish='chicken burrito bowl with black beans',
  ai='FTC endorsement guides cover virtual influencers. Paid or affiliate links need a clear disclosure, and the source advises also saying the influencer is virtual, inside the video.',
  bet=('verify', 'US betting promotion is state by state and was not verified. Check each state and get legal advice before any betting persona. Show 21+ and a responsible-gambling message.'),
  ph=('Hi', '(hy)', 'Thank you', '(thank yoo)', 'Where is the station?', '(wair iz the STAY-shun)', 'Hola', 'Gracias', '¿Dónde está la estación?')),
 dict(id='uk', name='English (UK)', short='EN-UK', lang='English', city='Manchester', cur='£', rate=0.8, climate='cold',
  accent='neutral British accent with a light northern touch', speech='Neutral British, no caricature',
  watch='American vocabulary, units and dates; use pounds, miles, DD/MM dates',
  fillers='"right, so", "to be fair", "proper", "a bit"',
  local=['Tesco-style supermarkets and corner shops', 'Trams, buses and rail passes', 'Drizzly weather and umbrellas'],
  dish='sausage and bean traybake with roasted veg',
  ai='UK AI-labelling rules were not researched; check advertising rules for sponsored posts and label the persona as AI.',
  bet=('ok', 'UK: affiliates can generally promote locally licensed brands under strict content, timing and placement rules. Verify the current rules before launch.'),
  ph=('Hi', '(hy)', 'Thank you', '(thank yoo)', 'Where is the station?', '(wair iz the STAY-shun)', 'Hola', 'Gracias', '¿Dónde está la estación?')),
 dict(id='es', name='Spanish (Latin America)', short='ES-LATAM', lang='Spanish', city='Mexico City', cur='US$', rate=1, climate='warm',
  accent='neutral Latin American Spanish accent', speech='Neutral Latin American, informal "tú"; pick one target country for slang',
  watch='Spain-only words, "vosotros", and Argentine "vos" if aiming elsewhere',
  fillers='"o sea", "la neta"-style local slang only if the target country is fixed, "entonces", "ahorita"',
  local=['Tianguis markets and corner tiendas', 'Metro and ride-hailing apps', 'Warm sunshine with afternoon rain'],
  dish='light chicken tinga bowl with beans and avocado',
  ai='Latin American rules were not researched; label the persona as AI and check each country.',
  bet=('verify', 'Latin American betting promotion varies by country and was not verified. Pick one country and check its regulator before any betting persona.'),
  ph=('Hola', '(OH-lah)', 'Gracias', '(GRAH-see-ahs)', '¿Dónde está la estación?', '(DOHN-deh ehs-TAH lah ehs-tah-SYOHN)', 'Hola', 'Gracias', '¿Dónde está la estación?')),
 dict(id='br', name='Portuguese (Brazil)', short='PT-BR', lang='Portuguese (Brazil)', city='São Paulo', cur='R$', rate=5.5, climate='warm',
  accent='São Paulo Brazilian Portuguese accent', speech='"você", "a gente", casual Brazilian',
  watch='European Portuguese vocabulary and accent',
  fillers='"tipo", "né", "então", "mano"',
  local=['Padarias and feira markets', 'Metro, buses and ride-hailing apps', 'Marmita lunchboxes and weekend churrasco'],
  dish='marmita with rice, beans and grilled chicken',
  ai='Brazilian rules were not researched; label the persona as AI and check the current advertising rules.',
  bet=('verify', 'Brazil regulates betting and its advertising, but this was not verified here. Check the current rules with a lawyer before any betting persona.'),
  ph=('Oi', '(oy)', 'Obrigado / Obrigada', '(oh-bree-GAH-doo / -dah)', 'Onde fica a estação?', '(ON-jee FEE-kah ah ehs-tah-SOWN)', 'Hi', 'Thank you', 'Where is the station?')),
 dict(id='pt', name='Portuguese (Portugal)', short='PT-PT', lang='Portuguese (Portugal)', city='Porto', cur='€', rate=0.92, climate='mild',
  accent='European Portuguese accent from the north', speech='European Portuguese, informal "tu", European vocabulary',
  watch='Brazilian words, "você" overuse and Brazilian accent',
  fillers='"pá", "então", "tipo", "pronto"',
  local=['Pastelarias and neighbourhood markets', 'Metro and CP trains', 'Mild, damp winters'],
  dish='light bacalhau with chickpeas and greens',
  ai='EU: AI Act Article 50 applies from 2 August 2026; tool providers must mark AI output, and tools already on the market get until 2 December 2026. Label the persona as AI anyway.',
  bet=('verify', 'Portuguese betting promotion rules were not verified. Check the regulator (SRIJ) and get legal advice before any betting persona.'),
  ph=('Olá', '(oh-LAH)', 'Obrigado / Obrigada', '(oh-bree-GAH-doo / -dah)', 'Onde fica a estação?', '(ON-deh FEE-kah ah shtah-SOWN)', 'Hi', 'Thank you', 'Where is the station?')),
 dict(id='fr', name='French', short='FR', lang='French', city='Lyon', cur='€', rate=0.92, climate='cold',
  accent='standard metropolitan French accent', speech='Standard metropolitan French, informal "tu", relaxed spoken contractions',
  watch='Stiff written French, and Canadian or Belgian vocabulary',
  fillers='"du coup", "genre", "franchement", "en fait"',
  local=['Boulangeries and Sunday markets', 'Métro, tram and TGV', 'Supermarkets like Carrefour-style hypermarkets'],
  dish='ratatouille with chicken and quinoa',
  ai='France: the 2023 influencer law requires "Publicité" or "Collaboration commerciale" on sponsored posts and "Image virtuelle" on AI-generated posts. Influencers and advertisers share liability, and influencers answer for dropshipped products.',
  bet=('no', 'France: since the law of 9 June 2023 influencers may not promote paid sports-tip subscriptions, and tip services cannot be presented as improving the chance of winning. No betting persona in France.'),
  ph=('Bonjour', '(bohn-ZHOOR)', 'Merci', '(mehr-SEE)', 'Où est la gare ?', '(oo eh lah GAHR)', 'Hi', 'Thank you', 'Where is the station?')),
 dict(id='it', name='Italian', short='IT', lang='Italian', city='Milan', cur='€', rate=0.92, climate='cold',
  accent='standard neutral Italian accent', speech='Standard neutral Italian, informal',
  watch='Stiff, translated phrasing',
  fillers='"dai", "cioè", "allora", "praticamente"',
  local=['Bars with espresso at the counter', 'Metro, trams and Trenitalia', 'Weekly local markets'],
  dish='pasta e fagioli, lighter version with vegetables',
  ai='EU: AI Act Article 50 applies from 2 August 2026; tools already on the market get until 2 December 2026 for the marking duty. Label the persona as AI.',
  bet=('no', 'Italy: near-total ban; influencer ads and affiliate marketing for betting are prohibited. No betting persona in Italy.'),
  ph=('Ciao', '(CHOW)', 'Grazie', '(GRAHT-see-eh)', "Dov'è la stazione?", '(doh-VEH lah stah-TSYOH-neh)', 'Hi', 'Thank you', 'Where is the station?')),
 dict(id='de', name='German', short='DE', lang='German', city='Hamburg', cur='€', rate=0.92, climate='cold',
  accent='standard German (Hochdeutsch) accent', speech='Standard German, informal "du"',
  watch='Over-formal phrasing and too many English words',
  fillers='"also", "halt", "irgendwie", "quasi"',
  local=['Bakeries and discounters like Aldi-style stores', 'S-Bahn, U-Bahn and the Deutschland ticket', 'Rainy, cool weather'],
  dish='lentil soup with a Quark dip and rye bread',
  ai='EU: AI Act Article 50 applies from 2 August 2026; tools already on the market get until 2 December 2026 for the marking duty. Label the persona as AI.',
  bet=('ok', 'Germany: affiliates can generally promote locally licensed brands under strict content, timing and placement rules. Verify the current rules before launch.'),
  ph=('Hallo', '(HAH-loh)', 'Danke', '(DAHN-kuh)', 'Wo ist der Bahnhof?', '(voh ist dehr BAHN-hohf)', 'Hi', 'Thank you', 'Where is the station?')),
 dict(id='fi', name='Finnish', short='FI', lang='Finnish', city='Helsinki', cur='€', rate=0.92, climate='cold',
  accent='Helsinki Finnish accent', speech='Spoken Finnish, not formal written Finnish',
  watch='Voice quality is untested; use short sentences and test heavily',
  fillers='"no niin", "tota", "siis", "vähän"',
  local=['K-Market and S-Market grocery chains', 'Trams, metro and trains', 'Dark winters and long summer evenings'],
  dish='light salmon soup (lohikeitto) with rye bread',
  ai='EU: AI Act Article 50 applies from 2 August 2026; tools already on the market get until 2 December 2026 for the marking duty. Label the persona as AI.',
  bet=('no', 'Finland: state gambling monopoly; promoting other operators is illegal marketing, and a new law from 1 July 2027 effectively bans influencers from distributing even licensed operators\' marketing. No betting persona.'),
  ph=('Hei', '(hay)', 'Kiitos', '(KEE-tohs)', 'Missä on asema?', '(MIS-sa on AH-seh-mah)', 'Hi', 'Thank you', 'Where is the station?')),
 dict(id='dk', name='Danish', short='DA', lang='Danish', city='Copenhagen', cur='kr', rate=7, climate='cold',
  accent='Copenhagen Danish accent', speech='Standard Copenhagen Danish',
  watch='Pronunciation is hard for voice models; test heavily',
  fillers='"altså", "jo", "ikke også", "sådan"',
  local=['Bakeries, Netto-style discounters and bike lanes', 'Metro, S-train and cargo bikes', 'Grey, windy winters and hygge'],
  dish='open rye sandwich (smørrebrød) with egg, shrimp and salad',
  ai='EU: AI Act Article 50 applies from 2 August 2026; tools already on the market get until 2 December 2026 for the marking duty. Label the persona as AI.',
  bet=('ok', 'Denmark: affiliates can generally promote locally licensed brands under strict content, timing and placement rules. Verify the current rules before launch.'),
  ph=('Hej', '(hy)', 'Tak', '(tahk)', 'Hvor er stationen?', '(vor air stah-SHOHN-en)', 'Hi', 'Thank you', 'Where is the station?')),
 dict(id='no', name='Norwegian', short='NO', lang='Norwegian', city='Oslo', cur='kr', rate=10.5, climate='cold',
  accent='Oslo Norwegian (Bokmål) accent', speech='Bokmål with an Oslo-area accent',
  watch='Dialect mismatch; test heavily',
  fillers='"altså", "liksom", "ikke sant", "egentlig"',
  local=['Grocery chains like Rema-style stores', 'T-bane, trams and ferries', 'Snowy winters and outdoor culture'],
  dish='light fish cakes (fiskekaker) with vegetables',
  ai='Norwegian AI-labelling rules were not researched; label the persona as AI and check advertising rules.',
  bet=('no', 'Norway: promotion is limited to the two monopoly operators; helping market sites licensed elsewhere is illegal. No betting persona.'),
  ph=('Hei', '(hy)', 'Takk', '(tahk)', 'Hvor er stasjonen?', '(voor air stah-SHOON-en)', 'Hi', 'Thank you', 'Where is the station?')),
]
MK = {m['id']: m for m in M}

# ---------------------------------------------------------------- roster (woman, man)
R = {
 'us': dict(food=('Hannah','Tyler'), code=('Chloe','Ethan'), design=('Zoe','Noah'), bet=(None,'Jake'), gadget=('Riley','Mason'), home=('Maya','Caleb'), lang=('Lily','w')),
 'uk': dict(food=('Poppy','Harry'), code=('Imogen','Oliver'), design=('Isla','Archie'), bet=(None,'Dean'), gadget=('Amelia','Callum'), home=('Holly','Toby'), lang=('Jack','m')),
 'es': dict(food=('Valentina','Santiago'), code=('Camila','Mateo'), design=('Daniela','Diego'), bet=(None,'Sebastian'), gadget=('Lucia','Andres'), home=('Paula','Joaquin'), lang=('Sofia','w')),
 'br': dict(food=('Larissa','Gabriel'), code=('Juliana','Rafael'), design=('Mariana','Lucas'), bet=(None,'Matheus'), gadget=('Fernanda','Thiago'), home=('Bruna','Pedro'), lang=('Felipe','m')),
 'pt': dict(food=('Ines','Tiago'), code=('Marta','Diogo'), design=('Catarina','Duarte'), bet=(None,'Hugo'), gadget=('Rita','Rui'), home=('Joana','Miguel'), lang=('Sara','w')),
 'fr': dict(food=('Camille','Antoine'), code=('Lea','Maxime'), design=('Manon','Theo'), bet=(None,None), gadget=('Oceane','Romain'), home=('Juliette','Baptiste'), lang=('Elodie','w')),
 'it': dict(food=('Giulia','Luca'), code=('Chiara','Marco'), design=('Elisa','Alessandro'), bet=(None,None), gadget=('Martina','Matteo'), home=('Federica','Davide'), lang=('Lorenzo','m')),
 'de': dict(food=('Lena','Jonas'), code=('Annika','Felix'), design=('Mia','Leon'), bet=(None,'Florian'), gadget=('Laura','Tobias'), home=('Jana','Lukas'), lang=('Niklas','m')),
 'fi': dict(food=('Aino','Eero'), code=('Helmi','Elias'), design=('Venla','Onni'), bet=(None,None), gadget=('Siiri','Joonas'), home=('Emmi','Veeti'), lang=('Ilona','w')),
 'dk': dict(food=('Sofie','Mads'), code=('Ida','Magnus'), design=('Clara','Oscar'), bet=(None,'Rasmus'), gadget=('Nanna','Frederik'), home=('Mille','Anders'), lang=('Emil','m')),
 'no': dict(food=('Ingrid','Henrik'), code=('Nora','Sander'), design=('Thea','Jakob'), bet=(None,None), gadget=('Maja','Kristian'), home=('Silje','Andreas'), lang=('Hedda','w')),
}

# ---------------------------------------------------------------- niches
def clips(*items): return list(items)

N = [
 dict(id='food', name='Healthy food', icon='fork', color=('#30D158', '#0A9E7B'), genders='Woman and man',
  tagline='Kcal-smart meals that are practical to cook.',
  what='Recipes with kcal per portion, weight-loss swaps, practical weekly planning and gentle wellness habits (sleep-friendly dinners, hydration, simple routines). Wellness lives inside this niche.',
  why='Food content is saved and shared, and a plan or shopping list is an easy low-price product. Kcal on screen gives a clear hook and a clear result.',
  series=[('Plate of the Day', 'One recipe, kcal and protein on screen, finished plate in the first second.'),
          ('The 7-Day Plan', 'A week of meals in 7 parts; the full printable plan is the offer.'),
          ('Swap Saturday', 'Swap one ingredient and show the kcal saved.'),
          ('Grocery Run', 'The shopping list and total cost for a week.')],
  pillars=['Recipes with kcal and portions', 'Weight-loss swaps that keep you full', 'Practicality: time, cost, batch cooking', 'Wellness habits (no medical claims)'],
  angles_w=['The 20-minute weeknight cook', 'The budget meal-prepper', 'The kcal-swap detective', 'The batch-cooking Sunday planner'],
  angles_m=['The high-protein simple cook', 'The cut-without-boredom cook', 'The lunchbox-for-work planner', 'The sheet-pan and grill cook'],
  clips=[('Recipe', 'One pan, 400 kcal: {dish}'), ('Swaps', '3 swaps that cut 300 kcal without feeling hungry'), ('Prep', 'Sunday prep: 5 lunches in 40 minutes'),
         ('Education', 'What 500 kcal looks like, three ways'), ('Shopping', 'One grocery list, a whole week, total cost on screen'),
         ('Comparison', 'Takeaway order vs the home version, kcal side by side'), ('Recipe', 'A breakfast under 300 kcal that keeps you full'),
         ('Mistake', 'The mistake that makes meal prep taste boring'), ('Series', 'A week of dinners under 450 kcal (Part 1)'),
         ('Series', 'Part 2: the full plan reveal and where to get it')],
  hooks=['"{c}" Say the number in the first second.', 'Contrarian: "Stop counting calories like this."', 'Number: "Four ingredients, nine minutes, 410 kcal."'],
  offer='4-week meal plans by kcal range with shopping lists, recipe books and a kcal tracker sheet.',
  price=(12, 25), ladder=['Free: the recipe in the video', 'Low: 7-day plan with shopping list', 'Mid: 4-week plan + tracker + swaps guide'],
  honesty='Show kcal and portions as information. No extreme diets, no promised weight loss, no medical claims. Point people with medical needs to a doctor or dietitian. Check kcal with a food database, not by guess.',
  kpis=['Saves and shares per video', 'Average watch time', 'Link clicks to the plan', 'Plan sales'],
  tags=['#mealprep', '#healthyrecipes', '#caloriedeficit', '#easydinner', '#aiinfluencer'],
  desc=dict(tt='{h} Which would you cook first? Part 2 tomorrow. Full plan in my profile. {tags}',
            ig='{h} Dinner used to be my calorie trap, so I planned the whole week in one shop. Save this for your next grocery run. The full plan is linked in my profile. (AI creator.) {tags}',
            yt_title='{t}', yt='In this Short: the recipe, the portions and the kcal. The complete printable plan is linked below. I am an AI creator; the link is a product link where stated. #Shorts {tags}'),
  bio='AI creator. Kcal-smart meals you can actually cook. Plan below.',
  ),
 dict(id='code', name='Coding and AI', icon='code', color=('#0A84FF', '#5E5CE6'), genders='Woman and man',
  tagline='Shows an AI app, prompt, workflow, skill or repo and runs it live.',
  what='Courses, mini courses, prompts, workflows, Claude skills, GitHub repos and AI apps, each presented and then shown working. Long builds are split into parts so each clip is short and viewers come back.',
  why='A visible result in the first seconds is the strongest hook, and prompt packs, templates and courses are natural low-price digital products.',
  series=[('Build in Parts', 'A project split into Part 1, 2, 3; each part ends on a question.'),
          ('Prompt of the Week', 'One prompt, the exact output, how to adapt it.'),
          ('Repo of the Week', 'A GitHub repo explained in 30 seconds and run live.'),
          ('Skill Drop', 'A Claude skill or workflow that saves time, shown end to end.')],
  pillars=['Result first, then how', 'Prompts and workflows shown running', 'Repos and skills explained simply', 'Courses and mini courses split into parts'],
  angles_w=['The ship-it-in-a-weekend builder', 'The prompt engineer who shows the output', 'The beginner\'s translator (code in plain words)', 'The GitHub repo explorer'],
  angles_m=['The automation builder', 'The weekend app shipper', 'The workflow tinkerer', 'The AI-tools tester who shows the result'],
  clips=[('Build', 'I built a small app in 12 minutes with AI: result first'), ('Prompt', 'The prompt that writes my weekly report'),
         ('Repo', 'Repo of the week: what it does and a live run'), ('Skills', '3 Claude skills that save two hours'),
         ('Workflow', 'Automate one boring task (Part 1)'), ('Workflow', 'Part 2: the finished automation running'),
         ('Education', 'Beginner mistake when asking an AI to build an app'), ('Course', 'Lesson 1 free: from idea to working page'),
         ('Test', 'I tried to break this AI-built app: bug hunt'), ('Series', 'Build a landing page in parts (Part 1)')],
  hooks=['"{c}" Open on the finished app running.', 'Contrarian: "You do not need a developer for this."', 'Number: "Twelve minutes, one prompt, a working app."'],
  offer='Mini courses, courses, prompt packs, workflow templates, Claude skill packs and paid repos.',
  price=(9, 99), ladder=['Free: Part 1 and the first prompt', 'Low: prompt pack or template', 'Mid: mini course or paid repo', 'High: full course'],
  honesty='Show real runs, including errors. No "make 10k with AI" or income claims. Credit open-source repos and licences. Only present code and apps the team actually ran.',
  kpis=['Watch time on Part 1', 'Part 1 to Part 2 return rate', 'Link clicks', 'Pack and course sales'],
  tags=['#coding', '#ai', '#promptengineering', '#buildinpublic', '#aiinfluencer'],
  desc=dict(tt='{h} Part 2 tomorrow. Prompt and template in my profile. {tags}',
            ig='{h} I show the result first, then exactly how it works. Save this and follow for part 2. The pack is linked in my profile. (AI creator.) {tags}',
            yt_title='{t}', yt='In this Short: the idea, the prompt and the live result. Part 2 is next. The full course and templates are linked below. I am an AI creator. #Shorts {tags}'),
  bio='AI creator. I build with AI and show it working. Courses below.',
  ),
 dict(id='design', name='Design', icon='pen', color=('#BF5AF2', '#5E5CE6'), genders='Woman and man',
  tagline='Apps, coded apps and Figma work with a before vs after animated transition.',
  what='Presents app designs, coded apps and Figma files, always with a before vs after and an animated transition between them.',
  why='A satisfying transition is a built-in hook and a built-in loop, and UI kits and templates sell well to designers and founders.',
  series=[('Before vs After', 'A real design before and after, joined by an animated transition.'),
          ('Figma in 60 Seconds', 'One technique in one minute with the result.'),
          ('App Teardown', 'What works and what to fix in a design the team made.'),
          ('Coded App Showcase', 'A coded app, then the design that made it feel good.')],
  pillars=['Before vs after with animated transitions', 'Figma tips shown in the file', 'Coded app showcases', 'Design critiques of the team\'s own work'],
  angles_w=['The before/after redesigner', 'The Figma speed-runner', 'The coded-app showcase builder', 'The app-teardown critic'],
  angles_m=['The before/after redesigner', 'The UI-systems nerd', 'The motion-and-transition designer', 'The design-to-code builder'],
  clips=[('Before/After', 'Redesign of a booking screen: before, after, transition'), ('Figma', 'Auto layout in 60 seconds'),
         ('Teardown', 'What is wrong with this onboarding screen'), ('Coded app', 'A small app in code: the design and the result'),
         ('Before/After', 'A cluttered dashboard made calm'), ('Figma', 'Build a button system in one minute'),
         ('Motion', 'The transition that makes an app feel premium'), ('Series', 'Redesign a settings screen (Part 1)'),
         ('Series', 'Part 2: the reveal with the animated transition'), ('Offer', 'Inside the UI kit: five screens in 20 seconds')],
  hooks=['"{c}" Start on the before frame, then cut.', 'Contrarian: "Your app does not need more features, it needs this."', 'Number: "Three changes, one screen, completely different."'],
  offer='Figma UI kits, app templates, design systems and UI prompt packs.',
  price=(15, 79), ladder=['Free: the screen shown in the video', 'Low: component pack', 'Mid: full UI kit', 'High: design system + templates'],
  honesty='Only show designs the team actually made. Do not pass off other people\'s work as yours, and do not recreate real brands\' apps or logos.',
  kpis=['Replays and loops', 'Shares', 'Link clicks', 'Kit sales'],
  tags=['#uidesign', '#figma', '#beforeandafter', '#appdesign', '#aiinfluencer'],
  desc=dict(tt='{h} Watch the transition. Kit in my profile. {tags}',
            ig='{h} Before and after, one screen. Save this for your next design. The full kit is linked in my profile. (AI creator.) {tags}',
            yt_title='{t}', yt='In this Short: the before, the after and the animated transition. The UI kit is linked below. I am an AI creator. #Shorts {tags}'),
  bio='AI creator. Before and after designs. UI kits below.',
  ),
 dict(id='bet', name='Sports betting', icon='ball', color=('#FF9F0A', '#FF375F'), genders='Man only',
  tagline='Promotes a tips app: every step shown, a real bet, the real result.',
  what='Walks through the tips app screen by screen (sign-up, settings, reading a tip, bankroll, history, limits), then shows a real bet and the game result.',
  why='Step-by-step app tours are searchable and the weekly results recap builds trust. Earns from the app\'s affiliate or referral program.',
  series=[('How the App Works', 'One screen or feature per clip, with the real app.'),
          ('The Bet', 'A real bet placed on a real account, with the stake.'),
          ('Result Day', 'The game result and what it means for the bet, win or loss.'),
          ('Weekly Recap', 'All bets of the week with true totals, losses included.')],
  pillars=['Step-by-step app tour', 'Real bets with stakes', 'Real results, wins and losses', 'Limits and responsible gambling'],
  angles_w=[], angles_m=['The step-by-step app explainer', 'The weekly results recap guy', 'The stake-discipline guy'],
  clips=[('App tour', 'Part 1: sign-up and settings'), ('App tour', 'Part 2: the home screen and how a tip looks'),
         ('App tour', 'Part 3: the bankroll and stake tools'), ('Bet', 'A real bet: the tip, the odds, the stake'),
         ('Result', 'The game result and what happened to the bet'), ('App tour', 'Setting limits and responsible-gambling tools'),
         ('Mistake', 'The mistake that makes people chase losses'), ('Recap', 'Week 1: all bets, true totals'),
         ('Bet', 'Another real bet, explained step by step'), ('Result', 'Result day and the honest weekly numbers')],
  hooks=['"{c}" Show the app screen in the first second.', 'Contrarian: "A tip is not a guarantee. Here is the whole app."', 'Number: "Five screens, here is how the app works."'],
  offer='The tips app through its affiliate or referral program, where legal.',
  price=(0, 0), ladder=['Free: app tour parts', 'Soft: results recap', 'Commission: the app link, where legal'],
  honesty='Real account, real bets, real results including losses. Never staged or invented winning slips or balances. Never say tips improve the chance of winning or guarantee profit. Show the age limit and a responsible-gambling message. Disclose the affiliate link and that the persona is AI.',
  kpis=['Watch time on app tours', 'Recap views', 'Link clicks', 'Referral sign-ups'],
  tags=['#sportstips', '#bettingapp', '#18plus', '#responsiblegambling', '#aiinfluencer'],
  desc=dict(tt='{h} Real account, real results. 18+ gamble responsibly. Link in profile. {tags}',
            ig='{h} I show every step of the app and the real result, wins and losses. 18+ only, gamble responsibly. (AI creator, affiliate link in profile.) {tags}',
            yt_title='{t}', yt='In this Short: a step in the app and a real result. 18+ only. Gamble responsibly. I am an AI creator and the link below is an affiliate link. #Shorts {tags}'),
  bio='AI creator. Betting app walkthroughs, real results. 18+. Affiliate link.',
  ),
 dict(id='gadget', name='Gadgets', icon='bolt', color=('#64D2FF', '#0A84FF'), genders='Woman and man',
  tagline='Gadgets the team found, bought and reviewed.',
  what='Discovered, bought and reviewed gadgets: unboxing, real use, honest verdict and downsides. Reviews are by the team with real footage; the persona presents the findings.',
  why='Review content answers a buying question directly, and affiliate links and buyer\'s guides are natural monetization.',
  series=[('Bought It, Tested It', 'One gadget, one real test, one verdict.'),
          ('Keep or Return', 'The verdict after a week of use.'),
          ('Under {cur}30', 'Cheap finds that were worth it.'),
          ('Cheap vs Expensive', 'Two versions of the same gadget side by side.')],
  pillars=['Discover: how we found it', 'Test: real footage of real use', 'Verdict: keep, return or skip', 'Honest downsides'],
  angles_w=['The "we bought it so you do not have to" tester', 'The under-30 finds hunter', 'The desk-and-travel gadget tester', 'The smart-home starter tester'],
  angles_m=['The hardware tester', 'The battery-and-specs checker', 'The deals-and-value hunter', 'The smart-home tinkerer'],
  clips=[('Review', 'We bought it, we tested it: gadget #1'), ('Verdict', 'Keep or return after one week'), ('Comparison', 'Cheap vs expensive, same job'),
         ('Review', 'Gadget #2: the setup in 60 seconds'), ('Test', 'Real battery test: hours, not claims'), ('List', '3 gadgets we would buy again'),
         ('Honest', 'The one that disappointed us and why'), ('Review', 'Gadget #3: unboxing and first impression'),
         ('Under {cur}30', 'Five finds under thirty'), ('Offer', 'Our buyer\'s guide: what to buy first')],
  hooks=['"{c}" Show the gadget working in the first second.', 'Contrarian: "Do not buy this until you see the test."', 'Number: "Three weeks, one gadget, one honest verdict."'],
  offer='Affiliate links to tested products, buyer\'s guides and a deals newsletter.',
  price=(5, 15), ladder=['Free: the review', 'Low: buyer\'s guide', 'Recurring: deals newsletter'],
  honesty='The team really bought and tested every product, with real footage. Use "we bought" and "our test", include the downsides, no invented personal experience, no fake reviews. Disclose affiliate links in the video and the description.',
  kpis=['Watch time', 'Saves', 'Affiliate clicks', 'Guide sales'],
  tags=['#gadgets', '#techfinds', '#unboxing', '#honestreview', '#aiinfluencer'],
  desc=dict(tt='{h} Our honest test. Link in profile (affiliate). {tags}',
            ig='{h} We bought it with our own money and tested it for a week. The honest verdict is in the video. Affiliate links in my profile. (AI creator.) {tags}',
            yt_title='{t}', yt='In this Short: what we bought, how we tested it and our verdict, downsides included. Links below are affiliate links. I am an AI creator. #Shorts {tags}'),
  bio='AI creator. We buy gadgets, test them, tell you the truth. Affiliate links.',
  ),
 dict(id='home', name='Home finds', icon='home', color=('#FF9F0A', '#FF6B35'), genders='Woman and man',
  tagline='Home items the team found, bought and reviewed.',
  what='Same idea as Gadgets, for the home: organizers, kitchen finds, cleaning, small upgrades, with before and after of the space.',
  why='Before and after is a natural hook, and finds guides and checklists sell with little work.',
  series=[('Bought It for the Home', 'One item, one real test, one verdict.'),
          ('Before / After Room', 'A small space improved with a real purchase.'),
          ('Under {cur}20 Home Finds', 'Cheap home finds that were worth it.'),
          ('Does It Work?', 'A direct test of a hyped home product.')],
  pillars=['Discover: how we found it', 'Test in a real home', 'Before and after of the space', 'Honest verdict and downsides'],
  angles_w=['The small-space organizer', 'The kitchen finds tester', 'The renter-friendly upgrade tester', 'The cleaning-hacks tester'],
  angles_m=['The DIY and tools tester', 'The garage and utility finds tester', 'The smart-home upgrade tester', 'The tidy home-office tester'],
  clips=[('Review', 'We bought it for the kitchen: test and verdict'), ('Before/After', 'A small corner, before and after'),
         ('Under {cur}20', 'Five home finds under twenty'), ('Test', 'Does this hyped cleaner actually work?'),
         ('Review', 'The organizer that fixed our shelf'), ('Honest', 'The home find we returned and why'),
         ('Before/After', 'A desk setup, before and after'), ('List', '3 home items we would buy again'),
         ('Review', 'Renter-friendly upgrade: no drilling'), ('Offer', 'Our home finds checklist: start here')],
  hooks=['"{c}" Open on the before frame.', 'Contrarian: "You do not need a bigger home, you need this."', 'Number: "One shelf, twenty minutes, completely different."'],
  offer='Affiliate links to tested items, finds guides, room checklists and planning templates.',
  price=(7, 19), ladder=['Free: the review', 'Low: room checklist', 'Mid: finds guide + planning template'],
  honesty='The team really bought and tested every item, with real footage and real before/after photos. Use "we bought" wording, show downsides, no invented personal experience, no fake reviews. Disclose affiliate links.',
  kpis=['Watch time', 'Saves', 'Affiliate clicks', 'Guide sales'],
  tags=['#homefinds', '#homeorganization', '#beforeandafter', '#honestreview', '#aiinfluencer'],
  desc=dict(tt='{h} Tested in a real home. Link in profile (affiliate). {tags}',
            ig='{h} We bought it and tested it at home. Before and after is in the video. Affiliate links in my profile. (AI creator.) {tags}',
            yt_title='{t}', yt='In this Short: what we bought for the home, the test and the verdict. Links below are affiliate links. I am an AI creator. #Shorts {tags}'),
  bio='AI creator. Home finds we bought and tested. Affiliate links.',
  ),
 dict(id='lang', name='Language learning', icon='speech', color=('#34C759', '#30B0C7'), genders='One persona per language',
  tagline='Short numbered episodes, one every 1 to 3 days.',
  what='Short lessons in the persona\'s own language in numbered episodes (Episode 1 to 30, in seasons). A fixed rhythm: one episode every 1 to 3 days. Default audience: English speakers learning the persona\'s language, with English captions.',
  why='A numbered series gives viewers a reason to follow, finish and come back, and workbooks, flashcards and audio packs match the lesson format.',
  series=[('Season 1: Basics', 'Episodes 1 to 10: greetings, politeness, numbers, ordering.'),
          ('Season 2: Eating and Shopping', 'Episodes 11 to 20.'),
          ('Season 3: Getting Around', 'Episodes 21 to 30.'),
          ('Recap and Quiz', 'The last episode of each season.')],
  pillars=['One phrase per episode', 'Slow, then natural speed', 'Phonetic spelling on screen', 'Quiz and recap each season'],
  angles_w=['The patient café teacher', 'The travel-phrases teacher', 'The everyday-conversation coach', 'The pronunciation coach'],
  angles_m=['The patient café teacher', 'The travel-phrases teacher', 'The everyday-conversation coach', 'The pronunciation coach'],
  clips=[('Ep 1', 'Hello and goodbye'), ('Ep 2', 'Please, thank you, sorry'), ('Ep 3', 'Yes, no, I do not understand'),
         ('Ep 4', 'Introduce yourself'), ('Ep 5', 'Numbers 1 to 10'), ('Ep 6', 'Order a coffee'),
         ('Ep 7', 'How much is it?'), ('Ep 8', 'Where is the station?'), ('Ep 9', 'Asking for help'), ('Ep 10', 'Season 1 recap and quiz')],
  hooks=['"{c}" The phrase on screen in the first second.', 'Curiosity: "The one word that makes locals smile."', 'Number: "Ten seconds, one phrase, you can say it today."'],
  offer='Phrase workbooks, flashcard decks, audio packs and mini courses.',
  price=(9, 49), ladder=['Free: the episode', 'Low: season workbook', 'Mid: flashcards + audio pack', 'High: mini course'],
  honesty='A native speaker must check every episode before it goes out. Give a phonetic spelling for each new word. Never teach wrong or invented phrases.',
  kpis=['Episode completion', 'Follows after episode 3', 'Workbook clicks', 'Season completion'],
  tags=['#learnlanguages', '#languagetips', '#speaklikeanative', '#dailylanguage', '#aiinfluencer'],
  desc=dict(tt='{h} Episode {n}. Follow for the next one. Workbook in profile. {tags}',
            ig='{h} Episode {n} of the series. Save it and say it out loud. The full workbook is linked in my profile. (AI creator.) {tags}',
            yt_title='{t}', yt='In this Short: one phrase, said slowly and then at natural speed, with the phonetic spelling. The workbook is linked below. I am an AI creator. #Shorts {tags}'),
  bio='AI language coach. One phrase per episode. Workbook below.',
  ),
]

N.append(dict(id='glam', name='Glam and lifestyle', icon='eye', color=('#FF375F', '#BF5AF2'), genders='A woman (clearly an adult AI character)',
  tagline='A glamorous lifestyle persona with a consistent world.',
  what='A clearly labelled AI-generated adult woman who looks native to her market. Short reels, stories and photos of her days (home, café, gym, trips) at fashion and swimwear level. Every place is a fixed set that looks identical in every photo, story and reel. The link goes to her own page where the platform allows it.',
  why='Lifestyle accounts grow on a place and a person people can follow. A fixed, believable world is what makes a character feel consistent, and consistency is what viewers come back for.',
  series=[('A day in her room', 'Mornings and evenings in the same bedroom.'), ('Café and gym', 'The same café and the same gym.'), ('Trip arcs', 'One city for a week, with one hotel room that never changes.'), ('Your questions', 'She answers real comments.')],
  pillars=['A fixed world that never changes', 'Outfits and routines', 'Trips told over several days', 'Replies to real comments'],
  angles_w=['The glam traveller', 'The city girl with a morning routine', 'The fitness and style girl', 'The weekend-trip storyteller'], angles_m=[],
  clips=[('Morning', 'Morning in my room'), ('Café', 'Coffee in the corner café'), ('Gym', 'Gym session, her way'), ('Trip', 'Packing for Paris'), ('Trip', 'The hotel room in Paris')],
  hooks=['Place first: "This is my room, and this is how my day starts."', 'Open loop: "I leave for Paris tomorrow. What should I pack?"', 'Choice: "Two dresses, one coffee. Help me choose."'],
  offer='Her own page on a platform that allows clearly labelled AI characters (Fanvue says it does, with ID verification; check the current wording).',
  price=(0, 0), ladder=['Free: the reels, stories and photos', 'Low: the page subscription'],
  honesty='She is an AI-generated adult character and says so: the Instagram "AI-generated profile" label, TikTok and YouTube AI labels, and a bio line. Never claim or imply she is real, no fake DMs or fake fans, no real person\'s likeness, nothing explicit, and nothing that could read as a minor. Public posts stay at fashion and swimwear level. Link to an adult-subscription page only where the platform allows it; TikTok bans promoting premium sexual content and Instagram restricts adult-service promotion. If a platform forbids it, do not link and do not hint at it.',
  kpis=['Reach to non-followers', 'Follows per reel', 'Story replies and poll votes', 'Clicks to her page where allowed'],
  tags=['#aigenerated', '#lifestyle', '#travelvlog', '#ootd', '#aiinfluencer'],
  desc=dict(tt='{h} AI-generated character. {tags}', ig='{h} I am an AI-generated character. More of my days in my profile where allowed. {tags}', yt_title='{t}', yt='A day in the life of an AI-generated character. #Shorts {tags}'),
  bio='AI-generated character. My days, my trips. My page below where allowed.',
  ))
NK = {n['id']: n for n in N}

# ---- rework (7 Nov 2026): one persona per niche per language; own product per persona ----
NICHE_OVR = {
 'food': dict(genders='A woman (healthy recipes) and, in the US, a man (weight loss and getting lean)',
   what='Two personas in the US. The woman cooks one healthy recipe per reel (cakes, pies, burgers, lettuce wraps) and points to her recipe book. The man covers weight loss and getting lean: recipes, what to eat and what not to eat with kcal, and calculators for kcal, protein and water, pointing to his recipe book and 7-day plan. Other languages get one woman doing the healthy recipes. Wellness lives inside this niche.',
   offer='Hannah: a recipe book. Tyler: a 7-day shred plan and a recipe book.',
   ladder=['Free: the recipe or the trick in the reel', 'Low: the recipe book', 'Mid: the 7-day plan (Tyler) or recipe book bundle'],
   angles_m=['The cut-and-keep-the-muscle cook', 'The what-to-eat-and-what-not coach', 'The kcal, protein and water calculator guy', 'The 7-day shred planner']),
 'code': dict(genders='A man',
   what='One man who teaches AI and coding hacks with Claude, tests trending GitHub repos and says whether they really work, builds apps on camera, and sells a PDF or short book of AI tricks.',
   offer='A PDF or short book of AI tricks (Claude workflows, prompts, repo tests), plus optional prompt packs.',
   ladder=['Free: the trick in the reel', 'Low: the AI tricks PDF', 'Mid: prompt and workflow pack', 'High: mini course'], price=(9, 39),
   angles_m=['The Claude hacks guy', 'The does-this-repo-really-work tester', 'The weekend app builder', 'The workflow automator']),
 'design': dict(genders='A woman',
   what='One woman who teaches design for digital: spacing rules, colour palettes applied to a real site or app (start with one colour, add a second, the third makes it pop), type, contrast and before and afters, and sells a course.',
   offer='A design course (with UI kits and palettes).',
   ladder=['Free: the tip or palette in the reel', 'Low: a template or palette pack', 'Mid: the design course'], price=(9, 149),
   angles_w=['The spacing-and-palette teacher', 'The before/after redesigner', 'The Figma speed-runner', 'The design-for-digital teacher']),
 'gadget': dict(genders='A man',
   what='A Shopify store that sells the gadgets themselves. Each reel shows a problem most people have, the gadget that solves it working on camera, and sends people to the store.',
   offer='The gadgets themselves, sold in the persona\'s Shopify store.', price=(12, 60),
   ladder=['Free: the reel and the demo', 'Low: a small gadget', 'Mid: the better version or a bundle'],
   series=[('Problem, gadget, proof', 'One everyday problem, the gadget that fixes it, shown working.'), ('Under {cur}30', 'Cheap gadgets that solve a real problem.'), ('Does it really work?', 'A direct test of a gadget, downsides included.'), ('Setup in 30 seconds', 'How to start using the gadget.')],
   pillars=['A problem most people have', 'The gadget solving it on camera', 'Honest limits and downsides', 'Where to get it (the store)'],
   honesty='Sell only products you ordered and tested yourself, with real footage. State the real price and shipping time and honour returns (EU and UK: 14 days). No fake reviews, countdown timers or stock claims. Check product safety marks, VAT and each platform\'s rules for selling and ads.'),
 'home': dict(genders='A woman',
   what='A Shopify store that sells home items. Each reel shows a problem most homes have, the item that solves it working in a real room, and sends people to the store.',
   offer='The home items themselves, sold in the persona\'s Shopify store.', price=(10, 50),
   ladder=['Free: the reel and the demo', 'Low: a small item', 'Mid: a set or bundle'],
   series=[('Problem, item, proof', 'One home problem, the item that fixes it, shown working in a real room.'), ('Under {cur}20', 'Cheap home items that solve a real problem.'), ('Before / After room', 'A small space improved with a real item.'), ('Does it really work?', 'A direct test of a hyped item, downsides included.')],
   pillars=['A problem most homes have', 'The item solving it in a real room', 'Before and after of the space', 'Honest limits and where to get it (the store)'],
   honesty='Sell only items you ordered and tested yourself, with real footage and real before and after photos. State the real price and shipping time and honour returns (EU and UK: 14 days). No fake reviews, countdown timers or stock claims. Check product safety marks, VAT and each platform\'s rules for selling and ads.'),
}
for _k, _v in NICHE_OVR.items(): NK[_k].update(_v)
PBIO = {('glam', 'w'): 'AI-generated character. My days and my trips. My page below where allowed.',('food', 'w'): 'AI creator. One healthy recipe per reel. Recipe book below.',
        ('food', 'm'): 'AI creator. Lose fat, keep the muscle. 7-day plan below.',
        ('code', 'm'): 'AI creator. Claude hacks and repo tests. AI tricks PDF below.',
        ('design', 'w'): 'AI creator. Design tips for apps and sites. Course below.',
        ('gadget', 'm'): 'AI creator. Gadgets that fix daily problems. Store below.',
        ('home', 'w'): 'AI creator. Home items that fix daily problems. Store below.'}
POFFER = {('glam', 'w'): 'Her own AI-labelled page, linked where the platform allows it',('food', 'w'): 'Recipe book (link in bio)', ('food', 'm'): '7-day shred plan and recipe book (link in bio)', ('code', 'm'): 'AI tricks PDF (link in bio)',
          ('design', 'w'): 'Design course (link in bio)', ('gadget', 'm'): 'The gadgets, in his Shopify store (link in bio)', ('home', 'w'): 'The home items, in her Shopify store (link in bio)'}
BACK_TYLER = "{n} got tired of crash diets and guessing calories, and learned to lose fat while keeping muscle by tracking kcal, protein and water. {Sc} shows what to eat and what not to eat with the numbers on screen, does the maths live, and is clear that it is information, not medical advice. {Sc} is a creator, not a doctor."

# ---------------------------------------------------------------- persona building helpers
HAIR_W = ['shoulder-length dark brown hair with a few flyaway strands', 'long wavy light-brown hair loosely tied back', 'a short bob with natural texture', 'medium-length hair in a messy low bun', 'curly hair worn naturally', 'long straight hair tucked behind one ear']
HAIR_M = ['short dark hair with a natural messy texture', 'short light-brown hair and a few days of stubble', 'medium-length wavy hair pushed back', 'a short fade with natural texture', 'short curly hair', 'a light beard and short tidy hair']
OUT = {
 ('food','w'): 'a linen shirt and jeans with the sleeves rolled up', ('food','m'): 'a plain henley and chinos with a kitchen towel on the shoulder',
 ('code','w'): 'an oversized knit sweater and jeans with headphones around the neck', ('code','m'): 'a plain hoodie and jeans',
 ('design','w'): 'a simple structured jacket over a tee with minimal jewellery', ('design','m'): 'a crewneck sweatshirt and clean sneakers',
 ('bet','m'): 'a casual jacket over a tee and jeans',
 ('gadget','w'): 'a denim jacket and a crossbody bag', ('gadget','m'): 'a utility jacket and jeans',
 ('home','w'): 'a soft cardigan and jeans', ('home','m'): 'a flannel shirt and work trousers',
 ('glam','w'): 'a fitted summer dress and sunglasses', ('lang','w'): 'a smart-casual knit top and jeans', ('lang','m'): 'a smart-casual shirt and jeans',
}
CLIM = {'cold': ', with a warm coat and scarf in the cold season', 'mild': ', with a light jacket', 'warm': ', in light breathable fabrics'}
SET = {
 'food': 'in a bright home kitchen with fresh groceries on the counter',
 'code': 'at a desk in a cosy apartment with a laptop and a plant',
 'design': 'at a small desk with a tablet and printed sketches',
 'bet': 'on a sofa in a living room, relaxed, phone in hand',
 'gadget': 'at a table with a plain unbranded gadget box and a phone',
 'home': 'in a small tidy living room corner with a shelf',
 'lang': 'at a local café table with a notebook and a coffee',
 'glam': 'in a bright bedroom with white linen and a brass lamp, relaxed',
}
TONE = {
 'food': 'warm and encouraging', 'code': 'clear, curious and quick', 'design': 'calm and precise with dry humour',
 'bet': 'level-headed and measured, never hyped', 'gadget': 'curious, a little sceptical and honest',
 'home': 'practical and cheerful', 'glam': 'warm, playful and a little flirty, always honest that she is AI', 'lang': 'patient, clear and smiling, slightly slower and articulate',
}

def pro(g):
    return dict(S='she', O='her', P='her', Sc='She') if g == 'w' else dict(S='he', O='him', P='his', Sc='He')

BACK = {
 'food': "{n} works a regular job and started cooking practical meals after getting tired of takeaway and guessing calories. {Sc} tracks kcal without obsessing, loves recipes that fit a busy week, and explains things like a friend in the kitchen. {Sc} is honest about what works and what does not, laughs at {P} failed experiments, and posts about meal plans, swaps and simple wellness habits.",
 'code': "{n} learned to build things with AI tools and loves turning ideas into working apps fast. {Sc} explains in plain words, always shows the result running, and is open about bugs and dead ends. {Sc} shares prompts, workflows, Claude skills and GitHub repos, and teaches in short parts.",
 'design': "{n} is a designer who loves interfaces that feel calm and clear. {Sc} redesigns screens, builds apps in code and works in Figma, and always shows a before and after. {Sc} is honest about design choices and enjoys a good transition animation.",
 'bet': "{n} follows sport closely and prefers clear numbers over hype. {Sc} explains betting apps step by step, shows real bets and real results, and talks openly about losses. {Sc} always mentions limits and responsible gambling, and never promises profit.",
 'gadget': "{n} loves finding useful gadgets and tests them properly before saying anything. {Sc} and the team buy what they review, say what disappoints them and keep the verdict short. {Sc} is curious, a little sceptical and honest.",
 'home': "{n} enjoys making a home work better with small, practical changes. {Sc} and the team buy the items they review, test them in a real home and show honest before and afters. {Sc} is cheerful, practical and straight about what is not worth buying.",
 'glam': "{n} is an AI-generated character who shares her days: her room, her favourite café, her gym and trips. {Sc} is warm, playful and a little flirty, says openly that she is an AI character, and keeps every place looking exactly the same from post to post.",
 'lang': "{n} is a patient teacher who believes anyone can learn a few useful phrases in seconds. {Sc} speaks {L} natively, teaches one phrase per episode, repeats it slowly and then at natural speed, and keeps lessons short and warm.",
}

def price_str(niche, m):
    lo, hi = niche['price']
    if lo == 0 and hi == 0: return 'Commission through the app\'s affiliate or referral program'
    r = m['rate']; c = m['cur']
    f = lambda v: int(round(v * r)) if r < 2 else int(round(v * r / 5) * 5)
    about = '' if r == 1 else f' (about ${lo} to ${hi})'
    return f"from {c}{f(lo)} to {c}{f(hi)}{about}; rough starting range, not researched"

PILOT = {('us', 'food', 'w'), ('us', 'code', 'm')}

def wave_of(market, niche):
    if niche == 'bet': return 3
    if niche == 'glam': return 1
    if market in ('us', 'pt'):
        return 1 if niche in ('food', 'code', 'design') else 2
    return 4

LEARNER = {'en': 'Spanish'}

def build_persona(mid, nid, g, name, idx):
    m = MK[mid]; n = NK[nid]; p = pro(g)
    angles = n['angles_w'] if g == 'w' and n['angles_w'] else n['angles_m']
    mi = [x['id'] for x in M].index(mid)
    angle = angles[mi % len(angles)] if nid != 'lang' else angles[mi % len(angles)]
    age = 24 + (mi * 3 + idx) % 8 if g == 'w' else 26 + (mi * 2 + idx) % 8
    hair = (HAIR_W if g == 'w' else HAIR_M)[(mi + idx) % 6]
    outfit = OUT[(nid, g)]
    weather = {'cold':'For outdoor shots add a warm coat and scarf.','mild':'For outdoor shots add a light jacket.','warm':'Keep fabrics light and breathable.'}[m['climate']]
    setting = SET[nid] if (nid, g) != ('food', 'm') else 'in a bright home kitchen with a food scale and a shaker on the counter'
    learner = (LEARNER['en'] + ' (with a second set of captions in Portuguese later)') if mid in ('us', 'uk') else 'English'
    langname = m['lang']
    gw = 'woman' if g == 'w' else 'man'
    backstory = (BACK_TYLER if (nid, g) == ('food', 'm') else BACK[nid]).format(n=name, Sc=p['Sc'], P=p['P'], L=langname)
    voice = f"{age} years old, from {m['city']}, {m['accent']}, {'medium pitch' if g=='w' else 'medium-low pitch'}, {TONE[nid]}, relaxed conversational pace like talking to a friend, slightly casual and unpolished, not an announcer, not a sales voice."
    photo = (f"Photorealistic candid phone photo of a {age}-year-old {gw} who could plausibly be from {m['city']}, with {hair}, wearing {outfit}, {setting}. "
             f"Natural skin texture with real imperfections, no beauty-filter gloss, slightly imperfect framing as if a friend took it, soft natural light. Full body, vertical 4:5, 4K.")
    sheet = (f"Three-panel character sheet of @{name} in 16:9 on a plain 18% gray background. Far left: full-body front view of the outfit with the head completely out of frame, cut off at the neck. "
             f"Middle: full-body rear view. Right: close-up of the face looking straight at the camera. Same person, same outfit ({outfit}), same hair ({hair}), natural skin texture, soft even lighting, no props.")
    # clips
    cl = []
    for i, (kind, title) in enumerate(n['clips']):
        t = title.replace('{dish}', m['dish']).replace('{cur}', m['cur'])
        cl.append(dict(n=i + 1, kind=kind.replace('{cur}', m['cur']), title=t))
    first = cl[0]
    hooks = [h.replace('{c}', first['title']) for h in n['hooks']]
    # video prompt
    vp = (f"@{name} 12 seconds, vertical 9:16, 1080p, audio on. {name} is {setting.replace('in a','in a')}, wearing {outfit}, talking to the camera like telling a friend. "
          f"Hook in the first second: {first['title']}. Second by second: 0 to 3 s the hook line and the key visual; 3 to 9 s the main point shown on screen; 9 to 12 s a calm closing line. "
          f"Spoken in {langname} as a native creator would say it, short and casual (ask Claude to write the exact line). Same face, hair and outfit for the whole clip. No music, no background voices, no subtitles, no on-screen text.")
    ask = (f"Use the ai-influencer-builder skill. Persona: {name} ({gw}), niche {n['name']}, language {langname}, city {m['city']}, angle: {angle}. "
           f"For clip 1 ({first['title']}) write three native-language hooks, the spoken line, and the TikTok, Instagram Reels and YouTube Shorts descriptions in {langname}. "
           f"Ask me the phonetic spelling for any brand or foreign word before finalizing.")
    # descriptions (English drafts)
    h0 = first['title'].rstrip('.') + '.'
    tags = ' '.join(n['tags'])
    d = n['desc']
    dd = dict(
        tt=d['tt'].format(h=h0, tags=tags, n=1), ig=d['ig'].format(h=h0, tags=tags, n=1),
        yt_title=first['title'][:70], yt=d['yt'].format(tags=tags, h=h0))
    wave = 0 if (mid, nid, g) in PILOT else wave_of(mid, nid)
    rules = [('AI label', m['ai'])]
    if nid == 'bet': rules.append(('Betting', m['bet'][1]))
    rules.append(('Niche rule', n['honesty']))
    rules.append(('Language check', f"Have a native {langname} speaker watch three sample clips with the sound on before scaling. {m['watch']}."))
    if mid in ('fi', 'dk', 'no'): rules.append(('Voice quality', 'Nordic voice quality is untested. Launch last and test heavily.'))
    if nid == 'lang': rules.append(('Pronunciation', 'Every episode is checked by a native speaker. Phonetic respellings on screen are approximate.'))
    # checklist
    check = ['Chose the face from the first photo', 'Named and saved the character in OpenArt', 'Voice designed and tested with a normal sentence',
             'Character sheet added', 'Three photos in different outfits and places', 'Native speaker checked three sample clips',
             'Account created with AI label and bio', 'First 8 clips posted over 4 weeks (mix of formats)', 'Reviewed the numbers and the credits spent']
    sample_ph = None
    if nid == 'lang':
        ph = m['ph']
        sample_ph = dict(hello=(ph[0], ph[1]), thanks=(ph[2], ph[3]), station=(ph[4], ph[5]), caption=(ph[6], ph[7] if len(ph)>7 else ''))
        if mid in ('us','uk'):
            sample_ph = dict(hello=('Hi', '(hy)'), thanks=('Thank you', '(thank yoo)'), station=('Where is the station?', '(wair iz the STAY-shun)'), caption=('Hola · Gracias · ¿Dónde está la estación?', ''))
    pid = f"{mid}-{nid}" + ('' if nid == 'lang' else '-' + g)
    return dict(id=pid, name=name, g=g, mkt=mid, niche=nid, age=age, angle=angle, wave=wave,
                price=price_str(n, m), learner=learner if nid == 'lang' else None,
                bio=PBIO.get((nid, g), n['bio']), offer=POFFER.get((nid, g), n['offer']), backstory=backstory, voice=voice, photo=photo, sheet=sheet, video=vp, ask=ask,
                clips=cl, hooks=hooks, desc=dd, rules=rules, check=check, ph=sample_ph, weather=weather, hair=hair, outfit=outfit, setting=setting)

PICK = {'food': 'w', 'code': 'm', 'design': 'w', 'gadget': 'm', 'home': 'w'}
for _mid in R:
    for _nid, _gg in PICK.items():
        _w, _m = R[_mid][_nid]
        R[_mid][_nid] = (_w, None) if _gg == 'w' else (None, _m)
R['us']['food'] = ('Hannah', 'Tyler')
for _m in R: R[_m]['glam'] = (None, None)
R['us']['glam'] = ('Brooke', None); R['pt']['glam'] = ('Leonor', None)

P = []
idx = 0
for m in M:
    for nid in ['food', 'code', 'design', 'bet', 'gadget', 'home', 'lang', 'glam']:
        w, mn = R[m['id']][nid]
        if nid == 'lang':
            P.append(build_persona(m['id'], nid, mn, w, idx)); idx += 1
        else:
            if w:
                P.append(build_persona(m['id'], nid, 'w', w, idx)); idx += 1
            if mn:
                P.append(build_persona(m['id'], nid, 'm', mn, idx)); idx += 1
assert len(P) == 76, len(P)

# episode plan for language niche
EPIS = [
 ('Season 1: Basics', ['Hello and goodbye', 'Please, thank you, sorry', 'Yes, no, I do not understand', 'Introduce yourself', 'Numbers 1 to 10', 'Order a coffee', 'How much is it?', 'Where is the station?', 'Asking for help', 'Recap and quiz']),
 ('Season 2: Eating and shopping', ['Menu words', 'Allergies and preferences', 'Order dinner', 'Pay the bill', 'At the market', 'Sizes and colours', 'Asking for a discount', 'Complimenting the food', 'Small talk about the weather', 'Recap and quiz']),
 ('Season 3: Getting around', ['Train tickets', 'Taxi and ride-hailing', 'Directions', 'Hotel check-in', 'Time and dates', 'Emergencies', 'Making plans', 'Texting slang', 'A mini conversation', 'Finale quiz']),
]

# ---------------------------------------------------------------- plan pages (blocks: h, p, list, steps, prompt, note)
def L(*a): return ('list', list(a))
def Pp(t): return ('p', t)
def H(t): return ('h', t)
def NT(t): return ('note', t)
def PR(title, t): return ('prompt', title, t)
def ST(*items): return ('steps', [list(i) for i in items])
def CD(*items): return ('cards', [list(i) for i in items])

PLAN = [
 dict(id='waves', title='Launch plan: pilot first', sub='Two personas, four weeks, then decide', icon='flag', blocks=[
  Pp('A 12 s talking video costs about 3,850 credits, so this plan starts small. Run a pilot with two personas, learn what works and what it costs, and only then add more.'),
  CD(('Pilot · weeks 1 to 4', 'Hannah (Healthy food, English US) and Ethan (Coding and AI, English US). Each posts about 2 clips a week: 1 talking video and 1 cheap format. Record views, follows, link clicks and credits spent per clip.'),
     ('Wave 1 · only if the pilot works', 'Tyler (weight loss food), Zoe (design), Brooke (glam and lifestyle, clearly labelled AI) and the Portuguese Ines, Diogo, Catarina and Leonor. Add 2 to 3 at a time, never all at once.'),
     ('Wave 2', 'Mason and Maya with their Shopify stores, Lily for language learning, and Rui, Joana and Sara in Portuguese. Open the store only after you have ordered and tested the first products.'),
     ('Wave 3', 'One betting persona only after a legal check in an allowed market, and only with real bets and real results.'),
     ('Wave 4', 'The remaining languages. Nordic ones last because voice quality is untested and they need native review.')),
  Pp('Every Pilot, Wave 1 and Wave 2 persona (15 in all) has a four-week plan on its own page, under Calendar, Topics and Setup: 12 connected topics, each with a teaser photo, a teaser story, the reel and a reel-is-live story that points to the product. The other personas get theirs when their wave starts.'),
  H('Move on when'),
  L('After about 8 clips a persona, you can see which hooks and formats get views, and what each clip cost in credits.', 'Keep a persona if people follow and click. Change the angle before you spend more on it.', 'Do not judge in 7 days: the 7-day challenge account that was written off later had a video pass 250,000 views.'),
  H('Credits and cost'),
  Pp('The full price list, plan comparison and monthly budgets are on the next page: Credits and cost.'),
  NT('Later languages to consider (general knowledge, not researched): Swedish, Dutch, Polish, Hindi and Indian English, Indonesian, Turkish, Arabic.'),
 ]),
 dict(id='cost', title='Credits and cost', sub='What each piece costs, which plan, monthly budgets', icon='bolt', blocks=[
  Pp('Numbers come from the first tutorial (screens shown in Oct 2026) and the OpenArt plan page (6 Nov 2026). They change, so trust the Generate button on your own screen. Figures marked "estimate" are my arithmetic, not shown on screen.'),
  H('What each thing costs'),
  CD(('Talking video · 3,850 credits', 'Seedance 2.5, 9:16, 1080p, 12 seconds, audio on. The voice is made inside the video, so there is no separate voice fee per clip. A 15 s video is about 4,800 (estimate).'),
     ('Photo · 245 credits', 'GPT Image 2.5, 4K, quality High. The character sheet is one such generation. Lower resolution or a lighter model should cost less; check the button.'),
     ('Character · no price shown', 'Creating and saving the character did not show a credit price. You are limited by the number of character slots in your plan.'),
     ('Voice · 250 credits, once', 'Designing a voice costs 1 credit per preview. Saving it costs 250 once, and it can be reused for other characters without paying again.'),
     ('Cheaper video settings', 'The model list shows Seedance 2.5 Draft at 480p (can be upgraded to 1080p within 7 days), 720p and 480p options, and Kling 4.0 marked 50% off. Their exact prices were not shown.')),
  H('Plans'),
  CD(('Starter · $14 a month ($13 annual)', '4,000 credits: about 1 talking video a month. Commercial use rights are not listed on this plan, so skip it for a monetized account. 13 characters.'),
     ('Plus · $34 ($27 annual)', '12,000 credits: about 3 talking videos a month. Commercial use rights. 40 characters. Credits can be added as needed.'),
     ('Pro · $56 ($44 annual)', '24,000 credits: about 6 talking videos a month. 80 characters, 32 parallel generations. Kling 4.0 50% off and GPT Image 2.6 30% off.'),
     ('Wonder · $240 ($175 annual)', '106,000 credits: about 27 talking videos a month. 353 characters, priority support, and "Unlimited Creation" (check which models it covers before counting on it).')),
  H('Cost of one 12 s talking video (estimate)'),
  L('Starter: about $13.50 monthly, $12.50 annual.', 'Plus: about $10.90 monthly, $8.70 annual.', 'Pro: about $9.00 monthly, $7.10 annual.', 'Wonder: about $8.70 monthly, $6.40 annual.', 'Expect at least one retry per clip, so double these for real planning.'),
  H('Budgets'),
  CD(('Setting up one persona', 'About 2,000 to 2,500 credits (estimate): character sheet, three photos with a few retries, and the 250 voice fee. Roughly $5 to $6 on Pro.'),
     ('Pilot: 2 personas, 4 weeks', 'Per persona per week: 1 talking video (3,850) and 1 cheap format (a photo with voiceover, about 250 to 750). About 17 talking videos and 17 cheap posts in the month would be about 65,000 credits without retries, or about 130,000 with them. Start with Wonder or Pro plus added credits, and cut to 1 talking video a week if the budget runs out.'),
     ('Wave 1: 7 more personas', 'At 3 talking videos a week each, one persona is about 50,000 credits a month (estimate). Seven personas is about 350,000, or about 450,000 with the two pilot personas: more than four Wonder plans. At 2 talking videos a week, about 300,000 for all nine. Add personas only as the budget and the results allow.')),
  H('Ways to spend less'),
  L('Preview in Draft 480p and upgrade only the winners within 7 days.', 'Use 6 second clips when a short line is enough: cost grows with length (estimate).', 'Mix formats: a photo with a slow push-in and a voiceover costs a fraction of a talking video.', 'Use 1K or 2K photos for references and 4K only for the final.', 'Try Kling 4.0 on Pro or Wonder while it is 50% off.', 'Make one video and post it on TikTok, Instagram and YouTube Shorts with three different captions.', 'Set a credit cap per persona per week and write down what each clip cost.'),
  H('Before you subscribe'),
  ST(('1. Read the real prices', 'In OpenArt, open each video and image setting you plan to use and note the number on the Generate button: 480p, 720p, 1080p, 6 s and 12 s, Draft, and Kling.'),
     ('2. Check the terms', 'Read the commercial-use terms and what Unlimited Creation includes.'),
     ('3. Start one month', 'Pick the smallest plan that covers the pilot, not the biggest. Switch only after you have measured real credits per clip.')),
 ]),
 dict(id='stages', title='Build a persona, step by step', sub='Stages 1 to 7 with prompts', icon='steps', blocks=[
  Pp('The same seven stages for every persona. Each persona page has its own filled-in prompts. Settings come from the tutorial (Oct 2026); if your screen differs, trust the screen.'),
  ST(('1. Design the character and first photo', 'In OpenArt: Image, GPT Image 2.5 (Sunburst for quality, Flare for speed), Auto Polish off, 4:5, 4K, quality High. Paste the photo prompt. The result should look like a casual phone photo, not a studio shoot.'),
     ('2. Name', 'One word, no spaces, no accents, easy to type. It becomes the @Name tag.'),
     ('3. Voice and backstory', 'Design a voice (Clone needs a recording). Test it on an ordinary sentence in the persona\'s language. Backstory: 3 to 4 sentences, no looks, clothes or places, or the character gets locked to one outfit or location.'),
     ('4. Create the character', 'Character, Create character, Start from an image, add the photo and name, add the voice, paste the backstory, Create.'),
     ('5. Character sheet', 'Three panels on gray: headless front, rear, face close-up. Then Character, Browse library, gear icon, Add additional angles.'),
     ('6. Photo set', 'Character image with @Name; three everyday moments in different places and clearly different outfits. Describe the outfit in full every time.'),
     ('7. Videos', 'Character video: Seedance 2.5, 9:16, 1080p, 12 s (15 s for explainers), audio on. Add the matching photo as @image1 to keep place and outfit. Run the hook step and the phonetic step first.')),
  H('Common problems'),
  L('Saved outfit or tote bag returns: the prompt lacked a full outfit description.', 'A different person appears: character not saved, or @Name missing.', 'Face not recognised: add a character sheet with a clear face close-up.', 'Stuck in one outfit or place: the backstory mentioned clothes or places.', 'Video changes place or outfit: add the matching photo as a second reference.', 'Voice sounds like an ad: ask for casual, unpolished wording and test an ordinary sentence.', 'A brand is mispronounced: redo the phonetic step.', 'Speech sounds translated: rewrite natively and get a native speaker to check.'),
 ]),
 dict(id='hooks', title='Hooks and stop-scroll', sub='The first 3 seconds of every video', icon='hook', blocks=[
  Pp('Based on common creator guides, not platform-confirmed rules. For every video Claude writes three hook variants in the persona\'s native register; you pick one. Viewers decide to swipe within about 3 seconds.'),
  H('Structure of each clip (15 to 45 seconds)'),
  ST(('Hook · 0 to 3 s', 'One sentence or image that makes the next second necessary.'), ('Bridge · 3 to 8 s', 'Promise what is coming and why it matters, without giving it away.'),
     ('Payoff', 'The recipe, build, redesign, test or lesson. Show the result.'), ('Soft close and loop', 'One low-pressure line; cut the end so it flows back into the first frame.')),
  H('Hook types to rotate'),
  CD(('Curiosity gap', 'State the result, hide the method.'), ('Contrarian', 'Challenge a common belief.'), ('Specific number', '"Four ingredients, nine minutes, 410 kcal."'), ('Mistake or warning', 'Name a costly error.'),
     ('Before and after', 'Show the end state first.'), ('Direct call-out', '"If you can\'t cook, watch this."'), ('Open loop', 'Start mid-story.'), ('Pattern interrupt', 'Sudden close-up or sound change.')),
  H('Stop-scroll techniques (use at least two)'),
  L('Visual: open on motion or a striking close-up; no logo, no slow fade-in, no "hi guys"; the result in the first second; eye contact.', 'Text: large, bold, high-contrast hook text in frame one, in the persona\'s language, inside the safe area; burned-in captions for the whole clip.', 'Audio: spoken hook in the first second, a sound change near 3 s, a trending sound where supported.', 'Pacing: a cut, zoom or new angle every 2 to 4 seconds; no dead air.'),
  H('Measure'),
  L('Share still watching at 3 seconds', 'Average watch time as a percent of length', 'Saves, shares and link clicks'),
  NT('If viewers leave before 3 seconds, change the hook, not the video. Test three hook variants. Never use a hook translated from English: write it as a native creator would say it.'),
 ]),
 dict(id='sell', title='Selling without selling', sub='Create desire without sounding like an ad', icon='tag', blocks=[
  Pp('Each video gives something useful first. The offer appears as the natural next step. The viewer should want the next thing, not be told to buy.'),
  H('Rotate three post types'),
  CD(('Value-first · about 60%', 'Useful tip, recipe, build, lesson or result. No offer, or only "more in my profile".'), ('Story · about 25%', 'A problem and how it was solved, with the product inside the story.'), ('Soft call to action · about 15%', 'The product in use plus one calm line.')),
  NT('The 60/25/15 split is a starting suggestion; the sources give no fixed ratio. Test it.'),
  H('Techniques'),
  L('Show, don\'t pitch: demonstrate the plan, app or before and after in use.', 'Normalize the mention: the offer is part of the routine.', 'Create the need first: make the viewer\'s problem vivid, then show the way out.', 'Answer the unspoken doubt: "does it work for a beginner?"', 'Open loops across a series: end Part 1 with the question Part 2 answers.', 'Real proof only: real screenshots, real results, honest limits.'),
  H('Soft call-to-action lines'),
  L('"The full plan is in my bio if you want it, no pressure."', '"I put the whole thing in one file, link\'s in my profile."', '"Part 2 tomorrow."'),
  NT('Avoid "Limited time only!" and "Don\'t miss out!" Disclose affiliate or paid content in the video and the description.'),
 ]),
 dict(id='desc', title='Descriptions per platform', sub='TikTok, Instagram Reels, YouTube Shorts', icon='text', blocks=[
  Pp('Claude writes all three for every video, three versions each, in the persona\'s language. Each persona page has an English draft for clip 1 and a ready-to-copy request for Claude.'),
  CD(('TikTok', 'Best length 15 to 60 s. First line: the hook plus the main keyword. 1 to 3 short lines and a question to trigger comments. 4 to 7 hashtags: 3 to 5 trending and relevant plus 1 or 2 niche. Use TikTok\'s AI-generated content label and "AI creator" in the profile.'),
     ('Instagram Reels', 'Best length 15 to 90 s. The hook goes before the "more" cut. 2 to 4 short lines with line breaks; a story or a save-worthy list. 5 to 10 niche hashtags at the end or in the first comment. Use the AI label setting and the Paid partnership label when it applies.'),
     ('YouTube Shorts', 'Under 60 s (up to 3 min). Searchable title with the main keyword; no hashtags in the title. Description 100 to 300 words, keywords used naturally, chapters if over 60 s. 3 to 5 hashtags including #Shorts. Turn on the altered or synthetic content disclosure; mention affiliate links.')),
  H('Rhythm and file'),
  L('From one guide (verify): TikTok and Reels 5 to 7 per week, Shorts 1 to 2 per day.', 'Upload the original full-resolution file, not a screen recording.', 'Keep key elements centred; Reels crop to 4:5 in the feed.'),
  H('Worked example · Healthy food, English (US)'),
  PR('TikTok', 'Seven dinners under 450 kcal and I only shopped once. Which day would you cook first? Part 2 tomorrow. Plan is in my profile. #mealprep #healthyrecipes #caloriedeficit #easydinner #aiinfluencer'),
  PR('Instagram', 'Dinner used to be my biggest calorie trap. So I planned the whole week in one shop: seven meals, every one under 450 kcal. Save this for your next grocery run. The full plan is linked in my profile. (I\'m an AI creator.) #mealprep #healthyrecipes #easydinners #caloriedeficit'),
  PR('YouTube Shorts title and description', '7 dinners under 450 kcal (one grocery trip)\n\nSeven simple dinners, each under 450 kcal, from one grocery trip. In this Short: the shopping list, the portions and the swap that cut the most calories. The complete printable week plan is linked below. I\'m an AI creator; the link is a product link where stated. #Shorts #mealprep #healthyrecipes #caloriedeficit'),
 ]),
 dict(id='nat', title='Naturality standard', sub='Looks, movement, speech', icon='eye', blocks=[
  Pp('Spotless means the same believable face every time, motion a viewer does not question, and speech a native speaker accepts as their own. Run this on every clip.'),
  H('Look'),
  L('Real imperfections (skin texture, freckles, flyaway hair), no beauty-filter gloss, Auto Polish off.', 'Phone-camera feel: candid framing, slight tilt, natural noise.', 'Local details that match the market: language on signs, plugs, cars, clothes for the weather, plausible local cafes and kitchens.', 'A full outfit description in every prompt.'),
  H('Movement'),
  L('Clips of 12 seconds or less, one action each, handheld or selfie style, at most one camera move.', 'Ask for the action second by second.', 'Check hands and fingers, blinking, eye line, teeth, jewellery flicker, background text, extra people, outfit continuity and audio glitches. Regenerate rather than fix.'),
  H('Speech'),
  L('One or two short sentences per 12-second clip, written the way people talk, not the way ads read.', 'Use the filler words and rhythm of the language, and have a native speaker confirm them.', 'Use the register a creator would use on camera, not textbook speech.'),
  NT('Before scaling any persona: make three sample clips, have a native speaker watch them with the sound on, save the persona bible, and re-check the pronunciation of every brand and foreign name. The tutorial only showed English; native voice quality in other languages is untested.'),
 ]),
 dict(id='brand', title='Brands and phonetic spelling', sub='Always ask before writing the final line', icon='mic', blocks=[
  Pp('Voice models mispronounce brand names, app names, acronyms and foreign words. Whenever a script names one, Claude stops and asks you how it should sound.'),
  ST(('List every risky word', 'Brands, product and app names, people\'s names, acronyms, URLs, prices and numbers.'),
     ('Ask one question per word', '"How should [brand] sound when [persona] says it in [language]?" Claude may suggest a spelling; you confirm it, because only a native speaker knows the local sound.'),
     ('Write the line with the confirmed spelling', 'Keep the correct spelling in the on-screen text or caption.'),
     ('Listen and fix', 'Report any word that still sounds wrong; regenerate only that clip.'),
     ('Keep a glossary per persona', 'Reuse it in later scripts.')),
  L('Write numbers and prices out in words in the spoken line.', 'Do not read web addresses aloud: say "link in bio" and show it on screen.', 'Show a real product only when the team bought and filmed it; otherwise plain unbranded props.', 'In language-learning episodes, give each new word a phonetic spelling too.'),
 ]),
 dict(id='rules', title='Rules and risks', sub='Checked 5 Nov 2026 · not legal advice', icon='shield', blocks=[
  NT('These come from web sources, not lawyers. Verify locally before launch.'),
  H('AI labelling and sponsored content'),
  CD(('United States', M[0]['ai']), ('European Union', 'AI Act Article 50 applies from 2 August 2026. Tool providers must mark AI output in machine-readable form; people making deepfakes must disclose it. Tools already on the market get until 2 December 2026 for the marking duty. Whether a fully invented person counts as a deepfake was not settled in the source, so label anyway.'),
     ('France', MK['fr']['ai']), ('UK, Norway, Brazil, Latin America', 'Not researched. Label the persona as AI and check the local advertising rules.')),
  H('Sports betting promotion by market'),
  CD(*[(m['name'], m['bet'][1]) for m in M]),
  H('Content rules wherever betting is used'),
  L('Real account, real bets, real outcomes including losses.', 'No claims that tips improve the chance of winning or guarantee profit.', 'Show the age limit and a responsible-gambling message.', 'Check the app and its promotion are legal in that market.', 'Disclose the affiliate link and that the persona is AI.'),
  H('Other'),
  L('Healthy food: kcal and portions as information, no extreme diets or medical promises.', 'Never base a persona on a real person\'s face or voice.', 'Check OpenArt\'s terms on commercial use of outputs and saved characters.', 'Check tax or business registration where you live.'),
 ]),
 dict(id='teaser', title='Adult-adjacent persona (women only)', sub='What is possible and what is not', icon='lock', blocks=[
  Pp('You asked for a women-only persona with more natural, more erotic videos to send visitors to a subscription page. I can help build a suggestive-but-not-explicit teaser persona. I will not write or plan explicit sexual content.'),
  H('Where the subscription page can live'),
  CD(('OnlyFans', 'One third-party source (checked 5 Nov 2026) reports that the October 2026 Terms require AI content to clearly feature the verified creator and prohibit wholly AI-generated accounts. A fully invented persona is likely not allowed. Verify with OnlyFans\' own terms or support.'),
     ('Fanvue', 'Its help page says fully AI virtual characters are allowed if you pass ID verification, label the account clearly as AI, never tell fans she is real, and the character looks clearly adult. It must not resemble a real identifiable person without documented consent. Verify the current wording.')),
  H('Where teasers can be posted'),
  L('TikTok bans content promoting sexual solicitation, including premium sexual content. A 2021 report said linking an OnlyFans from a profile got accounts banned; policies may have changed.', 'Instagram and YouTube restrict sexually suggestive content, nudity and adult-service promotion.', 'On those three platforms the persona stays lifestyle-level and does not mention, link or hint at an adult page where the rules forbid it.', 'No coded wording, hidden links or other ways around moderation.'),
  H('The persona'),
  L('Clearly an adult woman (25 or older in appearance), an invented face, no real person\'s likeness.', 'Warm, confident, flirty personality; everyday settings; natural movement and speech.', 'Clearly labelled as AI in the bio and with each platform\'s AI label.', 'Suggestive means styling, framing and personality at roughly PG-13 level.'),
  H('Keep out'),
  L('Anything that could read as a minor.', 'Deepfakes or content from other people\'s photos.', 'Claims she is a real woman, or fake private messages.', 'Explicit content: I will not write it, and image tools usually restrict it.'),
  NT('Brooke (US) and Leonor (Portugal) are now in Wave 1, with a 12-topic plan and a location bible. Read the current rules of the subscription site and each posting platform before the first link, and keep the AI label on.'),
 ]),
 dict(id='caveats', title='Honest expectations', sub='What the tutorials really showed', icon='scale', blocks=[
  L('The only real-money result: 23 workbook sales at $12 = $276 revenue, minus $19.52 payment fees and a $99 tool plan = $157.48 profit in a week, short of the author\'s $1,000 goal.', 'Both tutorials carry affiliate links and one is sponsored. Results shown are curated; real work includes retries and wasted credits.', 'Label every account as AI. Do not present generated people, testimonials or sponsored content as a real person\'s genuine experience.', 'Not covered by the tutorials: OpenArt\'s commercial terms, each platform\'s current rules for AI accounts, and tax rules.'),
  H('Strategy from the 7-day challenge'),
  L('Research first: study existing AI accounts and how they earn.', 'Make the character distinctive, not generic.', 'Test several accounts, about 10 videos each, and compare.', 'Ways to earn: brand deals (slow), physical products, affiliate (quick), digital products (a structured workbook sold for $12 and linked from the bio).', 'Use the persona to gain attention, then put one offer in front of that audience through the bio link.'),
 ]),
 dict(id='week', title='First-week plan', sub='Five steps to start', icon='calendar', blocks=[
  ST(('1. Check credits and terms', 'Read the Credits and cost page, check the Generate prices on your screen, and pick a pilot persona and a distinctive character concept.'), ('2. Build the character', 'Stages 1 to 5. Save the persona bible.'),
     ('3. Make content', 'Three photos, one talking video from a photo, one selfie video. Run the hook step, the naturality checklist and the phonetic step. Write the three platform descriptions.'),
     ('4. Create the account', 'AI label and a clear bio. Post 2 to 4 clips over the week, with captions, mixing one talking video and cheaper formats.'),
     ('5. Review', 'After a week, note which hooks and video types got views. Only then choose how the persona earns.')),
 ]),
]

for n in N: n['research'] = RS.NICHE.get(n['id'])
for m in M: m['research'] = RS.MARKET.get(m['id'])

PLAN.insert(0, dict(id='research', title='Research: what works now', sub='Algorithm, labels, what sells. Sources inside', icon='bolt', blocks=[
  Pp('Collected on 7 Nov 2026 from web sources. Many are vendor or agency blogs, so treat the numbers as signals to test, not facts. Each niche and each language page has its own research section with sources.'),
  H('What the platforms reward'), L(*RS.GLOBAL['algo']),
  H('AI labels'), L(*RS.GLOBAL['labels']),
  H('How people sell'), L(*RS.GLOBAL['sell']),
  H('What this changes in our plan'),
  L('Clips are 12 seconds because of cost. The research favours 15 to 30 seconds for products and 30 to 60 for reach. Options: stitch two clips, or use voiceover over b-roll, which was the best-performing hook type for food.',
    'Food: weekly menus and budget meal prep replace three single-recipe topics. Recipes stay, but they are no longer the whole plan.',
    'Every reel ends with a comment-a-keyword line, so the free resource goes out by DM and the paid product follows by email.',
    'Tyler cannot use a transformation story. His credibility comes from the maths, the recipes and the tools.',
    'Gadgets and home depend on a registered company in the selling country and on TikTok Shop status, which is unclear in Portugal and absent in the Nordics.'),
  ('src', [list(x) for x in RS.GLOBAL['src']]),
]))
BANKS = dict(food=bank_food, shred=bank_shred, code=bank_code, design=bank_design, gadget=bank_gadget, home=bank_home, lang=bank_lang, glam=bank_glam)
BANK = {k: dict(topics=m.TOPICS, intro=m.INT) for k, m in BANKS.items()}
for k, v in BANK.items(): assert len(v['topics']) == 12, k
def bank_key(p): return 'shred' if (p['niche'] == 'food' and p['g'] == 'm') else p['niche']
for p in P:
    p['plan'] = bool(p['wave'] <= 2 and p['mkt'] in ('us', 'pt') and bank_key(p) in BANK)
    p['bank'] = bank_key(p)
out = dict(markets=M, niches=N, personas=P, plan=[{k: v for k, v in s.items()} for s in PLAN], epis=EPIS, bank=BANK)
json.dump(out, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('personas', len(P), 'bytes', len(json.dumps(out, ensure_ascii=False)))
