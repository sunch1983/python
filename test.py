for i in range(1,10):
    for z in range(1,i+1):
        print ('%d*%d=%d' % (z, i, i * z), end='\t')
    print('\n')