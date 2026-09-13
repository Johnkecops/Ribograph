"""Ribograph Streamlit app — human noncoding RNA interactome."""

from __future__ import annotations

import streamlit as st

from ribograph.data import (
    GRAPH_LINKS,
    GRAPH_NODES,
    NODE_BY_ID,
    NODE_COLORS,
    NODE_TYPE_META,
    NODE_TYPE_ORDER,
    NodeType,
    neighbors_of,
    search_nodes,
)
from ribograph.graph import layout_positions, make_figure
from ribograph.references import REFERENCES, references_for_node, search_references

st.set_page_config(
    page_title="Ribograph",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
      @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,500;6..72,600&display=swap");
      html, body, [data-testid="stAppViewContainer"] {
        font-family: "IBM Plex Sans", sans-serif;
      }
      h1, h2, h3 { font-family: Newsreader, Georgia, serif; letter-spacing: -0.03em; }
      .stApp { background: #08090c; }
      section[data-testid="stSidebar"] { background: #12141a; border-right: 1px solid #23262f; }
      .block-container { padding-top: 1rem; padding-bottom: 1rem; max-width: 100%; }
      div[data-testid="stMetricValue"] { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
      .stPlotlyChart, div[data-testid="stPlotlyChart"] {
        position: relative;
        z-index: 0;
        overflow: hidden;
        background: #08090c;
      }
      div[data-testid="stHorizontalBlock"] { align-items: flex-start; }
      div[data-testid="stVerticalBlockBorderWrapper"] { background: #12141a; }
    </style>
    """,
    unsafe_allow_html=True,
)

if "selected_id" not in st.session_state:
    st.session_state.selected_id = None
if "positions" not in st.session_state:
    st.session_state.positions = layout_positions()


def select_node(node_id: str | None) -> None:
    st.session_state.selected_id = node_id


def render_sidebar() -> tuple[set[str], set[NodeType]]:
    st.sidebar.markdown("### Ribograph")
    st.sidebar.caption("Human ncRNA interactome")

    query = st.sidebar.text_input(
        "Search",
        placeholder="MALAT1, miR-21, NSCLC…",
        label_visibility="collapsed",
        key="search",
    )
    matches = search_nodes(query)
    match_ids = {node.id for node in matches}

    if query.strip():
        if not matches:
            st.sidebar.caption("No matching nodes")
        else:
            for node in matches[:8]:
                if st.sidebar.button(
                    f"{node.display_name}  ·  {NODE_TYPE_META[node.type]['short']}",
                    key=f"hit-{node.id}",
                    use_container_width=True,
                ):
                    select_node(node.id)

    st.sidebar.markdown("#### Biotype")
    hidden: set[NodeType] = set()
    for node_type in NODE_TYPE_ORDER:
        shown = st.sidebar.checkbox(
            NODE_TYPE_META[node_type]["short"],
            value=True,
            key=f"type-{node_type}",
        )
        if not shown:
            hidden.add(node_type)
    if len(hidden) == len(NODE_TYPE_ORDER):
        st.sidebar.caption("Keep at least one biotype visible.")
        hidden = set()

    st.sidebar.markdown("#### Atlas")
    c1, c2 = st.sidebar.columns(2)
    c1.metric("Nodes", len(GRAPH_NODES))
    c2.metric("Edges", len(GRAPH_LINKS))
    st.sidebar.metric("PubMed sources", len(REFERENCES))

    if st.sidebar.button("Clear selection", use_container_width=True):
        select_node(None)

    return match_ids, hidden


def render_network(match_ids: set[str], hidden: set[NodeType]) -> None:
    st.markdown("### Network")
    legend = " · ".join(
        f'<span style="color:{NODE_COLORS[t]}">●</span> {NODE_TYPE_META[t]["short"]}'
        for t in NODE_TYPE_ORDER
        if t not in hidden
    )
    st.markdown(legend, unsafe_allow_html=True)

    fig = make_figure(
        hidden_types=hidden,
        selected_id=st.session_state.selected_id,
        match_ids=match_ids,
        positions=st.session_state.positions,
        height=540,
    )
    event = st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "scrollZoom": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["lasso2d", "select2d", "autoScale2d"],
        },
        on_select="rerun",
        selection_mode="points",
        key="network",
    )

    points = getattr(getattr(event, "selection", None), "points", None) or []
    if points:
        custom = points[0].get("customdata")
        if isinstance(custom, list) and custom:
            custom = custom[0]
        if isinstance(custom, str) and custom in NODE_BY_ID:
            if st.session_state.selected_id != custom:
                select_node(custom)
                st.rerun()


def render_node_panel() -> None:
    selected = NODE_BY_ID.get(st.session_state.selected_id) if st.session_state.selected_id else None
    st.markdown("### Selected node")
    if selected is None:
        st.info("Click a node on the network, or search from the sidebar.")
        return

    meta = NODE_TYPE_META[selected.type]
    color = NODE_COLORS[selected.type]
    st.markdown(
        f"<span style='color:{color}'>●</span> **{selected.display_name}** · {meta['short']}",
        unsafe_allow_html=True,
    )
    bits = []
    if selected.locus:
        bits.append(selected.locus)
    if selected.role:
        bits.append(selected.role)
    if bits:
        st.caption(" · ".join(bits))
    if selected.aliases:
        st.markdown("**Aliases:** " + " · ".join(selected.aliases))
    st.write(selected.description)

    edges = neighbors_of(selected.id)
    st.markdown(f"**{len(edges)} interaction{'s' if len(edges) != 1 else ''}**")
    for other_id, link, direction in edges:
        other = NODE_BY_ID[other_id]
        verb = link.label if direction == "out" else f"{link.label} of"
        note = f" — {link.note}" if link.note else ""
        col_a, col_b = st.columns([4, 1])
        with col_a:
            st.markdown(
                f"<span style='color:{NODE_COLORS[other.type]}'>●</span> "
                f"**{other.display_name}** · {verb}{note}",
                unsafe_allow_html=True,
            )
        with col_b:
            if st.button("Open", key=f"nbr-{selected.id}-{other.id}-{link.id}"):
                select_node(other.id)
                st.rerun()


def render_references_panel() -> None:
    st.markdown("### PubMed sources")
    st.caption(
        "Indexed journal articles that source the atlas. "
        "Each PMID was retrieved from NCBI PubMed."
    )

    selected_id = st.session_state.selected_id
    follow = st.checkbox(
        "Follow selected node",
        value=True,
        help="When a node is selected, show only papers that source it.",
    )
    ref_query = st.text_input(
        "Search papers",
        placeholder="Hansen, HOTAIR, 23446346…",
        label_visibility="collapsed",
        key="ref_query",
    )

    if follow and selected_id:
        refs = references_for_node(selected_id)
        heading = f"Papers for {selected_id}"
        if ref_query.strip():
            q = ref_query.strip().lower()
            refs = [
                ref
                for ref in refs
                if q in ref.vancouver().lower() or q in ref.supports.lower()
            ]
    else:
        refs = search_references(ref_query)
        heading = "All papers"

    st.caption(f"{heading} · {len(refs)} of {len(REFERENCES)}")

    if not refs:
        st.info("No papers match this filter. Uncheck “Follow selected node” to see the full set.")
        return

    with st.container(height=760, border=True):
        for i, ref in enumerate(refs, start=1):
            st.markdown(f"**{i}. {ref.title}**")
            st.caption(ref.vancouver())
            st.write(ref.supports)
            chips = [
                f"<span style='color:{NODE_COLORS[NODE_BY_ID[node_id].type]}'>●</span> {node_id}"
                for node_id in ref.nodes
            ]
            chips.extend(f"`{source} → {target}`" for source, target in ref.edges)
            if chips:
                st.markdown(" · ".join(chips), unsafe_allow_html=True)
            st.link_button(f"PubMed {ref.pmid}", ref.pubmed_url)
            st.divider()


match_ids, hidden = render_sidebar()

st.markdown("# Ribograph")
st.caption(
    "Force-directed atlas of human noncoding RNA interactions — lncRNA, miRNA, "
    "circRNA, protein-coding targets, RNA-binding proteins, and disease associations."
)

network_col, refs_col = st.columns([1.35, 1], gap="large")
with network_col:
    render_network(match_ids, hidden)
    render_node_panel()
with refs_col:
    render_references_panel()
