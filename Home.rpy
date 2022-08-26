image Room_morning = "images/BG/Room_morning.webp"
image Room_afternoon = "images/BG/Room_afternoon.webp"
image Room_evening = "images/BG/Room_evening.webp"
image Room_night = "images/BG/Room_night.webp"
image Namaahfirstcall1 = "images/Namaah/Namaahfirstcall1.webp"
image Namaahfirstcall2 = "images/Namaah/Namaahfirstcall2.webp"
image Namaahfirstcall3 = "images/Namaah/Namaahfirstcall3.webp"
image Namaahfirstcall4 = "images/Namaah/Namaahfirstcall4.webp"
image Namaahcall1 = "images/Namaah/Namaahcall1.webp"




label home:

    $ persistent.Home = True

    $ persistent.School = False

    if clock.time == "Morning":

        scene Room_morning

    elif clock.time == "Noon":

        scene Room_afternoon

    elif clock.time == "Evening":

        scene Room_evening

    elif clock.time == "Night":

        scene Room_night

    call screen homeUI



label Jenroom:

    if Quest4 == True and clock.time == "Evening":
        jump Jenniferbeforedildo
    elif Quest6 == True and clock.time == "Evening" and dildo == 1:
        jump Jenniferdildo
    elif Quest9 == True and clock.time == "Noon" or clock.time == "Morning" and clock.weekday == "Sunday" or clock.weekday == "Saturday":
        jump Jenniferafterdildo
    elif clock.time == "Morning":
        "Nobody is here"
        if persistent.School:
            jump school
        elif persistent.Home:
            jump home
    elif clock.time == "Noon":
        "Nobody is here"
        if persistent.School:
            jump school
        elif persistent.Home:
            jump home
    elif clock.time == "Evening":
        "Nobody is here"
        if persistent.School:
            jump school
        elif persistent.Home:
            jump home
    elif clock.time == "Night":
        "It's locked"
        if persistent.School:
            jump school
        elif persistent.Home:
            jump home
