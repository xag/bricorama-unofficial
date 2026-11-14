"""The wood panels Bricorama France lists, as data on furniture-design's kinds (source, clause, material),
each line read as a board of wood-panels. Unofficial: Bricorama neither wrote nor endorsed it.

What the shop lists comes from its public product sitemap (range.json, read by tools/read_range.py from the
sitemap files as fetched): every product whose title or address states a board, its line, thickness and sheet
size. Each is a clause under sources/bricorama-sitemap. wood_panels.shops reads the titles and makes the materials:
one per line and thickness, `bricorama-<line>-<thickness>`, its payload `shop` saying what is sold and which
board its values are.

    from furniture_design.knowledge import knowledge as general, merge
    from wood_panels import knowledge as wood_panels
    from bricorama_unofficial import knowledge as bricorama
    tree.root.children = merge(general(), wood_panels(), bricorama()) + [pieces]
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from quern.tree import Node
from wood_panels import shops

HERE = Path(__file__).parent
SHOP = "Bricorama"
PREFIX = "bricorama"
SOURCE = "bricorama-sitemap"


@lru_cache(maxsize=1)
def rows() -> list[dict]:
    return json.loads((HERE / "range.json").read_text(encoding="utf-8"))



def knowledge() -> list[Node]:
    """The branches to merge beside furniture-design's and wood-panels's: the sources, the materials."""
    out = shops.knowledge(PREFIX, SHOP, SOURCE, "Bricorama France, product sitemap (https://www.bricorama.fr/sitemap/sitemap.xml)",
                          "https://www.bricorama.fr/sitemap/sitemap.xml", "2026-11-14", rows())
    return out
