"""Curated human ncRNA interactome used by the Streamlit app."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

NodeType = Literal["lncRNA", "miRNA", "circRNA", "mRNA", "protein", "disease"]
EdgeType = Literal["sponges", "targets", "binds", "regulates", "associated"]


@dataclass(frozen=True)
class GraphNode:
    id: str
    type: NodeType
    description: str
    label: str | None = None
    aliases: tuple[str, ...] = ()
    locus: str | None = None
    role: str | None = None

    @property
    def display_name(self) -> str:
        return self.label or self.id


@dataclass(frozen=True)
class GraphLink:
    id: str
    source: str
    target: str
    type: EdgeType
    label: str
    note: str | None = None


NODE_TYPE_META: dict[NodeType, dict[str, str]] = {
    "lncRNA": {"label": "Long noncoding RNA", "short": "lncRNA"},
    "miRNA": {"label": "MicroRNA", "short": "miRNA"},
    "circRNA": {"label": "Circular RNA", "short": "circRNA"},
    "mRNA": {"label": "Protein-coding target", "short": "mRNA"},
    "protein": {"label": "RNA-binding protein", "short": "RBP"},
    "disease": {"label": "Disease / phenotype", "short": "Disease"},
}

NODE_TYPE_ORDER: tuple[NodeType, ...] = (
    "lncRNA",
    "miRNA",
    "circRNA",
    "mRNA",
    "protein",
    "disease",
)

EDGE_TYPE_META: dict[EdgeType, str] = {
    "sponges": "ceRNA sponge",
    "targets": "miRNA target",
    "binds": "direct bind",
    "regulates": "regulation",
    "associated": "disease association",
}

NODE_COLORS: dict[NodeType, str] = {
    "lncRNA": "#7ec8c3",
    "miRNA": "#9eb6d9",
    "circRNA": "#6f9e90",
    "mRNA": "#c5c9d4",
    "protein": "#a7b0c0",
    "disease": "#c4a4a4",
}


def _n(
    node_id: str,
    node_type: NodeType,
    description: str,
    *,
    label: str | None = None,
    aliases: tuple[str, ...] = (),
    locus: str | None = None,
    role: str | None = None,
) -> GraphNode:
    return GraphNode(
        id=node_id,
        type=node_type,
        description=description,
        label=label,
        aliases=aliases,
        locus=locus,
        role=role,
    )


def _e(
    source: str,
    target: str,
    edge_type: EdgeType,
    label: str,
    note: str | None = None,
) -> GraphLink:
    return GraphLink(
        id=f"{source}→{target}:{edge_type}",
        source=source,
        target=target,
        type=edge_type,
        label=label,
        note=note,
    )


GRAPH_NODES: tuple[GraphNode, ...] = (
    _n(
        "MALAT1",
        "lncRNA",
        "Nuclear-retained lncRNA that scaffolds splicing factors and is broadly upregulated in solid tumors.",
        aliases=("NEAT2",),
        locus="11q13.1",
        role="Splicing scaffold",
    ),
    _n(
        "HOTAIR",
        "lncRNA",
        "HOX antisense RNA that recruits PRC2/EZH2 to silence HOXD and other loci. Canonical oncogenic lncRNA.",
        locus="12q13.13",
        role="Chromatin recruiter",
    ),
    _n(
        "XIST",
        "lncRNA",
        "Master regulator of X-chromosome inactivation; coats Xi in cis and recruits Polycomb complexes.",
        locus="Xq13.2",
        role="X-inactivation",
    ),
    _n(
        "NEAT1",
        "lncRNA",
        "Architectural lncRNA of paraspeckles; sequesters RNA-binding proteins and is stress-inducible.",
        locus="11q13.1",
        role="Paraspeckle scaffold",
    ),
    _n(
        "H19",
        "lncRNA",
        "Imprinted lncRNA at 11p15.5; host of miR-675 and a well-studied ceRNA in development and cancer.",
        locus="11p15.5",
        role="Imprinted ceRNA",
    ),
    _n(
        "GAS5",
        "lncRNA",
        "Growth-arrest lncRNA that decoys the glucocorticoid receptor and sponges oncogenic microRNAs.",
        locus="1q25.1",
        role="Hormone-receptor decoy",
    ),
    _n(
        "MEG3",
        "lncRNA",
        "Maternally expressed tumor-suppressor lncRNA that stabilizes p53 and sponges miR-29 family members.",
        locus="14q32.2",
        role="p53 stabilizer",
    ),
    _n(
        "TUG1",
        "lncRNA",
        "Taurine-upregulated lncRNA; ceRNA for miR-145 / miR-29 and a chromatin partner of Polycomb proteins.",
        locus="22q12.2",
        role="ceRNA",
    ),
    _n(
        "PVT1",
        "lncRNA",
        "MYC-neighboring lncRNA at 8q24 that stabilizes MYC protein and sponges let-7 and miR-200.",
        locus="8q24.21",
        role="MYC neighbor",
    ),
    _n(
        "ANRIL",
        "lncRNA",
        "CDKN2B-AS1 at the 9p21 CAD risk locus; recruits PRC1/PRC2 to silence the CDKN2A/B cluster.",
        aliases=("CDKN2B-AS1",),
        locus="9p21.3",
        role="CDKN2A/B silencer",
    ),
    _n(
        "DANCR",
        "lncRNA",
        "Differentiation-antagonizing lncRNA that promotes stemness and sponges miR-214 in several cancers.",
        locus="4q12",
        role="Stemness regulator",
    ),
    _n(
        "UCA1",
        "lncRNA",
        "Urothelial cancer associated 1; cytoplasmic ceRNA for miR-143/145 and a glycolytic regulator.",
        locus="19p13.12",
        role="ceRNA",
    ),
    _n(
        "NORAD",
        "lncRNA",
        "Abundant cytoplasmic lncRNA that sequesters PUMILIO proteins to preserve genome stability.",
        aliases=("LINC00657",),
        locus="20q11.23",
        role="PUMILIO decoy",
    ),
    _n(
        "CYTOR",
        "lncRNA",
        "Cytoskeleton regulator RNA (LINC00152); sponges miR-17 family members and tracks with EMT.",
        aliases=("LINC00152",),
        locus="2p11.2",
        role="ceRNA",
    ),
    _n(
        "miR-21",
        "miRNA",
        "OncomiR targeting PTEN, PDCD4 and BCL2; among the most consistently upregulated microRNAs in carcinoma.",
        locus="17q23.1",
        role="OncomiR",
    ),
    _n(
        "miR-155",
        "miRNA",
        "Inflammation- and immunity-linked microRNA; targets SOCS1 and is overexpressed in lymphoma and breast cancer.",
        locus="21q21.3",
        role="Immune oncomiR",
    ),
    _n(
        "miR-34a",
        "miRNA",
        "p53-inducible microRNA that represses SIRT1, BCL2 and MYC; a core effector of the p53 network.",
        locus="1p36.22",
        role="p53 effector",
    ),
    _n(
        "let-7a",
        "miRNA",
        "Founding tumor-suppressor microRNA; represses KRAS, HMGA2 and MYC. Antagonized by LIN28.",
        aliases=("let-7",),
        locus="9q22.32",
        role="Tumor suppressor",
    ),
    _n(
        "miR-200c",
        "miRNA",
        "EMT-suppressing microRNA that targets ZEB1/ZEB2; loss permits epithelial–mesenchymal transition.",
        locus="12p13.31",
        role="EMT suppressor",
    ),
    _n(
        "miR-122",
        "miRNA",
        "Liver-specific microRNA that maintains hepatocyte identity and targets CCNG1; lost in HCC.",
        locus="18q21.31",
        role="Hepatocyte identity",
    ),
    _n(
        "miR-145",
        "miRNA",
        "Smooth-muscle and tumor-suppressor microRNA targeting MYC and stemness factors; sponged by several lncRNAs.",
        locus="5q32",
        role="Tumor suppressor",
    ),
    _n(
        "miR-29b",
        "miRNA",
        "Epigenetic-regulatory microRNA targeting DNMT3A and extracellular-matrix genes; often silenced in cancer.",
        locus="7q32.3",
        role="Epigenetic regulator",
    ),
    _n(
        "miR-7",
        "miRNA",
        "Brain-enriched microRNA targeting EGFR; the classic cargo of the CDR1as circRNA sponge.",
        locus="9q21.32",
        role="EGFR repressor",
    ),
    _n(
        "miR-124",
        "miRNA",
        "Neuron-enriched microRNA targeting STAT3 and CDK4; sponged by circHIPK3 in several tumors.",
        locus="8p23.1",
        role="Neuronal identity",
    ),
    _n(
        "miR-101",
        "miRNA",
        "Tumor-suppressor microRNA that represses EZH2; frequently lost in solid tumors.",
        locus="1p31.3",
        role="EZH2 repressor",
    ),
    _n(
        "miR-214",
        "miRNA",
        "Context-dependent microRNA targeting EZH2; sponged by NEAT1 and DANCR.",
        locus="1q24.3",
        role="EZH2 repressor",
    ),
    _n(
        "miR-17",
        "miRNA",
        "Seed member of the MYC-activated miR-17~92 oncomiR cluster; targets PTEN and E2F-family genes.",
        aliases=("miR-17-5p",),
        locus="13q31.3",
        role="OncomiR cluster",
    ),
    _n(
        "miR-143",
        "miRNA",
        "Co-transcribed with miR-145; represses KRAS and is frequently downregulated in colorectal cancer.",
        locus="5q32",
        role="KRAS repressor",
    ),
    _n(
        "CDR1as",
        "circRNA",
        "ciRS-7, a circular RNA densely packed with miR-7 sites — the textbook circRNA sponge.",
        aliases=("ciRS-7", "CDR1-AS"),
        locus="Xq27.1",
        role="miR-7 sponge",
    ),
    _n(
        "circHIPK3",
        "circRNA",
        "Circular isoform of HIPK3 that sponges miR-124 and miR-29, promoting growth in several cancers.",
        locus="11p13",
        role="ceRNA",
    ),
    _n(
        "circPVT1",
        "circRNA",
        "Circular isoform from the PVT1 locus; sponges let-7 and tracks with proliferation in NSCLC.",
        locus="8q24.21",
        role="let-7 sponge",
    ),
    _n(
        "circSMARCA5",
        "circRNA",
        "Circular RNA from SMARCA5; sponges miR-17 and is often downregulated in glioblastoma.",
        locus="4q31.21",
        role="ceRNA",
    ),
    _n(
        "PTEN",
        "mRNA",
        "Lipid-phosphatase tumor suppressor antagonizing PI3K/AKT; targeted by miR-21 and miR-17.",
        locus="10q23.31",
        role="PI3K antagonist",
    ),
    _n(
        "TP53",
        "mRNA",
        "Guardian of the genome; transactivates miR-34a and is stabilized by MEG3.",
        aliases=("p53",),
        locus="17p13.1",
        role="Tumor suppressor",
    ),
    _n(
        "MYC",
        "mRNA",
        "Master transcription factor driving the miR-17~92 cluster; repressed by let-7 and miR-34a.",
        aliases=("c-MYC",),
        locus="8q24.21",
        role="Oncogene",
    ),
    _n(
        "BCL2",
        "mRNA",
        "Anti-apoptotic regulator targeted by miR-21 and miR-34a.",
        locus="18q21.33",
        role="Apoptosis brake",
    ),
    _n(
        "ZEB1",
        "mRNA",
        "EMT transcription factor in a double-negative feedback loop with the miR-200 family.",
        locus="10p11.22",
        role="EMT factor",
    ),
    _n(
        "KRAS",
        "mRNA",
        "GTPase oncogene repressed by let-7 and miR-143; frequent driver in NSCLC and CRC.",
        locus="12p12.1",
        role="Oncogene",
    ),
    _n(
        "EZH2",
        "mRNA",
        "Catalytic subunit of PRC2; repressed by miR-101 / miR-214 and recruited by HOTAIR.",
        locus="7q36.1",
        role="H3K27 methyltransferase",
    ),
    _n(
        "SIRT1",
        "mRNA",
        "NAD+-dependent deacetylase that inactivates p53; repressed by miR-34a in a feedback loop.",
        locus="10q21.3",
        role="p53 deacetylase",
    ),
    _n(
        "EGFR",
        "mRNA",
        "Receptor tyrosine kinase targeted by miR-7; amplified in a subset of NSCLC and glioblastoma.",
        locus="7p11.2",
        role="RTK oncogene",
    ),
    _n(
        "STAT3",
        "mRNA",
        "Cytokine-activated transcription factor targeted by miR-124; a downstream node of inflammation.",
        locus="17q21.2",
        role="Inflammatory TF",
    ),
    _n(
        "PDCD4",
        "mRNA",
        "Translation-inhibitor tumor suppressor and canonical miR-21 target.",
        locus="10q25.2",
        role="Translation inhibitor",
    ),
    _n(
        "HMGA2",
        "mRNA",
        "Chromatin architectural protein repressed by let-7; promotes stemness and EMT.",
        locus="12q14.3",
        role="Chromatin factor",
    ),
    _n(
        "SOCS1",
        "mRNA",
        "Negative regulator of JAK/STAT signaling and a principal target of miR-155.",
        locus="16p13.13",
        role="JAK/STAT brake",
    ),
    _n(
        "CCNG1",
        "mRNA",
        "Cyclin G1, a liver-enriched miR-122 target that modulates p53 stability.",
        locus="5q34",
        role="Cell-cycle cyclin",
    ),
    _n(
        "DNMT3A",
        "mRNA",
        "De novo DNA methyltransferase targeted by miR-29; links microRNAs to the epigenome.",
        locus="2p23.3",
        role="DNA methyltransferase",
    ),
    _n(
        "PRC2",
        "protein",
        "Polycomb repressive complex 2 (EZH2/SUZ12/EED); recruited in cis or trans by HOTAIR and XIST.",
        role="H3K27me3 writer",
    ),
    _n(
        "PUM1",
        "protein",
        "PUMILIO RNA-binding protein sequestered by NORAD to protect mitotic mRNAs.",
        aliases=("PUMILIO1",),
        role="3′ UTR repressor",
    ),
    _n(
        "SFPQ",
        "protein",
        "Paraspeckle protein (PSF) bound by NEAT1; also a splicing regulator.",
        aliases=("PSF",),
        role="Paraspeckle RBP",
    ),
    _n(
        "SRSF1",
        "protein",
        "SR splicing factor scaffolded by MALAT1 in nuclear speckles.",
        aliases=("ASF/SF2",),
        role="Splicing factor",
    ),
    _n(
        "hnRNPA1",
        "protein",
        "Abundant hnRNP that binds MALAT1 and NEAT1 and regulates alternative splicing.",
        role="Splicing RBP",
    ),
    _n(
        "Breast Ca",
        "disease",
        "Hormone-driven and triple-negative carcinomas with extensive ncRNA rewiring.",
        aliases=("Breast cancer", "BRCA tumor"),
        role="Solid tumor",
    ),
    _n(
        "NSCLC",
        "disease",
        "Non-small cell lung cancer — the disease in which MALAT1 was first linked to metastasis.",
        aliases=("Lung adenocarcinoma", "Non-small cell lung cancer"),
        role="Solid tumor",
    ),
    _n(
        "HCC",
        "disease",
        "Hepatocellular carcinoma; defined in part by loss of miR-122 and gain of H19/PVT1.",
        aliases=("Hepatocellular carcinoma", "Liver cancer"),
        role="Solid tumor",
    ),
    _n(
        "CRC",
        "disease",
        "Colorectal carcinoma; KRAS, HOTAIR and the miR-143/145 cluster are recurrent nodes.",
        aliases=("Colorectal cancer",),
        role="Solid tumor",
    ),
    _n(
        "Glioma",
        "disease",
        "Diffuse gliomas; PTEN loss and circSMARCA5 downregulation are characteristic.",
        aliases=("GBM", "Glioblastoma"),
        role="CNS tumor",
    ),
    _n(
        "Ovarian Ca",
        "disease",
        "High-grade serous ovarian carcinoma; NEAT1 paraspeckles track with progression.",
        aliases=("Ovarian cancer",),
        role="Solid tumor",
    ),
    _n(
        "Prostate Ca",
        "disease",
        "Androgen-driven carcinoma; GAS5 and the p53/miR-34a axis are frequently altered.",
        aliases=("Prostate cancer",),
        role="Solid tumor",
    ),
    _n(
        "CAD",
        "disease",
        "Coronary artery disease. The 9p21 risk haplotype acts through ANRIL at CDKN2B-AS1.",
        aliases=("Atherosclerosis", "Coronary artery disease"),
        role="Vascular disease",
    ),
)

GRAPH_LINKS: tuple[GraphLink, ...] = (
    _e("MALAT1", "miR-200c", "sponges", "sponges", "ceRNA"),
    _e("MALAT1", "miR-101", "sponges", "sponges", "ceRNA"),
    _e("MALAT1", "miR-145", "sponges", "sponges", "ceRNA"),
    _e("MALAT1", "SRSF1", "binds", "binds", "Nuclear speckle scaffold"),
    _e("MALAT1", "hnRNPA1", "binds", "binds"),
    _e("MALAT1", "NSCLC", "associated", "associated", "Metastasis lncRNA"),
    _e("MALAT1", "Breast Ca", "associated", "associated"),
    _e("HOTAIR", "miR-34a", "sponges", "sponges", "ceRNA"),
    _e("HOTAIR", "miR-145", "sponges", "sponges"),
    _e("HOTAIR", "PRC2", "binds", "binds", "PRC2 recruitment"),
    _e("HOTAIR", "EZH2", "binds", "binds"),
    _e("HOTAIR", "Breast Ca", "associated", "associated"),
    _e("HOTAIR", "CRC", "associated", "associated"),
    _e("XIST", "miR-34a", "sponges", "sponges"),
    _e("XIST", "miR-155", "sponges", "sponges"),
    _e("XIST", "PRC2", "binds", "binds", "Xi coating"),
    _e("XIST", "Breast Ca", "associated", "associated"),
    _e("NEAT1", "miR-34a", "sponges", "sponges"),
    _e("NEAT1", "miR-214", "sponges", "sponges"),
    _e("NEAT1", "SFPQ", "binds", "binds", "Paraspeckle"),
    _e("NEAT1", "hnRNPA1", "binds", "binds"),
    _e("NEAT1", "Ovarian Ca", "associated", "associated"),
    _e("H19", "let-7a", "sponges", "sponges", "ceRNA"),
    _e("H19", "miR-200c", "sponges", "sponges"),
    _e("H19", "HCC", "associated", "associated"),
    _e("GAS5", "miR-21", "sponges", "sponges", "ceRNA"),
    _e("GAS5", "miR-145", "sponges", "sponges"),
    _e("GAS5", "Breast Ca", "associated", "associated"),
    _e("GAS5", "Prostate Ca", "associated", "associated"),
    _e("MEG3", "miR-29b", "sponges", "sponges"),
    _e("MEG3", "miR-21", "sponges", "sponges"),
    _e("MEG3", "TP53", "regulates", "stabilizes", "p53 stabilization"),
    _e("MEG3", "HCC", "associated", "associated"),
    _e("TUG1", "miR-145", "sponges", "sponges"),
    _e("TUG1", "miR-29b", "sponges", "sponges"),
    _e("PVT1", "miR-200c", "sponges", "sponges"),
    _e("PVT1", "let-7a", "sponges", "sponges"),
    _e("PVT1", "MYC", "regulates", "stabilizes", "Protein stabilization"),
    _e("PVT1", "HCC", "associated", "associated"),
    _e("PVT1", "Breast Ca", "associated", "associated"),
    _e("ANRIL", "miR-17", "sponges", "sponges"),
    _e("ANRIL", "PRC2", "binds", "binds", "9p21 silencing"),
    _e("ANRIL", "CAD", "associated", "associated", "9p21 GWAS locus"),
    _e("ANRIL", "Glioma", "associated", "associated"),
    _e("DANCR", "miR-214", "sponges", "sponges"),
    _e("DANCR", "EZH2", "regulates", "recruits"),
    _e("UCA1", "miR-143", "sponges", "sponges"),
    _e("UCA1", "miR-145", "sponges", "sponges"),
    _e("NORAD", "PUM1", "binds", "sequesters", "Genome-stability decoy"),
    _e("CYTOR", "miR-17", "sponges", "sponges"),
    _e("CDR1as", "miR-7", "sponges", "sponges", "Classic circRNA sponge"),
    _e("CDR1as", "HCC", "associated", "associated"),
    _e("CDR1as", "CRC", "associated", "associated"),
    _e("circHIPK3", "miR-124", "sponges", "sponges"),
    _e("circHIPK3", "miR-29b", "sponges", "sponges"),
    _e("circPVT1", "let-7a", "sponges", "sponges"),
    _e("circPVT1", "NSCLC", "associated", "associated"),
    _e("circSMARCA5", "miR-17", "sponges", "sponges"),
    _e("circSMARCA5", "Glioma", "associated", "associated"),
    _e("miR-21", "PTEN", "targets", "targets", "RISC"),
    _e("miR-21", "PDCD4", "targets", "targets", "RISC"),
    _e("miR-21", "BCL2", "targets", "targets"),
    _e("miR-21", "Breast Ca", "associated", "associated"),
    _e("miR-21", "NSCLC", "associated", "associated"),
    _e("miR-155", "SOCS1", "targets", "targets"),
    _e("miR-155", "Breast Ca", "associated", "associated"),
    _e("miR-34a", "SIRT1", "targets", "targets"),
    _e("miR-34a", "BCL2", "targets", "targets"),
    _e("miR-34a", "MYC", "targets", "targets"),
    _e("miR-34a", "Prostate Ca", "associated", "associated"),
    _e("let-7a", "KRAS", "targets", "targets"),
    _e("let-7a", "HMGA2", "targets", "targets"),
    _e("let-7a", "MYC", "targets", "targets"),
    _e("let-7a", "NSCLC", "associated", "associated"),
    _e("miR-200c", "ZEB1", "targets", "targets", "EMT double-negative loop"),
    _e("miR-122", "CCNG1", "targets", "targets"),
    _e("miR-122", "HCC", "associated", "associated", "Lost in HCC"),
    _e("miR-145", "MYC", "targets", "targets"),
    _e("miR-29b", "DNMT3A", "targets", "targets"),
    _e("miR-7", "EGFR", "targets", "targets"),
    _e("miR-124", "STAT3", "targets", "targets"),
    _e("miR-101", "EZH2", "targets", "targets"),
    _e("miR-214", "EZH2", "targets", "targets"),
    _e("miR-17", "PTEN", "targets", "targets"),
    _e("miR-143", "KRAS", "targets", "targets"),
    _e("TP53", "miR-34a", "regulates", "activates", "Direct transactivation"),
    _e("MYC", "miR-17", "regulates", "activates", "miR-17~92 cluster"),
    _e("TP53", "Breast Ca", "associated", "associated"),
    _e("KRAS", "NSCLC", "associated", "associated"),
    _e("KRAS", "CRC", "associated", "associated"),
    _e("EGFR", "NSCLC", "associated", "associated"),
    _e("EGFR", "Glioma", "associated", "associated"),
    _e("PTEN", "Glioma", "associated", "associated"),
    _e("ZEB1", "CRC", "associated", "associated"),
    _e("MYC", "CRC", "associated", "associated"),
)


def _assert_graph(nodes: tuple[GraphNode, ...], links: tuple[GraphLink, ...]) -> None:
    ids = [node.id for node in nodes]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate node id in ncRNA graph")
    known = set(ids)
    degree: dict[str, int] = {node_id: 0 for node_id in known}
    for link in links:
        if link.source not in known:
            raise ValueError(f"Unknown link source: {link.source}")
        if link.target not in known:
            raise ValueError(f"Unknown link target: {link.target}")
        degree[link.source] += 1
        degree[link.target] += 1
    isolated = [node_id for node_id, count in degree.items() if count == 0]
    if isolated:
        raise ValueError(f"Isolated nodes: {', '.join(isolated)}")


_assert_graph(GRAPH_NODES, GRAPH_LINKS)

NODE_BY_ID: dict[str, GraphNode] = {node.id: node for node in GRAPH_NODES}


def degree_map(links: tuple[GraphLink, ...] = GRAPH_LINKS) -> dict[str, int]:
    degree: dict[str, int] = {}
    for link in links:
        degree[link.source] = degree.get(link.source, 0) + 1
        degree[link.target] = degree.get(link.target, 0) + 1
    return degree


def adjacency(links: tuple[GraphLink, ...] = GRAPH_LINKS) -> dict[str, set[str]]:
    adj: dict[str, set[str]] = {}
    for link in links:
        adj.setdefault(link.source, set()).add(link.target)
        adj.setdefault(link.target, set()).add(link.source)
    return adj


def search_nodes(query: str, nodes: tuple[GraphNode, ...] = GRAPH_NODES) -> list[GraphNode]:
    q = query.strip().lower()
    if not q:
        return []
    hits: list[GraphNode] = []
    for node in nodes:
        haystacks = (
            node.id,
            node.display_name,
            node.type,
            node.locus or "",
            node.role or "",
            node.description,
            *node.aliases,
        )
        if any(q in value.lower() for value in haystacks):
            hits.append(node)
    return hits


def neighbors_of(
    node_id: str,
    links: tuple[GraphLink, ...] = GRAPH_LINKS,
) -> list[tuple[str, GraphLink, Literal["out", "in"]]]:
    result: list[tuple[str, GraphLink, Literal["out", "in"]]] = []
    for link in links:
        if link.source == node_id:
            result.append((link.target, link, "out"))
        elif link.target == node_id:
            result.append((link.source, link, "in"))
    return result
