# Ribograph

Interactive atlas of a curated **human noncoding RNA interactome**.

Ribograph is a [Streamlit](https://streamlit.io) application. It maps well-studied lncRNAs, microRNAs, circular RNAs, their mRNA targets, RNA-binding proteins, and disease associations as a force-directed network you can search, filter, and inspect.

This is a teaching / exploration atlas, not a genome-wide interaction database. Edges are literature-anchored ceRNA sponging, RISC targeting, direct binding, regulation, and disease association.

## Features

- Force-directed network of lncRNA, miRNA, circRNA, mRNA, RBP, and disease nodes
- Search by gene symbol, alias, locus, role, or free text (`MALAT1`, `miR-21`, `NSCLC`)
- Filter by biotype
- Click a node (or a search hit) to see locus, role, description, and first-degree interactions
- Walk the neighborhood with **Open** on any neighbor
- Side-by-side dashboard: network and selected-node inspector on the left, 40 PubMed-indexed sources on the right

## Requirements

- Python 3.10 or newer (3.11–3.14 are fine)
- pip
- A modern browser

## Installation

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The virtual environment is recommended so Streamlit, NetworkX, and Plotly stay isolated from other Python work.

## Run the app

```bash
streamlit run app.py
```

Streamlit prints a local URL, usually:

```text
http://localhost:8501
```

Open that address in your browser. To bind a specific host or port:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

To stop the server, press `Ctrl+C` in the terminal.

Run `streamlit run app.py` from the project root so Python can import the `ribograph` package next to `app.py`.

## Using the atlas

1. Pan by dragging the canvas; scroll to zoom.
2. Type a symbol in the sidebar search and click a hit, or click a node on the map.
3. Uncheck a biotype to hide that class (at least one class must remain visible).
4. **Open** a neighbor to jump along an edge (for example MALAT1 → miR-200c → ZEB1).
5. **Clear selection** restores the full graph.
6. Read matching papers in the **PubMed sources** column on the right (follows the selected node; uncheck to see all 40).

Suggested starting nodes: `MALAT1`, `HOTAIR`, `CDR1as`, `miR-34a`, `ANRIL`.

## Project layout

```text
app.py                 Streamlit entry point
ribograph/
  data.py              Curated nodes, edges, search, neighbors
  graph.py             NetworkX layout + Plotly figure
  references.py        PubMed-indexed sources (PMID-verified)
  __init__.py
requirements.txt       Python dependencies
LICENSE.md             MIT license
```

The interactome lives in `ribograph/data.py`. Import-time checks reject duplicate node IDs, dangling edges, and isolated nodes.

`src/` is an earlier browser canvas prototype. The supported application is the Streamlit app.

## AI Disclaimer

Portions or the entirety of this codebase, including associated logic, documentation, and automated scripts, were generated, refactored, or assisted by Grok, an artificial intelligence model developed by xAI. The developer is entirely responsible for the validity of the source code. 

## License

MIT. See [LICENSE.md](LICENSE.md).
