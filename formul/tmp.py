from formul import exprtosol, exprtoans
import re


def quote(match):
    return ''.join(['"', match.group(1), '"'])


formula = input()

formula = formula.replace(" ", "")
parts = formula.split("=")
nparts = len(parts)

if nparts == 1:
    output = exprtosol(parts[0]).replace("'|'", "")
    print(output)
elif nparts == 2:
    print(exprtoans(parts[0]) + " = " + exprtoans(parts[1]) + ";")
    # output = ''.join([exprtosol(parts[0]), "'='", exprtosol(parts[1])])
    # output = output.replace("'|'", '')
    # output = output.replace('"|\'', '')
    # output = output.replace('\'|"', '')
    # output = re.sub(r"'([\w=\-+()]{2,})'", quote, output)
    # output = re.sub(r"\"([\w=\-+()]+)'", quote, output)
    # output = re.sub(r"'([\w=\-+()]+)\"", quote, output)
    # print(output)
elif nparts > 2:
    print(exprtosol(parts[0]), end='')
    for part in parts[1:]:
        print("'='" + exprtosol(part), end='')
