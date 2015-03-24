import csv

years = ["1955", "1959", "1963", "1968", "1972", "1980", "1984", "1988", "1991", "1997", "2001", "2006", "2011"]

with open("results_by_party.csv", "w") as csvfile:
  fieldNames = ["year", "AI", "BS", "CP", "DP", "DPP", "INDP", "JPS", "KURA", "LP", "LSP", "NSP", "PAP", "PF", "PKMS", "PMIP", "PP", "PRSSD", "RP", "SA", "SC", "SDA", "SDP", "SJP", "SLF", "SPA", "SPP", "SUF", "UF", "UNF", "UDP", "UPF", "UPP", "WP"]
  w = csv.DictWriter(csvfile, fieldNames)
  w.writeheader()

  def writerows(year):
    w.writerow({'year': year})

  def countVotes(year):
    with open("result_" + year + ".csv", "rb") as f:
      result = csv.reader(f, delimiter=',', quotechar='|')
      for row in result:
        party = row[1]
        vote = row[3]

        if party != "party":
          # w.writerow({'year': year, party: sum()})
          

  for x in years:
    writerows(x)