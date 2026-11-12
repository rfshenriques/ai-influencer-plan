# The Make tab: one production line, organised by step (not by persona). Prompts are filled for the persona and topic chosen on screen.
# Block types: p (text), h (heading), list, warn, prompt(title, persona field), beats (one prompt per beat of the chosen topic), scenes.
MAKE = [
 dict(id='setup', title='Set up once', sub='Accounts, plan, rules', credits='No credits', blocks=[
  ('p', 'Do this once for the whole business, then repeat steps 1 to 10 for each persona and topic.'),
  ('list', [
   'Higgsfield plan: Ultra is EUR 129 for 3,000 credits (6K is EUR 220, 9K is EUR 310). Check the price and credits on your own screen before paying.',
   'In Higgsfield note the number on the Generate button for: a Nano Banana Pro image, a character sheet (8 credits), a Gemini Omni Flash clip (its price was not on the page I read), a video swap (112 credits for 15 s, 720p 9:16) and a motion transfer (63 credits).',
   'On your iPhone make one album per persona: 1 Reference, 2 Avatar, 3 Clips, 4 Final. Name files with the persona and the topic number.',
   'Instagram: create the account, then turn on the "AI-generated profile" label. Instagram renamed its AI creator label to this and cuts the reach of AI profiles that do not use it. The sources I read do not give the exact menu path, so use the account settings or Instagram help and check that the label shows on the profile.',
   'Keep the label on for every persona, always. Realism here means natural-looking, not hidden: the point is that people enjoy the video, not that they believe the person is real.']),
  ('warn', 'Three hard rules: never base a persona on a real person, never show an AI person as a doctor, nurse or other professional, and never write "I tried it" or "it worked for me" about something the persona cannot have done. Gadget and home personas only review what you ordered and tested yourself.'),
 ]),
 dict(id='ref', title='Reference photo (shoot your own)', sub='The step most people skip', credits='0 credits', blocks=[
  ('p', 'Why: an AI face made from nothing has no pores, no grain and no tiny imperfections, so when it moves it looks waxy and people feel it is fake. A real iPhone photo already carries those details. The video you sent says this step should take about half of the whole effort.'),
  ('h', 'Shoot it'),
  ('prompt', 'Reference photo brief (for you or a friend)', 'ref'),
  ('list', [
   'Framing: decide on purpose. Camera at eye level or chest height, person close enough to the phone that a small microphone would pick up the voice.',
   'Light: soft daylight from a window. Some shine on the forehead is fine, but if any area is pure white with no detail, take the photo again. White areas have no data, so the video turns them into a glossy mask.',
   'Background: not empty and not busy. A few objects with some space behind the person (a plant, a lamp, a shelf), so the room has a personality.',
   'No captions or text in the frame, and both hands visible if possible.']),
  ('h', 'What we do instead of copying a TikTok creator'),
  ('p', 'The video downloads a stranger\'s TikTok clip and changes the face. We do not. A real person\'s video can carry their likeness, their room, their style and a copyright, and the creator can recognise it. Use only: your own photo, a friend who agreed in writing, or a licensed photo whose licence allows AI edits (read it first). The image is only a source for framing, light and grain.'),
  ('warn', 'If you only have a licensed stock photo, check the licence text for AI modification. If you are not sure, shoot your own: it takes ten minutes with your iPhone.'),
 ]),
 dict(id='avatar', title='Build the avatar image', sub='One prompt, many tries', credits='About 20 credits (10 images at 2)', blocks=[
  ('p', 'Open Higgsfield, Image, Nano Banana Pro (the original Pro, not Nano Banana 2). The video says GPT Image 2.x makes faces look too perfect, which is the opposite of what we want. Attach your best reference photo, paste the prompt, set 9:16, and generate.'),
  ('prompt', 'Avatar prompt (one shot)', 'photo'),
  ('list', [
   'Generate 8 to 12 versions. Do not edit one result again and again: every edit repaints pixels and brings back the plastic look. Change the prompt and generate again instead.',
   'The new person must not be the person in the reference. The prompt changes the face, eye colour, hair and details on purpose.',
   'Accept only an image that passes this check: visible pores; grain; a slightly asymmetric face; no shine that is pure white; hair with flyaways; accessories look natural (one earbud, a watch); a visible small microphone or the phone close to the face; the background has a personality.',
   'About 1 reference in 10 will not animate well even when it looks good. Then go back to the photo, do not fight the video model.']),
 ]),
 dict(id='sheet', title='Character sheet and voice', sub='Lock the identity', credits='8 credits', blocks=[
  ('p', 'Attach the avatar you chose and generate the character sheet (8 credits on your screen). Save the avatar and the sheet as the persona\'s character in Higgsfield, or in the album if the app does not offer saving.'),
  ('prompt', 'Character sheet (16:9)', 'sheet'),
  ('h', 'Voice'),
  ('prompt', 'Voice description (add to every video prompt)', 'voice'),
  ('list', [
   'Test the voice on one clip with a normal sentence in the persona\'s language before anything else.',
   'Gemini Omni Flash on Higgsfield lists English, Spanish, French, German, Portuguese and others with regional accents. I could not confirm European Portuguese or the Nordic languages, so have a native speaker listen to three clips.',
   'If Higgsfield accepts an audio file with the video (the page says MP3 or WAV up to 30 s), attach the audio from the first approved clip to the next ones to keep the same voice. Test that it works.']),
 ]),
 dict(id='lock', title='Lock the video prompt', sub='Three parts, then only change the line', credits='3 test clips', blocks=[
  ('p', 'This is the prompt structure from the video: PART 1 the scene, PART 2 the dialogue, PART 3 the fixed rules. You spend time on it now, once per persona, and afterwards you only swap the line.'),
  ('lockprompt', 'Locked video prompt (beat 1 of the chosen topic)'),
  ('h', 'Tune it'),
  ('list', [
   'Attach the avatar image. Set 9:16, native 720p, audio on, and the shortest length that fits the line (see the next step).',
   'Generate 3 takes of the same line. Judge them harshly with sound on.',
   'For each problem, add one sentence to PART 3 and generate again. Examples: "Higher energy, faster pace." / "Smile slightly at the start and the end." / "More confident, less flat." / "Speaks at a natural speed, not slow." / "Keep the camera still, no drift."',
   'Camera: if the person holds the phone and walks, change PART 1 to "Handheld UGC iPhone shot with slight natural movement". If you do not say how the camera moves, the model drifts and makes things up.',
   'When one take feels right, freeze PART 1 and PART 3. From now on only the line in PART 2 changes.']),
 ]),
 dict(id='clips', title='Make the three clips', sub='One prompt per beat of the topic', credits='3 clips per reel', blocks=[
  ('p', 'Each beat is a clip where the person speaks and shows the thing at the same time. The prompts below are filled with the topic chosen at the top. Paste each one with the avatar attached.'),
  ('beats',),
  ('h', 'Length, pacing and stress'),
  ('list', [
   'The video says its model offers 4, 6, 8 and 10 s clips. Higgsfield\'s page for Gemini Omni Flash says the default clip is 8 s and longer clips are built in 10 s steps, so check the lengths on your screen.',
   'If the line fits between two lengths, pick the longer one and add a short throwaway sentence at the end (it is suggested below). The model paces the real line properly, and you cut the extra at the edit.',
   'Stress: capital letters make the voice stress that word. The suggested capital is a starting point. If it sounds wrong, move the capital to another word and generate again.',
   'Write numbers and brand names the way they are spoken. Ask Claude for the phonetic spelling when the line has a brand name or a foreign word.',
   'Save each approved clip as beat1, beat2, beat3 in the persona\'s album.']),
 ]),
 dict(id='scene', title='Change of scene (optional)', sub='A second position or place, same person', credits='2 credits per still; 63 credits for a motion transfer', blocks=[
  ('p', 'The video adds a scene change: the same person in a new position near the end. Make the new still first with Nano Banana Pro, then make the clip with the same locked prompt using that still.'),
  ('scenes',),
  ('h', 'Motion transfer with your own footage (optional)'),
  ('p', 'Use it when the person must move (walk, point, put something down) and not speak. Film yourself on your iPhone doing the action for 10 to 15 s, then use the motion transfer with the avatar as the character. On your screen it costs 63 credits at 9:16, 720p. Use only footage you filmed or have rights to, never another creator\'s clip.'),
  ('prompt', 'Motion transfer prompt', 'motion'),
 ]),
 dict(id='check', title='Realism check', sub='Approve or reject each clip', credits='0 credits', blocks=[
  ('p', 'Watch each clip on your iPhone, full screen, with sound on, before you edit. Reject it if any of these is true.'),
  ('list', [
   'The skin looks smooth or glossy, or the forehead shines white.',
   'The teeth or the eyes change shape while talking, or the eyes do not blink.',
   'The mouth does not match the words, or the voice sounds like an announcer.',
   'The hands have the wrong number of fingers or melt into the object.',
   'The face, hair, outfit, accessories or room differ from the avatar.',
   'The camera drifts, zooms or cuts in a clip that should be one take.',
   'The accent is wrong for the market (a native speaker listens to three clips).',
   'The line promises a result, a price or a feeling the persona cannot have had.']),
  ('p', 'Fix order when something is wrong: first the line, then PART 3 of the prompt, and only then the avatar image. The video\'s own rule: it is cheaper and faster to regenerate images than to scrap videos.'),
 ]),
 dict(id='edit', title='Edit and export', sub='On your iPhone', credits='0 credits', blocks=[
  ('list', [
   'Use CapCut or iMovie on your iPhone. Put beat 1, 2 and 3 on one timeline, in order. Cut the throwaway sentence at the end of each clip.',
   'Total length: 20 to 25 s. Beat 1 is the hook and the first second must show the result or the number.',
   'Captions: highlighted subtitles, large, in the language of the line. Check every word.',
   'Sound: keep the person\'s voice. No music in the file. Add a trending in-app sound at low volume inside Instagram or TikTok after upload, if you want.',
   'Keep it simple: one message per reel, no fast flashing cuts. The video argues that clear delivery beats hyper-edited videos.',
   'Export vertical 1080 x 1920. If the clips are 720p, upscale in the editor or in Higgsfield (1080p upscale is a separate step).',
   'Do not strip the file\'s metadata. Gemini Omni Flash outputs carry an invisible watermark and content credentials, and we want platforms to see an honestly labelled AI video.']),
 ]),
 dict(id='post', title='Publish with the AI label on', sub='Caption, label, rhythm', credits='0 credits', blocks=[
  ('list', [
   'Check that the profile still shows "AI-generated profile". If an upload offers an "AI info" or "AI-generated" toggle, switch it on.',
   'Add "(AI creator)" or "AI-generated" in the caption of the first reel of each topic, and keep it in the bio.',
   'Use the caption and sticker text from the Plan tab for this topic (teaser day, reel day, reel-is-live story, carousel, silent re-cut).',
   'Ask for the comment keyword and send the free resource by DM, then the $9 PDF.',
   'Do not post the clip on a second account or as if it were a real person.']),
  ('warn', 'The sources I read cover the profile-level label. They do not say that every single post needs its own label, so we add the caption note ourselves.'),
 ]),
 dict(id='learn', title='After 48 hours', sub='What to look at', credits='0 credits', blocks=[
  ('list', [
   'Look at: hook rate (the first 3 seconds), completion, saves and shares, comments with the keyword, link clicks.',
   'If the video looks great but gets nothing, change the script, not the avatar. The video says the script and message decide the result and the format cannot save a bad one.',
   'Write down which hook, which topic and what it cost in credits. Repeat what worked and change one thing at a time.']),
 ]),
]

