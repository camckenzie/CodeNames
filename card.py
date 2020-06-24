class Card:
    
    """This is a card."""

    def __init__(self, text: str, team: str = 'neutral') -> 'Card':
        self._text = text
        self._team = team

    def getText(self) -> str:
        return self._text
    
    def setText(self, new_text) -> None:
        self._text = new_text

    def getTeam(self) -> str:
        return self._team
    
    def setTeam(self, new_team) -> None:
        self._team = new_team
