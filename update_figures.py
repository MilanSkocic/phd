import os
import shutil
import argparse

parser = argparse.ArgumentParser(description="Update figures in chapters")
# group = parser.add_mutually_exclusive_group()
parser.add_argument("-v", "--verbose", action="store_true", help='All outputs')
parser.add_argument("-c","--chapters", type=int, nargs='+', required=True,
                    help="Copy the figure of the given chapter number")
args = parser.parse_args()

dir_chapter = './mainmatter/'
chapters = []

for i in args.chapters:
    chapters.append('chapter_' + str(i))

root_directory = 'C:/Users/mskocic/Documents/1-PhD/'
fig_folder_name = 'figures'

folders = ['1-Bibliography/4-Pictures/Extracted/',
    '1-Bibliography/4-Pictures/Plots/png/',
    '1-Bibliography/4-Pictures/Drawings/',
    '3-Experiments/140778-Galvanic_Coupling-MA/2-Pictures/Plots/',
    '3-Experiments/140778-Galvanic_Coupling-MA/2-Pictures/Drawings/',
    '3-Experiments/140778-Galvanic_Coupling-MA/2-Pictures/Plots/png/',
'3-Experiments/140778-Galvanic_Coupling-MA/1-Data/SEM/Extracted_Pictures/',
    '3-Experiments/130008-Sapphire_Aging-MA/2-Pictures/Plots/png/',
    '3-Experiments/131293-Comparison_X718_X750-A33/2-Pictures/Plots/png/',
    '3-Experiments/140834-UV_Source_Comparison-SHC/2-Pictures/Plots/png/',
    '3-Experiments/141059-Chemistry_Effect-SHC/2-Pictures/Plots/png/',
    '3-Experiments/141059-Chemistry_Effect-SHC/2-Pictures/Drawings/',
    '3-Experiments/150215-Chemistry_Effect-SHC/2-Pictures/Plots/png/',
    '3-Experiments/150215-Chemistry_Effect-SHC/2-Pictures/Drawings/png/',
    '3-Experiments/150888-X750-SHC/2-Pictures/Plots/png/',
    '3-Experiments/150569-Fe_coating-SHC/2-Pictures/Plots/png/',
    '2-Design_Shadow_Cell/Pictures/Drawings/',
    '2-Design_Shadow_Cell/Pictures/Extracted/',
    '2-Design_Shadow_Cell/Pictures/Plots/png/',
    '6-Programming/Python/PEC/Testing_CI/2-Pictures/png/']

source_folders = []
for i in folders:
    source_folders.append(root_directory + i)


for i in chapters:
    if args.verbose:
        print(i)
    chapter_path = dir_chapter + i + '/' + fig_folder_name + '/'
    lof = os.listdir(chapter_path)
    found_figures = []
    not_found_figures = []
    for j in lof:
        found = False
        for k in source_folders:
            if os.path.exists(k + j) is True:
                found = True
                found_figures.append(k + j)
                break
            else:
                found = False
                not_found_figures.append(j)
        if found is False:
            if args.verbose:
                print('\t' + j + '   --->   Not found' )

    if len(found_figures) == len(lof):
        if args.verbose:
            print('\tAll figures were found.')
    else:
        if args.verbose:
            print('All figures were not found')

    for ff in found_figures:
        try:
            if args.verbose:
                print('\tCopying ' + os.path.basename(ff))
            shutil.copyfile(ff, chapter_path+os.path.basename(ff))
        except IOError as err:
            if args.verbose:
                print(ff + ' could not be copied')

