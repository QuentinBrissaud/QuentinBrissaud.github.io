#!/usr/bin/env python3
from pdb import set_trace as bp
from scholarly import scholarly
import pandas as pd

def modify_author(input, name, max_author):

    input_split = input.split(' and ')
    input = input_split[:max_author]
    idx   = input_split.index(name)
    if idx > 2:
        if idx > 3:
            input += ['...']
        input += [name]
    
    if idx < len(input_split)-1:
        input += ['et al']
        
    input[input.index(name)] = '**' + name + '**'
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

    list_conf = ['AGU', 'EGU', 'ESSOAR'] # should be uppercase
    tests     = ['journal', 'publisher']
    type = 'journal'
    for test in tests:
        if test in bib.keys():
            for conf in list_conf:
                if conf in bib[test].upper():
                    type = 'conference'
    
    return type

def get_one_entry(name, pub, keys_publications):
    
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

def collect_all_studies(name, database=''):

    if database:
        studies = pd.read_csv(database, sep='|', header=[0])
    else:
        database = './database_publications.csv'
        studies  = pd.DataFrame()
        
    ## Publication information to save
    keys_publications = ['type', 'title', 'pub_year', 'author', 'volume', 'number', 'pages', 'journal', 'publisher', 'abstract']

    ## Retrieve the author's data, fill-in
    search_query = scholarly.search_author(name)
    author = scholarly.fill(next(search_query))

    ## Retrieve all publication data
    any_change = False
    for pub in author['publications']:
    
        if studies.size > 0:
            if pub['bib']['title'] in studies['title'].values:
                continue
                
        any_change = True
        new_entry = get_one_entry(name, pub, keys_publications)
        studies = studies.append( [new_entry] )
        
    studies['title_upper'] = studies['title'].astype(str).str.upper()
    studies.drop_duplicates(subset=['title_upper'], inplace=True)
    studies.sort_values(by='pub_year', ascending=False, inplace=True)
    studies.reset_index(drop=True, inplace=True)
    
    if any_change:
        studies.to_csv(database, sep='|', header=True, index=False)
    
    return studies

def process_one_study(study, name, max_author, istudy):
    
    keys_int = ['pub_year', 'volume', 'number']
    dict_study = study.to_dict()
    dict_study['no'] = istudy
    dict_study['author'] = modify_author(dict_study['author'], name, max_author)
    for key in dict_study:
        if dict_study[key] == 'N/A':
            dict_study[key] = ''
        if key in keys_int:
            if dict_study[key]:
                dict_study[key] = int(dict_study[key])
            
    return dict_study

def write_md_studies(studies, name, format_md, max_author=3):
    
    studies = studies.fillna('')
    grouped = studies.groupby('type')
    with open(options['output'], 'w') as md_file:
        
        for type, group in grouped:
        
            md_file.write(type.capitalize() + '\n')
            md_file.write('=====\n\n')
            group.reset_index(drop=True, inplace=True)
            for istudy, study in group.iterrows():
                
                dict_study = process_one_study(study, name, max_author, istudy)
                line   = format_md['base'].format(**dict_study)
                if dict_study['volume']:
                    line += format_md['volume'].format(**dict_study)
                line += '\n'
                md_file.write(line)

options = {}
options['format']   = {
    'base': '{no}. {author}. ({pub_year}) [{title}]({url}). *{journal}*',
    'volume': ', {number}({volume}):{pages}',
    }
options['database'] = ''#'./database_publications.csv'
options['name']     = 'Quentin Brissaud'
options['output']   = './publications.md'
studies  = collect_all_studies(options['name'], options['database'])
write_md_studies(studies, options['name'], options['format'])

bp()