import pandas as pd
from Constants import Constants


def get_data(path=Constants.turkish_news_article_path, encoding=None, header='infer'):
    data = pd.read_csv(path, encoding=encoding, header=header)
    return data 