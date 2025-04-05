from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.types import Integer, Unicode, UnicodeText
from sqlalchemy.schema import ForeignKey

engine = create_engine("postgresql://postgres:!P@ssw0rd@localhost/test3")
metadata = MetaData()

countries_table = Table("countries",
                        metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', Unicode(255)),
                        Column('code', Unicode(255)))

indicators_table = Table("indicators",
                         metadata,
                         Column('id', Unicode(255), primary_key=True),
                         Column('name', Unicode(255)))

data_table = Table("data",
                   metadata,
                   Column('country_id', ForeignKey("countries.id")),
                   Column('indicator', ForeignKey("indicators.id")),
                   Column('data', UnicodeText))
metadata.create_all(engine)
# OR
# countries_table.create(engine)
# indicators_table.create(engine)
# data_table.create(engine)
