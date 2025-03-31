#!/usr/bin/env python3
from pdb import set_trace as bp
from scholarly import scholarly
import pandas as pd

def modify_author(input, names, max_author):

    last_name = names.split(' ')[-1]

    input_split = input.split(' and ')
    input = input_split[:max_author]
    
    """
    idx = []
    for name in last_name:
        for iname, name_ in enumerate(input_split):
            if name in name_:
                idx.append( iname )
    bp()
    idx = idx[0]
    """
    #try:
    idx   = [iname for iname, name_ in enumerate(input_split) if last_name in name_]
    if len(idx) == 0:
        return None
    idx = idx[0] #input_split.index(name)
    name_right_format = input_split[idx]
        
    if idx > 2:
        if idx > 3:
            input += ['...']
        input += [name_right_format]
    
    if idx < len(input_split)-1:
        input += ['et al']
        
    input[input.index(name_right_format)] = '**' + names + '**'
    if len(input) > 1:
        input_ = ', '.join(input[:-1])
    else:
        input_ = input[0]
    if 'et al' in input:
        input_ += ', et al'
    elif len(input) > 1:
        input_ += ', and ' + input[-1]
    
    return input_

def modify_type(new_entry, bib):

    list_conf = ['AGU', 'EGU', 'ESSOAR', 'MEETING'] # should be uppercase
    tests     = ['journal', 'publisher']
    type = 'journal'
    for test in tests:
        if test in bib.keys():
            for conf in list_conf:
                if conf in bib[test].upper():
                    type = 'conference'
    
    return type

def get_one_entry(pub, keys_publications):
    
    publication_full = scholarly.fill(pub)
    new_entry = {}
    for key in keys_publications:
        if key == 'type':
            new_entry[key] = modify_type(new_entry, publication_full['bib'])
            
        else:
            if key in publication_full['bib'].keys():
            
                input = publication_full['bib'][key]
                #if key == 'author':
                #    input = modify_author(input, name, max_author)
                    
                new_entry[key] = input
            else:
                new_entry[key] = 'N/A'
    
    new_entry['url'] = pub['pub_url']
    
    return new_entry

def collect_all_studies(names, database='', remove_by_hand=[]):

    if database:
        studies = pd.read_csv(database, sep='|', header=[0])
    else:
        database = './database_publications.csv'
        studies  = pd.DataFrame()
        
    ## Publication information to save
    keys_publications = ['type', 'title', 'pub_year', 'author', 'volume', 'number', 'pages', 'journal', 'publisher', 'abstract']

    ## Retrieve the author's data, fill-in
    search_query = scholarly.search_author(names)
    author = scholarly.fill(next(search_query))

    ## Retrieve all publication data
    any_change = False
    for pub in author['publications']:
    
        if remove_by_hand:
            found = False
            for entry in remove_by_hand:
                for key in entry:
                    #print('- ', entry[key], pub['bib']['title'])
                    if entry[key] in pub['bib']['title']:
                        found = True
            if found:
                continue
                        
        if studies.size > 0:
            if pub['bib']['title'] in studies['title'].values:
                continue
                
        any_change = True
        new_entry = get_one_entry(pub, keys_publications)
        studies = studies.append( [new_entry] )
        
    studies['title_upper'] = studies['title'].astype(str).str.upper()
    studies.drop_duplicates(subset=['title_upper'], inplace=True)
    studies = studies.loc[~(studies.pub_year=='N/A')]
    studies.sort_values(by='pub_year', ascending=False, inplace=True)
    studies.reset_index(drop=True, inplace=True)
    
    if any_change:
        studies.to_csv(database, sep='|', header=True, index=False)
    
    return studies

def process_one_study(study, name, max_author, istudy):
    
    keys_int = ['pub_year', 'volume', 'number']
    dict_study = study.to_dict()
    dict_study['no'] = istudy
    try:
        dict_study['author'] = modify_author(dict_study['author'], name, max_author)
    except:
        dict_study['author'] = modify_author(dict_study['author'], 'Quentin Brissaud', max_author)

    if dict_study['author'] is None:
        return None

    for key in dict_study:
        if dict_study[key] == 'N/A':
            dict_study[key] = ''
        if key in keys_int:
            if dict_study[key]:
                ## Some conference volumes have letters in it (e.g., EGU21-1224)
                try:
                    dict_study[key] = int(dict_study[key])
                except:
                    pass
                    
    return dict_study

def write_md_studies(studies, name, format_md, max_author=3):
    
    studies = studies.fillna('')
    grouped = studies.groupby('type')
    with open(options['output'], 'w') as md_file:
        
        list_of_groups = [(type, group) for type, group in grouped]
        for type, group in list_of_groups[::-1]:
        
            md_file.write(type.capitalize() + '\n')
            md_file.write('=====\n\n')
            group.reset_index(drop=True, inplace=True)
            for istudy, study in group.iterrows():
                
                dict_study = process_one_study(study, name, max_author, istudy)
                if dict_study is None:
                    continue
                line   = format_md['base'].format(**dict_study)
                if dict_study['volume']:
                    line += format_md['volume'].format(**dict_study)
                line += '\n'
                md_file.write(line)

            line = '\n'
            md_file.write(line)

