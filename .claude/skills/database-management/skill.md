## Skill: Database Management & ORM
## Description: Managing Data Persistence using SQLModel and Neon Postgres.

technologies:
  orm: "SQLModel"
  database: "PostgreSQL (Neon Serverless)"
  migrations: "Alembic"

guidelines:
  - "Define models inheriting from `SQLModel`."
  - "Use `table=True` for database tables and `table=False` for Pydantic schemas."
  - "Always use asynchronous sessions (`AsyncSession`) for database interaction."
  - "Never hardcode database credentials; use `.env` files."

workflow:
  1. Define Model in Python code.
  2. Generate Migration Script (`alembic revision --autogenerate`).
  3. Apply Migration (`alembic upgrade head`).