default persistent.MCDomtoggle = False

label MCTitle:

    $ povtitle = renpy.input("{size=+1}{font=Charm-Bold.ttf}You can pick a title to be called, or just retype your name. What'll it be?{/font}{/size}", length = 32)

    $ persistent.povtitle = povtitle

    return
