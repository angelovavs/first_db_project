from sqlalchemy import inspect
from alchemy import Base, engine

#conn = engine.connect()


inspector = inspect(engine)
schemas = inspector.get_schema_names()

for schema in schemas:
    print("schema: %s" % schema)
    for table_name in inspector.get_table_names(schema=schema):
        print('table_name:', table_name)
        #for column in inspector.get_columns(table_name, schema=schema):
         #   print("Column: %s" % column)