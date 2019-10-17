#!/usr/bin/python -tt

# from: http://www.techgaun.com/2012/03/extracting-all-hyperlinks-from-webpages.html

import re
import sys
import urllib2

def main():
  ''' Usage: url_extractor.py "http://example.com/"
      NOTICE: Intended for root urls; ie no */file or /subfolder/*
      In that case you need to edit this file first
      './abc', '/abc' will be translated to
      'http://example.com/abc' (../ not translated)
      Return value: list
  '''
  if (len(sys.argv) != 2):
    print 'Usage: ./web-scraping.py http://www.example.com/'
    return []
  else:
    url = str(sys.argv[1])  

  links_regex = re.compile('<a\s+.*href=[\'"]?([^\'" >]+)', re.IGNORECASE)
  print(links_regex.pattern)


  url_request = urllib2.Request(url)
  try:
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.43 Safari/536.11')]
    response = opener.open(url)
    html = response.read()

    links = links_regex.findall(html)

    fixed_links = []
    i = 0
    for link in links:
      full_url = re.sub(r'^\.?/{1,2}', url, link, count=1)
      if len(full_url) > 7 and full_url != "javascript:void(0)":
        if (full_url not in fixed_links) and full_url.find(':'):
            print(f'i = {i:03}')
            fixed_links.append(str(i).zfill(1) + ' ' + full_url)

    fixed_links.sort()
    print()
    print (len(fixed_links))
    #print(fixed_links[0:15])

    print '\n'.join(fixed_links)

  except urllib2.URLError:
    print 'Can\'t Connect to the website'

if __name__ == '__main__':
  sys.exit(main())