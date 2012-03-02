def last_in_line(cds,n):
    cds2=cds.split(',')
    cdsc=len(cds2)
    if n>=cdsc:
        nn=n
        while nn>=cdsc:
            print"Please choose a number that is at least one less than the number of elements in your string:"
            nn=int(raw_input("> "))
        n=nn
    #cds2[len(cds2):]=cds2[n] or
    cds2.append(cds2[n])
    del cds2[n]
    print cds2