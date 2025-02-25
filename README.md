## Excess Chemical Potential of Hydrophobes in Water  
Here is a simple method to implement test particle insertion (TPI) to estimate excess chemical potential. The cross interactions for hydrophobes in TIP4P/2005 are taken from "J. Phys. Chem. B 2020, 124, 6924−6942." Bulk water consisting of 266 water molecules was first equilibrated at constant pressure and constant temperature, then the TPI method was applied to 1001 snapshots sampled from the production stage. Considering having sampling enough, the number of insertions was set to 50,000 times, adding up to almost 50 million calculations for each solute.  
  
Considering the number of snapshots and the number of insertions, in this code, I used parallelized computing of energy difference generated from inserting a virtual atom randomly. I also have automized this approach using bash script, "config". By executing config, you can achieve excess chemical potentials of your interest system.  

## Results
