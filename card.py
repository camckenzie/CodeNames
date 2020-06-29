class Card:
    
    """This is a card."""

    def __init__(self, text: str, team: str, click: str = 'N') -> 'Card':
        self._text = text
        self._team = team
        self._click = click

    def getText(self) -> str:
        return self._text
    
    def setText(self, new_text) -> None:
        self._text = new_text

    def getTeam(self) -> str:
        return self._team
    
    def setTeam(self, new_team) -> None:
        self._team = new_team

    def getClick(self) -> str:
        return self._click
    
    def setClick(self, new_click) -> None:
        self._click = new_click