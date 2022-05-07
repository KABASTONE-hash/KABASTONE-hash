#Importation des librairies nécessaires pour cla réalisation de ce projet
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
#MISE EN PLACE DU DASHBOARD
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
#Importation de la base de données téléchargée  sur le site de l'offiche des changes du maroc
df=pd.read_csv("ExportData.csv",sep=';', decimal=',')
#affichage des cinq premiers éléments de la base de données
df.head(5)
df.shape
#Nous allons supprimer la dernière colonne de la base de données car elle ne contient que des valeurs manquantes et elle n'est pas utile pour notre projet
data=df.drop("Unnamed: 22",1)
#Affichons maintenant la base de données sur laquelle nous allons travaller
data.head()
#Pour connaître la dimension de notre base de données
data.shape
data.info()
#Détection des valeurs manquantes
print("Le nombre de valeurs manquantes par colonne est :")
data.isnull().sum()
#Affichage des valeurs manquantes de la colonne code du pays
vm=data[data['Code du pays'].isnull()]
vm.head()
#On remplace NaN du code du pays de namibie par NAM
data["Code du pays"].fillna("NMB",inplace=True)
#Affichage des valeurs manquantes de la colonne Continent
vm=data[data['Continent'].isnull()]
vm.head()
#On remplace NaN du continentpar AFRIQUE car NAMIBIE est dans l'AFRIQUE
data["Continent"].fillna("AFRIQUE",inplace=True)
#Affichage des valeurs manquantes de la colonne code du pays
vm=data[data['Libellé du pays'].isnull()]
vm.head()
#On remplace NaN du libellé du pays par namibie car NAM correspond au pays NAMIBIE
data["Libellé du pays"].fillna("NAMIBIE",inplace=True)
#Détection des valeurs manquantes
print("Le nombre de valeurs manquantes par colonne est :")
data.isnull().sum()
#Box plot détection des valeurs abérantes
#Pour le libellé du flux
fig = px.box(data, x="Libellé du flux", y="Valeur DHS 2020",log_y=True,color="Continent",title="Visualisation des valeurs abberantes pour le libellé du flux" )
fig.show()
#Pour le libellé du flux
fig = px.box(data, x="Libellé du groupement d'utilisation", y="Valeur DHS 2020", log_y=True,color="Continent",title="Visualisation des valeurs aberrantes pour le libellé du groupement d'utilisation", notched=True)
fig.show()

