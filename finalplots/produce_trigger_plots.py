import argparse
import flatanalysis
import mplhep
import matplotlib.pyplot as plt
import os.path as osp, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('year', choices=['2016', '2017', '2018', 'all'], nargs='*', type=str)
    args = parser.parse_args()
    if 'all' in args.year: args.year = ['2016', '2017', '2018']
    for year in args.year:
        signals = flatanalysis.samples.init_sigs_nohtcut(year, max_entries=None, progressbar=True)
        for variable in ['ht', 'jetpt', 'mt', 'met', 'msd']:
            flatanalysis.trigger.trigger_plots_for_year_signal(year, variable, signals=signals)

if __name__ == '__main__':
    main()