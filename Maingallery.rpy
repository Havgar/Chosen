default persistent.gallerySusan = False
default persistent.galleryNamaah = False
default persistent.galleryCaroline = False
default persistent.galleryStacy = False
default persistent.galleryJennifer = False
default Gallerytime = True

screen Maingallery:

    tag menu



    add gui.gallery_background

    hbox:



        yalign 0.26
        xalign 0.8

        use gallery_navigation




        #This will show the screen gallery_navigation from gallery_navigation.rpy


        grid 4 2:
            spacing 25

            button:
                if persistent.galleryNamaah == True:
                     imagebutton auto "images/UI/Thumbnails/Namaah_%s.webp" action ShowMenu("galleryNamaah") focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")

            button:
                if persistent.galleryCaroline :
                     imagebutton auto "images/UI/Thumbnails/Caroline_%s.webp" action ShowMenu("galleryCaroline") focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")

            button:
                if persistent.gallerySusan :
                     imagebutton auto "images/UI/Thumbnails/Susan_%s.webp" action ShowMenu("gallerySusan") focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")


            button:
                if persistent.galleryStacy :
                     imagebutton auto "images/UI/Thumbnails/Stacy_%s.webp" action ShowMenu("galleryStacy") focus_mask True
                else:
                     image ("images/UI/Thumbnails/Locked.webp")

            button:
                if persistent.galleryJennifer :
                     imagebutton auto "images/UI/Thumbnails/Jennifer_%s.webp" action ShowMenu("galleryJennifer") focus_mask True
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


label Gallerynames:

    $ persistent.Hannahrelation = Hannahrelation

    $ persistent.Carolinerelation = Carolinerelation

    $ persistent.Jenniferrelation = Jenniferrelation

    $ persistent.povname = povname

    return
