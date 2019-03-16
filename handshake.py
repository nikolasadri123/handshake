def main():
    n = input()
    for _ in xrange(n):
        t = input()
        if (t == 1):
            print 0
        else:
            print t*(t-1)/2
            
    
if __name__ == '__main__':
    main()
