from django.db import models

class Quote(models.Model):
    CRIME_AND_PUNISHMENT = 'Crime and Punishment'
    HUMILIATED_AND_INSULTED = 'Humiliated and Insulted'
    NETOCHKA_NEZVANOVA = 'Netochka Nezvanova'
    NOTES_FROM_UNDERGROUND = 'Notes from Underground'
    POOR_FOLK = 'Poor Folk'
    THE_ADOLESCENT = 'The Adolescent'
    THE_BROTHERS_KARAMAZOV = 'The Brothers Karamazon'
    THE_DOUBLE = 'The Double'
    THE_ETERNAL_HUSBAND = 'The Eternal Husband'
    THE_GAMBLER = 'The Gambler'
    THE_HOUSE_OF_THE_DEAD = 'The House of the Dead'
    THE_IDIOT = 'The Idiot'
    THE_LANDLADY = 'The Landlady'
    THE_POSSESSED = 'The Possessed'
    THE_VILLAGE_OF_STEPANCHIKOVO = 'The Village of Stepanchikovo'
    UNCLES_DREAM = "Unclue's Dream"

    NOVEL_LIST_CHOICES = [
    (CRIME_AND_PUNISHMENT, 'Crime and Punishment'),
    (HUMILIATED_AND_INSULTED, 'Humiliated and Insulted'),
    (NETOCHKA_NEZVANOVA, 'Netochka Nezvanova'),
    (NOTES_FROM_UNDERGROUND, 'Notes from Underground'),
    (THE_ADOLESCENT, 'The Adolescent'),
    (THE_BROTHERS_KARAMAZOV, 'The Brothers Karamazon'),
    (THE_DOUBLE, 'The Double'),
    (THE_ETERNAL_HUSBAND, 'The Eternal Husband'),
    (THE_GAMBLER, 'The Gambler'),
    (THE_HOUSE_OF_THE_DEAD, 'The House of the Dead'),
    (THE_IDIOT, 'The Idiot'),
    (THE_LANDLADY, 'The Landlady'),
    (THE_POSSESSED, 'The Possessed'),
    (THE_VILLAGE_OF_STEPANCHIKOVO, 'The Village of Stepanchikovo'),
    (UNCLES_DREAM, "Unclue's Dream"),
    (POOR_FOLK, 'Poor Folk'),
    ]

    text = models.CharField(max_length=120, unique=True)
    novel = models.CharField(max_length=28, choices=NOVEL_LIST_CHOICES)

    def __str__(self):
        return self.text
