"""NetworkX layout and Plotly figure for the Ribograph atlas."""

from __future__ import annotations

import networkx as nx
import plotly.graph_objects as go

from .data import (
    GRAPH_LINKS,
    GRAPH_NODES,
    NODE_COLORS,
    NodeType,
    adjacency,
    degree_map,
)


def build_network() -> nx.Graph:
    graph = nx.Graph()
    degrees = degree_map()
    for node in GRAPH_NODES:
        graph.add_node(
            node.id,
            type=node.type,
            label=node.display_name,
            degree=degrees.get(node.id, 1),
        )
    for link in GRAPH_LINKS:
        graph.add_edge(link.source, link.target, type=link.type, label=link.label)
    return graph


def layout_positions(seed: int = 7) -> dict[str, tuple[float, float]]:
    graph = build_network()
    raw = nx.spring_layout(graph, seed=seed, k=0.62, iterations=220, dim=2)
    return {node_id: (float(xy[0]), float(xy[1])) for node_id, xy in raw.items()}


def node_size(degree: int, node_type: NodeType) -> float:
    base = {
        "lncRNA": 18,
        "miRNA": 13,
        "circRNA": 16,
        "mRNA": 12,
        "protein": 14,
        "disease": 17,
    }[node_type]
    return base + min(10.0, degree**0.5 * 2.4)


def make_figure(
    *,
    hidden_types: set[NodeType],
    selected_id: str | None,
    match_ids: set[str],
    positions: dict[str, tuple[float, float]],
    height: int = 560,
) -> go.Figure:
    adj = adjacency()
    neighbor_ids = adj.get(selected_id, set()) if selected_id else set()
    visible_nodes = [node for node in GRAPH_NODES if node.type not in hidden_types]
    visible_ids = {node.id for node in visible_nodes}

    fig = go.Figure()

    def edge_xy(highlight: bool) -> tuple[list[float], list[float]]:
        xs: list[float] = []
        ys: list[float] = []
        for link in GRAPH_LINKS:
            if link.source not in visible_ids or link.target not in visible_ids:
                continue
            incident = bool(selected_id and selected_id in (link.source, link.target))
            if incident != highlight:
                continue
            x0, y0 = positions[link.source]
            x1, y1 = positions[link.target]
            xs.extend((x0, x1, None))
            ys.extend((y0, y1, None))
        return xs, ys

    bg_x, bg_y = edge_xy(False)
    if bg_x:
        fig.add_trace(
            go.Scatter(
                x=bg_x,
                y=bg_y,
                mode="lines",
                line={"width": 1.0, "color": "#3d4454"},
                hoverinfo="skip",
                showlegend=False,
                opacity=0.18 if selected_id else 0.85,
            )
        )
    hi_x, hi_y = edge_xy(True)
    if hi_x:
        fig.add_trace(
            go.Scatter(
                x=hi_x,
                y=hi_y,
                mode="lines",
                line={"width": 2.2, "color": "#7ec8c3"},
                hoverinfo="skip",
                showlegend=False,
            )
        )

    xs: list[float] = []
    ys: list[float] = []
    sizes: list[float] = []
    colors: list[str] = []
    opacities: list[float] = []
    texts: list[str] = []
    hovers: list[str] = []
    custom: list[str] = []
    degrees = degree_map()

    for node in visible_nodes:
        x, y = positions[node.id]
        selected = node.id == selected_id
        neighbor = node.id in neighbor_ids
        matched = node.id in match_ids
        dimmed = bool(selected_id) and not selected and not neighbor
        xs.append(x)
        ys.append(y)
        sizes.append(node_size(degrees.get(node.id, 1), node.type) * (1.35 if selected else 1.0))
        colors.append(NODE_COLORS[node.type])
        opacities.append(1.0 if not dimmed else 0.18)
        texts.append(node.display_name if selected or neighbor or matched or not selected_id else "")
        locus = f"<br>Locus {node.locus}" if node.locus else ""
        role = f"<br>{node.role}" if node.role else ""
        hovers.append(
            f"<b>{node.display_name}</b><br>{node.type}{locus}{role}"
            f"<br>{degrees.get(node.id, 0)} interactions"
        )
        custom.append(node.id)

    fig.add_trace(
        go.Scatter(
            x=xs,
            y=ys,
            mode="markers+text",
            text=texts,
            textposition="top center",
            textfont={"color": "#e8eaef", "size": 11, "family": "IBM Plex Sans, sans-serif"},
            marker={
                "size": sizes,
                "color": colors,
                "opacity": opacities,
                "line": {"width": 1.4, "color": "#08090c"},
            },
            customdata=custom,
            hovertemplate="%{hovertext}<extra></extra>",
            hovertext=hovers,
            showlegend=False,
        )
    )

    fig.update_layout(
        paper_bgcolor="#08090c",
        plot_bgcolor="#08090c",
        margin={"l": 8, "r": 8, "t": 8, "b": 8},
        height=height,
        hovermode="closest",
        uirevision="ribograph",
        xaxis={"visible": False, "showgrid": False, "zeroline": False},
        yaxis={
            "visible": False,
            "showgrid": False,
            "zeroline": False,
            "scaleanchor": "x",
            "scaleratio": 1,
        },
        dragmode="pan",
    )
    fig.update_traces(selector={"mode": "markers+text"}, marker_sizemode="diameter")
    return fig
