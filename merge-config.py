# -*- coding: utf-8 -*-
# Este script toma los feeds de python de feeds-python, los full de feeds-full
# la config de config-base y genera config, config-python y config-full
# para hacer que rawdog pueda generar dos "pseudoplanetas"

config=open('config-base').read()
fullurls=[]
pythonurls=[]

for linea in open('feeds-full'):
    config+=linea
    if linea.startswith("feed "):
        url=' '.join(linea.split(' ')[2:]).strip()
        if url: fullurls.append(url)
    
#for linea in open('feeds-python'):
#    config+=linea
#    if linea.startswith("feed "):
#        url=' '.join(linea.split(' ')[2:]).strip()
#        if url: pythonurls.append(url)

# Configuracion para generar planeta full
open ("config-full","w").write("""
template template-full
outputxml           /srv/www/lugli/index.xml 
outputfoaf          /srv/www/lugli/foafroll.xml
outputopml          /srv/www/lugli/feeds.opml
xmltitle            Planeta LUGLi
xmllink           http://lugli.netmanagers.com.ar/
xmllanguage       es
xmlurl            http://lugli.netmanagers.com.ar/index.xml
xmldescription    Miembros del LUGLi
xmlownername      Roberto Alsina
xmlowneremail     ralsina@netmanagers.com.ar
outputfile /srv/www/lugli/index.html
selectfeeds %s
"""%' '.join(fullurls))

# Configuracion para generar planeta solo python
#open ("config-python","w").write("""
#template template-python
#outputxml           /srv/www/pyar/python.xml
#outputfoaf          /srv/www/pyar/foafroll-python.xml
#outputopml          /srv/www/pyar/feeds-python.opml
#xmltitle            Planeta PyAr (Python)
#xmllink           http://planeta.python.org.ar/python.html
#xmllanguage       es
#xmlurl            http://planeta.python.org.ar/python.xml
#xmldescription    Miembros de Python Argentina
#xmlownername      Roberto Alsina
#xmlowneremail     ralsina@netmanagers.com.ar
#outputfile        /srv/www/pyar/python.html
#selectfeeds %s
#"""%' '.join(pythonurls))

open ("config","w").write(config)
