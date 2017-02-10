#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, DateTime
import sqlalchemy
import sqlalchemy.ext.declarative

@sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

Base = sqlalchemy.ext.declarative.declarative_base()

class MirrorCheckResult(Base):
    __tablename__          = 'mirrorcheckresult'
    id                     = Column(Integer, primary_key=True)

    site                   = Column(String, nullable=False, unique=True)
    last_test              = Column(DateTime, nullable=False)
    last_noerror           = Column(DateTime)

    trace_master_timestamp = Column(DateTime)
    error                  = Column(String)
    warning                = Column(String)