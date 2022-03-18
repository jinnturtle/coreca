#!/usr/bin/python3

import sys
program_name = "Compound Reliability Calculator"
ver_maj = 0
ver_min = 1
ver_patch = 0

def ver_str():
    return f"v{ver_maj}.{ver_min}.{ver_patch}"

def about():
    print("\n*** {} {} ***".format(program_name, ver_str()))
    print("Derives compound reliability percentage given list of percentages.")
    print("\nUSAGE:")
    print("\t {} <filepath>".format(sys.argv[0]))

def use_err(text):
    print(f"ERROR: {text}")
    about()

def read_chances(filename):
    print(f"processing {filename}")
    with open(filename) as f:
        lines = f.readlines();

    chances = []
    for l in lines:
        chances.append(float(l) / 100)

    return chances

def main():
    if len(sys.argv) < 2:
        use_err("no file supplied")
        exit(1)

    chances = read_chances(str(sys.argv[1]))

    total_sc = 1.0
    for i,sc in enumerate(chances):
        total_sc *= sc
        print("{}: {:02.02f} ({:02.02f})".format(i, total_sc*100, sc*100))

main()
