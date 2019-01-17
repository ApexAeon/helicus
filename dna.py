def transcribe(gene):
    matches = {"a":"u","t":"a","g":"c","c":"g"}
    transcription = ""
    for base in gene:
        transcription = transcription + matches[base]
    return transcription
def tokenize(mRNA):
    i = 0
    current_codon = ""
    codons = []
    for base in mRNA:
        i = i + 1
        current_codon = current_codon + base
        if i == 3:
            i = 0
            codons.append(current_codon)
            current_codon = ""
    return codons
def translate(codons):
    codon_matches = {
    "uuu":"phe",  "ucu":"ser",  "uau":"tyr",  "ugu":"cys",
    "uuc":"phe",  "ucc":"ser",  "uac":"tyr",  "ugc":"cys",
    "uua":"leu",  "uca":"ser",  "uaa":"stp",  "uga":"stp",
    "uug":"leu",  "ucg":"ser",  "uag":"stp",  "ugg":"trp",

    "cuu":"leu",  "ccu":"pro",  "cau":"his",  "cgu":"arg",
    "cuc":"leu",  "ccc":"pro",  "cac":"his",  "cgc":"arg",
    "cua":"leu",  "cca":"pro",  "cag":"gln",  "cga":"arg",
    "cug":"leu",  "ccg":"pro",  "caa":"gln",  "cgg":"arg",

    "auu":"ile",  "acu":"thr",  "aau":"asn",  "agu":"ser",
    "auc":"ile",  "acc":"thr",  "aac":"asn",  "agc":"ser",
    "aua":"ile",  "aca":"thr",  "aaa":"lys",  "aga":"arg",
    "aug":"met",  "acg":"thr",  "aag":"lys",  "agg":"arg",

    "guu":"val",  "gcu":"ala",  "gau":"asp",  "ggu":"gly",
    "guc":"val",  "gcc":"ala",  "gac":"asp",  "ggc":"gly",
    "gua":"val",  "gca":"ala",  "gaa":"glu",  "gga":"gly",
    "gug":"val",  "gcg":"ala",  "gag":"glu",  "ggg":"gly"
    }
    amino_acids = []
    for codon in codons:
        amino_acids.append(codon_matches[codon])
    return amino_acids
def transfer_rna(gene):
    matches = {"a":"u","u":"a","g":"c","c":"g"}
    transcription = ""
    for base in gene:
        transcription = transcription + matches[base]
    return transcription   
while True:
    gene = input("Input Gene: ")
    print("Gene:             ",end=" ")
    for dna_codon in tokenize(gene):
        print(dna_codon,end=" ")
    print("\nRNA Transcription:",end=" ")
    for rna_codon in tokenize(transcribe(gene)):
        print(rna_codon,end=" ")
    print("\nAmino Acids:      ",end=" ")
    for amino in translate(tokenize(transcribe(gene))):
        print(amino,end=" ")
    print("\ntRNA:             ",end=" ")
    for rna_codon in tokenize(transfer_rna(transcribe(gene))):
        print(rna_codon,end=" ")
    print("\n================")

