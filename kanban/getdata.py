import pandas as pd
import datetime as dt

def getdata(str_date):
    df = pd.DataFrame([['2019-11-22', '네이버', 20, 'kospi', -10.1, 10000],
                        ['2019-11-22', '다음', 10, 'kosdaq', -5.2, 5000], 
                        ['2019-11-22', '구글', 3, 'kospi', 55.3, 8000], 
                        ['2019-11-22', '아프리카코끼리', 30, 'kosdaq', 102.3, 7000]
                                                ], columns=['date', '종목명', '등락률', '시장', '누적수익률', '시가총액']
                                                )

    # df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    # str_date = date.strftime('%Y-%m-%d')
    df_sel = df[df['date'] == str_date]

    return df_sel
