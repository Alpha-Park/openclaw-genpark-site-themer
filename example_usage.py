# -*- coding: utf-8 -*-
from client import OpenClawGenParkSiteThemer

themer = OpenClawGenParkSiteThemer()

# 1. Semantic CSS Tokens (Dark Mode)
dark_theme = themer.generate_semantic_css_custom_properties("#3b82f6", "#1e293b", is_dark_mode=True)
print(f"Generated CSS Theme: Mode={dark_theme['mode']} ({dark_theme['total_tokens_count']} tokens)")
print(dark_theme['css_code_snippet'][:300]); print("...}")

# 2. Color Distinctiveness Distance
dist = themer.calculate_palette_color_distance_delta_e("#0f172a", "#f8fafc")
print()
print(f"Color Distance: DeltaE={dist['euclidean_distance']} ({dist['distinctiveness_rating']}, Ratio={dist['distinctiveness_ratio']})")
