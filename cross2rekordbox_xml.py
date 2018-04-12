# -*- coding: utf-8 -*-
# cross2rekordbox_xml.py
# Author: André Perron
# E-mail: andre.perron@gmail.com
# Version: 0.1

import sys
import argparse
import elementtree.ElementTree as ET

parser = argparse.ArgumentParser(prog='cross_rekordbox_xml_offset_fix',
                                 description='Fixes beatgrid offsets in exported rekordbox.xml file.')
parser.add_argument('-d', '--dump', action='store_true',
                    help='Dump fixed XML to standard output instead of file')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Display a list of items fixed in the output file')
parser.add_argument('-D', '--debug', action='store_true',
                    help='Enable debug mode')
args = parser.parse_args()

offset = float(0.024)
input_file = open('m0du1us.mp3.xml', 'r')
output_file = open('fixed_m0du1us.mp3.xml', 'w')
entry_num = int(0)

if args.debug:
    print args.accumulate(args.integers)
    print 'sys.api_version: {}'.format(sys.api_version)
    print 'sys.argv: {}'.format(sys.argv)
    print 'sys.builtin_module_names: {}'.format(sys.builtin_module_names)
    print 'sys.byteorder: {}'.format(sys.byteorder)
    print 'sys.copyright: {}'.format(sys.copyright)
    print 'sys.dllhandle: {}'.format(sys.dllhandle)
    print 'sys.dont_write_bytecode: {}'.format(sys.dont_write_bytecode)
    #print 'sys.exc_traceback: {}'.format(sys.exc_traceback)
    #print 'sys.exc_value: {}'.format(sys.exc_value)
    print 'sys.exec_prefix: {}'.format(sys.exec_prefix)
    print 'sys.executable: {}'.format(sys.executable)
    print 'sys.flags: {}'.format(sys.flags)
    print 'sys.float_info: {}'.format(sys.float_info)
    print 'sys.float_repr_style: {}'.format(sys.float_repr_style)
    print 'sys.hexversion: {}'.format(sys.hexversion)
    print 'sys.long_info: {}'.format(sys.long_info)
    print 'sys.maxint: {}'.format(sys.maxint)
    print 'sys.maxsize: {}'.format(sys.maxsize)
    print 'sys.maxunicode: {}'.format(sys.maxunicode)
    print 'sys.meta_path: {}'.format(sys.meta_path)
    print 'sys.modules: {}'.format(sys.modules)
    print 'sys.path: {}'.format(sys.path)
    print 'sys.path_hooks: {}'.format(sys.path_hooks)
    print 'sys.path_importer_cache: {}'.format(sys.path_importer_cache)
    print 'sys.platform: {}'.format(sys.platform)
    print 'sys.prefix: {}'.format(sys.prefix)
    print 'sys.py3kwarning: {}'.format(sys.py3kwarning)
    print 'sys.stderr: {}'.format(sys.stderr)
    print 'sys.stdin: {}'.format(sys.stdin)
    print 'sys.stdout: {}'.format(sys.stdout)
    print 'sys.version: {}'.format(sys.version)
    print 'sys.version_info: {}'.format(sys.version_info)
    print 'sys.warnoptions: {}'.format(sys.warnoptions)
    print 'sys.winver: {}'.format(sys.winver)
else:
    pass

tree = ET.ElementTree(file=input_file)
collection_entries = tree.getroot().find('.//COLLECTION').get('Entries')
#xml_comment = ET.Comment(text='_COMMENT_')

if args.verbose:
    print 'offset={}'.format(offset)
    print 'input_file="{}"'.format(input_file.name)
    print 'output_file="{}"'.format(output_file.name)
    print 'COLLECTION Entries="{}"'.format(collection_entries)
else:
    pass

track_list = tree.getroot().findall('.//COLLECTION/TRACK')
for track_entry, track in enumerate(track_list):
    if args.verbose:
        print '{}: TRACK TrackID="{}"'.format(
            track_entry, track.get('TrackID'))
    else:
        pass

    tempo_list = track.getiterator(tag='TEMPO')
    for tempo_entry, tempo in enumerate(tempo_list):
        tempo_inizio = tempo.get('Inizio')
        tempo_inizio_fixed = float(tempo_inizio) + offset
        tempo.set('Inizio', str(tempo_inizio_fixed))
        if args.verbose:
            print '    TEMPO Inizio="{}" -> {}'.format(
                tempo_inizio, tempo.get('Inizio'))
        else:
            pass

    position_mark_list = track.getiterator(tag='POSITION_MARK')
    for position_mark_entry, position_mark in enumerate(position_mark_list):
        position_mark_start = position_mark.get('Start')
        position_mark_start_fixed = float(position_mark_start) + offset
        position_mark.set('Start', str(position_mark_start_fixed))
        if args.verbose:
            print '    POSITION_MARK Start="{}" -> {}'.format(
                position_mark_start, position_mark.get('Start'))
        else:
            pass

if args.dump:
    print '<?xml version="1.0" encoding="utf-8"?>\n'
    ET.dump(tree)
    output_file.close
    input_file.close
    exit
else:
    output_file.seek(0)
    output_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
    tree.write(output_file, encoding="utf-8")
    output_file.flush
    output_file.close
    input_file.close
    exit