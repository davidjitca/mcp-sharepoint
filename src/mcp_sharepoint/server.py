# server.py

import asyncio
from .common import logger, mcp, SHP_SITE_URL, SHP_TENANT_ID, SHP_CLIENT_ID
from office365.sharepoint.client_context import ClientContext

async def main():
    logger.info("Starting SharePoint MCP server ...")

    # Authenticate with SharePoint interactively
    logger.info("Authenticating with SharePoint...")
    try:
        # sp_context = ClientContext(SHP_SITE_URL).with_certificate(
        # me = sp_context.web.current_user.get().execute_query()
        # logger.info(f"Authenticated as: {me.login_name}")
        cert_credentials = {
            "tenant": SHP_TENANT_ID,
            "client_id": SHP_CLIENT_ID,
            "thumbprint": "096C5B14584886B417AF9F2DE3C0AF7A45872448",
            "cert_path": "./mcp_sharepoint/privatekey.pem",
        }
        sp_context = ClientContext(SHP_SITE_URL).with_client_certificate(**cert_credentials)
        current_web = sp_context.web.get().execute_query()

    except Exception as e:
        logger.exception("Failed to authenticate with SharePoint")
        raise

    # 🔑 Inject sp_context where needed
    from . import tools
    from . import resources
    resources.init(sp_context)


    # ✅ Start MCP server AFTER everything is ready
    logger.info("Running MCP server...")
    await mcp.run_stdio_async()

if __name__ == "__main__":
    asyncio.run(main())
