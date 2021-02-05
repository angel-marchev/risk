get_ipython().magic('reset -f')
import pandas as pd
from pathlib import Path
import fuzzynoisymatcher as fm
import sqlite3
from sqlite_fts4 import register_functions
import numpy as np
import pandas_profiling

demogr = pd.read_excel('demogr-filtered.xlsx')

big5 = pd.read_excel('big5_data.xlsx')

left_on = ["sex", "age_sim"]
right_on = ["gender", "age"]

match_table = fm.link_table(demogr, big5, left_on, right_on, left_id_col='ind', right_id_col='id')

matched_results = fm.fuzzy_left_join(demogr, big5, left_on, right_on, left_id_col='ind', right_id_col='id')

del matched_results['best_match_score']
del matched_results['__id_right']
del matched_results['__id_left']
del matched_results['id']
del matched_results['age']
del matched_results['gender']
del matched_results['Unnamed: 0']

zzz=matched_results.sex.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
matched_results['binsex']=zxc
del zzz
del zxc

zzz=matched_results.age_sim.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
matched_results['binage_sim']=zxc
del zzz
del zxc

zzz=matched_results.lv_educ.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
matched_results['binlv_educ']=zxc
del zzz
del zxc

indrisk = pd.read_excel('ind_risk_data.xlsx',dtype={'gender':int,'age':int,'edu_level':int})

zzz=indrisk.gender.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
indrisk['bingender']=zxc
del zzz
del zxc

zzz=indrisk.age.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
indrisk['binage']=zxc
del zzz
del zxc

zzz=indrisk.edu_level.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
indrisk['binedu_level']=zxc
del zzz
del zxc

left_on = ["binsex", "binage_sim", "binlv_educ"]
right_on = ["bingender", "binage", "binedu_level"]

match_table = fm.link_table(matched_results, indrisk, left_on, right_on, left_id_col='ind', right_id_col='ind')

matched_results = fm.fuzzy_left_join(matched_results, indrisk, left_on, right_on, left_id_col='ind', right_id_col='ind')

del matched_results['best_match_score']
del matched_results['__id_right']
del matched_results['__id_left']
del matched_results['binsex']
del matched_results['binage_sim']
del matched_results['binlv_educ']
del matched_results['bingender']
del matched_results['binage']
del matched_results['binedu_level']
del matched_results['Unnamed: 0']

zzz=matched_results.sex.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
matched_results['binsex']=zxc
del zzz
del zxc

zzz=matched_results.age_sim.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
matched_results['binage_sim']=zxc
del zzz
del zxc

zzz=matched_results.lv_educ.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
matched_results['binlv_educ']=zxc
del zzz
del zxc

indrisk = pd.read_excel('invest_pref.xlsx')

zzz=indrisk.gender.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
indrisk['bingender']=zxc
del zzz
del zxc

zzz=indrisk.age.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
indrisk['binage']=zxc
del zzz
del zxc

zzz=indrisk.level_educ.values
zxc=[None]*len(zzz)
for i in range(len(zzz)):
    zxc[i] = '{0:08b}'.format(zzz[i])
indrisk['binedu_level']=zxc
del zzz
del zxc

left_on = ["binsex", "binage_sim", "binlv_educ"]
right_on = ["bingender", "binage", "binedu_level"]

match_table = fm.link_table(matched_results, indrisk, left_on, right_on, left_id_col='ind_left', right_id_col='id')

matched_results = fm.fuzzy_left_join(matched_results, indrisk, left_on, right_on, left_id_col='ind_left', right_id_col='id')

matched_results.drop(['best_match_score','__id_right','__id_left','ind_left','binsex','binage_sim','binlv_educ','bingender', 'binage','nation','edu','temperam','ind_risk_sim','invest_exp_sim','shares_left','corp_oblig','oth','inv_fund','cash_left',  'crypto_left','gov_bond','ind_right','gender_left','age_left','years_edu','edu_level','prof','montly_income','town','position','industry','id','gender_right','age_right','income','houshold_people','level_educ','bk_acc','binedu_level'],axis=1,inplace=True)

matched_results.to_excel("matched_results3.xlsx")
