def last_in_line(cds,n):
    cds2=cds.split(',')
    cds2[len(cds2):]=cds2[n]
    del cds2[n]
    print cds2