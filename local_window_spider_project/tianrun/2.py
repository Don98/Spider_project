import csv

if __name__ == '__main__':
    with open('tianrun.csv','r') as f:
        data = f.readlines()
    L = []
    for i in data:
        if not i in L:
            L.append(i)
    with open('try.csv','w',newline = "") as csvfile:
        a = csv.writer(csvfile,dialect='excel')
        raw = ['title','url','sales']            
        a.writerow(raw)
        for i in L:
            a.writerow(i.split(','))