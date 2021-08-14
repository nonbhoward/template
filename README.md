## template
a generic starting point for new projects  
this project could be used in many ways,  
but the two recommended approaches are :

1. fork this project, program directly into it
2. use built-in soft-link deployment, described below


#### startup sequence
*( $ python ./script/initialize.py )*
1. ./common/paths creates relative path object
2. ./configure/settings creates the application configuration from ./setting/settings  
3. ./script/initialize configures the logger

#### soft-link deployment
*( see ./setting/deployment.yaml for more information )*  
this project will create soft-links in parallel  
projects containing the deployment.yaml manifest.  
the soft-links created depend on the manifest configuration  

#### known bugs
1. logging does not work as expected  
