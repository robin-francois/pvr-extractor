#!/usr/bin/env python3
import sys, bitstring
import struct

print("Handline "+sys.argv[1])

infile = open(sys.argv[1],'rb')
data = infile.read()
datad = bitstring.BitArray(data)
slices = datad.split('0x47424958')
i = 0
next(slices)
for slic in slices:
	gbix_header_size=4
	gbix_header_loc=0
	gbix_header = slic[gbix_header_loc*8:(gbix_header_loc+gbix_header_size)*8]
	
	gbix_len_loc = gbix_header_loc + gbix_header_size
	gbix_len_size = 4
	gbix_len = slic[gbix_len_loc*8:(gbix_len_loc+gbix_len_size)*8]
	gbix_len_int = gbix_len.uintle
	
	pvrt_header_loc = gbix_header_loc + gbix_header_size + gbix_len_size + gbix_len_int
	pvrt_header_size = 4
	pvrt_header = slic[(pvrt_header_loc)*8:(pvrt_header_loc+pvrt_header_size)*8]

	pvrt_len_loc = pvrt_header_loc + pvrt_header_size
	pvrt_len_size = 4
	pvrt_len = slic[(pvrt_len_loc)*8:(pvrt_len_loc+pvrt_len_size)*8]
	pvrt_len_int = pvrt_len.uintle

	data = slic[0:(gbix_header_size+gbix_len_size+gbix_len_int +
	pvrt_header_size+pvrt_len_size+pvrt_len_int)*8]
	
	f = open(sys.argv[1]+'_text'+str(i).zfill(7)+'.pvr', 'wb')
	data.tofile(f)
	f.close()
	i += 1
infile.close()
