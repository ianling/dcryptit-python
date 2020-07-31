# dcryptit
A python3 library for interacting with http://dcrypt.it, a website for decrypting DLC files.

A legacy python2.x version can be found under the 1.0 tag, or the python2 branch.

# Example Usage

There are two ways to use dcryptit.

1. Upload a DLC file.
2. Submit a URL to a DLC file.

Both ways return a list of the links that were in the DLC file.

    import dcryptit
    
    dlc_path = '/home/ianling/links.dlc'
    links = dcryptit.read_dlc(file=dlc_path)
    
    dlc_url = 'https://mywebsite.com/links.dlc'
    links = dcryptit.read_dlc(url=dlc_url)
