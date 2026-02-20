#!/usr/bin/env python3
"""
generate_mindmap.py

Generates a dark-themed radial mind map of the EDM paper landscape
from papers.yaml.

Requirements:
    pip install matplotlib networkx pyyaml

Usage:
    python generate_mindmap.py
    python generate_mindmap.py --output my_map.png
"""

import argparse
import math
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import networkx as nx
import yaml

# ── Colour palette ────────────────────────────────────────────────────────────
PALETTE = {
    "bg":          "#0D1117",
    "root":        "#F0A500",
    "category":    "#E05C5C",
    "subcategory": "#5CA4E0",
    "paper":       "#5CE08A",
    "edge":        "#3A3A5C",
}

NODE_SIZE = {"root": 6000, "category": 3500, "subcategory": 2000, "paper": 900}
FONT_SIZE = {"root": 9,    "category": 8,    "subcategory": 7,    "paper": 5.5}


# ── Graph construction ────────────────────────────────────────────────────────

def _paper_label(paper: dict) -> str:
    first = paper["authors"].split(",")[0].strip().split()[-1]
    return f"{first}\n({paper['year']})"


def build_graph(data: dict):
    G = nx.DiGraph()
    meta: dict[str, dict] = {}  # node → {color, size, fontsize}

    root = "Empirical\nDynamical\nModeling"
    G.add_node(root)
    meta[root] = {"color": PALETTE["root"],
                  "size": NODE_SIZE["root"],
                  "fs": FONT_SIZE["root"],
                  "tier": "root"}

    seen: dict[str, int] = {}  # deduplicate label collisions

    def add_paper(parent: str, paper: dict) -> None:
        base = _paper_label(paper)
        seen[base] = seen.get(base, 0) + 1
        label = base if seen[base] == 1 else f"{base}[{seen[base]}]"
        G.add_node(label)
        G.add_edge(parent, label)
        meta[label] = {"color": PALETTE["paper"],
                       "size": NODE_SIZE["paper"],
                       "fs": FONT_SIZE["paper"],
                       "tier": "paper"}

    for cat in data["categories"]:
        cnode = cat["name"]
        G.add_node(cnode)
        G.add_edge(root, cnode)
        meta[cnode] = {"color": PALETTE["category"],
                       "size": NODE_SIZE["category"],
                       "fs": FONT_SIZE["category"],
                       "tier": "category"}

        for paper in cat.get("papers", []):
            add_paper(cnode, paper)

        for sub in cat.get("subcategories", []):
            snode = sub["name"]
            G.add_node(snode)
            G.add_edge(cnode, snode)
            meta[snode] = {"color": PALETTE["subcategory"],
                           "size": NODE_SIZE["subcategory"],
                           "fs": FONT_SIZE["subcategory"],
                           "tier": "subcategory"}
            for paper in sub.get("papers", []):
                add_paper(snode, paper)

    return G, meta, root


# ── Layout ────────────────────────────────────────────────────────────────────

def radial_layout(G: nx.DiGraph, root: str) -> dict:
    """Radial / sunburst layout centred on root."""
    pos = {root: (0.0, 0.0)}
    layers = list(nx.bfs_layers(G, root))
    radii = [0, 3.5, 7.0, 10.5]  # ring radii per depth

    for depth, layer in enumerate(layers[1:], start=1):
        r = radii[min(depth, len(radii) - 1)]
        for i, node in enumerate(layer):
            angle = 2 * math.pi * i / len(layer) - math.pi / 2
            pos[node] = (r * math.cos(angle), r * math.sin(angle))

    return pos


# ── Drawing ───────────────────────────────────────────────────────────────────

def draw(G: nx.DiGraph, meta: dict, root: str, output: str = "edm_mindmap.png"):
    pos = radial_layout(G, root)

    fig, ax = plt.subplots(figsize=(26, 22), facecolor=PALETTE["bg"])
    ax.set_facecolor(PALETTE["bg"])

    # Edges
    nx.draw_networkx_edges(
        G, pos, ax=ax,
        edge_color=PALETTE["edge"],
        arrows=False, width=0.9, alpha=0.75,
    )

    # Nodes — draw large tiers first so they sit behind smaller ones
    for tier in ("root", "category", "subcategory", "paper"):
        nodes = [n for n, m in meta.items() if m["tier"] == tier]
        nx.draw_networkx_nodes(
            G, pos, nodelist=nodes, ax=ax,
            node_color=[meta[n]["color"] for n in nodes],
            node_size=[meta[n]["size"] for n in nodes],
            alpha=0.92,
        )

    # Labels
    for node, (x, y) in pos.items():
        ax.text(x, y, node,
                ha="center", va="center",
                fontsize=meta[node]["fs"],
                fontweight="bold",
                color="white",
                multialignment="center")

    # Legend
    legend = [
        mpatches.Patch(facecolor=PALETTE["root"],        label="Root"),
        mpatches.Patch(facecolor=PALETTE["category"],    label="Category"),
        mpatches.Patch(facecolor=PALETTE["subcategory"], label="Sub-category"),
        mpatches.Patch(facecolor=PALETTE["paper"],       label="Paper"),
    ]
    ax.legend(handles=legend, loc="lower right",
              facecolor="#1C1C2E", labelcolor="white",
              fontsize=11, framealpha=0.85)

    ax.set_title("Empirical Dynamical Modeling — Paper Landscape",
                 color="white", fontsize=17, fontweight="bold", pad=18)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(output, dpi=160, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print(f"Mind map saved to: {output}")
    plt.show()


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate EDM paper mind map")
    parser.add_argument("--output", default="edm_mindmap.png",
                        help="Output PNG file (default: edm_mindmap.png)")
    parser.add_argument("--yaml", default="papers.yaml",
                        help="Path to papers.yaml (default: papers.yaml)")
    args = parser.parse_args()

    yaml_path = Path(args.yaml)
    if not yaml_path.exists():
        raise FileNotFoundError(f"{yaml_path} not found. Run from the repo root.")

    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    G, meta, root = build_graph(data)
    draw(G, meta, root, output=args.output)


if __name__ == "__main__":
    main()
