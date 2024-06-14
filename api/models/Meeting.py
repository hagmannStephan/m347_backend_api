class Meeting:

    _last_id = 1    # Set to 0 if meetings_data gets cleared

    def __init__(self, description: str, Businesstrip_idBusinesstrip: int, title: str):
        Meeting._last_id += 1
        self.idMeeting = Meeting._last_id
        self.description = description
        self.Businesstrip_idBusinesstrip = Businesstrip_idBusinesstrip
        self.title = title

    def to_dict(self):
        return {
            'idMeeting': self.idMeeting,
            'description': self.description,
            'Businesstrip_idBusinesstrip': self.Businesstrip_idBusinesstrip,
            'title': self.title
        }
