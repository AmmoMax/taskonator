import sqlalchemy


def create_database_schema(engine: sqlalchemy.engine.Engine, schema: str) -> None:
    with engine.connect() as connection:
        if not engine.dialect.has_schema(connection, schema):
            connection.execute(sqlalchemy.schema.CreateSchema(schema))
            connection.commit()
