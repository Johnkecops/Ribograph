"""PubMed-indexed sources for Ribograph nodes and edges.

Every PMID was retrieved from NCBI E-utilities (esummary, db=pubmed) and is a
live PubMed record. The list is a curated teaching set (20–40 papers), not an
exhaustive bibliography of every edge.
"""

from __future__ import annotations

from dataclasses import dataclass

from .data import NODE_BY_ID


@dataclass(frozen=True)
class Reference:
    pmid: str
    year: int
    authors: tuple[str, ...]
    title: str
    journal: str
    volume: str
    issue: str
    pages: str
    nodes: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]
    supports: str

    @property
    def pubmed_url(self) -> str:
        return f"https://pubmed.ncbi.nlm.nih.gov/{self.pmid}/"

    @property
    def author_line(self) -> str:
        names = list(self.authors)
        if len(names) > 6:
            names = names[:6] + ["et al."]
        return ", ".join(names)

    def vancouver(self) -> str:
        loc = self.journal
        if self.year:
            loc += f". {self.year}"
        if self.volume:
            loc += f";{self.volume}"
            if self.issue:
                loc += f"({self.issue})"
        if self.pages:
            loc += f":{self.pages}"
        loc += "."
        return f"{self.author_line}. {self.title} {loc} PMID: {self.pmid}."


