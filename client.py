# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Site Themer Client
Pure Python Standard Library (Zero External Dependencies)
Implements semantic CSS custom properties token generation, dark/light mode luminance inversion,
and Euclidean RGB color distance Delta-E auditing.
"""

import math
from typing import Dict, Any, List, Optional, Tuple

class OpenClawGenParkSiteThemer:
    """
    Design tokens and multi-mode theme generation engine for web platforms and agent portals.
    """

    def __init__(self):
        pass

    def _hex_to_rgb(self, hex_str: str) -> Tuple[int, int, int]:
        clean = hex_str.lstrip("#")
        if len(clean) == 3:
            clean = "".join([c * 2 for c in clean])
        val = int(clean, 16)
        return ((val >> 16) & 255, (val >> 8) & 255, val & 255)

    def generate_semantic_css_custom_properties(
        self,
        brand_primary_hex: str = "#2563eb",
        brand_secondary_hex: str = "#0f172a",
        is_dark_mode: bool = False
    ) -> Dict[str, Any]:
        """
        Generates production semantic CSS `:root` variables for design tokens across light and dark modes.
        """
        if is_dark_mode:
            tokens = {
                "--bg-canvas": "#0f172a",
                "--bg-surface": "#1e293b",
                "--bg-surface-elevated": "#334155",
                "--text-primary": "#f8fafc",
                "--text-secondary": "#94a3b8",
                "--text-muted": "#64748b",
                "--border-default": "#334155",
                "--border-subtle": "#1e293b",
                "--color-brand-primary": brand_primary_hex,
                "--color-brand-secondary": "#38bdf8",
                "--color-success": "#22c55e",
                "--color-warning": "#f59e0b",
                "--color-danger": "#ef4444"
            }
        else:
            tokens = {
                "--bg-canvas": "#f8fafc",
                "--bg-surface": "#ffffff",
                "--bg-surface-elevated": "#f1f5f9",
                "--text-primary": "#0f172a",
                "--text-secondary": "#475569",
                "--text-muted": "#94a3b8",
                "--border-default": "#e2e8f0",
                "--border-subtle": "#f1f5f9",
                "--color-brand-primary": brand_primary_hex,
                "--color-brand-secondary": brand_secondary_hex,
                "--color-success": "#16a34a",
                "--color-warning": "#d97706",
                "--color-danger": "#dc2626"
            }

        css_lines = [":root {"]
        for k, v in tokens.items():
            css_lines.append(f"  {k}: {v};")
        css_lines.append("}")

        return {
            "mode": "dark" if is_dark_mode else "light",
            "total_tokens_count": len(tokens),
            "css_code_snippet": chr(10).join(css_lines),
            "tokens": tokens
        }

    def calculate_palette_color_distance_delta_e(
        self,
        color_hex_a: str,
        color_hex_b: str
    ) -> Dict[str, Any]:
        """
        Calculates Euclidean color difference in RGB space:
          DeltaE = sqrt( (R1 - R2)^2 + (G1 - G2)^2 + (B1 - B2)^2 )
        Evaluates visual distinctiveness between foreground and background tokens.
        """
        r1, g1, b1 = self._hex_to_rgb(color_hex_a)
        r2, g2, b2 = self._hex_to_rgb(color_hex_b)

        dist = math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)
        dist = round(dist, 2)

        # Max RGB distance is sqrt(255^2 * 3) = 441.67
        distinctiveness_ratio = round(dist / 441.67, 3)

        if dist >= 250.0:
            rating = "HIGHLY_DISTINCT_SHARP_CONTRAST"
        elif dist >= 120.0:
            rating = "MODERATELY_DISTINCT"
        else:
            rating = "MUTED_LOW_CONTRAST"

        return {
            "color_a": color_hex_a,
            "color_b": color_hex_b,
            "euclidean_distance": dist,
            "distinctiveness_ratio": distinctiveness_ratio,
            "distinctiveness_rating": rating
        }
