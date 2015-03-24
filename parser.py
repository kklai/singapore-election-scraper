import csv

years = ["1959", "1963", "1968", "1972", "1980", "1984", "1988", "1991", "1997", "2001", "2006", "2011"]

with open("results_by_seats.csv", "w") as csvfile:
  fieldNames = ["year", "PAP", "SPP", "WP", "Others"]
  w = csv.DictWriter(csvfile, fieldNames)
  w.writeheader()

  def countVotes(year):
    with open("result_" + year + ".csv", "rb") as f:
      result = csv.reader(f, delimiter=',', quotechar='|')

      pap_vote = 0
      spp_vote = 0
      wp_vote = 0
      others = 0

      findWinner = []


      for idx, row in enumerate(result):
        if idx == 1:
          currentDistrict = row[0].split("(")[0]

        if row[1] != "party":
          district = row[0].split("(")[0]
          if currentDistrict == district:
            findWinner.append([district, row[1], row[4], row[3]])
          else:
            # print(findWinner)
            if len(findWinner) == 1:
              winner = row[1]
              winner_count = 1
            else:
              votes = []
              for x in findWinner:
                votes.append(int(float(x[2])))
              winner = findWinner[votes.index(max(votes))][1]
              winner_count = int(findWinner[votes.index(max(votes))][3])

            if winner == "PAP":
              pap_vote += winner_count
            elif winner == "SPP":
              spp_vote += winner_count
            elif winner == "WP":
              wp_vote += winner_count
            else:
              others += winner_count

            findWinner = []
            currentDistrict = district
            findWinner.append([district, row[1], row[4], row[3]])

      w.writerow({'year': year, "PAP": pap_vote, "SPP": spp_vote, "WP": wp_vote, "Others": others})
          

          


      #   party = row[1]
      #   vote = row[3]


      #   if vote != "Uncontested" and vote != "votes":
      #     if party == "PAP":
      #       pap_vote += int(float(vote))
      #     elif party == "SPP":
      #       spp_vote += int(float(vote))
      #     elif party == "WP":
      #       wp_vote += int(float(vote))
      #     else:
      #       others += int(float(vote))

      # w.writerow({'year': year, "PAP": pap_vote, "SPP": spp_vote, "WP": wp_vote, "Others": others})
            

  for x in years:
    countVotes(x)