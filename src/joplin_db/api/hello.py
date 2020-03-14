""" Implement the uuids command.

"""
from ..core.logger import logger
from ..models import Base, Folder

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main(data) -> str:
    """ Execute the command.
    
    :param data: Directory contain joplin database and files
    """
    engine = create_engine('sqlite:///database.sqlite') # TODO
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    # Make a query to find all Persons in the database
    folders = session.query(Folder).all()

    for folder in folders:
        print(str(folder.title))

    folders_str = '\n'.join(str(folders))
    logger.debug("executing uuids command")
    return folders_str