#Pour le nouveau produit remarquable
fig = px.box(data, x="Libellé du nouveau produits remarquables", y="Valeur DHS 2020",log_y=True,color="Continent",title="Visualisation des valeurs aberrantes pour le libellé du nouveau produit remarquable", notched=True)
fig.show()
#Exploration des données
data.describe()
#Déduction de la matrice de corrélation entre les variables quantitatives
a=data.drop(["Code du groupement d'utilisation","Code du nouveau produits remarquables"],1)
Corr=a.corr()
sns.heatmap(Corr,annot=True)
#Les différentes compositions des variables catégorielles
fig1 = px.pie(data, values='Valeur DHS 2020', names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },title='Répartition des flux par Valeur DHS 2020')
fig1.show()
#Les différentes compositions des variables catégorielles
fig2 = px.pie(data, values='Poids en KG 2020', names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver' },title='Répartition des flux par Poids en KG 2020')
fig2.show()
fig3=px.pie(data, values='Valeur DHS 2019',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Valeur DHS 2019')
fig4=px.pie(data, values='Poids en KG 2019',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Poids en KG 2019')
fig5=px.pie(data, values='Valeur DHS 2018',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Valeur DHS 2018')
fig6=px.pie(data, values='Poids en KG 2018',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Poids en KG 2018')
fig7=px.pie(data, values='Valeur DHS 2017',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Valeur DHS 2017')
fig8=px.pie(data, values='Poids en KG 2017',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Poids en KG')
fig9=px.pie(data, values='Valeur DHS 2016',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Valeur DHS 2016')
fig10=px.pie(data, values='Poids en KG 2016',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Poids en KG 2016')
fig11=px.pie(data, values='Valeur DHS 2015',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Valeur DHS 2015')
fig12=px.pie(data, values='Poids en KG 2015',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Poids en KG 2015')
fig13=px.pie(data, values='Valeur DHS 2014',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Valeur DHS 2014')
fig14=px.pie(data, values='Poids en KG 2014',
                       names='Libellé du flux', color='Libellé du flux',color_discrete_map={'Importations CAF':'black',
                                 'Exportations CAF':'silver'
                                                                                          },
                       title='Répartition des flux par Poids en KG 2014')
#Les différentes compositions des variables catégorielles
fig15 = px.pie(data, values='Valeur DHS 2020', names='Libellé du nouveau produits remarquables', color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                                                               "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                                                                "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                                                                          },title='Répartition des produits remarquables par Valeur DHS 2020')
fig15.show()
#Les différentes compositions des variables catégorielles
fig16 = px.pie(data, values='Poids en KG 2020', names='Libellé du nouveau produits remarquables', color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                                                               "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                                                                "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                                                                          },title='Répartition des produits remarquables par Poids en KG 2020')
fig16.show()
fig17=px.pie(data, values='Valeur DHS 2019', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Valeur DHS 2019')
fig18= px.pie(data, values='Poids en KG 2019', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Poids en KG 2019')
fig19=px.pie(data, values='Valeur DHS 2018', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Valeur DHS 2018')
fig20=px.pie(data, values='Poids en KG 2018', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Poids en KG 2018')
fig21=px.pie(data, values='Valeur DHS 2017', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Valeur DHS 2017')
fig22=px.pie(data, values='Poids en KG 2017', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Poids en KG 2017')
fig23=px.pie(data, values='Valeur DHS 2016', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Valeur DHS 2016')
fig24= px.pie(data, values='Poids en KG 2016', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Poids en KG 2016')
fig25=px.pie(data, values='Valeur DHS 2015', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Valeur DHS 2015')
fig26=px.pie(data, values='Poids en KG 2015', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Poids en KG 2015')
fig27=px.pie(data, values='Valeur DHS 2014', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Valeur DHS 2014')
fig28=px.pie(data, values='Poids en KG 2014', names='Libellé du nouveau produits remarquables',
                color='Libellé du nouveau produits remarquables',color_discrete_map={'ARGUMES':'lightcyan',
                                 'AMIDON':'cyan',
                                 "BEURRE":'royalblue',
                                 "AMIDONS,GLUTEN DE FROMENT ET DÉRIVÉS":'darkblue',
                                            "BIÈRES; VINS; VERMOUTHS; ET AUTRES BOISSONS SPIRITUEUSES":'green',
                                                        "CACAO ET PREPARATIONS À BASE DE CACAO":'red',
                                        },title='Répartition des produits remarquables par Poids en KG 2014')
fig28.show()
#Les différentes compositions des variables catégorielles
fig29 = px.pie(data, values='Valeur DHS 2020', names="Libellé du groupement d'utilisation", color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par valeur DHS 2020")
fig29.show()
#Les différentes compositions des variables catégorielles
fig30 = px.pie(data, values='Poids en KG 2020', names="Libellé du groupement d'utilisation",
               color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par poids en KG 2020")
fig30.show()
#Les différentes compositions des variables catégorielles
fig31 = px.pie(data, values='Valeur DHS 2019', names="Libellé du groupement d'utilisation",
               color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par Valeur DHS 2019")
fig31.show()
fig32=px.pie(data, values='Poids en KG 2019', names="Libellé du groupement d'utilisation",
               color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par poids en KG 2019")
fig33=px.pie(data, values='Valeur DHS 2018', names="Libellé du groupement d'utilisation", color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par valeur DHS 2018")
fig34=px.pie(data, values='Poids en KG 2018', names="Libellé du groupement d'utilisation",
               color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par poids en KG 2018")
fig35=px.pie(data, values='Valeur DHS 2017', names="Libellé du groupement d'utilisation", color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par valeur DHS 2017")
fig36=px.pie(data, values='Poids en KG 2017', names="Libellé du groupement d'utilisation",
               color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par poids en KG 2017")
fig37=px.pie(data, values='Valeur DHS 2016', names="Libellé du groupement d'utilisation", color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par valeur DHS 2016")
fig38=px.pie(data, values='Poids en KG 2016', names="Libellé du groupement d'utilisation",
               color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par poids en KG 2016")
fig39=px.pie(data, values='Valeur DHS 2015', names="Libellé du groupement d'utilisation", color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par valeur DHS 2015")
fig40=px.pie(data, values='Poids en KG 2015', names="Libellé du groupement d'utilisation",
               color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par poids en KG 2015")
fig41=px.pie(data, values='Valeur DHS 2014', names="Libellé du groupement d'utilisation", color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par valeur DHS 2014")
fig42=px.pie(data, values='Poids en KG 2014', names="Libellé du groupement d'utilisation",
               color="Libellé du groupement d'utilisation",color_discrete_map={
    'PRODUITS FINIS DE CONSOMMATION':'black',
                                 "PRODUITS FINIS D'EQUIPEMENT INSDUSTRIEL":'silver',
           'DEMI PRODUITS':"beige"},title="Répartition de groupement d'utilisation par poids en KG 2014")
fig42.show()
#Distribution entre l'importation et l'exportation par continent
fig43=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Valeur DHS 2020",
             title="Distribution entre l'importation et l'exportation par continent pour Valeur DHS 2020")
fig43.show()
fig44=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Poids en KG 2020",
             title="Distribution entre l'importation et l'exportation par continent pour Poids en KG 2020")
fig44.show()
fig45=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Valeur DHS 2019",
             title="Distribution entre l'importation et l'exportation par continent pour Valeur DHS 2019")
fig46=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Poids en KG 2019",
             title="Distribution entre l'importation et l'exportation par continent pour Poids en KG 2019")
fig47=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Valeur DHS 2018",
             title="Distribution entre l'importation et l'exportation par continent pour Valeur DHS 2018")
fig48=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Poids en KG 2018",
             title="Distribution entre l'importation et l'exportation par continent pour Poids en KG 2018")
fig49=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Valeur DHS 2017",
             title="Distribution entre l'importation et l'exportation par continent pour Valeur DHS 2017")
fig50=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Poids en KG 2017",
             title="Distribution entre l'importation et l'exportation par continent pour Poids en KG 2017")
fig51=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Valeur DHS 2016",
             title="Distribution entre l'importation et l'exportation par continent pour Valeur DHS 2016")
fig52=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Poids en KG 2016",
             title="Distribution entre l'importation et l'exportation par continent pour Poids en KG 2016")
fig53=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Valeur DHS 2015",
             title="Distribution entre l'importation et l'exportation par continent pour Valeur DHS 2015")
fig54=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Poids en KG 2015",
             title="Distribution entre l'importation et l'exportation par continent pour Poids en KG 2015")
fig55=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Valeur DHS 2014",
             title="Distribution entre l'importation et l'exportation par continent pour Valeur DHS 2014")
fig56=px.histogram(data,x="Continent",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},hover_name="Libellé du pays",
             hover_data=data.columns,barmode="group",y="Poids en KG 2014",
             title="Distribution entre l'importation et l'exportation par continent pour Poids en KG 2014")
fig56.show()
#Distribution entre l'importation et l'exportation par pays
fig57=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2020",
                   title="Distribution entre l'importation et l'exportation par pays pour Valeur DHS 2020")
fig57.show()
fig58=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2020",
                   title="Distribution entre l'importation et l'exportation par pays pour Poids en KG 2020")
fig58.show()
fig59=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2019",
                   title="Distribution entre l'importation et l'exportation par pays pour Valeur DHS 2019")
fig60=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2019",
                   title="Distribution entre l'importation et l'exportation par pays pour Poids en KG 2019")
fig61=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2018",
                   title="Distribution entre l'importation et l'exportation par pays pour Valeur DHS 2018")
fig62=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2018",
                   title="Distribution entre l'importation et l'exportation par pays pour Poids en KG 2018")
fig63=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2017",
                   title="Distribution entre l'importation et l'exportation par pays pour Valeur DHS 2017")
fig64=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2017",
                   title="Distribution entre l'importation et l'exportation par pays pour Poids en KG 2017")
fig65=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2016",
                   title="Distribution entre l'importation et l'exportation par pays pour Valeur DHS 2016")
fig66=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2016",
                   title="Distribution entre l'importation et l'exportation par pays pour Poids en KG 2016")
fig67=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2015",
                   title="Distribution entre l'importation et l'exportation par pays pour Valeur DHS 2015")
fig68=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2015",
                   title="Distribution entre l'importation et l'exportation par pays pour Poids en KG 2015")
fig69=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2014",
                   title="Distribution entre l'importation et l'exportation par pays pour Valeur DHS 2014")
fig70=px.histogram(data,x="Libellé du pays",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2014",
                   title="Distribution entre l'importation et l'exportation par pays pour Poids en KG 2014")
fig70.show()
dg=data.groupby(["Libellé du groupement d'utilisation","Libellé du flux"],as_index=False).sum()
#Distribution entre l'importation et l'exportation par groupement d'utilisation en utilisant les valeurs
fig71=px.histogram(data,x="Libellé du groupement d'utilisation",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2020",
                   title="Distribution entre l'importation et l'exportation par groupement d'utilisation pour Valeur DHS 2020")
fig71.show()
#Distribution entre l'importation et l'exportation par groupement d'utilisation en utilisant les poids
#graphiques en entonnoir utilisés pour représenter des données du poids rélatif au groupement d'utilisation à différentes étapes.
#C'est un mécanisme important de la Business Intelligence pour identifier les problèmes potentiels d'un processus.
#il est utilisé ici pour observer le poids importé et exporté pour chaque
#type de groupement d'utilisation et affiche des valeurs.
fig72= px.funnel(dg, x="Poids en KG 2020", y="Libellé du groupement d'utilisation",
                 color="Libellé du flux",color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'})
fig72.show()
#Distribution entre l'importation et l'exportation par groupement d'utilisation en utilisant les valeurs
px.histogram(data,x="Libellé du groupement d'utilisation",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2020",
                   title="Distribution entre l'importation et l'exportation par groupement d'utilisation pour Poids en KG 2020")
fig73=px.histogram(data,x="Libellé du groupement d'utilisation",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2019",
                   title="Distribution entre l'importation et l'exportation par groupement d'utilisation pour valeur DHS 2019")
fig74=px.funnel(dg, x="Poids en KG 2019", y="Libellé du groupement d'utilisation",
                 color="Libellé du flux",color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'})
fig75=px.histogram(data,x="Libellé du groupement d'utilisation",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2018",
                   title="Distribution entre l'importation et l'exportation par groupement d'utilisation pour valeur DHS 2018")
fig76=px.funnel(dg, x="Poids en KG 2018", y="Libellé du groupement d'utilisation",
                 color="Libellé du flux",color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'})
fig77=px.histogram(data,x="Libellé du groupement d'utilisation",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2017",
                   title="Distribution entre l'importation et l'exportation par groupement d'utilisation pour valeur DHS 2017")
fig78=px.funnel(dg, x="Poids en KG 2017", y="Libellé du groupement d'utilisation",
                 color="Libellé du flux",color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'})
fig79=px.histogram(data,x="Libellé du groupement d'utilisation",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2016",
                   title="Distribution entre l'importation et l'exportation par groupement d'utilisation pour valeur DHS 2016")
fig80=px.funnel(dg, x="Poids en KG 2016", y="Libellé du groupement d'utilisation",
                 color="Libellé du flux",color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'})
fig81=px.histogram(data,x="Libellé du groupement d'utilisation",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2015",
                   title="Distribution entre l'importation et l'exportation par groupement d'utilisation pour valeur DHS 2015")
fig82=px.funnel(dg, x="Poids en KG 2015", y="Libellé du groupement d'utilisation",
                 color="Libellé du flux",color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'})


fig83=px.histogram(data,x="Libellé du groupement d'utilisation",color="Libellé du flux",
                   color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
                   hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2014",
                   title="Distribution entre l'importation et l'exportation par groupement d'utilisation pour valeur DHS 2014")
fig84=px.funnel(dg, x="Poids en KG 2014", y="Libellé du groupement d'utilisation",
                 color="Libellé du flux",color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'})
fig84.show()
#Distribution entre l'importation et l'exportation par produits remarquables
fig85=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2020",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Valeur DHS 2020")
fig85.show()
#Distribution entre l'importation et l'exportation par produits remarquables
fig86=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2020",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Pois en KG 2020")
fig86.show()
fig87=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2019",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Valeur DHS 2019")
fig88=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2019",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Pois en KG 2019")
fig89=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2018",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Valeur DHS 2018")
fig90=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2018",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Pois en KG 2018")
fig91=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2017",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Valeur DHS 2017")
fig92=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2017",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Pois en KG 2017")
fig93=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2016",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Valeur DHS 2016")
fig94=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2016",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Pois en KG 2016")
fig95=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2015",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Valeur DHS 2015")
fig96=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2015",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Pois en KG 2015")
fig97=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Valeur DHS 2014",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Valeur DHS 2014")
fig98=px.histogram(data,x="Libellé du nouveau produits remarquables",color="Libellé du flux",
             color_discrete_map={"Importations CAF":"black", "Exportations FAB":'purple'},
             hover_name="Libellé du pays",hover_data=data.columns,barmode="group",y="Poids en KG 2014",
             title="Distribution entre l'importation et l'exportation par produits remarquables pour Pois en KG 2014")
fig98.show()
#Extraction de la data pour uniquement les importationns
dataimp=data[data['Libellé du flux']=="Importations CAF"]
dataimp.head()
#Extraction de la data pour uniquement les exportations
dataexp=data[data['Libellé du flux']=="Exportations FAB"]
dataexp.head()
#Nous voulons tracer l'évolution des importations et exportations aucours de ces 7 années pour les valeurs en DHS
table1 = pd.pivot_table(data, index= data['Libellé du flux'],values=["Valeur DHS 2014","Valeur DHS 2015","Valeur DHS 2016","Valeur DHS 2017","Valeur DHS 2018","Valeur DHS 2019","Valeur DHS 2020"],aggfunc=sum)
table1.head()
#La table v va contenir la transposée de la table1
v=table1.transpose()
v.head()
#On crée une colonne date que nous aloons l'ajouter à la data v
date=[2014,2015,2016,2017,2018,2019,2020]
#Ajout de la colonne Date
v["Date"]=date
#Affichage de la data v
v.head()
#Evolution des Exportations FAB aucours de ces 7 années
fig141=px.bar(v,x="Date",y="Exportations FAB",color="Date",
              color_discrete_map={2014:"aliceblue",2015:"antiquewhite",2017:"bisque",2018:"blue",2019:'brown',2020:'black'},
              title="Evolution en Valeur DHS des exportations 2014-2020")
fig141.show()
#Evolution des importations aucours de ces 7 années
couleur={2014:"aliceblue",2015:"antiquewhite",2017:"bisque",2018:"blue",2019:'brown',2020:'black'}
fig142=px.bar(v,x="Date",y="Importations CAF",color="Date",
              color_discrete_map={2014:"aliceblue",2015:"antiquewhite",2017:"bisque",2018:"blue",2019:'brown',2020:'black'},
              title="Evolution en Valeur DHS des importations 2014-2020")
fig142.show()
#Nuage des points des exportations en fonction des importations separé par date pour comparer les importations et les exportations de chaque année
fig147=px.scatter(v,x="Importations CAF",y="Exportations FAB",facet_col="Date",
                  color="Date",size="Exportations FAB",
                  title="Evolution des exportations en fonction des importations par année")
fig147.show()
#Nuage des points des exportations en fonction des importations pour comparer les importations et les exportations de chaque année
fig145=px.scatter(v,x="Importations CAF",y="Exportations FAB",color="Date",
           color_discrete_map={2014:"aliceblue",2015:"antiquewhite",2017:"bisque",2018:"blue",2019:'brown',2020:'black'},
           size="Exportations FAB",title="Evolution des exportations en fonction des importations de 2014 à 2020")
fig145.show()
#Nous voulons tracer l'évolution des importations et exportations aucours de ces 7 années pour les poids en KG
table2 = pd.pivot_table(data, index= data['Libellé du flux'], values=["Poids en KG 2014","Poids en KG 2015","Poids en KG 2016","Poids en KG 2017","Poids en KG 2018","Poids en KG 2019","Poids en KG 2020"],aggfunc=sum)
table2.head()
#La table w va contenir la transposée de la table2
w=table2.transpose()
#On crée une colonne Date dans la data w
w["Date"]=date
#Evolution des exportations aucours de ces 7 années
fig143=px.bar(w,x="Date",y="Exportations FAB",color="Date",color_discrete_map=couleur,
              title="Evolution en Poids KG des exportations 2014-2020")
fig143.show()
#Evolution des importations aucours de ces 7 années
fig144=px.bar(w,x="Date",y="Importations CAF",color="Date", color_discrete_map=couleur,
       title="Evolution en Poids KG des importations 2014-2020")
fig144.show()
#Nuage des points des exportations en fonction des importations pour comparer les importations et les exportations de chaque année
fig146=px.scatter(w,x="Importations CAF",y="Exportations FAB",color="Date",
           color_discrete_map={2014:"aliceblue",2015:"antiquewhite",2016:"black",2017:"bisque",2018:"blue",2019:'brown',2020:'burlywood'},
                               size="Exportations FAB",title="Evolution des exportations en fonction des importations de 2014 à 2020")
#Nous voulons tracer l'Evolution des exportations faites par le Maroc pour chaque continent
table4 = pd.pivot_table(dataexp, index= data['Continent'], values=["Valeur DHS 2014","Valeur DHS 2015","Valeur DHS 2016","Valeur DHS 2017","Valeur DHS 2018","Valeur DHS 2019","Valeur DHS 2020"],aggfunc=sum)
table4.head()
fig146.show()
#Nuage des points des exportations en fonction des importations separé par date pour comparer les importations et les exportations de chaque année
fig148=px.scatter(w,x="Importations CAF",y="Exportations FAB",facet_col="Date",
           color="Date",size="Exportations FAB",title="Evolution des exportations en fonction des importations par année")
fig148.show()
#Evolution par continent
for i in data["Continent"].unique():
    datacontinent = data[data["Continent"] == i]
    #Nous voulons tracer l'évolution des importations et exportations aucours de ces 7 années pour les poids en KG
    table = pd.pivot_table(datacontinent, index= data['Libellé du flux'], values=["Valeur DHS 2014","Valeur DHS 2015","Valeur DHS 2016","Valeur DHS 2017","Valeur DHS 2018","Valeur DHS 2019","Valeur DHS 2020"],aggfunc=sum)
    #La table w va contenir la transposée de la table2
    w=table.transpose()
    #On crée une colonne Date dans la data w
    w["Date"]=date
    px.bar(w,x="Date",y="Exportations FAB",color="Date",color_discrete_map=couleur,
              title="Evolution des exportations par valeur 2014-2020")
    px.bar(w,x="Date",y="Importations CAF",color="Date",color_discrete_map=couleur,
              title="Evolution des exportations 2014-2020")
# Nous voulons tracer l'Evolution des importations faites par le Maroc pour chaque continent

table3 = pd.pivot_table(dataimp, index=data['Continent'],
            values=["Valeur DHS 2014", "Valeur DHS 2015", "Valeur DHS 2016", "Valeur DHS 2017",
                            "Valeur DHS 2018", "Valeur DHS 2019", "Valeur DHS 2020"], aggfunc=sum)
table3.head()
# La table t contient la transposée de la table3
t = table3.transpose()
# On ajoute la colonne Date à la table t
t["Date"] = date
t

fig149 = px.line(t, x="Date", y=["AFRIQUE", "AMERIQUE", "ASIE", "AUSTRALIE", "AUTRE", "EUROPE"],
                     color_discrete_map={'EUROPE': "blue", "ASIE": "darkblue", "AMERIQUE": 'green', 'AFRIQUE': 'black'},
                     title="Evolution des importations en Valeur DHS par continent")
fig149.show()
# Nous voulons tracer l'Evolution des exportations faites par le Maroc pour chaque continent
table4 = pd.pivot_table(dataexp, index=data['Continent'],
                            values=["Valeur DHS 2014", "Valeur DHS 2015", "Valeur DHS 2016", "Valeur DHS 2017",
                                    "Valeur DHS 2018", "Valeur DHS 2019", "Valeur DHS 2020"], aggfunc=sum)
table4.head()
# d2 contient la transposée de la table4
d2 = table4.transpose()
# On ajoute la colonne date à la data d2
d2["Date"] = date
d2.head()
fig150 = px.line(d2, x="Date", y=["AFRIQUE", "AMERIQUE", "ASIE", "AUSTRALIE", "AUTRE", "EUROPE"],
                     color_discrete_map={'EUROPE': "blue", "ASIE": "darkblue", "AMERIQUE": 'green', 'AFRIQUE': 'black'},
                     title="Evolution des exportations en Valeur DHS par continent")
fig150.show()
#Nous voulons tracer l'Evolution des importations faites par le Maroc pour chaque pays
table5 = pd.pivot_table(dataimp, index=data['Libellé du pays'],
                            values=["Valeur DHS 2014", "Valeur DHS 2015", "Valeur DHS 2016", "Valeur DHS 2017",
                                    "Valeur DHS 2018", "Valeur DHS 2019", "Valeur DHS 2020"], aggfunc=sum)
table5.head()
# d3 contient la transposée de la table5
d3 = table5.transpose()
d3.head()
# On ajoute l colonne Date à la data D3
d3["Date"] = date
d3.head()
fig151 = px.line(d3, x="Date", y=[y for y in d3.columns],
                     color_discrete_map={'ETATS-UNIS': "blue", "CHINE": "darkblue", "FRANCE": 'green',
                                         'ESPAGNE': 'black'},
                     title="Evolution des importations en Valeur DHS par pays")
fig151.show()
#Nous voulons tracer l'Evolution des exportations faites par le Maroc pour chaque pays
table6 = pd.pivot_table(dataexp, index=data['Libellé du pays'],
                            values=["Valeur DHS 2014", "Valeur DHS 2015", "Valeur DHS 2016", "Valeur DHS 2017",
                                    "Valeur DHS 2018", "Valeur DHS 2019", "Valeur DHS 2020"], aggfunc=sum)
table6.head()
# d4 contient la transposée de la table6
d4 = table6.transpose()
d4.head()
# On ajoute l colonne Date à la data D4
d4["Date"] = date
d4.head()
fig152=px.line(d4,x="Date",y=[y for y in d4.columns],
               color_discrete_map={'ETATS-UNIS': "blue", "CHINE":"darkblue","FRANCE":'green', 'ESPAGNE':'black'},
               title="Evolution des exportations en Valeur DHS par pays")
fig152.show()
#Carte à case
fig99= px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Valeur DHS 2020',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig99.show()
fig100=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Poids en KG 2020',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig100.show()
fig101=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Valeur DHS 2019',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig102=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Poids en KG 2019',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig103=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Valeur DHS 2018',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig104=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Poids en KG 2018',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig105=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Valeur DHS 2017',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig106=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Poids en KG 2017',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig107=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Valeur DHS 2016',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig108=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Poids en KG 2016',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig109=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Valeur DHS 2015',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig110=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Poids en KG 2015',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig111=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Valeur DHS 2014',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
fig111.show()
fig112=px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays','Libellé du flux'],
                  values='Poids en KG 2014',
                  color='Continent',
                  color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                  hover_data=['Code du pays'])
