import pandas as pd
import datetime as dt

def getdata(str_date):
    df = pd.DataFrame([['2019-11-22', '네이버', 28, 'kospi'],
                        ['2019-11-22', '다음', 20, 'kodaq'], 
                        ['2019-11-22', '구글', 15, 'kospi'], 
                        ['2019-11-22', '아프리카코끼리', 30, 'kodaq']
                                                ], columns=['date', '종목명', '등락률', '시장']
                                                )

    # df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    # str_date = date.strftime('%Y-%m-%d')
    df_sel = df[df['date'] == str_date]

    return df_sel
