from sqlmodel import create_engine, Session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import AsyncAdaptedQueuePool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname")

# Create async engine and session maker (deferred initialization)
def get_engine():
    return create_async_engine(
        DATABASE_URL,
        poolclass=AsyncAdaptedQueuePool,
        echo=False  # Set to False in production
    )

def get_session_maker():
    engine = get_engine()
    return async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

# Dependency to get async session
async def get_async_session():
    session_local = get_session_maker()
    async with session_local() as session:
        yield session


# Alias for compatibility with routes
get_session = get_async_session