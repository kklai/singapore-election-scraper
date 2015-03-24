#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import urllib, os
import string
import csv

years = ["1955", "1959", "1963", "1968", "1972", "1980", "1984", "1988", "1991", "1997", "2001", "2006", "2011"]

def extract(year):
    with open("result_" + year + ".csv", "w") as csvfile:
      fieldNames = ["district", "party", "candidates", "candidates_count", "votes", "pct_votes"]

      w = csv.DictWriter(csvfile, fieldNames)

      w.writeheader()
      
      mech = Browser()
      if year == "2011":
          url = "http://www.eld.gov.sg/elections_results2011.html"
      else:
          url = "http://www.eld.gov.sg/elections_past_parliamentary" + year + ".html"
      
      page = mech.open(url)
      html = page.read()
      soup = BeautifulSoup(html)

      data = soup.findAll("div", style="display:table-row; width:auto; clear:both;")

      for row in data:
          col = row.findAll("div", {"class": "byContent"})
          
          district = col[0].text

          candidates = col[1].findAll("div")
          candidates_count = len(candidates)

          party = col[2].findAll("a")

          total_votes = col[3].findAll("div")

          total_votes_pct = col[4].findAll("div")


          if (len(party) > 1):
            for x in range(len(party)):
              w.writerow({'district': district.replace(",", ""), 'party': party[x].text.replace(",", ""), 'candidates': candidates[x].text.replace(",", ""), 'candidates_count': candidates_count, 'votes': total_votes[x].text.replace(",", ""),'pct_votes': total_votes_pct[x].text.replace(",", "") })
          elif (total_votes[0].text == "Uncontested"):
            w.writerow({'district': district.replace(",", ""), 'party': party[0].text.replace(",", ""), 'candidates': candidates[0].text.replace(",", ""), 'candidates_count': candidates_count, 'votes': total_votes[0].text.replace(",", ""),'pct_votes': 0})

for x in years:
    extract(x)