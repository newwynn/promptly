import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database import Base, SQLALCHEMY_DATABASE_URL
import database.models as models

def recreate_db():
    # Wait a moment to ensure any existing connections are closed
    time.sleep(1)
    
    # Remove existing database file if it exists
    db_file = "sql_app.db"
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
            print(f"Removed existing database: {db_file}")
        except Exception as e:
            print(f"Warning: Could not remove {db_file}: {e}")
    
    # Create new engine and session
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    
    # Drop all tables (in case they exist)
    print("Dropping existing tables...")
    Base.metadata.drop_all(bind=engine)
    
    # Create all tables
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    print("Database recreated successfully!")

if __name__ == "__main__":
    recreate_db()
