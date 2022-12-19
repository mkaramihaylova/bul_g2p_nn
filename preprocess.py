#!/usr/bin/env python3

import argparse
import pandas as pd


def main(args: argparse.Namespace) -> None:
    with open(args.input, "r") as file:
        with open(args.col_1, "w") as column_1:
            with open(args.col_2, "w") as column_2:
                df = pd.read_csv(file, delimiter="\t")
                word_df = df.set_axis(
                    ["word1", "word2"], axis=1, inplace=False
                )
                word1 = word_df["word1"].to_list()
                word2 = word_df["word2"].to_list()

                for word in word1:
                    print(" ".join(word), file=column_1)

                for word in word2:
                    print(" ".join(word), file=column_2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input tsv file path")
    parser.add_argument("col_1", help="spaced column 1 output file path")
    parser.add_argument("col_2", help="spaced column 2 output file path")
    main(parser.parse_args())
