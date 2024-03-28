


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



ALL_SEASON = [
    Season(1950),
    Season(1951),
    Season(1952),
    Season(1953),
    Season(1954),
    Season(1955),
    Season(1956),
    Season(1957),
    Season(1958),
    Season(1959),
    Season(1960),
    Season(1961),
    Season(1962),
    Season(1963),
    Season(1964),
    Season(1965),
    Season(1966),
    Season(1967),
    Season(1968),
    Season(1969),
    Season(1970),
    Season(1971),
    Season(1972),
    Season(1973),
    Season(1974),
    Season(1975),
    Season(1976),
    Season(1977),
    Season(1978),
    Season(1979),
    Season(1980),
    Season(1981),
    Season(1982),
    Season(1983),
    Season(1984),
    Season(1985),
    Season(1986),
    Season(1987),
    Season(1988),
    Season(1989),
    Season(1990),
    Season(1991),
    Season(1992),
    Season(1993),
    Season(1994),
    Season(1995),
    Season(1996),
    Season(1997),
    Season(1998),
    Season(1999),
    Season(2000),
    Season(2001),
    Season(2002),
    Season(2003),
    Season(2004),
    Season(2005),
    Season(2006),
    Season(2007),
    Season(2008),
    Season(2009),
    Season(2010),
    Season(2011),
    Season(2012),
    Season(2013),
    Season(2014),
    Season(2015),
    Season(2016),
    Season(2017),
    Season(2018),
    Season(2019),
    Season(2020),
    Season(2021),
    Season(2022),
    Season(2023),
    Season(2024),
]