#!/usr/bin/env python3

import argparse


def main(args: argparse.Namespace) -> None:
    with open(args.input, "r") as file:
        pred = file.readlines()
        predictions = [i.strip() for i in pred]

        target_word_list = []
        hyp_word_list = []

        for line in predictions:
            if line.startswith("T-"):
                target_word_list.append(line.split("\t")[-1])

        for line in predictions:
            if line.startswith("H-"):
                hyp_word_list.append(line.split("\t")[-1])

        num_not_equal = sum(
            word1 != word2
            for word1, word2 in zip(target_word_list, hyp_word_list)
        )

        wer = (num_not_equal / len(target_word_list)) * 100
        print("WER =", round(wer))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input file path")
    main(parser.parse_args())
