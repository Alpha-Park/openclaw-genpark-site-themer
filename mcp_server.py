# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Site Themer MCP Server
FastMCP standard interface for semantic CSS variables generation and color distance auditing.
"""

import json
from typing import Dict, Any
from client import OpenClawGenParkSiteThemer

from mcp.server.fastmcp import FastMCP

mcp = FastMCP('openclaw-genpark-site-themer')

themer = OpenClawGenParkSiteThemer()

@mcp.tool()
def generate_semantic_css_custom_properties(
    brand_primary_hex: str = "#2563eb",
    brand_secondary_hex: str = "#0f172a",
    is_dark_mode: bool = False
) -> str:
    """
    Generates production semantic CSS variables for design tokens across light and dark modes.
    """
    res = themer.generate_semantic_css_custom_properties(brand_primary_hex, brand_secondary_hex, is_dark_mode)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_palette_color_distance_delta_e(
    color_hex_a: str,
    color_hex_b: str
) -> str:
    """
    Calculates Euclidean color difference in RGB space.
    """
    res = themer.calculate_palette_color_distance_delta_e(color_hex_a, color_hex_b)
    return json.dumps(res, indent=2)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