# Short, one-action-per-line version of each step (shown first, big). The long text above is kept under "Why and details".
FOCUS = {
 'setup': ('Get your tools ready. You only do this once.', [
   'Open Higgsfield and pick the Ultra plan',
   'Write down the credit price of an image, a clip and the sheet',
   'Make one album per persona on your iPhone',
   'Create the Instagram account',
   'Turn on the "AI-generated profile" label']),
 'ref': ('Take one real iPhone photo of the room and pose.', [
   'Copy the photo brief below',
   'Stand by a window. Flash off',
   'Normal Photo mode, not Portrait',
   'Take 10 photos. Move your hands a little',
   'Check that nothing is pure white',
   'Keep the best 2 in the Reference album']),
 'avatar': ('Turn your photo into the persona\'s face.', [
   'Open Higgsfield, Image, Nano Banana Pro',
   'Attach your best reference photo',
   'Paste the avatar prompt below. Choose 9:16',
   'Generate 8 to 12 versions',
   'Pick the most real one: pores, grain, no shine',
   'Save it in the Avatar album']),
 'sheet': ('Lock the face and the voice.', [
   'Attach the avatar. Paste the sheet prompt. Choose 16:9',
   'Generate it (8 credits) and save it',
   'Copy the voice text into your Notes app',
   'Portuguese personas: plan a native speaker check later']),
 'lock': ('Make one test clip feel right. Then never change the prompt again.', [
   'Open Gemini Omni Flash in Higgsfield',
   'Attach the avatar. Paste the locked prompt',
   'Choose 9:16 and sound on',
   'Generate 3 takes of the same line',
   'Write down what is wrong: energy, speed, smile',
   'Add one fix sentence to PART 3 for each problem',
   'Generate again until one take feels right',
   'Save the final prompt in Notes']),
 'clips': ('Make the three clips of this topic.', [
   'Attach the avatar',
   'Paste the Clip 1 prompt and generate',
   'Watch it with sound on',
   'Do the same for Clip 2',
   'Do the same for Clip 3',
   'Save them as beat1, beat2, beat3']),
 'scene': ('Optional. Skip it on your first reel.', [
   'Paste prompt A in Nano Banana Pro with the avatar',
   'Pick the best still',
   'Use it as the first image of a clip']),
 'check': ('Decide if each clip is good enough.', [
   'Watch each clip full screen with sound',
   'Skin: not glossy, no white shine',
   'Face and outfit: same as the avatar',
   'Mouth matches the words, hands look normal',
   'Camera does not drift or zoom',
   'Redo any clip that fails']),
 'edit': ('Put the three clips into one reel.', [
   'Open CapCut on your iPhone',
   'Put the three clips in order',
   'Cut the extra throwaway sentences',
   'Keep the reel between 20 and 25 seconds',
   'Add large captions',
   'Export 1080 x 1920']),
 'post': ('Post it with the AI label on.', [
   'Check the AI label shows on the profile',
   'Paste the caption from the Plan tab',
   'Add "(AI creator)" to the first caption',
   'Post it',
   'Answer keyword comments with the DM']),
 'learn': ('Look at the numbers after 2 days.', [
   'Wait 48 hours',
   'Check hook rate, completion, saves, shares',
   'Write one thing to change next time']),
}
for _s in MAKE:
    _s['goal'], _s['do'] = FOCUS[_s['id']]
