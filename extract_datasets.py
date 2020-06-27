import re
import lingcorpora
import pandas as pd
from statistics import mean
from functools import partial


YEAR = re.compile(r'[0-9]+')
DF = partial(pd.DataFrame, columns=['text', 'movement', 'style', 'year'])


def get_year(meta):
    return round(mean(int(y) for y in re.findall(YEAR, meta) if len(y) == 4))


if __name__ == '__main__':
    c = lingcorpora.Corpus('rus')

    main_iz = c.search('из Москвы', n_results=250)[0]
    main_s = c.search('с Москвы', n_results=500)[0]
    spoken_iz = c.search('из Москвы', n_results=100, subcorpus='spoken')[0]
    spoken_s = c.search('с Москвы', n_results=200, subcorpus='spoken')[0]

    miz = DF([(r.text, '', '', get_year(r.meta))  for r in main_iz])
    ms = DF([(r.text, '', '', get_year(r.meta))  for r in main_s])
    siz = DF([(r.text, '', '', get_year(r.meta))  for r in spoken_iz])
    ss = DF([(r.text, '', '', get_year(r.meta))  for r in spoken_s])
    
    miz.to_csv('data/main_iz.csv')
    ms.to_csv('data/main_s.csv')
    siz.to_csv('data/spoken_iz.csv')
    ss.to_csv('data/spoken_s.csv')