#Diagramme en rayon solaire
fig113= px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Valeur DHS 2020',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig113.show()
#Diagramme en rayon solaire
fig114= px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Poids en KG 2020',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2020",hover_data=['Code du pays'])
fig114.show()
fig115=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Valeur DHS 2019',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig116=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Poids en KG 2019',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2019",hover_data=['Code du pays'])
fig117=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Valeur DHS 2018',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig118=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Poids en KG 2018',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2018",hover_data=['Code du pays'])
fig119=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Valeur DHS 2017',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig120=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Poids en KG 2017',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2017",hover_data=['Code du pays'])
fig121=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Valeur DHS 2016',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig122=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Poids en KG 2016',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2016",hover_data=['Code du pays'])
fig123=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Valeur DHS 2015',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig124=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Poids en KG 2015',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2015",hover_data=['Code du pays'])
fig125=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Valeur DHS 2014',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig126=px.sunburst(data, path=['Continent', 'Libellé du pays','Libellé du flux'], values='Poids en KG 2014',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2014",hover_data=['Code du pays'])
#Diagramme en rayon solaire
fig127= px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'],
                    values='Valeur DHS 2020',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig127.show()
#Diagramme en rayon solaire
fig128= px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'], values='Poids en KG 2020',
                  color='Continent', color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2020",hover_data=['Code du pays'])
