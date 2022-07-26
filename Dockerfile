FROM ubuntu
RUN apt update -y
RUN apt install -y python python3-pip
RUN pip install uvicorn fastapi asyncpg loguru loguru aiosql bcrypt passlib pydantic[email] jwt pypika slugify pydantic[dotenv] pydantic alembic psycopg2-binary
ADD . /app
#ADD alembic.ini /app/app/alembic.ini
#ADD /app/db/migrations /app/app/db/migrations
#ADD sleep.py /app
WORKDIR /app
CMD ["python3", "sleep.py"]