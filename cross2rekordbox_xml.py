#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Tool to fix beatgrid offsets in rekordbox.xml exported by Mixvibes Cross.
#
# Copyright (c) 2018-2019 by André Perron.  All rights reserved.
#
# binaryguruca@yahoo.ca
# https://github.com/binaryguru
# https://binaryguru.wordpress.com

"""
MIT License

Copyright (c) 2018 André Perron

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import argparse as AP
import elementtree.ElementTree as ET

# Commandline argument parsing
PARSER = AP.ArgumentParser(prog='cross2rekordbox_xml',
                           description='Tool to fix beatgrid offsets in'
                           'rekordbox.xml exported by Mixvibes Cross.')
PARSER.add_argument('-d', '--dump', action='store_true',
                    help='Dump fixed XML to standard output instead of file')
PARSER.add_argument('-v', '--verbose', action='store_true',
                    help='Display a list of items fixed in the output file')
PARSER.add_argument('-D', '--debug', action='store_true',
                    help='Enable debug mode')
ARGS = PARSER.parse_args()

# Initial variables
OFFSET = float(0.024)
INPUT_FILE = open('m0du1us.mp3.xml', 'r')
OUTPUT_FILE = open('fixed_m0du1us.mp3.xml', 'w')
ENTRY_NUM = int(0)

if ARGS.debug:
    print ARGS.accumulate(ARGS.integers)
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

TREE = ET.ElementTree(file=INPUT_FILE)
COLLECTION_ENTRIES = TREE.getroot().find('.//COLLECTION').get('Entries')

if ARGS.verbose:
    print 'OFFSET={}'.format(OFFSET)
    print 'INPUT_FILE="{}"'.format(INPUT_FILE.name)
    print 'OUTPUT_FILE="{}"'.format(OUTPUT_FILE.name)
    print 'COLLECTION Entries="{}"'.format(COLLECTION_ENTRIES)
else:
    pass

TRACK_LIST = TREE.getroot().findall('.//COLLECTION/TRACK')
for track_entry, track in enumerate(TRACK_LIST):
    if ARGS.verbose:
        print '{}: TRACK TrackID="{}"'.format(
            track_entry, track.get('TrackID'))
    else:
        pass

    tempo_list = track.getiterator(tag='TEMPO')
    for tempo_entry, tempo in enumerate(tempo_list):
        tempo_inizio = tempo.get('Inizio')
        tempo_inizio_fixed = float(tempo_inizio) + OFFSET
        tempo.set('Inizio', str(tempo_inizio_fixed))
        if ARGS.verbose:
            print '    TEMPO Inizio="{}" -> {}'.format(
                tempo_inizio, tempo.get('Inizio'))
        else:
            pass

    position_mark_list = track.getiterator(tag='POSITION_MARK')
    for position_mark_entry, position_mark in enumerate(position_mark_list):
        position_mark_start = position_mark.get('Start')
        position_mark_start_fixed = float(position_mark_start) + OFFSET
        position_mark.set('Start', str(position_mark_start_fixed))
        if ARGS.verbose:
            print '    POSITION_MARK Start="{}" -> {}'.format(
                position_mark_start, position_mark.get('Start'))
        else:
            pass

if ARGS.dump:
    # Add XML version and encoding to top of dump
    print '<?xml version="1.0" encoding="utf-8"?>\n'
    ET.dump(TREE)  # Dump XML tree to sys.stdout
    OUTPUT_FILE.close()
    INPUT_FILE.close()
    exit()
else:
    OUTPUT_FILE.seek(0)
    # Add XML version and encoding to top of file
    OUTPUT_FILE.write('<?xml version="1.0" encoding="utf-8"?>\n')
    TREE.write(OUTPUT_FILE, encoding="utf-8")
    OUTPUT_FILE.flush()
    OUTPUT_FILE.close()
    INPUT_FILE.close()
    exit()
