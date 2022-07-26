from alembic.config import Config
from alembic import command


while True:
    try:
        alembic_cfg = Config("alembic.ini")
        command.current(alembic_cfg, verbose=True)
        command.upgrade(alembic_cfg, "head")
        break
    except Exception:
        print("try again")

import uvicorn
from app.main import my_app
uvicorn.run(my_app, host='0.0.0.0')
