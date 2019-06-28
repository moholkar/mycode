#!/usr/bin/python3


import yaml

def main():
    hitchhikers = [{'name': 'Zaphod Beeblebrox', 'species' : 'Betelgeusian'}, {'name': 'Arthur Dent' , 'Sepcies' : 'Human'}]

    print(hitchhikers)

    zfile = open('galaxyguide.yaml','w')

    yaml.dump(hitchhikers,zfile) 

    zfile.close()

main()