REFERENCES: tuple[Reference, ...] = (
    Reference(
        pmid="12970751",
        year=2003,
        authors=(
            "Ji P", "Diederichs S", "Wang W", "Böing S", "Metzger R",
            "Schneider PM", "Tidow N", "Brandt B", "Buerger H", "Bulk E",
            "Thomas M", "Berdel WE", "Serve H", "Müller-Tidow C",
        ),
        title="MALAT-1, a novel noncoding RNA, and thymosin beta4 predict metastasis and survival in early-stage non-small cell lung cancer.",
        journal="Oncogene",
        volume="22",
        issue="39",
        pages="8031-41",
        nodes=("MALAT1", "NSCLC"),
        edges=(("MALAT1", "NSCLC"),),
        supports="Discovery of MALAT1 as a metastasis-associated lncRNA in NSCLC.",
    ),
    Reference(
        pmid="20797886",
        year=2010,
        authors=(
            "Tripathi V", "Ellis JD", "Shen Z", "Song DY", "Pan Q", "Watt AT",
            "Freier SM", "Bennett CF", "Sharma A", "Bubulya PA", "Blencowe BJ",
            "Prasanth SG", "Prasanth KV",
        ),
        title="The nuclear-retained noncoding RNA MALAT1 regulates alternative splicing by modulating SR splicing factor phosphorylation.",
        journal="Mol Cell",
        volume="39",
        issue="6",
        pages="925-38",
        nodes=("MALAT1", "SRSF1"),
        edges=(("MALAT1", "SRSF1"),),
        supports="MALAT1 scaffolds SR splicing factors, including SRSF1, in nuclear speckles.",
    ),
    Reference(
        pmid="17604720",
        year=2007,
        authors=(
            "Rinn JL", "Kertesz M", "Wang JK", "Squazzo SL", "Xu X",
            "Brugmann SA", "Goodnough LH", "Helms JA", "Farnham PJ",
            "Segal E", "Chang HY",
        ),
        title="Functional demarcation of active and silent chromatin domains in human HOX loci by noncoding RNAs.",
        journal="Cell",
        volume="129",
        issue="7",
        pages="1311-23",
        nodes=("HOTAIR",),
        edges=(),
        supports="Identification of HOTAIR as a HOX antisense lncRNA.",
    ),
    Reference(
        pmid="20393566",
        year=2010,
        authors=(
            "Gupta RA", "Shah N", "Wang KC", "Kim J", "Horlings HM", "Wong DJ",
            "Tsai MC", "Hung T", "Argani P", "Rinn JL", "Wang Y", "Brzoska P",
            "Kong B", "Li R", "West RB", "van de Vijver MJ", "Sukumar S",
            "Chang HY",
        ),
        title="Long non-coding RNA HOTAIR reprograms chromatin state to promote cancer metastasis.",
        journal="Nature",
        volume="464",
        issue="7291",
        pages="1071-6",
        nodes=("HOTAIR", "PRC2", "Breast Ca"),
        edges=(("HOTAIR", "PRC2"), ("HOTAIR", "Breast Ca")),
        supports="HOTAIR recruits Polycomb and promotes breast-cancer metastasis.",
    ),
    Reference(
        pmid="20616235",
        year=2010,
        authors=(
            "Tsai MC", "Manor O", "Wan Y", "Mosammaparast N", "Wang JK",
            "Lan F", "Shi Y", "Segal E", "Chang HY",
        ),
        title="Long noncoding RNA as modular scaffold of histone modification complexes.",
        journal="Science",
        volume="329",
        issue="5992",
        pages="689-93",
        nodes=("HOTAIR", "PRC2", "EZH2"),
        edges=(("HOTAIR", "PRC2"), ("HOTAIR", "EZH2")),
        supports="HOTAIR is a modular scaffold for PRC2/EZH2 histone-modification complexes.",
    ),
    Reference(
        pmid="8538762",
        year=1996,
        authors=("Penny GD", "Kay GF", "Sheardown SA", "Rastan S", "Brockdorff N"),
        title="Requirement for Xist in X chromosome inactivation.",
        journal="Nature",
        volume="379",
        issue="6561",
        pages="131-7",
        nodes=("XIST",),
        edges=(),
        supports="Genetic requirement for Xist in X-chromosome inactivation.",
    ),
    Reference(
        pmid="18974356",
        year=2008,
        authors=("Zhao J", "Sun BK", "Erwin JA", "Song JJ", "Lee JT"),
        title="Polycomb proteins targeted by a short repeat RNA to the mouse X chromosome.",
        journal="Science",
        volume="322",
        issue="5902",
        pages="750-6",
        nodes=("XIST", "PRC2"),
        edges=(("XIST", "PRC2"),),
        supports="Xist Repeat A RNA recruits PRC2 to the inactive X.",
    ),
    Reference(
        pmid="19217333",
        year=2009,
        authors=(
            "Clemson CM", "Hutchinson JN", "Sara SA", "Ensminger AW", "Fox AH",
            "Chess A", "Lawrence JB",
        ),
        title="An architectural role for a nuclear noncoding RNA: NEAT1 RNA is essential for the structure of paraspeckles.",
        journal="Mol Cell",
        volume="33",
        issue="6",
        pages="717-26",
        nodes=("NEAT1", "SFPQ"),
        edges=(("NEAT1", "SFPQ"),),
        supports="NEAT1 is the architectural RNA of paraspeckles (SFPQ/PSF partners).",
    ),
    Reference(
        pmid="24055342",
        year=2013,
        authors=(
            "Kallen AN", "Zhou XB", "Xu J", "Qiao C", "Ma J", "Yan L", "Lu L",
            "Liu C", "Yi JS", "Zhang H", "Min W", "Bennett AM", "Gregory RI",
            "Ding Y", "Huang Y",
        ),
        title="The imprinted H19 lncRNA antagonizes let-7 microRNAs.",
        journal="Mol Cell",
        volume="52",
        issue="1",
        pages="101-12",
        nodes=("H19", "let-7a"),
        edges=(("H19", "let-7a"),),
        supports="H19 functions as a molecular sponge for let-7.",
    ),
    Reference(
        pmid="20124551",
        year=2010,
        authors=("Kino T", "Hurt DE", "Ichijo T", "Nader N", "Chrousos GP"),
        title="Noncoding RNA gas5 is a growth arrest- and starvation-associated repressor of the glucocorticoid receptor.",
        journal="Sci Signal",
        volume="3",
        issue="107",
        pages="ra8",
        nodes=("GAS5",),
        edges=(),
        supports="GAS5 as a glucocorticoid-receptor decoy lncRNA.",
    ),
    Reference(
        pmid="17569660",
        year=2007,
        authors=(
            "Zhou Y", "Zhong Y", "Wang Y", "Zhang X", "Batista DL", "Gejman R",
            "Ansell PJ", "Zhao J", "Weng C", "Klibanski A",
        ),
        title="Activation of p53 by MEG3 non-coding RNA.",
        journal="J Biol Chem",
        volume="282",
        issue="34",
        pages="24731-42",
        nodes=("MEG3", "TP53"),
        edges=(("MEG3", "TP53"),),
        supports="MEG3 activates/stabilizes p53.",
    ),
    Reference(
        pmid="25043044",
        year=2014,
        authors=(
            "Tseng YY", "Moriarity BS", "Gong W", "Akiyama R", "Tiwari A",
            "Kawakami H", "Ronning P", "Reuland B", "Guenther K", "Beadnell TC",
            "Essig J", "Otto GM", "O'Sullivan MG", "Largaespada DA",
            "Schwertfeger KL", "Marahrens Y", "Kawakami Y", "Bagchi A",
        ),
        title="PVT1 dependence in cancer with MYC copy-number increase.",
        journal="Nature",
        volume="512",
        issue="7512",
        pages="82-6",
        nodes=("PVT1", "MYC"),
        edges=(("PVT1", "MYC"),),
        supports="PVT1 is required to sustain MYC protein in 8q24-amplified cancers.",
    ),
    Reference(
        pmid="20541999",
        year=2010,
        authors=(
            "Yap KL", "Li S", "Muñoz-Cabello AM", "Raguz S", "Zeng L",
            "Mujtaba S", "Gil J", "Walsh MJ", "Zhou MM",
        ),
        title="Molecular interplay of the noncoding RNA ANRIL and methylated histone H3 lysine 27 by polycomb CBX7 in transcriptional silencing of INK4a.",
        journal="Mol Cell",
        volume="38",
        issue="5",
        pages="662-74",
        nodes=("ANRIL", "PRC2"),
        edges=(("ANRIL", "PRC2"),),
        supports="ANRIL binds Polycomb to silence the CDKN2A/B (INK4a) locus.",
    ),
    Reference(
        pmid="20056914",
        year=2010,
        authors=(
            "Holdt LM", "Beutner F", "Scholz M", "Gielen S", "Gäbel G",
            "Bergert H", "Schuler G", "Thiery J", "Teupser D",
        ),
        title="ANRIL expression is associated with atherosclerosis risk at chromosome 9p21.",
        journal="Arterioscler Thromb Vasc Biol",
        volume="30",
        issue="3",
        pages="620-7",
        nodes=("ANRIL", "CAD"),
        edges=(("ANRIL", "CAD"),),
        supports="ANRIL expression tracks 9p21 coronary-artery-disease risk.",
    ),
    Reference(
        pmid="26724866",
        year=2016,
        authors=(
            "Lee S", "Kopp F", "Chang TC", "Sataluri A", "Chen B",
            "Sivakumar S", "Yu H", "Xie Y", "Mendell JT",
        ),
        title="Noncoding RNA NORAD Regulates Genomic Stability by Sequestering PUMILIO Proteins.",
        journal="Cell",
        volume="164",
        issue="1-2",
        pages="69-80",
        nodes=("NORAD", "PUM1"),
        edges=(("NORAD", "PUM1"),),
        supports="NORAD sequesters PUMILIO proteins to preserve genome stability.",
    ),
    Reference(
        pmid="23446346",
        year=2013,
        authors=(
            "Hansen TB", "Jensen TI", "Clausen BH", "Bramsen JB", "Finsen B",
            "Damgaard CK", "Kjems J",
        ),
        title="Natural RNA circles function as efficient microRNA sponges.",
        journal="Nature",
        volume="495",
        issue="7441",
        pages="384-8",
        nodes=("CDR1as", "miR-7"),
        edges=(("CDR1as", "miR-7"),),
        supports="ciRS-7/CDR1as is a circular RNA sponge for miR-7.",
    ),
    Reference(
        pmid="27050392",
        year=2016,
        authors=(
            "Zheng Q", "Bao C", "Guo W", "Li S", "Chen J", "Chen B", "Luo Y",
            "Lyu D", "Li Y", "Shi G", "Liang L", "Gu J", "He X", "Huang S",
        ),
        title="Circular RNA profiling reveals an abundant circHIPK3 that regulates cell growth by sponging multiple miRNAs.",
        journal="Nat Commun",
        volume="7",
        issue="",
        pages="11215",
        nodes=("circHIPK3", "miR-124", "miR-29b"),
        edges=(("circHIPK3", "miR-124"), ("circHIPK3", "miR-29b")),
        supports="circHIPK3 sponges multiple miRNAs, including miR-124 and miR-29.",
    ),
    Reference(
        pmid="27928058",
        year=2017,
        authors=(
            "Panda AC", "Grammatikakis I", "Kim KM", "De S", "Martindale JL",
            "Munk R", "Yang X", "Abdelmohsen K", "Gorospe M",
        ),
        title="Identification of senescence-associated circular RNAs (SAC-RNAs) reveals senescence suppressor CircPVT1.",
        journal="Nucleic Acids Res",
        volume="45",
        issue="7",
        pages="4021-4035",
        nodes=("circPVT1", "let-7a"),
        edges=(("circPVT1", "let-7a"),),
        supports="circPVT1 binds and suppresses let-7 activity.",
    ),
    Reference(
        pmid="29415469",
        year=2018,
        authors=(
            "Barbagallo D", "Caponnetto A", "Cirnigliaro M", "Brex D",
            "Barbagallo C", "D'Angeli F", "Morrone A", "Caltabiano R",
            "Barbagallo GM", "Ragusa M", "Di Pietro C", "Hansen TB", "Purrello M",
        ),
        title="CircSMARCA5 Inhibits Migration of Glioblastoma Multiforme Cells by Regulating a Molecular Axis Involving Splicing Factors SRSF1/SRSF3/PTB.",
        journal="Int J Mol Sci",
        volume="19",
        issue="2",
        pages="480",
        nodes=("circSMARCA5", "Glioma"),
        edges=(("circSMARCA5", "Glioma"),),
        supports="circSMARCA5 is downregulated and anti-migratory in glioblastoma.",
    ),
    Reference(
        pmid="17681183",
        year=2007,
        authors=(
            "Meng F", "Henson R", "Wehbe-Janek H", "Ghoshal K", "Jacob ST",
            "Patel T",
        ),
        title="MicroRNA-21 regulates expression of the PTEN tumor suppressor gene in human hepatocellular cancer.",
        journal="Gastroenterology",
        volume="133",
        issue="2",
        pages="647-58",
        nodes=("miR-21", "PTEN", "HCC"),
        edges=(("miR-21", "PTEN"),),
        supports="miR-21 directly represses PTEN.",
    ),
    Reference(
        pmid="17968323",
        year=2008,
        authors=(
            "Asangani IA", "Rasheed SA", "Nikolova DA", "Leupold JH",
            "Colburn NH", "Post S", "Allgayer H",
        ),
        title="MicroRNA-21 (miR-21) post-transcriptionally downregulates tumor suppressor Pdcd4 and stimulates invasion, intravasation and metastasis in colorectal cancer.",
        journal="Oncogene",
        volume="27",
        issue="15",
        pages="2128-36",
        nodes=("miR-21", "PDCD4", "CRC"),
        edges=(("miR-21", "PDCD4"),),
        supports="miR-21 targets PDCD4 in colorectal cancer.",
    ),
    Reference(
        pmid="19144316",
        year=2009,
        authors=(
            "Lu LF", "Thai TH", "Calado DP", "Chaudhry A", "Kubo M", "Tanaka K",
            "Loeb GB", "Lee H", "Yoshimura A", "Rajewsky K", "Rudensky AY",
        ),
        title="Foxp3-dependent microRNA155 confers competitive fitness to regulatory T cells by targeting SOCS1 protein.",
        journal="Immunity",
        volume="30",
        issue="1",
        pages="80-91",
        nodes=("miR-155", "SOCS1"),
        edges=(("miR-155", "SOCS1"),),
        supports="miR-155 targets SOCS1.",
    ),
    Reference(
        pmid="17554337",
        year=2007,
        authors=(
            "He L", "He X", "Lim LP", "de Stanchina E", "Xuan Z", "Liang Y",
            "Xue W", "Zender L", "Magnus J", "Ridzon D", "Jackson AL",
            "Linsley PS", "Chen C", "Lowe SW", "Cleary MA", "Hannon GJ",
        ),
        title="A microRNA component of the p53 tumour suppressor network.",
        journal="Nature",
        volume="447",
        issue="7148",
        pages="1130-4",
        nodes=("TP53", "miR-34a"),
        edges=(("TP53", "miR-34a"),),
        supports="The miR-34 family is a p53-network effector.",
    ),
    Reference(
        pmid="18755897",
        year=2008,
        authors=("Yamakuchi M", "Ferlito M", "Lowenstein CJ"),
        title="miR-34a repression of SIRT1 regulates apoptosis.",
        journal="Proc Natl Acad Sci U S A",
        volume="105",
        issue="36",
        pages="13421-6",
        nodes=("miR-34a", "SIRT1"),
        edges=(("miR-34a", "SIRT1"),),
        supports="miR-34a represses SIRT1.",
    ),
    Reference(
        pmid="15766527",
        year=2005,
        authors=(
            "Johnson SM", "Grosshans H", "Shingara J", "Byrom M", "Jarvis R",
            "Cheng A", "Labourier E", "Reinert KL", "Brown D", "Slack FJ",
        ),
        title="RAS is regulated by the let-7 microRNA family.",
        journal="Cell",
        volume="120",
        issue="5",
        pages="635-47",
        nodes=("let-7a", "KRAS"),
        edges=(("let-7a", "KRAS"),),
        supports="let-7 directly represses RAS/KRAS.",
    ),
    Reference(
        pmid="17322030",
        year=2007,
        authors=("Mayr C", "Hemann MT", "Bartel DP"),
        title="Disrupting the pairing between let-7 and Hmga2 enhances oncogenic transformation.",
        journal="Science",
        volume="315",
        issue="5818",
        pages="1576-9",
        nodes=("let-7a", "HMGA2"),
        edges=(("let-7a", "HMGA2"),),
        supports="let-7 targeting of HMGA2 constrains oncogenic transformation.",
    ),
    Reference(
        pmid="18376396",
        year=2008,
        authors=(
            "Gregory PA", "Bert AG", "Paterson EL", "Barry SC", "Tsykin A",
            "Farshid G", "Vadas MA", "Khew-Goodall Y", "Goodall GJ",
        ),
        title="The miR-200 family and miR-205 regulate epithelial to mesenchymal transition by targeting ZEB1 and SIP1.",
        journal="Nat Cell Biol",
        volume="10",
        issue="5",
        pages="593-601",
        nodes=("miR-200c", "ZEB1"),
        edges=(("miR-200c", "ZEB1"),),
        supports="miR-200 family members target ZEB1 and suppress EMT.",
    ),
    Reference(
        pmid="17616664",
        year=2007,
        authors=(
            "Gramantieri L", "Ferracin M", "Fornari F", "Veronese A",
            "Sabbioni S", "Liu CG", "Calin GA", "Giovannini C", "Ferrazzi E",
            "Grazi GL", "Croce CM", "Bolondi L", "Negrini M",
        ),
        title="Cyclin G1 is a target of miR-122a, a microRNA frequently down-regulated in human hepatocellular carcinoma.",
        journal="Cancer Res",
        volume="67",
        issue="13",
        pages="6092-9",
        nodes=("miR-122", "CCNG1", "HCC"),
        edges=(("miR-122", "CCNG1"), ("miR-122", "HCC")),
        supports="miR-122 is lost in HCC and targets cyclin G1 (CCNG1).",
    ),
    Reference(
        pmid="19202062",
        year=2009,
        authors=(
            "Sachdeva M", "Zhu S", "Wu F", "Wu H", "Walia V", "Kumar S",
            "Elble R", "Watabe K", "Mo YY",
        ),
        title="p53 represses c-Myc through induction of the tumor suppressor miR-145.",
        journal="Proc Natl Acad Sci U S A",
        volume="106",
        issue="9",
        pages="3207-12",
        nodes=("miR-145", "MYC", "TP53"),
        edges=(("miR-145", "MYC"),),
        supports="miR-145, induced by p53, represses MYC.",
    ),
    Reference(
        pmid="17890317",
        year=2007,
        authors=(
            "Fabbri M", "Garzon R", "Cimmino A", "Liu Z", "Zanesi N",
            "Callegari E", "Liu S", "Alder H", "Costinean S",
            "Fernandez-Cymering C", "Volinia S", "Guler G", "Morrison CD",
            "Chan KK", "Marcucci G", "Calin GA", "Huebner K", "Croce CM",
        ),
        title="MicroRNA-29 family reverts aberrant methylation in lung cancer by targeting DNA methyltransferases 3A and 3B.",
        journal="Proc Natl Acad Sci U S A",
        volume="104",
        issue="40",
        pages="15805-10",
        nodes=("miR-29b", "DNMT3A"),
        edges=(("miR-29b", "DNMT3A"),),
        supports="miR-29 family members target DNMT3A/3B.",
    ),
    Reference(
        pmid="18483236",
        year=2008,
        authors=(
            "Kefas B", "Godlewski J", "Comeau L", "Li Y", "Abounader R",
            "Hawkinson M", "Lee J", "Fine H", "Chiocca EA", "Lawler S", "Purow B",
        ),
        title="microRNA-7 inhibits the epidermal growth factor receptor and the Akt pathway and is down-regulated in glioblastoma.",
        journal="Cancer Res",
        volume="68",
        issue="10",
        pages="3566-72",
        nodes=("miR-7", "EGFR", "Glioma"),
        edges=(("miR-7", "EGFR"),),
        supports="miR-7 represses EGFR and is lost in glioblastoma.",
    ),
    Reference(
        pmid="23636127",
        year=2013,
        authors=(
            "Wei J", "Wang F", "Kong LY", "Xu S", "Doucette T", "Ferguson SD",
            "Yang Y", "McEnery K", "Jethwa K", "Gjyshi O", "Qiao W",
            "Levine NB", "Lang FF", "Rao G", "Fuller GN", "Calin GA",
            "Heimberger AB",
        ),
        title="miR-124 inhibits STAT3 signaling to enhance T cell-mediated immune clearance of glioma.",
        journal="Cancer Res",
        volume="73",
        issue="13",
        pages="3913-26",
        nodes=("miR-124", "STAT3", "Glioma"),
        edges=(("miR-124", "STAT3"),),
        supports="miR-124 inhibits STAT3 signaling in glioma.",
    ),
    Reference(
        pmid="19008416",
        year=2008,
        authors=(
            "Varambally S", "Cao Q", "Mani RS", "Shankar S", "Wang X", "Ateeq B",
            "Laxman B", "Cao X", "Jing X", "Ramnarayanan K", "Brenner JC",
            "Yu J", "Kim JH", "Han B", "Tan P", "Kumar-Sinha C", "Lonigro RJ",
            "Palanisamy N", "Maher CA", "Chinnaiyan AM",
        ),
        title="Genomic loss of microRNA-101 leads to overexpression of histone methyltransferase EZH2 in cancer.",
        journal="Science",
        volume="322",
        issue="5908",
        pages="1695-9",
        nodes=("miR-101", "EZH2"),
        edges=(("miR-101", "EZH2"),),
        supports="miR-101 loss drives EZH2 overexpression.",
    ),
    Reference(
        pmid="19818710",
        year=2009,
        authors=("Juan AH", "Kumar RM", "Marx JG", "Young RA", "Sartorelli V"),
        title="Mir-214-dependent regulation of the polycomb protein Ezh2 in skeletal muscle and embryonic stem cells.",
        journal="Mol Cell",
        volume="36",
        issue="1",
        pages="61-74",
        nodes=("miR-214", "EZH2"),
        edges=(("miR-214", "EZH2"),),
        supports="miR-214 represses EZH2.",
    ),
    Reference(
        pmid="15944709",
        year=2005,
        authors=("O'Donnell KA", "Wentzel EA", "Zeller KI", "Dang CV", "Mendell JT"),
        title="c-Myc-regulated microRNAs modulate E2F1 expression.",
        journal="Nature",
        volume="435",
        issue="7043",
        pages="839-43",
        nodes=("MYC", "miR-17"),
        edges=(("MYC", "miR-17"),),
        supports="MYC transactivates the miR-17~92 cluster.",
    ),
    Reference(
        pmid="19137007",
        year=2009,
        authors=(
            "Chen X", "Guo X", "Zhang H", "Xiang Y", "Chen J", "Yin Y", "Cai X",
            "Wang K", "Wang G", "Ba Y", "Zhu L", "Wang J", "Yang R", "Zhang Y",
            "Ren Z", "Zen K", "Zhang J", "Zhang CY",
        ),
        title="Role of miR-143 targeting KRAS in colorectal tumorigenesis.",
        journal="Oncogene",
        volume="28",
        issue="10",
        pages="1385-92",
        nodes=("miR-143", "KRAS", "CRC"),
        edges=(("miR-143", "KRAS"),),
        supports="miR-143 targets KRAS in colorectal cancer.",
    ),
    Reference(
        pmid="21802130",
        year=2011,
        authors=("Salmena L", "Poliseno L", "Tay Y", "Kats L", "Pandolfi PP"),
        title="A ceRNA hypothesis: the Rosetta Stone of a hidden RNA language?",
        journal="Cell",
        volume="146",
        issue="3",
        pages="353-8",
        nodes=(),
        edges=(),
        supports="Conceptual source for lncRNA/circRNA sponge (ceRNA) edges in the atlas.",
    ),
    Reference(
        pmid="25964079",
        year=2016,
        authors=(
            "Yuan SX", "Wang J", "Yang F", "Tao QF", "Zhang J", "Wang LL",
            "Yang Y", "Liu H", "Wang ZG", "Xu QG", "Fan J", "Liu L", "Sun SH",
            "Zhou WP",
        ),
        title="Long noncoding RNA DANCR increases stemness features of hepatocellular carcinoma by derepression of CTNNB1.",
        journal="Hepatology",
        volume="63",
        issue="2",
        pages="499-511",
        nodes=("DANCR", "HCC"),
        edges=(),
        supports="DANCR as an oncogenic stemness lncRNA in hepatocellular carcinoma.",
    ),
    Reference(
        pmid="16914571",
        year=2006,
        authors=(
            "Wang XS", "Zhang Z", "Wang HC", "Cai JL", "Xu QW", "Li MQ",
            "Chen YC", "Qian XP", "Lu TJ", "Yu LZ", "Zhang Y", "Xin DQ",
            "Na YQ", "Chen WF",
        ),
        title="Rapid identification of UCA1 as a very sensitive and specific unique marker for human bladder carcinoma.",
        journal="Clin Cancer Res",
        volume="12",
        issue="16",
        pages="4851-8",
        nodes=("UCA1",),
        edges=(),
        supports="Discovery of UCA1 as a urothelial-cancer-associated lncRNA.",
    ),
    Reference(
        pmid="29371936",
        year=2017,
        authors=(
            "Zeng B", "Ye H", "Chen J", "Cheng D", "Cai C", "Chen G", "Chen X",
            "Xin H", "Tang C", "Zeng J",
        ),
        title="LncRNA TUG1 sponges miR-145 to promote cancer progression and regulate glutamine metabolism via Sirt3/GDH axis.",
        journal="Oncotarget",
        volume="8",
        issue="69",
        pages="113650-113661",
        nodes=("TUG1", "miR-145"),
        edges=(("TUG1", "miR-145"),),
        supports="TUG1 sponges miR-145.",
    ),
)


