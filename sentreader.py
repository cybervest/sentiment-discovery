'''
Created on Oct 27, 2017

@author: tester
'''
import os
import time
import pandas as pd
import datetime as datetime
import numpy as np
import argparse
#from html2text import unescape #conda install -c auto html2text 


COLUMNS = ["date","message_id","symbol","sentiment","user","text"]
#LCOLUMNS = ["datetime", "symbol","user","text"]
#SCOLUMNS = ["datetime", "symbol","user","text", "sentiment"]
LCOLUMNS = ["ltext"]
SCOLUMNS = ["symbol", "user", "text", "sentiment"]



def readfile(datafile, concat):
    print('reading: ' + datafile)
    concat.append(pd.read_csv(datafile, header = 0))
    return concat
        
    
#    tw = twits[['symbol','user','text']]
#    if not (outfile is None):
#        if os.path.exists(outfile):
#            outf = open(outfile, "a")
            #twits.to_csv(outf, index=False, columns=LCOLUMNS, header=False, sep = '\t')
#            tw.to_csv(outf, index=False, columns=LCOLUMNS, header=False)
#        else:
#            outf = open(outfile, "a")
#            tw.to_csv(outf, index=False, columns=COLUMNS)
#        outf.close()
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type = str, default = './')
    parser.add_argument('--output', type = str, default = 'output.csv')
    settings = vars(parser.parse_args())
    print(settings)
    
    root = settings['root']
    outfile = settings['output'] 
    concat = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            print(os.path.join(path, name))
            concat.append(pd.read_csv(os.path.join(path, name), header = 0))
    concat = pd.concat(concat)
    concat = concat.sort_values('datetime')
    l = len(concat)
    concat = concat.drop_duplicates()
    print('percent duplicates : %.1f' % (100*(l-len(concat))*1.0/l))
    #re.sub(r'\$\w+', r'$T', s)
    #re.sub(r'http\S+', r'URL', s)
    #concat['text'] = unescape(concat['text'])

#    concat.to_csv('raw.txt')
    concat['text'].replace(to_replace= '&#39;', value = r"'", regex=True, inplace=True)
    concat['text'].replace(to_replace= '&quot;', value = r'"', regex=True, inplace=True)
    concat['text'].replace(to_replace= '&amp;', value = r'&', regex=True, inplace=True)
    concat['text'].replace(to_replace= '&lt;', value = r'<', regex=True, inplace=True)
    concat['text'].replace(to_replace= '&gt;', value = r'>', regex=True, inplace=True)
    
    concat['text'].replace(to_replace= '\$[a-zA-Z]+', value=r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$\w+\.[xX]', value=r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= 'http\S+', value=r'URL', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\@\w+', value = r'@N', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\#[a-zA-Z]+', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T\.[xX]', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= ' [a-zA-Z]+\.[Xx]', value = r' $T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '  ', value = r' ', regex=True, inplace=True)
    concat['text'].replace(to_replace= '  ', value = r' ', regex=True, inplace=True)
    concat['text'].replace(to_replace= '(\b\d{1,2}\D{0,3})?\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\D?(\d{1,2}(st|nd|rd|th)?)?(([,.\-\/])\D?)?((19[7-9]\d|20\d{2})|\d{2})*', value = r'$D', regex=True, inplace=True) 
#    concat['text'].replace(to_replace= '\b\d+(?:\.\d+)?[mMbBkK]?\b', value = r'NN', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\d+\,?\.?\d+[mMkKbB]?', value = r'$N' , regex=True, inplace=True)
    
    concat['text'].replace(to_replace= '\$T, \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T, \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T, \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T, \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T, \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '  ', value = r' ', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '  ', value = r' ', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '\$T \$T', value = r'$T', regex=True, inplace=True)
    concat['text'].replace(to_replace= '  ', value = r' ', regex=True, inplace=True)
    concat["text"] = concat["text"] + "~ " 
#    concat["ltext"] = concat["text"] + concat["sentiment"].map(str)
    concat = concat.drop_duplicates(subset=["text", "sentiment"])
    concat = concat.drop_duplicates(subset=["text"], keep=False) #throw away data with inconsistent labels
    
    outf = open('lang_' + outfile, "w")
    concat.to_csv(outf, index=False)
    outf.close()

    sent = concat[concat['sentiment'] != 0]
    sent['sentiment']= sent['sentiment'].replace(-1,0)
    outf = open('sent_' + outfile, "w")
    sent.to_csv(outf, index=False)
    outf.close()

if __name__ == '__main__':
    main()


