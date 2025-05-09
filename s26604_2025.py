"""
Program: Random DNA Sequence Generator in FASTA Format
Author: s26604
"""

import random

# Function to generate a random DNA sequence of specified length
def generate_dna_sequence(length):
    """Generates a random DNA sequence of given length."""
    return ''.join(random.choices('ACGT', k=length))

# Function to insert the user's name at a random position in the DNA sequence
def insert_name(sequence, name):
    """Inserts the given name at a random position in the DNA sequence."""
    position = random.randint(0, len(sequence))
    return sequence[:position] + name + sequence[position:]

# Function to calculate nucleotide statistics (excluding the inserted name)
def calculate_statistics(sequence, name):
    """Calculates percentage of A, C, G, T and CG% excluding the name."""
    clean_seq = sequence.replace(name, "")
    total = len(clean_seq)

    # ORIGINAL:
    # stats = {nuc: clean_seq.count(nuc) for nuc in 'ACGT'}
    # MODIFIED (clarity improvement: use individual variables to clarify logic and allow reuse):
    count_A = clean_seq.count('A')
    count_C = clean_seq.count('C')
    count_G = clean_seq.count('G')
    count_T = clean_seq.count('T')
    stats = {'A': count_A, 'C': count_C, 'G': count_G, 'T': count_T}

    # Calculate percentages
    percentages = {nuc: round((count / total) * 100, 1) for nuc, count in stats.items()}
    cg = count_C + count_G
    cg_percent = round((cg / total) * 100, 1)
    return percentages, cg_percent

# Function to format sequence to 60 characters per line (FASTA formatting)
def format_fasta_sequence(seq):
    """Formats a sequence string into lines of 60 characters."""
    return '\n'.join(seq[i:i+60] for i in range(0, len(seq), 60))

def main():
    # Ask the user for required inputs
    try:
        length = int(input("Enter the sequence length: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        print("Invalid input:", e)
        return

    seq_id = input("Enter the sequence ID: ").strip()
    description = input("Provide a description of the sequence: ").strip()
    name = input("Enter your name: ").strip()

    # ORIGINAL:
    # dna_seq = generate_dna_sequence(length)
    # MODIFIED (traceability: add print statement to visualize the raw sequence before name insertion):
    dna_seq = generate_dna_sequence(length)
    # print("Generated DNA (without name):", dna_seq)

    # Insert name into sequence
    dna_seq_with_name = insert_name(dna_seq, name)

    # Calculate and display statistics
    percentages, cg_percent = calculate_statistics(dna_seq_with_name, name)

    # Format final sequence in proper FASTA layout
    formatted_sequence = format_fasta_sequence(dna_seq_with_name)

    # Save to FASTA file
    fasta_filename = f"{seq_id}.fasta"

    # ORIGINAL:
    # with open(fasta_filename, 'w') as fasta_file:
    #     fasta_file.write(f">{seq_id} {description}\n")
    #     fasta_file.write(dna_seq_with_name + "\n")
    # MODIFIED (readability and formatting: apply 60-character formatting):
    with open(fasta_filename, 'w') as fasta_file:
        fasta_file.write(f">{seq_id} {description}\n")
        fasta_file.write(formatted_sequence + "\n")

    # Display summary and statistics to user
    print(f"\nThe sequence was saved to the file {fasta_filename}")
    print("Sequence statistics:")
    for nuc in 'ACGT':
        print(f"{nuc}: {percentages[nuc]}%")
    print(f"%CG: {cg_percent}")

# Program entry point
if __name__ == "__main__":
    main()