def _assert_references() -> None:
    pmids = [ref.pmid for ref in REFERENCES]
    if len(pmids) != len(set(pmids)):
        raise ValueError("Duplicate PMID in REFERENCES")
    if not 20 <= len(REFERENCES) <= 40:
        raise ValueError(f"Expected 20–40 references, got {len(REFERENCES)}")
    for ref in REFERENCES:
        for node_id in ref.nodes:
            if node_id not in NODE_BY_ID:
                raise ValueError(f"PMID {ref.pmid} cites unknown node {node_id}")
        for source, target in ref.edges:
            if source not in NODE_BY_ID or target not in NODE_BY_ID:
                raise ValueError(f"PMID {ref.pmid} cites unknown edge {source}→{target}")


_assert_references()


def references_for_node(node_id: str) -> list[Reference]:
    hits = [
        ref
        for ref in REFERENCES
        if node_id in ref.nodes or any(node_id in edge for edge in ref.edges)
    ]
    hits.sort(key=lambda ref: (ref.year, ref.pmid))
    return hits


def search_references(query: str) -> list[Reference]:
    q = query.strip().lower()
    ordered = sorted(REFERENCES, key=lambda ref: (ref.year, ref.pmid))
    if not q:
        return ordered
    hits: list[Reference] = []
    for ref in ordered:
        haystacks = (
            ref.pmid,
            ref.title,
            ref.journal,
            ref.supports,
            " ".join(ref.authors),
            " ".join(ref.nodes),
            " ".join(f"{a} {b}" for a, b in ref.edges),
        )
        if any(q in value.lower() for value in haystacks):
            hits.append(ref)
    return hits
