$ persistent.Namaahfootjob1 = False
$ persistent.Namaahfuck1 = False


screen galleryNamaah:

    tag menu

    add gui.gallery_background

    hbox:

        yalign 0.2
        xalign 0.8


        #This will show the screen gallery_navigation from gallery_navigation.rpy
        use gallery_navigation

        grid 4 1:
            spacing 25

            button:
                action If(persistent.Namaahfootjob1, Replay("Namaahfootjob1", locked=False))
                if persistent.Namaahfootjob1 :
                     image ("images/UI/Thumbnails/Namaahfootjob1.webp")
                else:
                     image ("images/CGs/small/locked.jpg")

            button:
                action If(persistent.Namaahfuck1, Replay("Namaahfuck1", locked=False))
                if persistent.Namaahfuck1 :
                     image ("images/UI/Thumbnails/Namaahfuck1.webp")
                else:
                     image ("images/CGs/small/locked.jpg")

            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")


            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")
