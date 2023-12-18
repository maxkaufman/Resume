# M012-Project2-Group10

This program returns the total happiness generated using different methods based on three different cafeterias

<h1> Using the exploreOnly, exploitOnly and eGreedy files </h1>
<h3> The exploitOnly file returns the total happiness for 300 days where for the first 3 days each cafeteria is visited and the best one is visited for the remaining 297 days </h3>

<p> When the exploitOnly file is run, a random happiness is generated for the first three days for each cafeteria based on the mean and standard deviation given. Then the cafeteria that generated the highest happiness is found and picked for the next 297 days. The happiness is calculated for each of the 297 days and added to the happiness found for the first three days. The total happiness is finally returned. </p>

<h3> The exploreOnly file returns the total happiness for 300 days where each cafeteria is visited equally </h3>

<p> When the exploreOnly file is run, a random happiness is generated for each cafeteria 100 times each. Each happiness is added to the totalhappiness which is returned. </p>

<h3> The eGreedy file functions similarly to exploitOnly but for the remaining 297 days, an input value e is used to randomly choose whether you visit the best cafeteria or one of the other ones. </h3>

<p> First, the happiness is found for the first three days at each cafeteria. Next, e is used to determine whether you will go to a random cafeteria or go to the best cafeteria. e% of the time you will randomly pick a cafeteria while 100-e% of the time you will go to the best cafeteria. For whichever cafeteria is randomly chosen, the happiness is calculated based on the normal distribution of that cafeteria. The total happiness is returned. </p>

<h1> Using the simulation file </h1>
<h3> The simulation file runs each of the previous files for t number of trials and will print certain information </h3>

<p> When the simulation file is run, it will take a number t as input for the number of trials to run. Then it will print the optimum happiness, expected total happiness and regret, average total happiness, and average regret for each function previously explained in t trials. </p>
