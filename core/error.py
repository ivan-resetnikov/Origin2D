import core.term as term



CORRECT_USE = f"{term.fg.green}[✓] Correct use:{term.fg.reset}"
DOC_LINK = f"{term.fg.purple}[Q] Documentation link:"



INIT_CALLBACK_NOT_ASSIGNED = \
f"""Initialisation callback function was not assigned

{CORRECT_USE}
 | 
 | {term.fg.gray}main_scene = core.Scene({term.fg.reset}
 | {term.fg.cyan}    callback_init=scenes.main_menu.init,{term.fg.reset}
 | {term.fg.gray}    callback_update=scenes.main_menu.update,{term.fg.reset}
 | {term.fg.gray}    callback_draw=scenes.main_menu.draw,{term.fg.reset}
 | {term.fg.gray}    name="example_scene"){term.fg.reset}
 | 

{DOC_LINK}
https://github.com/ivan-reshetnikov/Origin2D/docs/window.html#draw-callback
"""

UPDATE_CALLBACK_NOT_ASSIGNED = \
f"""Update callback function was not assigned

{CORRECT_USE}
 | 
 | {term.fg.gray}main_scene = core.Scene({term.fg.reset}
 | {term.fg.gray}    callback_init=scenes.main_menu.init,{term.fg.reset}
 | {term.fg.cyan}    callback_update=scenes.main_menu.update,{term.fg.reset}
 | {term.fg.gray}    callback_draw=scenes.main_menu.draw,{term.fg.reset}
 | {term.fg.gray}    name="example_scene"){term.fg.reset}
 | 

{DOC_LINK}
https://github.com/ivan-reshetnikov/Origin2D/docs/window.html#draw-callback
"""

DRAW_CALLBACK_NOT_ASSIGNED = \
f"""Draw callback function was not assigned

{CORRECT_USE}
 | 
 | {term.fg.gray}main_scene = core.Scene({term.fg.reset}
 | {term.fg.gray}    callback_init=scenes.main_menu.init,{term.fg.reset}
 | {term.fg.gray}    callback_update=scenes.main_menu.update,{term.fg.reset}
 | {term.fg.cyan}    callback_draw=scenes.main_menu.draw,{term.fg.reset}
 | {term.fg.gray}    name="example_scene"){term.fg.reset}
 | 

{DOC_LINK}
https://github.com/ivan-reshetnikov/Origin2D/docs/window.html#draw-callback
"""