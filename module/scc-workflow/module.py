#
# Collective Knowledge ()
#
#
#
#
# Developer:
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)

import os

##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# compile application

def compile(i):
    """
    Input:  {
              (data_uoa) - CK entry with artifacts
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Find artifact

    r=find_artifact(i)
    if r['return']>0: return  r

    duoa=r['data_uoa']

    ck.out('')
    ck.out('TBD')


    return {'return':0}

##############################################################################
# run application

def run(i):
    """
    Input:  {
              (data_uoa) - CK entry with artifacts
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    r=find_artifact(i)
    if r['return']>0: return r

    duoa=r['data_uoa']

    ck.out('')
    ck.out('TBD')


    return {'return':0}

##############################################################################
# test workflow

def test(i):
    """
    Input:  {
              (data_uoa) - CK entry with artifacts
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    r=find_artifact(i)
    if r['return']>0: return r

    duoa=r['data_uoa']

    ck.out('')
    ck.out('TBD')


    return {'return':0}

##############################################################################
# plot graphs

def plot(i):
    """
    Input:  {
              (data_uoa) - CK entry with artifacts
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    r=find_artifact(i)
    if r['return']>0: return r

    duoa=r['data_uoa']

    ck.out('')
    ck.out('TBD')


    return {'return':0}

##############################################################################
# prepare SCC workflow

def prepare(i):
    """
    Input:  {
              (data_uoa) - if the entry name to customize workflow is set,
                           use it instead of year/team below
                 or
              (data)

              (repo)     - CK repo to be created (it will keep user artifacts)

              (year) - /string/ competition year
              (team) - /string/ team number 
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    # If entry name is forced by a user
    duoa=i.get('data_uoa','')
    if duoa=='':
       duoa=i.get('data','')

    # Check forced repo
    repo=i.get('repo','')

    tags=[] # tags to find artifacts

    if duoa=='':
       # Check year
       year=i.get('year','')

       if year=='':
          ck.out('')
          r=ck.inp({'text':'Please enter the year of the competition: '})
          if r['return']>0: return r

          year=r['string'].strip()

       # Check team
       team=i.get('team','')

       if team=='':
          ck.out('')
          r=ck.inp({'text':'Please enter your team number: '})
          if r['return']>0: return r

          team=r['string'].strip()

       # prepare entry name to keep artifacts
       duoa=year+'-'+team

       tags=['scc-'+year, 'team-'+team]

       if repo=='':
          repo='scc-'+year+'-'+team

    # If repo is not defined above ask
    if repo=='':
       ck.out('')
       r=ck.inp({'text':'Please enter a new name of the CK repo to keep your artifacts: '})
       if r['return']>0: return r

       repo=r['string'].strip()

    # Checking if CK repo already exists
    ck.out('')
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['repo'],
                 'data_uoa':repo})
    if r['return']!=0 and r['return']!=16: return r
    if r['return']==0:
       return {'return':1, 'error':'CK repo "'+repo+'" already exists'}

    # Creating repo
    ck.out('Creating CK repo "'+repo+'" ...')

    r=ck.access({'action':'add',
                 'module_uoa':cfg['module_deps']['repo'],
                 'data_uoa':repo,
                 'repo_deps': [{"repo_uoa": "ck-scc", "repo_url":"https://github.com/reproindex/ck-scc"}],
                 'out':'',
                 'quiet':'yes'})
    if r['return']>0: return r

    # Check where created
    r=ck.access({'action':'where',
                 'module_uoa':cfg['module_deps']['repo'],
                 'data_uoa':repo,
                 'out':''})
    if r['return']>0: return r

    p=r['path']

    ck.out('')
    ck.out('Repository was successfully created in '+p)



    ck.out('')
    ck.out('Creating SCC workflow entry "'+duoa+'" to keep you artifacts ...')

    ck.out('')
    ii={'action':'copy',
        'module_uoa':work['self_module_uid'],
        'data_uoa':'template',
        'new_repo_uoa':repo,
        'new_data_uoa':duoa,
        'out':o}

    if len(tags)>0:
       ii['dict']={'tags':tags}

    r=ck.access(ii)
    if r['return']>0: return r

    pa=r['path'] # artifacts

    ck.out('')
    ck.out('Please go to directory "'+pa+'" to prepare your Digital Artifact')

    ck.out('')
    ck.out('You can pack it via "ck pack scc-workflow:'+duoa+'" when ready!')

    return {'return':0}

##############################################################################
# find artifact entry

def find_artifact(i):

    o=i.get('out','')

    duoa=i.get('data_uoa','')

    # Checking how many artifacts exist
    r=ck.access({'action':'search',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r

    lst1=r['lst']
    lst=[]

    # Prune template
    for q in lst1:
        if q.get('data_uoa','')!='template':
           lst.append(q)

    # Select
    if len(lst)==0:
       return {'return':1, 'error':'no SCC workflows found. Please use "ck prepare scc-workflow"'}
    elif len(lst)==1:
       duoa=lst[0]['data_uoa']
    else:
       ck.out('')
       ck.out('Select SCC workflow:')
       ck.out('')

       r=ck.select_uoa({'choices':lst})
       if r['return']>0: return r
       duoa=r['choice']

    # Get path
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']

    ck.out('')
    ck.out('SCC digital artifact directory: '+p)

    os.chdir(p)

    return {'return':0, 'data_uoa':duoa, 'path':p}

##############################################################################
# pack your Digital Artifact

def pack(i):
    """
    Input:  {
              (data_uoa) - pack this digital artifact

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    duoa=i.get('data_uoa','')
    if duoa=='':
       return {'return':1, 'error':'please specify the CK entry with your Digital artifact (for example "ck pack scc-workflow:2019-6")'}

    ii={'action':'find',
        'module_uoa':work['self_module_uid'],
        'data_uoa':duoa}
    r=ck.access(ii)
    if r['return']>0: return r

    p=r['path']

    ck.out('Packing Digital Artifact from '+p+' ...')

    filename='scc-'+duoa+'.zip'

    # Prepare archive
    import zipfile

    zip_method=zipfile.ZIP_DEFLATED

    r=ck.list_all_files({'path':p})
    if r['return']>0: return r

    fl=r['list']

    # Write archive
    try:
       f=open(filename, 'wb')
       z=zipfile.ZipFile(f, 'w', zip_method)
       for fn in fl:
           p1=os.path.join(p, fn)
           z.write(p1, fn, zip_method)
       z.close()
       f.close()

    except Exception as e:
       return {'return':1, 'error':'failed to pack your Digital Artiact ('+format(e)+')'}

    ck.out('')
    ck.out('Digital Artifact Archive: '+filename)

    return {'return':0}
