# Hate Detector

Group project for [Hack the North 2019](https://hackthenorth.com). 

Team members: 
- [Wais Shahbaz](https://github.com/wshahbaz)
- [Jack Lu](https://github.com/Jacklu0831)
- [Sunanda Gamage](https://github.com/sgamage2)
- [Eric Luo](https://github.com/2017soft)

## About

## Background

## Resources

## Azure deployment instructions


Login to Azure shell and execute the following commands

az configure --defaults group=sgamage2_rg_Linux_centralus



az webapp config set --resource-group sgamage2_rg_Linux_centralus --name hate-detector --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 --chdir backend hello:backend"