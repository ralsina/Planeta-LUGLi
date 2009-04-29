#!/bin/sh

# Script para regenerar planeta LUGLi
cd ~/Planeta-LUGLi

# Regenerar la configuración
python merge-config.py

# Bajar los feeds
rawdog -d . -u

# Regenerar planeta full
LANG=es_ES rawdog -d ~/Planeta-LUGLi -c config-full -w

# Subir a github
git commit -a
git push origin master 
