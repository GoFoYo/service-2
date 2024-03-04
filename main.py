# SQLAlchemy setup
DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
# Define the ProcessedAgentData table
processed_agent_data = Table(
"processed_agent_data",
metadata,
Column("id", Integer, primary_key=True, index=True),
Column("road_state", String),
Column("x", Float),
Column("y", Float),
Column("z", Float),
Column("latitude", Float),
Column("longitude", Float),
Column("timestamp", DateTime),
)