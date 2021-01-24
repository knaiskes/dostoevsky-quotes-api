from django.db import models

class Quote(models.Model):
    POOR_FOLK = 'Poor Folk'
    THE_DOUBLE = 'The Double'
    THE_LANDLADY = 'The Landlady'
    NETOCHKA_NEZVANOVA = 'Netochka Nezvanova'
    UNCLES_DREAM = "Unclue's Dream"
    THE_VILLAGE_OF_STEPANCHIKOVO = 'The Village of Stepanchikovo'
    HUMILIATED_AND_INSULTED = 'Humiliated and Insulted'
    THE_HOUSE_OF_THE_DEAD = 'The House of the Dead'
    NOTES_FROM_UNDERGROUND = 'Notes from Underground'
    CRIME_AND_PUNISHMENT = 'Crime and Punishment'
    THE_GAMBLER = 'The Gambler'
    THE_IDIOT = 'The Idiot'
    THE_ETERNAL_HUSBAND = 'The Eternal Husband'
    THE_POSSESSED = 'The Possessed'
    THE_ADOLESCENT = 'The Adolescent'
    THE_BROTHERS_KARAMAZOV = 'The Brothers Karamazon'

    NOVEL_LIST_CHOICES = [
        (POOR_FOLK, 'Poor Folk'),
        (THE_DOUBLE, 'The Double'),
        (THE_LANDLADY, 'The Landlady'),
        (NETOCHKA_NEZVANOVA, 'Netochka Nezvanova'),
        (UNCLES_DREAM, "Unclue's Dream"),
        (THE_VILLAGE_OF_STEPANCHIKOVO, 'The Village of Stepanchikovo'),
        (HUMILIATED_AND_INSULTED, 'Humiliated and Insulted'),
        (THE_HOUSE_OF_THE_DEAD, 'The House of the Dead'),
        (NOTES_FROM_UNDERGROUND, 'Notes from Underground'),
        (CRIME_AND_PUNISHMENT, 'Crime and Punishment'),
        (THE_GAMBLER, 'The Gambler'),
        (THE_IDIOT, 'The Idiot'),
        (THE_ETERNAL_HUSBAND, 'The Eternal Husband'),
        (THE_POSSESSED, 'The Possessed'),
        (THE_ADOLESCENT, 'The Adolescent'),
        (THE_BROTHERS_KARAMAZOV, 'The Brothers Karamazon'),
    ]

    text = models.CharField(max_length=120, unique=True)
    novel = models.CharField(max_length=28, choices=NOVEL_LIST_CHOICES)

    def __str__(self):
        return self.text
