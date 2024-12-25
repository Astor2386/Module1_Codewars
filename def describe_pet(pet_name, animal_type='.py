def make_shirt(size= 'large',message= 'I love Python.'):
    """Summarize the shirt size and 
    message."""
    
    print("The shirt size is " + size + 
" and it has '" + message + "' printed on it.")

# Make a large shirt with the default message
make_shirt()
    
#make a medium shirt with the default message
make_shirt(size = 'medium')

#Make a shirt of any size (small here) with a different message
make_shirt('small', 'Python will be my greatest challenge.')