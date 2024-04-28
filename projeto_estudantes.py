# -*- coding: utf-8 -*-
"""Projeto Estudantes.py

**Sobre o conjunto de dados**
Este conjunto de dados consiste nas notas obtidas pelos alunos em várias disciplinas.

**Introdução**
Vamos tentar entender a influência dos antecedentes dos pais, preparação para testes etc. no desempenho dos alunos.

[Download dos Dados](https://www.kaggle.com/spscientist/students-performance-in-exams)
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# Lendo a Base de Dados
Base_Dados = pd.read_csv('StudentsPerformance (1).csv')

# dimensão
Base_Dados.shape

# Head
Base_Dados.head()

# Campos nulos
Nulos = Base_Dados.isnull()

plt.figure( figsize=(16,5 ) )
plt.title('Analise campos nulos')
sns.heatmap( Nulos, cbar=False );

# Unicos
Base_Dados.nunique()

# Campos duplicados
Base_Dados.duplicated().sum()

# Estatistca
Base_Dados.describe()

# Info
Base_Dados.info()

Base_Dados['gender'].value_counts( normalize=True ) * 100

Base_Dados['race/ethnicity'].value_counts( normalize=True ) * 100

Base_Dados['parental level of education'].value_counts( normalize=True ) * 100

Base_Dados['lunch'].value_counts( normalize=True ) * 100

Base_Dados['test preparation course'].value_counts( normalize=True ) * 100

sns.boxplot( data=Base_Dados, x='math score', y='gender')

sns.boxplot( data=Base_Dados, x='reading score', y='gender')

sns.boxplot( data=Base_Dados, x='writing score', y='gender')

Base_Dados.groupby( by=['gender'] ).describe()['math score'].reset_index()

sns.pairplot( Base_Dados, hue='race/ethnicity' )

sns.boxplot( data=Base_Dados, x='math score', y='race/ethnicity')

sns.boxplot( data=Base_Dados, x='math score', y='parental level of education')

Base_Dados.groupby( by=['parental level of education']).describe()['math score'].reset_index()

sns.boxplot( data=Base_Dados, x='math score', y='test preparation course')

Base_Dados.groupby( by=['test preparation course']).describe()['math score'].reset_index()

sns.scatterplot( data=Base_Dados, x='math score', y='writing score')

