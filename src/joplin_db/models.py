# coding: utf-8
from sqlalchemy import Column, Integer, LargeBinary, Numeric, Table, Text, text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Alarm(Base):
    __tablename__ = 'alarms'

    id = Column(Integer, primary_key=True)
    note_id = Column(Text, nullable=False, index=True)
    trigger_time = Column(Integer, nullable=False)


class DeletedItem(Base):
    __tablename__ = 'deleted_items'

    id = Column(Integer, primary_key=True)
    item_type = Column(Integer, nullable=False)
    item_id = Column(Text, nullable=False)
    deleted_time = Column(Integer, nullable=False)
    sync_target = Column(Integer, nullable=False, index=True)


class Folder(Base):
    __tablename__ = 'folders'

    id = Column(Text, primary_key=True)
    title = Column(Text, nullable=False, index=True, server_default=text("\"\""))
    created_time = Column(Integer, nullable=False)
    updated_time = Column(Integer, nullable=False, index=True)
    user_created_time = Column(Integer, nullable=False, server_default=text("0"))
    user_updated_time = Column(Integer, nullable=False, index=True, server_default=text("0"))
    encryption_cipher_text = Column(Text, nullable=False, server_default=text("\"\""))
    encryption_applied = Column(Integer, nullable=False, index=True, server_default=text("0"))
    parent_id = Column(Text, nullable=False, server_default=text("\"\""))


class ItemChange(Base):
    __tablename__ = 'item_changes'

    id = Column(Integer, primary_key=True)
    item_type = Column(Integer, nullable=False, index=True)
    item_id = Column(Text, nullable=False, index=True)
    type = Column(Integer, nullable=False)
    created_time = Column(Integer, nullable=False, index=True)
    source = Column(Integer, nullable=False, server_default=text("1"))
    before_change_item = Column(Text, nullable=False, server_default=text("\"\""))


class KeyValue(Base):
    __tablename__ = 'key_values'

    id = Column(Integer, primary_key=True)
    key = Column(Text, nullable=False, unique=True)
    value = Column(Text, nullable=False)
    type = Column(Integer, nullable=False)
    updated_time = Column(Integer, nullable=False)


class MasterKey(Base):
    __tablename__ = 'master_keys'

    id = Column(Text, primary_key=True)
    created_time = Column(Integer, nullable=False)
    updated_time = Column(Integer, nullable=False)
    source_application = Column(Text, nullable=False)
    encryption_method = Column(Integer, nullable=False)
    checksum = Column(Text, nullable=False)
    content = Column(Text, nullable=False)


class Migration(Base):
    __tablename__ = 'migrations'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    updated_time = Column(Integer, nullable=False)
    created_time = Column(Integer, nullable=False)


class NoteResource(Base):
    __tablename__ = 'note_resources'

    id = Column(Integer, primary_key=True)
    note_id = Column(Text, nullable=False, index=True)
    resource_id = Column(Text, nullable=False, index=True)
    is_associated = Column(Integer, nullable=False)
    last_seen_time = Column(Integer, nullable=False)


class NoteTag(Base):
    __tablename__ = 'note_tags'

    id = Column(Text, primary_key=True)
    note_id = Column(Text, nullable=False, index=True)
    tag_id = Column(Text, nullable=False, index=True)
    created_time = Column(Integer, nullable=False)
    updated_time = Column(Integer, nullable=False, index=True)
    user_created_time = Column(Integer, nullable=False, server_default=text("0"))
    user_updated_time = Column(Integer, nullable=False, index=True, server_default=text("0"))
    encryption_cipher_text = Column(Text, nullable=False, server_default=text("\"\""))
    encryption_applied = Column(Integer, nullable=False, index=True, server_default=text("0"))


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Text, primary_key=True)
    parent_id = Column(Text, nullable=False, server_default=text("\"\""))
    title = Column(Text, nullable=False, index=True, server_default=text("\"\""))
    body = Column(Text, nullable=False, server_default=text("\"\""))
    created_time = Column(Integer, nullable=False)
    updated_time = Column(Integer, nullable=False, index=True)
    is_conflict = Column(Integer, nullable=False, index=True, server_default=text("0"))
    latitude = Column(Numeric, nullable=False, server_default=text("0"))
    longitude = Column(Numeric, nullable=False, server_default=text("0"))
    altitude = Column(Numeric, nullable=False, server_default=text("0"))
    author = Column(Text, nullable=False, server_default=text("\"\""))
    source_url = Column(Text, nullable=False, server_default=text("\"\""))
    is_todo = Column(Integer, nullable=False, index=True, server_default=text("0"))
    todo_due = Column(Integer, nullable=False, server_default=text("0"))
    todo_completed = Column(Integer, nullable=False, server_default=text("0"))
    source = Column(Text, nullable=False, server_default=text("\"\""))
    source_application = Column(Text, nullable=False, server_default=text("\"\""))
    application_data = Column(Text, nullable=False, server_default=text("\"\""))
    order = Column(Integer, nullable=False, index=True, server_default=text("0"))
    user_created_time = Column(Integer, nullable=False, server_default=text("0"))
    user_updated_time = Column(Integer, nullable=False, index=True, server_default=text("0"))
    encryption_cipher_text = Column(Text, nullable=False, server_default=text("\"\""))
    encryption_applied = Column(Integer, nullable=False, index=True, server_default=text("0"))
    markup_language = Column(Integer, nullable=False, server_default=text("1"))


t_notes_fts = Table(
    'notes_fts', metadata,
    Column('id', NullType),
    Column('title', NullType),
    Column('body', NullType)
)


