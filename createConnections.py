from dataclasses import dataclass
import random
import config

@dataclass
class participant:
    name: str
    email: str
    secretSanta: str
    hasGiver: bool

def createAssociations():
    validAssociations = True
    participants = []
    # create participants array with just player name and email
    for player in config.player_info:
        participants.append(participant(player, config.player_info[player], '', False))

    # match participant with another to create secret santa associations
    for person in participants:
        matched = False
        checkedAmt = 0
        while (not matched):
            recip = participants[random.randint(0,len(participants)-1)]
            if (recip.hasGiver == False):
                if (recip.name != person.name):
                    person.secretSanta = recip.name
                    recip.hasGiver = True
                    matched = True
            checkedAmt += 1

            # break condition incase of infinite loop
            if (checkedAmt > 100):
                validAssociations = False
                break

    if (validAssociations):
        return True, participants
    else:
        return False, []

# create participants array and infinitely call until each player has unique
# secret santa
participants = []
while(True):
    breakCond, participants = createAssociations()
    if (breakCond):
        break

# Test print
# for participant in participants:
#     print(participant.name, "has", participant.secretSanta)
