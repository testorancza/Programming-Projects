import numpy as np
from matplotlib import pyplot as plt

''' You’re part of an impartial research group that conducts phone surveys prior to local elections. 
During this election season, the group conducted a survey to determine how many people would vote for Cynthia Ceballos vs. Justin Kerrigan 
in the mayoral election.Now that the election has occurred, your group wants to compare the survey responses to the actual results.'''

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = survey_responses.count("Ceballos")
print(total_ceballos)

survey_responses_array = np.array(survey_responses)

percentage_ceballos = np.mean(survey_responses_array == "Ceballos")
print(percentage_ceballos)

""" 
In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos. 
Your supervisors are concerned because this is a very different outcome than what the poll predicted. 
They want you to determine if there is something wrong with the poll or if given the sample size, it was an entirely reasonable result.
Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town’s population as its parameters. 
Then divide the distribution by the number of survey responses. Save your calculation to the variable possible_surveys."""

binomial = np.random.binomial(70, 0.54, size = 10000)
possible_surveys = binomial / 70.

plt.hist(possible_surveys, bins = 20 , range = (0,1))
plt.show()

""" As we saw, 47% of people we surveyed said they would vote for Ceballos, but 54% of people voted for Ceballos in the actual election.
Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote and save it to the variable ceballos_loss_surveys."""

ceballos_loss_surveys = np.mean(possible_surveys < .5)

print(ceballos_loss_surveys)

""" With this current poll, about 20% of the time a survey output would predict Kerrigan winning, even if Ceballos won the actual election.
Your co-worker points out that your poll would be more accurate if it had more responders.
Generate another binomial distribution, but this time, see what would happen if you had instead surveyed 7,000 people. 
Divide the distribution by the size of the survey and save your findings to large_survey."""

binomial2 = np.random.binomial(7000, 0.54, size = 10000)
large_survey = binomial2 / 7000.

ceballos_loss_new = np.mean(large_survey < .5)
print(ceballos_loss_new)