# test.py:  test plugin for Bywaf

print "loaded Test plugin"

# required dictionary
options = {
  # <name>    <value>    <default value>   <required>  <description>
  "SLEEP_SECONDS": ("", "10", "Yes", "Number of seconds to sleep"),
  "FILENAME": ("", "", "No", "Name of the file to display")  
  }


def do_sleepfunction(line):
    """sleep for a few seconds"""

    # use current value, defaulting to the default value if no current
    # value has been defined.
    try:
        seconds = int(options['SLEEP_SECONDS'][0])
    except:
        seconds = int(options['SLEEP_SECONDS'][1]) 

    # sleep for the given period of seconds    
    print('Sleeping for {} seconds....'.format(seconds))
    import time
    time.sleep(seconds)
    
    # return value that is displayed upon command completion
    return "this is the return value after having slept {} seconds.".format(seconds)


def do_cat(line):
    """display contents of a file"""
    
    # if user did not supply an argument at command-line, then 
    # check to see if user specified an option
    fnames = line
    
    if not line:
        
        if options['FILENAME'][0]:
            fnames = options['FILENAME'][0]
        else:
            fnames = options['FILENAME'][1]

    # assume user gave argument at the wafterpreter command line.  
    # Note, this assumes that filenames do not contain spaces.
    fnames = line.split()
    
    # complain if the user did not supply a filename
    if not fname:
        print("cat: must specify a filename on the command line or in 'filename' option")
        return

    # iterate over filenames and display contents of each
    for fn in fnames:
        try:
            print(_cat(fn))
        except IOError as e:
            print('Could not load file "{}": {}', fn, e)
            
# Completion function for cat():     
def complete_cat(text,line,begin_idx,end_idx):
    return app.filename_completer(text, line, begin_idx, end_idx)

# Read a file and return its contents.
def cat(fn):
    with open(fn) as f:
        contents = f.read()
    return contents
    
def do_choice(line):
    """Select a subcommand"""
    print('this is another command')
    
def complete_choice(text,line,begin_idx,end_idx):
   option_names = ['foo', 'bar', 'baz']

   opts = [x for x in option_names if x.startswith(text)]
   return opts                                     
