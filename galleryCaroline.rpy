$ persistent.Carolineboobjob1 = False
$ persistent.Carolinehandjob1 = False


screen galleryCaroline:



    tag menu

    add gui.gallery_background



    hbox:


        use gallery_navigation



        yalign 0.2
        xalign 0.8





        grid 4 1:
            spacing 25

            button:
                if persistent.Carolineboobjob1 == True:
                     imagebutton auto "images/UI/Thumbnails/Carolineboobjob1_%s.webp" action Replay("Carolineboobjobg", locked=False) focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")

            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")


            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")


            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")