class NotesFtsDocsize(Base):
    __tablename__ = 'notes_fts_docsize'

    docid = Column(Integer, primary_key=True)
    size = Column(LargeBinary)


class NotesFtsSegdir(Base):
    __tablename__ = 'notes_fts_segdir'

    level = Column(Integer, primary_key=True, nullable=False)
    idx = Column(Integer, primary_key=True, nullable=False)
    start_block = Column(Integer)
    leaves_end_block = Column(Integer)
    end_block = Column(Integer)
    root = Column(LargeBinary)


class NotesFtsSegment(Base):
    __tablename__ = 'notes_fts_segments'

    blockid = Column(Integer, primary_key=True)
    block = Column(LargeBinary)


class NotesFtsStat(Base):
    __tablename__ = 'notes_fts_stat'

    id = Column(Integer, primary_key=True)
    value = Column(LargeBinary)


t_notes_normalized = Table(
    'notes_normalized', metadata,
    Column('id', Text, nullable=False, index=True),
    Column('title', Text, nullable=False, server_default=text("\"\"")),
    Column('body', Text, nullable=False, server_default=text("\"\""))
)


class ResourceLocalState(Base):
    __tablename__ = 'resource_local_states'

    id = Column(Integer, primary_key=True)
    resource_id = Column(Text, nullable=False, index=True)
    fetch_status = Column(Integer, nullable=False, index=True, server_default=text("\"2\""))
    fetch_error = Column(Text, nullable=False, server_default=text("\"\""))


class Resource(Base):
    __tablename__ = 'resources'

    id = Column(Text, primary_key=True)
    title = Column(Text, nullable=False, server_default=text("\"\""))
    mime = Column(Text, nullable=False)
    filename = Column(Text, nullable=False, server_default=text("\"\""))
    created_time = Column(Integer, nullable=False)
    updated_time = Column(Integer, nullable=False)
    user_created_time = Column(Integer, nullable=False, server_default=text("0"))
    user_updated_time = Column(Integer, nullable=False, server_default=text("0"))
    file_extension = Column(Text, nullable=False, server_default=text("\"\""))
    encryption_cipher_text = Column(Text, nullable=False, server_default=text("\"\""))
    encryption_applied = Column(Integer, nullable=False, server_default=text("0"))
    encryption_blob_encrypted = Column(Integer, nullable=False, server_default=text("0"))
    size = Column(Integer, nullable=False, server_default=text("-1"))


class ResourcesToDownload(Base):
    __tablename__ = 'resources_to_download'

    id = Column(Integer, primary_key=True)
    resource_id = Column(Text, nullable=False, index=True)
    updated_time = Column(Integer, nullable=False, index=True)
    created_time = Column(Integer, nullable=False)


class Revision(Base):
    __tablename__ = 'revisions'

    id = Column(Text, primary_key=True)
    parent_id = Column(Text, nullable=False, index=True, server_default=text("\"\""))
    item_type = Column(Integer, nullable=False, index=True)
    item_id = Column(Text, nullable=False, index=True)
    item_updated_time = Column(Integer, nullable=False, index=True)
    title_diff = Column(Text, nullable=False, server_default=text("\"\""))
    body_diff = Column(Text, nullable=False, server_default=text("\"\""))
    metadata_diff = Column(Text, nullable=False, server_default=text("\"\""))
    encryption_cipher_text = Column(Text, nullable=False, server_default=text("\"\""))
    encryption_applied = Column(Integer, nullable=False, server_default=text("0"))
    updated_time = Column(Integer, nullable=False, index=True)
    created_time = Column(Integer, nullable=False)


class Setting(Base):
    __tablename__ = 'settings'

    key = Column(Text, primary_key=True)
    value = Column(Text)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class SyncItem(Base):
    __tablename__ = 'sync_items'

    id = Column(Integer, primary_key=True)
    sync_target = Column(Integer, nullable=False, index=True)
    sync_time = Column(Integer, nullable=False, index=True, server_default=text("0"))
    item_type = Column(Integer, nullable=False, index=True)
    item_id = Column(Text, nullable=False, index=True)
    sync_disabled = Column(Integer, nullable=False, server_default=text("\"0\""))
    sync_disabled_reason = Column(Text, nullable=False, server_default=text("\"\""))
    force_sync = Column(Integer, nullable=False, server_default=text("0"))
    item_location = Column(Integer, nullable=False, server_default=text("1"))


class TableField(Base):
    __tablename__ = 'table_fields'

    id = Column(Integer, primary_key=True)
    table_name = Column(Text, nullable=False)
    field_name = Column(Text, nullable=False)
    field_type = Column(Integer, nullable=False)
    field_default = Column(Text)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Text, primary_key=True)
    title = Column(Text, nullable=False, index=True, server_default=text("\"\""))
    created_time = Column(Integer, nullable=False)
    updated_time = Column(Integer, nullable=False, index=True)
    user_created_time = Column(Integer, nullable=False, server_default=text("0"))
    user_updated_time = Column(Integer, nullable=False, index=True, server_default=text("0"))
    encryption_cipher_text = Column(Text, nullable=False, server_default=text("\"\""))
    encryption_applied = Column(Integer, nullable=False, index=True, server_default=text("0"))


t_tags_with_note_count = Table(
    'tags_with_note_count', metadata,
    Column('id', Text),
    Column('title', Text),
    Column('created_time', Integer),
    Column('updated_time', Integer),
    Column('note_count', NullType)
)


t_version = Table(
    'version', metadata,
    Column('version', Integer, nullable=False)
)
