# Component Specification

 - Name
	 -`SunnyScraper`  
 - What it does:
	 -Gets weather data
 - Inputs (with type information)
	 -The code? 
 - Outputs (with type information)
	 -Data from weather site
	 
 - Name
	 -`SunnyWriter`  
 - What it does:
	 -Turns weather data into something comprehensible and makes a text
 - Inputs (with type information)
	 -Weather data from `SunnyScraper`
 - Outputs (with type information)
	 -Data from weather site

 - Name
	 -`SunnyTexter`  
 - What it does:
	 -Texts user
 - Inputs (with type information)
	 -User contact and `SunnyWriter` prompt
 - Outputs (with type information)
	 -Data from weather site
	 
 - Name
	 -`SunnyDatabase`  
 - What it does:
	 -Contains names, phone numbers, location info of useres
 - Inputs (with type information)
	 -Info from user
 - Outputs (with type information)
	 -Info to SunnyScraper and SunnyWriter



	 

