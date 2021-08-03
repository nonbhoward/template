# template
a generic starting point for new projects  
includes logging and a path dictionary  

startup sequence  
1. common.paths builds the paths dictionary  
	access via script.initialize.path  
2. user configuration is loaded from setting.settings.yaml into a dict  
	access via script.initialize.config  
3. the script.initialize configures the logger according to config['logger']  

