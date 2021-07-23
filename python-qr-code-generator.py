import qrcode
img = qrcode.make("https://www.youtube.com/channel/UCMUSIgtI6otfdIVm6flvNWA")
img.save("myyoutubechannel.jpg")