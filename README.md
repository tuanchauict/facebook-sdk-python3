facebook-sdk-python3
===================

I did not write a new facebook sdk, I just fixed something for [facebook-sdk](https://github.com/pythonforfacebook/facebook-sdk) which helps you run `facebook-sdk` in `Python3`

#Example:
  	
  	import facebook3 as fb

	token = fb.get_app_access_token('your_app_id', 'your_app_secret')
	graph = fb.GraphAPI(token)
	graph.get_object('/me')


#License:
This library uses the [Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html). Please see the library's individual files for more information.


#Note: 
I don't know how to create setup.py. So, you can copy [facebook3.py](https://github.com/tuanchauict/faceboo-sdk-python3/blob/master/facebook3.py) to your project or put it into `site-packages` folder