fig128.show()
fig129=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'],
                    values='Valeur DHS 2019',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig130=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'], values='Poids en KG 2019',
                  color='Continent', color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2019",hover_data=['Code du pays'])
fig131=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'],
                    values='Valeur DHS 2018',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig132=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'], values='Poids en KG 2018',
                  color='Continent', color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2018",hover_data=['Code du pays'])
fig133=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'],
                    values='Valeur DHS 2017',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig134=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'], values='Poids en KG 2017',
                  color='Continent', color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2017",hover_data=['Code du pays'])
fig135=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'],
                    values='Valeur DHS 2016',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig136=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'], values='Poids en KG 2016',
                  color='Continent', color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2016",hover_data=['Code du pays'])
fig137=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'],
                    values='Valeur DHS 2015',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig138=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'], values='Poids en KG 2015',
                  color='Continent', color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2015",hover_data=['Code du pays'])
fig139=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'],
                    values='Valeur DHS 2014',
                  color='Continent',
                    color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_data=['Code du pays'])
fig140=px.sunburst(data, path=['Continent', 'Libellé du nouveau produits remarquables','Libellé du flux'], values='Poids en KG 2014',
                  color='Continent', color_discrete_map={'EUROPE': "blue", "ASIE":"darkblue","AMERIQUE":'green', 'AFRIQUE':'red'},
                    hover_name="Valeur DHS 2014",hover_data=['Code du pays'])
