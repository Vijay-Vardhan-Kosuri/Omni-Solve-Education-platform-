"""
Biology & Life Sciences Solver Engine
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

class BiologyEngine:
    """
    Comprehensive Biology & Life Sciences Solver covering:
    - Genetics & Mendelian Inheritance (Monohybrid / Dihybrid Crosses, Punnett Square)
    - Cell Biology & Metabolism (Mitosis, Meiosis, Glycolysis, Krebs Cycle, Photosynthesis)
    - Molecular Biology (DNA Replication, RNA Transcription, Translation & Genetic Code)
    - Human Physiology (Nervous system action potential, Circulatory, Excretory, Endocrine)
    - Ecology & Evolution (Trophic levels, Natural selection, Hardy-Weinberg Equilibrium)
    """

    @staticmethod
    def solve_doubt(title, question_text, latex_formula=""):
        combined_text = f"{title} {question_text} {latex_formula}".lower()

        if any(term in combined_text for term in ['genetics', 'punnett', 'allele', 'dominant', 'recessive', 'genotype', 'phenotype', 'mendel']):
            steps = BiologyEngine._solve_genetics(combined_text)
        elif any(term in combined_text for term in ['dna', 'rna', 'transcription', 'translation', 'codon', 'replication', 'polymerase']):
            steps = BiologyEngine._solve_molecular_biology(combined_text)
        elif any(term in combined_text for term in ['cell', 'mitosis', 'meiosis', 'atp', 'krebs', 'photosynthesis', 'respiration']):
            steps = BiologyEngine._solve_cell_biology(combined_text)
        elif any(term in combined_text for term in ['hardy-weinberg', 'ecology', 'population', 'evolution', 'trophic']):
            steps = BiologyEngine._solve_ecology(combined_text)
        else:
            steps = BiologyEngine._solve_general_biology(combined_text)

        return {
            'subject': 'Biology',
            'category': 'Core Biology Solver',
            'steps': steps
        }

    @staticmethod
    def _solve_genetics(text):
        return [
            {
                'title': 'Identify Parent Genotypes',
                'explanation': 'Determine parental alleles (e.g. Heterozygous Aa x Heterozygous Aa or Homozygous AA x aa).',
                'formula': r'P_1: Aa \times Aa'
            },
            {
                'title': 'Construct Punnett Square Matrix',
                'explanation': 'Grid breakdown: Gametes A and a from Parent 1 combine with A and a from Parent 2 -> AA, Aa, Aa, aa.',
                'formula': r'\begin{matrix} & A & a \\ A & AA & Aa \\ a & Aa & aa \end{matrix}'
            },
            {
                'title': 'Calculate Genotypic & Phenotypic Ratios',
                'explanation': 'Genotypic Ratio: 1 AA : 2 Aa : 1 aa (1:2:1). Phenotypic Ratio (Dominant vs Recessive): 3 Dominant : 1 Recessive (3:1, or 75% : 25%).',
                'formula': r'\text{Genotypic: } 1:2:1, \quad \text{Phenotypic: } 3:1'
            }
        ]

    @staticmethod
    def _solve_molecular_biology(text):
        return [
            {
                'title': 'Identify DNA/RNA Strand Orientation & Pairing',
                'explanation': 'DNA complementary base pairing: Adenine (A) pairs with Thymine (T), Cytosine (C) with Guanine (G). In RNA, Thymine is replaced by Uracil (U).',
                'formula': r'\text{DNA: 5\'-ATCG-3\' } \longrightarrow \text{mRNA: 3\'-UAGC-5\'}'
            },
            {
                'title': 'Trace Transcription & Translation Codons',
                'explanation': 'mRNA codons read in triplets (5\' to 3\') starting from AUG (Methionine Start Codon) until UAA, UAG, or UGA (Stop Codons).',
                'formula': r'\text{Codon: AUG } \longrightarrow \text{Amino Acid: Methionine (Start)}'
            },
            {
                'title': 'Synthesize Polypeptide Chain',
                'explanation': 'tRNA anticodons deliver corresponding amino acids to ribosome A-site, creating peptide bonds.',
                'formula': r'\text{Ribosome } (\text{P-site} \rightarrow \text{A-site peptide bond formation})'
            }
        ]

    @staticmethod
    def _solve_cell_biology(text):
        return [
            {
                'title': 'Identify Metabolic Stage or Cell Cycle Phase',
                'explanation': 'Determine cellular process: Interphase (G1, S phase DNA replication, G2) -> Mitosis (Prophase, Metaphase, Anaphase, Telophase).',
                'formula': r'\text{Cell Cycle: G1 } \rightarrow \text{ S } \rightarrow \text{ G2 } \rightarrow \text{ M}'
            },
            {
                'title': 'Trace ATP / Energy Yield',
                'explanation': 'Glycolysis (2 ATP, 2 NADH) -> Pyruvate Oxidation -> Krebs Cycle (2 ATP, 6 NADH, 2 FADH2) -> Electron Transport Chain (~30-32 total ATP).',
                'formula': r'C_6H_{12}O_6 + 6O_2 \longrightarrow 6CO_2 + 6H_2O + 32 \text{ ATP}'
            },
            {
                'title': 'Conclusion & Cellular Function',
                'explanation': 'Explain role of organelles (Mitochondria, Chloroplasts, Endoplasmic Reticulum, Golgi Body).',
                'formula': r'\text{Photosynthesis: } 6CO_2 + 6H_2O + \text{light} \rightarrow C_6H_{12}O_6 + 6O_2'
            }
        ]

    @staticmethod
    def _solve_ecology(text):
        return [
            {
                'title': 'Identify Population & Ecosystem Model',
                'explanation': 'For allele frequency in population equilibrium, apply Hardy-Weinberg Equation: p^2 + 2pq + q^2 = 1 and p + q = 1.',
                'formula': r'p + q = 1, \quad p^2 + 2pq + q^2 = 1'
            },
            {
                'title': 'Calculate Allele & Genotype Frequencies',
                'explanation': 'If q^2 (recessive phenotype frequency) is given, compute q = sqrt(q^2), p = 1 - q, and 2pq (heterozygotes).',
                'formula': r'q = \sqrt{\text{recessive frequency}}, \quad p = 1 - q'
            },
            {
                'title': 'Ecosystem Energy Pyramids & 10% Rule',
                'explanation': 'Energy transfer between trophic levels: Producers (100%) -> Primary Consumers (10%) -> Secondary Consumers (1%).',
                'formula': r'E_{\text{next}} = 0.10 \times E_{\text{current}}'
            }
        ]

    @staticmethod
    def _solve_general_biology(text):
        return [
            {
                'title': 'Biological Concept Analysis',
                'explanation': 'Analyze anatomical, physiological, or taxonomic characteristics of given organism/system.',
                'formula': r'\text{Kingdom } \rightarrow \text{ Phylum } \rightarrow \text{ Class } \rightarrow \text{ Order}'
            },
            {
                'title': 'Physiological Mechanism Breakdown',
                'explanation': 'Detail homeostatic feedback loops (positive/negative feedback control).',
                'formula': r'\text{Stimulus } \rightarrow \text{ Receptor } \rightarrow \text{ Control Center } \rightarrow \text{ Effector}'
            },
            {
                'title': 'Summary & Significance',
                'explanation': 'Summarize biological relevance and evolutionary significance.',
                'formula': r'\text{Homeostasis maintained}'
            }
        ]
