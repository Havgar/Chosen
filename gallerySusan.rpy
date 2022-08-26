default persistent.Susanblow1 = False


screen gallerySusan:



    tag menu

    add gui.gallery_background


    hbox:


        use gallery_navigation



        yalign 0.2
        xalign 0.8





        grid 4 1:
            spacing 25

            button:
                if persistent.Susanblow1 == True:
                     imagebutton auto "images/UI/Thumbnails/Susanblow1_%s.webp" action Replay("Susanblowg", locked=False) focus_mask True
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
