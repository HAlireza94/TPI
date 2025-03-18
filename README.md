# Excess Chemical Potential of Hydrophobes in Water  
Here is a simple method to implement test particle insertion (TPI) to estimate excess chemical potential. The cross interactions for hydrophobes in TIP4P/2005 are taken from "J. Phys. Chem. B 2020, 124, 6924−6942." Bulk water consisting of 266 water molecules was first equilibrated at constant pressure and constant temperature, then the TPI method was applied to 1001 snapshots sampled from the production stage. Considering having sampling enough, the number of insertions was set to 50,000 times, adding up to almost 50 million calculations for each solute.  
  
Considering the number of snapshots and the number of insertions, in this code, I used parallelized computing of energy difference generated from inserting a virtual atom randomly. I also have automized this approach using bash script, "config". By executing config, you can achieve excess chemical potentials of your interest system.  

## Results
Here the results for the noble gas group where you can see the calculated excess chemical potential using the test particle insertion method. As can be seen, we are in a good agreement with the experimental data.
<img width="561" alt="Image" src="https://github.com/user-attachments/assets/8fb058a5-7f95-49a6-8e98-2904939b0f0a" />



# Excess Chemical Potential of CO2 and H2S in Water  
The release of carbon dioxide from fossil fuel combustion is a significant contributor to global warming. This concern has led to increasing interest in capturing and storing CO₂ from post-combustion and oxy-fuel combustion processes. Effective separation process design and optimization rely on a thorough understanding of the thermodynamic properties of phase equilibria. In the same token, H2S also plays a hazardous role in upstream and downstream industries, where efforts have been taken to address challenges related to H2S removal over the past years. Desining an efficient separation, often using liquid-liquid extraction (LLE), requires to have a deep understanding of the mechanism through which H2S dissolves in the solvent. Given this, the question arises: how can we expect to design an effective LLE process without sufficient molecular-level understanding of the solubility of these gases in a basic solvent such as water? Current united force fields appear to suffer delivering an accurate description of the thermodynamic properties of these gases, especially solubility. In this side project, I tried to optimize the cross-interactions between CO2/H2S + Water. The Lennard - Jones parameters for CO2 and H2S are taken from ref [1-2]. To benchmark against experimental data, thermodynamic data is used from Solvation Thermodynamics[3].



## Results
To assess the performance of the current molecular parameters the excess chemical potentials of these gases in two water models, including TIP4P/2005[4] and TIP4P-epsilon[5], are calculated over 50,000 sampled frames from pure solvents by inserting 10,000 times each solute per frame. The estimated uncertainty is computed using blocking average. As can be seen from Fig 1, There are some key findings to take as follows:  
- Both become more insoluble by increasing temperature.
- Over the entire temperature range, H2S is more soluble than CO2.
- Close to the critical temperature of CO2, employed cross interactions still represent CO2 is soluble in water.
- Comparing the results at the ambient temperature and atmospheric pressure, the excess chemical potentials of CO2 and H2S are both underestimated.
- The excess chemical potentials of CO2 and H2S in TIP4P/2005 and TIP4P-epsilon show almost the same, no wonder that in this test particle insertion, I did not first take into account the dissociation of CO2 in water. Besides, for united atoms, electrostatic interactions are not considered. This means electrostatic interactions play a great role in accurately describing the solubulity. Because of this, free energy calculations using Thermodynamic integration is recommended to study the effect of applying a water model that has a more realistic dielectric constant.

To optimize cross interactions at 298.15 K and 1 atm, I used the following approach[6]:  
<img width="482" alt="Image" src="https://github.com/user-attachments/assets/c3e9ca86-f124-41a7-9be4-d47491b74ff4" />


The obtained results are shown in Fig 2. According to this approach, it seems that the optimum **&chi;** value is +0.021 and -0.039 for CO2 and H2S, respectively.



#### Figure 1- Calculated excess chemical potential of CO2 and H2S as a function of temperature in two different water models, TIP4P/2005 and TIP4P-epsilon.
<img width="1005" alt="Image" src="https://github.com/user-attachments/assets/46aac0aa-4bee-4205-a784-b95e72b93b76" />


  
#### Figure 2- Calculated excess chemical potential of CO2 and H2S as a function of **&chi;**.
<img width="1085" alt="Image" src="https://github.com/user-attachments/assets/e2ac6359-8da6-4d14-b995-f9d1176b8ec3" />




### References:
[1] https://pubs.acs.org/doi/10.1021/jp204908d  
[2] https://doi.org/10.1016/j.fluid.2016.08.002  
[3] https://link.springer.com/book/10.1007/978-1-4757-6550-2  
[4] https://doi.org/10.1063/1.2121687  
[5] https://pubs.acs.org/doi/10.1021/jp410865y

