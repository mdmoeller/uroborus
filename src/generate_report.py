#!/usr/bin/python

import sys

def usage_and_quit():
    sys.stderr.write("usage: generate_report.py <source>")
    sys.exit(1)

def html_color(color, brightness=1.0):
    """Computes an html string for an int color on [0,120] and a float brightness on [0,1]."""

    # On invalid input, return blue.
    if color < 0 or color > 120 or brightness < 0 or brightness > 1.0:
        print color, brightness
        return "#0000ff"

    adjusted_brightness = 0.75 * brightness

    html_color = "#"

    # Compute red and append
    red = int(min(-255.0 * color / 60.0 + 510, 255.0) * adjusted_brightness)
    red_hex = hex(red)[2:]
    if len(red_hex) == 1:
        red_hex = "0" + red_hex

    html_color += red_hex


    # Compute green and append
    green = int(min(255.0 * color / 60.0, 255.0) * adjusted_brightness)
    green_hex = hex(green)[2:]
    if len(green_hex) == 1:
        green_hex = "0" + green_hex

    html_color += green_hex

    # We never use any blue:
    html_color += "00"

    return html_color


def compute_color(pct_passed, pct_failed):
    """Computes a hue value between 0 and 120 according to the formula in the Tarantula paper.

    Very red (likely failure): 0
    Very green (likely OK): 120"""

    return pct_passed / (pct_passed + pct_failed) * 120

def compute_brightness(pct_passed, pct_failed):
    """Computes a brightness value between 0 and 1 according to the formula in the Tarantula paper. """

    return max(pct_passed, pct_failed)


def main():
    args = sys.argv

    if len(args) != 2:
        usage_and_quit()

    source_filename = args[1]
    basename = source_filename.split('.')[0]

    
    # Assumes the coverage and pass/fail files have default names
    # as created by Instrum.py
    SOURCE = open(source_filename, 'r')
    PASSFAIL = open(basename + "_passfail.txt", 'r')
    COVERAGE = open(basename + "_coverage.txt", 'r')

    # Map from run number to bool, indicating pass or failure for the run
    #    essentially is just an array read in from the passfail file
    all_runs_passfail = {}
    total_passes = 0
    total_fails = 0


    # Read the passfail file into all_runs_passfail
    for line in PASSFAIL.readlines():
        run_and_result = line.split('\t')

        run_number = int(run_and_result[0].strip())

        # 'passfail' is whether the current line passed or failed
        passfail = bool(int(run_and_result[1].strip()))


        all_runs_passfail[run_number] = passfail
        if passfail:
            total_passes += 1
        else:
            total_fails += 1


    # If everything passed or everything failed, we can't continue,
    #     because in either case "pass/fail percentages" wouldn't make sense
    if total_passes == 0 or total_fails == 0:
        sys.stderr.write("Cannot compute percentages: require non-zero number of passes and fails\n")
        sys.exit(2)


    # Maps every statement number to a list of unique runs that cover it
    stmt_run_cover = {}

    # Fill the stmt_run_cover dictionary
    for line in COVERAGE.readlines():
        stmt_and_run = line.split('\t')
        stmt_num = int(stmt_and_run[0].strip())
        run_num = int(stmt_and_run[1].strip())

        if stmt_num not in stmt_run_cover.keys():
            stmt_run_cover[stmt_num] = []

        if run_num not in stmt_run_cover[stmt_num]:
            stmt_run_cover[stmt_num].append(run_num)


    # Maps every statement to a list [p, f] where p and f are the numbers of RUNS
    #     that cover it and respectively passed and failed
    stmt_passfail_count = {}
    for stmt in stmt_run_cover.keys():
        passed = 0
        failed = 0
        for run in stmt_run_cover[stmt]:
            if all_runs_passfail[run]:
                passed += 1
            else:
                failed += 1
        stmt_passfail_count[stmt] = [passed, failed]


    stmt_html_colors = {}

    # Compute the colors (range 0-120) for each statement
    for stmt in stmt_passfail_count.keys():
        passfail = stmt_passfail_count[stmt]
        pass_pct = float(passfail[0])/total_passes
        fail_pct = float(passfail[1])/total_fails

        color = compute_color(pass_pct, fail_pct)
        brightness = compute_brightness(pass_pct, fail_pct)

        stmt_html_colors[stmt] = html_color(color, brightness)


    # Set up the html output file:
    HTML_OUT = open(basename + "_deprecated_report.html", 'w')

    HTML_OUT.write("<html>\n")

    HTML_OUT.write('<body bgcolor="#e0e0e0">\n')
    source = SOURCE.readlines()


    num_lines = len(source)
    # Since stmt_html_colors uses "line numbers" starting at 1, and
    #   source is just an array of lines from the source, the line numbers
    #   need to be bumped by 1 for references to stmt_html_colors
    for i in range(num_lines):

        # Adjust line number alignment
        prepad = ""
        if num_lines > 10 and i < 9:
            prepad = "0"
        if num_lines > 100 and i < 99:
            prepad = prepad + "0"
        if num_lines > 1000 and i < 999:
            prepad = prepad + "0"

        # Print the line number
        HTML_OUT.write('<font face="Courier New" color="#0000ff">' + prepad + str(i+1) + ': </font>\n')

        # Indent properly
        for c in source[i]:
            if c == ' ':
                HTML_OUT.write('&nbsp;'*2)
            elif c== '\t':
                HTML_OUT.write('&nbsp;'*8)
            else:
                break

        # Whether we have a calculated color or not (we might not if it wasn't instrumented)
        if i+1 in stmt_html_colors:
            HTML_OUT.write('<font face="Courier New" color="' + stmt_html_colors[i+1] + '">' + source[i] + '</font><br>\n')

        # If we don't have a color, just brint the line black
        else:
            HTML_OUT.write('<font face="Courier New" color="#000000">' + source[i] + '</font><br>\n')

    HTML_OUT.write("</body></html>\n")
    
main()