def add_specific_studies(studies, add_by_hand):

    columns = studies.columns
    for study in add_by_hand:
        for column in columns:
            if not column in study:
                study[column] == 'N/A'
        studies = studies.append( [study] )
    
    studies.reset_index(inplace=True, drop=True)
    studies.sort_values(inplace=True, by='pub_year', ascending=False)
    
    return studies

options = {}
options['format']   = {
    'base': '{no}. {author}. ({pub_year}) [{title}]({url}). *{journal}*',
    'volume': ', {number}({volume}):{pages}',
    }
options['database'] = ''#'./database_publications.csv'
options['name']     = 'Quentin Brissaud'
options['output']   = './publications.md'

## Manual entries
options['add_by_hand'] = []
#options['remove_by_hand'] = [{'title': 'Predicting infrasound transmission loss using deep learning'},]
options['remove_by_hand'] = [{'title': 'Supporting Information for Parsimonious velocity inversion applied to the Los Angeles Basin, CA'},]

entry = {
    'type': 'conference', 'title': 'Balloons as geophysical probes', 'pub_year': 2021, 'author': 'Quentin Brissaud and Siddharth Krishnamoorthy and Jennifer M Jackson and Daniel C Bowman and Attila Komjathy and James A Cutts and Zhongwen Zhan and Michael T Pauken and Jacob S Izraelevitz and Gerald J Walsh', 'volume': 'N/A', 'number': 'N/A', 'pages': 'N/A', 'journal': 'Invited presentation at GeoAzur', 'publisher': '', 'abstract': '', 'url': 'https://geoazur.oca.eu/fr/agenda-geoazur', 'title_upper': '',
}
entry['title_upper'] = entry['title'].upper()
options['add_by_hand'].append( entry )

entry = {
    'type': 'conference', 'title': 'Detection and properties of local artillery infrasound', 'pub_year': 2021, 'author': 'Quentin Brissaud and Tormod Kværna and Kamran Iranpour and Tina Kaschwich and Idar Dyrdal', 'volume': 'N/A', 'number': 'N/A', 'pages': 'N/A', 'journal': 'CTBT Science and Technology Conference 2021 (SnT2021)', 'publisher': '', 'abstract': '', 'url': 'https://conferences.ctbto.org/event/7/book-of-abstracts.pdf', 'title_upper': '',
}
entry['title_upper'] = entry['title'].upper()
options['add_by_hand'].append( entry )

entry = {
    'type': 'conference', 'title': 'Listening to earthquakes from the clouds', 'pub_year': 2022, 'author': 'Quentin Brissaud', 'volume': 'N/A', 'number': 'N/A', 'pages': 'N/A', 'journal': 'Chinese Academy of Science', 'publisher': '', 'abstract': '', 'url': 'http://www.epp.ac.cn/activityView.asp?NewsId=857', 'title_upper': '',
}
entry['title_upper'] = entry['title'].upper()
options['add_by_hand'].append( entry )

entry = {
    'type': 'journal', 'title': '', 'pub_year': 2023, 'author': 'Quentin Brissaud and Antoine Turquet and Celso Alvizuri and Sven Peter Nasholm and Alexis Le Pichon and Johan Kero', 'volume': '', 'number': '', 'pages': '', 'journal': 'Geophysical Research Letters (in review)', 'publisher': '', 'abstract': '', 'url': '', 'title_upper': '',
}
entry['title_upper'] = entry['title'].upper()
options['add_by_hand'].append( entry )

"""
entry = {
    'type': 'journal', 'title': 'Predicting infrasound transmission loss using deep learning', 'pub_year': 2022, 'author': 'Quentin Brissaud and Sven Peter Nasholm and Antoine Turquet and Alexis Le Pichon', 'volume': '232', 'number': '1', 'pages': '274–286', 'journal': 'Geophysical Journal International', 'publisher': '', 'abstract': '', 'url': 'https://doi.org/10.1093/gji/ggac307', 'title_upper': '',
}
entry['title_upper'] = entry['title'].upper()
options['add_by_hand'].append( entry )


entry = {
    'type': 'journal', 'title': 'Near-real-time detection of co-seismic ionospheric disturbances using machine learning', 'pub_year': 2021, 'author': 'Quentin Brissaud and Elvira Astafyeva', 'volume': 'N/A', 'number': 'N/A', 'pages': 'N/A', 'journal': 'Geophysical Journal International - Express letter (in review)', 'publisher': '', 'abstract': '', 'url': '', 'title_upper': '',
}
entry['title_upper'] = entry['title'].upper()
options['add_by_hand'].append( entry )


entry = {
    'type': 'journal', 'title': 'Parsimonious velocity inversion applied to the Los Angeles Basin, CA', 'pub_year': 2021, 'author': 'Jack B Muir and Robert Clayton and Victor C Tsai and Quentin Brissaud', 'volume': 'N/A', 'number': 'N/A', 'pages': 'N/A', 'journal': 'Geophysical Journal International (in review)', 'publisher': '', 'abstract': '', 'url': 'https://doi.org/10.31223/X5F03K', 'title_upper': '',
}
entry['title_upper'] = entry['title'].upper()
options['add_by_hand'].append( entry )
"""
## Fetch and build reference list
studies = collect_all_studies(options['name'], options['database'], options['remove_by_hand'])
studies = add_specific_studies(studies, options['add_by_hand'])
write_md_studies(studies, options['name'], options['format'])

bp()
