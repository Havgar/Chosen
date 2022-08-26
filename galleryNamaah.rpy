default persistent.Namaahfootjob1 = False
default persistent.Namaahfuck1 = False
default Namaahboobjobg = False
default Namaahtitfuckg = False


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
                if persistent.Namaahfootjob1 == True:
                     imagebutton auto "images/UI/Thumbnails/Namaahfootjob1_%s.webp" action Replay("Namaahfootjobg", locked=False) focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")

            button:
                if persistent.Namaahfuck1 == True:
                     imagebutton auto "images/UI/Thumbnails/Namaahfuck1_%s.webp" action Replay("Namaahfuckg", locked=False) focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")

            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")


            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")
