
class Movie:
    'Information about a Movie'

    name = ''
    ID = ''
    actorIDs = []
    average = 0

    def __init__(self, name, ID, actorIDs):
        self.name = name
        self.ID = ID
        self.actorIDs = actorIDs

    def __str__(self):
        template = 'Name="{0}", ID="{1}" ActorIDs={2} Average={3}'
        return template.format(self.name.encode('utf-8'),
                               self.ID,
                               self.actorIDs,
                               self.average)

    def ComputeAverageAge():
        return None
