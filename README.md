# Excess Chemical Potential of Hydrophobes in Water  
Here is a simple method to implement test particle insertion (TPI) to estimate excess chemical potential. The cross interactions for hydrophobes in TIP4P/2005 are taken from "J. Phys. Chem. B 2020, 124, 6924−6942." Bulk water consisting of 266 water molecules was first equilibrated at constant pressure and constant temperature, then the TPI method was applied to 1001 snapshots sampled from the production stage. Considering having sampling enough, the number of insertions was set to 50,000 times, adding up to almost 50 million calculations for each solute.  
  
Considering the number of snapshots and the number of insertions, in this code, I used parallelized computing of energy difference generated from inserting a virtual atom randomly. I also have automized this approach using bash script, "config". By executing config, you can achieve excess chemical potentials of your interest system.  

## Results
Here the results for the noble gas group where you can see the calculated excess chemical potential using the test particle insertion method. As can be seen, we are in a good agreement with the experimental data.
<img width="561" alt="Image" src="https://github.com/user-attachments/assets/8fb058a5-7f95-49a6-8e98-2904939b0f0a" />



# Excess Chemical Potential of CO2 and H2S in Water  
The release of carbon dioxide from fossil fuel combustion is a significant contributor to global warming. This concern has led to increasing interest in capturing and storing CO₂ from post-combustion and oxy-fuel combustion processes. Effective separation process design and optimization rely on a thorough understanding of the thermodynamic properties of phase equilibria. In the same token, H2S also plays a hazardous role in upstream and downstream industries, where efforts have been taken to address challenges related to H2S removal over the past years. Desining an efficient separation, often using liquid-liquid extraction (LLE), requires to have a deep understanding of the mechanism through which H2S dissolves in the solvent. Given this, the question arises: how can we expect to design an effective LLE process without sufficient molecular-level understanding of the solubility of these gases in a basic solvent such as water? Current united force fields appear to suffer delivering an accurate description of the thermodynamic properties of these gases, especially solubility. In this side project, I tried to optimize the cross-interactions between CO2/H2S + Water. The Lennard - Jones parameters for CO2 and H2S are taken from ref [1-2]. To benchmark against experimental data, thermodynamic data is used from Solvation Thermodynamics[3].



## Results
Recently, I focused on optimizing two important gases in the world, CO2 and H2S. I started calculating excess chemical potential as a function of temperature in TIP4P/2005 water model, and then I tried to optimize the cross interactions at the ambient temperature and atmospheric pressure, where I could show that my results are describing efficiently the solubility of these gases at those conditions I mentioned, compared to the experimental data. Also, this is an ongoing – side project I started.







#### Figure 1- Calculated excess chemical potential of CO2 and H2S as a function of temperature in two different water models, TIP4P/2005 and TIP4P-epsilon.
<img width="1005" alt="Image" src="https://github.com/user-attachments/assets/46aac0aa-4bee-4205-a784-b95e72b93b76" />


#### Figure 2- Calculated excess chemical potential of CO2 and H2S as a function of chai.
<img width="1085" alt="Image" src="https://github.com/user-attachments/assets/e2ac6359-8da6-4d14-b995-f9d1176b8ec3" />




### References:
[1] https://pubs.acs.org/doi/10.1021/jp204908d  
[2] https://doi.org/10.1016/j.fluid.2016.08.002
[3] https://link.springer.com/book/10.1007/978-1-4757-6550-2
[4] https://doi.org/10.1063/1.2121687
[5] https://pubs.acs.org/doi/10.1021/jp410865y

