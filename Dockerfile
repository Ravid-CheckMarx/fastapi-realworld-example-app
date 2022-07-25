FROM ubuntu
RUN apt update -y
RUN apt install -y python python3-pip
RUN pip install uvicorn fastapi asyncpg loguru loguru aiosql bcrypt passlib pydantic[email] jwt pypika slugify pydantic[dotenv] pydantic
ADD dist /app
WORKDIR /app
CMD ["python3", "main.py"]