#Répresentation des données géographiques sur une carte,
#mais plotly express n'arrive pas à reconnaître le code du pays dans la base de données
figgeo=px.line_geo(data,locations="Code du pays",color="Continent",projection="orthographic")
figgeo.show()
# Le choroplèthe qui est une carte utilise des différences de couleur dans des zones définies
#autour d'une propriété commune afin de visualiser les données sous forme de résumé agrégé de chaque pays.
#Mais plotly express n'arrive pas à reconnaître le code du pays dans la base de données.
figc1=px.choropleth(data,locations="Code du pays",color="Valeur DHS 2020",
              hover_name="Libellé du pays",color_continuous_scale=px.colors.sequential.Plasma,
             projection="natural earth")
figc1.show()
figc2=px.choropleth(data,locations="Code du pays",color="Poids en KG 2020",
              hover_name="Libellé du pays",color_continuous_scale=px.colors.sequential.Plasma,
             projection="natural earth")

#MATRICE DE NUAGE DES POINTS
figm= px.scatter_matrix(data, dimensions=["Valeur DHS 2014","Valeur DHS 2015","Valeur DHS 2016","Valeur DHS 2017","Valeur DHS 2018","Valeur DHS 2019","Valeur DHS 2020"], color="Libellé du flux")
figm.show()


figmp = px.scatter_matrix(data, dimensions=["Poids en KG 2014","Poids en KG 2015","Poids en KG 2016","Poids en KG 2017","Poids en KG 2018","Poids en KG 2019","Poids en KG 2020"], color="Libellé du flux")
figmp.show()
#MISE EN PLACE D'UN MODELE POUR EXPLIQUER LA VALEUR DHS EN FONCTION DU POIDS EN KG
X1=data["Valeur DHS 2014"].sum()
X2=data["Valeur DHS 2015"].sum()
X3=data["Valeur DHS 2016"].sum()
X4=data["Valeur DHS 2017"].sum()
X5=data["Valeur DHS 2018"].sum()
X6=data["Valeur DHS 2019"].sum()
X7=data["Valeur DHS 2020"].sum()
X=[X1,X2,X3,X4,X5,X6,X7]
Y1=data["Poids en KG 2014"].sum()
Y2=data["Poids en KG 2015"].sum()
Y3=data["Poids en KG 2016"].sum()
Y4=data["Poids en KG 2017"].sum()
Y5=data["Poids en KG 2018"].sum()
Y6=data["Poids en KG 2019"].sum()
Y7=data["Poids en KG 2020"].sum()
Y=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]

DE= pd.DataFrame(list(zip(Y,X)), columns = ['Poids en KG','VALEUR DHS'])
DE
px.scatter(DE,"Poids en KG","VALEUR DHS",trendline="ols")
y=DE.iloc[:,-1]
y
x=DE.iloc[:,:-1]
x
Reg=LinearRegression()
Reg.fit(x,y)
y_pred=Reg.predict(x)
y_pred
#MISE EN PLACE DU DASHBOARD

#Calcul du R2
Reg.score(x,y)
#Calcul des coefficients
print(Reg.intercept_)
print(Reg.coef_)
#En supprimant le point abberant de l'année 2017 on aura
X=[X1,X2,X3,X4,X5,X6]
Y=[Y1,Y2,Y3,Y4,Y5,Y6]

DE= pd.DataFrame(list(zip(Y,X)), columns = ['Poids en KG','VALEUR DHS'])
DE
px.scatter(DE,"Poids en KG","VALEUR DHS",trendline="ols")
y=DE.iloc[:,-1]
y
x=DE.iloc[:,:-1]
x
Reg=LinearRegression()
Reg.fit(x,y)

