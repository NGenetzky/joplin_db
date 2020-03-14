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

    uuids = []

    # Make queries to find all Items in the database
    folders = session.query(Folder).all()
    for folder in folders:
        uuids.append(folder.id)

    logger.debug("uuids is returning {} values".format(len(uuids)))
    folders_str = '\n'.join(sorted(uuids))
    print(folders_str)
    return folders_str
