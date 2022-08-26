default persistent.Jenniferdildo = False
default persistent.Jenniferboobjob = False


screen galleryJennifer:



    tag menu

    add gui.gallery_background


    hbox:


        use gallery_navigation



        yalign 0.2
        xalign 0.8





        grid 4 1:
            spacing 25

            button:
                if persistent.Jenniferdildo == True:
                     imagebutton auto "images/UI/Thumbnails/Jenniferdildo1_%s.webp" action Replay("Jenniferdildog", locked=False) focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")

            button:
                if persistent.Jenniferboobjob == True:
                     imagebutton auto "images/UI/Thumbnails/Jenniferboobjob1_%s.webp" action Replay("Jenniferboobjobg", locked=False) focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")

            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")


            button:
                action Replay("")
                image ("images/UI/Thumbnails/Black.webp")
