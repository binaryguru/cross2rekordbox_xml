import argparse

parser = argparse.ArgumentParser(prog='Cross2Rekordbox_XML',
                                 description='Tool to fix beatgrid offsets in rekordbox.xml exported by Mixvibes Cross.')
parser.add_argument('-d', '--dump', action='store_true',
                    help='Dump fixed XML to standard output instead of file')
args = parser.parse_args()
