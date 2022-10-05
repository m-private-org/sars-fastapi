import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from ..config import settings

# if we are running in a GCP environment, use the unix socket
gcp_service_account = settings.GCP_SERVICE_ACCOUNT
if gcp_service_account:
    unix_socket_path = f"/cloudsql/{gcp_service_account}"
    db_query = {"unix_socket": unix_socket_path}
else:
    db_query = None

engine = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=settings.DB_USER,
            password=settings.DB_PASS,
            database=settings.DB_NAME,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            query=db_query,
        )
    )


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
