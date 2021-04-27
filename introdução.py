from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns

train_df = pd.read_csv("brazilian_headlines_sentiments.csv")
train_df.columns.values
cols = ['Unnamed: 0', 'headlineEnglish', 'keywords',
       'sentimentScoreEnglish', 'isOnline', 'sentimentScorePortuguese',
       'headlinePortuguese', 'onlineStartDate', 'onlineTotalTimeMS',
       'sentimentMagnitudePortuguese', 'sentimentMagnitudeEnglish',
       'onlineEndDate', 'website']

cols = ['headlinePortuguese', 'website']
train_df = pd.read_csv("brazilian_headlines_sentiments.csv", usecols=cols, encoding='ISO-8859-1')

sns.countplot(y='website', data=train_df, palette='pastel')

labelencoder = LabelEncoder()
websites = labelencoder.fit_transform(train_df['website'])

x_train, x_test, y_train, y_test = train_test_split(train_df['headlinePortuguese'], websites, test_size=0.2,
                                        random_state=5)
redeNeural = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('clf', LinearSVC())
])

pipeline.fit(x_train, y_train)
previsao = pipeline.predict(x_test)
accuracy_score(y_test, previsao)
print(classification_report(y_test, previsao))

text = 'Bolsonario diz que é super atleta'
predicao = pipeline.predict([text])
print(predicao)

labelencoder.inverse_transform(predicao)[0]