col_option1=[dict(label=x,value=x) for x in ["Valeur DHS 2014",
                                             "Poids en KG 2014","Valeur DHS 2015",
                                             "Poids en KG 2015","Valeur DHS 2016",
                                             "Poids en KG 2016","Valeur DHS 2017",
                                             "Poids en KG 2017","Valeur DHS 2018",
                                             "Poids en KG 2018","Valeur DHS 2019","Poids en KG 2019",
                                             "Valeur DHS 2020","Poids en KG 2020"]]
col_option2=[dict(label=x,value=x) for x in data["Libellé du flux"].unique()]
col_option3=[dict(label=x,value=x) for x in ["Selon poids","Selon Valeur"]]
col_option4=[dict(label=x,value=x) for x in data["Continent"].unique()]
col_option5=[dict(label=x,value=x) for x in data["Libellé du pays"].unique()]
col_option6=[dict(label=x,value=x) for x in ["Valeur DHS 2020","Poids en KG 2020"]]
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1("PROJET DE DATA VIZ FAIT PAR KABA SEKOU"),
    html.H1("COMMERCE EXTERIEUR DU MAROC"),
    html.H3("EVOLUTION DES IMPORTATIONS ET EXPORTATIONS AUCOURS DES SEPT ANNEES"),
    html.P("Selectionnez le sens du flux "),
    dcc.Dropdown(id="Libellé_du_flux",value="Importations CAF",options=col_option2),
    dcc.Graph(id="graph11",figure={}),
    dcc.Graph(id="graph12",figure={}),
    html.P("EVOLUTION DU FLUX PAR CONTINENT "),
    dcc.Graph(id="graph15",figure={}),
    html.P("EVOLUTION DU FLUX PAR PAYS "),
    dcc.Graph(id="graph16",figure={}),
    html.P("EVOLUTION DU FLUX POUR CHAQUE CONTINENT"),
    html.P("Selectionnez votre continent"),
    dcc.Dropdown(id="Continent",value="EUROPE",options=col_option4),
    dcc.Graph(id="graph17",figure={}),
    dcc.Graph(id="graph18",figure={}),
    html.P("EVOLUTION DU FLUX POUR CHAQUE PAYS"),
    html.P("Selectionnez votre pays"),
    dcc.Dropdown(id="Pays",value="ESPAGNE",options=col_option5),
    dcc.Graph(id="graph19",figure={}),
    dcc.Graph(id="graph20",figure={}),
    html.P("Nuage des points des exportations en fonction des importations"),
    html.P(" pour comparer les importations et les exportations de chaque année selon le poids en KG ou la valeur DHS"),
    html.P("Selectionner votre préference"),
    dcc.Dropdown(id="Nuage",value="Selon Valeur",options=col_option3),
    dcc.Graph(id="graph13",figure={}),
    dcc.Graph(id="graph14",figure={}),
    html.P("Selectionnez le poids en KG ou la valeur en DHS d'une année pour voir"),
    html.P(" les répartitions des flux, des produits remarquables,du groupement d'utilisation"),
    html.P(", pour voir les distributions entre l'importation et l'exportation par continent,"),
    html.P(" par pays, par groupement d'utilisation,par produits remarquables et pour "),
    html.P("visualiser les données hiérarchisées en arborescence comme un diagramme en arbre"),
    html.P(" sur une carte à case et sur un diagramme solaire"),
    dcc.Dropdown(id="Repartition", value="Valeur DHS 2020", options=col_option1),
    dcc.Graph(id="graph1", figure={}),
    dcc.Graph(id="graph2", figure={}),
    dcc.Graph(id="graph3", figure={}),
    dcc.Graph(id="graph4", figure={}),
    dcc.Graph(id="graph5", figure={}),
    dcc.Graph(id="graph6", figure={}),
    dcc.Graph(id="graph7", figure={}),
    html.H4("Visualisation des données hiérarchisées en arborescence comme un diagramme en arbre sur une carte à case"),
    dcc.Graph(id="graph8", figure={}),
    html.H4("Visualisation des données hiérarchisées en arborescence comme un diagramme en arbre"),
    html.H4("sur un diagramme solaire avec sous branches comme pays"),
    dcc.Graph(id="graph9", figure={}),
    html.H4("Visualisation des données hiérarchisées en arborescence comme un diagramme en arbre"),
    html.H4("sur un diagramme solaire avec sous branches comme produits remarquables"),
    dcc.Graph(id="graph10", figure={}),
    html.P("Le choroplèthe qui est une carte qui utilise des différences de couleur dans des zones définies "),
    html.P("autour d'une propriété commune afin de visualiser les données sous forme de résumé agrégé de chaque pays."),
    html.P("Mais plotly express n'arrive pas à reconnaître le code du pays dans la base de données."),
    dcc.Dropdown(id="Cartegeo", value="Valeur DHS 2020", options=col_option6),
    dcc.Graph(id="graph21", figure={})
])
@app.callback(
    Output('graph11', 'figure'),
    [Input('Libellé_du_flux', 'value')]
)
def cb11(Libellé_du_flux):
    Libellé_du_flux=Libellé_du_flux if Libellé_du_flux else "Importations CAF"
    if Libellé_du_flux=="Exportations FAB":
        return  fig141
    else:
        return fig142
@app.callback(
    Output('graph12', 'figure'),
    [Input('Libellé_du_flux', 'value')]
)
def cb12(Libellé_du_flux):
    Libellé_du_flux=Libellé_du_flux if Libellé_du_flux else "Importations CAF"
    if Libellé_du_flux=="Exportations FAB":
        return  fig143
    else:
        return fig144
@app.callback(
    Output('graph15', 'figure'),
    [Input('Libellé_du_flux', 'value')]
)
def cb15(Libellé_du_flux):
    Libellé_du_flux=Libellé_du_flux if Libellé_du_flux else "Importations CAF"
    if Libellé_du_flux=="Exportations FAB":
        return  fig150
    else:
        return fig149
@app.callback(
    Output('graph16', 'figure'),
    [Input('Libellé_du_flux', 'value')]
)
def cb16(Libellé_du_flux):
    Libellé_du_flux=Libellé_du_flux if Libellé_du_flux else "Importations CAF"
    if Libellé_du_flux=="Exportations FAB":
        return  fig152
    else:
        return fig151
@app.callback(
    Output('graph17', 'figure'),
    [Input('Continent', 'value')]
)
def cb17(Continent):
    Continent=Continent if Continent else "EUROPE"
    # Faisons maintenant une étude particulière de la rélation qui existe entre le maroc et l'espagne
    datacontinent = data[data["Continent"] == Continent]
    tablecon = pd.pivot_table(datacontinent, index=data['Libellé du flux'],
                           values=["Valeur DHS 2014", "Valeur DHS 2015", "Valeur DHS 2016", "Valeur DHS 2017",
                                   "Valeur DHS 2018", "Valeur DHS 2019", "Valeur DHS 2020"], aggfunc=sum)
    # La table w va contenir la transposée de la table2
    TC= tablecon.transpose()
    # On crée une colonne Date dans la data w
    TC["Date"] = date
    return px.bar(TC,x="Date",y="Exportations FAB",color="Date",color_discrete_map=couleur,
              title="Evolution des exportations par valeur 2014-2020")
