# My study projects 

In this repository you can see my projects.
Each project is aimed at practicing a specific skill:
- EDA. (статистики по датасету, боксплоты, разброс категорий, ...)
- Data Cleaning. (пропуски через fillna, чистка категорий, объединение категорий)
- Data preparation(обработка категорий — label/ohe/frequency, проекция числовых на категории, трансформация числовых, бининг)
- Models

## Telecom project
- [telecom.ipynb](https://github.com/Kargin-Alexey/study_projects/blob/main/telecom.ipynb) 
     
     ___Продажа квартир в Санкт-Петербурге — анализ рынка недвижимости___
     
     Используя данные персональные данные о некоторых клиентах, телекоммуникационная компания хочет научиться предсказывать отток клиентов. В проект входит: обработка и анализ данных, возможный план работ, подбор алгоритма МО для задачи, подбор гиперпараметров. Сформированы выводы. Качество моделей 
     - CatBoostClassifier (ROC-AUC=0.86)
     - LogisticRegressionCV (ROC-AUC=0.85)
     - RandomForestClassifier (ROC-AUC=0.85)
     
     В качестве реализации есть наброски API с использованием FastAPI
     
