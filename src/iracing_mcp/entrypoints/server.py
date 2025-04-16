"""iRacing MCP server entrypoint."""

import os
from typing import Any

from iracingdataapi.client import irDataClient
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("iRacing Data", dependencies=["iracingdataapi"])


@mcp.tool()
def get_iracing_profile_stats() -> dict[str, Any]:
    """Get the current iRacing profile statistics.

    Retrieves the user's iRacing profile information including license level,
    iRating, and other career stats.
    """
    username = os.environ.get("IRACING_USERNAME")
    password = os.environ.get("IRACING_PASSWORD")

    if not username or not password:
        raise ValueError("IRACING_USERNAME and IRACING_PASSWORD environment variables must be set")

    client = irDataClient(username, password)

    member_info = client.member_info()

    career_stats = client.stats_member_career(member_info["cust_id"])

    return {"profile": member_info, "career_stats": career_stats}


@mcp.tool()
def get_irating_chart(category: int) -> dict[str, Any]:
    """Get the iRating data for a specific license category.

    Retrieves the user's iRating history data for the specified racing category.
    This includes historical iRating values that can be used for charting.

    1 is oval, 2 is road, 3 is dirt oval, 4 is dirt road, 5 is sports car, and 6 is formula car.
    """
    username = os.environ.get("IRACING_USERNAME")
    password = os.environ.get("IRACING_PASSWORD")

    if not username or not password:
        raise ValueError("IRACING_USERNAME and IRACING_PASSWORD environment variables must be set")

    client = irDataClient(username, password)

    member_info = client.member_info()
    cust_id = member_info["cust_id"]

    chart_data = client.member_chart_data(cust_id=cust_id, category_id=category)

    return chart_data


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
