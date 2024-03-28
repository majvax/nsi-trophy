


class Season:
    def __init__(self, season: int):
        """

        Args:
            season ([int]): [in YYYY format]
        """
        if not isinstance(season, int):
            raise ValueError("Season must be an integer")
        
        if len(str(season)) != 4:
            raise ValueError("Season must be in YYYY format")
        
        self.season = season

    def __str__(self) -> str:
        return str(self.season)
    
    def __repr__(self) -> str:
        return f"Season({self.season})"
    