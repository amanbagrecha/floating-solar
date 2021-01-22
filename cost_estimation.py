def cost_estimation(cost_panel=[29,32], solar_power_output= 459, panel_type=335, mean_sun_light_hour=8.825):
	"""
	estimate the cost of setting up solar panels for given estimated output from floating
	solar photovoltaics. The unit of solar power output is in MW; unit of panel type is watts; 
	mean sun light hours is the average annual sun light for the city of bangalore.
	cost of panel is in Rupee ***(lower_bound, upper_bound)***

	-- aim --
	1. To find number of panels of given panel_type.
	2. To estimate the cost of setting up all of the panels. 

	**NOTE**
	The estimated cost is of the sonal panel alone, and does not include installation cost, workmanship.

	"""

	# solar power output in kwh
	solar_power_output_kwh = solar_power_output*365*24*1000

	# number of panels
	no_of_panels= solar_power_output_kwh/(365*panel_type*mean_sun_light_hour)


	# cost of setting up all panels in rupees
	lower_limit_cost = round(no_of_panels * panel_type * cost_panel[0], 0)
	upper_limit_cost = round(no_of_panels * panel_type * cost_panel[1], 0)
	return (lower_limit_cost,upper_limit_cost)

print(cost_estimation())