@app.callback(
    Output('graph18', 'figure'),
    [Input('Continent', 'value')]
)
def cb18(Continent):
    Continent=Continent if Continent else "EUROPE"
    # Faisons maintenant une étude particulière de la rélation qui existe entre le maroc et l'espagne
    datacontinent = data[data["Continent"] == Continent]
    tablecon = pd.pivot_table(datacontinent, index=data['Libellé du flux'],
                           values=["Valeur DHS 2014", "Valeur DHS 2015", "Valeur DHS 2016", "Valeur DHS 2017",
                                   "Valeur DHS 2018", "Valeur DHS 2019", "Valeur DHS 2020"], aggfunc=sum)
    # La table w va contenir la transposée de la table2
    TC= tablecon.transpose()
    # On crée une colonne Date dans la data w
    TC["Date"] = date
    return px.bar(TC,x="Date",y="Importations CAF",color="Date",color_discrete_map=couleur,
              title="Evolution des importations par valeur 2014-2020")
@app.callback(
    Output('graph19', 'figure'),
    [Input('Pays', 'value')]
)
def cb19(Pays):
    Pays=Pays if Pays else "ESPAGNE"
    datapays = data[data["Libellé du pays"] == Pays]
    tablepays = pd.pivot_table(datapays, index=data['Libellé du flux'],
                           values=["Valeur DHS 2014", "Valeur DHS 2015", "Valeur DHS 2016", "Valeur DHS 2017",
                                   "Valeur DHS 2018", "Valeur DHS 2019", "Valeur DHS 2020"], aggfunc=sum)
    # La table w va contenir la transposée de la table2
    TP= tablepays.transpose()
    # On crée une colonne Date dans la data w
    TP["Date"] = date
    return px.bar(TP,x="Date",y="Exportations FAB",color="Date",color_discrete_map=couleur,
              title="Evolution des exportations par valeur 2014-2020")
@app.callback(
    Output('graph20', 'figure'),
    [Input('Pays', 'value')]
)
def cb20(Pays):
    Pays=Pays if Pays else "ESPAGNE"
    datapays = data[data["Libellé du pays"] == Pays]
    tablepays = pd.pivot_table(datapays, index=data['Libellé du flux'],
                           values=["Valeur DHS 2014", "Valeur DHS 2015", "Valeur DHS 2016", "Valeur DHS 2017",
                                   "Valeur DHS 2018", "Valeur DHS 2019", "Valeur DHS 2020"], aggfunc=sum)
    # La table w va contenir la transposée de la table2
    TP= tablepays.transpose()
    # On crée une colonne Date dans la data w
    TP["Date"] = date
    return px.bar(TP,x="Date",y="Importations CAF",color="Date",color_discrete_map=couleur,
              title="Evolution des importations par valeur 2014-2020")
@app.callback(
    Output('graph13', 'figure'),
    [Input('Nuage', 'value')]
)
def cb13(Nuage):
    Nuage=Nuage if Nuage else "Selon Valeur"
    if Nuage=="Selon Valeur":
        return  fig145
    else:
        return fig146
@app.callback(
    Output('graph14', 'figure'),
    [Input('Nuage', 'value')]
)
def cb14(Nuage):
    Nuage=Nuage if Nuage else "Selon Valeur"
    if Nuage=="Selon Valeur":
        return  fig147
    else:
        return fig148

