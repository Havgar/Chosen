default persistent.Stacyhandjob = False
default persistent.Stacyfinger = False
default Stacyfuckg = False
default Stacypoundinggallery = False

screen galleryStacy:

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
                if persistent.Stacyhandjob == True:
                     imagebutton auto "images/UI/Thumbnails/Stacyhandjob_%s.webp" action Replay("Stacyhandjobg", locked=False) focus_mask True
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
