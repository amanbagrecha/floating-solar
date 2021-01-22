# floating-solar
calculations for estimating evaporation losses, energy output, cost estimation

## Energy Yield Assessment
PVWatts, an estimation tool developed by the national laboratory of the U.S Department of Energy was used in assessing the energy output. It estimates the annual energy yield based on the monthly average values of global solar radiation on a horizontal surface. The open-source software was synchronized with the Indian database and validation studies show an annual deviation ranging between -4% to -6% (Psomopoulos et al., 2015). The study considered, fixed solar modules having a nominal efficiency of 15%,and an area coverage ratio of 0.5 to 0.6.  Figure 8 shows the expected mean monthly solar output. Naturally, high output is witnessed during summer months and reduced output during the monsoon season. The analysis showed an average of 459MW of power from 3954 acres of the lake area. Amongst the 32 lakes considered, 7 lakes produced more than 25MW and 9 lakes have capacity lesser than 5MW. On an average 8.5 acres of land is needed to generate 1MW of power. Notably, Bettakote Lake located adjacent to the city’s airport has a capacity of 13MW, which can compensate at an average 65% of the demand and contribute to the existing rooftop solar capacity of 8.35MW enabling complete sustainable functioning of the airport (Philip, 2018). Compared to the total demand of the city, the lakes collectively can generate an average of 26% of the power to be supplied. The monthly variation of percentage of solar power of the demand is depicted in Figure 9. These values have been obtained from total monthly output of AC energy (kWh/month) across all water bodies considered. 

## Estimation of Evaporation losses
Water preservation and evaporation reduction occur due to the installation of floating solar systems on lakes, dams, irrigation ponds and reservoirs. The area covered by FSPV will result in the reduction of evaporation over the lakes. Evaporation loss has been studied over lakes using Mayer’s empirical formula given by Equation below (Subramanya, 2013).

<img src="https://latex.codecogs.com/svg.latex?\Large&space;E_l=K_M*(e_w-e_a)*(1+u_9/16)" title="\Large E_l=K_M*(e_w-e_a)*(1+u_9/16)" />

Where,
- EL (mm/day) is the lake evaporation
- ew (mmHg) saturated vapour pressure at the water surface temperature
- ea (mmHg) actual vapour pressure of overlying air at a specified height
- u9 (km/h) monthly mean wind velocity in about 9 m above ground
- KM coefficient accounting for various other factors with a value of 0.36

Actual vapour pressure and mean monthly temperature was obtained from India Meteorological Data for evaluating the depth of lake water evaporation per day. Wind velocity was obtained from WeatherOnline © portal by averaging annual wind velocity for a time frame of 20 years from 2000-2019.
Saturated vapor Pressure was calculated using Antoine Equation given by Equation 2 (Thomson, 1946),

<img src="https://latex.codecogs.com/svg.latex?\Large&space;P=10^{(A-B/(C+T))}" title="\Large P=10^{(A-B/(C+T)))}" />

Where,
- P (mm of mercury (Hg)) is the Saturated vapour Pressure.
- T (Celsius) is the mean temperature.
- A, B, C are Antoine Equation parameters.
Using the above formula, a reduction in evaporation loss is calculated and the final result has been summarised. Since the tilt angle of the panel is nearly zero, the result is approximate over the entire surface area. Annually, 22,866,653 m3 of water would be saved due to a reduction in evaporation calculated over 32 lakes. 


