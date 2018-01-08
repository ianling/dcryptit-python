from .exceptions import (DcryptItException, ConnectionError, HTTPError, APIError)
import requests
from json import loads as json_loads

def read_dlc(path=None, url=None):
    """
        Parameters:
            -path: the file path to the DLC file.
            -url: the URL to the DLC file.
        Returns a list of the links the DLC file contains.
        Otherwise, an exception is raised.
    """
    DCRYPTIT_UPLOAD_URL = 'http://dcrypt.it/decrypt/upload'
    DCRYPTIT_LINK_URL = 'http://dcrypt.it/decrypt/container'
    try:
        if path:
            files = {'dlcfile': open(path, 'rb') }
            response = requests.post(DCRYPTIT_UPLOAD_URL, files=files)
        elif url:
            data = {'link': url}
            response = requests.post(DCRYPTIT_LINK_URL, data=data)
        else:
            raise RuntimeError('No path or URL to DLC file provided')
    except requests.exceptions.RequestException:
        raise ConnectionError('Failed to connect to dcrypt.it')
    try:
        response.raise_for_status()
        response = response.text.replace('<textarea>', '').replace('</textarea>', '')
        response = json_loads(response)['success']['links']
        return response
    except requests.exceptions.HTTPError:
        raise HTTPError('The request to dcrypt.it returned an error')
    except ValueError, KeyError:
        raise APIError('dcrypt.it returned an error, or an invalid JSON response')
    except:
        raise DcryptItException('An unknown error occurred while parsing the response')
