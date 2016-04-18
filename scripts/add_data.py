from app.models import *

cs = Contestant.objects.all()
for c in cs:
    c.delete()
hs = Haircut.objects.all()
for h in hs:
    h.delete()

nick = Contestant.objects.create(
    first_name="Nick",
    last_name="Karlow",
    bio="here",
    photo="asdf/ddsgg.png")

jake = Contestant.objects.create(
    first_name="Jake",
    last_name="Groenendyk",
    bio="here",
    photo="asdf/ddsgg.png")

derek = Contestant.objects.create(
    first_name="Derek",
    last_name="Schloemann",
    bio="here",
    photo="asdf/ddsgg.png")

Haircut.objects.create(
    name="Mutton Chops",
    description="Hilarious too look at but not too absurd",
    contestant=derek,
    photo="/static/haircuts/mutton_chops.jpg",
    goal_amount=100)

Haircut.objects.create(
    name="Rent is too Damn High",
    description="Okay, Now we are getting silly",
    contestant=derek,
    photo="/static/haircuts/rent_too_high.jpg",
    goal_amount=500)

Haircut.objects.create(
    name="Captain Long Beard",
    description="Argh Matey",
    contestant=derek,
    photo="/static/haircuts/pirate.jpg",
    goal_amount=1000)

Haircut.objects.create(
    name="Super Sayan",
    description="And I thought I was just having a bowel movement...",
    contestant=jake,
    photo="/static/haircuts/dbz.png",
    goal_amount=100)

Haircut.objects.create(
    name="Two Face",
    description="Live or die, at the flip of a coin",
    contestant=jake,
    photo="/static/haircuts/two_face.jpg",
    goal_amount=500)

Haircut.objects.create(
    name="Mohawk",
    description="My hair doubles as a carpentry blade",
    contestant=jake,
    photo="/static/haircuts/mohawk.jpg",
    goal_amount=1000)

Haircut.objects.create(
    name="Almost Normal",
    description="Can you see?",
    contestant=nick,
    photo="/static/haircuts/almost_normal.jpg",
    goal_amount=100)

Haircut.objects.create(
    name="Half-shaved",
    description="Waiting..",
    contestant=nick,
    photo="/static/haircuts/asdf.jpg",
    goal_amount=500)

Haircut.objects.create(
    name="Ring-Around",
    description="the rosie...",
    contestant=nick,
    photo="/static/haircuts/ring_around.jpg",
    goal_amount=1000)





















