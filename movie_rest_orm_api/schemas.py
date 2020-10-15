"""
schema.py : model to be converted in json by fastapi
"""
from typing import Optional, List
from datetime import date

from pydantic import BaseModel

# common Base Class for Stars (abstract class)
class StarBase(BaseModel):
    name: str
    birthdate: Optional[date]

# item witout id, only for creation purpose
class StarCreate(StarBase):
    pass

# item from database with id
class Star(StarBase):
    id: int

    class Config:
        orm_mode = True

#nb de film, année 1er film, année dernier film avec seuil minimum de nb de films
# from BaseModel because dont want birthdate in output
class StarStat(BaseModel):
    name:str
    movie_count:int
    first_movie_year:int
    last_movie_year:int

class StarRecord(BaseModel):
    name:str
    movie_count:int
    worst:int
    best:int


# common Base Class for Movies (abstract class)
class MovieBase(BaseModel):
    title: str
    year: int
    duration: Optional[int]

# movies witout id, only for creation purpose
class MovieCreate(MovieBase):
    pass

# movies from database with id
class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True

# movies from database with director
class MovieDetail(Movie):
    director: Optional[Star] = None
    actors: List[Star] = []
    
    
class MovieStat(MovieBase):
    year:int
    count:int
    min_:int
    max_:int
    avg:int
    

    
    
    
        