@app.callback(
    Output('graph1', 'figure'),
    [Input('Repartition', 'value')]
)
def cb1(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig1
    elif Repartition == "Poids en KG 2020":
        return fig2
    elif Repartition == "Valeur DHS 2019":
        return fig3
    elif Repartition == "Poids en KG 2019":
        return fig4
    elif Repartition == "Valeur DHS 2018":
        return fig5
    elif Repartition == "Poids en KG 2018":
        return fig6
    elif Repartition == "Valeur DHS 2017":
        return fig7
    elif Repartition == "Poids en KG 2017":
        return fig8
    elif Repartition == "Valeur DHS 2016":
        return fig9
    elif Repartition == "Poids en KG 2016":
        return fig10
    elif Repartition == "Valeur DHS 2015":
        return fig11
    elif Repartition == "Poids en KG 2015":
        return fig12
    elif Repartition == "Valeur DHS 2014":
        return fig13
    else:
        return fig14


@app.callback(
    Output('graph2', 'figure'),
    [Input('Repartition', 'value')]
)
def cb2(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig15
    elif Repartition == "Poids en KG 2020":
        return fig16
    elif Repartition == "Valeur DHS 2019":
        return fig17
    elif Repartition == "Poids en KG 2019":
        return fig18
    elif Repartition == "Valeur DHS 2018":
        return fig19
    elif Repartition == "Poids en KG 2018":
        return fig20
    elif Repartition == "Valeur DHS 2017":
        return fig21
    elif Repartition == "Poids en KG 2017":
        return fig22
    elif Repartition == "Valeur DHS 2016":
        return fig23
    elif Repartition == "Poids en KG 2016":
        return fig24
    elif Repartition == "Valeur DHS 2015":
        return fig25
    elif Repartition == "Poids en KG 2015":
        return fig26
    elif Repartition == "Valeur DHS 2014":
        return fig27
    else:
        return fig28


@app.callback(
    Output('graph3', 'figure'),
    [Input('Repartition', 'value')]
)
def cb3(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig29
    elif Repartition == "Poids en KG 2020":
        return fig30
    elif Repartition == "Valeur DHS 2019":
        return fig31
    elif Repartition == "Poids en KG 2019":
        return fig32
    elif Repartition == "Valeur DHS 2018":
        return fig33
    elif Repartition == "Poids en KG 2018":
        return fig34
    elif Repartition == "Valeur DHS 2017":
        return fig35
    elif Repartition == "Poids en KG 2017":
        return fig36
    elif Repartition == "Valeur DHS 2016":
        return fig37
    elif Repartition == "Poids en KG 2016":
        return fig38
    elif Repartition == "Valeur DHS 2015":
        return fig39
    elif Repartition == "Poids en KG 2015":
        return fig40
    elif Repartition == "Valeur DHS 2014":
        return fig41
    else:
        return fig42


@app.callback(
    Output('graph4', 'figure'),
    [Input('Repartition', 'value')]
)
def cb4(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig43
    elif Repartition == "Poids en KG 2020":
        return fig44
    elif Repartition == "Valeur DHS 2019":
        return fig45
    elif Repartition == "Poids en KG 2019":
        return fig46
    elif Repartition == "Valeur DHS 2018":
        return fig47
    elif Repartition == "Poids en KG 2018":
        return fig48
    elif Repartition == "Valeur DHS 2017":
        return fig49
    elif Repartition == "Poids en KG 2017":
        return fig50
    elif Repartition == "Valeur DHS 2016":
        return fig51
    elif Repartition == "Poids en KG 2016":
        return fig52
    elif Repartition == "Valeur DHS 2015":
        return fig53
    elif Repartition == "Poids en KG 2015":
        return fig54
    elif Repartition == "Valeur DHS 2014":
        return fig55
    else:
        return fig56


@app.callback(
    Output('graph5', 'figure'),
    [Input('Repartition', 'value')]
)
def cb5(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig57
    elif Repartition == "Poids en KG 2020":
        return fig58
    elif Repartition == "Valeur DHS 2019":
        return fig59
    elif Repartition == "Poids en KG 2019":
        return fig60
    elif Repartition == "Valeur DHS 2018":
        return fig61
    elif Repartition == "Poids en KG 2018":
        return fig62
    elif Repartition == "Valeur DHS 2017":
        return fig63
    elif Repartition == "Poids en KG 2017":
        return fig64
    elif Repartition == "Valeur DHS 2016":
        return fig65
    elif Repartition == "Poids en KG 2016":
        return fig66
    elif Repartition == "Valeur DHS 2015":
        return fig67
    elif Repartition == "Poids en KG 2015":
        return fig68
    elif Repartition == "Valeur DHS 2014":
        return fig69
    else:
        return fig70


@app.callback(
    Output('graph6', 'figure'),
    [Input('Repartition', 'value')]
)
def cb6(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig71
    elif Repartition == "Poids en KG 2020":
        return fig72
    elif Repartition == "Valeur DHS 2019":
        return fig73
    elif Repartition == "Poids en KG 2019":
        return fig74
    elif Repartition == "Valeur DHS 2018":
        return fig75
    elif Repartition == "Poids en KG 2018":
        return fig76
    elif Repartition == "Valeur DHS 2017":
        return fig77
    elif Repartition == "Poids en KG 2017":
        return fig78
    elif Repartition == "Valeur DHS 2016":
        return fig79
    elif Repartition == "Poids en KG 2016":
        return fig80
    elif Repartition == "Valeur DHS 2015":
        return fig81
    elif Repartition == "Poids en KG 2015":
        return fig82
    elif Repartition == "Valeur DHS 2014":
        return fig83
    else:
        return fig84


@app.callback(
    Output('graph7', 'figure'),
    [Input('Repartition', 'value')]
)
def cb7(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig85
    elif Repartition == "Poids en KG 2020":
        return fig86
    elif Repartition == "Valeur DHS 2019":
        return fig87
    elif Repartition == "Poids en KG 2019":
        return fig88
    elif Repartition == "Valeur DHS 2018":
        return fig89
    elif Repartition == "Poids en KG 2018":
        return fig90
    elif Repartition == "Valeur DHS 2017":
        return fig91
    elif Repartition == "Poids en KG 2017":
        return fig92
    elif Repartition == "Valeur DHS 2016":
        return fig93
    elif Repartition == "Poids en KG 2016":
        return fig94
    elif Repartition == "Valeur DHS 2015":
        return fig95
    elif Repartition == "Poids en KG 2015":
        return fig96
    elif Repartition == "Valeur DHS 2014":
        return fig97
    else:
        return fig98


@app.callback(
    Output('graph8', 'figure'),
    [Input('Repartition', 'value')]
)
def cb8(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig99
    elif Repartition == "Poids en KG 2020":
        return fig100
    elif Repartition == "Valeur DHS 2019":
        return fig101
    elif Repartition == "Poids en KG 2019":
        return fig102
    elif Repartition == "Valeur DHS 2018":
        return fig103
    elif Repartition == "Poids en KG 2018":
        return fig104
    elif Repartition == "Valeur DHS 2017":
        return fig105
    elif Repartition == "Poids en KG 2017":
        return fig106
    elif Repartition == "Valeur DHS 2016":
        return fig107
    elif Repartition == "Poids en KG 2016":
        return fig108
    elif Repartition == "Valeur DHS 2015":
        return fig109
    elif Repartition == "Poids en KG 2015":
        return fig110
    elif Repartition == "Valeur DHS 2014":
        return fig111
    else:
        return fig112


@app.callback(
    Output('graph9', 'figure'),
    [Input('Repartition', 'value')]
)
def cb9(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig113
    elif Repartition == "Poids en KG 2020":
        return fig114
    elif Repartition == "Valeur DHS 2019":
        return fig115
    elif Repartition == "Poids en KG 2019":
        return fig116
    elif Repartition == "Valeur DHS 2018":
        return fig117
    elif Repartition == "Poids en KG 2018":
        return fig118
    elif Repartition == "Valeur DHS 2017":
        return fig119
    elif Repartition == "Poids en KG 2017":
        return fig120
    elif Repartition == "Valeur DHS 2016":
        return fig121
    elif Repartition == "Poids en KG 2016":
        return fig122
    elif Repartition == "Valeur DHS 2015":
        return fig123
    elif Repartition == "Poids en KG 2015":
        return fig124
    elif Repartition == "Valeur DHS 2014":
        return fig125
    else:
        return fig126


@app.callback(
    Output('graph10', 'figure'),
    [Input('Repartition', 'value')]
)
def cb10(Repartition):
    Repartition = Repartition if Repartition else "Valeur DHS 2020"
    if Repartition == "Valeur DHS 2020":
        return fig127
    elif Repartition == "Poids en KG 2020":
        return fig128
    elif Repartition == "Valeur DHS 2019":
        return fig129
    elif Repartition == "Poids en KG 2019":
        return fig130
    elif Repartition == "Valeur DHS 2018":
        return fig131
    elif Repartition == "Poids en KG 2018":
        return fig132
    elif Repartition == "Valeur DHS 2017":
        return fig133
    elif Repartition == "Poids en KG 2017":
        return fig134
    elif Repartition == "Valeur DHS 2016":
        return fig135
    elif Repartition == "Poids en KG 2016":
        return fig136
    elif Repartition == "Valeur DHS 2015":
        return fig137
    elif Repartition == "Poids en KG 2015":
        return fig138
    elif Repartition == "Valeur DHS 2014":
        return fig139
    else:
        return fig140
@app.callback(
    Output('graph21', 'figure'),
    [Input('Cartegeo', 'value')]
)
def cb21(Cartegeo):
    Cartegeo=Cartegeo if Cartegeo else "Valeur DHS 2020"
    if Cartegeo=="Valeur DHS 2020":
        return  figc1
    else:
        return figc2



if __name__ == '__main__':
    app.run_server(debug=True)

