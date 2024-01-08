import os
import pathlib
from dotenv import load_dotenv
load_dotenv()

apiToken = os.getenv("apiToken")
base_dir = pathlib.Path(__file__).parent
cmds_dir = base_dir / "cogs"
