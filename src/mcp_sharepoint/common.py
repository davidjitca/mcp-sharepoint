# common.py

import os
import logging
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Logging setup
logger = logging.getLogger('mcp_sharepoint')
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# Load environment variables
load_dotenv()

SHP_SITE_URL = os.getenv('SHP_SITE_URL')
SHP_CLIENT_ID = os.getenv('SHP_CLIENT_ID')
SHP_TENANT_ID = os.getenv('SHP_TENANT_ID')
SHP_DOC_LIBRARY = os.getenv('SHP_DOC_LIBRARY')
SHP_SITE_BASE_URL = os.getenv("SHP_SITE_BASE_URL", "")

SHAREPOINT_WEB_VIEW_PREFIX = f"{SHP_SITE_URL}/Shared%20Documents/Forms/AllItems.aspx?id="

# Validate config
if not SHP_SITE_URL or not SHP_CLIENT_ID or not SHP_TENANT_ID:
    raise ValueError("Missing SharePoint auth configuration.")

# Only initialize FastMCP here
mcp = FastMCP(
    name="mcp_sharepoint",
    instructions=f"This server provides tools to interact with SharePoint at {SHP_SITE_URL}"
)