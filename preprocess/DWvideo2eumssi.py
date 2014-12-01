#!/usr/bin/env python

import datetime
import json
from eumssi_converter import EumssiConverter

<<<<<<< HEAD
def transf_date(x):
    return datetime.datetime.utcfromtimestamp(json.loads(x)['$date']/1000) #convert from timestamp in milliseconds

def transf_lang(x):
    return x #TODO: probably need to maps "spanish"->"es", etc.
=======

def transf_date(x):
    '''convert from string in DD.MM.YYYY (or YYYY-MM-DD) format'''
    try:
        return datetime.datetime.strptime(x, "%d.%m.%Y")
    except ValueError:
        try:
            return datetime.datetime.strptime(x, "%Y-%m-%d")
        except ValueError:
            return "invalid date format"


def transf_lang(x):
    '''normalize language codes to ISO 639-1'''
    lang_map = {
        'german': 'de',
        'english': 'en',
        'spanish': 'es',
        'french': 'fr'  # doesn't actually appear in the data
    }
    return lang_map.get(x, x)
>>>>>>> upstream/master

'''
mapping in the form [<original_fieldname>, <eumssi_fieldname>, <transform_function>, [<available_data>,..]}
'''
dw_video_map = [
<<<<<<< HEAD
    ['publicationDate', 'datePublished', transf_date, []],
    ['language', 'inLanguage', transf_lang, []],
    ['httpHigh', 'httpHigh', None, ['video']],
    ['httpMedium', 'httpMedium', None, ['video']],
    ['tags','keywords',None,[]],
    ['title','headline',None,['text']]
=======
    ['dateText', 'datePublished', transf_date, []],
    ['language', 'inLanguage', transf_lang, []],
    ['httpHigh', 'httpHigh', None, ['video']],
    ['httpMedium', 'httpMedium', None, ['video']],
    ['tags', 'keywords', None, []],
    ['title', 'headline', None, ['text']]
>>>>>>> upstream/master
]


def main():
<<<<<<< HEAD
  conv = EumssiConverter('DW-video',dw_video_map)
  conv.run()

if __name__ == '__main__':
  main()
=======
    conv = EumssiConverter('DW-video', dw_video_map)
    conv.run()

if __name__ == '__main__':
    main()
>>>>>>> upstream/master
