from typing import List, Tuple

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
# Write a program that reads this file as a stream and returns the top 3 candidates at any given time. 
# If you find a voter voting more than once, report this as fraud.

def top_candidates(votes: List[Tuple]) -> int:
    """
    Given a list of tuples representing votes cast,
    Return the top three candidates, repr by a distinct candidate_id.
    Prints all malformed votes.
    """
    # list of ballot voters counted
    voted = []

    # dict of candidates and their counted votes
    count = {x[1]:0 for x in votes}

    # for each ballot, count it for the candidate
    # and add the voter to the voter roll
    for ballot in votes:
        if ballot[1] in count:
            count[ballot[1]] += 1
        voted.append(ballot[0])
    
    # Report double votes
    for voter in voted:
        n = voted.count(voter)
        if n > 1:
            print(f"ERROR: VOTER ID {voter} CAST {n} BALLOTS")

    # Sort dict count by the highest value
    sorted_candidates = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
    return(list(sorted_candidates.keys())[0:3])

if __name__ == "__main__":
    votes = [(1, 1), (2, 1), (3, 2), (4, 3), (5, 2), (6, 1), (7, 1), (8, 3)]
    print(top_candidates(votes)) # [1, 2, 3] (votes were {1:4, 2:2, 3:2})

    mal_votes = [(1, 2), (2, 1), (3, 3), (4, 3), (5, 2), (1, 2), (6, 1), (7, 1), (8, 3), (9,3), (10,4)] # voter 1 votes for 2 twice
    print(top_candidates(mal_votes)) # [2, 1, 3] (votes were {1:3, 2:3, 3:4, 4:1})
                                     # ERROR: VOTER ID 1 CAST 2 BALLOTS (x2)