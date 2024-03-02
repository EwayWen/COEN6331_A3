import numpy as np
import patterns


def validate_patterns():
    for pattern in patterns.patterns:
        assert len(pattern) == 120
        line = ""
        for count, pixel in enumerate(pattern):
            line += "X" if pixel == 1 else "_"
            if (count + 1) % 10 == 0:
                print(line)
                line = ""
        print("\n\n")


if __name__ == '__main__':
    validate_patterns()
