# template
a generic starting point for new projects  
includes logging and a path dictionary  

startup sequence  
1. constant.paths builds the paths dictionary  
2. user configuration is loaded from setting.settings.yaml into a dict  
3. the script.initialize configures the logger according to the dict  
