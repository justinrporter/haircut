# -*- coding: utf-8 -*-

from app.models import Contestant, Donation, Haircut

c = Contestant.objects.create(
    first_name="Nick",
    last_name="Karlow",
    bio="William O'Connell Bradley (1847–1914) was the 32nd Governor of Kentucky and a U.S. senator. The first Republican to serve as governor of the state, he became known as the father of the Republican Party in Kentucky.",
    photo="asdf/ddsgg.png")

Haircut.objects.create(
    name="Flock of Seagulls",
    description="ridiculous back-combed haircut",
    contestant=c,
    photo="addd/sdfdsdsd.png",
    goal_amount=550)

Haircut.objects.create(
    name="Buzzcut",
    description="no hair",
    contestant=c,
    photo="addd/sdfdsdsd.png",
    goal_amount=50)

Donation.objects.create(
    transaction_id='asdfee13234231ddsfd',
    email="asdf@ggg.com",
    amount=10,
    contestant=c)

Donation.objects.create(
    transaction_id='asdfee13235231ddsfd',
    email="another_one@ggg.com",
    amount=15,
    contestant=c)