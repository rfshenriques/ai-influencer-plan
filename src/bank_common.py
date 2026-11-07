"""Helpers for the content-plan banks. Every text field may be a plain string/list or an {en, pt} pair."""

def X(en, pt):
    return {'en': en, 'pt': pt}

def R(t, k, tech, h, sh, ot, s, te, se, g=None):
    """Reel. t title, k format, tech stop-scroll technique, h hook X, sh beats list (or X), ot on-screen text list (or X),
    s spoken script X, te what we show/teach, se soft sell line X, g 'w'/'m' for gender-specific."""
    d = dict(t=t, k=k, tech=tech, h=h, sh=sh, ot=ot, s=s, te=te, se=se)
    if g: d['g'] = g
    return d

def P(t, img, why, cap, g=None):
    """Photo post. img describes the frame, why is the reason it is on the grid, cap is an X caption."""
    d = dict(t=t, img=img, why=why, cap=cap)
    if g: d['g'] = g
    return d

def S(t, frames, sticker, goal, q=None, g=None):
    """Story set. frames are 3 to 4 frame descriptions, sticker the interaction, goal why, q optional X question text."""
    d = dict(t=t, fr=frames, st=sticker, go=goal)
    if q: d['q'] = q
    if g: d['g'] = g
    return d
