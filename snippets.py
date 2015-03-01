import logging
#set the log output file, and the log level
logging.basicConfig(filename="snippets.log",level=logging.DEBUG)

#Stubs - a function that is defoned but does nothing useful
def put(name, snippet):
    """
    Store a snippet with an associated name.
    Returns the name and snippet
    """
    logging.error("FIXME: Unimplemented - put ({!r}, {!r})".format(name,snippet))
    return name, snippet

def get(name):
    """
    Retrieve the snippet with a given name. 
    If there is no such snippet provide error message and ask user if they would like to create the snippet
    Returns the snippet.
    """
    logging.erro("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
