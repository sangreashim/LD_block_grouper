#!/usr/bin/python

import sys

in_list = open(sys.argv[1],'r').readlines()
file_out = open(sys.argv[2],'w')

group   = []
marker_dict = {}
num     = 0
for i in in_list:
        num     += 1
        cell    = i.strip().split()
        chromosome      = cell[0]
        marker_1        = cell[2]
        marker_2        = cell[5]
        rsquared        = float(cell[6])
        print str(num) +'/'+ str(len(in_list)) +' processed' +'\b'
        if rsquared     >= 0.9:
                if chromosome not in marker_dict.keys():
                        marker_dict[chromosome] = {}
                if marker_1 in marker_dict[chromosome].keys():
                        marker_dict[chromosome][marker_1].append(marker_2)
                else:
                        marker_dict[chromosome][marker_1]   = [marker_2]

#new_dict       = {}
def merging(chromosome_no):
        switch  = [0]*len(marker_dict[chromosome_no].keys())
        num     = 0
        for x in marker_dict[chromosome_no].keys():
                if switch[num] == 0:
                        marker_1        = x
                        marker_2        = marker_dict[chromosome_no][x]
                        markers = marker_2+[marker_1]
                        markers_set     = list(set(markers))
                        switch[num]     = 1
                        s_num   = 0
                        for y in marker_dict[chromosome_no].keys():
                                if switch[s_num] == 0:
                                        MK1     = y
                                        MK2     = marker_dict[chromosome_no][y]
                                        MKS     = MK2+[MK1]
                                        MKS_set = list(set(MKS))
                                        if len(set(MKS).intersection(markers_set)) >= 1:
                                                switch[s_num]   = 1
                                                markers_set     += MKS_set
                                                markers_set     = list(set(markers_set))
                                s_num += 1
                        file_out.write('\t'.join(markers_set)+'\n')
                num += 1

for k in marker_dict.keys():
        print 'chromosome '+k+' is under procedure'
        merging(k)
